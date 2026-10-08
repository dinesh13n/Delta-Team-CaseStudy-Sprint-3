# Integration Overview

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

## 1. Inbound
- [VF] HTTP: `/health`, `/records/{record_id}`, `/ai/summarize/{record_id}` (`apps/api/main.py`). `data/contracts/openapi-fragment.yaml` documents only `/health`.
- [VF] Web scaffold calls `/api/records/{id}` and `POST /api/ai/summarize/{id}` (`apps/web/src/app/api.service.ts`); no proxy or route mapping from `/api` is defined in the repository.

## 2. Outbound
- [VF] None in code. No HTTP client, DB driver or queue client is imported anywhere.
- [VF] `.env.example` names: `DATABASE_URL` (PostgreSQL, user `app_shared`), `AI_GATEWAY_KEY`, `LEGACY_BATCH_PASSWORD`, `OT_VENDOR_TOKEN`, `LOG_LEVEL`. No code reads these variables (grep for `os.environ`, `getenv`, `dotenv`: only `import os` in `ai_gateway.py`, unused).

## 3. Integrations implied by data and docs but not implemented
- [VF] Carrier partners: `carrier_bookings.csv` has `partner_ref`, `retry_count`, `compensation_required`; no partner client exists.
- [VF] AI model: `ai_invocations.csv` has `model`, `token_count`; `ai_gateway.py` has no provider call.
- [UNK] Real systems of record for shipments, fleet, routes, carriers, customs; ownership of any of them.
