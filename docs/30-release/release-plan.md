# Release plan

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (plan written; not executable) |
| Evidence sources | docs/18-delivery, evidence/30-release/EVD-N-03-backup-restore.json (SHA-256 a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e) |
| Assumptions | See body |
| Unresolved issues | OQ-01, OQ-05, OQ-07 |
| Residual risks | N-R-09 release never exercised on a platform |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What "release" means here
The deliverable is a **production candidate**: a tagged repository (`release/v1-production-candidate`, created in R5) with evidence, not a running service. Production deployment is blocked: no platform (OQ-01), no IdP (OQ-07), no model (OQ-02/03), no named approver (OQ-05). [VF]

## Candidate contents
| Item | Version / state |
|---|---|
| Application | `apps/api` 1.1.0, modular monolith, 170 tests passing, coverage 97% |
| Data pipeline | `etl/run_daily_batch.py`, atomic publish, row-shape quarantine |
| Policy | `semantic-layer/access-semantics.yaml` + generated Rego, parity-tested |
| AI | deterministic provider default; model provider unconfigured (fail-closed) |
| Observability | 15 alerts + 3 dashboards as code, validated against the exported metrics |
| Container | `Dockerfile` written; **image never built** (no container runtime in the working environment) |
| CI | `.github/workflows/ci.yml`; **never ran on GitHub** |
| IaC | **none** (BLOCKED, M-X2) |

## Sequence (when a platform exists)
1. Merge to main through reviewed PR; CI green (first real run).
2. Build image from the tag; record digest; scan; SBOM attach.
3. Deploy to a non-production environment; run smoke set (`scripts/sanity_check.py`, `/ready`, one request per route).
4. Restore drill on that environment (backup-validation.md).
5. Go/no-go (go-no-go-criteria.md) with named approvers.
6. Production deploy behind the AI kill switch set to **off** (`AI_ENABLED=false`), data and API first, AI second.
7. Enable AI with the deterministic provider; enable a model only after TEVV is re-run on that model (L stage thresholds).

## Not in this release
Real model, IdP/JWKS, four-eyes approvals, tracing, scheduler for the ETL, multi-replica audit.
