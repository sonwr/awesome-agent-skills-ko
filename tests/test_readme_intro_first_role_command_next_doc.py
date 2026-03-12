from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstRoleCommandNextDocTests(unittest.TestCase):
    def test_readme_mentions_intro_first_role_command_next_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_ROLE_COMMAND_NEXT_DOC.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_ROLE_COMMAND_NEXT_DOC.md").exists())


if __name__ == "__main__":
    unittest.main()
