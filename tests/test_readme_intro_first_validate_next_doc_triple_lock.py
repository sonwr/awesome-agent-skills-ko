from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateNextDocTripleLockTests(unittest.TestCase):
    def test_readme_mentions_intro_first_validate_next_doc_triple_lock(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_TRIPLE_LOCK.md", readme)
        self.assertTrue((ROOT / "docs" / "README_INTRO_FIRST_VALIDATE_NEXT_DOC_TRIPLE_LOCK.md").exists())


if __name__ == "__main__":
    unittest.main()
