# Reconciliation rules

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (rules); not exercised on live systems |
| Evidence sources | EVD-H-06, EVD-J-05 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. One live booking per (shipment, carrier). Reconcile by `idempotency_key`; any second live partner_ref for the same key is a defect.
2. `compensation_required=true` rows are reviewed by a person; the system never retries them.
3. Fixture reconciliation: 3 duplicate booking ids exist in `carrier_bookings` (quarantined as later duplicates by ETL); retry_count > 5 (max 4,995) is flagged, not corrected.
4. Orphans (events/bookings whose shipment_id is absent from shipments) are quarantined with reason `BR-FK`, never silently dropped.
