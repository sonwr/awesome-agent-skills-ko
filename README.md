# awesome-agent-skills-ko

한국어 기반 빌더를 위한 **에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음**입니다.

> 목표: 품질 높은 스킬을 쉽게 찾고, 재현 가능하게 검증하고, 실무 프로젝트에 바로 적용할 수 있게 만듭니다.

English mirror: A curated, practical collection of agent skills and runnable templates for Korean-speaking builders.

## 상단 핵심 콜아웃 / Top contributor callouts

- **한국어 기본 + 영어 병기 유지** — 문서 기본 언어는 한국어로 두고, 가능한 범위에서 같은 의미의 영어 미러를 함께 제공합니다.
- **최소 증빙 3종 필수** — 재현 명령 / 종료코드 / 핵심 출력을 PR 설명이나 문서에 남깁니다.
- **막힘까지 문서화** — 실패 원인만 적지 말고, 다음 실행에서 가장 먼저 할 일을 한 줄로 남깁니다.
- **상세 기준 링크** — 전체 리뷰 기준은 [docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md](docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md), 상단 문안 원본은 [docs/README_TOP_CALLOUTS.md](docs/README_TOP_CALLOUTS.md)에서 관리합니다.
- **처음 5분 기여 흐름** — README 상단 → 병기 체크리스트 → PR 증빙 워크스루 순서로 읽으면 첫 기여 온보딩을 5분 안에 끝낼 수 있습니다. 바로 실행 예시는 `examples/quickstart.md`로 이어집니다.

English mirror:

- **Keep Korean-first docs with English mirrors** so new contributors can review both local clarity and global portability.
- **Always record three evidence items**: reproduction command, exit code, and key output.
- **Document blockers with the next-run priority** instead of leaving failures context-free.
- **Use the full checklist** in [docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md](docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md); source callout copy lives in [docs/README_TOP_CALLOUTS.md](docs/README_TOP_CALLOUTS.md).
- **Use the first 5-minute contribution flow**: README top callouts → bilingual checklist → PR evidence walkthrough.

---

## Why this project exists

Most skill collections are either:

- too abstract to run immediately, or
- too coupled to one runtime/toolchain.

This repository focuses on a practical middle ground:

1. **curated skill patterns** that are easy to understand,
2. **runnable starter templates** that work with minimal setup,
3. **long-term governance** so quality does not decay as the repo grows.

---

## Project Direction (Long-term)

This project is intended to be maintained as a long-lived public resource, not a one-off list.

### 1) Curation over volume

We prioritize fewer, better entries.

Every added skill or template should prove:

- practical use-case clarity,
- reproducible setup,
- maintainability over time.

### 2) Runtime-portable standards

We avoid locking the collection to a single vendor runtime.

Each template should document:

- what is runtime-specific,
- what is portable,
- what needs adaptation.

### 3) Evidence-driven quality

No “looks good” approvals.

For template PRs, we require:

- setup steps,
- expected output,
- validation notes,
- limitations and known failure modes.

### 4) Contributor-friendly governance

The project should scale with community contributions.

We maintain:

- clear review criteria,
- issue labels for newcomers,
- stable docs for onboarding.

### 5) Sustainable release discipline

We prefer predictable progress over chaotic bursts.

Planned cadence:

- small, frequent updates,
- periodic curation cleanups,
- versioned snapshots of recommended template sets.

---

## Repository structure

```text
awesome-agent-skills-ko/
├─ README.md
├─ CONTRIBUTING.md
├─ docs/
│  ├─ ROADMAP.md
│  ├─ CURATION_POLICY.md
│  ├─ TEMPLATE_STANDARD.md
│  └─ BILINGUAL_CONTRIBUTION_CHECKLIST.md
├─ skills/
│  └─ (curated skill entries and references)
├─ templates/
│  └─ scripts/
│     └─ validate_template.py
├─ examples/
│  └─ quickstart.md
└─ .github/workflows/
   └─ ci.yml
```

---

## Initial scope (v0.1)

- Base curation policy
- Template quality standard
- Minimal validation script
- CI check for repository hygiene

---

## Quick start

한국어 문서를 기본으로 유지하면서 병기 품질까지 함께 검증하려면 아래 명령을 사용하세요.
English mirror: Run the command below to validate both baseline docs and bilingual quality markers.

## 처음 기여할 때 읽는 순서 / First-time contributor reading order

1. `README.md`의 상단 핵심 콜아웃과 빠른 기여 체크를 먼저 읽습니다. *(예상 1분 / Estimated 1 min)*
2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`에서 최소 증빙과 병기 규칙을 확인합니다. *(예상 2분 / Estimated 2 min)*
3. `examples/pr-evidence-mini-walkthrough.md`로 실제 PR 코멘트 증빙 형식을 복붙 가능한 수준으로 확인합니다. *(예상 2분 / Estimated 2 min)*

English mirror:

1. Read the top callouts and the quick contribution check in `README.md` first. *(Estimated 1 min / 예상 1분)*
2. Open `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` for the minimum evidence and bilingual rules. *(Estimated 2 min / 예상 2분)*
3. Use `examples/pr-evidence-mini-walkthrough.md` to copy a real PR evidence format before opening a review. *(Estimated 2 min / 예상 2분)*

```bash
git clone https://github.com/sonwr/awesome-agent-skills-ko.git
cd awesome-agent-skills-ko
python3 templates/scripts/validate_template.py
```

### 빠른 기여 체크 / Quick contribution check

- 한국어 기본 체크리스트: 문제 정의 / 재현 환경 / 예상 출력 / 실패 복구가 모두 문서에 있는지 먼저 확인하세요.
- English mirror: Before opening a PR, verify that the doc includes problem statement, reproducible environment, expected output, and failure recovery.
- 자세한 체크리스트: [docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md](docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md)

---

## What "done" looks like for each contribution

A contribution is acceptable when:

1. purpose is explicit,
2. setup is reproducible,
3. expected output is documented,
4. risks/limitations are written,
5. review checklist passes.

---

## 실무용 기여 체크리스트 / Practical contribution checklist

- 한국어 기본 + 영어 병기 체크리스트: [docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md](docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md)
- English mirror: Use the same checklist to keep Korean-first docs and English mirrors synchronized in every PR.
- 한국어/영어 공통 최소 증빙(명령/종료코드/핵심 출력) 섹션을 체크리스트에 포함해 리뷰 재현성을 높였습니다.
- 체크리스트 문서에 PR 코멘트 예시(한/영)를 추가해 신규 기여자가 바로 복붙 가능한 증빙 포맷을 제공합니다.
- 미니 워크스루 예시: [examples/pr-evidence-mini-walkthrough.md](examples/pr-evidence-mini-walkthrough.md) (한/영 동시 제공)
- 템플릿 검증 스크립트는 위 워크스루 문서의 한/영 핵심 섹션 마커까지 함께 점검합니다.

## Roadmap summary

See [docs/ROADMAP.md](docs/ROADMAP.md) for phase details.

- **Phase 1**: solid baseline + contribution rails
- **Phase 2**: category expansion + benchmark examples
- **Phase 3**: quality scoring and periodic curation reports
- **Phase 4**: ecosystem integration and community-maintained packs

---

## License

MIT
