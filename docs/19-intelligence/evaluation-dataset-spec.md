# Evaluation dataset specification

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (datasets precede first evaluation run) |
| Evidence sources | EVD-J-02 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Builder: `evaluation/build_datasets.py` (deterministic). Files: `evaluation/datasets/*.jsonl`. Manifest: `evidence/19-intelligence/EVD-J-02-dataset-manifest.json`.

| Set | Cases | SHA-256 (first 16) | Purpose |
|---|---|---|---|
| golden | 120 | 05f589b456bb14c1 | real curated shipments with their events and bookings; expected abstention and recommendation class from business rules |
| edge | 20 | ca27858cb6fbd95b | empty status, taxonomy noise, 200 events, retry 4995/5/6/non-numeric, control chars, 5,000-char value |
| adversarial | 43 | 8f87fdf9e70649bb | 14 injection payload types x 3 fields + canary-only case; includes zero-width split, homoglyph, `</data>` close, template braces, JSON break |
| failure | 9 | a104558fe29a923d | provider unavailable/raises/invalid JSON/non-dict/schema-invalid/bad confidence/low confidence/missing keys/leaky output |

**Ordering proof (J-X2).** thresholds.json declared 2026-10-08T10:37:53Z; datasets built 10:38:22Z; first evaluation run 10:38:32Z. The file timestamps live inside the artifacts; the operator should also commit datasets and thresholds in a commit **before** the commit that adds results (commands in the final hand-over).
**Honest limits.** [VF] The fixture contains no injection text (F-60), so adversarial inputs are constructed. [INF] The golden oracle (expected recommendation class) restates business rules, so for the deterministic provider it measures conformance, not insight. Abstention expectation uses `status-taxonomy.yaml` (`approved` is not a shipment status).
Reused unchanged by Stage L (TEVV) and the Stage Q comparison.
