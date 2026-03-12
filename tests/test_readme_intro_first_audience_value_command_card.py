from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstAudienceValueCommandCardTests(unittest.TestCase):
    def test_readme_mentions_intro_first_audience_value_command_card(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_AUDIENCE_VALUE_COMMAND_CARD.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_AUDIENCE_VALUE_COMMAND_CARD.md").exists())


if __name__ == "__main__":
    unittest.main()
