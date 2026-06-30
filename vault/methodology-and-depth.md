---
tags: [project, report, methodology, depth, hiring-feedback]
---

# Report Depth & Methodology (post hiring-manager review)

Enhancements made after a hiring-manager-perspective review flagged three concerns: no stated
scoring methodology, thin per-control rationale, and findings that needed more analysis. See
[[phase3-assessment]], [[messaging-and-framing]], [[phase4-showcase]].

## Added
- **Report §3 "How to read this report (scoring methodology)"** — rating scale (Met/Partial/Not
  Met/NA meanings + weights), the maturity formula, what each NIST function measures, and the gap
  severity rubric (impact × likelihood → High/Medium/Low).
- **Report §7 "Detailed findings"** — 3 deep-dives (résumé tool, governance root cause, chatbot
  transparency), each with regulatory hook → impact → affected population → recommendation. Driven by
  `data/findings.yaml` `detailed_findings` (new `DetailedFinding` model).
- **Per-gap severity rationale** — every gap in `data/gaps.yaml` now has `severity_rationale`
  (new optional `Gap.severity_rationale` field), rendered inline in the §8 gap table.
- **README** — new "Skills used & learned" section near the top; the "does the paperwork, not the
  judgment" framing + mini-example; a scoring-methodology summary; and a "Scope & limitations"
  honesty note (acknowledges the synthetic, self-authored nature).

## Verification
`airisk assess` regenerates cleanly; ruff clean; 11 pytest pass (incl. new assertions for the
methodology section, detailed findings, and per-gap rationale). Consistency unchanged (7H/6M/3L,
11.4%); every gap carries a rationale.

## Why
Directly closes the hiring-manager concerns: methodology answers "how/why did you score this";
detailed findings show analysis (the "so what"), not just findings; the scope note pre-empts the
"it's self-authored" critique by owning it.
