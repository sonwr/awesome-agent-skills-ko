#!/usr/bin/env python3
"""저장소 기본 품질 검증 스크립트 / Baseline repository quality validator.

한국어 기본 원칙을 유지하면서, 핵심 문서의 한/영 병기 여부를 점검한다.
Keep Korean-first docs while checking that key bilingual sections are present.
"""

from pathlib import Path
import re
import sys

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/ROADMAP.md",
    "docs/CURATION_POLICY.md",
    "docs/TEMPLATE_STANDARD.md",
    "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
    "docs/README_TOP_CALLOUTS.md",
    "docs/README_AUDIENCE_VALUE_MAP.md",
    "docs/README_PROJECT_VALUE_QUICKCHECK.md",
    "docs/README_PROJECT_VALUE_LADDER.md",
    "docs/README_PROJECT_INTRO_60S.md",
    "docs/README_FIRST_SCREEN_MAP.md",
    "docs/README_PROJECT_OVERVIEW_FAQ.md",
    "docs/README_VALUE_PROOF_POINTS.md",
    "docs/README_LANDING_QUICKSTART_MAP.md",
    "docs/README_PROJECT_INTRO_BLUEPRINT.md",
    "docs/README_PROJECT_POSITIONING.md",
    "docs/README_PROJECT_STARTER_PACK.md",
    "docs/README_PROJECT_FIRST_LOOK.md",
    "docs/README_PROJECT_QUICKSTART_PERSONAS.md",
    "docs/README_FIRST_ACTION_MATRIX.md",
    "docs/README_FIRST_VISIT_PACK.md",
    "docs/README_FIRST_VISITOR_PROMISES.md",
    "docs/README_FIRST_VISITOR_ROUTES.md",
    "docs/README_FIRST_SCREEN_DECISION_TREE.md",
    "docs/README_ROLE_STARTERS.md",
    "docs/README_WHO_STARTS_WHERE.md",
    "docs/README_INTRO_FIRST_MAINTENANCE_LOOP.md",
    "docs/PROJECT_OVERVIEW.md",
    "docs/PROJECT_ENTRY_PATHS.md",
    "docs/PROJECT_DIRECTION.md",
    "docs/README_INFORMATION_ARCHITECTURE.md",
    "docs/README_FIRST_SCREEN_CHECKLIST.md",
    "docs/README_FIRST_SCREEN_SCRIPT.md",
    "docs/README_FIRST_SCREEN_WIREFRAME.md",
    "docs/README_USER_JOURNEYS.md",
    "docs/README_FAST_PATHS.md",
    "examples/pr-evidence-mini-walkthrough.md",
    "examples/quickstart.md",
]


BILINGUAL_SECTION_MARKERS = {
    "README.md": [
        "English mirror:",
        "## 프로젝트 소개 / Project overview",
        "## 프로젝트 한눈에 보기 / Project at a glance",
        "## 빠른 적합성 체크 / Quick fit check",
        "## 핵심 가치 카드 / Value cards",
        "## 첫 화면 30초 요약 / 30-second landing summary",
        "## 이 저장소를 읽는 법 / How to read this repo",
        "## 프로젝트 스냅샷 / Project snapshot",
        "## 처음 방문 FAQ / First-time visitor FAQ",
        "## 10초 시작 선택 / 10-second start chooser",
        "## 프로젝트 시작 맵 / Project start map",
        "## 핵심 시작 버튼 / Core start buttons",
        "## 역할별 첫 클릭 묶음 / Role-based first-click bundles",
        "## 1분 빠른 시작 / 1-minute quick start",
        "## 역할별 첫 명령 / First command by role",
        "## 역할별 첫 성과 / First wins by role",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 대표 시작 예시 / Featured starter examples",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 빠른 시작 / Quick start",
        "## 한눈에 보는 3단계 시작 / 3-step start path",
        "## 첫 방문자 체크 / First-visit chooser",
        "## 30초 적합성 체크 / 30-second fit check",
        "## 빠른 적합성 체크 / Quick fit check",
        "## 이 저장소가 특히 맞는 경우 / Best-fit scenarios",
        "## 이 저장소가 덜 맞는 경우 / Not-for scenarios",
        "## 카테고리 바로가기 / Category jump links",
        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
        "## 역할별 1클릭 다음 문서 / Role-based 1-click next docs",
        "## 역할별 바로 열 문서 / Role-based first-open docs",
        "탐색형 / Explorer",
        "기여형 / Contributor",
        "운영형 / Operator",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 대표 활용 시나리오 / Featured use cases",
        "## 추천 시작 경로 / Recommended starting paths",
        "### 빠른 선택 카드 / Quick chooser cards",
        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
        "탐색형 / Explorer path",
        "기여형 / Contributor path",
        "운영형 / Operator path",
        "## 더 읽기 / Learn more",
        "## 상단 핵심 콜아웃 / Top contributor callouts",
        "최소 증빙 3종 필수",
        "Document blockers with the next-run priority",
        "처음 5분 기여 흐름",
        "first 5-minute contribution flow",
    ],
    "CONTRIBUTING.md": [
        "# 기여 가이드 / Contributing",
        "## 기여 원칙 / Principles",
        "## PR 필수 항목 / Pull request requirements",
        "## 리뷰 체크리스트 / Review checklist",
        "## 첫 기여 전에 볼 문서 / Read these before the first PR",
        "English mirror:",
        "README 상단 랜딩 구조",
        "README landing order",
    ],
    "docs/PROJECT_ENTRY_PATHS.md": [
        "프로젝트 진입 경로 / Project entry paths",
        "## 30초 탐색 경로 / 30-second exploration path",
        "## 5분 기여 경로 / 5-minute contribution path",
        "## 운영 문서 경로 / Governance follow-up path",
        "English mirror:",
    ],
    "docs/README_PROJECT_INTRO_BLUEPRINT.md": [
        "README 소개형 상단 설계 청사진 / README intro-first blueprint",
        "## 상단에 먼저 보여줄 것 / What should appear first",
        "## 뒤로 미룰 것 / What should move lower",
        "## English mirror",
    ],
    "docs/README_FIRST_VISIT_PACK.md": [
        "README 첫 방문 스타터 팩 / README first-visit pack",
        "## 첫 60초에 볼 것 / What to open in the first 60 seconds",
        "## 역할별 첫 묶음 / Role-based starter bundles",
        "## English mirror",
    ],
    "docs/README_FIRST_VISITOR_PROMISES.md": [
        "README 첫 방문 약속 / README first-visitor promises",
        "## 한국어 기준 / Korean-first promises",
        "## English mirror",
        "무엇을 찾는 저장소인가?",
        "What kind of repo is this?",
    ],
    "docs/README_FIRST_VISITOR_ROUTES.md": [
        "README 첫 방문 경로 / README first-visitor routes",
        "## 한국어 기준 / Korean-first routes",
        "## English mirror",
        "Explore first",
        "Validate now",
        "Contribute now",
        "Audit the structure",
    ],
    "docs/README_PROJECT_POSITIONING.md": [
        "README 프로젝트 포지셔닝 / README project positioning",
        "## 포지셔닝 문장 / Positioning statement",
        "## 첫 화면에서 먼저 약속할 가치 / Value promises to show first",
        "## 먼저 보이고 뒤로 내릴 것 / What stays first vs lower",
        "English mirror:",
    ],
    "docs/README_PROJECT_STARTER_PACK.md": [
        "README 프로젝트 스타터 팩 / README project starter pack",
        "## 한국어 기준 / Korean-first pack",
        "## English mirror",
        "## 유지 규칙 / Maintenance rule",
        "Project intro",
        "Quick start",
    ],
    "docs/README_PROJECT_VALUE_LADDER.md": [
        "README 프로젝트 가치 사다리 / README project value ladder",
        "## 한국어 기준 / Korean-first ladder",
        "## English mirror",
        "## 유지 규칙 / Maintenance rule",
        "Project intro",
        "Governance handoff",
    ],
    "docs/README_PROJECT_FIRST_LOOK.md": [
        "README 프로젝트 첫인상 가이드 / README project first-look guide",
        "## 한국어 기준 / Korean-first guide",
        "## English mirror",
        "## 유지 규칙 / Maintenance rule",
        "What does this project do?",
        "Where does governance go?",
    ],
    "docs/README_PROJECT_QUICKSTART_PERSONAS.md": [
        "README 소개형 페르소나 퀵스타트 / README intro-first persona quickstart",
        "## 한국어 기준 / Korean-first guide",
        "## English mirror",
        "### 탐색형 / Explorer",
        "### Contributor",
        "## 유지 규칙 / Maintenance rule",
    ],
    "docs/README_ROLE_STARTERS.md": [
        "README 역할별 시작 지도 / README role-based starters",
        "## 한국어 기준 / Korean-first map",
        "### 탐색형 / Explorer",
        "### 기여형 / Contributor",
        "### 운영형 / Operator",
        "## English mirror",
    ],
    "docs/README_WHO_STARTS_WHERE.md": [
        "README 누가 어디서 시작하나 / README who starts where",
        "## 한국어 기준 / Korean-first routing",
        "### 탐색형 / Explorer",
        "### 기여형 / Contributor",
        "### 운영형 / Operator",
        "## English mirror",
    ],
    "docs/README_INFORMATION_ARCHITECTURE.md": [
        "README 정보 구조 가이드 / README information architecture guide",
        "## 상단 우선순위 / Top-of-page priorities",
        "## 뒤로 보내는 내용 / What belongs lower in the page",
        "## 검증 기준 / Validation rule",
        "English mirror:",
    ],
    "docs/README_FIRST_SCREEN_CHECKLIST.md": [
        "README 첫 화면 체크리스트 / README first-screen checklist",
        "## 한국어 체크 / Korean checks",
        "## English mirror",
        "프로젝트 소개 → 대상 사용자 → 제공 가치",
        "overview -> audience -> value",
    ],
    "docs/README_FIRST_SCREEN_MAP.md": [
        "README 첫 화면 지도 / README first-screen map",
        "## 한국어 기준 / Korean-first map",
        "## English mirror",
        "프로젝트 소개 / Project intro",
        "Governance handoff",
    ],
    "docs/README_FIRST_SCREEN_SCRIPT.md": [
        "README 첫 화면 스크립트 / README first-screen script",
        "English mirror:",
        "## 첫 화면 60초 스크립트 / 60-second first-screen script",
        "## README 상단에서 바로 보여줄 문장 유형 / Sentence types to keep near the top",
        "## 뒤로 내려도 되는 내용 / What can move lower",
    ],
    "docs/README_FIRST_SCREEN_WIREFRAME.md": [
        "README 첫 화면 와이어프레임 / README first-screen wireframe",
        "## 상단 1스크린 구조 / First-screen structure",
        "## 아래로 미루는 내용 / What moves lower",
        "## 유지 점검 질문 / Maintenance prompts",
        "English mirror:",
    ],
    "docs/README_USER_JOURNEYS.md": [
        "README 사용자 여정 / README user journeys",
        "## 탐색형 방문자 / Explorer journey",
        "## 기여형 방문자 / Contributor journey",
        "## 운영형 방문자 / Operator journey",
        "English mirror:",
    ],
    "docs/README_INTRO_FIRST_MAINTENANCE_LOOP.md": [
        "README 소개 우선 유지 루프 / README intro-first maintenance loop",
        "## 1) 소개 먼저 확인 / Confirm the intro first",
        "## 2) 경로를 끊지 않기 / Preserve the handoff path",
        "## 3) 수정 후 검증 / Validate after edits",
        "English mirror:",
    ],
    "docs/README_FAST_PATHS.md": [
        "README 빠른 진입 경로 / README fast paths",
        "## 탐색형 60초 경로 / Explorer 60-second path",
        "## 기여형 60초 경로 / Contributor 60-second path",
        "## 운영형 60초 경로 / Operator 60-second path",
        "## README 역할 카드와의 연결 / How this maps to README role cards",
        "## 1-click handoff pairs / 한 번에 여는 다음 문서",
        "English mirror:",
    ],
    "docs/README_TOP_CALLOUTS.md": [
        "README 상단 콜아웃 문안 / README top callout copy",
        "English mirror:",
    ],
    "docs/README_AUDIENCE_VALUE_MAP.md": [
        "README 대상 사용자-가치 맵 / README audience-value map",
        "## 한국어 기준 / Korean-first map",
        "## English mirror",
        "탐색형 방문자",
        "기여형 방문자",
        "운영형 방문자",
        "One-line rule",
        "Contributors",
        "Operators",
    ],
    "docs/README_VALUE_PROOF_POINTS.md": [
        "README 가치 증명 포인트 / README value proof points",
        "## 한국어 기준 / Korean-first proof points",
        "## English mirror",
        "One-line project value",
        "Immediate audience benefit",
        "Runnable promise",
        "Governance later",
    ],
    "docs/README_LANDING_QUICKSTART_MAP.md": [
        "README 랜딩 빠른 시작 맵 / README landing quick-start map",
        "## 첫 화면 우선순위 / First-screen priorities",
        "## README 상단 체크 질문 / README top-check questions",
        "## 첫 화면 유지 루프 / First-screen maintenance loop",
        "python3 templates/scripts/validate_template.py",
        "docs/README_FIRST_SCREEN_CHECKLIST.md",
        "English mirror:",
    ],
    "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md": [
        "## 한국어 체크리스트 (Primary)",
        "## English mirror",
        "## 자동 검증 명령 / Validation commands",
        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
        "예상 3분 이내",
        "Estimated within 3 minutes",
        "## 리뷰어 메모 템플릿 / Reviewer note template",
        "## 반복 작업 방지 로그 / Anti-repeat run log",
    ],
    "examples/pr-evidence-mini-walkthrough.md": [
        "## 목적 (한국어)",
        "## Purpose (English)",
        "## PR 코멘트 예시 (한국어)",
        "## PR comment example (English)",
    ],
    "examples/quickstart.md": [
        "처음 5분 기여 흐름",
        "first 5-minute contribution flow",
        "## Copyable first command",
        "## Next reading step",
        "## 1분 PR 증빙 점프 / 1-minute PR evidence jump",
        "examples/pr-evidence-mini-walkthrough.md",
        "English mirror:",
    ],
}


def _check_required_files(root: Path) -> list[str]:
    return [f for f in REQUIRED_FILES if not (root / f).exists()]


def _extract_section(text: str, heading: str) -> str:
    pattern = rf"(?ms)^##\s*{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s|\Z)"
    match = re.search(pattern, text)
    return match.group("body") if match else ""


def _check_quickstart_validation_command(root: Path) -> list[str]:
    readme_path = root / "README.md"
    if not readme_path.exists():
        return []
    text = readme_path.read_text(encoding="utf-8")
    errors: list[str] = []
    lines = text.splitlines()
    overview_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 프로젝트 소개 / Project overview"), None)
    quickstart_command_line = next((idx for idx, line in enumerate(lines, start=1) if "python3 templates/scripts/validate_template.py" in line), None)
    start_here_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 바로 시작 요약 / Start-here summary"), None)
    if start_here_line is None or start_here_line > 32:
        errors.append(
            "README.md: start-here summary heading must appear within the first 32 lines so the landing area immediately exposes intro/audience/value/categories/quick-start cues"
        )
    if overview_line is None or overview_line > 50:
        errors.append(
            "README.md: project overview heading must appear within the first 50 lines so the README stays project-intro-first even after the compact landing summary blocks"
        )
    top_intro_window = "\n".join(lines[:80])
    top_project_pitch_window = "\n".join(lines[:20])
    first_visit_15s_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 첫 방문 15초 선택 / 15-second first-visit chooser"), None)
    if "에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음" not in top_project_pitch_window or "curated, practical collection of agent skills and runnable templates" not in top_project_pitch_window:
        errors.append(
            "README.md: the first 20 lines must keep the bilingual project pitch (agent-skill curation + runnable templates) so the landing area opens with project value before governance"
        )
    if "좋아 보이는 링크 모음" not in top_intro_window or "not just a link dump" not in top_intro_window:
        errors.append(
            "README.md: the first 80 lines must keep the bilingual 'not just a link dump' value proposition so visitors see the repo is project-intro-first, not governance-first"
        )
    if first_visit_15s_line is None or first_visit_15s_line > 75:
        errors.append(
            "README.md: the 15-second first-visit chooser must appear within the first 75 lines so explore/validate/contribute/audit routes stay visible in the intro-first landing block"
        )
    governance_handoff_window = "\n".join(lines[:40])
    if "운영 문서 위치 / Where governance lives" not in governance_handoff_window or "Governance details live below the landing block" not in governance_handoff_window:
        errors.append(
            "README.md: the first 40 lines must keep a bilingual governance-handoff cue so contribution/operations docs stay explicitly below the intro-first landing block"
        )
    first_action_matrix_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_FIRST_ACTION_MATRIX.md" in line), None)
    if first_action_matrix_line is None or first_action_matrix_line > 45:
        errors.append(
            "README.md: first action matrix link must appear within the first 45 lines so newcomers can pick the best first click without dropping into governance-heavy sections"
        )
    top_summary_markers = [
        "프로젝트 소개 / Project intro",
        "대상 사용자 / Who it helps",
        "대표 가치 / Immediate value",
        "대표 카테고리 / Featured categories",
        "빠른 시작 / Quick start",
    ]
    missing_top_summary_markers = [marker for marker in top_summary_markers if marker not in top_intro_window]
    if missing_top_summary_markers:
        errors.append(
            "README.md: the first 80 lines must keep the start-here summary markers for intro/audience/featured-categories/quick-start -> "
            + ", ".join(missing_top_summary_markers)
        )
    start_here_section = _extract_section(text, "바로 시작 요약 / Start-here summary")
    summary_order_markers = [
        "프로젝트 소개 / Project intro",
        "대상 사용자 / Who it helps",
        "대표 가치 / Immediate value",
        "대표 카테고리 / Featured categories",
        "빠른 시작 / Quick start",
    ]
    summary_order_positions = [start_here_section.find(marker) for marker in summary_order_markers]
    if all(position != -1 for position in summary_order_positions) and summary_order_positions != sorted(summary_order_positions):
        errors.append(
            "README.md: the start-here summary must keep intro -> audience -> immediate value -> featured categories -> quick start order inside the Start-here summary block"
        )
    quick_fit_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 빠른 적합성 체크 / Quick fit check"), None)
    if quick_fit_line is None or quick_fit_line > 110:
        errors.append(
            "README.md: quick fit check must appear within the first 110 lines so best-fit/not-for guidance stays in the intro-first landing block before deeper governance sections"
        )
    if quickstart_command_line is None or quickstart_command_line > 160:
        errors.append(
            "README.md: first validation command must appear within the first 160 lines so visitors can act from the landing screen without deep scrolling"
        )
    role_starter_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_ROLE_STARTERS.md" in line), None)
    intro_60s_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_PROJECT_INTRO_60S.md" in line), None)
    audience_quick_recipes_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_AUDIENCE_QUICK_RECIPES.md" in line), None)
    first_visitor_promises_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_FIRST_VISITOR_PROMISES.md" in line), None)
    first_visitor_routes_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_FIRST_VISITOR_ROUTES.md" in line), None)
    first_screen_decision_tree_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_FIRST_SCREEN_DECISION_TREE.md" in line), None)
    first_screen_quick_proof_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_FIRST_SCREEN_QUICK_PROOF.md" in line), None)
    project_value_quickcheck_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_PROJECT_VALUE_QUICKCHECK.md" in line), None)
    project_value_ladder_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_PROJECT_VALUE_LADDER.md" in line), None)
    if role_starter_line is None or role_starter_line > 90:
        errors.append(
            "README.md: role-based start map link must appear within the first 90 lines so explorer/contributor/operator visitors can branch from the landing block without hitting governance-heavy sections first"
        )
    who_starts_where_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_WHO_STARTS_WHERE.md" in line), None)
    if who_starts_where_line is None or who_starts_where_line > 95:
        errors.append(
            "README.md: who-starts-where routing doc link must appear within the first 95 lines so first-time visitors can see role -> first doc -> first action handoff without dropping into governance-heavy sections"
        )
    featured_use_cases_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 대표 활용 시나리오 / Featured use cases"), None)
    if featured_use_cases_line is None or featured_use_cases_line > 115:
        errors.append(
            "README.md: featured use cases must appear within the first 115 lines so intro-first visitors see representative onboarding / contribution / governance scenarios before deeper navigation"
        )
    three_line_heading = "## 첫 화면 핵심 3줄 / First-screen in 3 lines"
    three_line_section_heading = "첫 화면 핵심 3줄 / First-screen in 3 lines"
    three_line_line = next((idx for idx, line in enumerate(lines, start=1) if three_line_heading in line), None)
    if three_line_line is None or three_line_line > 32:
        errors.append(
            "README.md: first-screen in 3 lines section must appear within the first 32 lines so the landing area explains project intro, audience fit, and quick action before deeper navigation"
        )
    three_line_section = _extract_section(text, three_line_section_heading)
    if (
        "What is this project?" not in three_line_section
        or "Who should start here?" not in three_line_section
        or "What should I do now?" not in three_line_section
        or "python3 templates/scripts/validate_template.py" not in three_line_section
        or "examples/quickstart.md" not in three_line_section
    ):
        errors.append(
            "README.md: first-screen in 3 lines section must summarize project intro, target audience, and immediate quick-start action in Korean/English with the validation command and next doc"
        )
    first_minute_heading = "## 첫 1분에 얻는 결과 / What you get in the first minute"
    first_minute_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == first_minute_heading), None)
    if first_minute_line is None or first_minute_line > 90:
        errors.append(
            "README.md: first-minute outcome section must appear within the first 90 lines so the landing block states immediate value before governance-heavy navigation"
        )
    first_minute_section = _extract_section(text, "첫 1분에 얻는 결과 / What you get in the first minute")
    required_first_minute_markers = [
        "What you know after 1 minute",
        "What you have run after 1 minute",
        "What you open next after 1 minute",
        "python3 templates/scripts/validate_template.py",
        "examples/quickstart.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "docs/README_FAST_PATHS.md",
    ]
    missing_first_minute_markers = [marker for marker in required_first_minute_markers if marker not in first_minute_section]
    if missing_first_minute_markers:
        errors.append(
            "README.md: first-minute outcome section must keep the intro/value/next-doc handoff markers -> "
            + ", ".join(missing_first_minute_markers)
        )
    if intro_60s_line is None or intro_60s_line > 120:
        errors.append(
            "README.md: intro-in-60-seconds doc link must appear within the first 120 lines so first-time visitors can verify the project-intro reading order before deep governance sections"
        )
    featured_use_cases_doc_line = next((idx for idx, line in enumerate(lines, start=1) if "docs/README_FEATURED_USE_CASES.md" in line), None)
    if featured_use_cases_doc_line is None or featured_use_cases_doc_line > 120:
        errors.append(
            "README.md: featured-use-cases doc link must appear within the first 120 lines so intro-first visitors can jump from the landing pitch to representative onboarding / contribution / governance scenarios"
        )
    if audience_quick_recipes_line is None or audience_quick_recipes_line > 120:
        errors.append(
            "README.md: audience quick-recipes doc link must appear within the first 120 lines so role-specific first actions stay visible before governance-heavy sections"
        )
    if first_visitor_promises_line is None or first_visitor_promises_line > 120:
        errors.append(
            "README.md: first-visitor promises doc link must appear within the first 120 lines so the README keeps explicit newcomer value promises near the landing block"
        )
    if first_visitor_routes_line is None or first_visitor_routes_line > 120:
        errors.append(
            "README.md: first-visitor routes doc link must appear within the first 120 lines so newcomers can choose explore/validate/contribute/audit paths without dropping into governance-heavy sections first"
        )
    if first_screen_quick_proof_line is None or first_screen_quick_proof_line > 120:
        errors.append(
            "README.md: first-screen quick-proof doc link must appear within the first 120 lines so contributors can justify the intro-first landing contract without dropping into governance-heavy docs first"
        )
    if project_value_quickcheck_line is None or project_value_quickcheck_line > 120:
        errors.append(
            "README.md: project value quick-check doc link must appear within the first 120 lines so the intro/audience/value/examples/quick-start landing contract stays reusable near the top"
        )
    if project_value_ladder_line is None or project_value_ladder_line > 120:
        errors.append(
            "README.md: project value ladder doc link must appear within the first 120 lines so the README keeps the intro -> audience -> value -> examples -> quick-start promise visible near the landing block"
        )

    top_order_window = "\n".join(lines[:140])
    start_here_anchor = top_order_window.find("## 바로 시작 요약 / Start-here summary")
    ordered_intro_window = top_order_window[start_here_anchor:] if start_here_anchor >= 0 else top_order_window
    top_order_markers = [
        "프로젝트 소개 / Project intro",
        "대상 사용자 / Who it helps",
        "대표 가치 / Immediate value",
        "대표 카테고리 / Featured categories",
        "빠른 시작 / Quick start",
    ]
    top_order_positions = [ordered_intro_window.find(marker) for marker in top_order_markers]
    if any(position < 0 for position in top_order_positions):
        errors.append(
            "README.md: the first 140 lines must keep overview -> audience -> value -> featured categories -> quick start markers visible so the landing page stays project-intro-first"
        )
    elif top_order_positions != sorted(top_order_positions):
        errors.append(
            "README.md: the first 140 lines must keep overview -> audience -> value -> featured categories -> quick start in order so intro-first readers do not hit governance detours first"
        )

    for required_heading in [
        "## 바로 시작 요약 / Start-here summary",
        "## 프로젝트 소개 / Project overview",
        "## 프로젝트 한눈에 보기 / Project at a glance",
        "## 빠른 적합성 체크 / Quick fit check",
        "## 이 저장소를 읽는 법 / How to read this repo",
        "## 프로젝트 스냅샷 / Project snapshot",
        "## 처음 방문 FAQ / First-time visitor FAQ",
        "## 10초 시작 선택 / 10-second start chooser",
        "## 프로젝트 시작 맵 / Project start map",
        "## 핵심 시작 버튼 / Core start buttons",
        "## 역할별 첫 클릭 묶음 / Role-based first-click bundles",
        "## 1분 빠른 시작 / 1-minute quick start",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 대표 시작 예시 / Featured starter examples",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 한눈에 보는 3단계 시작 / 3-step start path",
        "## 첫 방문자 체크 / First-visit chooser",
        "## 30초 적합성 체크 / 30-second fit check",
        "## 빠른 적합성 체크 / Quick fit check",
        "탐색형 / Explorer",
        "기여형 / Contributor",
        "운영형 / Operator",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 대표 활용 시나리오 / Featured use cases",
        "## 추천 시작 경로 / Recommended starting paths",
        "### 빠른 선택 카드 / Quick chooser cards",
        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
    ]:
        if required_heading not in text:
            errors.append(f"README.md: missing landing-page heading {required_heading}")
    if "Jump to onboarding" not in text or "Jump to evidence examples" not in text or "Jump to governance docs" not in text:
        errors.append(
            "README.md: category jump links must expose onboarding/evidence/governance entry points in Korean/English near the landing section"
        )
    quickstart_followup_section = re.search(
        r"(?ms)^###\s*빠른 시작 후 바로 볼 문서 / What to open right after quick start\s*$\n(?P<body>.*?)(?=^##\s|^###\s|\Z)",
        text,
    )
    if quickstart_followup_section is None:
        errors.append(
            "README.md: missing quick-start follow-up section that maps the first command to the next three docs"
        )
    else:
        quickstart_followup_body = quickstart_followup_section.group("body")
        quickstart_followup_line = next(
            (idx for idx, line in enumerate(lines, start=1) if line.strip() == "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start"),
            None,
        )
        learn_more_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 더 읽기 / Learn more"), None)
        deeper_ops_line = next(
            (idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 운영/기여 상세 안내 / Deeper contributor and operations guide"),
            None,
        )
        if quickstart_followup_line is None or quickstart_followup_line > 560:
            errors.append(
                "README.md: quick-start follow-up section must appear within the first 560 lines so the landing page keeps next-doc guidance above long-form governance details"
            )
        if learn_more_line is not None and quickstart_followup_line is not None and quickstart_followup_line > learn_more_line:
            errors.append(
                "README.md: quick-start follow-up section must appear before Learn more so next-doc guidance stays above supporting references"
            )
        if deeper_ops_line is not None and quickstart_followup_line is not None and quickstart_followup_line > deeper_ops_line:
            errors.append(
                "README.md: quick-start follow-up section must appear before the deeper contributor/operations guide so intro-first flow stays intact"
            )
        required_followup_markers = [
            "examples/quickstart.md",
            "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
            "examples/pr-evidence-mini-walkthrough.md",
            "English mirror:",
        ]
        missing_followup_markers = [marker for marker in required_followup_markers if marker not in quickstart_followup_body]
        if missing_followup_markers:
            errors.append(
                "README.md: quick-start follow-up section must keep the next-doc trio and English mirror -> "
                + ", ".join(missing_followup_markers)
            )
    quick_chooser_section = _extract_section(text, "10초 시작 선택 / 10-second start chooser")
    required_quick_chooser_markers = [
        "python3 templates/scripts/validate_template.py",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/quickstart.md",
        "docs/README_FAST_PATHS.md",
        "docs/CURATION_POLICY.md",
        "English mirror:",
    ]
    missing_quick_chooser_markers = [marker for marker in required_quick_chooser_markers if marker not in quick_chooser_section]
    if missing_quick_chooser_markers:
        errors.append(
            "README.md: 10-second start chooser must keep intro-first jump links for execution/contribution/governance -> "
            + ", ".join(missing_quick_chooser_markers)
        )

    recommended_paths_section = _extract_section(text, "추천 시작 경로 / Recommended starting paths")
    if "Explorer path" not in recommended_paths_section or "Contributor path" not in recommended_paths_section or "Operator path" not in recommended_paths_section:
        errors.append(
            "README.md: recommended starting paths must expose bilingual explorer/contributor/operator path cards near the landing block"
        )
    if "python3 templates/scripts/validate_template.py" not in recommended_paths_section or "docs/CURATION_POLICY.md" not in recommended_paths_section:
        errors.append(
            "README.md: recommended starting paths must include the first validation command and the governance follow-up path for contributor/operator visitors"
        )

    if "## 역할별 한 줄 진입점 / Role-based one-line entry points" not in text or "**탐색형 / Explorer**" not in text or "**기여형 / Contributor**" not in text or "**운영형 / Operator**" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based one-line entry points for explorer/contributor/operator paths"
        )
    if "## 역할별 첫 클릭 묶음 / Role-based first-click bundles" not in text or "도착 문서" not in text or "landing doc" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based first-click bundles so each visitor can see first click, second click, and landing doc near the top"
        )
    role_first_click_bundle_section = _extract_section(text, "역할별 첫 클릭 묶음 / Role-based first-click bundles")
    required_role_anchor_markers = [
        "docs/README_FAST_PATHS.md#탐색형-60초-경로--explorer-60-second-path",
        "docs/README_FAST_PATHS.md#기여형-60초-경로--contributor-60-second-path",
        "docs/README_FAST_PATHS.md#운영형-60초-경로--operator-60-second-path",
        "빠른 경로 앵커",
        "fast-path anchor",
    ]
    missing_role_anchor_markers = [marker for marker in required_role_anchor_markers if marker not in role_first_click_bundle_section]
    if missing_role_anchor_markers:
        errors.append(
            "README.md: role-based first-click bundles must include bilingual fast-path anchors back into docs/README_FAST_PATHS.md -> "
            + ", ".join(missing_role_anchor_markers)
        )
    if "## 역할별 바로 점프 / Role-based instant jumps" not in text or "docs/README_FAST_PATHS.md#탐색형-60초-경로--explorer-60-second-path" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based instant jumps that deep-link explorer/contributor/operator visitors into docs/README_FAST_PATHS.md"
        )
    if "## 1분 빠른 시작 / 1-minute quick start" not in text or "CONTRIBUTING.md" not in text:
        errors.append(
            "README.md: landing section must include a bilingual 1-minute quick start block with validation, next-doc, and contributing-guide handoff cues"
        )
    featured_examples_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 대표 시작 예시 / Featured starter examples"), None)
    if featured_examples_line is None or featured_examples_line > 265:
        errors.append(
            "README.md: featured starter examples must appear within the first 265 lines so intro-first readers see runnable examples before deep governance details"
        )
    featured_examples_section = _extract_section(text, "대표 시작 예시 / Featured starter examples")
    required_featured_example_markers = [
        "python3 templates/scripts/validate_template.py",
        "examples/quickstart.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/pr-evidence-mini-walkthrough.md",
        "docs/README_FIRST_SCREEN_CHECKLIST.md",
        "docs/README_AUDIENCE_VALUE_MAP.md",
        "docs/README_PROJECT_INTRO_60S.md",
    "docs/README_FIRST_SCREEN_MAP.md",
        "docs/README_PROJECT_OVERVIEW_FAQ.md",
        "English mirror:",
    ]
    missing_featured_example_markers = [marker for marker in required_featured_example_markers if marker not in featured_examples_section]
    if missing_featured_example_markers:
        errors.append(
            "README.md: featured starter examples must keep validation/contribution/audit example links with an English mirror -> "
            + ", ".join(missing_featured_example_markers)
        )
    if "## 역할별 첫 명령 / First command by role" not in text or "first command" not in text or "docs/README_FIRST_SCREEN_CHECKLIST.md" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based first command by role cues so explorer/contributor/operator visitors can see one command plus the next doc immediately"
        )
    if "## 역할별 1클릭 다음 문서 / Role-based 1-click next docs" not in text or "docs/README_FAST_PATHS.md" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based 1-click next docs linked back to docs/README_FAST_PATHS.md so intro-first handoff stays explicit"
        )
    if "## 역할별 바로 열 문서 / Role-based first-open docs" not in text or "docs/README_FAST_PATHS.md" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based first-open docs so visitors can jump into explorer/contributor/operator paths in one click"
        )
    if "## 역할별 30초 선택 카드 / 30-second role chooser cards" not in text or "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md" not in text:
        errors.append(
            "README.md: landing section must include bilingual 30-second role chooser cards so explorer/contributor/operator paths stay compressed near the top"
        )
    if "60-second role guide" not in text or "docs/README_FAST_PATHS.md" not in text:
        errors.append(
            "README.md: landing section must explicitly hand role-based paths off to docs/README_FAST_PATHS.md with a bilingual 60-second role-guide cue"
        )
    role_first_open_section = _extract_section(text, "역할별 바로 열 문서 / Role-based first-open docs")
    required_role_docs = [
        "examples/quickstart.md",
        "docs/PROJECT_OVERVIEW.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/pr-evidence-mini-walkthrough.md",
        "docs/README_FAST_PATHS.md",
        "docs/README_FIRST_SCREEN_CHECKLIST.md",
        "docs/README_FIRST_SCREEN_SCRIPT.md",
        "docs/README_INFORMATION_ARCHITECTURE.md",
        "docs/CURATION_POLICY.md",
    ]
    missing_role_docs = [doc for doc in required_role_docs if doc not in role_first_open_section]
    if missing_role_docs:
        errors.append(
            "README.md: role-based first-open docs must keep explorer/contributor/operator handoff links together -> "
            + ", ".join(missing_role_docs)
        )
    value_cards_section = _extract_section(text, "핵심 가치 카드 / Value cards")
    for required_value_card_marker in [
        "탐색 카드 / Discover",
        "검증 카드 / Validate",
        "기여 카드 / Contribute",
        "python3 templates/scripts/validate_template.py",
        "examples/quickstart.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/pr-evidence-mini-walkthrough.md",
    ]:
        if required_value_card_marker not in value_cards_section:
            errors.append(
                "README.md: value cards must expose bilingual discover/validate/contribute entry points with the first command and follow-up docs near the top -> "
                + required_value_card_marker
            )

    start_here_section = _extract_section(text, "바로 시작 요약 / Start-here summary")
    for required_start_here_marker in [
        "프로젝트 소개 / Project intro",
        "대상 사용자 / Who it helps",
        "대표 가치 / Immediate value",
        "대표 카테고리 / Featured categories",
        "빠른 시작 / Quick start",
        "examples/quickstart.md",
        "English mirror:",
    ]:
        if required_start_here_marker not in start_here_section:
            errors.append(
                "README.md: start-here summary must expose intro/audience/value/categories/quick-start markers in Korean/English near the top -> "
                + required_start_here_marker
            )

    landing_summary_section = _extract_section(text, "첫 화면 30초 요약 / 30-second landing summary")
    for required_landing_summary_marker in [
        "프로젝트 소개 한 줄",
        "Project intro",
        "대상 사용자",
        "Best-fit audience",
        "대표 카테고리",
        "Featured categories",
        "빠른 시작",
        "Quick start",
        "python3 templates/scripts/validate_template.py",
        "examples/quickstart.md",
    ]:
        if required_landing_summary_marker not in landing_summary_section:
            errors.append(
                "README.md: 30-second landing summary must expose intro/audience/categories/quick-start markers in Korean/English near the top -> "
                + required_landing_summary_marker
            )

    if "대표 시작점" not in text or "Landing-page rule" not in text:
        errors.append(
            "README.md: project snapshot must surface representative entry points and the landing-page rule in Korean/English"
        )
    project_snapshot_section = _extract_section(text, "프로젝트 스냅샷 / Project snapshot")
    how_to_read_section = _extract_section(text, "이 저장소를 읽는 법 / How to read this repo")
    project_glance_section = _extract_section(text, "프로젝트 한눈에 보기 / Project at a glance")
    if "누구를 위한 저장소인가요?" not in project_glance_section or "무엇이 바로 되나요?" not in project_glance_section or "어디서 시작하나요?" not in project_glance_section:
        errors.append(
            "README.md: project at a glance must answer audience/immediate action/where-to-start prompts in Korean near the top"
        )
    if "Who is this for?" not in project_glance_section or "What can I do immediately?" not in project_glance_section or "Where do I start?" not in project_glance_section:
        errors.append(
            "README.md: project at a glance must keep English mirror prompts for audience/immediate action/where-to-start near the top"
        )
    if "Step 1" not in how_to_read_section or "Step 2" not in how_to_read_section or "Step 3" not in how_to_read_section or "python3 templates/scripts/validate_template.py" not in how_to_read_section or "examples/quickstart.md" not in how_to_read_section:
        errors.append(
            "README.md: how-to-read section must explain the 3-step intro -> route choice -> first validation flow in Korean/English near the top"
        )
    faq_section = _extract_section(text, "처음 방문 FAQ / First-time visitor FAQ")
    faq_line = next((idx for idx, line in enumerate(lines, start=1) if line.strip() == "## 처음 방문 FAQ / First-time visitor FAQ"), None)
    if faq_line is None or faq_line > 170:
        errors.append(
            "README.md: first-time visitor FAQ must appear within the first 170 lines so newcomers can confirm scope, first action, and contribution handoff before deeper ops sections"
        )
    for required_faq_marker in [
        "Is this just a link list?",
        "What should I do first?",
        "Where are the contribution rules?",
        "python3 templates/scripts/validate_template.py",
        "examples/quickstart.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "CONTRIBUTING.md",
    ]:
        if required_faq_marker not in faq_section:
            errors.append(
                "README.md: first-time visitor FAQ must answer scope/first-action/contribution-rule questions in Korean/English -> "
                + required_faq_marker
            )
            break
    if "python3 templates/scripts/validate_template.py" not in project_snapshot_section or "examples/quickstart.md" not in project_snapshot_section:
        errors.append(
            "README.md: project snapshot must include the first validation command and quickstart doc link so intro-first visitors can act without scrolling"
        )
    featured_starter_examples_section = _extract_section(text, "대표 시작 예시 / Featured starter examples")
    for required_example_marker in [
        "검증부터 시작",
        "기여 준비",
        "운영 점검",
        "Start with validation",
        "Prepare a contribution",
        "Audit the landing flow",
        "examples/quickstart.md",
        "examples/pr-evidence-mini-walkthrough.md",
        "docs/README_FAST_PATHS.md",
    ]:
        if required_example_marker not in featured_starter_examples_section:
            errors.append(
                "README.md: featured starter examples must expose bilingual validate/contribute/audit examples plus next docs near the intro-first landing area"
            )
            break
    project_start_map_section = _extract_section(text, "프로젝트 시작 맵 / Project start map")
    core_start_buttons_section = _extract_section(text, "핵심 시작 버튼 / Core start buttons")
    ordered_start_map_markers = [
        "탐색 먼저 / Explore first",
        "바로 검증 / Validate now",
        "바로 기여 / Contribute now",
        "운영 점검 / Audit the structure",
    ]
    ordered_start_map_positions = [project_start_map_section.find(marker) for marker in ordered_start_map_markers]
    if any(position < 0 for position in ordered_start_map_positions):
        errors.append(
            "README.md: project start map must keep explore/validate/contribute/audit routes together near the intro-first landing block"
        )
    elif ordered_start_map_positions != sorted(ordered_start_map_positions):
        errors.append(
            "README.md: project start map must keep explore -> validate -> contribute -> audit order so first-screen routing stays predictable"
        )
    for required_button in [
        "Understand the project",
        "Validate now",
        "Prepare the first PR",
        "Open governance guides",
        "Category jump links",
        "30-second role chooser cards",
        "Role-based 1-click next docs",
        "python3 templates/scripts/validate_template.py",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/pr-evidence-mini-walkthrough.md",
        "docs/README_FAST_PATHS.md",
        "docs/README_LANDING_QUICKSTART_MAP.md",
        "docs/README_AUDIENCE_VALUE_MAP.md",
    "docs/README_PROJECT_INTRO_60S.md",
    "docs/README_FIRST_SCREEN_MAP.md",
        "docs/CURATION_POLICY.md",
    ]:
        if required_button not in core_start_buttons_section:
            errors.append(
                "README.md: core start buttons must keep bilingual project/validate/contribute/governance entry points near the intro-first landing area"
            )
            break
    required_start_map_markers = [
        "탐색 먼저 / Explore first",
        "바로 검증 / Validate now",
        "바로 기여 / Contribute now",
        "운영 점검 / Audit the structure",
    ]
    missing_start_map_markers = [marker for marker in required_start_map_markers if marker not in project_start_map_section]
    if missing_start_map_markers:
        errors.append(
            "README.md: project start map must keep bilingual explore/validate/contribute/audit handoff bullets near the intro landing -> "
            + ", ".join(missing_start_map_markers)
        )
    project_overview_section = _extract_section(text, "프로젝트 소개 / Project overview")
    if "무엇을 하나요?" not in project_overview_section or "왜 필요한가요?" not in project_overview_section:
        errors.append(
            "README.md: project overview must explain both what the project does and why it matters in Korean near the top"
        )
    if "What does it do?" not in project_overview_section or "Why does it matter?" not in project_overview_section:
        errors.append(
            "README.md: project overview must include English mirror prompts for what the project does and why it matters near the top"
        )
    if "프로젝트 이해" not in text or "Understand the project" not in text:
        errors.append(
            "README.md: 3-step start path must include a Korean/English project-understanding step near the landing section"
        )
    if "첫 검증 실행" not in text or "Run the first validation" not in text:
        errors.append(
            "README.md: 3-step start path must include a Korean/English first-validation step near the landing section"
        )
    if "첫 PR 준비" not in text or "Prepare the first PR" not in text:
        errors.append(
            "README.md: 3-step start path must include a Korean/English first-PR prep step near the landing section"
        )
    if "## 역할별 첫 성과 / First wins by role" not in text or "find the first validation command" not in text:
        errors.append(
            "README.md: landing section must include bilingual first wins by role so explorer/contributor/operator visitors see immediate value before governance details"
        )
    if "이 저장소가 특히 맞는 경우 / Best-fit scenarios" not in text or "Teams that need Korean-first docs with English mirrors" not in text:
        errors.append(
            "README.md: landing section must include bilingual best-fit scenarios so visitors can self-qualify before diving into governance details"
        )
    if "이 저장소가 덜 맞는 경우 / Not-for scenarios" not in text or "plain link archive" not in text:
        errors.append(
            "README.md: landing section must include bilingual not-for scenarios so the README clarifies scope before long-form contribution guidance"
        )
    if "탐색이 먼저인가요?" not in text or "Just exploring first?" not in text:
        errors.append(
            "README.md: first-visit chooser must include a Korean/English exploration decision prompt near the landing section"
        )
    if "바로 기여할 건가요?" not in text or "Ready to contribute now?" not in text:
        errors.append(
            "README.md: first-visit chooser must include a Korean/English contribution decision prompt near the landing section"
        )
    if "새 저장소 온보딩" not in text or "New repo onboarding" not in text:
        errors.append(
            "README.md: featured use cases must include a Korean/English onboarding scenario near the landing section"
        )
    if "첫 PR 준비" not in text or "First PR prep" not in text:
        errors.append(
            "README.md: featured use cases must include a Korean/English first-PR scenario near the landing section"
        )
    if "Minute 4-5" not in text or "2분" not in text:
        errors.append(
            "README.md: first 5-minute contribution flow must include time-boxed Korean/English steps"
        )
    if "docs/README_FEATURED_CATEGORY_MAP.md" not in "\n".join(lines[:140]):
        errors.append(
            "README.md: the first 140 lines must link docs/README_FEATURED_CATEGORY_MAP.md so featured categories stay reusable near the intro-first landing block"
        )
    if "docs/README_FEATURED_EXAMPLE_PATHS.md" not in "\n".join(lines[:160]):
        errors.append(
            "README.md: the first 160 lines must link docs/README_FEATURED_EXAMPLE_PATHS.md so featured example paths stay attached to the intro-first landing block"
        )
    if "docs/README_PROJECT_STARTER_PACK.md" not in "\n".join(lines[:80]):
        errors.append(
            "README.md: the first 80 lines must link docs/README_PROJECT_STARTER_PACK.md so the project-intro starter pack stays visible in the landing block"
        )
    if "docs/README_PROJECT_FIRST_LOOK.md" not in "\n".join(lines[:80]):
        errors.append(
            "README.md: the first 80 lines must link docs/README_PROJECT_FIRST_LOOK.md so the project-intro first-look guide stays visible in the landing block"
        )
    if "docs/README_PROJECT_QUICKSTART_PERSONAS.md" not in "\n".join(lines[:100]):
        errors.append(
            "README.md: the first 100 lines must link docs/README_PROJECT_QUICKSTART_PERSONAS.md so role-based first sentence/command/doc handoff stays visible in the intro-first landing block"
        )
    if "docs/README_PROJECT_QUICKSTART_FLOW.md" not in "\n".join(lines[:100]):
        errors.append(
            "README.md: the first 100 lines must link docs/README_PROJECT_QUICKSTART_FLOW.md so project overview -> audience -> value -> featured examples -> quick-start flow stays visible during README landing rewrites"
        )
    if "docs/README_PROJECT_ENTRY_PROMISE.md" not in "\n".join(lines[:90]):
        errors.append(
            "README.md: the first 90 lines must link docs/README_PROJECT_ENTRY_PROMISE.md so the landing block keeps an explicit project-intro promise before governance-heavy sections"
        )
    if "docs/README_FIRST_ACTION_MATRIX.md" not in "\n".join(lines[:120]):
        errors.append(
            "README.md: the first 120 lines must link docs/README_FIRST_ACTION_MATRIX.md so explorer/contributor/operator first action -> next doc -> expected result stays attached to the landing block"
        )
    if "docs/README_FIRST_VISIT_PACK.md" not in "\n".join(lines[:100]):
        errors.append(
            "README.md: the first 100 lines must link docs/README_FIRST_VISIT_PACK.md so first-visit starter bundles stay attached to the intro-first landing block"
        )
    if "docs/README_FIRST_SCREEN_MAP.md" not in "\n".join(lines[:120]):
        errors.append(
            "README.md: the first 120 lines must link docs/README_FIRST_SCREEN_MAP.md so the intro -> audience -> value -> examples -> quick-start order stays visible during landing rewrites"
        )
    if "docs/README_PROJECT_POSITIONING.md" not in "\n".join(lines[:140]):
        errors.append(
            "README.md: the first 140 lines must link docs/README_PROJECT_POSITIONING.md so the landing block keeps an explicit project-value positioning handoff before governance-heavy sections"
        )
    if "docs/README_INTRO_FIRST_MAINTENANCE_LOOP.md" not in "\n".join(lines[:140]):
        errors.append(
            "README.md: the first 140 lines must link docs/README_INTRO_FIRST_MAINTENANCE_LOOP.md so intro-first maintenance guidance stays attached to the landing block"
        )

    if "docs/README_AUDIENCE_VALUE_MAP.md" not in text:
        errors.append(
            "README.md: landing or learn-more sections must link to docs/README_AUDIENCE_VALUE_MAP.md so audience/value-first messaging stays reusable"
        )

    if "docs/README_FIRST_SCREEN_SCRIPT.md" not in text:
        errors.append(
            "README.md: landing or learn-more sections must link to docs/README_FIRST_SCREEN_SCRIPT.md so intro-first copy guidance stays discoverable"
        )
    if "docs/README_PROJECT_VALUE_QUICKSTART.md" not in text:
        errors.append(
            "README.md: landing summary must link to docs/README_PROJECT_VALUE_QUICKSTART.md so contributors can keep the intro/audience/value/quick-start one-pager nearby"
        )
    if "docs/README_PROJECT_OVERVIEW_FAQ.md" not in "\n".join(lines[:80]):
        errors.append(
            "README.md: the first 80 lines must link docs/README_PROJECT_OVERVIEW_FAQ.md so first-time visitors can resolve intro/audience/quick-start questions without scrolling into governance sections"
        )
    if "docs/README_LANDING_QUICKSTART_MAP.md" not in "\n".join(lines[:140]):
        errors.append(
            "README.md: the first 140 lines must link docs/README_LANDING_QUICKSTART_MAP.md so intro/audience/value/categories/quick-start flow stays reusable near the landing block"
        )
    if "docs/README_VALUE_PROOF_POINTS.md" not in text:
        errors.append(
            "README.md: landing summary must link to docs/README_VALUE_PROOF_POINTS.md so the project value proof points stay reusable near the intro-first block"
        )
    if "## 빠른 시작 / Quick start" not in text:
        errors.append(
            "README.md: README must include a bilingual `## 빠른 시작 / Quick start` section after the landing-first overview block"
        )
    if "python3 templates/scripts/validate_template.py" not in text:
        errors.append(
            "README.md: quick start must include `python3 templates/scripts/validate_template.py` for reproducible validation"
        )
    if "examples/quickstart.md" not in text:
        errors.append(
            "README.md: landing and quick-start sections must point to examples/quickstart.md as the follow-up onboarding path"
        )
    if "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md" not in text:
        errors.append(
            "README.md: quick start/contribution section must link to docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md"
        )
    if "docs/PROJECT_OVERVIEW.md" not in text or "docs/PROJECT_DIRECTION.md" not in text:
        errors.append(
            "README.md: learn-more section must link to docs/PROJECT_OVERVIEW.md and docs/PROJECT_DIRECTION.md"
        )
    if "docs/PROJECT_ENTRY_PATHS.md" not in text:
        errors.append(
            "README.md: learn-more section must link to docs/PROJECT_ENTRY_PATHS.md for next-step navigation"
        )
    intro_blueprint_idx = text.find("docs/README_PROJECT_INTRO_BLUEPRINT.md")
    learn_more_idx = text.find("## 더 읽기 / Learn more")
    if intro_blueprint_idx == -1:
        errors.append(
            "README.md: learn-more section must link to docs/README_PROJECT_INTRO_BLUEPRINT.md so intro-first README copy stays reusable"
        )
    elif learn_more_idx != -1 and intro_blueprint_idx < learn_more_idx:
        errors.append(
            "README.md: docs/README_PROJECT_INTRO_BLUEPRINT.md should stay in the Learn more section, not in the landing-first block"
        )

    if "docs/README_USER_JOURNEYS.md" not in text:
        errors.append(
            "README.md: learn-more or journey sections must link to docs/README_USER_JOURNEYS.md so intro-first audience flows stay documented"
        )
    if "docs/README_FAST_PATHS.md" not in text:
        errors.append(
            "README.md: learn-more or quick-start sections must link to docs/README_FAST_PATHS.md so first-time visitors can choose an intro-first 60-second path"
        )
    if "### 빠른 기여 체크 / Quick contribution check" not in text:
        errors.append(
            "README.md: quick start must include the condensed bilingual contribution check heading"
        )
    if "## 처음 기여할 때 읽는 순서 / First-time contributor reading order" not in text:
        errors.append(
            "README.md: must include the first-time contributor reading order section near quick start"
        )
    if "Estimated 1 min" not in text or "Estimated 2 min" not in text:
        errors.append(
            "README.md: first-time contributor reading order must include estimated onboarding times"
        )

    ordered_sections = [
        "## 프로젝트 소개 / Project overview",
        "## 처음 방문 FAQ / First-time visitor FAQ",
        "## 프로젝트 한눈에 보기 / Project at a glance",
        "## 빠른 적합성 체크 / Quick fit check",
        "## 대표 활용 시나리오 / Featured use cases",
        "## 이 저장소를 읽는 법 / How to read this repo",
        "## 프로젝트 스냅샷 / Project snapshot",
        "## 10초 시작 선택 / 10-second start chooser",
        "## 프로젝트 시작 맵 / Project start map",
        "## 핵심 시작 버튼 / Core start buttons",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 대표 시작 예시 / Featured starter examples",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 한눈에 보는 3단계 시작 / 3-step start path",
        "## 첫 방문자 체크 / First-visit chooser",
        "## 30초 적합성 체크 / 30-second fit check",
        "## 이 저장소가 특히 맞는 경우 / Best-fit scenarios",
        "## 이 저장소가 덜 맞는 경우 / Not-for scenarios",
        "## 카테고리 바로가기 / Category jump links",
        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
        "## 역할별 1클릭 다음 문서 / Role-based 1-click next docs",
        "## 역할별 바로 열 문서 / Role-based first-open docs",
        "## 빠른 시작 / Quick start",
    ]
    positions = []
    for heading in ordered_sections:
        idx = text.find(heading)
        if idx == -1:
            continue
        positions.append((heading, idx))
    if len(positions) >= 2:
        only_positions = [idx for _, idx in positions]
        if only_positions != sorted(only_positions):
            errors.append(
                "README.md: landing-page sections must stay in order overview -> first-time visitor FAQ -> at-a-glance -> fit check -> featured use cases -> how-to-read -> snapshot -> audience -> value -> starter examples -> featured categories -> quick-start-at-a-glance -> 3-step-start -> first-visit-chooser -> 30-second-fit-check -> best-fit/not-for scenarios -> category-jump-links -> role-based entry sections -> quick start"
            )

    top_callout_idx = text.find("## 상단 핵심 콜아웃 / Top contributor callouts")
    fit_check_idx = text.find("## 30초 적합성 체크 / 30-second fit check")
    if top_callout_idx != -1 and fit_check_idx != -1 and top_callout_idx < fit_check_idx:
        errors.append(
            "README.md: Top contributor callouts must stay below the 30-second fit check so the landing page introduces project value before contribution guardrails"
        )

    quick_start_idx = text.find("## 빠른 시작 / Quick start")
    learn_more_idx = text.find("## 더 읽기 / Learn more")
    if quick_start_idx != -1 and learn_more_idx != -1 and learn_more_idx < quick_start_idx:
        errors.append(
            "README.md: Learn more must stay below the Quick start section so project intro/value/examples appear before long-form governance links"
        )
    first_time_idx = text.find("## 처음 기여할 때 읽는 순서 / First-time contributor reading order")
    if quick_start_idx != -1 and first_time_idx != -1 and first_time_idx < quick_start_idx:
        errors.append(
            "README.md: First-time contributor reading order must stay below the Quick start section so contributor onboarding does not displace the intro-first landing block"
        )

    quick_start_idx = text.find("## Quick start")
    repo_structure_idx = text.find("## Repository structure")
    if quick_start_idx != -1 and repo_structure_idx != -1 and repo_structure_idx < quick_start_idx:
        errors.append(
            "README.md: Repository structure must stay below the Quick start section so the landing page remains intro-first"
        )
    for lower_heading in [
        "## 실무용 기여 체크리스트 / Practical contribution checklist",
        "## Roadmap summary",
    ]:
        lower_idx = text.find(lower_heading)
        if quick_start_idx != -1 and lower_idx != -1 and lower_idx < quick_start_idx:
            errors.append(
                f"README.md: {lower_heading} must stay below the Quick start section to preserve the intro-first landing flow"
            )
    return errors



def _extract_top_level_bullets(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if re.fullmatch(r"- .+", line.strip())
    ]


def _normalize_sync_text(value: str) -> str:
    normalized = value.lower()
    normalized = normalized.replace("**", "")
    normalized = normalized.replace("`", "")
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def _check_readme_top_callout_sync(root: Path) -> list[str]:
    readme_path = root / "README.md"
    callouts_path = root / "docs" / "README_TOP_CALLOUTS.md"
    if not readme_path.exists() or not callouts_path.exists():
        return []

    readme_text = readme_path.read_text(encoding="utf-8")
    callout_text = callouts_path.read_text(encoding="utf-8")
    errors: list[str] = []

    if "## 상단 핵심 콜아웃 / Top contributor callouts" not in readme_text:
        return ["README.md: missing top contributor callouts section for sync validation"]

    readme_section = _extract_section(readme_text, "상단 핵심 콜아웃 / Top contributor callouts")
    required_markers = [
        "한국어 기본 + 영어",
        "재현 명령 / 종료코드 / 핵심 출력",
        "다음 실행",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "5-minute contribution flow",
        "docs/README_TOP_CALLOUTS.md",
        "docs/README_AUDIENCE_VALUE_MAP.md",
    "docs/README_PROJECT_INTRO_60S.md",
    "docs/README_FIRST_SCREEN_MAP.md",
        "docs/PROJECT_OVERVIEW.md",
        "docs/PROJECT_ENTRY_PATHS.md",
        "docs/PROJECT_DIRECTION.md",
        "docs/README_INFORMATION_ARCHITECTURE.md",
    ]
    missing_markers = [marker for marker in required_markers if marker not in readme_section]
    if missing_markers:
        errors.append(
            "README.md: top contributor callouts must retain source-callout coverage markers -> "
            + ", ".join(missing_markers)
        )

    if "README 상단 콜아웃" not in callout_text or "README top callouts" not in callout_text:
        errors.append(
            "docs/README_TOP_CALLOUTS.md: source callout doc must describe README top-callout synchronization in Korean and English"
        )

    return errors

def _check_bilingual_markers(root: Path) -> list[str]:
    errors: list[str] = []
    for rel_path, markers in BILINGUAL_SECTION_MARKERS.items():
        path = root / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        missing_markers = [marker for marker in markers if marker not in text]
        if missing_markers:
            marker_list = ", ".join(missing_markers)
            errors.append(f"{rel_path}: missing bilingual markers -> {marker_list}")

    checklist_path = root / "docs" / "BILINGUAL_CONTRIBUTION_CHECKLIST.md"
    if checklist_path.exists():
        text = checklist_path.read_text(encoding="utf-8")
        ko_items = re.findall(r"(?mi)^\s*- \[ \] .+$", _extract_section(text, "한국어 체크리스트 (Primary)"))
        en_items = re.findall(r"(?mi)^\s*- \[ \] .+$", _extract_section(text, "English mirror"))
        if ko_items and en_items and len(ko_items) != len(en_items):
            errors.append(
                "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md: Korean/English checklist item counts must match"
            )

        validation_section = _extract_section(text, "자동 검증 명령 / Validation commands")
        ko_command_block = re.search(r"(?ms)^한국어:\s*$\n(?P<body>.*?)(?=^English mirror:|\Z)", validation_section)
        en_command_block = re.search(r"(?ms)^English mirror:\s*$\n(?P<body>.*)$", validation_section)
        ko_command_items = (
            re.findall(r"(?mi)^\s*-\s+.+$", ko_command_block.group("body")) if ko_command_block else []
        )
        en_command_items = (
            re.findall(r"(?mi)^\s*-\s+.+$", en_command_block.group("body")) if en_command_block else []
        )
        if ko_command_items and en_command_items and len(ko_command_items) != len(en_command_items):
            errors.append(
                "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md: Korean/English validation command counts must match"
            )

    readme_path = root / "README.md"
    if readme_path.exists():
        text = readme_path.read_text(encoding="utf-8")
        english_mirror_line = next(
            (line for line in text.splitlines() if line.strip().startswith("English mirror:")),
            None,
        )
        if english_mirror_line is not None:
            mirror_body = english_mirror_line.split(":", 1)[1].strip()
            if len(mirror_body) < 12:
                errors.append(
                    "README.md: English mirror line must include a meaningful translated summary (>=12 chars)"
                )

    run_log_path = root / "docs" / "BILINGUAL_CONTRIBUTION_CHECKLIST.md"
    if run_log_path.exists():
        text = run_log_path.read_text(encoding="utf-8")
        run_log_section = _extract_section(text, "반복 작업 방지 로그 / Anti-repeat run log")
        ko_log_block = re.search(r"(?ms)^한국어:\s*$\n(?P<body>.*?)(?=^English mirror:|\Z)", run_log_section)
        en_log_block = re.search(r"(?ms)^English mirror:\s*$\n(?P<body>.*)$", run_log_section)
        ko_log_items = re.findall(r"(?mi)^\s*-\s+.+$", ko_log_block.group("body")) if ko_log_block else []
        en_log_items = re.findall(r"(?mi)^\s*-\s+.+$", en_log_block.group("body")) if en_log_block else []
        if ko_log_items and en_log_items and len(ko_log_items) != len(en_log_items):
            errors.append(
                "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md: Korean/English anti-repeat run-log item counts must match"
            )

    return errors


def _check_contributing_structure(root: Path) -> list[str]:
    path = root / "CONTRIBUTING.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    required_markers = [
        "README.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/pr-evidence-mini-walkthrough.md",
    ]
    for marker in required_markers:
        if marker not in text:
            errors.append(f"CONTRIBUTING.md: missing contributor handoff link {marker}")

    ordered_sections = [
        "## 기여 원칙 / Principles",
        "## PR 필수 항목 / Pull request requirements",
        "## 리뷰 체크리스트 / Review checklist",
        "## 첫 기여 전에 볼 문서 / Read these before the first PR",
    ]
    positions = []
    for heading in ordered_sections:
        idx = text.find(heading)
        if idx == -1:
            continue
        positions.append(idx)
    if len(positions) == len(ordered_sections) and positions != sorted(positions):
        errors.append(
            "CONTRIBUTING.md: section order must stay principles -> PR requirements -> review checklist -> first PR reading list"
        )

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[2]

    missing_files = _check_required_files(root)
    bilingual_errors = _check_bilingual_markers(root)
    quickstart_errors = _check_quickstart_validation_command(root)
    contributing_errors = _check_contributing_structure(root)
    readme_callout_sync_errors = _check_readme_top_callout_sync(root)

    if missing_files or bilingual_errors or quickstart_errors or contributing_errors or readme_callout_sync_errors:
        if missing_files:
            print("필수 파일 누락 / Missing required files:")
            for item in missing_files:
                print(f"- {item}")
        if bilingual_errors:
            print("한/영 병기 검증 실패 / Bilingual marker check failed:")
            for item in bilingual_errors:
                print(f"- {item}")
        if quickstart_errors:
            print("퀵스타트 재현성 검증 실패 / Quickstart reproducibility check failed:")
            for item in quickstart_errors:
                print(f"- {item}")
        if contributing_errors:
            print("기여 가이드 구조 검증 실패 / Contributing guide structure check failed:")
            for item in contributing_errors:
                print(f"- {item}")
        if readme_callout_sync_errors:
            print("README 상단 콜아웃 동기화 실패 / README top callout sync failed:")
            for item in readme_callout_sync_errors:
                print(f"- {item}")
        return 1

    print("검증 통과 / Validation passed: baseline + bilingual markers are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
