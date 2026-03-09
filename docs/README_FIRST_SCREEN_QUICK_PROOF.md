# README_FIRST_SCREEN_QUICK_PROOF.md

README 상단이 프로젝트 소개 우선 구조를 유지하는지 30초 안에 확인하는 빠른 점검표입니다.

English mirror: A 30-second proof sheet for checking that the README still leads with project intro, audience, value, examples, and quick start.

## 빠른 증명 순서 / Quick proof order

1. **프로젝트 소개가 첫 화면에 보이는가? / Does the project intro appear on the first screen?**
   - `## 프로젝트 소개 / Project overview`가 상단 블록 뒤 50줄 안에 있어야 합니다.
2. **대상 사용자와 가치가 소개보다 뒤처지지 않는가? / Do audience and value stay near the intro?**
   - `## 바로 시작 요약 / Start-here summary` 안에서 소개 → 대상 사용자 → 대표 가치 → 대표 카테고리 → 빠른 시작 순서를 유지합니다.
3. **첫 명령과 다음 문서가 바로 보이는가? / Are the first command and next doc immediately visible?**
   - `python3 templates/scripts/validate_template.py`와 `examples/quickstart.md`가 첫 화면 블록 안에 남아 있어야 합니다.
4. **운영 문서가 아래로 내려가 있는가? / Do governance docs stay below the landing block?**
   - `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, `docs/CURATION_POLICY.md`는 소개/가치/빠른 시작 뒤에 읽도록 안내되어야 합니다.

## 언제 열어보나 / When to open this

- README 상단 구조를 수정했을 때
- 기여자가 “왜 운영 문서보다 프로젝트 소개가 먼저 와야 하냐”고 물을 때
- validator 실패 메시지의 의도를 빠르게 설명해야 할 때

## 함께 보는 문서 / Companion docs

- `docs/README_FIRST_SCREEN_CHECKLIST.md`
- `docs/README_PROJECT_FIRST_SCREEN_OVERVIEW.md`
- `docs/README_PROJECT_ENTRY_PROMISE.md`
- `docs/README_PROJECT_QUICKSTART_FLOW.md`
