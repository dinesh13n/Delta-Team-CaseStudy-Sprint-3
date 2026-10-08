# After-intervention KPI sheet

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (measured) / no improvement demonstrated |
| Evidence sources | evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717) |
| Assumptions | See body |
| Unresolved issues | no operational data |
| Residual risks | O-R-01 an improvement could be mistakenly read from K9/K10 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Measured with `python -m scripts.after_kpis` using the frozen C1 definitions and the repository's own `apps/api/kpis.py`. Definitions were **not** modified. [VF]

| KPI | Baseline (C1) | After | Equal? | Reading |
|---|---|---|---|---|
| K1 latency p50 / p95 / max (ms) | 1667 / 13709 / 14999 | 1667 / 13709 / 14999 | yes | a column of the static fixture, not a service measurement |
| K2 cost per event | 2.2451 | 2.2451 | yes | static |
| K3 severe-event share | 39.6% | 39.6% | yes | static |
| K4 correlation completeness (source stream) | 33.6% | 33.6% | yes | the producer still emits no id (F-M3-01) |
| K5 declared AI tokens | 904,432 | 904,432 | yes | declared by the dataset |
| K6 retries min / mean / max | 51 / 2508.5 / 4995 | 51 / 2508.5 / 4995 | yes | static |
| K7 duplicate keys (raw layer) | 18 | 18 | yes | seeded defects remain in the raw files |
| K8 incomplete rows (raw layer) | 6 | 6 | yes | seeded defects remain |
| K9 tests | 3 of 3 pass (0 of 3 collected without httpx) | 170 passed, 7 xfailed | n/a | engineering health, not operations |
| K10 coverage | 45% | 97% (apps + etl) | n/a | engineering health |

Evidence: `EVD-O-01-after-kpis.json` (SHA-256 `3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717`).

**Conclusion:** K1 to K8 equal their baseline to the digit, as they must: they are computed from a static synthetic fixture that the intervention does not alter. K9 and K10 improved because tests were written. None of this is a business outcome.
