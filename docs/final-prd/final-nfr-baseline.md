# Final NFR baseline

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | `docs/17-implementation-prd/finalized-nfrs.md` (sha256 `d5f049f67e3b6663e6994e85bff20294a2905720ff6496446fc480e4636b775c`) |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| NFR | Target | Measured | Status |
|---|---|---|---|
| API read p95 | 250-500 ms | 6.3 ms (1 worker) / 33.6 ms (8) loopback | Partial (no deployment) |
| Availability | 99.5% | not measurable | Unmeasured |
| Correlation id on new events | 100% | 100% in tests | Met |
| Audit completeness | 100% | 10/10 fields | Met in test |
| Quarantine ratio ceiling | 5% | 1.41% | Met |
| Coverage | >= 80% | 96.9% (apps+etl) | Met (gate scope changed, D-013) |
| Runtimes | 3.11 and 3.14 | CI green on both; 3.13 also passes | Met |
| AI latency, cost | envelope | deterministic only | Unmeasured for a model |
