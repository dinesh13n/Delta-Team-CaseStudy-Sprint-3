# Prioritized capabilities (MoSCoW with evidence)

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | EVD-H-* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Rank | Capability | Priority | State after H | Remaining work |
|---|---|---|---|---|
| 1 | Contextual access control | Must | built | JWKS (OQ-07) |
| 2 | Trusted record access | Must | built | none |
| 3 | Validated intake | Must | built | owner rulings on BR-04, F-59 |
| 4 | Traceable decisions | Must | built | external sink |
| 5 | Governed exception summary | Must | built (deterministic) | real model (OQ-02) |
| 6 | Operational telemetry | Should | built | dashboards, alerts |
| 7 | Carrier saga | Should | not built | J5 |
| 8 | Thin operations view | Should | not built | J4 |
| 9 | ETA prediction / route optimisation | Won't (this release) | n/a | needs real history |
