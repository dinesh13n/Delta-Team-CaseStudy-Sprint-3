# Concentration risk analysis

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | vendor choices |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- **Today:** concentration is in GitHub (source, CI, history) and PyPI. No runtime vendor.
- **Future:** model, platform and IdP could all come from one vendor family. That would concentrate availability, price and legal exposure. The architecture keeps them separable: model behind `ModelProvider`, identity behind a verifier interface, storage as files.
- **Stage Q limitation:** the two-model comparison will use two Anthropic models, which tests prompt and output-contract portability *within one provider*, not provider concentration.
