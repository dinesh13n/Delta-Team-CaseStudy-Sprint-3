# Golden dataset specification

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evaluation/datasets/dataset_manifest.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Item | Value |
|---|---|
| File | `07-logistics-shipment-fleet-routing-ops/evaluation/datasets/golden.jsonl` |
| Cases | 120 |
| SHA-256 | `05f589b456bb14c18051ac6a75fbedbc65d3e1ced4663311505921f7fb75f08f` |
| Builder | `evaluation/build_datasets.py` (deterministic: same inputs give the same bytes) |

## Contents
Real shipments from the curated layer with their events and bookings; expected = fields the summary must be grounded in, recommendation class, approval flag true. Includes status mix (exception, delayed, in_transit, delivered) and shipments with 0, 1 and many events.

## Rules
- [VF] The file is not edited by L2. L2 verifies the checksum above against `dataset_manifest.json` and against the file on disk (see `tevv-results.md`).
- [VF] Cases are scored by code, not by judgement: every expected value is a field of the case.
- [ASM] The case count is small enough to read in full; it is not a statistical sample of production traffic. No production traffic exists.
