# README 첫 방문 체크포인트 / README first-visitor checkpoints

## 목적 / Purpose
README 첫 화면을 읽는 방문자가 **소개 이해 → 빠른 검증 → 다음 문서 이동**까지 막히지 않는지 점검합니다.
English mirror: Audit whether a first-time visitor can understand the intro, run validation quickly, and reach the next document without friction.

## 체크포인트 / Checkpoints
1. **프로젝트 소개가 먼저 보이는가? / Does the project intro appear first?** 저장소가 무엇을 하는지 첫 화면에서 바로 설명해야 합니다.
2. **첫 검증 명령이 노출되는가? / Is the first validation command visible?** `python3 templates/scripts/validate_template.py`가 첫 화면 흐름 안에 있어야 합니다.
3. **다음 문서가 분명한가? / Is the next document obvious?** `examples/quickstart.md` 또는 기여용 문서로 자연스럽게 이어져야 합니다.
4. **운영 문서는 아래로 내려갔는가? / Did governance stay lower?** 정책/운영 문서는 프로젝트 가치 소개를 가리지 않아야 합니다.
