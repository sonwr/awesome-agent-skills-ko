from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstOneScreenPromiseTests(unittest.TestCase):
    def test_readme_mentions_one_screen_promise(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("첫 화면 원스크린 약속 / First-screen one-screen promise", readme)
        self.assertIn("audience -> first validation command -> next doc", readme)


if __name__ == "__main__":
    unittest.main()
