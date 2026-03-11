from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstStarterPathsTests(unittest.TestCase):
    def test_readme_mentions_intro_first_starter_paths(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/README_FIRST_SCREEN_STARTER_PATHS.md', readme)
        self.assertTrue((ROOT / 'docs' / 'README_FIRST_SCREEN_STARTER_PATHS.md').exists())


if __name__ == '__main__':
    unittest.main()
