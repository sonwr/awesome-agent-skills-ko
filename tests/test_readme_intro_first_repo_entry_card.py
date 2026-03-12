from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstRepoEntryCardTests(unittest.TestCase):
    def test_readme_mentions_intro_first_repo_entry_card(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_REPO_ENTRY_CARD.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_REPO_ENTRY_CARD.md").exists())


if __name__ == "__main__":
    unittest.main()
