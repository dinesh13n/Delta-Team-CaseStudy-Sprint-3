# Final AI and agent baseline

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | `evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`) |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- Provider: deterministic 1.0 (default). A model interface exists; **no real model is configured or was ever called**.
- Prompt and model identity locked by `prompts.lock.json` and `models.lock.json`; the service refuses to start on mismatch.
- Output contract: summary, recommendation, confidence, abstained; schema-validated; fallback on timeout, breaker open, invalid output or policy violation.
- Human control: every suggestion requires a recorded decision; no endpoint changes operational state.
- Agents: none (J6 not applicable).
- Evaluation: 192 cases, 0 failures; thresholds committed before results (timestamps; git order not provable in the single import commit).
