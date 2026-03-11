from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeProjectQuickstartFlowTests(unittest.TestCase):
    def test_readme_mentions_project_quickstart_flow(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_PROJECT_QUICKSTART_FLOW.md", readme)
        self.assertTrue((ROOT / "docs" / "README_PROJECT_QUICKSTART_FLOW.md").exists())


if __name__ == "__main__":
    unittest.main()
