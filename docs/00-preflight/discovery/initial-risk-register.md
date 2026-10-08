# Initial Risk Register

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

Risks to the engagement and the system as observed. Severity is a first-pass judgement (H/M/L), not a scored assessment; no remedies are proposed here.

| ID | Risk | Evidence | Class | Severity |
|---|---|---|---|---|
| R-01 | Caller-supplied role header is the only access control; AI endpoint unauthenticated | `main.py` 11-24 | [VF] | H |
| R-02 | Wrong or other-entity record returned silently (any-column match, first-row fallback) | `domain_service.py` 11-15; REC-0001 appears in all six files | [VF] | H |
| R-03 | Credential-shaped values committed in source and templates | `legacy/reconcile_legacy.py`, `.env.example` | [VF] | H (low if truly synthetic) |
| R-04 | AI path has no guardrails, schema or injection defence; prompt built with untrusted fields | `ai_gateway.py` | [VF] | H |
| R-05 | Audit cannot reconstruct who did what; sink is a local file | `audit.py`, `otel-notes.md` | [VF] | H |
| R-06 | About 33% of events lack a correlation id | EVD-A-04b | [VF] | M |
| R-07 | Data defects: duplicate keys, blank mandatory fields, mismatched categorical values | EVD-A-04b | [VF] | M |
| R-08 | Declared capabilities (ETA, routing, copilot, portal, flows) are not implemented | `current-state.md` vs code | [VF] | M |
| R-09 | Test base is thin (3 pytest tests) and one test dependency is undeclared | `tests/`, `requirements.txt` | [VF] | M |
| R-10 | Pinned dependencies do not install on Python 3.14 | EVD-A-03c | [VF] | M |
| R-11 | Fixture-coupled smoke check will fail if data is cleaned | `sanity_check.py` | [VF] | L |
| R-12 | Repository is public and holds training material and planted credentials | GitHub repo visibility (user action) | [VF] | M |
| R-13 | Runbook contains at least one wrong quantitative claim (F-42) | assumptions-unknowns.md section 3 | [VF] | M |
| R-14 | No approver named; every gate is provisional | OQ-05 | [VF] | M |
