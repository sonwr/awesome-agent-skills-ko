from pathlib import Path


def test_readme_mentions_intro_first_validate_hold_status_note() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "README.md").read_text(encoding="utf-8")

    assert "검증 실패 시 보류 / Hold on validator failure" in text
    assert (root / "docs" / "README_INTRO_FIRST_VALIDATE_HOLD_STATUS_NOTE.md").exists()
