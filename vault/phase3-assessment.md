---
tags: [project, phase3, assessment, results]
---

# Phase 3 — The Assessment (built)

The real assessment content + renderer extensions. See [[phase3-plan]], [[phase2-engine]].

## Results (synthetic, by design)
- **Overall NIST AI RMF maturity: 11.4%** (72/72 assessed) — emerging org, deliberately low.
- By function: Govern 10.5% · Map 13.9% · **Measure 7.5% (weakest)** · Manage 15.4%.
- **16 gaps**: 7 High, 6 Medium, 3 Low. **10 roadmap actions**, prioritized.
- Headline finding: the high-risk résumé tool (EU Annex III.4) has no bias testing, no human
  oversight, no candidate notice, and no FRIA (Art 27).

## Data authored (`data/`)
- `assessments/nist_ai_rmf.yaml` — 72 ratings (Met/Partial/Not Met/NA) + evidence refs + notes.
- `assessments/eu_ai_act.yaml` — per use case: tier + deployer obligation statuses (UC-01 high-risk).
- `gaps.yaml` — gap register (id, mapping, risk, evidence, severity).
- `roadmap.yaml` — actions (owner, target, resources, success measure, addresses, priority).
- `findings.yaml` — executive-summary narrative + key findings.

## Code extended (`airisk`)
- `models.py` — `Severity`, `Gap`, `RoadmapAction`, `EUObligation`/`EUUseCaseAssessment`, `Findings`.
- `loaders.py` — optional loaders (return None if file absent → skeleton still renders).
- `scoring.py` — `gap_summary()` counts by severity.
- `report.py` + template — exec summary, EU obligation tables, gap register, roadmap.

## Verification
`airisk assess` → 11.4% with populated radar, gap table, roadmap. ruff clean; 11 pytest pass
(incl. full-report render + skeleton-without-phase3-data fallback + gap_summary).

## Scoring rationale (honesty)
Emerging org with no AI program → mostly Not Met; Partials where a general security/privacy/
vendor program gives incidental coverage; NA for human-subject testing + environmental (out of
scope). Tells a real "lots to do" story; roadmap sequences High-severity fixes first.

## Next
Phase 4 — showcase polish: portfolio README (use [[messaging-and-framing]]), screenshots, make public.
