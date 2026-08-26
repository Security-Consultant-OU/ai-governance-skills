#!/usr/bin/env python3
"""Validate marketplace skill sources, metadata, references, and archives."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path


ALLOWED_FRONTMATTER_KEYS = {"description", "name"}
FRONTMATTER_PATTERN = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
TOP_LEVEL_KEY_PATTERN = re.compile(r"^([A-Za-z0-9_-]+):(?:\s|$)", re.MULTILINE)
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NIST_ID_PATTERN = re.compile(r"^\|\s*((?:GV|MAP|ME|MG)-\d+\.\d+)\s*\|", re.MULTILINE)
ISO_CONTROL_PATTERN = re.compile(r"^\|\s*(A\.\d+(?:\.\d+){1,2})\s*\|", re.MULTILINE)


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def canonical_markdown(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def parse_frontmatter(skill_file: Path) -> tuple[dict[str, str], str] | None:
    text = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if match is None:
        return None

    frontmatter_text = match.group(1)
    values: dict[str, str] = {}
    lines = frontmatter_text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        key_match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if key_match is None:
            index += 1
            continue
        key = key_match.group(1)
        value = (key_match.group(2) or "").strip()
        if value in {">", "|"}:
            block: list[str] = []
            index += 1
            while index < len(lines) and (not lines[index] or lines[index][0].isspace()):
                block.append(lines[index].strip())
                index += 1
            values[key] = " ".join(part for part in block if part)
            continue
        values[key] = value.strip("\"'")
        index += 1
    return values, text[match.end() :]


def validate_frontmatter(skill_file: Path, root: Path) -> list[str]:
    errors: list[str] = []
    parsed = parse_frontmatter(skill_file)
    display_path = relative(skill_file, root)
    if parsed is None:
        return [f"{display_path}: missing or malformed YAML frontmatter"]

    values, _ = parsed
    frontmatter_text = FRONTMATTER_PATTERN.match(
        skill_file.read_text(encoding="utf-8")
    ).group(1)
    keys = set(TOP_LEVEL_KEY_PATTERN.findall(frontmatter_text))
    for key in sorted(keys - ALLOWED_FRONTMATTER_KEYS):
        errors.append(f"{display_path}: unsupported frontmatter key '{key}'")

    name = values.get("name", "")
    description = values.get("description", "")
    if not name:
        errors.append(f"{display_path}: missing frontmatter name")
    elif not SKILL_NAME_PATTERN.fullmatch(name):
        errors.append(f"{display_path}: invalid skill name '{name}'")
    elif name != skill_file.parent.name:
        errors.append(
            f"{display_path}: skill name '{name}' does not match folder '{skill_file.parent.name}'"
        )
    if not description:
        errors.append(f"{display_path}: missing frontmatter description")
    elif len(description) > 1024:
        errors.append(f"{display_path}: description exceeds 1024 characters")
    elif not description.startswith("Use when "):
        errors.append(f"{display_path}: description must start with 'Use when '")
    return errors


def validate_markdown_links(markdown_file: Path, root: Path) -> list[str]:
    errors: list[str] = []
    text = markdown_file.read_text(encoding="utf-8")
    for match in MARKDOWN_LINK_PATTERN.finditer(text):
        target = match.group(1).split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        target_path = (markdown_file.parent / target).resolve()
        if not target_path.exists():
            errors.append(
                f"{relative(markdown_file, root)}: missing local Markdown reference '{target}'"
            )
    return errors


def validate_reference_discovery(skill_file: Path, root: Path) -> list[str]:
    references = skill_file.parent / "references"
    if not references.is_dir():
        return []
    skill_text = skill_file.read_text(encoding="utf-8")
    return [
        f"{relative(skill_file, root)}: reference is not discoverable from SKILL.md: references/{reference.name}"
        for reference in sorted(references.glob("*.md"))
        if f"references/{reference.name}" not in skill_text
    ]


def validate_archives(skill_files: list[Path], root: Path) -> list[str]:
    output_directory = root / "skills"
    if not output_directory.is_dir():
        return []

    errors: list[str] = []
    expected_archives: set[str] = set()
    for skill_file in skill_files:
        skill_directory = skill_file.parent
        name = skill_directory.name
        archive = output_directory / f"{name}.skill"
        expected_archives.add(archive.name)
        if not archive.is_file():
            errors.append(f"{relative(archive, root)}: missing packed skill archive")
            continue

        expected: dict[str, bytes] = {
            f"{name}/SKILL.md": canonical_markdown(skill_file)
        }
        references = skill_directory / "references"
        if references.is_dir():
            for reference in sorted(references.glob("*.md")):
                expected[f"{name}/references/{reference.name}"] = canonical_markdown(
                    reference
                )

        with zipfile.ZipFile(archive) as packed:
            actual_files = {item for item in packed.namelist() if not item.endswith("/")}
            if actual_files != set(expected):
                errors.append(f"{relative(archive, root)}: archive file list does not match source")
                continue
            for packed_name, source_bytes in expected.items():
                if packed.read(packed_name) != source_bytes:
                    errors.append(
                        f"{relative(archive, root)}: stale packed content for {packed_name}"
                    )

    extra_archives = {
        archive.name for archive in output_directory.glob("*.skill")
    } - expected_archives
    for archive_name in sorted(extra_archives):
        errors.append(f"skills/{archive_name}: archive has no source skill")
    return errors


def validate_plugin_metadata(root: Path) -> list[str]:
    marketplace_file = root / ".claude-plugin" / "marketplace.json"
    if not marketplace_file.is_file():
        return []

    errors: list[str] = []
    marketplace = json.loads(marketplace_file.read_text(encoding="utf-8"))
    entries = {entry["name"]: entry for entry in marketplace.get("plugins", [])}
    plugin_directories = {
        path.name for path in (root / "plugins").iterdir() if path.is_dir()
    }
    if set(entries) != plugin_directories:
        errors.append(
            ".claude-plugin/marketplace.json: plugin names do not match plugins/ directories"
        )

    for name in sorted(plugin_directories & set(entries)):
        plugin_file = root / "plugins" / name / ".claude-plugin" / "plugin.json"
        if not plugin_file.is_file():
            errors.append(f"{relative(plugin_file, root)}: missing plugin metadata")
            continue
        plugin = json.loads(plugin_file.read_text(encoding="utf-8"))
        if plugin.get("name") != name:
            errors.append(f"{relative(plugin_file, root)}: plugin name mismatch")
        if plugin.get("version") != entries[name].get("version"):
            errors.append(f"{relative(plugin_file, root)}: marketplace version mismatch")
    return errors


def validate_catalog_invariants(root: Path) -> list[str]:
    errors: list[str] = []
    nist_references = (
        root / "plugins" / "nist-ai-rmf" / "skills" / "nist-ai-rmf" / "references"
    )
    if nist_references.is_dir():
        ids: list[str] = []
        for function_file in sorted(nist_references.glob("*-function.md")):
            ids.extend(NIST_ID_PATTERN.findall(function_file.read_text(encoding="utf-8")))
        if len(ids) != 72 or len(set(ids)) != 72:
            errors.append(
                "NIST Core invariant failed: expected 72 unique GOVERN/MAP/MEASURE/MANAGE outcomes"
            )

    iso_controls = (
        root
        / "plugins"
        / "iso42001"
        / "skills"
        / "iso42001"
        / "references"
        / "controls-annex-a.md"
    )
    if iso_controls.is_file():
        ids = ISO_CONTROL_PATTERN.findall(iso_controls.read_text(encoding="utf-8"))
        unique_ids = {control_id for control_id in ids if not control_id.endswith(".1")}
        if len(unique_ids) != 38:
            errors.append(
                f"ISO Annex A invariant failed: expected 38 unique selectable controls, found {len(unique_ids)}"
            )
    return errors


def validate(root: Path) -> tuple[list[str], int]:
    skill_files = sorted(root.glob("plugins/*/skills/*/SKILL.md"))
    errors: list[str] = []
    if not skill_files:
        errors.append("No skills found under plugins/*/skills/*/SKILL.md")
        return errors, 0

    for skill_file in skill_files:
        errors.extend(validate_frontmatter(skill_file, root))
        errors.extend(validate_reference_discovery(skill_file, root))
    for markdown_file in sorted(root.glob("plugins/**/*.md")):
        errors.extend(validate_markdown_links(markdown_file, root))
    errors.extend(validate_archives(skill_files, root))
    errors.extend(validate_plugin_metadata(root))
    errors.extend(validate_catalog_invariants(root))
    return errors, len(skill_files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    root = arguments.root.resolve()

    errors, skill_count = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s).")
        return 1

    print(f"Validated {skill_count} skills, references, metadata, catalog invariants, and archives.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
