# Support Chatbot — Standard Operating Procedure

> **SYNTHETIC ARTIFACT.** Fictional SOP for a portfolio assessment.

**Owner:** Customer Support · **System:** UC-02 customer support chatbot · **Version:** 1.1 (2026-01-20)

## Purpose
Define how the support chatbot is operated and when conversations escalate to human agents.

## Operation
- The chatbot answers common questions using the help-centre knowledge base.
- It can read basic account/subscription details to answer status questions.
- Confidence below threshold, or an explicit user request, triggers handoff to a human agent.

## Escalation
1. Bot attempts to resolve using knowledge base.
2. On low confidence or sensitive topics (billing disputes, security), escalate to a live agent.
3. Agents can see the prior chat transcript.

## Logging
- Conversations are stored for quality and training purposes.

---
### Gaps (assessor note)
- AI disclosure ("you are chatting with an AI assistant") is shown on the web widget but
  **not** in the in-app chat — disclosure is inconsistent (cf. EU AI Act Art 50(1)).
- No defined retention period for stored conversations; no deletion process.
- No evaluation process for harmful, incorrect, or hallucinated responses.
- No documented process for users to report a bad answer.
