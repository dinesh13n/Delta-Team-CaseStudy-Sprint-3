# Repository Overview

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

## 1. What it is
- [VF] A synthetic logistics repository named `07-logistics-shipment-fleet-routing-ops` (`pyproject.toml`, `data/manifest.json`), version 0.1.0, `requires-python >=3.10`.
- [VF] 51 files. Python source is 6 small modules (`apps/api/main.py` 24 lines, `ai_gateway.py` 18, `audit.py` 12, `domain_service.py` 19, `etl/run_daily_batch.py` 20, `legacy/reconcile_legacy.py` 14) plus `scripts/sanity_check.py` 33 lines. Everything else is data, docs, config and stubs (EVD-A-04).
- [VF] README describes it as combining "modern code, legacy scripts, data-quality issues, security weaknesses, incomplete tests, operational gaps, and AI governance debt" (`README.md`).
- [VF] `docs/architecture/current-state.md` states three engineering generations: legacy batch (`legacy/`, `etl/`), FastAPI (`apps/api/`), AI-assisted (`ai_gateway.py`).

## 2. Layout
| Path | Content |
|---|---|
| `apps/api/` | FastAPI application and three service modules |
| `apps/web/` | `package.json`, two TypeScript classes (`api.service.ts`, `operations.component.ts`) |
| `etl/`, `legacy/` | Batch scripts |
| `data/synthetic/` | Six CSVs of 354 data rows each and `events.jsonl` (3,000 lines) |
| `data/` | `manifest.json`, `quality_issues.json`, `README.md`, `contracts/openapi-fragment.yaml` |
| `tests/` | Two pytest files, one Playwright spec |
| `infra/terraform/`, `policy/opa/`, `.github/workflows/` | One stub each |
| `docs/`, `security/`, `observability/`, `supply-chain/` | Short markdown notes |

## 3. Observations
- [VF] No `.git` directory existed before Stage A (baseline established in A1).
- [VF] No Dockerfile, no lockfile, no `Makefile` target for run/serve; Makefile targets are `test`, `smoke`, `etl` (`Makefile`).
- [VF] README quick start says `uvicorn apps/api.main:app` (slash instead of dot), which is not a valid module path (`README.md`).
- [VF] `docs/discovery/README.md` is a placeholder for discovery notes.
- [INF] The repository is a teaching fixture; most "production" artifacts are intentionally stubs.
