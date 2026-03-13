from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeIntroFirstValidateNextDocProofTests(unittest.TestCase):
    def test_readme_mentions_validate_next_doc_proof(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_PROOF.md", readme)
        self.assertIn("validator as one bundle", readme)


if __name__ == "__main__":
    unittest.main()
