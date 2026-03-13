from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateTwoStepSignalTest(unittest.TestCase):
    def test_note_exists_with_validate_then_next_doc_signal(self) -> None:
        note = (ROOT / 'docs' / 'README_INTRO_FIRST_VALIDATE_TWO_STEP_SIGNAL.md').read_text(encoding='utf-8')
        self.assertIn('첫 검증 명령 / First validation command', note)
        self.assertIn('다음 문서 / Next doc', note)
        self.assertIn('examples/quickstart.md', note)


if __name__ == '__main__':
    unittest.main()
