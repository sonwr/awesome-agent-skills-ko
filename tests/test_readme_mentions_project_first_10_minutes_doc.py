from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeMentionsProjectFirst10MinutesDocTests(unittest.TestCase):
    def test_readme_mentions_project_first_10_minutes_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_PROJECT_FIRST_10_MINUTES.md", readme)
        self.assertTrue((ROOT / "docs" / "README_PROJECT_FIRST_10_MINUTES.md").exists())


if __name__ == "__main__":
    unittest.main()
