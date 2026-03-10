# README 첫 화면 증빙 루프 / README first-screen proof loop

README 상단을 intro-first로 유지할 때, 소개 -> 실행 -> 기여 handoff가 실제로 보이는지 빠르게 점검하는 메모입니다.

## 한국어 기준 / Korean-first loop

1. **소개 증빙 / Intro proof** — 첫 화면에 프로젝트 소개와 대상 사용자가 바로 보이는가?
2. **실행 증빙 / Action proof** — `python3 templates/scripts/validate_template.py` 와 다음 문서(`examples/quickstart.md`)가 같은 화면에 남아 있는가?
3. **기여 증빙 / Contribution proof** — `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` 또는 PR 증빙 예시가 초반 동선에 연결되는가?
4. **운영 분리 / Governance split** — 운영 규칙은 상단 설명을 방해하지 않고 아래 문서로 자연스럽게 내려갔는가?

## English mirror

Use this loop to confirm the README landing area still proves four things quickly: project intro, runnable first action, contribution handoff, and governance moved lower.

## 유지 규칙 / Maintenance rule

README를 다듬은 뒤에는 이 루프와 `python3 templates/scripts/validate_template.py`를 함께 확인해 첫 화면 가치가 말뿐이 아닌지 검증합니다.
