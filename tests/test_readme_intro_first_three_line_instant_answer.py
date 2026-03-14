from pathlib import Path


def test_readme_intro_first_three_line_instant_answer() -> None:
    text = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
    assert "첫 화면 3줄 즉답 / First-screen 3-line instant answer:" in text
    assert "`python3 templates/scripts/validate_template.py` -> `examples/quickstart.md`" in text
