from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeFirstScreenAudiencePromiseTests(unittest.TestCase):
    def test_readme_mentions_first_screen_audience_promise(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_FIRST_SCREEN_AUDIENCE_PROMISE.md", readme)
        self.assertTrue((ROOT / "docs" / "README_FIRST_SCREEN_AUDIENCE_PROMISE.md").exists())


if __name__ == "__main__":
    unittest.main()
