from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateKeepScreenTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = ROOT / "docs" / "README_INTRO_FIRST_VALIDATE_KEEP_SCREEN.md"

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_KEEP_SCREEN.md", readme)
        self.assertTrue(note.exists())


if __name__ == "__main__":
    unittest.main()
