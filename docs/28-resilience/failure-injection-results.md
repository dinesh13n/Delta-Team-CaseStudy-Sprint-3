# Failure injection results

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (5/5) after fixes |
| Evidence sources | evidence/28-resilience/EVD-M-03-drills/* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | F-M3-01, F-M3-02, F-M3-05 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Run: 2026-10-08, `python -m scripts.failure_drills`. Evidence: `evidence/28-resilience/EVD-M-03-drills/` (five result sets plus `summary.json`).

| Drill | Verdict | Key observations |
|---|---|---|
| 1 Correlation IDs | PASS | 7 variants all got a well-formed id (client ids kept only when valid; CRLF/script/200-char values replaced); 0 audit events without id; 100 % curated event rows carry `load_id` + `source_row` |
| 2 AI timeout | PASS | slow provider (2 s) answered by fallback `provider_timeout` in ~312 ms with core endpoints 200 (28 ms for the group); failing provider: 2 errors then `circuit_open` ×4, provider called twice; after the 1 s reset the next call reached the provider (`generated_by: model`); AI off: 503 and core 200 |
| 3 Duplicate replay | PASS | 40 replayed events: 40 quarantined (BR-01, BR-02), curated unchanged at 349; same input twice: identical bytes and `load_id`; saga: 50 sequential requests → 1 carrier call, 49 suppressed; 20 concurrent → 1 booked, 19 suppressed; after restart → suppressed, 0 calls |
| 4 Stale master data | PASS | master changed `exception → manual_hold`; record and AI output unchanged until reload; `X-Data-Load-Id` constant (`ld-89446323a790`) while stale and new (`ld-85c84f380135`) after; `/ready` 503 `data_fresh` at 30 h with a 24 h limit; audit `input_hash` identical for the two stale summaries and different after reload |
| 5 Partial failure | PASS | legacy batch: exit 0, prints "legacy reconciled 354", no report, no reject list (silent). ETL on the same input: 7 quarantined with reasons (incl. `ROW-SHAPE` ×2), processed = curated + quarantined; crash at entity 4: published layers byte-identical, staging removed |

## What the drills found (and what was done)
| ID | Finding | Action |
|---|---|---|
| F-M3-01 | source event stream has no correlation column | recorded; owner/data-contract ruling |
| F-M3-02 | timed-out worker cannot be killed; bulkhead not wired | recorded; wire before a real model |
| F-M3-03 | replay with a changed business key is a new fact | stated limit |
| F-M3-04 | freshness check is off by default | documented; set in every environment |
| F-M3-05 | audit event lacks the data load id | backlog DB-16 |
| F-M3-06 | legacy batch fails silently | must not be a control; retire at cutover |
| F-M3-07 | ETL wrote layers directly; a crash left a mix | **FIXED**: staged writes + publish; tests |
| F-M3-08 | **ETL crashed with a TypeError on a row with the wrong column count** (found when drill 5 first ran) | **FIXED**: `ROW-SHAPE` quarantine rule; test |
| F-M3-09 | no `X-Data-Load-Id` to tie responses to data | **FIXED**: header on every response; test |

## Iteration, stated plainly
- First execution: drill 2 reported FAIL because my pass criterion assumed the breaker starts clean; the system was right (the phase-1 timeout already counted as a failure) and the criterion was corrected; drill 4 crashed on a script assumption (summary text can be absent when the AI abstains) and was corrected; drill 5 exposed F-M3-08 in the ETL. The criteria for drills 1, 3 and 5 were not loosened.
- The final run (all PASS) is the evidence kept; earlier runs were overwritten before registration. Their outcomes are recorded here.
- Not drilled: audit-sink failure, disk full, process crash (FM-12, FM-14, FM-15).
