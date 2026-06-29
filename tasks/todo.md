# Tasks — TODO

## Current Task: AI Governance Risk Assessment (FakeOrg)

**Goal:** Deliver a portfolio-grade, simulated AI governance risk assessment of a fictional org (**FakeOrg**) using synthetic data — NIST AI RMF maturity + EU AI Act review — with a Python tool that scores the controls and generates the report.

**Scope:** locked — see vault `architecture-decisions.md` (ADR-001..007).

**Process rule:** plan-before-build. Each phase's plan is approved before implementation. One feature branch + PR per phase. NEVER push to `main`. Synthetic data only.

---

### Phase 0 — Foundations & plan (branch: `feat/foundations-spec`) — THIS PR
- [x] Record locked decisions in vault (ADR-001..007), rename org → FakeOrg
- [x] Write this build plan
- [ ] Get plan sign-off from user before any build

### Phase 1 — Research & data design (own PR; plan + approve first)
- [ ] Grounded research subagents: exact NIST AI RMF structure (functions/categories/subcategories) + current EU AI Act obligations, risk tiers, timeline
- [ ] Build framework reference maps under `frameworks/`
- [ ] Design FakeOrg profile + AI use-case inventory under `data/`
- [ ] Add synthetic evidence artifacts under `evidence/`

### Phase 2 — Scoring engine + report generator (own PR; plan + approve first)
- [ ] pydantic schemas: organization, inventory, assessment, gaps
- [ ] scoring engine: Met(1.0)/Partial(0.5)/Not Met(0)/NA(excluded) → maturity % per NIST function
- [ ] Jinja2 report renderer + maturity chart (matplotlib/SVG)
- [ ] Typer CLI: `airisk assess`
- [ ] pytest tests + ruff clean

### Phase 3 — The assessment content (own PR; plan + approve first)
- [ ] Score NIST AI RMF subcategories honestly, with synthetic evidence
- [ ] EU AI Act risk-tier + obligations review per use case
- [ ] Gap register (severity High/Med/Low)
- [ ] Improvement roadmap (action / owner / target date / resources / success measure)
- [ ] Generate scorecard + report into `reports/`

### Phase 4 — Showcase (own PR; plan + approve first)
- [ ] Executive-summary final report
- [ ] Polished public README: overview, skills/tools, synthetic-data disclaimer, screenshots
- [ ] Final review pass; make repo public + link from profile README

---

**Review:** _(filled in on completion)_
