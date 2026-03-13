import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateKeepScreenTests(unittest.TestCase):
    def test_readme_mentions_intro_first_validate_keep_screen(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_KEEP_SCREEN.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_VALIDATE_KEEP_SCREEN.md").exists())


if __name__ == "__main__":
    unittest.main()
