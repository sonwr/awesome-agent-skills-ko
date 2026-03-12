from pathlib import Path
import unittest


class ReadmeIntroFirstNextDocLockTests(unittest.TestCase):
    def test_readme_mentions_intro_first_next_doc_lock(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_NEXT_DOC_LOCK.md", readme)
        self.assertIn("다음 문서 handoff", readme)


if __name__ == "__main__":
    unittest.main()
