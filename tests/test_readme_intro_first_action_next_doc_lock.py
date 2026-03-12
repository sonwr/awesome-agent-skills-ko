from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstActionNextDocLockTests(unittest.TestCase):
    def test_readme_mentions_intro_first_action_next_doc_lock(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_ACTION_NEXT_DOC_LOCK.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_ACTION_NEXT_DOC_LOCK.md").exists())


if __name__ == "__main__":
    unittest.main()
