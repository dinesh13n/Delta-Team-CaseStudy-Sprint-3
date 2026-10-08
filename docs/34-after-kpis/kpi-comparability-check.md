# KPI comparability check

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (identical by construction) |
| Evidence sources | evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717) |
| Assumptions | See body |
| Unresolved issues | no freeze-time hash |
| Residual risks | O-R-04 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

O-X1/O-X2 check, automated in `scripts/after_kpis.py`: [VF]

| Check | Result |
|---|---|
| `kpi-dictionary.md` and `semantic-layer/metrics.yaml` agree on all 8 fields of all 10 KPIs | identical (0 field differences); canonical SHA-256 of the dictionary rows `98c21c39cfe977a086f48d1028f6c9de6e01a52b6d2dab713d1c17d196258330` |
| `metrics.yaml` declares `status: FROZEN` | yes |
| Fixture files byte-identical to tag `baseline/v0.1-as-delivered-bytes` | 7 of 7 identical |
| Recomputed K1 to K8 reproduce the C1 baseline values | 8 of 8 equal |
| Measurement window | same single static fixture; no time span exists |
| Population | same 354 rows per entity, 3,000 events |

## Limit on "byte-identical to the frozen set" (O-X1)
No hash of the dictionary was recorded when it was frozen, and the C-stage documents were not yet committed when this check ran, so a byte comparison with a specific past commit is **not possible**. What the check proves is: the two copies of the definitions agree; the definitions reproduce every baseline number exactly (which a changed definition would not); and the fixture is unchanged. The hash above is recorded now so the next stage can detect any later change. Commit order handed to the user puts `docs/04-baseline-kpis` before this evidence.
