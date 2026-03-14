# README Quick Fit Check

README 첫 화면에서는 아래 3가지를 스크롤 없이 확인할 수 있어야 합니다.
English mirror: On the first README screen, readers should confirm these three cues without scrolling for context.

1. **누구를 위한 저장소인지 / Who this repo helps**
2. **바로 실행할 첫 검증 명령 / First validation command to run now**
3. **검증 직후 열 다음 문서 / Next document right after validation**

기본 intro-first 빠른 경로 / Default intro-first quick lane:

- `python3 templates/scripts/validate_template.py`
- `examples/quickstart.md`
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`

짧은 점검 질문 / Quick check question:

> 소개 바로 아래에서 `대상 사용자 -> 첫 검증 명령 -> 다음 문서`가 한 시야에 남는가?

If the answer is no, trim or reorder the first-screen copy before committing README changes.
