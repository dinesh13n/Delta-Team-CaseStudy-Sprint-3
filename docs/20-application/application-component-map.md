# Application component map

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | repository tree |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Component | Path | Role |
|---|---|---|
| API composition | `apps/api/main.py` | 10 operations, middleware (correlation, metrics, CSP for /ops) |
| Config | `apps/api/config.py` | env settings, feature flags, fail-fast validation |
| Identity | `apps/api/security/tokens.py` | HS256 verifier; JWKS stub fail-closed |
| Policy | `apps/api/security/policy.py` | persona decision, field mask; generated Rego mirror |
| Data | `apps/api/data/repository.py` | exact-key CSV adapter (curated layer) |
| AI gateway | `apps/api/ai/*` | allow-list, sanitise, prompt, provider port, schema, fallback |
| Approvals | `apps/api/approvals.py` | one decision per suggestion |
| Audit | `apps/api/audit_chain.py` | hash-chained JSONL |
| Integration | `apps/api/integration/carrier_saga.py` | idempotent booking saga |
| ETL | `etl/` | validation, quarantine, curated layer |
| Operations view | `apps/web/public/` | static read-only UI at `/ops` |
| Evaluation | `evaluation/` | datasets, runner, thresholds |
