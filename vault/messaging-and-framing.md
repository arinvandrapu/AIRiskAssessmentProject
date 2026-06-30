---
tags: [project, messaging, readme, report]
---

# Messaging & Framing (use in README + final report)

Plain-English framing approved by the user. Reuse this language in the portfolio README
(Phase 4) and the report's executive summary / methodology (Phase 3). See [[airisk-explainer]]
context in [[phase2-engine]].

## One-liner
A Python CLI that reads AI-assessment data (YAML) and automatically produces the scored
report, scorecard, and maturity chart — so the assessment is reproducible, not hand-assembled.

## The core idea (lead with this)
**`airisk` does the paperwork, not the judgment.** A human analyst reads the evidence and
decides each control rating (e.g. "GOVERN 1.1 → Partial"); the tool validates the data, computes
the maturity math, classifies use cases under the EU AI Act, and renders the report. This mirrors
how real GRC tooling works, and makes the whole assessment **reproducible** — change a rating,
re-run one command, the report updates.

## Inputs → outputs
`data/` + `frameworks/` (YAML: org, inventory, control ratings, framework catalogs)
→ `airisk assess` (validate, score, classify, render) → `reports/` (scorecard, final report, chart).

## Three commands
- `airisk validate` — schema-check every YAML input (catch typos early).
- `airisk init-assessment` — generate the blank 72-control worksheet.
- `airisk assess` — score + render the report and chart.

## Mini-example (good for README)
Rate `GOVERN 1.1 = Met`, `1.2 = Partial`, `1.3 = Not Met` → weights 1.0 / 0.5 / 0.0 →
average 50% maturity for that group → rolled up across categories/functions → drawn on the radar.

## Why it's in the portfolio (the pitch)
Signals **two skills at once**: GRC depth (models NIST AI RMF + the EU AI Act correctly) AND
engineering (clean, tested Python — pydantic, Typer, Jinja2, pytest). Most candidates show one.
