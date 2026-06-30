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
- [x] Open Phase 2 PR; signal explicitly when complete + ready to merge

### Phase 3 — The assessment content (branch `feat/phase3`) — BUILT, IN REVIEW
**Data:**
- [x] `data/assessments/nist_ai_rmf.yaml` — all 72 subcategories rated honestly (→ 11.4% overall)
- [x] `data/assessments/eu_ai_act.yaml` — per-use-case tier + high-risk obligation statuses
- [x] `data/gaps.yaml` — 16-gap register (7 High / 6 Medium / 3 Low)
- [x] `data/roadmap.yaml` — 10 prioritized improvement actions
- [x] `data/findings.yaml` — authored executive-summary narrative + key findings
**Code (`airisk`):**
- [x] Models + loaders for gaps, roadmap, EU assessment, findings (optional → skeleton still works)
- [x] Scoring: gap counts by severity
- [x] Report templates: EU obligation tables + gap register + roadmap + real exec summary
- [x] Tests for the new logic (11 passing); ruff clean
- [x] Regenerated `reports/` with real scores + meaningful chart
- [x] Open Phase 3 PR; signal when complete + ready to merge

### Phase 4 — Showcase polish & report review (branch `feat/phase4`) — BUILT, IN REVIEW
Scope per user: finish the steps + review the reports; NOT making public / linking profile.
- [x] Polished portfolio README (framing, results snapshot, embedded chart, quickstart, structure)
- [x] Consistency checks (gaps↔controls↔roadmap, tiers) — pass
- [x] Independent subagent review; **fixed a critical EU-law error (FRIA Art 27) + 6 more**
- [x] Add LICENSE (MIT)
- [x] Final verification (validate + assess + pytest + ruff); regenerated reports
- [x] Open Phase 4 PR; signal when complete + ready to merge

---
