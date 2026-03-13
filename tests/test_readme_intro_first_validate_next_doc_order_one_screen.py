from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateNextDocOrderOneScreenTests(unittest.TestCase):
    def test_readme_mentions_intro_first_validate_next_doc_order_one_screen(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_ORDER_ONE_SCREEN.md', readme)
        self.assertTrue((ROOT / 'docs' / 'README_INTRO_FIRST_VALIDATE_NEXT_DOC_ORDER_ONE_SCREEN.md').exists())


if __name__ == '__main__':
    unittest.main()
