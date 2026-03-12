from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateDownloadPathTests(unittest.TestCase):
    def test_readme_mentions_intro_first_validate_download_path(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_DOWNLOAD_PATH.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_VALIDATE_DOWNLOAD_PATH.md").exists())


if __name__ == "__main__":
    unittest.main()
