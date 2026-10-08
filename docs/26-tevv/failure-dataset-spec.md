# Failure dataset specification

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
| File | `07-logistics-shipment-fleet-routing-ops/evaluation/datasets/failure.jsonl` |
| Cases | 9 |
| SHA-256 | `a104558fe29a923d7cb3e201a7fc98bb2e98296aed053df94354d0aa64d3d5eb` |
| Builder | `evaluation/build_datasets.py` (deterministic: same inputs give the same bytes) |

## Contents
Provider faults: timeout, error, malformed JSON, schema-invalid JSON, leaked forbidden value in the output, low confidence, empty output, circuit open, unconfigured model. Expected = deterministic fallback with a named reason, never a 500.

## Rules
- [VF] The file is not edited by L2. L2 verifies the checksum above against `dataset_manifest.json` and against the file on disk (see `tevv-results.md`).
- [VF] Cases are scored by code, not by judgement: every expected value is a field of the case.
- [ASM] The case count is small enough to read in full; it is not a statistical sample of production traffic. No production traffic exists.
