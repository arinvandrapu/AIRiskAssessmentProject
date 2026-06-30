---
tags: [project, phase2, engine, python]
---

# Phase 2 — `airisk` Engine (built)

The Python tool that turns Phase 1 data into the report. See [[phase2-plan]] and [[phase1-foundations]].

## Package (`src/airisk/`)
- **`models.py`** — pydantic v2 schemas; `Status` is a `StrEnum` (Met/Partial/Not Met/Not Applicable); `extra="forbid"` on hand-authored inputs so typos fail fast.
- **`loaders.py`** — `Paths` resolves files under a project root; `DataError` wraps missing-file / validation failures with friendly messages.
- **`scoring.py`** — `score_nist()` rolls maturity subcategory → category → function. NA excluded from denominator; unrated (None) tracked as coverage, not scored. EU AI Act tier-distribution + obligations helpers.
- **`report.py` + `templates/`** — Jinja2 → `scorecard.md` + `final-report.md`. Inline-joined strings are precomputed in Python to avoid `trim_blocks` line-merge bugs.
- **`chart.py`** — matplotlib (Agg) radar of maturity-by-function → PNG.
- **`cli.py`** — Typer: `validate`, `init-assessment`, `assess`. Entry point `airisk = airisk.cli:main`.

## Behaviour
`init-assessment` generates a blank 72-row `data/assessments/nist_ai_rmf.yaml`; `assess` scores it
and renders `reports/`. With blank ratings the report is an honest skeleton ("not assessed").

## Verification
ruff clean; 9 pytest tests pass (schema, scoring math incl. NA/unrated, end-to-end render).
Tests caught a real data bug: an unquoted YAML colon in `organization.yaml` parsed a list item
as a dict — now quoted.

## Gotchas
- Jinja `trim_blocks` eats the newline after a block-close tag; never end a content line with an
  inline `{% endfor %}`/`{% endif %}` — precompute the string instead.
- `reports/` + blank `data/assessments/` are committed (showcase artifacts); build/venv/cache gitignored.

## Next
Phase 3 — fill in honest control ratings, build the gap register + improvement roadmap.
