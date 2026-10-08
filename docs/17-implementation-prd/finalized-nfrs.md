# Finalized NFRs with measured values

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | EVD-H-04, EVD-H-06, EVD-H-07, EVD-H-11 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| NFR | Target | Measured so far | Status |
|---|---|---|---|
| Availability SLO | 99.5% [ASM] | not measurable (no deployment) | UNMEASURED |
| Latency, API p95 | 250 ms [ASM] | 11.4 ms in-process (EVD-H-07), no network | PARTIAL |
| Latency, AI summary p95 | 2 s with a real model [ASM] | deterministic only | UNMEASURED for model |
| Security: no unauthenticated business route | 100% | 100% (16 negative tests) | MET |
| Audit completeness | 100% of business actions | chain valid over 351 records | MET (in test) |
| Data quality: quarantine ratio ceiling | 5% | 1.41% | MET |
| Test coverage | >= 80% | 96% | MET |
| Reproducible install | clean clone works | EVD-H-02 | MET |
| Supported runtimes | Python 3.11 and 3.14 | both pass | MET |
| Cost | per A6 envelope | deterministic = 0; real model UNMEASURED | PARTIAL |
