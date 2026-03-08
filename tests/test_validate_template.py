from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from templates.scripts import validate_template


class ValidateTemplateTests(unittest.TestCase):
    def test_landing_section_order_check_reports_reversed_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 대상 사용자 / Who this is for",
                        "## 프로젝트 소개 / Project overview",
                        "## 제공 가치 / What you get",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
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


if __name__ == "__main__":
    unittest.main()
