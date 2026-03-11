from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestReadmeIntroFirstStartOrderNoteTests(unittest.TestCase):
    def test_readme_mentions_readme_intro_first_start_order_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_START_ORDER_NOTE.md", readme)
        self.assertTrue((ROOT / "docs/README_INTRO_FIRST_START_ORDER_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
