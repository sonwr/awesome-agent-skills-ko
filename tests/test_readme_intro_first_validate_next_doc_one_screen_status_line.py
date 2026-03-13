from pathlib import Path


def test_readme_mentions_intro_first_validate_next_doc_one_screen_status_line() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_ONE_SCREEN_STATUS_LINE.md" in readme
