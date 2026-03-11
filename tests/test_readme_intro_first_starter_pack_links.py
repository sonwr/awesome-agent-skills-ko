from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeIntroFirstStarterPackLinksTests(unittest.TestCase):
    def test_readme_keeps_intro_first_starter_pack_links(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        required_docs = [
            "docs/README_PROJECT_STARTER_PACK.md",
            "docs/README_PROJECT_VALUE_STARTERS.md",
            "docs/README_PROJECT_LANDING_BLUEPRINT.md",
        ]

        for doc in required_docs:
            with self.subTest(doc=doc):
                self.assertIn(doc, readme)
                self.assertTrue((root / doc).exists(), f"missing doc: {doc}")


if __name__ == "__main__":
    unittest.main()
