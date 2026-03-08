# awesome-agent-skills-ko

A curated, practical collection of agent skills and runnable templates for Korean-speaking builders.

> Goal: make high-quality agent skills easy to discover, test, and operate in real projects.

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
│  └─ TEMPLATE_STANDARD.md
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

```bash
git clone https://github.com/sonwr/awesome-agent-skills-ko.git
cd awesome-agent-skills-ko
python3 templates/scripts/validate_template.py
```

---

## What "done" looks like for each contribution

A contribution is acceptable when:

1. purpose is explicit,
2. setup is reproducible,
3. expected output is documented,
4. risks/limitations are written,
5. review checklist passes.

---

## Roadmap summary

See [docs/ROADMAP.md](docs/ROADMAP.md) for phase details.

- **Phase 1**: solid baseline + contribution rails
- **Phase 2**: category expansion + benchmark examples
- **Phase 3**: quality scoring and periodic curation reports
- **Phase 4**: ecosystem integration and community-maintained packs

---

## License

MIT
