# Substitution strategy

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (strategy) |
| Evidence sources | apps/api/ai/providers.py; apps/api/config.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Component | Substitute by | Verification before switch |
|---|---|---|
| Model provider | implement `ModelProvider`; set `AI_PROVIDER`; deterministic stays as fallback | full evaluation at L1 thresholds; red team re-run; prompt lock re-issued |
| IdP | implement JWKS verifier (stub exists); map roles to `access-semantics.yaml` | security suite; policy parity |
| Platform | image + env vars; no platform SDK in code | restore drill; smoke; alerts routed |
| Observability backend | any Prometheus-compatible scraper | `scripts/validate_observability.py` |
| CI | translate `ci.yml` | same gates |

Rule: the deterministic provider and the kill switch must keep working throughout any substitution.
