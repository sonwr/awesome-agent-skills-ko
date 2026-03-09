# README 첫 화면 체크리스트 / README first-screen checklist

README 첫 화면을 프로젝트 소개형 랜딩으로 유지할 때 빠르게 확인하는 체크리스트입니다.
English mirror: Use this checklist to keep the README opening focused on project discovery instead of governance overflow.

## 한국어 체크 / Korean checks

- [ ] 첫 화면에 **프로젝트 소개 → 대상 사용자 → 제공 가치 → 대표 카테고리/활용 시나리오 → 빠른 시작** 흐름이 보인다.
- [ ] `## 프로젝트 소개 / Project overview` 헤딩이 README 첫 12줄 안에 있다.
- [ ] 첫 검증 명령(`python3 templates/scripts/validate_template.py`)과 다음 읽을 문서(`examples/quickstart.md`)를 1분 안에 찾을 수 있다.
- [ ] 첫 검증 명령(`python3 templates/scripts/validate_template.py`)이 README 첫 160줄 안에 노출된다.
- [ ] 이 저장소가 누구에게 맞는지(추천 대상 / Best for)를 첫 화면에서 바로 판단할 수 있다.
- [ ] 기여 규칙/운영 철학/로드맵은 README 하단이나 `CONTRIBUTING.md`, `docs/`로 내려가 있다.
- [ ] 첫 방문자가 탐색형/기여형/운영형 경로 중 하나를 바로 고를 수 있다.
- [ ] 한국어 기본 문안과 영어 미러가 같은 메시지를 전달한다.

## English mirror

- [ ] The first screen shows **overview -> audience -> value -> featured categories/use cases -> quick start** in that order.
- [ ] The `## 프로젝트 소개 / Project overview` heading appears within the first 12 lines of the README.
- [ ] A newcomer can find the first validation command (`python3 templates/scripts/validate_template.py`) and next doc (`examples/quickstart.md`) within a minute.
- [ ] The first validation command (`python3 templates/scripts/validate_template.py`) appears within the first 160 lines so the landing screen stays action-oriented.
- [ ] The first screen makes it obvious who the repo is best for before governance details take over.
- [ ] Contribution rules, governance philosophy, and roadmap details stay lower in the README or move into `CONTRIBUTING.md` / `docs/`.
- [ ] A first-time visitor can immediately choose an explorer, contributor, or operator path.
- [ ] The Korean-first copy and English mirror communicate the same landing message.

- 역할별 바로 점프 / Role-based instant jumps 섹션이 README 상단에 있고 `docs/README_FAST_PATHS.md`의 역할별 앵커로 직접 연결되는지 확인한다.
- Confirm the README top keeps a `역할별 바로 점프 / Role-based instant jumps` section that deep-links to the role anchors in `docs/README_FAST_PATHS.md`.

- 상단 순서 고정 / Keep the top order fixed: `overview -> audience -> value -> featured categories -> quick start`
- 첫 140줄 안에서 위 순서를 지켜 소개 우선 흐름이 운영/기여 문서보다 먼저 보이게 합니다.

English mirror:
- Keep `overview -> audience -> value -> featured categories -> quick start` visible in order within the first 140 lines so the README stays intro-first before governance-heavy sections.
