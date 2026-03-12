from pathlib import Path


def test_readme_mentions_intro_first_ten_second_check() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/README_INTRO_FIRST_TEN_SECOND_CHECK.md" in readme
    assert "첫 10초 안에 읽히는지" in readme
