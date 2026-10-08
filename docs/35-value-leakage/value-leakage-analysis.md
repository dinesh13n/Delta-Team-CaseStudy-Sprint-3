# Value leakage analysis

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (identified) |
| Evidence sources | docs/31-observability, docs/32-finops, evidence/36-benefits/EVD-O-03-benefit-model.json (SHA-256 2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Where value would leak between capability and outcome, by the runbook's categories:

| Leakage | Evidence | Size |
|---|---|---|
| Low adoption | no users; training and change management not designed | unknown |
| Overrides / rejects | self-approval allowed, no approval expiry; rejects not yet observed | unknown |
| Errors | 0 of 192 evaluation cases failed with the deterministic provider; a real model not tested | unknown |
| Rework from enum noise | `[unrecognised]` and enum flags on most rows (DEBT-15) hide real defects | high in fixture |
| Latency | API fast; model latency unknown | unknown |
| Control friction | mandatory human approval adds review time; the benefit model shows review time decides the outcome | key sensitivity |
| AI/infrastructure cost | tokens negligible; platform unknown | small / unknown |
| Workflow displacement | review moves from "decide" to "check the suggestion" | unmeasured |
| Missing automation | ETL has no scheduler (DATA_STALE would fire daily) | operational gap |
| Orphan capability | policy/audit can prove decisions, but no consumer (auditor workflow) exists | adoption gap |
