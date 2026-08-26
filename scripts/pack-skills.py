#!/usr/bin/env python3
"""Pack each plugins/*/skills/<name>/ tree into skills/<name>.skill (zip)."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
OUT = ROOT / "skills"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def canonical_markdown(path: Path) -> bytes:
    """Return UTF-8 Markdown with stable LF line endings."""
    text = path.read_text(encoding="utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def write_bytes(zf: zipfile.ZipFile, name: str, content: bytes) -> None:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zf.writestr(info, content)


def write_directory(zf: zipfile.ZipFile, name: str) -> None:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
    info.external_attr = 0o40755 << 16
    zf.writestr(info, b"")


def skill_dirs() -> list[Path]:
    found: list[Path] = []
    for plugin in sorted(PLUGINS.iterdir()):
        skills = plugin / "skills"
        if not skills.is_dir():
            continue
        for skill in sorted(skills.iterdir()):
            if (skill / "SKILL.md").is_file():
                found.append(skill)
    return found


def pack(src: Path) -> Path:
    name = src.name
    dest = OUT / f"{name}.skill"
    OUT.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        write_directory(zf, f"{name}/")
        write_bytes(zf, f"{name}/SKILL.md", canonical_markdown(src / "SKILL.md"))
        refs = src / "references"
        if refs.is_dir():
            write_directory(zf, f"{name}/references/")
            for md in sorted(refs.glob("*.md")):
                write_bytes(zf, f"{name}/references/{md.name}", canonical_markdown(md))
    return dest


def main() -> None:
    packed = [pack(src) for src in skill_dirs()]
    for path in packed:
        print(f"{path.name}\t{path.stat().st_size}")
    print(f"packed {len(packed)} skill archives into {OUT}")


if __name__ == "__main__":
    main()
