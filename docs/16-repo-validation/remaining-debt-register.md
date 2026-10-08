# Remaining debt register

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft; owners UNRESOLVED, dates proposed [ASM] |
| Evidence sources | EVD-H-* , docs/14-transformation/transformation-risks.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Debt | Finding | Why deferred | Owner | Target |
|---|---|---|---|---|---|
| DEBT-01 | CI never executed on GitHub; branch protection not applied | F-08, F-47 | needs push + admin | Repository Owner (UNRESOLVED) | at first push |
| DEBT-02 | JWKS/IdP verifier is a stub | F-17 | no IdP (OQ-07) | Platform/Security lead (UNRESOLVED) | before any non-local env |
| DEBT-03 | Real model not wired; tokens are estimates | F-27, F-28 | OQ-02 unresolved | AI lead (UNRESOLVED) | J1/Q |
| DEBT-04 | Audit sink is local file (hash chain only) | F-44 | no external store | Platform lead (UNRESOLVED) | M2 |
| DEBT-05 | Scope narrowing (hub/fleet) not enforceable | F-18 | no attributes in data | Data owner (UNRESOLVED) | when attributes exist |
| DEBT-06 | Docker, Terraform not built/validated | F-07, F-48 | no runtime | Platform lead | M1 |
| DEBT-07 | Dashboards/alerts as code | F-46 | needs platform | SRE (UNRESOLVED) | N1 |
| DEBT-08 | BR-04 declared block but 354/354 violate; ETL flags instead | rule | meaning unknown | Business owner (UNRESOLVED) | before production |
| DEBT-09 | F-59: actual > declared weight on 171 rows, meaning unknown | F-59 | no owner answer | Business owner | before production |
| DEBT-10 | Web operator portal does not exist | F-05, F-52 | OQ-06 | Product owner | J4 |
| DEBT-11 | History contains secret-shaped values | F-09..F-12 | cannot rewrite baseline | Repository Owner | rotate before deploy |
| DEBT-12 | Legacy shims (`services/audit.py`, `domain_service.py`) remain | F-43 | compatibility | Dev lead | after FF-02 sunset |
| DEBT-13 | `starlette TestClient` httpx deprecation warning | n/a | tool chain | Dev lead | next dependency bump |
| DEBT-14 | npm audit not run | F-04 | scaffold only | Web lead | J4 |
