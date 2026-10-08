# PRD change log (Initial PRD -> Implementation PRD)

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | EVD-F-04, EVD-H-*, D-012 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Section | Initial PRD | Implementation PRD | Why (evidence) |
|---|---|---|---|---|
| 1 | K4 definition | non-null correlation_id / total | usable (non-null AND non-empty) share; baseline 33.6% (1,008/3,000) not 66.4% inverse reading | D-012; recount EVD-A-04c: 983 null, 1,009 empty, 1,008 non-empty |
| 2 | Scope: operator portal | OQ-06: thin view in MVP | thin read-only view specified as Release 1 item; Angular portal still out | MVP scope; F-05, F-52 |
| 3 | Scope: carrier saga | Future scope | Release 1 library with simulated carrier | runbook J5; data shows duplicate bookings and retry_count up to 4,995 |
| 4 | Access model | 8 personas | 8 personas plus 2 platform roles (ops, auditor) for /metrics and /audit/verify | [ASM]; personas have no ops function; flagged for owner decision |
| 5 | Health | /health as dependency check (runbook H8) | /health liveness (unchanged behaviour), /ready dependency check | probe P1 shows /health preserved; D-013 |
| 6 | Rule BR-04 | severity block | ETL downgrades to flag | 354/354 rows violate; owner UNRESOLVED |
| 7 | Feature flags | FF-01..FF-07 | FF-06 (audit v1 switch) dropped; rollback by revert | would double audit write paths |
| 8 | AI tokens | token_count reported | token figure is an *estimate* until a real model is used; mean 267.6 vs baseline about 2,562 | EVD-H-07 |
| 9 | Latency | p95 target | p95 measured 11.4 ms in-process only; network/model latency UNMEASURED | EVD-H-07 |
| 10 | Coverage target | >= 80% | achieved 96% (apps + etl) | EVD-H-11 |
| 11 | Schemas | v1.0 | audit/ai-summary schemas v1.1 (relaxed action pattern, added fields) | F3 corrections |
| 12 | Findings count | 57 | 62 (F-58..F-62 added) | EVD-F-04 |
| 13 | Data injection claim | data contains injection payloads | no such payloads exist; tests use constructed payloads | F-60 |
| 14 | Auth | IdP-backed | HS256 bearer now; JWKS verifier fail-closed stub | OQ-07 |
