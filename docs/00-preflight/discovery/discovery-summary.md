# Discovery Summary

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

## 1. Orientation in six lines
1. [VF] A small, file-backed FastAPI service (3 routes), two batch scripts, an unwired web scaffold, and synthetic data, with stubs for IaC, policy and CI.
2. [VF] The data layer holds six 354-row CSVs and a 3,000-event stream, all with seeded defects.
3. [VF] Access control is a caller-set header; the AI endpoint has none; audit is a local file without actor or correlation id.
4. [VF] The declared domain (4 business flows, 8 personas, 3 AI capabilities) is mostly absent from code.
5. [VF] Three tests exist; the suite needs an undeclared dependency and has not been run.
6. [UNK] Real runtime, ownership, platform and models remain unanswered (OQ-01, 02, 03, 05, 11).

## 2. Cross-check against the runbook
- Independently reproduced: tree and inventory, endpoints, role header and allow-list, hardcoded credential, first-row fallback, 354/3,000 counts, duplicate keys and blank fields in each CSV, `REC-` key in all six files.
- Contradicted: F-42 magnitude (983 nulls, 32.8%, not 66.4%). See assumptions-unknowns.md section 3.
- Documentation drift confirmed: README `uvicorn apps/api.main:app` is not a valid module path; `clinician` in a logistics role list.

## 3. Readiness for the next step
- A5 (provisional operating contract) can proceed: components, stores and boundaries are enumerated.
- Qualification (Stage B) and the economics envelope (A6) depend on UNK-1 to UNK-5 only for gating, not for drafting.
