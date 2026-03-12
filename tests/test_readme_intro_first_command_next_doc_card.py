import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstCommandNextDocCardTest(unittest.TestCase):
    def test_readme_mentions_intro_first_command_next_doc_card(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/README_INTRO_FIRST_COMMAND_NEXT_DOC_CARD.md', readme)
        self.assertTrue((ROOT / 'docs' / 'README_INTRO_FIRST_COMMAND_NEXT_DOC_CARD.md').exists())
