# README 첫 클릭 근거 카드 / README first-click proof card

README 첫 화면을 다듬을 때, 첫 클릭이 프로젝트 소개와 빠른 시작을 실제로 이어주는지 30초 안에 점검하는 카드입니다.
English mirror: A 30-second card for checking whether the first click still connects the project intro to the quick-start path.

## 3가지 확인 / Three checks

1. **소개 다음 클릭 / Intro handoff** — 첫 클릭이 운영 문서가 아니라 프로젝트 소개·대표 예시·빠른 시작 중 하나로 이어지나요?
   English mirror: Does the first click go to the project intro, featured examples, or quick start instead of governance-heavy docs?
2. **가치 다음 클릭 / Value handoff** — 클릭 직후 "왜 이 저장소인가"를 보여주는 문장이 이어지나요?
   English mirror: Right after the click, can the visitor still see why this repo exists?
3. **실행 다음 클릭 / Action handoff** — `python3 templates/scripts/validate_template.py` 또는 `examples/quickstart.md`로 자연스럽게 이어지나요?
   English mirror: Does the path naturally continue to `python3 templates/scripts/validate_template.py` or `examples/quickstart.md`?

## 빠른 판정 / Fast verdict

- **유지 / Keep** — 소개 → 가치 → 빠른 시작 흐름이 첫 클릭 뒤에도 유지됩니다.
- **재배치 / Reorder** — 첫 클릭이 너무 빨리 운영/정책 문서로 떨어지면 README 상단에서 한 단계 아래로 내립니다.

## 한 줄 원칙 / One-line rule

첫 클릭은 설명보다 먼저 정책으로 떨어지면 안 되고, 빠른 시작으로 이어지지 않으면 landing proof가 약해집니다.
English mirror: The first click should not dump visitors into policy before value, and it should still lead toward quick start.
