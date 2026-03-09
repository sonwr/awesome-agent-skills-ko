# README 역할별 시작 지도 / README role-based starters

README 상단을 프로젝트 소개 우선 구조로 유지하면서도, 방문자 유형별 첫 행동을 한 장에서 바로 고르게 만드는 보조 문서입니다.

## 한국어 기준 / Korean-first map

### 탐색형 / Explorer
- 첫 질문: 이 저장소가 무엇을 해결하나?
- 첫 문서: `README.md` → `## 프로젝트 소개 / Project overview`
- 첫 행동: `## 대표 카테고리와 예시 / Featured categories and examples`까지 읽고 `examples/quickstart.md`로 이동
- 바로 얻는 가치: 링크 나열이 아니라 실행 가능한 출발점인지 1분 안에 판단

### 기여형 / Contributor
- 첫 질문: 첫 PR을 어디서 어떻게 시작하나?
- 첫 문서: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- 첫 행동: `examples/pr-evidence-mini-walkthrough.md`를 열어 최소 PR 증빙 형식을 복사
- 바로 얻는 가치: 기여 규칙을 찾느라 README 상단 흐름을 깨지 않고도 바로 실행 가능

### 운영형 / Operator
- 첫 질문: README 소개 우선 구조가 유지되고 있나?
- 첫 문서: `docs/README_FIRST_SCREEN_CHECKLIST.md`
- 첫 행동: `python3 templates/scripts/validate_template.py` 실행 후 `docs/README_FAST_PATHS.md`와 함께 점검
- 바로 얻는 가치: 정보구조/가드레일/운영 문서가 프로젝트 소개보다 위로 올라오지 않는지 빠르게 확인

## English mirror

### Explorer
- First question: what problem does this repo solve?
- First doc: `README.md` → `## Project overview`
- First action: read through `## Featured categories and examples`, then continue to `examples/quickstart.md`
- Immediate value: decide within a minute whether this is a runnable starting point, not a vague link list

### Contributor
- First question: where does the first PR start?
- First doc: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- First action: open `examples/pr-evidence-mini-walkthrough.md` and copy the minimum PR evidence format
- Immediate value: start contributing without dragging governance-heavy detail above the README landing intro

### Operator
- First question: is the intro-first README structure still intact?
- First doc: `docs/README_FIRST_SCREEN_CHECKLIST.md`
- First action: run `python3 templates/scripts/validate_template.py`, then audit with `docs/README_FAST_PATHS.md`
- Immediate value: verify quickly that information architecture and governance docs have not displaced the project intro/value/quick-start flow
