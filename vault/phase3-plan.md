---
tags: [project, phase3, plan, assessment]
---

# Phase 3 Plan — The Assessment Content

Turn the skeleton into a real assessment: honest control ratings, EU AI Act review, gap register,
and improvement roadmap — then extend `airisk` to render them. Status: **awaiting approval.**
See [[phase2-engine]], [[phase1-foundations]], and reuse [[messaging-and-framing]].

## Data to author (the assessment itself)
- **`data/assessments/nist_ai_rmf.yaml`** — rate all 72 subcategories honestly for FakeOrg's
  *emerging* posture (mostly Not Met/Partial, a few Met, a few N/A), each with evidence refs + notes.
  Target overall maturity ~low (realistic, not flattering).
- **`data/assessments/eu_ai_act.yaml`** — per use case: confirmed tier; for UC-01 (high-risk) map
  each provider/deployer obligation to met/gap; UC-02 (limited) the Art 50 status; minimal noted.
- **`data/gaps.yaml`** — gap register: id, title, description, framework mapping (NIST subcat / EU
  article), risk/impact, evidence, severity (High/Med/Low). ~12-18 gaps.
- **`data/roadmap.yaml`** — improvement actions: action, owner, target date, resources, success
  measure, linked gap(s), priority. ~8-12 actions grouped by theme.
- Short authored **executive-summary narrative** (synthetic) for credibility.

## Code to extend (`airisk`)
- `models.py` — add `Gap`, `RoadmapAction`, EU-assessment schemas.
- `loaders.py` — load the new files.
- `scoring.py` — gap counts by severity; attach EU obligation statuses.
- `report.py` + templates — populate report sections 5 (EU detail), 6 (gaps), 7 (roadmap);
  real exec summary; scorecard shows real maturity.
- `tests/` — gap counts, EU mapping, render includes gaps/roadmap.

## Verify
Run `airisk assess` → real maturity %, populated radar, gap register + roadmap in the report.
ruff clean, tests green.

## Defaults (override on request)
- FakeOrg scores honestly low (emerging) to surface real findings.
- ~12-18 gaps, ~8-12 roadmap actions.
- Exec summary = short authored synthetic narrative + computed top findings.

## Output
One PR (`feat/phase3`). Signal explicitly when complete + ready to merge.
