# 기여 체크리스트 (한국어 기본 + 영어 병기)

이 문서는 `awesome-agent-skills-ko` 저장소에서 새 스킬/템플릿을 추가할 때 최소 품질 기준을 빠르게 점검하기 위한 체크리스트입니다.

참고: CI의 `templates/scripts/validate_template.py`는 README의 `English mirror:` 문구 존재 여부, 번역 문구 최소 길이(의미 있는 설명), 본 문서의 한/영 섹션 마커, 그리고 자동 검증 명령 목록의 한/영 항목 수 일치를 함께 검증합니다.

## 한국어 체크리스트 (Primary)

- [ ] 문제 정의가 3줄 이내로 명확한가?
- [ ] 실행 환경(런타임/의존성/OS) 정보가 재현 가능하게 적혀 있는가?
- [ ] 설치/실행 명령을 처음부터 따라 했을 때 결과가 재현되는가?
- [ ] 예상 출력(성공 기준/실패 신호)이 문서화되어 있는가?
- [ ] 한계/리스크/실패 복구 절차가 포함되어 있는가?
- [ ] 유지보수 관점(버전, 호환성, 향후 업데이트 포인트)이 적혀 있는가?

## English mirror

- [ ] Is the problem statement clear within 3 lines?
- [ ] Is runtime/dependency/OS context documented for reproducibility?
- [ ] Can a newcomer reproduce the same result by following setup/run commands?
- [ ] Are expected outputs (success criteria and failure signals) documented?
- [ ] Are limitations, risks, and failure-recovery steps included?
- [ ] Are maintenance notes (version/compatibility/future update points) included?

## 자동 검증 명령 / Validation commands

한국어:

- 템플릿/문서 기본 검증: `python3 templates/scripts/validate_template.py`
- CI 전 로컬 스모크 점검: `python3 templates/scripts/validate_template.py && git diff --stat`

English mirror:

- Baseline template/doc validation: `python3 templates/scripts/validate_template.py`
- Local smoke check before CI: `python3 templates/scripts/validate_template.py && git diff --stat`

## 최소 증빙 스니펫 / Minimal evidence snippet

한국어:

- [ ] PR 코멘트에 아래 3줄을 붙였는가?
  - 실행 명령:
  - 성공/실패 코드:
  - 핵심 출력 1~2줄:

English mirror:

- [ ] Did you paste the following 3 lines in the PR comment?
  - Command executed:
  - Exit code (success/fail):
  - Key output (1-2 lines):

### PR 코멘트 예시 / PR comment examples

한국어 예시:

```text
[재현 증빙]
- 실행 명령: python3 templates/scripts/validate_template.py
- 종료 코드: 0
- 핵심 출력: baseline + bilingual markers are present
```

English mirror:

```text
[Repro evidence]
- Command executed: python3 templates/scripts/validate_template.py
- Exit code: 0
- Key output: baseline + bilingual markers are present
```

## 처음 기여할 때 읽는 순서 / First-time contributor reading order

한국어:

- `README.md` 상단 핵심 콜아웃 → 빠른 기여 체크 → 이 체크리스트 순서로 읽습니다. *(예상 3분 이내)*
- 실제 증빙 예시가 필요하면 `examples/pr-evidence-mini-walkthrough.md`를 바로 엽니다. *(예상 2분 이내)*

English mirror:

- Read `README.md` top callouts → quick contribution check → this checklist in order. *(Estimated within 3 minutes)*
- Open `examples/pr-evidence-mini-walkthrough.md` immediately when you need a copyable evidence example. *(Estimated within 2 minutes)*

## 리뷰어 메모 템플릿 / Reviewer note template

한국어:

```text
- 승인 여부: (Approve/Request changes)
- 핵심 근거:
- 재현 확인 범위:
- 누락/보완 요청:
```

English:

```text
- Decision: (Approve/Request changes)
- Key rationale:
- Reproduction scope verified:
- Missing items / requested follow-up:
```

## 반복 작업 방지 로그 / Anti-repeat run log

한국어:

- 최근 3회 실행에서 동일 변경을 반복하지 않았는가? (무엇을 새로 바꿨는지 1줄 기록)
- 실패/막힘이 있었다면 다음 실행 우선순위를 명시했는가?

English mirror:

- Did this run avoid repeating the same change from the last 3 runs? (add one line on what is new)
- If there was a failure/blocker, did you document the top priority for the next run?

