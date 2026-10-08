# Baseline KPI Sheet (frozen values)

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 4 KPI baseline) |
| Runbook step | C1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | evidence/04-baseline-kpis/EVD-C-05-data-profile.json; evidence/04-baseline-kpis/EVD-C-05-profile.py; EVD-C-03 |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Values measured 2026-10-08 on the baseline-hash-verified fixture. All are proxies.

| ID | Value | Note |
|---|---|---|
| K1 | p50 1667 ms; p95 13709 ms; p99 14776 ms; max 14999 ms | randomly generated; not a service measurement |
| K2 | 2.2451 cost units per event; total 6735.29 | currency unknown |
| K3 | 1188 of 3000 = 39.6% | severity uniformly spread, not a real error rate |
| K4 | 33.6% usable (1,008 of 3000 non-null and non-empty); literal non-null share 67.2% | amended definition D-012: empty string is not an id; runbook C1 text 33.6% was right |
| K5 | 904432 over 353 parsed of 354 rows | declared, synthetic |
| K6 | min 51, mean 2508.5, max 4995 | implausible for real retries |
| K7 | 18 keys (3 in each of 6 datasets) | pattern *-00004, *-00013, *-00019 |
| K8 | 6 rows (1 per dataset, all non-key fields blank) | row 353 of each CSV |
| K9 | 3 of 3 pass (after adding httpx in the venv) | 0 of 3 collected without httpx |
| K10 | 45% (54 of 98 statements missed) | etl, legacy, scripts at 0% |

Cost by entity (K2 segmentation):

| Entity | Events | Cost units | Cost per event |
|---|---|---|---|
| ai_invocations | 505 | 1151.39 | 2.28 |
| carrier_bookings | 519 | 1131.77 | 2.181 |
| routes | 527 | 1197.56 | 2.272 |
| shipments | 474 | 1063.77 | 2.244 |
| tracking_events | 500 | 1121.66 | 2.243 |
| vehicles | 475 | 1069.13 | 2.251 |
