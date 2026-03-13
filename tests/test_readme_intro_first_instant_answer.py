from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstInstantAnswerTests(unittest.TestCase):
    def test_readme_mentions_intro_first_instant_answer_phrase(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("첫 화면 intro-first 즉답 / Intro-first instant answer", readme)
        self.assertIn("누구를 위한 저장소인지 -> 첫 검증 명령 -> 다음 문서", readme)


if __name__ == "__main__":
    unittest.main()
