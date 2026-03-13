from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValuePathsTests(unittest.TestCase):
    def test_note_exists_with_intro_audience_value_quick_start_signal(self) -> None:
        note = (ROOT / 'docs' / 'README_INTRO_FIRST_VALUE_PATHS.md').read_text(encoding='utf-8')
        self.assertIn('프로젝트 소개', note)
        self.assertIn('quick start', note.lower())


if __name__ == '__main__':
    unittest.main()
