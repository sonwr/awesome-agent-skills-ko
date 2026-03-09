# README 프로젝트 빠른 시작 번들 / README project quickstart bundle

## 한국어 기준 / Korean-first bundle

README 상단은 프로젝트 소개 다음에 **바로 실행할 첫 검증 묶음**을 보여줘야 합니다.
이 문서는 그 묶음의 기준 문서입니다.

### 첫 검증 묶음 / First validation bundle
- 첫 명령 / First command — `python3 templates/scripts/validate_template.py`
- 다음 문서 / Next doc — `examples/quickstart.md`
- 첫 PR 증빙 / First PR evidence — `examples/pr-evidence-mini-walkthrough.md`
- 병기/기여 규칙 / Bilingual contribution rule — `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`

### 왜 필요한가 / Why this matters
- README 첫 화면에서 실행 경로가 바로 보여야 합니다.
- 소개 우선 구조를 유지하되, 소개만 읽고 멈추지 않게 해야 합니다.
- 기여 규칙은 운영 문서로 내려도, 첫 검증 묶음은 상단에서 바로 연결되어야 합니다.

### 유지 규칙 / Maintenance rule
- README 상단을 바꾼 뒤에는 위 네 항목이 첫 화면 근처에 모두 남아 있는지 확인합니다.
- 빠른 시작 설명이 길어지면 운영/기여 세부 규칙은 하단 문서로 내리고, 상단에는 이 번들만 유지합니다.
- 새 스타터 문서를 추가하더라도 기존 첫 검증 묶음의 순서를 깨지 않습니다.

## English mirror

The README should show a **first validation bundle** immediately after the project intro.
This document defines that bundle.

### First validation bundle
- First command — `python3 templates/scripts/validate_template.py`
- Next doc — `examples/quickstart.md`
- First PR evidence — `examples/pr-evidence-mini-walkthrough.md`
- Bilingual contribution rule — `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`

### Why this matters
- The first README screen should expose an executable path, not just repo context.
- The intro-first structure should lead directly into action.
- Governance details can move lower, but the first validation bundle must stay visible near the top.

### Maintenance rule
- After editing the top of the README, verify that all four bundle items still appear near the first screen.
- If quickstart prose grows, move deeper governance/contribution details lower and keep only the bundle near the top.
- New starter docs must not break the order of the existing validation bundle.
