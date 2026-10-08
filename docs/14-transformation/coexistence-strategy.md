# Coexistence strategy

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/10-architecture; docs/11-data-context; docs/12-specs |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; platform OQ-01 |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Legacy path | Modern path | Coexistence rule | Retirement trigger |
|---|---|---|---|
| `apps/api/services/domain_service.load_record` (first-row fallback) | DataRepository exact lookup | modern is default; legacy behaviour kept behind `LOOKUP_MODE=legacy` for local comparison only | H10 report accepted and one release without regression |
| `apps/api/services/audit.write_event` | AuditSink v2 | v1 lines remain readable; v2 file is separate (`audit-v2.log`) | v1 writer deleted after H11 |
| `etl/run_daily_batch.py` counting | validated ETL with quarantine | old CLI flags (`--sample`) kept; old output keys retained plus new keys | next minor version |
| `legacy/reconcile_legacy.py` | not modernised in MVP | untouched; documented as legacy reconciliation | OQ decision on carrier saga scope |
| `data/synthetic/*` | `data/curated`, `data/quarantine` (derived) | fixture read-only, `sanity_check.py` still asserts against it | never (fixture is the oracle) |
| ADR-0001 partial modernization | ADR-0002 modular monolith | ADR-0001 marked superseded, not deleted | done in H12 |
