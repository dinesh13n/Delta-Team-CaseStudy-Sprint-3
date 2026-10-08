# Invalidated assumptions

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | see table |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Assumption | Where made | Invalidated by | Evidence |
|---|---|---|---|---|
| IA-1 | Uncorrelated events are those with JSON null correlation_id (F-42 = about one third) | A4, D-007, D-010 | counting empty strings as missing gives 1,992/3,000 uncorrelated | EVD-A-04c; D-012 |
| IA-2 | data/README.md ships prompt-injection payloads | C/F | no free-text field carries them | F-60 |
| IA-3 | The Playwright suite tests a portal | C | test asserts `body` visible against nothing | F-52 |
| IA-4 | Rule BR-04 (block) can be enforced as declared | D3 | every one of 354 rows violates it | EVD-D-05; EVD-H-06 |
| IA-5 | Shipments link to routes and vehicles by foreign key | D1 | only `*_.shipment_id` links to shipments | EVD-D-* relationships |
| IA-6 | Scope-narrowed personas (hub/fleet) can be enforced | F2 | data carries no hub/fleet attribute | policy engine `scope_enforced=false` |
| IA-7 | /health can double as dependency check | runbook H8 | would make liveness flap with data readiness | D-013 |
| IA-8 | An audit-v1 switch (FF-06) is a safe rollback | G2 | two write paths risk divergent chains | D-013 |
| IA-9 | A named CTO/approver will sign the G4 authorisation | G4 | none named | D-009, OQ-05 |
