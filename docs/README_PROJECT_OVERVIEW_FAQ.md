# README 프로젝트 소개 FAQ / README project overview FAQ

README 상단을 처음 읽는 사람이 프로젝트 의미와 다음 행동을 바로 파악하도록 돕는 짧은 FAQ입니다.
This short FAQ helps first-time README readers understand the project meaning and the next action immediately.

## 1) 이 저장소는 무엇인가요? / What is this repository?
- 한국어 기본으로 에이전트 스킬, 템플릿, 검증 흐름을 큐레이션한 저장소입니다.
- README 첫 화면만 읽어도 프로젝트 소개, 대표 카테고리, 빠른 시작, 기여 경로를 바로 찾게 만드는 구조를 지향합니다.
- It is a Korean-first curated repository of agent skills, templates, and validation flows.
- The README is designed so the first screen points directly to project intro, featured categories, quick start, and contribution paths.

## 2) 누구에게 맞나요? / Who is it for?
- 한국어 기본 문서 흐름으로 스킬을 탐색하고 검증하며 첫 PR까지 빠르게 연결하고 싶은 개인/팀에게 맞습니다.
- It fits builders and teams who want Korean-first discovery, validation, and contribution handoff.

## 3) 왜 README 상단이 소개 우선인가요? / Why is the README intro-first?
- 방문자가 운영 규칙보다 먼저 프로젝트의 가치와 사용 맥락을 이해해야 이탈이 줄어듭니다.
- 그래서 상단은 소개 → 대상 사용자 → 제공 가치 → 대표 카테고리 → 빠른 시작 순서를 유지합니다.
- Visitors should understand value and usage context before governance detail, so the README keeps overview → audience → value → featured categories → quick start first.

## 4) 무엇을 먼저 실행하면 되나요? / What should I run first?
```bash
python3 templates/scripts/validate_template.py
```
- 그다음 기본 흐름은 `examples/quickstart.md`입니다.
- The default next doc after the first command is `examples/quickstart.md`.

## 5) 기여 규칙과 운영 문서는 어디 있나요? / Where do contribution and governance docs live?
- 기여 규칙: `CONTRIBUTING.md`, `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- 운영/랜딩 구조 점검: `docs/README_FAST_PATHS.md`, `docs/README_FIRST_SCREEN_CHECKLIST.md`, `docs/CURATION_POLICY.md`
- Contribution rules live in `CONTRIBUTING.md` and `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`.
- Governance and landing audits live in `docs/README_FAST_PATHS.md`, `docs/README_FIRST_SCREEN_CHECKLIST.md`, and `docs/CURATION_POLICY.md`.
