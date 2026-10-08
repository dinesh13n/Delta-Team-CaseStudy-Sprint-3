# Data ownership

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | BR-04, F-59, DEBT-15 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Accountable: Data Owner (UNRESOLVED). Open rulings that only the owner can give: BR-04 (declared block violated by 354 of 354 rows), F-59 (actual weight > declared on 171 rows), the enum vocabulary behind DEBT-15, and a producer correlation id and shipment id on events. Until answered, the ETL flags rather than blocks and quarantine follows the written contract.
