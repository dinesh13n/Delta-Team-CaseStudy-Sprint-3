# Total cost of ownership model

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (components listed; values unknown) |
| Evidence sources | docs/00-preflight/ai-economics/preliminary-tco.md |
| Assumptions | See body |
| Unresolved issues | OQ-01, OQ-07, OQ-09 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Cost component | Pilot | Production | Value |
|---|---|---|---|
| Model tokens | tiny | small | see finops-model.md |
| Platform compute, storage, network | unknown | unknown | [UNK] OQ-01 |
| Observability stack | unknown | unknown | [UNK] |
| IdP | unknown | unknown | [UNK] OQ-07 |
| Human review | main running cost | main running cost | [UNK] |
| Security / compliance work (RA-01..RA-12) | unknown | unknown | [UNK] |
| Operations (on-call, runbook upkeep) | unknown | unknown | [UNK] OQ-05 |
| Delivery effort (this transformation) | not tracked in money | n/a | [UNK] |
| Evaluation and drift monitoring | recurring | recurring | [UNK] |

A TCO total would require platform and labour inputs that do not exist. The O3 ROI model uses these as stated assumptions with a downside scenario.
