from pathlib import Path
import unittest


class ReadmeIntroFirstValidateNextDocCardTests(unittest.TestCase):
    def test_readme_mentions_validate_next_doc_card_near_top(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_CARD.md", readme)
        self.assertTrue((root / "docs" / "README_INTRO_FIRST_VALIDATE_NEXT_DOC_CARD.md").exists())


if __name__ == "__main__":
    unittest.main()
