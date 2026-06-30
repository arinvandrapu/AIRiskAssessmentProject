# AI Governance Risk Assessment

A simulated **AI governance risk assessment** of a fictional company (**FakeOrg**), built as a
portfolio project. It models a real GRC engagement end-to-end — inventory an organization's AI
use, assess governance maturity against the **NIST AI RMF**, review it against the **EU AI Act**,
and produce a scored report with a gap register and prioritized roadmap — all driven by a small,
tested Python tool (`airisk`).

> **NOTE: Synthetic data.** FakeOrg is invented. All organization details, evidence, and findings are
> fictional. This is a personal project that models what a real assessment looks like, it is not
> an assessment of any real company.

## Skills used & learned

**Used (demonstrated here)**
- **GRC / AI governance:** AI risk-assessment methodology, control maturity scoring, gap analysis
  with severity rating, improvement-roadmap planning.
- **Frameworks:** NIST AI RMF 1.0 (all 72 subcategories) and the EU AI Act (Regulation (EU)
  2024/1689) — risk classification and provider/deployer obligation mapping.
- **Engineering:** Python (pydantic v2, Typer, Jinja2, matplotlib), testing (pytest), linting
  (ruff), packaging (hatchling), and structured data modeling in YAML.

**Learned (built during this project)**
- The internal structure of the NIST AI RMF (Govern / Map / Measure / Manage → 19 categories → 72
  subcategories) and how to turn an outcome-based framework into a measurable scoring rubric.
- EU AI Act specifics — risk tiers, the Annex III high-risk categories, and (importantly) the
  **applicability** of obligations: e.g., that an Art 27 Fundamental Rights Impact Assessment is *not*
  triggered for a private employer under Annex III.4, whereas a **GDPR Art 35 DPIA** is mandatory for
  systematic candidate profiling. Verifying *who an obligation binds* — not just that it exists — is
  a lesson this project drove home.
- Designing a **reproducible** assessment: keep the analysis as data, and regenerate the whole
  report from one command.

## What this project demonstrates

The key idea: **`airisk` does the paperwork, not the judgment.** A human analyst decides each control
rating from the evidence; the tool validates the data, computes the maturity math, classifies each
use case under the EU AI Act, and renders the report and chart. That mirrors how real GRC tooling
works, and makes the assessment reproducible.

*Mini-example:* rate `GOVERN 1.1 = Met`, `1.2 = Partial`, `1.3 = Not Met` → weights 1.0 / 0.5 / 0.0
→ 50% maturity for that group → rolled up across categories and functions → drawn on the radar.

## Results at a glance 

| Metric | Result |
|---|---|
| Overall NIST AI RMF maturity | **11.4%** (emerging) — over 70 applicable subcategories |
| Weakest function | **Measure — 7.5%** (no testing, monitoring, or bias evaluation) |
| By function | Govern 10.5% · Map 13.9% · Measure 7.5% · Manage 15.4% |
| Gaps identified | **16** — 7 High · 6 Medium · 3 Low |
| Improvement actions | **10**, prioritized with owners + target dates |

![NIST AI RMF maturity by function](reports/maturity-chart.png)

**Headline finding:** FakeOrg's highest-risk system — an AI résumé-screening tool classified
**high-risk** under the EU AI Act (Annex III, employment) — runs with no bias/fairness testing, no
defined human-oversight procedure, and no candidate notification.

**Read the full assessment:** [`reports/final-report.md`](reports/final-report.md) ·
[`reports/scorecard.md`](reports/scorecard.md)

## How it works

```
data/ + frameworks/  ──►  airisk assess  ──►  reports/
(YAML: org, inventory,    (validate, score,    (scorecard.md,
 control ratings,          render, chart)       final-report.md,
 framework catalogs)                            maturity-chart.png)
```

## Scoring methodology (summary)

- **Maturity ratings:** each control is **Met (1.0) / Partial (0.5) / Not Met (0.0) / Not Applicable
  (excluded)**. Maturity % = weighted sum ÷ applicable controls, rolled up subcategory → category →
  function.
- **Gap severity** combines **impact** (harm to individuals, legal exposure, breadth) and
  **likelihood**: **High** = high-risk safeguard missing / direct legal exposure / systemic; **Medium**
  = meaningful risk, narrower scope; **Low** = good-practice gap, limited immediate impact.

The full rubric and the meaning of each NIST function are documented in §3 of
[`reports/final-report.md`](reports/final-report.md).

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
| `data/` | FakeOrg profile, AI use-case inventory, control ratings, gaps, roadmap, findings |
| `frameworks/` | NIST AI RMF (72 subcategories) + EU AI Act reference catalogs |
| `evidence/` | Synthetic evidence artifacts (policies, vendor docs, SOPs) |
| `src/airisk/` | The Python tool (pydantic models, scoring, Jinja2 report, chart, CLI) |
| `tests/` | pytest suite |
| `reports/` | Generated scorecard, report, and maturity chart |

## Frameworks & methodology

- **NIST AI RMF 1.0** — maturity scoring across the Govern / Map / Measure / Manage functions.
- **EU AI Act (Regulation (EU) 2024/1689)** — risk classification (prohibited / high-risk / limited /
  minimal) and obligation mapping for the high-risk and limited-risk use cases.

The engagement follows a real methodology: scope → AI use-case inventory → maturity assessment →
EU AI Act review → gap register (severity-rated) → improvement roadmap → report.

## Scope & limitations

This is a **synthetic, self-authored exercise** — FakeOrg, its evidence, and its findings were all
designed for the project. It demonstrates methodology, framework fluency, and tooling, but it does
**not** replace what a real engagement adds: real (often incomplete) evidence, stakeholder
interviews, negotiation over findings, and judgment under ambiguity. Read it as a worked example of
*how* an AI governance assessment is structured and reasoned, not as a real compliance verdict.

## Future work

- Add ISO/IEC 42001 (AI management system) as a second maturity lens.
- Expand the use-case inventory and evidence base.

## License

MIT — see [`LICENSE`](LICENSE). All assessment data is synthetic.
