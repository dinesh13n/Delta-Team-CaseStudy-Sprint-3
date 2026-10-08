# Security and Observability Overview

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0A pre-flight discovery |
| Runbook step | A4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead review |
| Evidence sources | EVD-A-04-repo-tree-annotated.txt; EVD-A-04b-data-profile.txt; direct file reads of the repository |
| Assumptions | See assumptions-unknowns.md |
| Unresolved issues | See assumptions-unknowns.md |
| Residual risks | Read-only discovery only; no behavioural run yet (Stage C) |

Classification key: **[VF]** Verified Fact (read in a cited file), **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown. Paths are relative to `07-logistics-shipment-fleet-routing-ops/`. This document makes no transformation recommendations (Spine 0A).

## 1. Security mechanisms as found
- [VF] Authorisation: `x_user_role` request header, defaulting to `operator`, checked against a hardcoded list; unmatched role returns HTTP 200 with `{"error":"forbidden"}` (`main.py` lines 11-17). Identity is whatever the caller sends.
- [VF] `/ai/summarize/{record_id}` has no role check at all (`main.py` 19-24).
- [VF] Record lookup matches the id against any column value and falls back to the first row (`domain_service.py`).
- [VF] The prompt template interpolates the record with `str.format`; response states `guardrail_status: not_enforced` (`ai_gateway.py`).
- [VF] Credential-shaped values: `SHARED_DB_PASSWORD = "Welcome123"` (`legacy/reconcile_legacy.py`); `.env.example` repeats `Welcome123`, `sk-workshop-hardcoded-example`, `replace-me-but-currently-shared`, `legacy-batch-password`. `LOG_LEVEL=DEBUG`.
- [VF] Terraform writes `shared_user=app_shared` to `generated-env.txt` (`main.tf`).
- [VF] `policy/opa/access.rego` allows `admin` anything and `operator` read; unused by code. `security/threat-model.md` lists six concerns without controls.
- [VF] No TLS, rate limiting, input validation models, CORS settings, dependency scanning or SBOM (`supply-chain/dependency-risk-register.md` says "no SBOM").

## 2. Observability as found
- [VF] `/health` returns static `ok`.
- [VF] Audit log: local file, fields `ts` (naive UTC, `datetime.utcnow()`), `action`, `details`. No actor, correlation id, tenant, model input hash or approval id (code comment and `observability/otel-notes.md` agree).
- [VF] No metrics, tracing, structured application logging, SLOs or dashboards (`otel-notes.md`).
- [VF] `incident-response.md` is "intentionally incomplete"; `failure-injection-drills.md` lists five drills, none executed.
- [UNK] Any existing production monitoring outside this repository.
