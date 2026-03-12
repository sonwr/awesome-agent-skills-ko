from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeIntroFirstThreeLineCardTests(unittest.TestCase):
    def test_readme_mentions_intro_first_three_line_card_doc(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_THREE_LINE_CARD.md", readme)
        self.assertTrue((root / "docs" / "README_INTRO_FIRST_THREE_LINE_CARD.md").exists())
