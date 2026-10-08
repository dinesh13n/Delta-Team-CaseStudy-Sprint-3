# Failure injection plan

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/runbooks/failure-injection-drills.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The five drills in `docs/runbooks/failure-injection-drills.md`, executed exactly as named, by `scripts/failure_drills.py` against copies of the fixture in temporary directories.

| Drill | Declared | How injected | Pass criteria (set before running) |
|---|---|---|---|
| 1 | missing correlation IDs in event streams | 7 header variants; unauthenticated and 422 requests; audit and curated-lineage inspection | all responses well-formed id, no audit event without id, lineage on every curated event |
| 2 | AI gateway timeout, core degradation | slow, failing, healthy and disabled providers | fallback within timeout, core 200, breaker stops calls, recovery after reset |
| 3 | duplicate event replay vs idempotency | 40 replayed events; double ETL; 50 sequential, 20 concurrent and post-restart booking replays | no duplicate fact or booking |
| 4 | stale master data traced downstream | source changed, ETL not run | stale value visible and explainable; /ready detects; reload heals; audit hash differs |
| 5 | legacy batch partial failure vs audit evidence | damaged input to legacy and ETL; ETL crash at entity 4 of 6 | ETL reconciles and records reasons; crash leaves published layers byte-identical |

Safety: nothing touches `data/`; no network; no real provider. Evidence: `evidence/28-resilience/EVD-M-03-drills/`.
