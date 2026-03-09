# README_FEATURED_USE_CASES.md

README 상단에서 먼저 보여줘야 하는 대표 활용 시나리오를 정리한다. 목표는 방문자가 저장소 소개를 이해한 직후, 자신의 상황에 맞는 첫 실행 경로를 30초 안에 고르게 만드는 것이다.

## 핵심 원칙 / Core principle

- 프로젝트 소개 다음에는 추상적인 운영 규칙보다 **대표 활용 시나리오**를 먼저 보여준다.
- 각 시나리오는 **누가 보는지 → 무엇을 여는지 → 무엇을 실행하는지 → 다음 문서가 무엇인지**가 한 번에 보이게 쓴다.
- README 상단에는 최소 3개 시나리오를 유지한다: 온보딩, 첫 PR 준비, 운영/큐레이션 점검.

## 권장 시나리오 / Recommended scenarios

1. **새 저장소 온보딩 / New repo onboarding**
   - 첫 읽기: `프로젝트 소개 / Project overview`
   - 첫 실행: `python3 templates/scripts/validate_template.py`
   - 다음 문서: `examples/quickstart.md`

2. **첫 PR 준비 / First PR prep**
   - 첫 읽기: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
   - 첫 증빙: `examples/pr-evidence-mini-walkthrough.md`
   - 문맥 보강: `docs/README_PROJECT_OVERVIEW_FAQ.md`

3. **운영 구조 점검 / Governance audit**
   - 첫 읽기: `docs/PROJECT_ENTRY_PATHS.md`
   - 구조 확인: `docs/README_INFORMATION_ARCHITECTURE.md`
   - 운영 기준: `docs/CURATION_POLICY.md`

## README 반영 체크 / README integration check

- README 첫 120줄 안에 이 문서 링크가 보여야 한다.
- README의 `대표 활용 시나리오 / Featured use cases` 섹션은 이 문서를 기준으로 유지/확장한다.
- 소개 우선 흐름을 해치지 않도록 기여 규칙이나 운영 세부 규칙은 시나리오 뒤쪽으로 내린다.
