---
tags: [project, phase4, plan, showcase, review]
---

# Phase 4 Plan — Showcase Polish & Report Review

Final phase. Scope adjusted by user: **finish the steps + review the reports**; do NOT make the
repo public or link it from the profile. Status: **awaiting approval.** Reuse
[[messaging-and-framing]]; see [[phase3-assessment]].

## A. Portfolio README (the showcase landing page)
Rewrite README using the approved framing:
- One-liner + prominent synthetic-data disclaimer
- "What this demonstrates" pitch (GRC + engineering)
- Results snapshot: 11.4% maturity, embedded radar chart, 16 gaps, headline résumé-tool finding
- How it works diagram (data → airisk → reports) + quickstart (3 commands)
- Repo structure table; skills & tools; link to `reports/final-report.md`
- Short "future work" note (ISO 42001, etc.)

## B. Review the reports (QA / accuracy pass)
- **Consistency:** every gap traces to a Not Met/Partial control or EU gap; every gap is addressed
  by ≥1 roadmap action; EU obligation statuses align with ratings/evidence; inventory tiers match
  the EU assessment.
- **Accuracy:** spot-check NIST IDs/titles + EU article refs (Art 27 FRIA, Annex III.4); verify the
  longest verbatim NIST statements (MEASURE 2.5/2.6, MANAGE 4.1) per the Phase 1 reviewer note.
- **Polish:** rendered Markdown reads cleanly; disclaimers present; no orphaned placeholders.
- **Independent review:** run a review subagent to adversarially check the report for
  correctness/consistency/credibility; fix what it finds.

## C. Finishing touches
- Add `LICENSE` (MIT, matches pyproject).
- Final verification: `airisk validate` + `assess` + `pytest` + `ruff` all green; reports regenerate
  cleanly and consistently.

## Defaults (override on request)
- Embed the chart + a results snapshot in the README.
- Run an independent subagent review of the reports and fix findings before the PR.
- Repo stays private; "publish + link profile" left as a manual step for the user.

## Output
One PR (`feat/phase4`). Signal explicitly when complete + ready to merge.
