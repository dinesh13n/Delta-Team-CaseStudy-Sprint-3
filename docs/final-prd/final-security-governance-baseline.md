# Final security and governance baseline

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | `docs/24-security-privacy/threat-model.md` (sha256 `567e5c870bc129a82f391c7975fc383c32bfe7913be9052aeb712a05162336be`) |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Controls: signed tokens with fixed algorithm and required claims; deny-by-default policy; masking; AI forbidden fields; 64 KiB body cap (Content-Length only); per-subject AI rate limit; no CORS; generic errors; env-only secrets; secret scan; SBOM; hash-chained audit.
Governance: operating contract PROVISIONAL; 12 risk acceptances proposed, 0 signed; transformation authorisation is an unsigned operator instruction (D-009); Stage gates self-signed (GOV-10). Residual items: `residual-risk-register.md`.
