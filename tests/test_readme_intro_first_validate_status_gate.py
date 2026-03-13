from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateStatusGateTests(unittest.TestCase):
    def test_readme_mentions_intro_first_validate_status_gate(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/README_INTRO_FIRST_VALIDATE_STATUS_GATE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'README_INTRO_FIRST_VALIDATE_STATUS_GATE.md').exists())


if __name__ == '__main__':
    unittest.main()
