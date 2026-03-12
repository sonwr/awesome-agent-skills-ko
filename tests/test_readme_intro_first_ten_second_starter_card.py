from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstTenSecondStarterCardTests(unittest.TestCase):
    def test_readme_mentions_ten_second_starter_card(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("첫 화면 10초 스타터 카드 / First-screen 10-second starter card", readme)
        self.assertIn("who this repo is for -> validation command to run now -> next document", readme)


if __name__ == "__main__":
    unittest.main()
