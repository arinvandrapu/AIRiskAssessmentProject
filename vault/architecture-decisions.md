---
tags: [project, decisions, adr]
---

# Architecture Decisions

Append-only log of design decisions. See [[project-overview]] for context.

## ADR-001: Project angle — DECIDED (2026-06-29)

**Decision:** Simulated **AI governance / GRC risk assessment** of a fictional organization — a modeled consulting engagement (not a generic tool), following a real methodology: scope → AI use-case inventory → maturity assessment → gap register → improvement roadmap → portfolio report.
**Rationale:** Targets GRC / AI-governance roles; demonstrates end-to-end assessment capability.

## ADR-002: Form factor — DECIDED (2026-06-29)

**Decision:** **Hybrid** — inventory + control assessments stored as structured YAML; a Python tool scores maturity and generates the scorecard + report. The fictional org is the showcase input.
**Rationale:** Shows both GRC methodology and automation/tooling skill.

## ADR-003: Stack & tooling — DECIDED (2026-06-29)

**Decision:** Python 3.11+, pydantic v2 (data models/validation), Typer (CLI), Jinja2 (report rendering), matplotlib (maturity chart), pytest (tests), ruff (lint). Lean dependencies.
**Rationale:** User is comfortable with Python; production-style build.

## ADR-004: Frameworks — DECIDED (2026-06-29)

**Decision:** Score maturity against **NIST AI RMF** (Govern / Map / Measure / Manage). Apply the **EU AI Act** as a risk-classification + obligations lens. **ISO/IEC 42001** deferred to "future work."
**Rationale:** Two strong, focused frameworks; keeps depth manageable.

## ADR-005: Fictional organization — DECIDED (2026-06-29)

**Decision:** **FakeOrg** — composite mid-size B2B SaaS (~500 staff) with AI use cases spanning EU AI Act risk tiers (e.g. AI resume screening [high-risk], support chatbot, sales/code copilots, marketing content generation).
**Rationale:** Widest spread of findings across risk tiers; name signals clearly that the org is fictional.

## ADR-006: Synthetic data only — CONSTRAINT (2026-06-29)

**Decision:** All organization data, evidence, and findings are fictional/synthetic. The README carries a prominent disclaimer.
**Rationale:** Personal experiment modeling a real assessment; no real client data.

## ADR-007: Plan-before-build — PROCESS (2026-06-29)

**Decision:** No build work begins until the build plan (`tasks/todo.md`) is reviewed and approved. Each phase ships as its own feature branch + PR; never push to `main`.
**Rationale:** User requirement — plan first, PR-based workflow.
