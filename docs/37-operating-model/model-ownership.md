# Model and prompt ownership

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | OQ-02, OQ-03, OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Accountable: AI Governance Owner (UNRESOLVED). A model or prompt enters service only by a reviewed change to `models.lock.json` or `prompts.lock.json` (CODEOWNERS covers `apps/api/ai/`), followed by the evaluation at L1 thresholds. Today the single "model" is the deterministic provider; no external model exists. Duties when one does: version pinning, evaluation on every change, deprecation tracking, provider incident intake.
