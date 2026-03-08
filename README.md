# awesome-agent-skills-ko

한국어 기반 빌더를 위한 **에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음**입니다.

> 목표: 품질 높은 스킬을 쉽게 찾고, 재현 가능하게 검증하고, 실무 프로젝트에 바로 적용할 수 있게 만듭니다.

English mirror: A curated, practical collection of agent skills and runnable templates for Korean-speaking builders.

## 프로젝트 소개 / Project overview

이 저장소는 **한국어 기반 빌더를 위한 에이전트 스킬 큐레이션 + 실행 가능한 템플릿 모음**입니다.

- 무엇을 하나요? 검증 가능한 스킬/템플릿을 모으고, 한국어 기본 문서 흐름과 영어 미러까지 함께 제공합니다.
- 왜 필요한가요? "좋아 보이는 링크 모음"이 아니라, 바로 실행·검증·기여할 수 있는 출발점을 만들기 위해서입니다.

English mirror:
A curated collection of agent skills and runnable templates for Korean-speaking builders, with Korean-first docs and practical English mirrors.

## 대상 사용자 / Who this is for

- 한국어로 스킬/프롬프트/자동화 자산을 빠르게 탐색하고 싶은 개발자
- 공개 저장소에 재현 가능한 예시와 검증 명령까지 함께 남기고 싶은 기여자
- 특정 런타임에 잠기지 않는 휴대 가능한 스킬 구조를 찾는 팀

English mirror:
- Builders who want to discover skills, prompts, and automation assets in Korean first.
- Contributors who care about reproducible examples, validation commands, and review evidence.
- Teams looking for runtime-portable skill patterns instead of vendor-locked snippets.

## 제공 가치 / What you get

1. **큐레이션된 스킬 관점** — 무작정 많이 모으기보다 실무 적용성과 유지보수성을 먼저 봅니다.
2. **실행 가능한 템플릿** — quickstart, 검증 스크립트, PR 증빙 예시까지 연결된 형태로 제공합니다.
3. **병기/운영 가드레일** — 한국어 기본 문서와 영어 미러, 재현 증빙, 반복 작업 방지 흐름을 같이 관리합니다.

English mirror:
1. **Curated skill patterns** that optimize for practical reuse, not raw link volume.
2. **Runnable starter templates** connected to quickstart docs, validation scripts, and PR evidence examples.
3. **Governance rails** for Korean-first docs, English mirrors, reproducible evidence, and anti-repeat workflows.

## 빠른 시작 한눈에 보기 / Quick start at a glance

- 무엇부터 보면 되나요? **프로젝트 소개 → 대상 사용자 → 제공 가치 → 빠른 시작 명령** 순서로 1분 안에 핵심을 파악할 수 있습니다.
- 첫 실행 명령은 무엇인가요? `python3 templates/scripts/validate_template.py`
- 첫 PR 전에 무엇을 보나요? `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`, `examples/pr-evidence-mini-walkthrough.md`

English mirror:
- Where should I start? Read **project overview → audience → value → quick start command** to understand the repo in under a minute.
- What is the first command to run? `python3 templates/scripts/validate_template.py`
- What should I open before a first PR? `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`, `examples/pr-evidence-mini-walkthrough.md`

## 대표 카테고리와 예시 / Featured categories and examples

- **온보딩/기여 가이드** — `examples/quickstart.md`, `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- **리뷰 증빙 템플릿** — `examples/pr-evidence-mini-walkthrough.md`
- **큐레이션/운영 기준** — `docs/CURATION_POLICY.md`, `docs/TEMPLATE_STANDARD.md`, `docs/ROADMAP.md`

English mirror:
- **Onboarding and contribution guides** — `examples/quickstart.md`, `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`
- **Review evidence templates** — `examples/pr-evidence-mini-walkthrough.md`
- **Curation and governance standards** — `docs/CURATION_POLICY.md`, `docs/TEMPLATE_STANDARD.md`, `docs/ROADMAP.md`

## Quick start

### 처음 5분 기여 흐름 / First 5-minute contribution flow

- 1분: README 상단의 프로젝트 소개/대상 사용자/제공 가치를 훑습니다.
- 2분: 아래 quick start 검증 명령을 실행합니다.
- 2분: `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`와 `examples/pr-evidence-mini-walkthrough.md`를 열어 PR 증빙 형식을 확인합니다.

English mirror:
- Minute 1: scan the README overview, audience, and value sections.
- Minute 2-3: run the quick start validation command below.
- Minute 4-5: open `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` and `examples/pr-evidence-mini-walkthrough.md` to copy the PR evidence format.

한국어 문서를 기본으로 유지하면서 병기 품질까지 함께 검증하려면 아래 명령을 사용하세요.
English mirror: Run the command below to validate both baseline docs and bilingual quality markers.

```bash
git clone https://github.com/sonwr/awesome-agent-skills-ko.git
cd awesome-agent-skills-ko
python3 templates/scripts/validate_template.py
```

### 빠른 시작 후 바로 볼 문서 / What to open right after quick start

1. `examples/quickstart.md` — 첫 복붙 명령과 다음 읽기 순서
2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — 최소 증빙/병기 규칙
3. `examples/pr-evidence-mini-walkthrough.md` — PR 코멘트 예시

English mirror:
1. `examples/quickstart.md` — first copy-paste command and next reading step
2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` — minimum evidence and bilingual rules
3. `examples/pr-evidence-mini-walkthrough.md` — PR comment example

## 추천 시작 경로 / Recommended starting paths

### 빠른 선택 카드 / Quick chooser cards

**탐색형 / Explorer path**
- 목적: 프로젝트 가치와 카테고리를 30초 안에 파악
- 시작: 프로젝트 소개 → 대상 사용자 → 제공 가치 → 대표 카테고리
- 다음 이동: `examples/quickstart.md` → `docs/CURATION_POLICY.md`

English mirror:
- Goal: understand the project value and category map within 30 seconds.
- Start with the project overview → audience → value → featured categories.
- Next stop: `examples/quickstart.md` → `docs/CURATION_POLICY.md`

**기여형 / Contributor path**
- 목적: 첫 검증 명령부터 실행하고 빠르게 PR 준비
- 시작: quick start 검증 명령 실행
- 다음 이동: `examples/quickstart.md` → `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`

English mirror:
- Goal: run the first validation command immediately and prepare a PR fast.
- Start by running the quick start validation command.
- Next stop: `examples/quickstart.md` → `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`

### 1) 탐색부터 시작 / Start by exploring
- 먼저 볼 것: 프로젝트 소개 → 대상 사용자 → 제공 가치 → 대표 카테고리
- 추천 대상: "무엇이 들어 있는지" 먼저 알고 싶은 사용자/팀
- 다음 이동: `examples/quickstart.md` → `docs/CURATION_POLICY.md`

English mirror:
- Open the project overview, audience, value, and featured categories first.
- Best for users or teams deciding whether this collection fits their workflow.
- Next stop: `examples/quickstart.md` → `docs/CURATION_POLICY.md`

### 2) 바로 기여 시작 / Start contributing immediately
- 먼저 할 것: quick start 검증 명령 실행
- 추천 대상: 첫 PR을 빨리 열고 싶은 기여자
- 다음 이동: `examples/quickstart.md` → `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`

English mirror:
- Run the quick start validation command first.
- Best for contributors who want to open a first PR quickly.
- Next stop: `examples/quickstart.md` → `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` → `examples/pr-evidence-mini-walkthrough.md`


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

## 처음 기여할 때 읽는 순서 / First-time contributor reading order

1. `README.md`의 프로젝트 소개/빠른 시작/상단 콜아웃을 먼저 훑습니다. *(예상 1분 / Estimated 1 min)*
2. `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md`에서 최소 증빙과 병기 규칙을 확인합니다. *(예상 2분 / Estimated 2 min)*
3. `examples/pr-evidence-mini-walkthrough.md`로 실제 PR 코멘트 증빙 형식을 복붙 가능한 수준으로 확인합니다. *(예상 2분 / Estimated 2 min)*

English mirror:

1. Scan the project overview, quick start, and top contributor callouts in `README.md` first. *(Estimated 1 min / 예상 1분)*
2. Open `docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md` for the minimum evidence and bilingual rules. *(Estimated 2 min / 예상 2분)*
3. Use `examples/pr-evidence-mini-walkthrough.md` to copy a real PR evidence format before opening a review. *(Estimated 2 min / 예상 2분)*

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

## 상단 핵심 콜아웃 / Top contributor callouts


- **한국어 기본 + 영어 병기 유지** — 문서 기본 언어는 한국어로 두고, 가능한 범위에서 같은 의미의 영어 미러를 함께 제공합니다.
- **최소 증빙 3종 필수** — 재현 명령 / 종료코드 / 핵심 출력을 PR 설명이나 문서에 남깁니다.
- **막힘까지 문서화** — 실패 원인만 적지 말고, 다음 실행에서 가장 먼저 할 일을 한 줄로 남깁니다.
- **상세 기준 링크** — 전체 리뷰 기준은 [docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md](docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md), 상단 문안 원본은 [docs/README_TOP_CALLOUTS.md](docs/README_TOP_CALLOUTS.md)에서 관리합니다.
- **처음 5분 기여 흐름** — README 상단 → 병기 체크리스트 → PR 증빙 워크스루 순서로 읽으면 첫 기여 온보딩을 5분 안에 끝낼 수 있습니다. 바로 실행 예시는 `examples/quickstart.md`로 이어집니다.
- **상단 콜아웃 소스 동기화** — README 상단 핵심 콜아웃은 `docs/README_TOP_CALLOUTS.md`와 같은 메시지를 유지하며, 검증 스크립트로 드리프트를 바로 잡습니다.

English mirror:

- **Keep Korean-first docs with English mirrors** so new contributors can review both local clarity and global portability.
- **Always record three evidence items**: reproduction command, exit code, and key output.
- **Document blockers with the next-run priority** instead of leaving failures context-free.
- **Use the full checklist** in [docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md](docs/BILINGUAL_CONTRIBUTION_CHECKLIST.md); source callout copy lives in [docs/README_TOP_CALLOUTS.md](docs/README_TOP_CALLOUTS.md).
- **Use the first 5-minute contribution flow**: README top callouts → bilingual checklist → PR evidence walkthrough.

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
