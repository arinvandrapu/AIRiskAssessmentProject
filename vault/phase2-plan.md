---
tags: [project, phase2, plan, engine]
---

# Phase 2 Plan — `airisk` Scoring Engine + Report Generator

The build plan for the Python tool. Status: **awaiting user approval before implementation.**
See [[phase1-foundations]] (inputs this consumes) and [[architecture-overview]].

## Goal
A tested Python CLI that ingests Phase 1 YAML (`data/`, `frameworks/`) and *generates* the
scorecard, final report, and maturity chart. End of Phase 2 = pipeline runs end-to-end and
renders a report **skeleton** (controls present but unrated). Honest ratings come in Phase 3.

## Package layout
`src/airisk/` → `models.py` (pydantic v2 schemas), `loaders.py` (load + validate YAML),
`scoring.py` (maturity rollups + EU AI Act helpers), `report.py` + `templates/` (Jinja2 → Markdown),
`chart.py` (matplotlib radar), `cli.py` (Typer). Plus `tests/`, `pyproject.toml`.

## CLI
- `airisk validate` — schema-validate every YAML file.
- `airisk init-assessment` — generate blank `data/assessments/nist_ai_rmf.yaml` (72 subcats, status null) for Phase 3.
- `airisk assess` — load org + inventory + frameworks + ratings → maturity → render `reports/{scorecard.md, final-report.md, maturity-chart.png}`.

## Scoring
Per-subcategory rating → weight (Met 1.0 / Partial 0.5 / Not Met 0.0); NA excluded from denominator;
null/unrated reported as "not assessed". Roll up subcategory → category → function → overall %.

## Tests
pytest: schema (good/bad fixtures), scoring math (known inputs), NA handling, end-to-end render smoke test. ruff-clean.

## Defaults (override on request)
- Chart = radar/spider of maturity-by-function (bar is the alternative).
- Phase 2 emits the blank assessment template so `assess` runs now; report shows "not yet assessed".

## Stack
Python 3.11+, pydantic, pyyaml, typer, jinja2, matplotlib, pytest, ruff.
