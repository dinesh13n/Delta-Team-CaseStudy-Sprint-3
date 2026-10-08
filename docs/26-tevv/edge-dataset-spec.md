# Edge dataset specification

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
| File | `07-logistics-shipment-fleet-routing-ops/evaluation/datasets/edge.jsonl` |
| Cases | 20 |
| SHA-256 | `ca27858cb6fbd95b385ede3f6564c76e7741a21793228d57e3da2394dc1709ba` |
| Builder | `evaluation/build_datasets.py` (deterministic: same inputs give the same bytes) |

## Contents
Boundary shapes: no events, 1 event, more than 10 events (truncation keeps the exception event), missing optional fields, very long values, unicode, empty strings, duplicate event ids, maximum token context.

## Rules
- [VF] The file is not edited by L2. L2 verifies the checksum above against `dataset_manifest.json` and against the file on disk (see `tevv-results.md`).
- [VF] Cases are scored by code, not by judgement: every expected value is a field of the case.
- [ASM] The case count is small enough to read in full; it is not a statistical sample of production traffic. No production traffic exists.
