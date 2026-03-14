from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeIntroFirstOneBreathTrioTests(unittest.TestCase):
    def test_readme_mentions_intro_first_one_breath_trio_doc(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_ONE_BREATH_TRIO.md", readme)
        self.assertTrue((root / "docs" / "README_INTRO_FIRST_ONE_BREATH_TRIO.md").exists())


if __name__ == "__main__":
    unittest.main()
