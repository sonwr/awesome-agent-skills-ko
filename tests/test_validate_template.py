from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from templates.scripts import validate_template


class ValidateTemplateTests(unittest.TestCase):


    def test_readme_requires_bilingual_project_pitch_within_first_twenty_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음",
                "스킬 링크 모음",
            ).replace(
                "A curated, practical collection of agent skills and runnable templates",
                "A Korean-first link list",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first 20 lines must keep the bilingual project pitch" in error for error in errors))

    def test_readme_requires_project_overview_heading_within_first_twenty_eight_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join([f"line {idx}" for idx in range(1, 53)])
                + "\n## 프로젝트 소개 / Project overview\n"
                + "python3 templates/scripts/validate_template.py\n",
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first 50 lines" in error for error in errors))

    def test_readme_requires_15_second_first_visit_chooser_within_first_seventy_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join([f"line {idx}" for idx in range(1, 78)])
                + "\n## 첫 방문 15초 선택 / 15-second first-visit chooser\n"
                + "python3 templates/scripts/validate_template.py\n",
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first 75 lines" in error for error in errors))

    def test_readme_requires_start_here_summary_to_keep_intro_audience_value_category_quickstart_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                """- **대표 가치 / Immediate value** — 첫 검증 명령, 다음 문서, 첫 PR 증빙 경로를 한 번에 찾게 만듭니다.
- **대표 카테고리 / Featured categories** — 온보딩·PR 증빙·큐레이션/운영 기준 문서를 우선 노출합니다.
""",
                """- **대표 카테고리 / Featured categories** — 온보딩·PR 증빙·큐레이션/운영 기준 문서를 우선 노출합니다.
- **대표 가치 / Immediate value** — 첫 검증 명령, 다음 문서, 첫 PR 증빙 경로를 한 번에 찾게 만듭니다.
""",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("intro -> audience -> immediate value -> featured categories -> quick start order inside the Start-here summary block" in error for error in errors))

    def test_readme_requires_first_minute_outcome_section_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 첫 1분에 얻는 결과 / What you get in the first minute\n",
                "",
                1,
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-minute outcome section" in error for error in errors))

    def test_readme_requires_governance_handoff_cue_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "- **운영 문서 위치 / Where governance lives** — 기여 규칙·체크리스트·운영 가이드는 첫 화면 아래 `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, `docs/CURATION_POLICY.md`로 내려가 있으며, the README opens with project value first.\n",
                "",
            ).replace(
                "Governance details live below the landing block in `CONTRIBUTING.md`, `docs/README_FAST_PATHS.md`, and `docs/CURATION_POLICY.md`.\n",
                "",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("governance-handoff cue" in error for error in errors))

    def test_readme_requires_first_action_matrix_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_FIRST_ACTION_MATRIX.md",
                "docs/README_FIRST_ACTION_MATRIX_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first action matrix link" in error for error in errors))

    def test_readme_requires_project_entry_promise_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_ENTRY_PROMISE.md",
                "docs/README_PROJECT_ENTRY_PROMISE_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_PROJECT_ENTRY_PROMISE.md" in error for error in errors))

    def test_readme_requires_project_quickstart_flow_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_QUICKSTART_FLOW.md",
                "docs/README_PROJECT_QUICKSTART_FLOW_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_PROJECT_QUICKSTART_FLOW.md" in error for error in errors))

    def test_readme_requires_project_intro_paths_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_INTRO_PATHS.md",
                "docs/README_PROJECT_INTRO_PATHS_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_PROJECT_INTRO_PATHS.md" in error for error in errors))

    def test_readme_requires_role_based_start_map_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_ROLE_STARTERS.md",
                "docs/README_ROLE_STARTERS_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("role-based start map link" in error for error in errors))

    def test_readme_requires_who_starts_where_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_WHO_STARTS_WHERE.md",
                "docs/README_WHO_STARTS_WHERE_REMOVED.md",
                1,
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("who-starts-where routing doc link" in error for error in errors))

    def test_readme_requires_intro_value_quickstart_one_pager_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_VALUE_QUICKSTART.md",
                "docs/README_PROJECT_VALUE_QUICKSTART_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_PROJECT_VALUE_QUICKSTART.md" in error for error in errors))

    def test_readme_requires_project_first_look_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_FIRST_LOOK.md",
                "docs/README_PROJECT_FIRST_LOOK_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_PROJECT_FIRST_LOOK.md" in error for error in errors))

    def test_readme_requires_intro_60_seconds_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_INTRO_60S.md",
                "docs/README_PROJECT_INTRO_60S_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("intro-in-60-seconds doc link" in error for error in errors))

    def test_readme_requires_value_proof_points_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_VALUE_PROOF_POINTS.md",
                "docs/README_VALUE_PROOF_POINTS_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("README_VALUE_PROOF_POINTS.md" in error for error in errors))

    def test_readme_requires_audience_quick_recipes_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_AUDIENCE_QUICK_RECIPES.md",
                "docs/README_AUDIENCE_QUICK_RECIPES_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("audience quick-recipes doc link" in error for error in errors))

    def test_readme_requires_featured_use_cases_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_FEATURED_USE_CASES.md",
                "docs/README_FEATURED_USE_CASES_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("featured-use-cases doc link" in error for error in errors))

    def test_readme_requires_first_click_guide_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_FIRST_CLICK_GUIDE.md",
                "docs/README_FIRST_CLICK_GUIDE_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-click guide doc link" in error for error in errors))

    def test_readme_requires_first_visitor_promises_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_FIRST_VISITOR_PROMISES.md",
                "docs/README_FIRST_VISITOR_PROMISES_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-visitor promises doc link" in error for error in errors))

    def test_readme_requires_first_visitor_routes_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_FIRST_VISITOR_ROUTES.md",
                "docs/README_FIRST_VISITOR_ROUTES_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-visitor routes doc link" in error for error in errors))

    def test_readme_requires_project_value_ladder_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_VALUE_LADDER.md",
                "docs/README_PROJECT_VALUE_LADDER_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project value ladder doc link" in error for error in errors))

    def test_readme_requires_first_screen_quick_proof_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_FIRST_SCREEN_QUICK_PROOF.md",
                "docs/README_FIRST_SCREEN_QUICK_PROOF_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-screen quick-proof doc link" in error for error in errors))

    def test_readme_requires_project_value_quickcheck_doc_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "docs/README_PROJECT_VALUE_QUICKCHECK.md",
                "docs/README_PROJECT_VALUE_QUICKCHECK_REMOVED.md",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("project value quick-check doc link" in error for error in errors))

    def test_readme_requires_bilingual_not_just_a_link_dump_value_prop_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                '좋아 보이는 링크 모음"이 아니라, README 첫 화면만 읽어도 실행·검증·기여 경로가 바로 보이는 출발점을 만들기 위해서입니다.\n',
                '',
            ).replace(
                'instead of a vague link dump.\n',
                '',
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("not just a link dump" in error for error in errors))

    def test_readme_requires_ten_second_start_chooser_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "## 프로젝트 소개 / Project overview\n"
                + "\n".join([f"line {idx}" for idx in range(1, 112)])
                + "\n## 10초 시작 선택 / 10-second start chooser\n"
                + "python3 templates/scripts/validate_template.py\n",
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("10-second start chooser" in error for error in errors))

    def test_readme_requires_first_validation_command_within_first_160_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "## 프로젝트 소개 / Project overview\n"
                + "\n".join([f"line {idx}" for idx in range(1, 161)])
                + "\npython3 templates/scripts/validate_template.py\n",
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first 160 lines" in error for error in errors))

    def test_readme_requires_intro_first_top_order_within_first_140_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "## 바로 시작 요약 / Start-here summary",
                        "- 프로젝트 소개 / Project intro",
                        "- 대표 가치 / Immediate value",
                        "- 대상 사용자 / Who it helps",
                        "- 대표 카테고리 / Featured categories",
                        "- 빠른 시작 / Quick start",
                        "python3 templates/scripts/validate_template.py",
                    ]
                ),
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first 140 lines must keep overview -> audience -> value -> featured categories -> quick start in order" in error for error in errors))

    def test_readme_requires_featured_use_cases_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 대표 활용 시나리오 / Featured use cases",
                "## 대표 활용 시나리오 상세 / Featured use case details",
                1,
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("featured use cases" in error for error in errors))

    def test_readme_requires_value_cards_section_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 핵심 가치 카드 / Value cards\n",
                "",
                1,
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("value cards" in error for error in errors))

    def test_readme_requires_start_here_summary_markers_for_intro_audience_categories_and_quick_start(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "대표 카테고리 / Featured categories",
                "대표 분류 / Featured grouping",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("start-here summary markers" in error for error in errors))

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

    def test_readme_requires_first_time_visitor_faq_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8")
            sample = sample.replace("## 처음 방문 FAQ / First-time visitor FAQ", "## 방문자 FAQ / Visitor FAQ")
            sample = sample.replace("Is this just a link list?", "Is this just a list?")
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("first-time visitor FAQ" in error for error in errors))

    def test_readme_requires_bilingual_one_minute_quick_start_section(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "## 1분 빠른 시작 / 1-minute quick start\n\n```bash\npython3 templates/scripts/validate_template.py\n```\n\n- 바로 다음 문서 / Next doc: `examples/quickstart.md`\n- 첫 PR 준비 / First PR prep: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`\n- 소개형 랜딩 점검 / Intro-first landing audit: `docs/README_FIRST_SCREEN_CHECKLIST.md`, `docs/README_FIRST_SCREEN_WIREFRAME.md`\n- 전체 기여 규칙 / Full contributing guide: `CONTRIBUTING.md`\n\nEnglish mirror:\n- Run the validation command first, then open `examples/quickstart.md`.\n- For the first PR, continue with `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`.\n- For landing-page audits, open `docs/README_FIRST_SCREEN_CHECKLIST.md` and `docs/README_FIRST_SCREEN_WIREFRAME.md`.\n- Full contribution policy lives in `CONTRIBUTING.md`.\n\n",
                "",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("1-minute quick start" in error for error in errors))

    def test_readme_requires_featured_starter_examples_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                "## 프로젝트 소개 / Project overview\n"
                + "\n".join([f"line {idx}" for idx in range(1, 267)])
                + "\n## 대표 시작 예시 / Featured starter examples\n"
                + "python3 templates/scripts/validate_template.py\n",
                encoding="utf-8",
            )

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("featured starter examples must appear within the first 265 lines" in error for error in errors))

    def test_readme_requires_featured_starter_example_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8").replace(
                "English mirror:\n- **Project overview FAQ**",
                "English mirror removed:\n- **Project overview FAQ**",
            )
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("featured starter examples must keep validation/contribution/audit example links" in error for error in errors))

    def test_readme_requires_quickstart_followup_doc_trio(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8")
            sample = sample.replace("2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — 최소 증빙/병기 규칙\n", "")
            sample = sample.replace("3. `examples/pr-evidence-mini-walkthrough.md` — PR 코멘트 예시\n", "")
            sample = sample.replace("2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — minimum evidence and bilingual rules\n", "")
            sample = sample.replace("3. `examples/pr-evidence-mini-walkthrough.md` — PR comment example\n", "")
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("next-doc trio" in error for error in errors))

    def test_readme_requires_quickstart_followup_section_before_learn_more(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = Path(__file__).resolve().parents[1] / "README.md"
            sample = readme.read_text(encoding="utf-8")
            followup = """### 빠른 시작 후 바로 볼 문서 / What to open right after quick start

1. `examples/quickstart.md` — 첫 복붙 명령과 다음 읽기 순서
2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — 최소 증빙/병기 규칙
3. `examples/pr-evidence-mini-walkthrough.md` — PR 코멘트 예시

이 세 문서는 quick start 직후의 기본 후속 동선이며, 검증 스크립트가 빠짐없이 유지되는지 함께 확인합니다.

English mirror:
1. `examples/quickstart.md` — first copy-paste command and next reading step
2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — minimum evidence and bilingual rules
3. `examples/pr-evidence-mini-walkthrough.md` — PR comment example

These three docs are the default follow-up path after quick start, and the validator checks that the trio stays intact.

"""
            sample = sample.replace(followup, "")
            sample = sample.replace("## 더 읽기 / Learn more\n", "## 더 읽기 / Learn more\n\n" + followup)
            (root / "README.md").write_text(sample, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("before Learn more" in error for error in errors))

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

            self.assertTrue(any("overview -> first-time visitor FAQ -> at-a-glance" in error for error in errors))

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



    def test_check_quickstart_validation_command_requires_first_screen_in_3_lines_section(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            examples = root / "examples"
            templates = root / "templates" / "scripts"
            docs.mkdir(parents=True)
            examples.mkdir(parents=True)
            templates.mkdir(parents=True)

            (root / "README.md").write_text(
                "# awesome-agent-skills-ko\n\n"
                "## 프로젝트 소개 / Project overview\n"
                "python3 templates/scripts/validate_template.py\n"
                "examples/quickstart.md\n",
                encoding="utf-8",
            )
            for path in validate_template.REQUIRED_FILES:
                file_path = root / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                if not file_path.exists():
                    file_path.write_text("English mirror:\n", encoding="utf-8")
            errors = validate_template._check_quickstart_validation_command(root)
            self.assertTrue(any("first-screen in 3 lines section" in error for error in errors))


class AudienceValueMapValidationTests(unittest.TestCase):

    def test_audience_value_map_requires_operator_and_one_line_rule_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            docs.mkdir()
            (root / "README.md").write_text("## 프로젝트 소개 / Project overview\npython3 templates/scripts/validate_template.py\n", encoding="utf-8")
            (root / "CONTRIBUTING.md").write_text("# 기여 가이드 / Contributing\nEnglish mirror:\n", encoding="utf-8")
            for rel in [
                "ROADMAP.md",
                "CURATION_POLICY.md",
                "TEMPLATE_STANDARD.md",
                "BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                "README_TOP_CALLOUTS.md",
                "PROJECT_OVERVIEW.md",
                "PROJECT_ENTRY_PATHS.md",
                "PROJECT_DIRECTION.md",
                "README_INFORMATION_ARCHITECTURE.md",
                "README_FIRST_SCREEN_CHECKLIST.md",
                "README_FIRST_SCREEN_SCRIPT.md",
                "README_USER_JOURNEYS.md",
                "README_FAST_PATHS.md",
            ]:
                (docs / rel).write_text("placeholder\nEnglish mirror:\n", encoding="utf-8")
            examples = root / "examples"
            examples.mkdir()
            (examples / "pr-evidence-mini-walkthrough.md").write_text("## 목적 (한국어)\n## Purpose (English)\n", encoding="utf-8")
            (examples / "quickstart.md").write_text("English mirror:\n## Copyable first command\n", encoding="utf-8")
            (docs / "README_AUDIENCE_VALUE_MAP.md").write_text(
                "# README 대상 사용자-가치 맵 / README audience-value map\n\n## 한국어 기준 / Korean-first map\n- 탐색형 방문자\n- 기여형 방문자\n\n## English mirror\n- Contributors\n",
                encoding="utf-8",
            )

            errors = validate_template._check_bilingual_markers(root)

            self.assertTrue(any("docs/README_AUDIENCE_VALUE_MAP.md" in error and "운영형 방문자" in error for error in errors))
            self.assertTrue(any("docs/README_AUDIENCE_VALUE_MAP.md" in error and "One-line rule" in error for error in errors))


class FirstScreenWireframeValidationTests(unittest.TestCase):

    def test_wireframe_doc_requires_first_screen_structure_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            docs.mkdir()
            (root / "README.md").write_text("## 프로젝트 소개 / Project overview\npython3 templates/scripts/validate_template.py\n", encoding="utf-8")
            (root / "CONTRIBUTING.md").write_text("# 기여 가이드 / Contributing\nEnglish mirror:\n", encoding="utf-8")
            for rel in [
                "ROADMAP.md",
                "CURATION_POLICY.md",
                "TEMPLATE_STANDARD.md",
                "BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                "README_TOP_CALLOUTS.md",
                "README_AUDIENCE_VALUE_MAP.md",
                "PROJECT_OVERVIEW.md",
                "PROJECT_ENTRY_PATHS.md",
                "PROJECT_DIRECTION.md",
                "README_INFORMATION_ARCHITECTURE.md",
                "README_FIRST_SCREEN_CHECKLIST.md",
                "README_FIRST_SCREEN_SCRIPT.md",
                "README_USER_JOURNEYS.md",
                "README_FAST_PATHS.md",
            ]:
                (docs / rel).write_text("placeholder\nEnglish mirror:\n", encoding="utf-8")
            (docs / "README_FIRST_SCREEN_WIREFRAME.md").write_text(
                "# README 첫 화면 와이어프레임 / README first-screen wireframe\n\n## 상단 1스크린 구조 / First-screen structure\n",
                encoding="utf-8",
            )
            examples = root / "examples"
            examples.mkdir()
            (examples / "pr-evidence-mini-walkthrough.md").write_text("## 목적 (한국어)\n## Purpose (English)\n", encoding="utf-8")
            (examples / "quickstart.md").write_text("English mirror:\n## Copyable first command\n", encoding="utf-8")

            errors = validate_template._check_bilingual_markers(root)

            self.assertTrue(any("docs/README_FIRST_SCREEN_WIREFRAME.md" in error and "What moves lower" in error for error in errors))
            self.assertTrue(any("docs/README_FIRST_SCREEN_WIREFRAME.md" in error and "Maintenance prompts" in error for error in errors))



    def test_readme_requires_featured_category_map_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace(
                "docs/README_FEATURED_CATEGORY_MAP.md",
                "docs/MISSING_FEATURED_CATEGORY_MAP.md",
                1,
            )
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("docs/README_FEATURED_CATEGORY_MAP.md" in error for error in errors))


    def test_readme_requires_featured_example_paths_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace(
                "docs/README_FEATURED_EXAMPLE_PATHS.md", "docs/MISSING_FEATURED_EXAMPLE_PATHS.md"
            )
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 160 lines must link docs/README_FEATURED_EXAMPLE_PATHS.md so featured example paths stay attached to the intro-first landing block",
                errors,
            )

    def test_check_quickstart_validation_command_requires_landing_quickstart_map_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_LANDING_QUICKSTART_MAP.md", "docs/MISSING_LANDING_QUICKSTART_MAP.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 140 lines must link docs/README_LANDING_QUICKSTART_MAP.md so intro/audience/value/categories/quick-start flow stays reusable near the landing block",
                errors,
            )

    def test_check_quickstart_validation_command_requires_project_overview_faq_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_PROJECT_OVERVIEW_FAQ.md", "docs/MISSING_PROJECT_OVERVIEW_FAQ.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 80 lines must link docs/README_PROJECT_OVERVIEW_FAQ.md so first-time visitors can resolve intro/audience/quick-start questions without scrolling into governance sections",
                errors,
            )

    def test_check_quickstart_validation_command_requires_project_positioning_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_PROJECT_POSITIONING.md", "docs/MISSING_PROJECT_POSITIONING.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 140 lines must link docs/README_PROJECT_POSITIONING.md so the landing block keeps an explicit project-value positioning handoff before governance-heavy sections",
                errors,
            )

    def test_check_quickstart_validation_command_requires_project_starter_pack_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_PROJECT_STARTER_PACK.md", "docs/MISSING_PROJECT_STARTER_PACK.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 80 lines must link docs/README_PROJECT_STARTER_PACK.md so the project-intro starter pack stays visible in the landing block",
                errors,
            )

    def test_check_quickstart_validation_command_requires_persona_quickstart_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_PROJECT_QUICKSTART_PERSONAS.md", "docs/MISSING_PROJECT_QUICKSTART_PERSONAS.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 100 lines must link docs/README_PROJECT_QUICKSTART_PERSONAS.md so role-based first sentence/command/doc handoff stays visible in the intro-first landing block",
                errors,
            )

    def test_check_quickstart_validation_command_requires_first_action_matrix_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_FIRST_ACTION_MATRIX.md", "docs/MISSING_FIRST_ACTION_MATRIX.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertTrue(any("docs/README_FIRST_ACTION_MATRIX.md" in error for error in errors))

    def test_check_quickstart_validation_command_requires_first_visit_pack_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_FIRST_VISIT_PACK.md", "docs/MISSING_FIRST_VISIT_PACK.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 100 lines must link docs/README_FIRST_VISIT_PACK.md so first-visit starter bundles stay attached to the intro-first landing block",
                errors,
            )

    def test_check_quickstart_validation_command_requires_project_overview_faq_link_within_first_eighty_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_PROJECT_OVERVIEW_FAQ.md", "docs/MISSING_PROJECT_OVERVIEW_FAQ.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 80 lines must link docs/README_PROJECT_OVERVIEW_FAQ.md so first-time visitors can resolve intro/audience/quick-start questions without scrolling into governance sections",
                errors,
            )

    def test_validate_template_requires_project_quickstart_personas_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            for rel_path in validate_template.REQUIRED_FILES:
                if rel_path == "docs/README_PROJECT_QUICKSTART_PERSONAS.md":
                    continue
                path = root / rel_path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("placeholder\n", encoding="utf-8")

            errors = validate_template._check_required_files(root)

            self.assertIn("docs/README_PROJECT_QUICKSTART_PERSONAS.md", errors)

    def test_validate_template_requires_project_starter_pack_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            docs = root / "docs"
            examples = root / "examples"
            templates_scripts = root / "templates" / "scripts"
            docs.mkdir(parents=True, exist_ok=True)
            examples.mkdir(parents=True, exist_ok=True)
            templates_scripts.mkdir(parents=True, exist_ok=True)

            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
            (root / "README.md").write_text(readme, encoding="utf-8")
            for required in [
                "CONTRIBUTING.md",
                "docs/ROADMAP.md",
                "docs/CURATION_POLICY.md",
                "docs/TEMPLATE_STANDARD.md",
                "docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md",
                "docs/README_TOP_CALLOUTS.md",
                "docs/README_AUDIENCE_VALUE_MAP.md",
                "docs/README_PROJECT_VALUE_QUICKCHECK.md",
                "docs/README_PROJECT_INTRO_60S.md",
                "docs/README_PROJECT_OVERVIEW_FAQ.md",
                "docs/README_VALUE_PROOF_POINTS.md",
                "docs/README_LANDING_QUICKSTART_MAP.md",
                "docs/README_PROJECT_INTRO_BLUEPRINT.md",
                "docs/README_PROJECT_POSITIONING.md",
                "docs/README_FIRST_VISIT_PACK.md",
                "docs/README_FIRST_SCREEN_MAP.md",
                "docs/README_FIRST_VISITOR_PROMISES.md",
                "docs/README_FIRST_VISITOR_ROUTES.md",
                "docs/README_FIRST_SCREEN_DECISION_TREE.md",
                "docs/README_ROLE_STARTERS.md",
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
            ]:
                (root / required).write_text("ok", encoding="utf-8")

            errors = validate_template._check_required_files(root)

            self.assertIn("docs/README_PROJECT_STARTER_PACK.md", errors)

    def test_check_quickstart_validation_command_requires_intro_first_maintenance_loop_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8").replace("docs/README_INTRO_FIRST_MAINTENANCE_LOOP.md", "docs/MISSING_README_INTRO_FIRST_MAINTENANCE_LOOP.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 140 lines must link docs/README_INTRO_FIRST_MAINTENANCE_LOOP.md so intro-first maintenance guidance stays attached to the landing block",
                errors,
            )


    def test_validate_template_requires_first_screen_map_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            for rel_path in validate_template.REQUIRED_FILES:
                path = root / rel_path
                path.parent.mkdir(parents=True, exist_ok=True)
                source = Path(__file__).resolve().parents[1] / rel_path
                path.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

            readme = (root / "README.md").read_text(encoding="utf-8").replace("docs/README_FIRST_SCREEN_MAP.md", "docs/MISSING_FIRST_SCREEN_MAP.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 120 lines must link docs/README_FIRST_SCREEN_MAP.md so the intro -> audience -> value -> examples -> quick-start order stays visible during landing rewrites",
                errors,
            )

    def test_validate_template_requires_fast_intro_link_near_top(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            for rel_path in validate_template.REQUIRED_FILES:
                path = root / rel_path
                path.parent.mkdir(parents=True, exist_ok=True)
                source = Path(__file__).resolve().parents[1] / rel_path
                path.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

            readme = (root / "README.md").read_text(encoding="utf-8").replace("docs/README_PROJECT_FAST_INTRO.md", "docs/MISSING_PROJECT_FAST_INTRO.md")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_template._check_quickstart_validation_command(root)

            self.assertIn(
                "README.md: the first 90 lines must link docs/README_PROJECT_FAST_INTRO.md so the compact project intro source-of-truth stays attached to the intro-first landing block",
                errors,
            )
