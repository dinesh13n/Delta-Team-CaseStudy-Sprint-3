# Implementation PRD (v2, supersedes the Initial PRD)

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | docs/09-initial-prd/*, EVD-H-* |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED (OQ-05) |
| Residual risks | TR-02 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Derived from `docs/09-initial-prd/initial-prd.md` and reconciled with what Stage H proved. It is **not** a copy: see `prd-change-log.md` (14 material changes) and `invalidated-assumptions.md` (9 assumptions).

## 1. Problem and outcome
Unchanged in substance (docs/03-problem-value): operations staff cannot trust record lookup, access, intake quality or AI output in the logistics platform. Outcome for this release: a service where a record lookup is exact, access is persona-based and enforced, data defects are quarantined, an exception summary is governed and suggest-only, and every decision is traceable.

## 2. What is built (proven in Stage H)
| Capability | State | Evidence |
|---|---|---|
| Trusted record access (exact key, 404/422) | BUILT | EVD-H-05 |
| Contextual access control (8 personas, field masking, Rego parity) | BUILT; scope narrowing NOT enforceable | EVD-H-04 |
| Validated data intake (curated + quarantine, run report, exit code) | BUILT | EVD-H-06 |
| Governed exception summary (deterministic default) | BUILT; real model BLOCKED by OQ-02 | EVD-H-07 |
| Traceable decisions (hash-chained audit, correlation id, approvals) | BUILT; external sink DEFERRED | EVD-H-08 |
| Operational telemetry (/metrics, /ready, JSON logs) | BUILT; dashboards/alerts in N1 | EVD-H-09 |
| Thin read-only operations view | Release 1 (J4) | AC-26 |
| Carrier booking saga (idempotency, retry ceiling, compensation) | moved INTO Release 1 as a tested library with a simulated carrier (J5) | AC-27 (new) |

## 3. Requirements
FR-01..FR-20 and NFR-1..NFR-10 stand; finalized NFR values are in `finalized-nfrs.md`; acceptance criteria in `finalized-acceptance-criteria.md` (AC-01..AC-27).

## 4. Success metrics
K1..K10 frozen in C1 **with one amendment**: K4 is now "usable (non-null and non-empty) correlation share", baseline 33.6% (D-012). All other definitions are unchanged.

## 5. AI position
Suggest-only (L0). The model path is a port with a deterministic default; a real model is a condition of production (OQ-02, OQ-03).

## 6. Boundaries
See `release-boundaries.md`. Out of scope: ETA prediction, route optimisation (no real history), full portal, agents.
