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

### Phase 2 — Scoring engine + report generator (branch `feat/phase2-engine`) — PLAN AWAITING APPROVAL
Build the `airisk` Python CLI that ingests Phase 1 data and generates the report.
End state: pipeline runs end-to-end, rendering a report skeleton (controls present, unrated);
honest ratings come in Phase 3.

Package layout: `src/airisk/{models,loaders,scoring,report,chart,cli}.py` + `templates/` + `tests/` + `pyproject.toml`.

- [ ] `models.py` — pydantic v2 schemas (organization, inventory, framework catalog, assessment ratings, gaps)
- [ ] `loaders.py` — load + schema-validate YAML from `data/` and `frameworks/`
- [ ] `scoring.py` — Met(1.0)/Partial(0.5)/Not Met(0)/NA(excluded) → maturity % rolled up subcategory → category → function; EU AI Act tier/obligation helpers
- [ ] `report.py` + `templates/` — Jinja2 render to `reports/scorecard.md` + `reports/final-report.md`
- [ ] `chart.py` — matplotlib radar chart of maturity-by-function → `reports/maturity-chart.png`
- [ ] `cli.py` — Typer commands: `airisk validate`, `airisk init-assessment`, `airisk assess`
- [ ] `init-assessment` generates blank `data/assessments/nist_ai_rmf.yaml` (72 subcats, status null) for Phase 3
- [ ] pytest tests (schema, scoring math, NA handling, end-to-end render) + ruff clean
- [ ] `pyproject.toml` with `airisk` entry point; `pip install -e .` works
- [ ] Open Phase 2 PR; signal explicitly when complete + ready to merge

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
