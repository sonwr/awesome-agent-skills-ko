from pathlib import Path


def test_readme_mentions_intro_first_validate_next_doc_two_step_lock() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_TWO_STEP_LOCK.md" in readme
