---
tags: [project, overview]
---

# AI Risk Assessment Project — Overview

Portfolio project for the user's cybersecurity new-grad job search (security-focused roles). Built to the workspace **Portfolio Standards** (hiring-manager-grade README, explicit skills/tools, clean structure).

## Status: setup complete, scope decision PENDING

- Repo `github.com/arinvandrapu/AIRiskAssessmentProject` (private) cloned locally on branch `main`.
- Neutral project skeleton scaffolded (CLAUDE.md, tasks/, vault/).
- Project angle and form factor NOT yet chosen — see [[architecture-decisions]].

## Candidate angles under consideration

1. **LLM app security scanner** — tests an AI/LLM app against the OWASP LLM Top 10; targets AppSec / AI Security roles.
2. **AI governance / GRC tool** — assesses an AI system vs NIST AI RMF / ISO 42001, scores risk, generates a report; targets GRC / risk roles.
3. **AI-powered risk analyzer** — uses the Claude API to threat-model a system description (STRIDE/attack surface); targets security engineer / AppSec.
4. **ML model / supply-chain scanner** — scans model artifacts for unsafe deserialization, embedded code, risky deps; targets ML security niche.

## Open questions

- Which angle (ADR-001)?
- Form factor: Python CLI / web app / CLI + report (ADR-002)?
- User's stack experience level (calibrates build depth + explanation).
