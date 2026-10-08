# Service ownership map

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Component | Runs where | Owner role | Dependencies | Runbook |
|---|---|---|---|---|
| API (`apps/api`) | one container | Dev lead | data layer, semantic layer, audit files | operational-runbook.md |
| ETL (`etl/`) | scheduled job (no scheduler exists) | Data Owner | synthetic/real source files | operational-runbook.md A-13 |
| Policy (semantic layer, Rego) | repo | Security Owner | `access-semantics.yaml` | K4 change process |
| AI gateway | inside the API | AI Governance Owner | provider (deterministic today) | ai-incident-playbook.md |
| Audit and approvals | local files | Compliance Owner | filesystem | incident-response-plan.md |
| Observability | rules in repo; collector undecided | SRE | Prometheus-compatible | observability-spec |
| CI | GitHub Actions | Dev lead | GitHub | ci.yml (never run) |
