from pathlib import Path


def test_readme_mentions_intro_first_two_step_path() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/README_INTRO_FIRST_TWO_STEP_PATH.md" in readme
    assert "첫 두 단계 이동 경로" in readme
