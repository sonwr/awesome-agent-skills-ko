# README 프로젝트 빠른 소개 / README project fast intro

README 첫 화면이 길어져도 맨 위에서 반드시 먼저 보여야 하는 **프로젝트 소개 압축본**입니다.
운영 규칙이나 긴 링크 묶음보다 앞에서, 방문자가 이 저장소의 목적·대상 사용자·첫 실행 경로를 30초 안에 이해하게 만드는 기준 문서로 사용합니다.

English mirror: This is the compact project intro that must stay visible near the top of the README even when the landing page grows.
Use it as the source-of-truth for the repo purpose, best-fit audience, and first action path before heavier governance/link bundles.

## 한국어 기준 / Korean-first rule

- **무엇을 하는 저장소인가?** 한국어 기반 빌더를 위한 에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음
- **누구를 돕는가?** 한국어 기본 흐름으로 탐색·검증·기여를 빠르게 시작하려는 개인/팀
- **첫 행동은 무엇인가?** `python3 templates/scripts/validate_template.py` 실행 후 `examples/quickstart.md` 열기
- **운영 문서는 어디로 보내는가?** `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, `docs/CURATION_POLICY.md`는 소개 블록 아래로 내림
- **상단 유지 규칙은 무엇인가?** 소개 → 대상 사용자 → 제공 가치 → 대표 예시/빠른 시작 순서를 첫 화면에서 지킨다

## English mirror

- **What is this repo?** A curated collection of agent skills and runnable templates for Korean-speaking builders.
- **Who does it help?** Individuals and teams who want a fast Korean-first path for discovery, validation, and contribution.
- **What is the first action?** Run `python3 templates/scripts/validate_template.py`, then open `examples/quickstart.md`.
- **Where do governance docs go?** Keep `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, and `docs/CURATION_POLICY.md` below the intro block.
- **What is the landing rule?** Preserve the order overview -> audience -> value -> featured examples/quick start on the first screen.

## 유지 규칙 / Maintenance rule

- README 상단을 수정한 뒤 `docs/README_PROJECT_FAST_INTRO.md`의 세 문장(무엇/누구/첫 행동)이 첫 90줄 안에 반영됐는지 확인합니다.
- 새 링크 묶음이나 운영 문서를 추가할 때도 `docs/README_PROJECT_FAST_INTRO.md` 링크는 첫 화면에 남겨 둡니다.
- 검증은 `python3 templates/scripts/validate_template.py`로 고정합니다.
