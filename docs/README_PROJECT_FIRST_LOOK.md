# README 프로젝트 첫인상 가이드 / README project first-look guide

README 상단을 **프로젝트 소개 우선 구조**로 유지할 때, 첫 방문자가 가장 먼저 봐야 하는 질문과 문장을 압축해 둔 문서입니다.
English mirror: A compact guide to the questions and sentences that should appear first when the README stays project-intro-first.

## 한국어 기준 / Korean-first guide

1. **이 프로젝트는 무엇을 하나?** 한국어 기반 빌더를 위한 에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음이라는 설명이 먼저 보입니다.
2. **누구에게 바로 도움이 되나?** 탐색형/기여형/운영형 방문자가 자신에게 맞는 시작 경로를 15초 안에 찾을 수 있어야 합니다.
3. **무엇을 바로 실행하나?** `python3 templates/scripts/validate_template.py`와 `examples/quickstart.md`가 같은 첫 화면 흐름 안에 있어야 합니다.
4. **운영 문서는 어디로 가나?** 기여 규칙과 장기 운영 문서는 첫 화면 아래 `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, `docs/CURATION_POLICY.md`로 내려갑니다.

## English mirror

1. **What does this project do?** Lead with the message that this repo is a curated collection of agent skills and runnable templates for Korean-speaking builders.
2. **Who benefits first?** Explorer / contributor / operator visitors should find their route within about 15 seconds.
3. **What should they run immediately?** Keep `python3 templates/scripts/validate_template.py` and `examples/quickstart.md` in the same first-screen flow.
4. **Where does governance go?** Move contribution rules and long-range operating docs below the landing block into `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, and `docs/CURATION_POLICY.md`.

## 유지 규칙 / Maintenance rule

- README 상단을 바꾼 뒤에는 `python3 templates/scripts/validate_template.py`를 실행합니다.
- `docs/README_FIRST_SCREEN_CHECKLIST.md`, `docs/README_PROJECT_VALUE_QUICKCHECK.md`, `docs/README_PROJECT_FIRST_LOOK.md`를 함께 열어 소개/대상 사용자/가치/빠른 시작 순서가 유지되는지 확인합니다.
