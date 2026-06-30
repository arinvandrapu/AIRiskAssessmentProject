---
tags: [project, phase4, showcase, review]
---

# Phase 4 — Showcase Polish & Report Review (in progress)

Final phase. See [[phase4-plan]]; reuses [[messaging-and-framing]]; reviews [[phase3-assessment]].

## Done so far (commit a26414f)
- **Portfolio README** rewritten as the showcase landing page: pitch ("does the paperwork, not
  the judgment"), results-at-a-glance table, embedded maturity chart, headline finding, quickstart,
  repo structure, frameworks, skills/tools. Preserves the user's edited title.
- **MIT `LICENSE`** added (matches pyproject).
- **Internal consistency verified** (script): every gap is addressed by ≥1 roadmap action; every
  NIST-mapped gap is Not Met/Partial; inventory tiers match the EU assessment; ratings reconcile to
  11.4% (16 Partial, 54 Not Met, 2 N/A → 8.0/70).

## In progress
- **Independent reviewer subagent** checking EU AI Act / NIST accuracy. Key item flagged for it:
  whether **FRIA (Art 27)** actually applies to a private-sector *employment* deployer (Annex III.4)
  — Art 27 may only bind public bodies / public-service providers / Annex III 5(b)-(c). If confirmed,
  fix GAP-07, the UC-01 Art 27 obligation, findings.yaml, and roadmap ACT-07.

## Remaining
- Apply reviewer findings → regenerate reports → final verify (validate/assess/pytest/ruff) →
  open Phase 4 PR. Per user: NOT making public / linking profile.
