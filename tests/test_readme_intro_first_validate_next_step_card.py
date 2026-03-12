from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateNextStepCardTests(unittest.TestCase):
    def test_readme_mentions_intro_first_validate_next_step_card(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_NEXT_STEP_CARD.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_VALIDATE_NEXT_STEP_CARD.md").exists())


if __name__ == "__main__":
    unittest.main()
