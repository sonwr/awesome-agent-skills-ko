# README 첫 화면 결정 트리 / README first-screen decision tree

README 상단을 프로젝트 소개 우선 구조로 유지하면서도, 처음 방문한 사람이 **무엇을 먼저 읽고 실행할지** 15초 안에 결정하도록 돕는 압축 가이드입니다.
English mirror: A compact guide for helping first-time visitors decide what to read or run first within 15 seconds while keeping the README intro-first.

## 1) 나는 어떤 방문자인가? / What kind of visitor am I?

- **탐색형 / Explorer** — 저장소가 무엇인지 빠르게 이해하고 싶다 → `## 프로젝트 소개 / Project overview` → `examples/quickstart.md`
- **기여형 / Contributor** — 첫 PR이나 증빙 예시가 필요하다 → `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`
- **운영형 / Operator** — README 상단 정보구조와 운영 가드레일을 점검하고 싶다 → `docs/README_FIRST_SCREEN_CHECKLIST.md` → `docs/README_FAST_PATHS.md`

## 2) 첫 행동은 무엇인가? / What is the first action?

1. 프로젝트 이해가 먼저면 `프로젝트 소개 / Project overview`를 읽습니다.
2. 바로 실행하고 싶으면 `python3 templates/scripts/validate_template.py`를 실행합니다.
3. 첫 PR 흐름이 필요하면 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`를 엽니다.
4. 랜딩 구조 감사가 목적이면 `docs/README_FIRST_SCREEN_CHECKLIST.md`를 엽니다.

1. Read `Project overview` first if you need to understand the repo.
2. Run `python3 templates/scripts/validate_template.py` first if you want immediate execution.
3. Open `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` if you need the first PR flow.
4. Open `docs/README_FIRST_SCREEN_CHECKLIST.md` if you are auditing the landing structure.

## 3) 유지 원칙 / Maintenance rule

- 이 결정 트리는 README 상단의 **소개 → 대상 사용자 → 제공 가치 → 대표 예시/카테고리 → 빠른 시작** 흐름을 보조해야 하며, 운영 문서를 위로 끌어올리면 안 됩니다.
- README 상단 구조를 바꿨다면 `templates/scripts/validate_template.py`와 `docs/README_FIRST_SCREEN_CHECKLIST.md`를 함께 확인합니다.

- This decision tree should support the README flow of **overview -> audience -> value -> featured examples/categories -> quick start** without pulling governance-heavy docs upward.
- After changing the README top, re-run `templates/scripts/validate_template.py` and re-check `docs/README_FIRST_SCREEN_CHECKLIST.md`.
