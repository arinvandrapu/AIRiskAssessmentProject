# Project Architecture — AI Governance Risk Assessment (FakeOrg)

> **All data in this project is fictional/synthetic.** FakeOrg is an invented organization. This is a personal portfolio project that models what a real AI governance risk assessment looks like.

## 1. What this project is

A **simulated AI governance risk assessment engagement**, productized as a GitHub repo. The framing: *a GRC analyst was engaged to assess how FakeOrg uses AI, and this repo is their complete work product* — methodology, data, findings, and an improvement roadmap.

Two distinct senses of "tools" are involved:

- **Assessment frameworks (what we assess *with*)** — **NIST AI RMF** (governance maturity) and the **EU AI Act** (risk classification + obligations). These are the professional lenses; the *methodology*.
- **The software tool we *build*** — a Python CLI, `airisk`. It does **not** make judgments; it automates the mechanical work: validating data, computing maturity scores from the analyst's control ratings, classifying use cases under the EU AI Act, and generating the report + chart. The human assesses; the tool does the math and the paperwork.

## 2. How it works (end-to-end)

```
   INPUTS (structured YAML — the analyst's work)
   ┌─────────────────────────────────────────────┐
   │ data/organization.yaml    FakeOrg profile     │
   │ data/ai_inventory.yaml     AI use cases        │
   │ data/assessments/*.yaml    control ratings     │  ← Met / Partial / Not Met / NA
   │ frameworks/*.yaml          NIST + EU AI Act maps│    + evidence references
   └─────────────────────────────────────────────┘
                        │
                        ▼
        ┌──────────────────────────────────┐
        │  airisk assess   (Python tool)    │
        │  • pydantic validates the data    │
        │  • scoring engine → maturity %    │
        │  • EU AI Act tier + obligations   │
        │  • Jinja2 renders the report      │
        │  • matplotlib draws the chart     │
        └──────────────────────────────────┘
                        │
                        ▼
   OUTPUTS (generated — the deliverable)
   ┌─────────────────────────────────────────────┐
   │ reports/scorecard.md        maturity by func │
   │ reports/final-report.md      full assessment  │
   │ reports/maturity-chart.png   visual           │
   └─────────────────────────────────────────────┘
```

Core principle: **the assessment content lives as data, and one command regenerates the whole report.** Change a control rating, re-run `airisk assess`, and the scorecard + report update. This reproducibility is itself a signal of rigor.

## 3. The final deliverable on the repo

A public repo that reads as a complete, credible engagement:

| What a reviewer sees | Purpose |
|---|---|
| **README** (landing page) | The pitch — what it is, prominent synthetic-data disclaimer, skills/tools used, how to run it, screenshots, link to the report |
| **`reports/final-report.md`** | Headline artifact — exec summary, scope/methodology, AI inventory, NIST maturity findings, EU AI Act review, gap register, improvement roadmap |
| **`reports/maturity-chart.png`** | Visual maturity-by-function chart |
| **`data/`** | Structured inputs — methodology is rigorous, not hand-waved |
| **`frameworks/`** | NIST + EU AI Act reference maps assessed against |
| **`evidence/`** | Synthetic policies/SOPs/vendor docs — shows familiarity with real evidence |
| **`src/` + `tests/`** | The Python tool — demonstrates building *and* assessing |

The deliverable is three things at once: a professional GRC report, a clean dataset/methodology, and a working tool.

## 4. Methodology (engagement steps)

1. **Scope** — unit; internal / customer-facing / both; timeframe; depth; in/out of scope
2. **AI use-case inventory** — tool/model/vendor, purpose, owner, data used, human review, risk tier; stakeholders + evidence
3. **Assess maturity** — NIST AI RMF subcategories scored Met / Partial / Not Met / N/A; EU AI Act risk-tier + obligations review
4. **Gap register** — describe → map to framework → risk/impact → evidence → severity (High/Med/Low)
5. **Improvement roadmap** — action, owner, target date, resources, success measure
6. **Report** — exec summary, scope/methodology, inventory, NIST findings, EU AI Act review, key gaps/risks, improvement plan

## 5. Project roadmap

| Phase | Branch / PR | What gets built | Deliverable |
|---|---|---|---|
| **0 — Foundations** | `feat/foundations-spec` | Locked decisions (ADRs), build plan, this architecture doc | Vault ADRs, `tasks/todo.md`, `architecture/` |
| **1 — Research & data** | `feat/phase1-data` | Grounded NIST/EU AI Act research → framework maps; design FakeOrg + AI inventory; synthetic evidence | `frameworks/`, `data/`, `evidence/` |
| **2 — Engine** | `feat/scoring-engine` | pydantic schemas, scoring engine, Jinja2 renderer, chart, Typer CLI, pytest | Working `airisk assess` (renders an empty report) |
| **3 — Assessment** | `feat/assessment` | Score NIST controls honestly; EU AI Act review; gap register; improvement roadmap | Filled `data/assessments/` → generated report |
| **4 — Showcase** | `feat/showcase-readme` | Executive-summary polish; portfolio README; screenshots; make repo public | Recruiter-ready public repo |

Each phase: plan → user approval → build → PR. Never push to `main`.

## 6. Tech stack

Python 3.11+ · pydantic v2 (data models/validation) · Typer (CLI) · Jinja2 (report rendering) · matplotlib (maturity chart) · pytest (tests) · ruff (lint).

## 7. Frameworks assessed against

- **NIST AI RMF** — maturity scoring across the Govern / Map / Measure / Manage functions.
- **EU AI Act** — risk classification (prohibited / high-risk / limited-transparency / minimal) + obligations review.
- **ISO/IEC 42001** — out of scope for v1; noted as future work.

See `vault/architecture-decisions.md` for the decision record (ADR-001..007).
