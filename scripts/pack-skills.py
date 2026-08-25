#!/usr/bin/env python3
"""Pack each plugins/*/skills/<name>/ tree into skills/<name>.skill (zip)."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
OUT = ROOT / "skills"


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
        zf.writestr(f"{name}/", "")
        zf.write(src / "SKILL.md", f"{name}/SKILL.md")
        refs = src / "references"
        if refs.is_dir():
            zf.writestr(f"{name}/references/", "")
            for md in sorted(refs.glob("*.md")):
                zf.write(md, f"{name}/references/{md.name}")
    return dest


def main() -> None:
    packed = [pack(src) for src in skill_dirs()]
    for path in packed:
        print(f"{path.name}\t{path.stat().st_size}")
    print(f"packed {len(packed)} skill archives into {OUT}")


if __name__ == "__main__":
    main()
