from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstOneLineAudienceValidateNextDocTests(unittest.TestCase):
    def test_readme_mentions_intro_first_one_line_audience_validate_next_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_ONE_LINE_AUDIENCE_VALIDATE_NEXT_DOC.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_ONE_LINE_AUDIENCE_VALIDATE_NEXT_DOC.md").exists())


if __name__ == "__main__":
    unittest.main()
