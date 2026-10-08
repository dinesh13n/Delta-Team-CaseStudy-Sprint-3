# Deterministic control rules

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/main.py, semantic-layer/*.yaml |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Rules that never depend on a model. A model output can neither relax nor bypass them.

| Rule | Source | Where enforced |
|---|---|---|
| Deny by default | `access-semantics.yaml` | `PolicyEngine` |
| Entity key patterns (`SHI-nnnnn`, …) must match before any data access | `entities.yaml` | `check_key` in `main.py` (422) |
| Exact-match lookup on the entity's own key only (F-30/F-31/F-32) | `entities.yaml` | repository `get` |
| Curated layer only; invalid rows are quarantined | BR-K-*, BR-P-* | ETL |
| One active booking per shipment (BR-05) | `business-rules.yaml` | ETL flag + saga idempotency key |
| Retry ceiling (BR-13) | ASSUMPTION value 5 | `HARD_RETRY_CEILING` |
| Bounded page size (max 100) | NFR | `Query(le=100)` |
| AI rate limit per subject (default 30/min) | config | `rate_limited` |
| Output must validate against the summary schema, or fall back | `ai-context-policy.yaml` | gateway |
| Any forbidden value in output means fallback with `output_policy_violation` | same | gateway `_leaks` |
| Confidence < 0.5 means abstain | model-configuration | gateway |
| Audit event for every decision and every denial | AC-18 | `audit()` in `main.py` |

[VF] Each row names the file where it is enforced; the tests are listed in `autonomy-matrix.md` and `human-control-test-results.md`.
