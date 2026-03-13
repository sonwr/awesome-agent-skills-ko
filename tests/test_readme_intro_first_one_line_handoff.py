from pathlib import Path
import unittest

README = Path(__file__).resolve().parents[1] / 'README.md'


class ReadmeIntroFirstOneLineHandoffTests(unittest.TestCase):
    def test_readme_mentions_one_line_handoff_doc(self) -> None:
        text = README.read_text(encoding='utf-8')
        self.assertIn('docs/README_INTRO_FIRST_ONE_LINE_HANDOFF.md', text)


if __name__ == '__main__':
    unittest.main()
