# System Landscape

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

## 1. Components found
| Component | Evidence | State |
|---|---|---|
| REST API (FastAPI) | `apps/api/main.py` | [VF] Implemented, 3 routes |
| AI gateway | `apps/api/services/ai_gateway.py` | [VF] Simulated; no external model call (string template plus `time.sleep(0.01)`) |
| Audit writer | `apps/api/services/audit.py` | [VF] Appends JSON lines to `logs/audit.log` |
| Record loader | `apps/api/services/domain_service.py` | [VF] Reads `data/synthetic/shipments.csv` only |
| Daily batch ETL | `etl/run_daily_batch.py` | [VF] Counts rows and blank-field rows, prints a dict |
| Legacy reconcile | `legacy/reconcile_legacy.py` | [VF] Counts rows of `shipments.csv` |
| Web portal | `apps/web/` | [VF] Two classes, no framework dependency, `lint` is `echo scaffold` |
| IaC | `infra/terraform/main.tf` | [VF] One `local_file` resource |
| Policy | `policy/opa/access.rego` | [VF] Two allow rules; not referenced by any code |
| CI | `.github/workflows/ci.yml` | [VF] checkout, Python 3.11, pip install, pytest |

## 2. Not found
- [VF] No database, queue, cache, message broker, secrets manager, container or deployment manifest in the repository.
- [VF] No calls to any external service (grep of source shows only stdlib, fastapi imports).
- [UNK] Whether a real runtime exists elsewhere (production host, shared DB). `.env.example` names a PostgreSQL URL and vendor tokens but nothing in code reads them.

## 3. Declared versus present
- [VF] `docs/architecture/current-state.md` lists ETA Prediction, Route Optimization and Exception Copilot. Only one summarise endpoint exists in code; no ETA or routing code exists.
- [VF] `docs/domain-specific-spec.md` lists eight personas and four business flows; the code implements none of the flows beyond reading a shipment row.
