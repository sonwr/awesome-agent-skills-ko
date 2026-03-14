from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstTwoStepOneScreenBundleTest(unittest.TestCase):
    def test_note_exists_with_validate_then_next_doc_bundle(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'README_INTRO_FIRST_TWO_STEP_ONE_SCREEN_BUNDLE.md').read_text(encoding='utf-8')

        self.assertIn('한 화면 2단계 묶음 / One-screen two-step bundle', readme)
        self.assertIn('python3 templates/scripts/validate_template.py', note)
        self.assertIn('examples/quickstart.md', note)
        self.assertIn('English mirror:', note)


if __name__ == '__main__':
    unittest.main()
