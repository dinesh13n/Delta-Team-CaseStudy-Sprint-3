# Production performance report

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT APPLICABLE (not in production) |
| Evidence sources | evidence/28-resilience, evidence/26-tevv, evidence/30-release |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The system has never run in production, so there is no production performance. [VF] What exists are development-environment measurements, listed so nobody mistakes them for production:

| Measure | Value | Where it comes from |
|---|---|---|
| Throughput, one process, loopback | 145 to 244 rps | EVD-M-02 load probe |
| p95 latency | 6 to 9 ms (1 worker); 34 to 45 ms (8 workers) | same |
| Evaluation pass | 192 of 192 cases | EVD-L-02 (deterministic provider, no model) |
| Red team | 10 of 12 baseline attacks succeeded, 0 of 12 on v2 | EVD-L-03 |
| Failure drills | 5 of 5 PASS | EVD-M-03 |
| Restore | 0.17 s to serving, fixture size | EVD-N-03 |

None of these is a production, user or business measure.
