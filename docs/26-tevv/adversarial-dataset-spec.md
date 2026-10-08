# Adversarial dataset specification

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
| File | `07-logistics-shipment-fleet-routing-ops/evaluation/datasets/adversarial.jsonl` |
| Cases | 43 |
| SHA-256 | `8f87fdf9e70649bb303f7d02d43b802de06c46d7476ba838b0a40c392aef7b6d` |
| Builder | `evaluation/build_datasets.py` (deterministic: same inputs give the same bytes) |

## Contents
Constructed payloads (the fixture has none, F-60) placed in free-text-capable fields: instruction override, role-play, delimiter break (`</data>`), zero-width and homoglyph obfuscation (NFKC), base64 text, markdown/HTML, template braces, requests to reveal customer or driver ids, tool-call lookalikes.

## Rules
- [VF] The file is not edited by L2. L2 verifies the checksum above against `dataset_manifest.json` and against the file on disk (see `tevv-results.md`).
- [VF] Cases are scored by code, not by judgement: every expected value is a field of the case.
- [ASM] The case count is small enough to read in full; it is not a statistical sample of production traffic. No production traffic exists.
