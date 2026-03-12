from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstProgressStatusLineTests(unittest.TestCase):
    def test_readme_mentions_intro_first_progress_status_line(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_PROGRESS_STATUS_LINE.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_PROGRESS_STATUS_LINE.md").exists())


if __name__ == "__main__":
    unittest.main()
