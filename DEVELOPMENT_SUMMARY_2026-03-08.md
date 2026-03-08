# 개발 요약 — 2026-03-08

## 실행 @ 04:53 UTC (cron)

### 계획
- 한국어 기본 + 영어 병기 품질 가이드를 README 흐름에 더 명확히 연결한다.
- 템플릿 검증 스크립트로 문서 품질 회귀를 즉시 확인한다.

### 변경 사항
- `README.md`의 실무용 체크리스트 섹션에 영어 병기 운영 원칙을 1줄 추가:
  - `English mirror: Use the same checklist to keep Korean-first docs and English mirrors synchronized in every PR.`

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`에 PR 리뷰어용 최소 증빙(명령 출력 샘플) 항목을 한/영으로 추가.

## 실행 @ 05:23 UTC (cron)

### 계획
- 이전 실행의 TODO였던 PR 최소 증빙 항목(명령/종료코드/핵심 출력)을 실제 체크리스트에 반영한다.
- 문서 검증 스크립트로 한/영 마커 정합성을 재확인한다.

### 변경 사항
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`에 **최소 증빙 스니펫 / Minimal evidence snippet** 섹션 추가.
  - 한국어/영어 체크 항목을 같은 구조로 제공해 리뷰 재현성 기준을 고정.
- `README.md` 체크리스트 섹션에 최소 증빙 반영 사실을 1줄 추가.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- 최소 증빙 스니펫을 실제 PR 코멘트 예시(`docs/` 예제 블록)로 확장해 신규 기여자 온보딩 시간을 줄이기.

## 실행 @ 05:53 UTC (cron)

### 계획
- 이전 TODO였던 PR 코멘트 예시를 한/영으로 실제 복붙 가능한 형태로 문서화한다.
- README에도 반영 사실을 연결해 신규 기여자 진입 경로를 줄인다.

### 변경 사항
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`에 **PR 코멘트 예시 / PR comment examples** 섹션 추가.
  - 한국어/영어 각각 `[재현 증빙]` 템플릿(명령/종료코드/핵심 출력) 제공.
- `README.md` 기여 체크리스트 안내에 PR 코멘트 예시 추가 사실 1줄 반영.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- PR 코멘트 예시를 `examples/`의 짧은 실제 변경 사례와 연결해, 리뷰어/기여자가 즉시 대조 가능한 mini walkthrough를 추가.

## 실행 @ 06:23 UTC (cron)

### 계획
- 이전 TODO였던 "실제 변경 사례 기반 mini walkthrough"를 examples로 추가한다.
- README에서 바로 접근 가능하도록 링크를 연결한다.

### 변경 사항
- `examples/pr-evidence-mini-walkthrough.md` 신규 추가.
  - 한국어 기본 설명 + 영어 미러를 같은 구조로 제공.
  - PR 코멘트 증빙 포맷(명령/종료코드/핵심 출력) 복붙 예시 수록.
- `README.md` 실무용 기여 체크리스트 섹션에 mini walkthrough 링크 추가.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- mini walkthrough를 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`의 해당 항목과 교차 링크해 온보딩 동선을 한 단계 줄이기.

## 실행 @ 06:53 UTC (cron)

### 계획
- 한/영 병기 품질 검증을 예시 문서까지 확장해 신규 기여자 온보딩 회귀를 줄인다.
- 템플릿 검증 스크립트로 즉시 회귀 여부를 확인한다.

### 변경 사항
- `templates/scripts/validate_template.py` 강화:
  - 필수 파일 목록에 `examples/pr-evidence-mini-walkthrough.md` 추가.
  - 해당 예시 문서의 핵심 한/영 섹션 마커(목적/예시 코멘트) 검증 로직 추가.
- `README.md`에 "미니 워크스루 문서 마커도 자동 검증한다"는 안내 1줄 추가.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- 체크리스트 문서에서 mini walkthrough로의 역방향 링크를 추가해 리뷰/기여 동선을 더 짧게 만든다.

## 실행 @ 07:23 UTC (cron)

### 계획
- README의 빠른 시작/기여 흐름이 병기 체크리스트로 반드시 연결되도록 자동 검증을 강화한다.
- 스크립트 변경 후 즉시 템플릿 검증을 재실행한다.

### 변경 사항
- `templates/scripts/validate_template.py` 강화:
  - README에 `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` 링크가 없으면 실패하도록 규칙 추가.
  - 기존 quick start 재현성 명령 검증과 함께 병기 거버넌스 연결성까지 점검.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`의 핵심 체크 항목을 README quick start 근처에 축약판으로 노출해 신규 기여자 탐색 비용을 줄인다.

## 실행 @ 08:23 UTC (cron)

### 계획
- 이전 TODO였던 README quick start 근처 축약 체크를 실제로 노출한다.
- 검증 스크립트도 같은 축약 섹션을 요구하도록 맞춘다.

### 변경 사항
- `README.md` quick start 아래에 **빠른 기여 체크 / Quick contribution check** 축약 섹션 추가.
  - 한국어 기본 + 영어 미러 + 상세 체크리스트 링크를 한 번에 노출.
- `templates/scripts/validate_template.py` 강화:
  - README에 축약 체크 섹션 헤더가 없으면 실패하도록 규칙 추가.

### 검증
- `python3 templates/scripts/validate_template.py`
- README 축약 섹션 존재 확인 스모크 파이썬 검사
- 결과: **PASS** (`baseline + bilingual markers are present` + quick contribution check present)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`의 핵심 3~4개 항목을 배지/콜아웃 형태로 더 압축해 README 상단 탐색 속도를 높이기.

## 실행 @ 09:00 UTC (cron)

### 계획
- README 상단에서 신규 기여자가 바로 보는 최소 규칙을 더 압축해 노출한다.
- 검증 스크립트도 같은 상단 콜아웃 구조를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md` 상단에 **상단 핵심 콜아웃 / Top contributor callouts** 섹션 추가.
- `docs/README_TOP_CALLOUTS.md`를 신설해 README 상단 문안을 별도 관리 문서로 분리.
- `templates/scripts/validate_template.py` 강화:
  - `docs/README_TOP_CALLOUTS.md`를 필수 파일로 요구
  - README 상단 콜아웃 헤더와 핵심 문구 존재 여부를 검증

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- README 상단 콜아웃과 예시 워크스루를 연결하는 "처음 기여할 때 읽는 순서" 섹션을 추가해 탐색 흐름을 더 짧게 만든다.

## 실행 @ 09:10 UTC (cron)

### 계획
- 이전 TODO였던 "처음 기여할 때 읽는 순서"를 README/체크리스트 양쪽에 추가한다.
- 검증 스크립트도 같은 온보딩 섹션을 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md`에 **처음 기여할 때 읽는 순서 / First-time contributor reading order** 섹션 추가.
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`에도 동일한 읽기 순서를 한/영으로 교차 링크.
- `templates/scripts/validate_template.py` 강화:
  - README의 읽기 순서 섹션이 없으면 실패
  - 체크리스트 문서의 읽기 순서 섹션 마커도 검증

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- README의 읽기 순서 각 단계에 예상 소요 시간(예: 1분/2분)을 붙여 신규 기여자 온보딩 속도를 더 예측 가능하게 만들기.

## 실행 @ 09:20 UTC (cron)

### 계획
- README/체크리스트의 "처음 기여할 때 읽는 순서"에 예상 소요 시간을 붙여 온보딩 속도를 더 예측 가능하게 만든다.
- 템플릿 검증 스크립트도 같은 시간 표기를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md`의 읽기 순서 3단계에 예상 소요 시간(1분/2분/2분)을 한/영 병기로 추가.
- `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`의 읽기 순서에도 단계별 예상 시간(3분/2분)을 추가.
- `templates/scripts/validate_template.py` 강화:
  - README의 읽기 순서 섹션에 estimated time 문구가 없으면 실패
  - 체크리스트 문서의 예상 시간 한/영 마커도 검증

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- README 상단 콜아웃에 "처음 5분 안에 끝내는 기여 흐름" 요약 문구를 추가해, 읽기 순서/예상 시간을 더 빠르게 발견하게 만들기.

## 실행 @ 09:30 UTC (cron)

### 계획
- README 상단 콜아웃에서 신규 기여자가 5분 온보딩 흐름을 즉시 발견하도록 문구를 더 압축한다.
- 검증 스크립트도 같은 상단 요약 문구를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md` 상단 핵심 콜아웃과 영어 미러에 **처음 5분 기여 흐름 / first 5-minute contribution flow** 문구를 추가.
- `docs/README_TOP_CALLOUTS.md` 원본 문안에도 같은 5분 흐름 문구를 반영.
- `templates/scripts/validate_template.py` 강화:
  - README에 `처음 5분 기여 흐름` / `first 5-minute contribution flow` 문구가 없으면 실패하도록 검증 추가.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- README 상단 5분 흐름을 `examples/quickstart.md`와 직접 연결해, README를 떠나지 않고도 첫 복붙 명령으로 내려가게 만들기.

## 실행 @ 09:40 UTC (cron)

### 계획
- README 상단 5분 흐름에서 quickstart 예시로 바로 이어지는 링크/문안을 실제로 만든다.
- 템플릿 검증 스크립트도 같은 quickstart 연결성을 요구하도록 맞춘다.

### 변경 사항
- `examples/quickstart.md`에 README의 **처음 5분 기여 흐름 / first 5-minute contribution flow**를 직접 참조하는 안내 문구 추가.
- `examples/quickstart.md`에 **Copyable first command**와 **Next reading step** 섹션을 추가해 첫 검증 명령과 다음 문서 이동 경로를 명확히 함.
- `README.md` 상단 콜아웃의 5분 흐름 문구에 `examples/quickstart.md` 연결 사실을 1줄 반영.
- `templates/scripts/validate_template.py` 강화:
  - `examples/quickstart.md`를 필수 파일로 추가
  - quickstart 문서의 5분 흐름/영어 미러/복붙 명령/다음 읽기 단계 마커를 검증하도록 확장

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- `examples/quickstart.md`에서 `examples/pr-evidence-mini-walkthrough.md`까지 이어지는 1분짜리 "PR 증빙 복붙 예시" 링크를 추가해 첫 기여 종료 경로를 더 짧게 만들기.

## 실행 @ 09:50 UTC (cron)

### 계획
- README 상단 5분 흐름을 quickstart 이후 PR 증빙 워크스루까지 더 짧게 연결한다.
- 템플릿 검증 스크립트가 이 온보딩 연결성을 실제로 강제하도록 맞춘다.

### 변경 사항
- `README.md`에 첫 5분 기여 흐름과 병기 체크리스트/워크스루 연결 문구를 보강했다.
- `examples/quickstart.md`와 `templates/scripts/validate_template.py`를 업데이트해 quickstart -> 체크리스트 -> PR 증빙 워크스루 흐름과 한/영 마커를 함께 검증하도록 확장했다.
- 신규 문서(`docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`, `docs/README_TOP_CALLOUTS.md`, `examples/pr-evidence-mini-walkthrough.md`)를 포함한 온보딩 동선을 실제 저장소 구조에 반영했다.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- `examples/quickstart.md`에서 `examples/pr-evidence-mini-walkthrough.md`로 바로 점프하는 1분짜리 PR 증빙 복붙 링크/섹션을 추가해 첫 기여 종료 경로를 더 짧게 만들기.


## 실행 @ 10:20 UTC (cron)

### 계획
- README 상단을 프로젝트 소개/가치/사용자/빠른 시작 중심으로 더 선명하게 만들고, 기여 운영 가이드는 뒤로 내린다.
- 검증 스크립트도 같은 랜딩 구조를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md` 상단에 **추천 시작 경로 / Recommended starting paths** 섹션을 추가해 탐색용 경로와 즉시 기여 경로를 분리했다.
- 기여자 중심의 **상단 핵심 콜아웃 / Top contributor callouts** 섹션을 하단의 체크리스트 근처로 이동해, README 첫 화면이 프로젝트 소개/가치/카테고리/빠른 시작에 더 집중되도록 재배치했다.
- `templates/scripts/validate_template.py`를 업데이트해 새 랜딩 섹션 존재를 자동 검증한다.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- README 상단의 추천 시작 경로를 실제 카테고리 예시 카드/표현으로 더 압축해, 첫 방문자가 30초 안에 진입 경로를 고르게 만들기.

## 실행 @ 10:30 UTC (cron)

### 계획
- README 상단의 추천 시작 경로를 30초 선택용 카드 형태로 압축한다.
- 검증 스크립트도 같은 카드 구조를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md`의 **추천 시작 경로 / Recommended starting paths** 아래에 **빠른 선택 카드 / Quick chooser cards** 섹션 추가.
  - `탐색형 / Explorer path`
  - `기여형 / Contributor path`
- 각 카드에 목적/시작/다음 이동을 한눈에 보이도록 정리해, 첫 방문자가 소개 탐색 경로와 즉시 기여 경로를 더 빠르게 고르게 했다.
- `templates/scripts/validate_template.py`를 업데이트해 새 카드 섹션과 양쪽 경로 라벨이 없으면 실패하도록 검증 강화.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- 빠른 선택 카드 아래에 실제 대표 카테고리별 바로가기(예: onboarding / evidence / governance)를 더 짧은 링크 묶음으로 추가해 첫 클릭 수를 줄이기.

## 실행 @ 10:40 UTC (cron)

### 계획
- README 상단 소개 구조를 유지하면서 신규 기여자의 첫 5분 동선을 더 전면에 노출한다.
- validator가 시간 박스 기반 온보딩 흐름까지 실제로 강제하도록 맞춘다.

### 변경 사항
- `README.md` quick start 상단에 **처음 5분 기여 흐름 / First 5-minute contribution flow** 섹션 추가.
- `templates/scripts/validate_template.py`에 해당 시간 박스 흐름(한/영 step marker) 검증 규칙 추가.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- CONTRIBUTING/quickstart/examples 간 링크 중복을 줄이면서 README 상단 카드형 진입점을 더 압축.


## 실행 @ 11:40 UTC (cron)

### 계획
- README 소개 우선 구조를 문서 규칙으로 명시하고 자동 검증까지 연결한다.
- 기여 문서에도 같은 랜딩 우선순위 기준을 연결한다.

### 변경 사항
- `docs/README_INFORMATION_ARCHITECTURE.md` 신규 추가.
  - README 첫 화면에서 소개/대상 사용자/제공 가치/대표 카테고리/빠른 시작을 우선 노출해야 한다는 기준을 한/영으로 문서화.
- `templates/scripts/validate_template.py` 강화:
  - 새 정보 구조 가이드 문서를 필수 파일/병기 마커 검증 대상에 추가.
  - `실무용 기여 체크리스트`, `Roadmap summary`가 `Quick start` 위로 올라오면 실패하도록 intro-first 검증 추가.
- `README.md`, `CONTRIBUTING.md`, `docs/README_TOP_CALLOUTS.md`에 새 정보 구조 가이드 링크를 연결.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 새 문서를 추가하면서 README 상단 콜아웃 동기화 검증이 한 번 실패했고, 상단 콜아웃에도 동일 링크를 연결해 드리프트를 해소함.

### 다음 실행 우선순위
- README 상단 대표 카테고리 블록을 카드형/선택형 구조로 더 다듬고, 예시 링크 밀도를 높여 첫 방문자 스캔 시간을 더 줄이기.

## 실행 @ 13:30 UTC (cron)

### 계획
- README 상단 소개 우선 구조를 유지한 채 대표 카테고리의 첫 클릭 수를 더 줄인다.
- validator가 새 상단 진입 블록을 실제로 강제하도록 맞춘다.

### 변경 사항
- `README.md` 상단 랜딩 구간에 **카테고리 바로가기 / Category jump links** 섹션 추가.
  - 온보딩 / 증빙 예시 / 운영 기준으로 바로 이동하는 한·영 링크 묶음을 노출했다.
- `templates/scripts/validate_template.py` 강화:
  - 새 카테고리 바로가기 섹션 헤더를 필수 마커에 추가.
  - onboarding / evidence / governance 진입점 3종이 README 상단에 없으면 실패하도록 검증 규칙을 추가했다.

### 검증
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (`baseline + bilingual markers are present`)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- 카테고리 바로가기와 추천 시작 경로 카드를 더 압축해서, README 상단에서 역할별(탐색/기여/운영) 진입점이 한 번에 보이도록 정리.

## 실행 @ 15:50 UTC (cron)

### 계획
- README 상단에서 탐색/기여/운영 역할별 진입 경로를 더 압축해 첫 클릭 수를 줄인다.
- intro-first README 구조가 유지되도록 validator/test에도 같은 규칙을 반영한다.

### 변경 사항
- `README.md`에 **역할별 30초 선택 카드 / 30-second role chooser cards** 섹션 추가.
  - Explorer / Contributor / Operator별 첫 30초 이동 경로를 한·영으로 압축 노출.
- `templates/scripts/validate_template.py`를 업데이트해 새 역할 카드 섹션과 contributor 경로 마커를 요구하도록 검증 강화.
- `tests/test_validate_template.py`에 역할 카드 누락 시 실패하는 회귀 테스트를 추가.

### 검증
- `python3 -m unittest discover -s tests -p 'test_*.py' -v`
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS** (15 tests + template validation pass)

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- 역할별 30초 선택 카드와 `docs/README_FAST_PATHS.md`를 더 강하게 연결해, README 상단만 읽고도 바로 다음 문서로 점프하게 만들기.

## 실행 @ 19:10 UTC (cron)

### 계획
- README 상단 소개 우선 구조를 유지하면서도 첫 행동 버튼을 더 압축해 노출한다.
- validator/test도 같은 상단 버튼 구조를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md` 상단에 **핵심 시작 버튼 / Core start buttons** 섹션 추가.
  - 프로젝트 이해 / 즉시 검증 / 첫 PR 준비 / 운영 가이드 열기 경로를 한·영으로 압축 노출했다.
- `docs/README_FAST_PATHS.md`에 새 상단 버튼 섹션이 Explorer / Contributor / Operator 경로의 압축판임을 명시했다.
- `templates/scripts/validate_template.py`를 업데이트해 새 상단 버튼 섹션과 필수 링크 묶음을 검증하도록 강화했다.
- `tests/test_validate_template.py`에 상단 버튼 필수 링크 누락 시 실패하는 회귀 테스트를 추가했다.

### 검증
- `python3 -m unittest discover -s tests -q`
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS**

### 막힘/리스크
- 처음에는 새 섹션을 `프로젝트 시작 맵` 내부에 끼워 넣으면서 기존 handoff bullet 검증이 깨졌다. 상단 버튼 섹션을 시작 맵 뒤로 재배치해 intro-first 흐름과 기존 검증을 모두 유지했다.

### 다음 실행 우선순위
- 핵심 시작 버튼을 카테고리 바로가기/역할 카드와 더 강하게 연결해, README 첫 화면에서 역할별 첫 클릭 수를 한 번 더 줄이기.

## 실행 @ 19:45 UTC (cron)

### 계획
- README 상단 소개 우선 구조를 유지하면서 역할별 첫 클릭 경로를 더 압축해 노출한다.
- validator/test도 같은 상단 번들 구조를 실제로 요구하도록 맞춘다.

### 변경 사항
- `README.md` 상단에 **역할별 첫 클릭 묶음 / Role-based first-click bundles** 섹션 추가.
  - Explorer / Contributor / Operator별로 첫 클릭, 두 번째 클릭, 도착 문서를 한/영으로 압축 노출했다.
- `templates/scripts/validate_template.py`를 업데이트해 새 상단 번들 섹션과 `도착 문서 / landing doc` 마커를 검증하도록 강화했다.
- `tests/test_validate_template.py`에 상단 번들 누락 시 실패하는 회귀 케이스를 보강했다.

### 검증
- `python3 -m unittest discover -s tests -q`
- `python3 templates/scripts/validate_template.py`
- 결과: **PASS**

### 막힘/리스크
- 없음.

### 다음 실행 우선순위
- 역할별 첫 클릭 묶음과 `docs/README_FAST_PATHS.md`를 더 직접적으로 연결해, README 첫 화면에서 역할별 다음 문서 점프를 한 단계 더 줄이기.
