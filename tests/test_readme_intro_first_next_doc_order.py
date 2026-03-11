import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstNextDocOrderTest(unittest.TestCase):
    def test_readme_mentions_intro_first_next_doc_order(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/README_INTRO_FIRST_NEXT_DOC_ORDER.md', readme)
        self.assertTrue((ROOT / 'docs' / 'README_INTRO_FIRST_NEXT_DOC_ORDER.md').exists())
