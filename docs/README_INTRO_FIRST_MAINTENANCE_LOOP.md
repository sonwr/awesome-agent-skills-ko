# README 소개 우선 유지 루프 / README intro-first maintenance loop

README 상단을 프로젝트 소개 중심으로 유지하기 위한 짧은 운영 루프입니다.

English mirror: A short operating loop for keeping the README top focused on project introduction before governance detail.

## 1) 소개 먼저 확인 / Confirm the intro first

- 첫 화면이 **무엇을 하는 저장소인지** 먼저 설명하는지 확인합니다.
- 대상 사용자, 제공 가치, 대표 예시/빠른 시작이 상단에 남아 있는지 확인합니다.
- 운영 규칙/체크리스트/장기 문서는 아래로 밀려 있는지 확인합니다.

English mirror:
- Confirm the first screen explains **what the project is** before anything else.
- Keep audience, value, featured examples, and quick start above the fold.
- Push governance checklists and long-form operating docs lower.

## 2) 경로를 끊지 않기 / Preserve the handoff path

- 소개 → 빠른 시작 → 다음 문서(`examples/quickstart.md`) 흐름이 한 번에 이어져야 합니다.
- 기여 경로는 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`, 운영 경로는 `docs/README_FAST_PATHS.md`로 이어집니다.

English mirror:
- Keep the intro -> quick start -> next doc (`examples/quickstart.md`) path continuous.
- Hand contribution paths to `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` and operator paths to `docs/README_FAST_PATHS.md`.

## 3) 수정 후 검증 / Validate after edits

```bash
python3 templates/scripts/validate_template.py
```

- 구조를 바꾼 뒤에는 `docs/README_FIRST_SCREEN_CHECKLIST.md`로 사람이 다시 읽습니다.
- 필요하면 `docs/README_PROJECT_INTRO_BLUEPRINT.md`와 함께 문구를 다듬습니다.

English mirror:
- After every structural change, re-read `docs/README_FIRST_SCREEN_CHECKLIST.md` as a human review step.
- When needed, refine the copy with `docs/README_PROJECT_INTRO_BLUEPRINT.md`.

## 4) 첫 화면 handoff 문장을 남기기 / Leave a first-screen handoff sentence

- 첫 화면을 손댄 날에는 **무엇을 하는 저장소인지 + 지금 무엇을 하면 되는지**를 한 줄로 다시 적어둡니다.
- 소개 문단이 길어지면, 가치 설명은 남기고 운영 문장은 별도 문서로 내립니다.
- `examples/quickstart.md` 또는 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`로 이어지는 다음 행동이 보이지 않으면 intro-first가 깨진 것으로 봅니다.

English mirror:
- On any day you touch the first screen, rewrite one sentence that states **what the repo is and what the reader should do now**.
- If the intro grows too long, keep the value statement and push operating detail into supporting docs.
- If the next action toward `examples/quickstart.md` or `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` disappears, treat the intro-first flow as broken.
