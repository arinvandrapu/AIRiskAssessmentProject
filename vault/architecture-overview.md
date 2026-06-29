---
tags: [project, architecture, reference]
---

# Architecture Overview

The full project architecture / rundown lives in the repo at `architecture/project-architecture.md`. This note is the vault pointer + summary.

Key points:
- Simulated AI governance assessment of fictional **FakeOrg** (synthetic data only).
- **Two senses of "tools":** the *frameworks* we assess with (NIST AI RMF + EU AI Act) vs. the *software tool we build* (`airisk` Python CLI). The tool automates scoring + report generation; the human makes the judgments.
- **Data flow:** structured YAML (`data/`, `frameworks/`) → `airisk assess` (pydantic validate → score → render) → `reports/` (scorecard, final report, maturity chart).
- **Deliverable:** the public repo = professional GRC report + clean dataset/methodology + working tool.

See [[project-overview]] for current status and [[architecture-decisions]] for the decision record (ADR-001..007).
