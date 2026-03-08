from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from templates.scripts import validate_template


class ValidateTemplateTests(unittest.TestCase):
    def test_repository_structure_must_stay_below_quick_start(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## Repository structure",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("Repository structure must stay below the Quick start section" in error for error in errors))

    def test_landing_section_order_check_reports_reversed_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 대상 사용자 / Who this is for",
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "탐색이 먼저인가요?",
                        "Just exploring first?",
                        "바로 기여할 건가요?",
                        "Ready to contribute now?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("landing-page sections must stay in order" in error for error in errors))

    def test_landing_section_order_check_requires_project_snapshot_after_overview(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 대상 사용자 / Who this is for",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "탐색이 먼저인가요?",
                        "Just exploring first?",
                        "바로 기여할 건가요?",
                        "Ready to contribute now?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("overview -> snapshot -> audience" in error for error in errors))

    def test_project_snapshot_requires_entry_points_and_landing_rule_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "탐색이 먼저인가요?",
                        "Just exploring first?",
                        "바로 기여할 건가요?",
                        "Ready to contribute now?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "탐색형 / Explorer path",
                        "기여형 / Contributor path",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project snapshot" in error for error in errors))

    def test_readme_requires_operator_path_marker_for_intro_first_navigation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "탐색이 먼저인가요?",
                        "Just exploring first?",
                        "바로 기여할 건가요?",
                        "Ready to contribute now?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "탐색형 / Explorer path",
                        "기여형 / Contributor path",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_bilingual_markers(root)

            self.assertTrue(any("운영형 / Operator path" in error for error in errors))


    def test_first_visit_chooser_is_required_near_intro_landing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "탐색형 / Explorer path",
                        "기여형 / Contributor path",
                        "운영형 / Operator path",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-visit chooser" in error for error in errors))

    def test_readme_requires_featured_use_case_markers_for_intro_first_landing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "탐색이 먼저인가요?",
                        "Just exploring first?",
                        "바로 기여할 건가요?",
                        "Ready to contribute now?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "탐색형 / Explorer path",
                        "기여형 / Contributor path",
                        "운영형 / Operator path",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("featured use cases" in error for error in errors))

    def test_top_callout_sync_check_reports_missing_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            docs.mkdir()
            (root / "README.md").write_text(
                "## 상단 핵심 콜아웃 / Top contributor callouts\n- 한국어 기본 + 영어\n",
                encoding="utf-8",
            )
            (docs / "README_TOP_CALLOUTS.md").write_text(
                "# README 상단 콜아웃 문안 / README top callouts\nEnglish mirror:\n",
                encoding="utf-8",
            )

            errors = validate_template._check_readme_top_callout_sync(root)

            self.assertTrue(any("top contributor callouts must retain source-callout coverage markers" in error for error in errors))


    def test_three_step_start_path_is_required_near_intro_landing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "탐색이 먼저인가요?",
                        "Just exploring first?",
                        "바로 기여할 건가요?",
                        "Ready to contribute now?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "탐색형 / Explorer path",
                        "기여형 / Contributor path",
                        "운영형 / Operator path",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "python3 templates/scripts/validate_template.py",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("3-step start path" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
