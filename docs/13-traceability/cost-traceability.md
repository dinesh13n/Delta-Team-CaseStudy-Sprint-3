# Cost traceability

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-E-03; EVD-F-04; acceptance-criteria.md |
| Assumptions | See body |
| Unresolved issues | Test files are PLANNED (written in Stage H/J/L); no test result is claimed here |
| Residual risks | See coverage-gap-register.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Cost requirement | Source | Target | Measurement |
|---|---|---|---|
| AI cost per request | NFR-10, A6 envelope | <= 2.25 cost units | usage report (N4) |
| AI latency | NFR-9 | p95 <= 3,000 ms | benchmark (J3) |
| Token budget per call | context-engineering-strategy | <= 2,000 [ASM] vs baseline mean ~2,562 | metrics ai_tokens_total |
| Model avoidance | E1 qualification | 9 of 10 interventions deterministic | architecture review |
Baseline: 6,735.29 cost units over 3,000 events and 904,432 tokens over 353 rows [VF]. Real prices are [UNK] without a chosen model (OQ-02).
