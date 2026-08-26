from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_skills.py"


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--root", str(root)],
        capture_output=True,
        check=False,
        text=True,
    )


def write_minimal_marketplace(root: Path, frontmatter: str) -> None:
    skill = root / "plugins" / "example" / "skills" / "example"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        f"---\n{frontmatter}\n---\n\n# Example\n",
        encoding="utf-8",
    )


class ValidateSkillsTests(unittest.TestCase):
    def test_current_repository_passes_all_marketplace_checks(self) -> None:
        result = run_validator(ROOT)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validated 14 skills", result.stdout)

    def test_rejects_unsupported_frontmatter_keys(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            write_minimal_marketplace(
                root,
                "name: example\ndescription: Use when testing examples.\nversion: 1.0.0",
            )

            result = run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("unsupported frontmatter key 'version'", result.stdout)

    def test_rejects_descriptions_that_do_not_state_when_to_use_the_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            write_minimal_marketplace(
                root,
                "name: example\ndescription: Produces an example report.",
            )

            result = run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("description must start with 'Use when '", result.stdout)

    def test_rejects_missing_local_markdown_references(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            write_minimal_marketplace(
                root,
                "name: example\ndescription: Use when testing examples.",
            )
            skill = root / "plugins" / "example" / "skills" / "example" / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\nRead [missing](references/missing.md).\n",
                encoding="utf-8",
            )

            result = run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing local Markdown reference", result.stdout)


if __name__ == "__main__":
    unittest.main()
