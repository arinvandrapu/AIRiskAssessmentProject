# AI Governance Risk Assessment 

A simulated **AI governance risk assessment** of a fictional company (**FakeOrg**), built as a
portfolio project. It models a real GRC engagement end-to-end: inventory an organization's AI
use, assess governance maturity against **NIST AI RMF**, review it against the **EU AI Act**,
and produce a scored report — all driven by a small Python tool.

> **⚠️ Synthetic data.** FakeOrg is invented. All organization details, evidence, and findings
> are fictional. This is a personal project modeling what a real assessment looks like — it is
> not an assessment of any real company.

## How it works

```
data/ + frameworks/  ──►  airisk assess  ──►  reports/
(YAML: org, inventory,    (validate, score,    (scorecard.md,
 control ratings,          render, chart)       final-report.md,
 framework catalogs)                            maturity-chart.png)
```

The assessment content lives as structured YAML; the `airisk` tool validates it, computes NIST
AI RMF maturity (Met / Partial / Not Met / N/A → % per function), classifies each use case under
the EU AI Act, and generates the report and maturity chart.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

airisk validate            # schema-check every YAML input
airisk init-assessment     # generate the blank control-rating worksheet
airisk assess              # score + render reports/ and the maturity chart
```

## Repository layout

| Path | Contents |
|---|---|
| `data/` | FakeOrg profile, AI use-case inventory, control ratings |
| `frameworks/` | NIST AI RMF (72 subcategories) + EU AI Act reference catalogs |
| `evidence/` | Synthetic evidence artifacts (policies, vendor docs, SOPs) |
| `src/airisk/` | The Python tool (pydantic models, scoring, Jinja2 report, CLI) |
| `tests/` | pytest suite |
| `reports/` | Generated scorecard, report, and chart |

## Skills & tools demonstrated

- **GRC / AI governance:** NIST AI RMF maturity assessment, EU AI Act risk classification &
  obligations mapping, gap analysis, improvement roadmaps
- **Python:** pydantic v2, Typer CLI, Jinja2, matplotlib, pytest, ruff, packaged with hatchling

## Status

Built incrementally (see `tasks/todo.md`):

- ✅ Phase 1 — framework catalogs + FakeOrg data + evidence
- ✅ Phase 2 — `airisk` scoring engine + report generator (this)
- ⏳ Phase 3 — score the controls; gap register + improvement roadmap
- ⏳ Phase 4 — showcase polish
