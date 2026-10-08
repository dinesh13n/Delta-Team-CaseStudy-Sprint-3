# Provisional Token Budget

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0C provisional AI economics envelope |
| Runbook step | A6 (runbook/02-TRANSFORMATION-RUNBOOK.md, Stage A) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | **PROVISIONAL**, Draft; approvers UNRESOLVED (OQ-05) |
| Evidence sources | evidence/00-preflight/EVD-A-06-ai-economics-profile.json; data/synthetic/ai_invocations.csv; data/synthetic/events.jsonl; apps/api/services/ai_gateway.py |
| Assumptions | Marked ASM in text; none is a measurement |
| Unresolved issues | OQ-02 (models), OQ-08/09 (KPIs, financial data), OQ-12, OQ-18 |
| Residual risks | Fixture figures are synthetic and may not resemble production |

**[M]** measured in the fixture (dataset-declared, synthetic), **[ASM]** assumption, **[UNK]** unknown. This pack does not decide that AI is justified; that is Stage E.

Provisional design constraints, **PROVISIONAL**, set before any model is chosen so economics do not get reverse-justified (runbook Step A6).

| Constraint | Value | Basis |
|---|---|---|
| Tokens per request (in + out), typical | <= 3,000 | [M] mean 2,562 plus margin; ASM |
| Tokens per request, hard cap | <= 5,000 | [M] observed max 4,989; ASM |
| Retry allowance | 1 per request, counted against the cap | ASM |
| Daily token ceiling | UNKNOWN until volume is known | UNK volume |

Any design that exceeds these must be justified at Stage E Step E2 against this envelope.
