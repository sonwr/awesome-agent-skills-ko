from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstQuickPromiseTests(unittest.TestCase):
    def test_readme_mentions_first_screen_quick_promise(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("첫 화면 빠른 약속 / First-screen quick promise", readme)
        self.assertIn("who this repo helps -> first validation command -> next doc", readme)


if __name__ == "__main__":
    unittest.main()
