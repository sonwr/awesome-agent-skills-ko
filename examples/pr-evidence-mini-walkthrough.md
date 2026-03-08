# PR 증빙 미니 워크스루 / PR Evidence Mini Walkthrough

## 목적 (한국어)
`docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`의 최소 증빙 규칙(명령/종료코드/핵심 출력)을 실제 PR 코멘트에 어떻게 적용하는지 1분 안에 확인할 수 있는 샘플입니다.

## Purpose (English)
This 1-minute sample shows how to apply the checklist's minimum evidence rule (command/exit-code/key output) in an actual PR comment.

---

## 예시 시나리오 / Sample scenario
- 변경 파일: `README.md`
- 변경 내용: 한/영 병기 안내 문장 1줄 추가
- 검증 명령: `python3 templates/scripts/validate_template.py`

## PR 코멘트 예시 (한국어)
```text
[재현 증빙]
- Command: python3 templates/scripts/validate_template.py
- Exit code: 0
- Key output: 검증 통과 / Validation passed: baseline + bilingual markers are present.
```

## PR comment example (English)
```text
[Repro evidence]
- Command: python3 templates/scripts/validate_template.py
- Exit code: 0
- Key output: Validation passed: baseline + bilingual markers are present.
```

## 빠른 점검 포인트 / Quick checks
- 한국어 기본 문서 흐름을 유지했는가?
- 영어 미러 설명이 동일 의미로 병기되었는가?
- 명령/종료코드/핵심 출력이 모두 들어갔는가?
