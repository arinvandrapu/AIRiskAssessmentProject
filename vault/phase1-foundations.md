---
tags: [project, phase1, data, frameworks]
---

# Phase 1 — Research & Data Foundations

What Phase 1 built (branch `feat/phase1-data`). See [[project-overview]] and [[architecture-overview]].

## Framework catalogs (`frameworks/`)
- **`nist_ai_rmf.yaml`** — full NIST AI RMF 1.0 catalog: 4 functions, 19 categories, **72 subcategories** (id, verbatim outcome title, plain-language intent). Scoring scale Met(1.0)/Partial(0.5)/Not Met(0.0)/NA(excluded); maturity rolls up subcategory → category → function. Sourced from NIST AI 100-1 + AIRC.
- **`eu_ai_act.yaml`** — Regulation (EU) 2024/1689: risk-tier decision tree (prohibited Art 5 / high-risk Annex I+III / limited Art 50 / minimal), provider + deployer high-risk obligations, GPAI obligations, and the binding Art 113 timeline.

## Key framework facts captured
- NIST AI RMF is **outcome-based, not pass/fail** — a Met/Partial/Not Met overlay is the standard way to score it.
- EU AI Act: **résumé screening is high-risk** (Annex III.4 employment) and profiling makes it *always* high-risk (Art 6(4)). Chatbots are **limited-risk** (Art 50(1) transparency).
- **Live-law caveat:** the "Digital Omnibus" amendment (Nov 2025) was in trilogue but NOT adopted as of this assessment, so the 2024/1689 dates remain binding. Recorded in the YAML `meta`.

## FakeOrg data (`data/`)
- **`organization.yaml`** — fictional ~520-person B2B SaaS, *emerging* AI governance (deliberately immature → real gaps), scope = internal + customer-facing.
- **`ai_inventory.yaml`** — 6 use cases: UC-01 résumé screening (high-risk), UC-02 support chatbot (limited), UC-03..06 minimal. Each carries owner, data, human-review, tier, and seeded gaps.

## Synthetic evidence (`evidence/`)
Four fictional artifacts (draft AI policy, vendor data sheet, chatbot SOP, partial vendor risk assessment) with intentional gaps the assessment cites. All clearly marked synthetic.

## Next
Phase 2 — build the Python scoring engine + report generator against these schemas.
