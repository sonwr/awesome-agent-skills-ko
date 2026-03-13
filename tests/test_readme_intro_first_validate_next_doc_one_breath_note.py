from __future__ import annotations

from pathlib import Path


def test_readme_mentions_intro_first_validate_next_doc_one_breath_note() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / 'README.md').read_text(encoding='utf-8')

    assert 'docs/README_INTRO_FIRST_VALIDATE_NEXT_DOC_ONE_BREATH_NOTE.md' in readme
    assert (root / 'docs' / 'README_INTRO_FIRST_VALIDATE_NEXT_DOC_ONE_BREATH_NOTE.md').exists()
