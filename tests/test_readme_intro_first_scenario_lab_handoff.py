from pathlib import Path


def test_readme_intro_first_scenario_lab_handoff_doc():
    text = Path("docs/README_INTRO_FIRST_SCENARIO_LAB_HANDOFF.md").read_text(encoding="utf-8")

    assert "scenario_lab" in text
    assert "README" in text
    assert "intro-first" in text
