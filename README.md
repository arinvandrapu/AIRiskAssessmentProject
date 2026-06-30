# AI Governance Risk Assessment

A simulated **AI governance risk assessment** of a fictional company (**FakeOrg**), built as a
portfolio project. It models a real GRC engagement end-to-end — inventory an organization's AI
use, assess governance maturity against the **NIST AI RMF**, review it against the **EU AI Act**,
and produce a scored report with a gap register and improvement roadmap — all driven by a small,
tested Python tool (`airisk`).

> **⚠️ Synthetic data.** FakeOrg is invented. All organization details, evidence, and findings are
> fictional. This is a personal project that models what a real assessment looks like — it is not
> an assessment of any real company.

## What this project demonstrates

Two skill sets in one artifact:

- **GRC / AI governance** — modelling the NIST AI RMF (all 72 subcategories) and the EU AI Act
  (risk classification + deployer/provider obligations), scoring maturity, and turning findings
  into a prioritized, owner-assigned roadmap.
- **Engineering** — a clean, tested Python CLI that makes the assessment *reproducible*: the data
  lives as YAML, and one command regenerates the whole report.

The key idea: **`airisk` does the paperwork, not the judgment.** A human analyst decides each
control rating from the evidence; the tool validates the data, computes the maturity math,
classifies each use case under the EU AI Act, and renders the report and chart.

## Results at a glance (FakeOrg, synthetic)

| Metric | Result |
|---|---|
| Overall NIST AI RMF maturity | **11.4%** (emerging) |
| Weakest function | **Measure — 7.5%** (no testing, monitoring, or bias evaluation) |
| By function | Govern 10.5% · Map 13.9% · Measure 7.5% · Manage 15.4% |
| Gaps identified | **16** — 7 High · 6 Medium · 3 Low |
| Improvement actions | **10**, prioritized with owners + target dates |

![NIST AI RMF maturity by function](reports/maturity-chart.png)

**Headline finding:** FakeOrg's highest-risk system — an AI résumé-screening tool classified
**high-risk** under the EU AI Act (Annex III, employment) — runs with no bias/fairness testing,
no defined human-oversight procedure, and no candidate notification.

📄 **Read the full assessment:** [`reports/final-report.md`](reports/final-report.md) ·
[`reports/scorecard.md`](reports/scorecard.md)

## How it works

```
data/ + frameworks/  ──►  airisk assess  ──►  reports/
(YAML: org, inventory,    (validate, score,    (scorecard.md,
 control ratings,          render, chart)       final-report.md,
 framework catalogs)                            maturity-chart.png)
```

Maturity scoring: each control is rated **Met (1.0) / Partial (0.5) / Not Met (0.0) /
Not Applicable (excluded)**, rolled up subcategory → category → function.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

airisk validate            # schema-check every YAML input
airisk init-assessment     # generate the blank control-rating worksheet
airisk assess              # score + render reports/ and the maturity chart
```

Run the tests with `pytest` and lint with `ruff check src tests`.

## Repository layout

| Path | Contents |
|---|---|
| `data/` | FakeOrg profile, AI use-case inventory, control ratings, gaps, roadmap |
| `frameworks/` | NIST AI RMF (72 subcategories) + EU AI Act reference catalogs |
| `evidence/` | Synthetic evidence artifacts (policies, vendor docs, SOPs) |
| `src/airisk/` | The Python tool (pydantic models, scoring, Jinja2 report, chart, CLI) |
| `tests/` | pytest suite |
| `reports/` | Generated scorecard, report, and maturity chart |

## Frameworks & methodology

- **NIST AI RMF 1.0** — maturity scoring across the Govern / Map / Measure / Manage functions.
- **EU AI Act (Regulation (EU) 2024/1689)** — risk classification (prohibited / high-risk /
  limited / minimal) and obligation mapping for the high-risk and limited-risk use cases.

The engagement follows a real methodology: scope → AI use-case inventory → maturity assessment →
EU AI Act review → gap register (severity-rated) → improvement roadmap → report.

## Skills & tools demonstrated

- **GRC / AI governance:** NIST AI RMF maturity assessment, EU AI Act risk classification &
  obligations mapping, gap analysis, severity prioritization, improvement roadmaps
- **Python:** pydantic v2, Typer CLI, Jinja2, matplotlib, pytest, ruff, packaged with hatchling

## Future work

- Add ISO/IEC 42001 (AI management system) as a second maturity lens.
- Expand the use-case inventory and evidence base.
- Export the report to PDF/HTML.

## License

MIT — see [`LICENSE`](LICENSE). All assessment data is synthetic.
