# Benefits realisation dashboard specification

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (spec) |
| Evidence sources | evidence/36-benefits/EVD-O-03-benefit-model.json (SHA-256 2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Source of truth: the audit trail plus a business data feed that does not yet exist.

| Panel | Definition | Needs |
|---|---|---|
| Outcomes with a reviewed suggestion | `ai.decision` approve, by week | real users |
| Review minutes per outcome | audit time between `ai.summary` and `ai.decision` (upper bound; includes waiting) | users, time-on-task study |
| Rejection share | reject / all decisions | users |
| Cases per month | cases from the operating system | case ids (CA-02) |
| Operations hours | time tracking | owner |
| Cumulative net hours vs payback line | model + actuals | all above |
Each panel states its measurement window and population. KPIs use the frozen definitions; changed definitions need a new version, not an edit.
