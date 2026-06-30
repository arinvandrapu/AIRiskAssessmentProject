# AI Governance Risk Assessment — FakeOrg

> **⚠️ Synthetic data.** FakeOrg is a fictional organization invented for a portfolio
> project. All people, tools, evidence, and findings are made up. Nothing here is a real
> assessment of a real company.

**Engagement:** AI Governance Risk Assessment · **Period:** Q2 2026 · **Depth:** Governance-level (control & process maturity; not a technical model audit)

**Frameworks:** NIST AI RMF 1.0 (maturity scoring), EU AI Act (risk classification + obligations)

---

## 1. Executive summary

FakeOrg is a B2B SaaS — project & work-management platform organization (~520 employees) with an AI governance posture rated **emerging**.

FakeOrg has adopted AI quickly and from the bottom up, but governance has not kept pace. There is no executive owner for AI risk, no approved AI policy, and — until this engagement — no inventory of where AI is used. Maturity against the NIST AI RMF is low overall, weakest in the MEASURE function, where there is essentially no testing, monitoring, or bias evaluation. The most urgent exposure is the AI resume-screening tool: it is high-risk under the EU AI Act (Annex III employment) yet operates with no bias testing, no human-oversight procedure, no candidate notification, and no Fundamental Rights Impact Assessment. The good news is that FakeOrg's existing security and privacy programs provide partial coverage to build on, and the improvement roadmap below sequences the highest-severity fixes first.


**Overall NIST AI RMF maturity:** 11.4% across 72/72 assessed subcategories; **16 gaps identified** (7 High, 6 Medium, 3 Low).

**Key findings**
- No executive ownership or committee for AI risk; governance is ad hoc.
- The AI acceptable-use policy is an unapproved draft with no high-risk provisions.
- The high-risk resume-screening tool lacks bias testing, human oversight, and candidate notice.
- No Fundamental Rights Impact Assessment exists for the high-risk use case (EU AI Act Art 27).
- MEASURE is the weakest function — no AI testing, monitoring, or metrics across the board.
- Existing vendor-security and GDPR programs give a foundation to extend to AI-specific risk.

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

**Overall:** 11.4% (72/72 assessed)

![Maturity by function](maturity-chart.png)

| Function | Maturity | Assessed | Applicable |
|---|---|---|---|
| Govern | 10.5% | 19/19 | 19 |
| Map | 13.9% | 18/18 | 18 |
| Measure | 7.5% | 22/22 | 20 |
| Manage | 15.4% | 13/13 | 13 |

See `scorecard.md` for the per-category breakdown.

## 5. EU AI Act review

Risk-tier distribution across the AI inventory:

- **high-risk** (1): AI resume screening
- **limited-risk** (1): Customer support chatbot
- **minimal-risk** (4): Sales copilot, Code assistant, Marketing content generation, Internal demand-forecasting model

### UC-01 — AI resume screening · high-risk

_Annex III.4 (employment/recruitment); performs profiling, so always high-risk (Art 6(4))._

| Obligation | Status | Note |
|---|---|---|
| Art 26(1) — Use in accordance with the provider's instructions for use | Partial | Used on vendor defaults; no documented instructions-for-use on file. |
| Art 26(2) — Assign competent, trained human oversight | Not Met | No named, trained overseer; recruiters rely on the ranking without guidance. |
| Art 26(5) — Monitor operation; report serious incidents | Not Met | No monitoring of outcomes or incident-reporting path. |
| Art 26(6) — Keep logs for at least 6 months (where under deployer control) | Partial | Vendor retains logs; FakeOrg has no defined retention/access control. |
| Art 26(11) — Inform affected persons subject to Annex III decisions | Not Met | Candidates are not told AI screening is used. |
| Art 27 — Fundamental Rights Impact Assessment (FRIA) | Not Met | No FRIA performed for the high-risk use case. |
| Art 86 — Provide affected persons a meaningful explanation | Not Met | No mechanism for candidates to obtain an explanation. |

### UC-02 — Customer support chatbot · limited-risk

_Article 50(1) transparency — users must be told they interact with an AI._

| Obligation | Status | Note |
|---|---|---|
| Art 50(1) — Disclose to users that they are interacting with an AI | Partial | Disclosed on the web widget but not in the in-app chat — inconsistent. |


## 6. Key gaps & risks

**16 gaps** — 7 High · 6 Medium · 3 Low.

| ID | Severity | Gap | Mapping | Risk |
|---|---|---|---|---|
| GAP-01 | High | No AI governance ownership or committee | GOVERN 2.1, GOVERN 2.3 | AI decisions are made ad hoc with no accountability; risks go unmanaged across the org. |
| GAP-02 | High | No approved AI policy | GOVERN 1.2, GOVERN 4.1 | Staff lack binding guidance; inconsistent and unsafe AI use. |
| GAP-03 | Medium | No AI use-case register or intake process | GOVERN 1.6 | Shadow AI proliferates; the org cannot see or govern what it runs. |
| GAP-04 | High | No bias/fairness testing of high-risk resume screening | MEASURE 2.11 | Potential discriminatory hiring outcomes; legal and reputational exposure. |
| GAP-05 | High | No human-oversight design for resume screening | Art 26(2), Art 14, MAP 3.5 | Automation bias; the AI effectively makes hiring decisions unchecked. |
| GAP-06 | High | Candidates not informed of AI use | Art 26(11) | Breach of EU AI Act deployer transparency duty for high-risk systems. |
| GAP-07 | High | No Fundamental Rights Impact Assessment | Art 27 | Non-compliance with a mandatory pre-use obligation; unassessed rights impacts. |
| GAP-08 | Medium | Inconsistent AI disclosure on support chatbot | Art 50(1) | Transparency-obligation gap; users may not know they are talking to AI. |
| GAP-09 | Medium | No AI-specific vendor assessment | GOVERN 6.1, MANAGE 3.1 | Third-party AI risk is unmanaged; unclear whether customer data trains vendor models. |
| GAP-10 | Medium | Shadow AI and no data-handling guidance | GOVERN 1.1, MAP 4.1 | Confidential data or source code may leak to third-party AI services. |
| GAP-11 | Medium | No model documentation for in-house forecasting model | MAP 2.3, MEASURE 2.9, MANAGE 3.2 | Undetected model drift; loss of capability if the owner leaves. |
| GAP-12 | High | No AI risk-management process or risk tolerances | GOVERN 1.3, GOVERN 1.4, MAP 1.5 | Risks are neither prioritized nor treated consistently. |
| GAP-13 | Medium | No AI incident response or deactivation capability | MANAGE 2.4, MANAGE 4.1 | A misbehaving AI system cannot be promptly detected or stopped. |
| GAP-14 | Low | No AI risk-management training | GOVERN 2.2 | Personnel cannot execute governance duties they are unaware of. |
| GAP-15 | Low | No chatbot output evaluation or log-retention policy | MEASURE 2.4, MEASURE 3.3 | Harmful answers go undetected; privacy/retention exposure on stored chats. |
| GAP-16 | Low | No user appeal or feedback channel for AI outcomes | MEASURE 3.3 | Errors persist; affected people have no recourse. |

## 7. Governance improvement plan

| ID | Priority | Action | Owner | Target | Success measure |
|---|---|---|---|---|---|
| ACT-01 | High | Establish an AI governance committee and assign an executive owner. | Executive sponsor (CISO chairs) | 2026-Q3 | Chartered committee meets monthly; named accountable executive. |
| ACT-02 | High | Finalize and approve the AI acceptable-use policy, including high-risk provisions. | Head of Compliance | 2026-Q3 | Board-approved policy published; staff attestation complete. |
| ACT-03 | Medium | Stand up a central AI use-case register with an intake and review gate. | Director of IT | 2026-Q3 | 100% of known AI tools registered; new tools reviewed before adoption. |
| ACT-04 | High | Commission a bias/adverse-impact audit of the resume-screening tool. | Head of Talent (with vendor) | 2026-Q3 | Documented bias audit with remediation actions tracked. |
| ACT-05 | High | Define and implement a human-oversight SOP for resume screening. | Head of Talent | 2026-Q4 | Documented SOP; recruiters trained; override/review rate monitored. |
| ACT-06 | High | Add AI transparency notices — inform candidates; fix chatbot disclosure everywhere. | Head of Talent and Director of Support | 2026-Q3 | Candidate notice live; AI disclosure shown in all chatbot surfaces. |
| ACT-07 | High | Conduct a Fundamental Rights Impact Assessment for the high-risk use case. | Head of Compliance | 2026-Q4 | Completed FRIA filed; mitigations assigned and tracked. |
| ACT-08 | Medium | Extend vendor risk assessment with an AI module (bias, training-data use, model docs). | Security & IT | 2026-Q4 | All AI vendors re-assessed with the AI module; gaps logged. |
| ACT-09 | Medium | Roll out an AI risk-management process, risk tolerances, and staff training. | Head of Compliance | 2027-Q1 | Documented process in use; risk tolerances approved; >90% trained. |
| ACT-10 | Medium | Define AI incident response, post-deployment monitoring, deactivation, and appeal channels. | CISO and Director of Support | 2027-Q1 | AI incident runbook tested; appeal channel live; monitoring in place. |
