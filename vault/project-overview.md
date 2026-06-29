---
tags: [project, overview]
---

# AI Risk Assessment Project — Overview

Portfolio project for the user's cybersecurity new-grad job search (GRC / AI-governance roles). Built to the workspace **Portfolio Standards** (hiring-manager-grade README, explicit skills/tools, clean structure).

## Status: SCOPE LOCKED — planning phase (no build started)

A simulated **AI governance risk assessment** of a fictional org (**FakeOrg**), using **synthetic data only**, delivered as a public GitHub repo showcase. Per user requirement, build plans are written and approved before any implementation.

## Locked direction (see [[architecture-decisions]])

- **Angle:** simulated GRC / AI-governance assessment engagement (ADR-001)
- **Form:** hybrid — YAML data + Python scoring/report generator (ADR-002, ADR-003)
- **Frameworks:** NIST AI RMF (maturity) + EU AI Act (compliance lens); ISO 42001 = future work (ADR-004)
- **Org:** FakeOrg — composite mid-size B2B SaaS (ADR-005)
- **Data:** 100% synthetic (ADR-006)
- **Process:** plan-before-build; PR per phase (ADR-007)

## Methodology (engagement steps)

1. **Scope** — unit; internal / customer-facing / both; timeframe; depth; in/out of scope
2. **AI use-case inventory** — tool/model/vendor, purpose, owner, data used, human review, risk tier; stakeholders (risk/compliance, IT, security, business owners) + evidence (policies, risk assessments, vendor docs, training, SOPs, examples)
3. **Assess maturity** — NIST AI RMF subcategories scored Met / Partial / Not Met / N/A; EU AI Act risk-tier + obligations review
4. **Gap register** — describe → map to framework → risk/impact → evidence → severity (High/Med/Low)
5. **Improvement roadmap** — action, owner, target date, resources, success measure
6. **Report** — exec summary, scope/methodology, inventory summary, NIST findings, EU AI Act review, key gaps/risks, improvement plan

## Build plan

Detailed phased plan lives in `tasks/todo.md` — four phased PRs (foundations → engine → assessment → showcase). No phase starts before its plan is approved.
