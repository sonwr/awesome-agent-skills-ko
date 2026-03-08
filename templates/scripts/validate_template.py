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
    "docs/PROJECT_OVERVIEW.md",
    "docs/PROJECT_ENTRY_PATHS.md",
    "docs/PROJECT_DIRECTION.md",
    "docs/README_INFORMATION_ARCHITECTURE.md",
    "docs/README_FIRST_SCREEN_CHECKLIST.md",
    "docs/README_USER_JOURNEYS.md",
    "docs/README_FAST_PATHS.md",
    "examples/pr-evidence-mini-walkthrough.md",
    "examples/quickstart.md",
]


BILINGUAL_SECTION_MARKERS = {
    "README.md": [
        "English mirror:",
        "## 프로젝트 소개 / Project overview",
        "## 프로젝트 스냅샷 / Project snapshot",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 빠른 시작 / Quick start",
        "## 한눈에 보는 3단계 시작 / 3-step start path",
        "## 첫 방문자 체크 / First-visit chooser",
        "## 30초 적합성 체크 / 30-second fit check",
        "## 카테고리 바로가기 / Category jump links",
        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
        "## 역할별 바로 열 문서 / Role-based first-open docs",
        "## 카테고리 바로가기 / Category jump links",
        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
        "## 역할별 바로 열 문서 / Role-based first-open docs",
        "탐색형 / Explorer",
        "기여형 / Contributor",
        "운영형 / Operator",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 대표 활용 시나리오 / Featured use cases",
        "## 추천 시작 경로 / Recommended starting paths",
        "### 빠른 선택 카드 / Quick chooser cards",
        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
        "### 빠른 선택 카드 / Quick chooser cards",
        "탐색형 / Explorer path",
        "기여형 / Contributor path",
        "운영형 / Operator path",
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
    "docs/README_USER_JOURNEYS.md": [
        "README 사용자 여정 / README user journeys",
        "## 탐색형 방문자 / Explorer journey",
        "## 기여형 방문자 / Contributor journey",
        "## 운영형 방문자 / Operator journey",
        "English mirror:",
    ],
    "docs/README_FAST_PATHS.md": [
        "README 빠른 진입 경로 / README fast paths",
        "## 탐색형 60초 경로 / Explorer 60-second path",
        "## 기여형 60초 경로 / Contributor 60-second path",
        "## 운영형 60초 경로 / Operator 60-second path",
        "English mirror:",
    ],
    "docs/README_TOP_CALLOUTS.md": [
        "README 상단 콜아웃 문안 / README top callout copy",
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
    for required_heading in [
        "## 프로젝트 소개 / Project overview",
        "## 프로젝트 스냅샷 / Project snapshot",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 한눈에 보는 3단계 시작 / 3-step start path",
        "## 첫 방문자 체크 / First-visit chooser",
        "## 30초 적합성 체크 / 30-second fit check",
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
    if "## 역할별 한 줄 진입점 / Role-based one-line entry points" not in text or "**탐색형 / Explorer**" not in text or "**기여형 / Contributor**" not in text or "**운영형 / Operator**" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based one-line entry points for explorer/contributor/operator paths"
        )
    if "## 역할별 바로 열 문서 / Role-based first-open docs" not in text or "docs/README_FAST_PATHS.md" not in text:
        errors.append(
            "README.md: landing section must include bilingual role-based first-open docs so visitors can jump into explorer/contributor/operator paths in one click"
        )
    if "## 역할별 30초 선택 카드 / 30-second role chooser cards" not in text or "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md" not in text:
        errors.append(
            "README.md: landing section must include bilingual 30-second role chooser cards so explorer/contributor/operator paths stay compressed near the top"
        )
    role_first_open_section = _extract_section(text, "역할별 바로 열 문서 / Role-based first-open docs")
    required_role_docs = [
        "examples/quickstart.md",
        "docs/PROJECT_OVERVIEW.md",
        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
        "examples/pr-evidence-mini-walkthrough.md",
        "docs/README_FAST_PATHS.md",
        "docs/README_INFORMATION_ARCHITECTURE.md",
        "docs/CURATION_POLICY.md",
    ]
    missing_role_docs = [doc for doc in required_role_docs if doc not in role_first_open_section]
    if missing_role_docs:
        errors.append(
            "README.md: role-based first-open docs must keep explorer/contributor/operator handoff links together -> "
            + ", ".join(missing_role_docs)
        )
    if "대표 시작점" not in text or "Landing-page rule" not in text:
        errors.append(
            "README.md: project snapshot must surface representative entry points and the landing-page rule in Korean/English"
        )
    project_snapshot_section = _extract_section(text, "프로젝트 스냅샷 / Project snapshot")
    if "python3 templates/scripts/validate_template.py" not in project_snapshot_section or "examples/quickstart.md" not in project_snapshot_section:
        errors.append(
            "README.md: project snapshot must include the first validation command and quickstart doc link so intro-first visitors can act without scrolling"
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
        "## 프로젝트 스냅샷 / Project snapshot",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 대표 활용 시나리오 / Featured use cases",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 한눈에 보는 3단계 시작 / 3-step start path",
        "## 첫 방문자 체크 / First-visit chooser",
        "## 30초 적합성 체크 / 30-second fit check",
        "## 카테고리 바로가기 / Category jump links",
        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
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
                "README.md: landing-page sections must stay in order overview -> snapshot -> audience -> value -> featured categories -> featured use cases -> quick-start-at-a-glance -> 3-step-start -> first-visit-chooser -> 30-second-fit-check -> category-jump-links -> role-based entry sections -> quick start"
            )

    top_callout_idx = text.find("## 상단 핵심 콜아웃 / Top contributor callouts")
    fit_check_idx = text.find("## 30초 적합성 체크 / 30-second fit check")
    if top_callout_idx != -1 and fit_check_idx != -1 and top_callout_idx < fit_check_idx:
        errors.append(
            "README.md: Top contributor callouts must stay below the 30-second fit check so the landing page introduces project value before contribution guardrails"
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
