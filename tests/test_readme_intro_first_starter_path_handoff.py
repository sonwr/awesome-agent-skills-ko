from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstStarterPathHandoffTests(unittest.TestCase):
    def test_readme_mentions_intro_first_starter_path_handoff(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_STARTER_PATH_HANDOFF.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_STARTER_PATH_HANDOFF.md").exists())


if __name__ == "__main__":
    unittest.main()
