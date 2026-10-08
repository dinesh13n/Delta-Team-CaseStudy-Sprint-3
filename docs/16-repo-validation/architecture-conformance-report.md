# Architecture conformance report

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (static import rules); CONDITIONAL (runtime topology) |
| Evidence sources | EVD-H-11-architecture-imports, EVD-F-01 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Checked against ADR-0002..0010 with an AST import-graph check (EVD-H-11-architecture-imports.txt).

| Rule | Result |
|---|---|
| Only `main` composes modules; nothing imports `main` | holds |
| `security` does not import `data` or `ai` | holds |
| `data` does not import `ai` or `security` | holds |
| `etl` does not import the web app | holds (it reuses `config` only) |
| Ports: DataRepository (CsvRepository), AuditSink (JsonlAuditSink), ModelProvider (registry), TokenVerifier (HS256, JWKS stub) | implemented |
| Policy source of truth is `semantic-layer/access-semantics.yaml`; Rego generated; parity test | implemented |
| Raw layer immutable; curated + quarantine derived | implemented |

[ASM] "Clock" port is implicit (timestamps via a single function in `audit_chain`), not a separate adapter. [UNK] A database adapter does not exist: storage is CSV/JSONL by design (ADR-0004).
