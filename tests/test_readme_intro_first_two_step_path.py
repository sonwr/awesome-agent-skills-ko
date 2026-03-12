from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstTwoStepPathTests(unittest.TestCase):
    def test_readme_mentions_intro_first_two_step_path(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/README_INTRO_FIRST_TWO_STEP_PATH.md", readme)
        self.assertIn("python3 templates/scripts/validate_template.py` 실행 뒤 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_TWO_STEP_PATH.md").exists())


if __name__ == "__main__":
    unittest.main()
