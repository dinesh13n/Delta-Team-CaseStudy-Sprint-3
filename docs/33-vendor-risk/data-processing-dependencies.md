# Data processing dependencies

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (today) / CONDITIONAL (future) |
| Evidence sources | docs/25-governance/compliance-obligations.md; docs/24-security-privacy |
| Assumptions | See body |
| Unresolved issues | RA-01 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Today: all processing is in-process on the host. **No data leaves the service.** Synthetic fixture only. [VF]

| Future flow | Data | Restriction |
|---|---|---|
| To model provider | allow-listed shipment facts only; no customer identifiers, no free text from untrusted fields (sanitiser + enum allow-list) | contract must forbid retention and training; residency [UNK] |
| To IdP | tokens only | n/a |
| To observability platform | metrics, structured logs without subjects | retention [UNK] |
| To backup storage | curated/quarantine layers, audit, approvals | encryption and retention [UNK] (RA-01) |

Real operational data, if ever used, triggers compliance-obligations.md (UNRESOLVED).
