from pathlib import Path


def test_readme_mentions_intro_first_validate_next_doc_one_card() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8")
    note = (root / "docs" / "README_INTRO_FIRST_VALIDATE_NEXT_DOC_ONE_CARD.md").read_text(encoding="utf-8")
    assert "README_INTRO_FIRST_VALIDATE_NEXT_DOC_ONE_CARD.md" in readme
    assert "python3 templates/scripts/validate_template.py" in note
    assert "examples/quickstart.md" in note
