# Model configuration

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (no real model) |
| Evidence sources | apps/api/ai/providers.py, docs/08-ai-qualification/qualification-decision.md |
| Assumptions | See body |
| Unresolved issues | OQ-02, OQ-03 |
| Residual risks | DR-3 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Setting | Value | Source |
|---|---|---|
| Provider | `deterministic` 1.0 (default and fallback) | `AI_PROVIDER` |
| Real model | NOT configured: `UnconfiguredModelProvider` always raises, so the gateway falls back | OQ-02 unresolved |
| max_record_tokens | 2000 | ai-context-policy.yaml |
| max_context_tokens | 8000 | ai-context-policy.yaml |
| Events kept per call | last 10 plus any older `exception` event | gateway |
| Confidence floor | below 0.5 -> abstain `low_confidence` | gateway |
| Rate limit | `AI_RATE_PER_MINUTE` per subject (429 beyond) | config |
| Kill switch | `AI_ENABLED=false` -> 503 | FF-04 |
| Temperature, max output tokens | not applicable: no model call | [UNK] set when OQ-02 is decided |

[ASM] A real model plugs in by implementing `ModelProvider.complete()` and returning provider token counts; the gateway then reports `token_source: provider`. Nothing else changes. No vendor SDK, price or data-residency position exists in the repository.
