# README 랜딩 빠른 시작 맵 / README landing quick-start map

README 첫 화면에서 **프로젝트 소개 → 대상 사용자 → 제공 가치 → 대표 카테고리 → 빠른 시작** 흐름을 한 번에 점검하기 위한 짧은 맵입니다.
English mirror: A compact map for checking that the README first screen still flows through project intro -> audience -> value -> featured categories -> quick start.

## 첫 화면 우선순위 / First-screen priorities

1. **프로젝트 소개 / Project intro** — 저장소가 무엇인지 첫 문단에서 바로 설명하는가?
2. **대상 사용자 / Audience** — 누가 이 저장소를 쓰는지 첫 화면에 보이는가?
3. **제공 가치 / Value** — 왜 이 저장소를 써야 하는지 즉시 이해되는가?
4. **대표 카테고리 / Featured categories** — 바로 탐색할 수 있는 대표 문서/카테고리가 보이는가?
5. **빠른 시작 / Quick start** — 첫 검증 명령과 다음 문서가 같은 화면에 있는가?

## README 상단 체크 질문 / README top-check questions

- 첫 화면이 링크 모음이 아니라 프로젝트 소개로 시작하는가?
- `python3 templates/scripts/validate_template.py`가 상단 실행 경로로 보이는가?
- `examples/quickstart.md`와 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`가 다음 행동으로 연결되는가?
- 운영/기여 규칙은 상단 소개 블록 아래로 내려가 있는가?

## 첫 화면 유지 루프 / First-screen maintenance loop

- README 상단을 편집할 때마다 소개 → 대상 사용자 → 가치 → 카테고리 → 빠른 시작 순서를 다시 확인합니다.
- 구조를 바꿨다면 `python3 templates/scripts/validate_template.py`를 실행해 상단 가드가 깨지지 않았는지 검증합니다.
- 세부 운영 문서를 올리고 싶어지면 먼저 `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, `docs/CURATION_POLICY.md`로 내릴 수 있는지 검토합니다.

## 권장 연결 / Recommended handoff

- README 상단 요약 블록 → `examples/quickstart.md`
- 역할별 진입 경로 → `docs/README_FAST_PATHS.md`
- 랜딩 구조 점검 → `docs/README_FIRST_SCREEN_CHECKLIST.md`
- 가치/메시지 근거 → `docs/README_AUDIENCE_VALUE_MAP.md`, `docs/README_VALUE_PROOF_POINTS.md`
