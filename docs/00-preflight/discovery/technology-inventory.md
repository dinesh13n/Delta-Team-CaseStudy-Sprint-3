# Technology Inventory

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0A pre-flight discovery |
| Runbook step | A4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead review |
| Evidence sources | EVD-A-04-repo-tree-annotated.txt; EVD-A-04b-data-profile.txt; direct file reads of the repository; evidence/00-preflight/EVD-A-03-toolchain-snapshot.txt |
| Assumptions | See assumptions-unknowns.md |
| Unresolved issues | See assumptions-unknowns.md |
| Residual risks | Read-only discovery only; no behavioural run yet (Stage C) |

Classification key: **[VF]** Verified Fact (read in a cited file), **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown. Paths are relative to `07-logistics-shipment-fleet-routing-ops/`. This document makes no transformation recommendations (Spine 0A).

## 1. Required by the repository (versus installed, see environment-snapshot.md)
| Technology | Required | Source | Sandbox state |
|---|---|---|---|
| Python | >=3.10 (pyproject), CI uses 3.11 | `pyproject.toml`, `ci.yml` | 3.10.12 default; 3.11.15 and 3.14.6 added |
| fastapi | ==0.115.0 | `requirements.txt` | not installed |
| uvicorn | ==0.30.6 | `requirements.txt` | not installed |
| pydantic | ==2.8.2 | `requirements.txt` | not installed; fails on Python 3.14 (EVD-A-03c) |
| pytest | ==8.3.2 | `requirements.txt` | not installed |
| python-dotenv | ==1.0.1 | `requirements.txt` | installed 1.2.3 |
| PyYAML | ==6.0.2 | `requirements.txt` | installed 6.0.3 |
| httpx | undeclared, needed by `fastapi.testclient` | `tests/test_api_contract.py` | not installed |
| @playwright/test | ^1.46.0 | `apps/web/package.json` | not installed |
| Terraform provider `local` | implicit | `infra/terraform/main.tf` | terraform absent |
| OPA / Rego | unversioned | `policy/opa/access.rego` | opa absent |

## 2. Observations
- [VF] `python-dotenv` and `PyYAML` are pinned but no source file imports them (grep of `*.py`).
- [VF] No lockfile for Python or Node; `apps/web/package.json` has no framework (no Angular) in dependencies.
- [VF] Terraform has no `terraform {}` block, no provider version constraints.
- [INF] The pinned set was current in 2024; compatibility with newer interpreters is not guaranteed (confirmed for 3.14, EVD-A-03c).
