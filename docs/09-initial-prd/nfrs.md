# NFRs (PRD)

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 9) |
| Runbook step | E3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/03-problem-value/; docs/08-ai-qualification/; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Carried unchanged from docs/03-problem-value/nfrs.md.

Thresholds are provisional proposals [ASM] pending sponsor confirmation (OQ-08).

| ID | NFR | Metric | Threshold | Method |
|---|---|---|---|---|
| NFR-1 | Read latency | p95 response time of record lookup | <= 500 ms | load test, 100 requests |
| NFR-2 | Availability | health check success | >= 99.5% in test window | scripted probe |
| NFR-3 | Traceability | share of events with a correlation id | 100% of new events | event scan |
| NFR-4 | Audit completeness | audit records containing actor and request id | 100% | log scan |
| NFR-5 | Data quality | duplicate keys and blank mandatory fields accepted into trusted store | 0 | validation run |
| NFR-6 | Test coverage | line coverage of service code | >= 80% | coverage report |
| NFR-7 | Secrets | credential-pattern matches in source | 0 | secret scan |
| NFR-8 | Reproducibility | clean-checkout test pass | 100% of tests pass | fresh venv run |
| NFR-9 | AI response (if used) | p95 latency | <= 3,000 ms | benchmark (A6 envelope) |
| NFR-10 | AI cost | cost per request | <= 2.25 cost units | usage report (A6 envelope) |
