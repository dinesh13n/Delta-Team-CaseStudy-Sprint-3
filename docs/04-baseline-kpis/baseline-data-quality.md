# Baseline Data Quality (Step C5)

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 4 KPI baseline) |
| Runbook step | C5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | evidence/04-baseline-kpis/EVD-C-05-data-profile.json; evidence/04-baseline-kpis/EVD-C-05-profile.py |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

See the full tables in the section below; machine-readable output is `evidence/04-baseline-kpis/EVD-C-05-data-profile.json`.

- **shipments.csv**: 354 rows (manifest 354); duplicate keys ['SHI-00004', 'SHI-00013', 'SHI-00019']; blank-field row at line [353]; out-of-domain timestamps {'promised_at': ['1900-01-01T00:00:00']}; REC-prefixed keys ['REC-0001'].
- **tracking_events.csv**: 354 rows (manifest 354); duplicate keys ['EVE-00004', 'EVE-00013', 'EVE-00019']; blank-field row at line [353]; out-of-domain timestamps {'event_time': ['1900-01-01T00:00:00']}; REC-prefixed keys ['REC-0001'].
- **vehicles.csv**: 354 rows (manifest 354); duplicate keys ['VEH-00004', 'VEH-00013', 'VEH-00019']; blank-field row at line [353]; out-of-domain timestamps {}; REC-prefixed keys ['REC-0001'].
- **routes.csv**: 354 rows (manifest 354); duplicate keys ['ROU-00004', 'ROU-00013', 'ROU-00019']; blank-field row at line [353]; out-of-domain timestamps {}; REC-prefixed keys ['REC-0001'].
- **carrier_bookings.csv**: 354 rows (manifest 354); duplicate keys ['BOO-00004', 'BOO-00013', 'BOO-00019']; blank-field row at line [353]; out-of-domain timestamps {'created_at': ['1900-01-01T00:00:00']}; REC-prefixed keys ['REC-0001'].
- **ai_invocations.csv**: 354 rows (manifest 354); duplicate keys ['AI_-00004', 'AI_-00013', 'AI_-00019']; blank-field row at line [353]; out-of-domain timestamps {}; REC-prefixed keys ['REC-0001'].

## Cross-dataset checks
- Range: `tracking_events.confidence` max 1.42, 1 value above 1 [VF].
- Referential integrity: {"tracking_events.csv": {"orphan_count": 1, "orphan_keys": ["REC-0001"]}, "carrier_bookings.csv": {"orphan_count": 1, "orphan_keys": ["REC-0001"], "shipments_with_multiple_bookings": 3}, "ai_invocations.csv": {"orphan_count": 1, "orphan_keys": ["REC-0001"]}} [VF].
- Weights: 171 of 351 shipments have actual weight above declared weight [VF]; meaning unknown [UNK] (not in runbook, new observation).
- Events: 3000 events (manifest 3000); correlation usable 33.6% (1,008 of 3,000; 983 null, 1,009 empty; literal non-null share is 67.2%); duplicate event_id 0.
- Events by actor: seven of eight actors are not in the API role allow-list (only `ai_agent` is), listed: carrier_partner, customer_support, customs_agent, dispatcher, driver, fleet_manager, warehouse_ops [VF].

## Comparison with the manifest and issue list
`data/manifest.json` and `data/quality_issues.json` declare the same four defect classes for every dataset (duplicate key, blank mandatory fields, impossible timestamp, out-of-range score); all four classes were found where a field of that kind exists. Declared-but-absent: vehicles and routes have no timestamp or score field, so two of the four classes cannot occur there [INF].

## Deviations from the runbook's expected results (C-X4)
1. `ai_invocations.csv` also has one orphan shipment reference (row REC-0001); the runbook listed only tracking_events and carrier_bookings. New finding F-58.
2. The blank row has its key present and all other fields empty, not an entirely empty row (consistent with F-34 text).
3. 171 shipments with actual weight greater than declared: new observation F-59 (meaning unknown).
4. Runbook C1 states 33.6% correlation completeness. CORRECT: 33.6% of events carry a non-empty id. An earlier note here measured 67.2% by counting only JSON null; reversed in D-012.

Everything else matched.
