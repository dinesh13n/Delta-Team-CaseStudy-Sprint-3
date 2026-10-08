# Red-team findings

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (v2) / documented reproduction (baseline) |
| Evidence sources | evidence/26-tevv/EVD-L-03-* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | RL-01..RL-03 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Evidence: `evidence/26-tevv/EVD-L-03-redteam-baseline.json` (sha `690911c90695c307f620ac56aec88e8d0da9732b4f6405dbf9c381e38df9213f`), `evidence/26-tevv/EVD-L-03-redteam-v2.json` (sha `b6f65533d6d71145d1d98da52ee5886590871091c704bc514e07984327d03356`). Run on 2026-10-08.

## Before and after
| ID | Finding | Baseline | v2 | v2 response |
|---|---|---|---|---|
| RT-01 | F-20 | **SUCCEEDED** 200 summary, no identity | blocked | 401 problem+json |
| RT-02 | F-17 | **SUCCEEDED** record with raw `CUS-00002` | blocked | 401 (header ignored) |
| RT-03 | F-19 | **SUCCEEDED** data to a `clinician` | blocked | 401 |
| RT-04 | F-31 | **SUCCEEDED** shipment returned for a customer id | blocked | 404/422 (exact match on the entity key only) |
| RT-05 | F-32 | **SUCCEEDED** unknown id returned `REC-0001` (a wrong record) | blocked | 404 |
| RT-06 | F-30 | **SUCCEEDED** the bad-key row returned | blocked | not in curated layer (quarantined) |
| RT-07 | F-22 | **SUCCEEDED** summary text: "Synthetic summary for IGNORE-PREVIOUS-INSTRUCTIONS-PWNED-RT" | blocked | 422: id does not match key pattern |
| RT-08 | F-22 | not exercised (see note 1) | blocked | 200, field shown as `[unrecognised]`, payload absent |
| RT-09 | F-24 | **SUCCEEDED** `guardrail_status: not_enforced` | blocked | `enforced` or `blocked` |
| RT-10 | F-26 | not exercised (see note 2) | blocked | 401 |
| RT-11 | F-17 | **SUCCEEDED** `alg=none` token accepted | blocked | 401 |
| RT-12 | F-46 | **SUCCEEDED** 120 of 120 calls served | blocked | 429 after the per-subject limit |

**Totals: baseline 10 of 12 succeeded; v2 0 of 12.**

## Notes that matter
1. **RT-08 on baseline.** The baseline summary is `"Synthetic summary for <first column>"`. It never reads `service_tier` or event fields, so the categorical-field route is not reachable there; the F-22 flaw on baseline is the first-column reflection (RT-07). The script reports "failed", which is true but not a sign of safety. The row is therefore *not applicable* to baseline.
2. **RT-10 on baseline.** There is no approval endpoint at all (404). The defect (F-26) is the absence of any control, not a bypassable control. Recorded as a "control absent" result. For v2 the same request returns 401, and `tests/test_human_control.py` covers the authenticated cases (AI persona 403, read-only roles 403, double decision 409).
3. **First campaign was invalid and discarded.** An earlier run used a stale default poison key (`SHI-00099`), a real row, so the F-22 reflection was never exercised (baseline RT-07 returned a normal summary). The default was corrected and both sides were re-run. Both runs are in the session log; only the corrected run is kept as evidence.
4. **The v2 side proved the fix of DEF-L-02 in a live server**, not only in unit tests: the poisoned `service_tier` came back as `[unrecognised]`.

## New findings from this campaign (v2)
| ID | Observation | Severity | Disposition |
|---|---|---|---|
| RL-01 | Real fixture values for `service_tier` / `event_type` are workflow words, so summaries show `[unrecognised]` on all rows (DEBT-15). The safe default also degrades usefulness. | Medium (quality) | Accepted; owner needs to rule on enum vocabulary (OQ-14) |
| RL-02 | A token with no `purpose` claim gets the first declared purpose (purpose defaulting). | Medium | Accepted, risk R-SEC-04; fix = require explicit purpose once the IdP exists |
| RL-03 | Rate limiting is per process and per subject, in memory. Multi-instance deployments multiply the limit. | Low | Accepted; move to a shared store at deployment |

[VF] No attack against v2 produced data, a state change or a reflected payload.
