from pathlib import Path


def test_readme_mentions_intro_first_validate_then_next_doc_status() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/README_INTRO_FIRST_VALIDATE_THEN_NEXT_DOC_STATUS.md" in text
