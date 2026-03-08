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
    "examples/pr-evidence-mini-walkthrough.md",
    "examples/quickstart.md",
]


BILINGUAL_SECTION_MARKERS = {
    "README.md": [
        "English mirror:",
        "## 프로젝트 소개 / Project overview",
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 추천 시작 경로 / Recommended starting paths",
        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
        "### 빠른 선택 카드 / Quick chooser cards",
        "탐색형 / Explorer path",
        "기여형 / Contributor path",
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
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## 추천 시작 경로 / Recommended starting paths",
        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
    ]:
        if required_heading not in text:
            errors.append(f"README.md: missing landing-page heading {required_heading}")
    if "Minute 4-5" not in text or "2분" not in text:
        errors.append(
            "README.md: first 5-minute contribution flow must include time-boxed Korean/English steps"
        )
    if "python3 templates/scripts/validate_template.py" not in text:
        errors.append(
            "README.md: quick start must include `python3 templates/scripts/validate_template.py` for reproducible validation"
        )
    if "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md" not in text:
        errors.append(
            "README.md: quick start/contribution section must link to docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md"
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
        "## 대상 사용자 / Who this is for",
        "## 제공 가치 / What you get",
        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
        "## 대표 카테고리와 예시 / Featured categories and examples",
        "## Quick start",
    ]
    positions = []
    for heading in ordered_sections:
        idx = text.find(heading)
        if idx == -1:
            continue
        positions.append((heading, idx))
    if len(positions) == len(ordered_sections):
        only_positions = [idx for _, idx in positions]
        if only_positions != sorted(only_positions):
            errors.append(
                "README.md: landing-page sections must stay in order overview -> audience -> value -> quick-start-at-a-glance -> featured categories -> quick start"
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

    if missing_files or bilingual_errors or quickstart_errors or contributing_errors:
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
        return 1

    print("검증 통과 / Validation passed: baseline + bilingual markers are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
