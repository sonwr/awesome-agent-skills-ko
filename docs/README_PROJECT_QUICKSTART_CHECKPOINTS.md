# README 프로젝트 빠른 시작 체크포인트 / README project quickstart checkpoints

README 상단의 빠른 시작 블록이 **소개 우선 구조를 깨지 않으면서도** 바로 실행 가능한지 점검하는 기준 문서입니다.
This note defines the checkpoints for a quick-start block that stays intro-first while remaining immediately runnable.

## 한국어 기준 / Korean-first checkpoints

1. 프로젝트 소개/대상 사용자/제공 가치가 빠른 시작보다 먼저 보인다.
2. 첫 명령은 `python3 templates/scripts/validate_template.py`로 고정한다.
3. 첫 명령 바로 뒤에는 `examples/quickstart.md` 같은 다음 문서가 붙는다.
4. 첫 PR 증빙 경로(`docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`, `examples/pr-evidence-mini-walkthrough.md`)를 빠른 시작 아래에서 바로 찾게 한다.
5. 운영/감사 문서는 상단 소개 블록 아래 별도 섹션으로 내린다.

## English mirror

1. Keep project intro, audience, and value above quick start.
2. Keep the first command anchored on `python3 templates/scripts/validate_template.py`.
3. Pair that first command with the next doc (`examples/quickstart.md`) immediately.
4. Make first-PR evidence docs easy to find right under the quick-start block.
5. Push governance/audit docs below the landing intro block.

## 유지 규칙 / Maintenance rule

- README 상단 문구를 바꿀 때는 이 문서와 `docs/README_PROJECT_QUICKSTART_BUNDLE.md`를 함께 갱신합니다.
- 빠른 시작이 길어지면 실행 명령/다음 문서/첫 PR 증빙만 남기고 세부 운영 가이드는 아래 섹션이나 별도 문서로 내립니다.
