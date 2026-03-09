# README 누가 어디서 시작하나 / README who starts where

README 첫 화면에서 프로젝트 소개를 먼저 보여주되, 방문자가 자기 역할에 맞는 첫 문서와 첫 행동을 10초 안에 고를 수 있도록 돕는 보조 문서입니다.

## 한국어 기준 / Korean-first routing

### 탐색형 / Explorer
- 먼저 볼 것: `## 프로젝트 소개 / Project overview`
- 첫 행동: `examples/quickstart.md`까지 이어서 읽기
- 기대 결과: 이 저장소가 단순 링크 모음이 아니라 실행 가능한 출발점인지 빠르게 판단

### 기여형 / Contributor
- 먼저 볼 것: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- 첫 행동: `examples/pr-evidence-mini-walkthrough.md`에서 최소 PR 증빙 형식 복사
- 기대 결과: README 상단의 소개 흐름을 깨지 않고도 첫 PR 준비 시작

### 운영형 / Operator
- 먼저 볼 것: `docs/README_FIRST_SCREEN_CHECKLIST.md`
- 첫 행동: `python3 templates/scripts/validate_template.py` 실행 후 `docs/README_FAST_PATHS.md` 재확인
- 기대 결과: 프로젝트 소개 → 대상 사용자 → 제공 가치 → 빠른 시작 흐름이 유지되는지 즉시 점검

## English mirror

### Explorer
- Open first: `## Project overview`
- First action: continue into `examples/quickstart.md`
- Expected outcome: decide quickly whether the repo is a runnable starting point instead of a plain link list

### Contributor
- Open first: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- First action: copy the minimum PR evidence shape from `examples/pr-evidence-mini-walkthrough.md`
- Expected outcome: start the first PR without pulling governance-heavy detail above the landing intro

### Operator
- Open first: `docs/README_FIRST_SCREEN_CHECKLIST.md`
- First action: run `python3 templates/scripts/validate_template.py`, then re-check `docs/README_FAST_PATHS.md`
- Expected outcome: confirm the intro -> audience -> value -> quick-start order is still visible from the README first screen
