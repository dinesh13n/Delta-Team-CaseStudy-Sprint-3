# Non-Functional Requirements

| Field | Value |
|---|---|
| Stage | B: Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md; docs/01-engagement/*; docs/domain-specific-spec.md (repo) |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-08, OQ-24 |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Thresholds are proposals [ASM] pending sponsor ratification (OQ-24); each has metric, threshold and method.
| ID | NFR | Metric | Threshold | Method |
|---|---|---|---|---|
| NFR-1 | Lookup correctness | wrong-record responses | 0 in test suite | contract tests |
| NFR-2 | Audit completeness | requests with actor + correlation id recorded | 100% | audit test |
| NFR-3 | Event correlation | events with correlation id | >= 99% for new events | data-quality check |
| NFR-4 | Non-advice API latency | p95 | <= 500 ms | load test, sandbox |
| NFR-5 | Advice latency | p95 | <= 3,000 ms (A6 envelope) | load test |
| NFR-6 | Unauthorised access | denied requests succeeding | 0 | negative tests |
| NFR-7 | Reproducibility | clean setup from README | passes in CI | CI job |
| NFR-8 | Retry bound | max retries per booking | configured ceiling enforced | integration test |
| NFR-9 | Degraded mode | core lookup works with advice disabled | yes | failure drill |
| NFR-10 | Evidence | every claim has an EVD id and hash | 100% | manifest check |
