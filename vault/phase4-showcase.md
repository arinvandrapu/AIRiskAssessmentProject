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

## Independent review — done, findings fixed
An adversarial GRC reviewer (subagent) verified EU AI Act claims against the regulation and
recomputed all NIST math. NIST accuracy + internal consistency were confirmed solid. EU-law fixes
applied:
- **C-1 (critical): FRIA Art 27 was NOT legally required** for a private Annex III.4 (employment)
  deployer — Art 27 binds public bodies / public-service providers / Annex III 5(b)-(c). Reframed
  GAP-07 + ACT-07 to the binding **GDPR Art 35 DPIA**; UC-01 Art 27 obligation → Not Applicable with
  explanation; corrected findings.yaml exec summary + key findings. (The deliverable had contradicted
  its own framework file — the worst kind of error for a GRC portfolio.)
- **M-1:** profiling override re-cited Art 6(4) → **Art 6(3) final subparagraph**.
- **M-2:** Art 50(1) is a provider duty → UC-02 role set to **provider/operator** (FakeOrg assembles
  + brands the chatbot).
- **Minors:** maturity wording now "over 70 applicable subcategories (72 assessed; 2 N/A)";
  resolved MEASURE 3.3 double-count (GAP-15/16); anchored Art 86 to GAP-16/ACT-10; dropped provider
  Art 14 from deployer GAP-05; "AI use reviewed: both" → "internal and customer-facing".

## Verified after fixes
`airisk assess` regenerates cleanly; consistency re-check passes (gaps↔controls↔roadmap, 7H/6M/3L
unchanged, 11.4% intact); ruff clean; 11 pytest pass.

## Lesson
Author-time EU AI Act details need verification against the regulation — applicability of an
obligation (who it binds) is as important as its existence. The independent review caught a
phantom mandatory obligation that internal consistency checks could not.
