from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeIntroFirstFirstActionLockTests(unittest.TestCase):
    def test_readme_mentions_intro_first_first_action_lock_doc(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_FIRST_ACTION_LOCK.md", readme)
        self.assertTrue((root / "docs" / "README_INTRO_FIRST_FIRST_ACTION_LOCK.md").exists())
