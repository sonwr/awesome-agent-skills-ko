from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateNextDocStatusLineTest(unittest.TestCase):
    def test_note_exists_with_intro_first_three_part_handoff(self) -> None:
        note = (ROOT / "docs" / "README_INTRO_FIRST_VALIDATE_NEXT_DOC_STATUS_LINE.md").read_text(encoding="utf-8")
        self.assertIn("누가 시작하는가 / Who should start", note)
        self.assertIn("첫 검증 명령 / First validation command", note)
        self.assertIn("다음 문서 / Next doc", note)


if __name__ == "__main__":
    unittest.main()
