from pathlib import Path
import unittest


class ReadmeFirstScreenThreeLineStarterCardTests(unittest.TestCase):
    def test_readme_mentions_first_screen_three_line_starter_card(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/README_FIRST_SCREEN_THREE_LINE_STARTER_CARD.md", readme)
        note = (root / "docs" / "README_FIRST_SCREEN_THREE_LINE_STARTER_CARD.md").read_text(encoding="utf-8")
        self.assertIn("소개 1줄", note)
        self.assertIn("첫 행동+다음 문서", note)


if __name__ == "__main__":
    unittest.main()
