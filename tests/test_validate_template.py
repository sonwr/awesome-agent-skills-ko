from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from templates.scripts import validate_template


class ValidateTemplateTests(unittest.TestCase):


    def test_readme_requires_30_second_landing_summary_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 첫 화면 30초 요약 / 30-second landing summary\n\n- **프로젝트 소개 한 줄 / Project intro** — 한국어 기본 큐레이션 저장소이며, 첫 화면에서 바로 검증 명령과 다음 문서를 찾게 만드는 구조를 지향합니다.\n- **대상 사용자 / Best-fit audience** — 한국어 기본 흐름으로 탐색·검증·기여를 빠르게 시작하려는 빌더/팀에게 맞습니다.\n- **대표 카테고리 / Featured categories** — 온보딩/기여 가이드, PR 증빙 템플릿, 큐레이션/운영 기준 문서를 우선 노출합니다.\n- **빠른 시작 / Quick start** — `python3 templates/scripts/validate_template.py` 실행 후 `examples/quickstart.md`로 이동합니다.\n\nEnglish mirror:\n- **Project intro** — a Korean-first curation repo designed so the first screen points directly to the validation command and next document.\n- **Best-fit audience** — builders and teams who want fast Korean-first discovery, validation, and contribution flows.\n- **Featured categories** — onboarding/contribution guides, PR evidence templates, and curation/governance docs.\n- **Quick start** — run `python3 templates/scripts/validate_template.py`, then open `examples/quickstart.md`.\n\n",
                "",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("30-second landing summary" in error for error in errors))

    def test_readme_requires_how_to_read_repo_section_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 이 저장소를 읽는 법 / How to read this repo\n\n- **1단계 / Step 1** — `프로젝트 소개 / Project overview`와 `프로젝트 한눈에 보기 / Project at a glance`만 읽고 대상 사용자와 핵심 가치를 먼저 잡습니다.\n- **2단계 / Step 2** — `프로젝트 시작 맵 / Project start map`에서 탐색/검증/기여/운영 중 지금 필요한 경로를 고릅니다.\n- **3단계 / Step 3** — 첫 실행은 `python3 templates/scripts/validate_template.py`, 다음 문서는 `examples/quickstart.md`로 이어갑니다.\n\nEnglish mirror:\n- **Step 1** — read `Project overview` and `Project at a glance` first to understand the audience and value.\n- **Step 2** — use the `Project start map` to pick the right route: explore, validate, contribute, or audit.\n- **Step 3** — run `python3 templates/scripts/validate_template.py`, then continue with `examples/quickstart.md`.\n\n",
                "",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("how-to-read section" in error for error in errors))

    def test_readme_requires_role_based_instant_jump_deep_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 역할별 바로 점프 / Role-based instant jumps",
                "## 역할별 점프 / Role-based jumps",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("role-based instant jumps" in error for error in errors))

    def test_readme_requires_bilingual_first_command_by_role_section(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 역할별 첫 명령 / First command by role\n\n- **탐색형 / Explorer** — 첫 명령: `python3 templates/scripts/validate_template.py` → 다음 문서: `examples/quickstart.md`\n- **기여형 / Contributor** — 첫 명령: `python3 templates/scripts/validate_template.py` → 다음 문서: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`\n- **운영형 / Operator** — 첫 명령: `python3 templates/scripts/validate_template.py` → 다음 문서: `docs/README_FIRST_SCREEN_CHECKLIST.md`\n\nEnglish mirror:\n- **Explorer** — first command: `python3 templates/scripts/validate_template.py` → next doc: `examples/quickstart.md`\n- **Contributor** — first command: `python3 templates/scripts/validate_template.py` → next doc: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`\n- **Operator** — first command: `python3 templates/scripts/validate_template.py` → next doc: `docs/README_FIRST_SCREEN_CHECKLIST.md`\n\n",
                "",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first command by role" in error for error in errors))

    def test_readme_requires_bilingual_first_wins_by_role_section(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "무엇을 하나요?",
                        "왜 필요한가요?",
                        "English mirror:",
                        "What does it do?",
                        "Why does it matter?",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "누구를 위한 저장소인가요?",
                        "무엇이 바로 되나요?",
                        "어디서 시작하나요?",
                        "Who is this for?",
                        "What can I do immediately?",
                        "Where do I start?",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "## 이 저장소가 특히 맞는 경우 / Best-fit scenarios",
                        "Teams that need Korean-first docs with English mirrors",
                        "## 이 저장소가 덜 맞는 경우 / Not-for scenarios",
                        "plain link archive",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 1클릭 다음 문서 / Role-based 1-click next docs",
                        "docs/README_FAST_PATHS.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 빠른 시작 / Quick start",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first wins by role" in error for error in errors))

    def test_readme_requires_bilingual_fast_path_handoff_cue(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "무엇을 하나요?",
                        "왜 필요한가요?",
                        "English mirror:",
                        "What does it do?",
                        "Why does it matter?",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "누구를 위한 저장소인가요?",
                        "무엇이 바로 되나요?",
                        "어디서 시작하나요?",
                        "Who is this for?",
                        "What can I do immediately?",
                        "Where do I start?",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "탐색형 / Explorer path",
                        "기여형 / Contributor path",
                        "운영형 / Operator path",
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
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "## 빠른 시작 / Quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("60-second role-guide cue" in error for error in errors))

    def test_readme_requires_intro_blueprint_doc_link_in_learn_more_section(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "examples/quickstart.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_USER_JOURNEYS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_PROJECT_INTRO_BLUEPRINT.md" in error for error in errors))
    def test_project_at_a_glance_requires_audience_action_and_start_prompts_in_both_languages(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "무엇을 하나요?",
                        "왜 필요한가요?",
                        "English mirror:",
                        "What does it do?",
                        "Why does it matter?",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "## 빠른 시작 / Quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project at a glance must answer audience/immediate action/where-to-start prompts in Korean" in error for error in errors))
            self.assertTrue(any("project at a glance must keep English mirror prompts" in error for error in errors))

    def test_project_overview_requires_what_and_why_prompts_in_both_languages(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "이 저장소는 스킬 큐레이션 모음입니다.",
                        "English mirror:",
                        "A curated collection.",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "## 빠른 시작 / Quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project overview must explain both what the project does and why it matters in Korean" in error for error in errors))
            self.assertTrue(any("project overview must include English mirror prompts" in error for error in errors))

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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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

    def test_project_snapshot_requires_validation_command_and_quickstart_link(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "examples/quickstart.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "docs/README_FAST_PATHS.md",
                        "## 상단 핵심 콜아웃 / Top contributor callouts",
                        "한국어 기본 + 영어",
                        "재현 명령 / 종료코드 / 핵심 출력",
                        "다음 실행",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "first 5-minute contribution flow",
                        "docs/README_TOP_CALLOUTS.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "## 빠른 시작 / Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project snapshot must include the first validation command and quickstart doc link" in error for error in errors))

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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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

    def test_readme_requires_user_journeys_doc_link_for_intro_first_navigation(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "examples/quickstart.md",
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

            self.assertTrue(any("README_USER_JOURNEYS.md" in error for error in errors))

    def test_readme_requires_fast_paths_doc_link_for_intro_first_navigation(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "examples/quickstart.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_USER_JOURNEYS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_FAST_PATHS.md" in error for error in errors))

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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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

    def test_readme_requires_quickstart_doc_link_near_intro_landing(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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

            self.assertTrue(any("examples/quickstart.md" in error for error in errors))


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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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


    def test_readme_requires_role_based_first_open_docs_section(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "examples/quickstart.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_FAST_PATHS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("role-based first-open docs" in error for error in errors))

    def test_role_based_first_open_docs_section_requires_all_handoff_links(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_USER_JOURNEYS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("role-based first-open docs must keep" in error for error in errors))



    def test_role_based_first_open_docs_require_first_screen_checklist_for_operator_path(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 빠른 시작 / Quick start",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "docs/README_FAST_PATHS.md",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_FIRST_SCREEN_CHECKLIST.md" in error for error in errors))

    def test_quickstart_at_a_glance_must_precede_role_cards(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            docs.mkdir()
            examples = root / "examples"
            examples.mkdir()
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "# awesome-agent-skills-ko",
                        "",
                        "English mirror: intro",
                        "## 프로젝트 소개 / Project overview",
                        "body",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "body",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "## 대상 사용자 / Who this is for",
                        "body",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "body",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "body",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "body",
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
                        "body",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 상단 핵심 콜아웃 / Top contributor callouts",
                        "최소 증빙 3종 필수",
                        "Document blockers with the next-run priority",
                        "처음 5분 기여 흐름",
                        "first 5-minute contribution flow",
                        "## 빠른 시작 / Quick start",
                        "python3 templates/scripts/validate_template.py",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_USER_JOURNEYS.md",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 더 읽기 / Learn more",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                    ]
                ),
                encoding="utf-8",
            )
            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("landing-page sections must stay in order" in error for error in errors))

if __name__ == "__main__":
    unittest.main()

    def test_top_callouts_must_stay_after_fit_check_and_before_role_paths(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
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
                        "## 상단 핵심 콜아웃 / Top contributor callouts",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "탐색형 / Explorer",
                        "기여형 / Contributor",
                        "운영형 / Operator",
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
                        "docs/README_USER_JOURNEYS.md",
                        "examples/quickstart.md",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("Top contributor callouts must stay below the 30-second fit check" in error for error in errors))



    def test_readme_requires_bilingual_quick_start_heading(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "examples/quickstart.md",
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

            self.assertTrue(any("bilingual `## 빠른 시작 / Quick start`" in error for error in errors))

    def test_readme_requires_10_second_start_chooser_near_landing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "## 이 저장소를 읽는 법 / How to read this repo",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "## 프로젝트 시작 맵 / Project start map",
                        "## 핵심 시작 버튼 / Core start buttons",
                        "## 역할별 첫 클릭 묶음 / Role-based first-click bundles",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "첫 PR 준비",
                        "Prepare the first PR",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 첫 클릭 묶음 / Role-based first-click bundles",
                        "도착 문서",
                        "landing doc",
                        "빠른 경로 앵커",
                        "fast-path anchor",
                        "docs/README_FAST_PATHS.md#탐색형-60초-경로--explorer-60-second-path",
                        "docs/README_FAST_PATHS.md#기여형-60초-경로--contributor-60-second-path",
                        "docs/README_FAST_PATHS.md#운영형-60초-경로--operator-60-second-path",
                        "## 역할별 바로 점프 / Role-based instant jumps",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "docs/CURATION_POLICY.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "Explorer path",
                        "Contributor path",
                        "Operator path",
                        "python3 templates/scripts/validate_template.py",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("10-second start chooser" in error for error in errors))


    def test_role_chooser_cards_are_required_near_landing_section(self) -> None:
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
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 빠른 시작 / Quick start",
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
                        "운영 기준을 점검하나요?",
                        "Auditing governance rails?",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "docs/README_FAST_PATHS.md",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "First PR prep",
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
                        "docs/README_USER_JOURNEYS.md",
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("30-second role chooser cards" in error for error in errors))

    def test_rejects_learn_more_above_quick_start(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "무엇을 하나요?",
                        "왜 필요한가요?",
                        "What does it do?",
                        "Why does it matter?",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "## 빠른 시작 / Quick start",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 상단 핵심 콜아웃 / Top contributor callouts",
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
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("Learn more must stay below the Quick start section" in error for error in errors))

    def test_rejects_first_time_reading_order_above_quick_start(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "무엇을 하나요?",
                        "왜 필요한가요?",
                        "What does it do?",
                        "Why does it matter?",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "새 저장소 온보딩",
                        "New repo onboarding",
                        "첫 PR 준비",
                        "First PR prep",
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
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 처음 기여할 때 읽는 순서 / First-time contributor reading order",
                        "Estimated 1 min",
                        "Estimated 2 min",
                        "## 빠른 시작 / Quick start",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "2분",
                        "Minute 4-5",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "### 빠른 기여 체크 / Quick contribution check",
                        "## 더 읽기 / Learn more",
                        "docs/PROJECT_ENTRY_PATHS.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/PROJECT_DIRECTION.md",
                        "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                        "docs/README_USER_JOURNEYS.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "## 상단 핵심 콜아웃 / Top contributor callouts",
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
                        "## Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("First-time contributor reading order must stay below the Quick start section" in error for error in errors))


class ValidateTemplateRoleHandoffTests(unittest.TestCase):

    def test_readme_requires_role_based_one_click_next_docs_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / 'README.md').write_text(
                "\n".join([
                    '## 프로젝트 소개 / Project overview',
                    '무엇을 하나요?',
                    '왜 필요한가요?',
                    'English mirror:',
                    'What does it do?',
                    'Why does it matter?',
                    '## 프로젝트 한눈에 보기 / Project at a glance',
                    '누구를 위한 저장소인가요?',
                    '무엇이 바로 되나요?',
                    '어디서 시작하나요?',
                    'Who is this for?',
                    'What can I do immediately?',
                    'Where do I start?',
                    '## 프로젝트 스냅샷 / Project snapshot',
                    '대표 시작점',
                    'Landing-page rule',
                    'python3 templates/scripts/validate_template.py',
                    'examples/quickstart.md',
                    '## 대상 사용자 / Who this is for',
                    '## 제공 가치 / What you get',
                    '## 대표 카테고리와 예시 / Featured categories and examples',
                    '## 대표 활용 시나리오 / Featured use cases',
                    '새 저장소 온보딩',
                    'New repo onboarding',
                    '첫 PR 준비',
                    'First PR prep',
                    '## 추천 시작 경로 / Recommended starting paths',
                    '### 빠른 선택 카드 / Quick chooser cards',
                    '탐색형 / Explorer path',
                    '기여형 / Contributor path',
                    '운영형 / Operator path',
                    '## 빠른 시작 한눈에 보기 / Quick start at a glance',
                    '## 한눈에 보는 3단계 시작 / 3-step start path',
                    '프로젝트 이해',
                    'Understand the project',
                    '첫 검증 실행',
                    'Run the first validation',
                    '첫 PR 준비',
                    'Prepare the first PR',
                    '## 첫 방문자 체크 / First-visit chooser',
                    '탐색이 먼저인가요?',
                    'Just exploring first?',
                    '바로 기여할 건가요?',
                    'Ready to contribute now?',
                    '## 30초 적합성 체크 / 30-second fit check',
                    '## 카테고리 바로가기 / Category jump links',
                    'Jump to onboarding',
                    'Jump to evidence examples',
                    'Jump to governance docs',
                    '## 역할별 한 줄 진입점 / Role-based one-line entry points',
                    '**탐색형 / Explorer**',
                    '**기여형 / Contributor**',
                    '**운영형 / Operator**',
                    '## 역할별 30초 선택 카드 / 30-second role chooser cards',
                    'python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md',
                    '## 역할별 바로 열 문서 / Role-based first-open docs',
                    'docs/README_FAST_PATHS.md',
                    'docs/README_FIRST_SCREEN_CHECKLIST.md',
                    'docs/README_FIRST_SCREEN_SCRIPT.md',
                    'docs/README_INFORMATION_ARCHITECTURE.md',
                    'docs/CURATION_POLICY.md',
                    'docs/PROJECT_OVERVIEW.md',
                    'docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md',
                    'examples/pr-evidence-mini-walkthrough.md',
                    '### 처음 5분 기여 흐름 / First 5-minute contribution flow',
                    '2분',
                    'Minute 4-5',
                    '### 빠른 시작 후 바로 볼 문서 / What to open right after quick start',
                    '## 빠른 시작 / Quick start',
                    '### 빠른 기여 체크 / Quick contribution check',
                    '## 처음 기여할 때 읽는 순서 / First-time contributor reading order',
                    'Estimated 1 min',
                    'Estimated 2 min',
                    '## 더 읽기 / Learn more',
                    'docs/PROJECT_DIRECTION.md',
                    'docs/PROJECT_ENTRY_PATHS.md',
                    'docs/README_PROJECT_INTRO_BLUEPRINT.md',
                    'docs/README_USER_JOURNEYS.md',
                    '## Quick start',
                ]),
                encoding='utf-8',
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any('1-click next docs' in error for error in errors))


    def test_project_start_map_requires_bilingual_handoff_bullets(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "무엇을 하나요?",
                        "왜 필요한가요?",
                        "English mirror:",
                        "What does it do?",
                        "Why does it matter?",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "누구를 위한 저장소인가요?",
                        "무엇이 바로 되나요?",
                        "어디서 시작하나요?",
                        "Who is this for?",
                        "What can I do immediately?",
                        "Where do I start?",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 프로젝트 시작 맵 / Project start map",
                        "- 탐색 먼저 / Explore first",
                        "- 바로 검증 / Validate now",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 1클릭 다음 문서 / Role-based 1-click next docs",
                        "docs/README_FAST_PATHS.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "Explorer path",
                        "Contributor path",
                        "Operator path",
                        "docs/CURATION_POLICY.md",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "## 빠른 시작 / Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project start map must keep bilingual explore/validate/contribute/audit handoff bullets" in error for error in errors))


    def test_core_start_buttons_require_project_validate_contribute_governance_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 프로젝트 소개 / Project overview",
                        "English mirror:",
                        "## 프로젝트 한눈에 보기 / Project at a glance",
                        "## 프로젝트 스냅샷 / Project snapshot",
                        "대표 시작점",
                        "Landing-page rule",
                        "python3 templates/scripts/validate_template.py",
                        "examples/quickstart.md",
                        "## 프로젝트 시작 맵 / Project start map",
                        "- 탐색 먼저 / Explore first",
                        "- 바로 검증 / Validate now",
                        "- 바로 기여 / Contribute now",
                        "- 운영 점검 / Audit the structure",
                        "## 핵심 시작 버튼 / Core start buttons",
                        "- Validate now",
                        "- Prepare the first PR",
                        "## 역할별 첫 클릭 묶음 / Role-based first-click bundles",
                        "도착 문서",
                        "landing doc",
                        "## 역할별 첫 명령 / First command by role",
                        "first command",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "## 대상 사용자 / Who this is for",
                        "## 제공 가치 / What you get",
                        "## 대표 시작 예시 / Featured starter examples",
                        "검증부터 시작 / Start with validation",
                        "기여 준비 / Prepare a contribution",
                        "운영 점검 / Audit the landing flow",
                        "examples/quickstart.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "## 대표 카테고리와 예시 / Featured categories and examples",
                        "## 대표 활용 시나리오 / Featured use cases",
                        "## 빠른 시작 한눈에 보기 / Quick start at a glance",
                        "## 한눈에 보는 3단계 시작 / 3-step start path",
                        "프로젝트 이해",
                        "Understand the project",
                        "첫 검증 실행",
                        "Run the first validation",
                        "## 첫 방문자 체크 / First-visit chooser",
                        "## 30초 적합성 체크 / 30-second fit check",
                        "## 카테고리 바로가기 / Category jump links",
                        "Jump to onboarding",
                        "Jump to evidence examples",
                        "Jump to governance docs",
                        "## 역할별 한 줄 진입점 / Role-based one-line entry points",
                        "**탐색형 / Explorer**",
                        "**기여형 / Contributor**",
                        "**운영형 / Operator**",
                        "## 역할별 30초 선택 카드 / 30-second role chooser cards",
                        "python3 templates/scripts/validate_template.py → docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "## 역할별 1클릭 다음 문서 / Role-based 1-click next docs",
                        "docs/README_FAST_PATHS.md",
                        "## 역할별 바로 열 문서 / Role-based first-open docs",
                        "examples/quickstart.md",
                        "docs/PROJECT_OVERVIEW.md",
                        "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                        "examples/pr-evidence-mini-walkthrough.md",
                        "docs/README_FAST_PATHS.md",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                        "docs/README_FIRST_SCREEN_SCRIPT.md",
                        "docs/README_INFORMATION_ARCHITECTURE.md",
                        "docs/CURATION_POLICY.md",
                        "## 추천 시작 경로 / Recommended starting paths",
                        "### 빠른 선택 카드 / Quick chooser cards",
                        "Explorer path",
                        "Contributor path",
                        "Operator path",
                        "docs/CURATION_POLICY.md",
                        "### 처음 5분 기여 흐름 / First 5-minute contribution flow",
                        "### 빠른 시작 후 바로 볼 문서 / What to open right after quick start",
                        "## 빠른 시작 / Quick start",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("core start buttons must keep bilingual project/validate/contribute/governance entry points" in error for error in errors))


    def test_required_landing_map_doc_mentions_maintenance_loop(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            docs.mkdir(parents=True, exist_ok=True)
            (docs / "README_LANDING_QUICKSTART_MAP.md").write_text(
                "\n".join(
                    [
                        "# README 랜딩 빠른 시작 맵 / README landing quick-start map",
                        "## 첫 화면 유지 루프 / First-screen maintenance loop",
                        "python3 templates/scripts/validate_template.py",
                        "docs/README_FIRST_SCREEN_CHECKLIST.md",
                    ]
                ),
                encoding="utf-8",
            )

            content = (docs / "README_LANDING_QUICKSTART_MAP.md").read_text(encoding="utf-8")

            self.assertIn("First-screen maintenance loop", content)
            self.assertIn("python3 templates/scripts/validate_template.py", content)
            self.assertIn("docs/README_FIRST_SCREEN_CHECKLIST.md", content)


class ReadmeProjectStartMapOrderTests(unittest.TestCase):

    def test_readme_requires_project_start_map_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "- **탐색 먼저 / Explore first** — 프로젝트 소개 → 대표 카테고리 → `examples/quickstart.md`\n- **바로 검증 / Validate now** — `python3 templates/scripts/validate_template.py` → `examples/quickstart.md`\n- **바로 기여 / Contribute now** — `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`\n- **운영 점검 / Audit the structure** — `docs/README_FAST_PATHS.md` → `docs/README_FIRST_SCREEN_CHECKLIST.md` → `docs/CURATION_POLICY.md`",
                "- **바로 기여 / Contribute now** — `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`\n- **탐색 먼저 / Explore first** — 프로젝트 소개 → 대표 카테고리 → `examples/quickstart.md`\n- **바로 검증 / Validate now** — `python3 templates/scripts/validate_template.py` → `examples/quickstart.md`\n- **운영 점검 / Audit the structure** — `docs/README_FAST_PATHS.md` → `docs/README_FIRST_SCREEN_CHECKLIST.md` → `docs/CURATION_POLICY.md`",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project start map must keep explore -> validate -> contribute -> audit order" in error for error in errors))
