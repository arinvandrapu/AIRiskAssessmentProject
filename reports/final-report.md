# AI Governance Risk Assessment — FakeOrg

> **⚠️ Synthetic data.** FakeOrg is a fictional organization invented for a portfolio
> project. All people, tools, evidence, and findings are made up. Nothing here is a real
> assessment of a real company.

**Engagement:** AI Governance Risk Assessment · **Period:** Q2 2026 · **Depth:** Governance-level (control & process maturity; not a technical model audit)

**Frameworks:** NIST AI RMF 1.0 (maturity scoring), EU AI Act (risk classification + obligations)

---

## 1. Executive summary

FakeOrg is a B2B SaaS — project & work-management platform organization (~520 employees) with an AI governance posture rated **emerging**.

Overall NIST AI RMF maturity is **not assessed** across 0/72 assessed subcategories.

> _This is a report skeleton: control ratings have not been entered yet (Phase 3). The
> structure, inventory, and EU AI Act classification below are final; maturity scores
> populate once `data/assessments/nist_ai_rmf.yaml` is filled in._

## 2. Scope & methodology

- **AI use reviewed:** both
- **In scope:**
  - All AI/ML tools and use cases across business units (internal & customer-facing)
  - Governance, policy, risk, data, vendor, and human-oversight controls
  - EU AI Act risk classification of each use case
- **Out of scope:**
  - Technical red-teaming / model security testing
  - Sub-processors' internal AI systems
  - Pure analytics/BI with no ML component
- **Stakeholders consulted:** Risk & Compliance (Head of Compliance); IT (Director of IT); Security (CISO); Business owners (VP Sales, VP Engineering, CMO, Head of Talent, Director of Support, CFO)
- **Evidence collected:** Draft AI acceptable-use policy; Vendor data sheets / DPAs; Support chatbot standard operating procedure; Partial vendor risk assessment; Security & data-protection policy excerpts

## 3. AI use-case inventory

| ID | Use case | Business unit | Owner | EU AI Act tier | Human review |
|---|---|---|---|---|---|
| UC-01 | AI resume screening | People (HR) | Head of Talent | high-risk | partial |
| UC-02 | Customer support chatbot | Customer Support | Director of Support | limited-risk | escalation |
| UC-03 | Sales copilot | Sales | VP Sales | minimal-risk | full |
| UC-04 | Code assistant | Engineering | VP Engineering | minimal-risk | full |
| UC-05 | Marketing content generation | Marketing | CMO | minimal-risk | full |
| UC-06 | Internal demand-forecasting model | Finance & Operations | CFO / FP&A | minimal-risk | full |

## 4. NIST AI RMF maturity findings

**Overall:** not assessed (0/72 assessed)

![Maturity by function](maturity-chart.png)

| Function | Maturity | Assessed | Applicable |
|---|---|---|---|
| Govern | not assessed | 0/19 | 0 |
| Map | not assessed | 0/18 | 0 |
| Measure | not assessed | 0/22 | 0 |
| Manage | not assessed | 0/13 | 0 |

See `scorecard.md` for the per-category breakdown.

## 5. EU AI Act review

Each AI use case is classified by EU AI Act risk tier:

- **high-risk** (1): AI resume screening
- **limited-risk** (1): Customer support chatbot
- **minimal-risk** (4): Sales copilot, Code assistant, Marketing content generation, Internal demand-forecasting model

### High-risk obligations checklist

The high-risk use case(s) above trigger the following obligations (compliance status assessed in Phase 3):

**Provider obligations**
- [ ] Art 9 — Continuous lifecycle risk-management system (intended use + foreseeable misuse)
- [ ] Art 10 — Representative, bias-examined training/validation/test data; bias mitigation
- [ ] Art 11 / Annex IV — Technical documentation, kept current (simplified for SMEs)
- [ ] Art 12 — Automatic event logging over the lifetime for traceability
- [ ] Art 13 — Transparency + complete instructions for use to deployers
- [ ] Art 14 — Human oversight by design (override, stop, counter automation bias)
- [ ] Art 15 — Accuracy, robustness, cybersecurity (poisoning/adversarial defenses)
- [ ] Art 17 — Quality management system
- [ ] Art 43 — Conformity assessment (internal Annex VI / notified body Annex VII)
- [ ] Art 47-48 — EU declaration of conformity + CE marking
- [ ] Art 49 — Registration in the EU database before market
- [ ] Art 72 — Post-market monitoring plan
- [ ] Art 73 — Serious-incident reporting (<=15 days; 10 if death; 2 if widespread)

**Deployer obligations**
- [ ] Art 26(1) — Use in accordance with instructions for use
- [ ] Art 26(2) — Assign competent, trained human oversight
- [ ] Art 26(5) — Monitor operation; suspend + report serious incidents
- [ ] Art 26(6) — Keep logs >= 6 months (where under deployer control)
- [ ] Art 26(7) — Inform workers/representatives before workplace deployment
- [ ] Art 26(11) — Inform affected persons subject to Annex III decisions
- [ ] Art 27 — Fundamental Rights Impact Assessment (public bodies, public-service providers, Annex III 5(b)/5(c))
- [ ] Art 86 — Provide affected persons a meaningful explanation of the AI system's role

## 6. Key gaps & risks

_Populated in Phase 3 from the gap register._

## 7. Governance improvement plan

_Populated in Phase 3 from the improvement roadmap._