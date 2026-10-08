# Preliminary TCO

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

No monetary TCO can be computed: model prices (OQ-02), engineering cost and volumes (OQ-09, UNK) are unknown. Structure only:

| Cost element | S1 | S2 | S3 | S4 | Status |
|---|---|---|---|---|---|
| Build effort | med | med | low-med | high | ASM, relative |
| Run: compute | low | low | low | low-med | ASM |
| Run: model tokens | 0 | 0 | volume x tokens x price | S3 x steps | needs OQ-02 |
| Governance and evaluation | low | low | med | high | ASM |
| Failure/rework risk | unknown | unknown | unknown | unknown | UNK |

Will be completed with real inputs in Stage E (Step E2).
