# Tasks — TODO

## Current Task: AI Governance Risk Assessment (FakeOrg)

**Goal:** Deliver a portfolio-grade, simulated AI governance risk assessment of a fictional org (**FakeOrg**) using synthetic data — NIST AI RMF maturity + EU AI Act review — with a Python tool that scores the controls and generates the report.

**Scope:** locked — see vault `architecture-decisions.md` (ADR-001..007).

**Process rule:** plan-before-build. Each phase's plan is approved before implementation. One feature branch + PR per phase. NEVER push to `main`. Synthetic data only.

---

### Phase 0 — Foundations & plan — DONE (merged)
- [x] Record locked decisions in vault (ADR-001..007), rename org → FakeOrg
- [x] Write the build plan
- [x] Plan sign-off from user

### Phase 1 — Research & data design — DONE (PR #5 merged)
- [x] Grounded research subagents: NIST AI RMF structure (72 subcategories) + EU AI Act obligations, risk tiers, timeline
- [x] Build framework reference maps under `frameworks/` (nist_ai_rmf.yaml, eu_ai_act.yaml)
- [x] Design FakeOrg profile + AI use-case inventory under `data/`
- [x] Add synthetic evidence artifacts under `evidence/`
- [x] Open + merge Phase 1 PR

### Phase 2 — Scoring engine + report generator (branch `feat/phase2-build`) — BUILT, IN REVIEW
- [x] `models.py` — pydantic v2 schemas (organization, inventory, framework catalog, ratings)
- [x] `loaders.py` — load + schema-validate YAML from `data/` and `frameworks/`
- [x] `scoring.py` — Met(1.0)/Partial(0.5)/Not Met(0)/NA(excluded) → maturity % rolled up subcategory → category → function; EU AI Act helpers
- [x] `report.py` + `templates/` — Jinja2 render to `reports/scorecard.md` + `reports/final-report.md`
- [x] `chart.py` — matplotlib radar chart → `reports/maturity-chart.png`
- [x] `cli.py` — Typer commands: `airisk validate`, `airisk init-assessment`, `airisk assess`
- [x] `init-assessment` generates blank `data/assessments/nist_ai_rmf.yaml` (72 subcats, status null)
- [x] pytest tests (schema, scoring math, NA handling, end-to-end render) — 9 passing + ruff clean
- [x] `pyproject.toml` with `airisk` entry point; `pip install -e .` works
- [x] Fixed a real data bug found by tests (unquoted YAML colon in organization.yaml)
- [ ] Open Phase 2 PR; signal explicitly when complete + ready to merge

### Phase 3 — The assessment content (branch `feat/phase3`) — PLAN AWAITING APPROVAL
Author the real assessment + extend `airisk` to render it. See vault `phase3-plan.md`.
**Data:**
- [ ] `data/assessments/nist_ai_rmf.yaml` — rate all 72 subcategories honestly (evidence + notes)
- [ ] `data/assessments/eu_ai_act.yaml` — per-use-case tier + high-risk obligation statuses
- [ ] `data/gaps.yaml` — gap register (id, mapping, risk/impact, evidence, severity H/M/L)
- [ ] `data/roadmap.yaml` — improvement actions (action/owner/date/resources/success measure)
- [ ] Short authored executive-summary narrative (synthetic)
**Code (`airisk`):**
- [ ] Models + loaders for gaps, roadmap, EU assessment
- [ ] Scoring: gap counts by severity; EU obligation statuses
- [ ] Report templates: populate EU detail + gap register + roadmap + real exec summary
- [ ] Tests for the new logic; ruff clean
- [ ] Regenerate `reports/` with real scores; open Phase 3 PR

### Phase 4 — Showcase (own PR; plan + approve first)  [use vault `messaging-and-framing.md`]
- [ ] Executive-summary final report
- [ ] Polished public README: overview, skills/tools, synthetic-data disclaimer, screenshots
- [ ] Final review pass; make repo public + link from profile README

---

**Review:** _(filled in on completion)_
