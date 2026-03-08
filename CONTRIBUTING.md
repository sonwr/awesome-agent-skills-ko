# 기여 가이드 / Contributing

`awesome-agent-skills-ko`에 기여해 주셔서 감사합니다.
English mirror: Thanks for contributing to `awesome-agent-skills-ko`.

## 기여 원칙 / Principles

- 실무 적용성과 유지보수성을 새로움보다 우선합니다.
- 재현 가능한 명령과 검증 결과를 함께 남깁니다.
- 장점뿐 아니라 tradeoff와 한계도 명시합니다.
- README 상단 랜딩 구조(프로젝트 소개 → 대상 사용자 → 제공 가치 → 대표 카테고리 → 빠른 시작)를 흐리지 않습니다.

English mirror:
- Prefer practical impact and maintainability over novelty.
- Always include reproducible commands and validation evidence.
- Document tradeoffs and limitations, not just the happy path.
- Keep the README landing order focused on overview → audience → value → featured categories → quick start.

## PR 필수 항목 / Pull request requirements

모든 PR에는 아래 내용을 포함하세요.

1. 해결하려는 문제 / What problem this solves
2. 재현 환경과 실행 명령 / Setup steps and runnable command
3. 기대 출력 또는 변경 전후 차이 / Expected output or before-vs-after diff
4. 검증 결과(종료코드 포함) / Validation result with exit code
5. 알려진 한계와 다음 작업 / Known limitations and next-step note

English mirror:
Include all of the following in every PR:
1. What problem this solves
2. Setup steps and runnable command
3. Expected output or before-vs-after diff
4. Validation result (including exit code)
5. Known limitations and the next-step note

## 리뷰 체크리스트 / Review checklist

- [ ] 목적이 명확하다 / Purpose is clear
- [ ] 재현 명령이 있다 / Reproduction command is present
- [ ] 핵심 출력 또는 검증 근거가 있다 / Key output or validation evidence is present
- [ ] 한계 또는 막힘이 적혀 있다 / Limitations or blockers are documented
- [ ] 특정 런타임 종속성이 숨겨져 있지 않다 / No hidden vendor lock-in assumptions
- [ ] README 상단 소개 흐름을 해치지 않는다 / Does not degrade the README landing flow

## 첫 기여 전에 볼 문서 / Read these before the first PR

- `README.md` — 프로젝트 소개와 빠른 시작 흐름
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — 한/영 병기 및 최소 증빙 기준
- `examples/pr-evidence-mini-walkthrough.md` — PR 설명 예시
- `docs/README_INFORMATION_ARCHITECTURE.md` — README 랜딩 우선순위 기준

English mirror:
- `README.md` — overview and quick start flow
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — bilingual and minimum-evidence rules
- `examples/pr-evidence-mini-walkthrough.md` — PR evidence example
- `docs/README_INFORMATION_ARCHITECTURE.md` — README landing-page priority guide
