# Cost per workflow

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (structure + measured parts) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | human time; platform |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Workflow W1: **exception review** = read record (no AI) → request suggestion → human decision.

| Component | Per run | Basis |
|---|---|---|
| Record read | compute only, ≈ 5 ms p50 | load probe |
| AI suggestion | 271 tokens est. | EVD-N-04 |
| Audit + approval storage | 1.36 KB | EVD-N-04 |
| Metrics / log storage | 53 series total (not per request) + one log line | EVD-N-04 |
| Human review time | **unmeasured** | no users |
| Platform compute | **unknown** | no platform |

Storage at 100× volume (35,400 requests per period): about 41 MB of audit per period (EVD-N-04). The audit file is a single local file; growth, rotation and archive are undefined (DEBT-N3-01).
