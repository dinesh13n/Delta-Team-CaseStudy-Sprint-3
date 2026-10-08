# As-built architecture

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/10-architecture; apps/api |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Modular monolith (FastAPI) with ports: `apps/api/main.py` (routes), `security/` (tokens, policy), `ai/` (gateway, providers, registry, sanitize, locks), `data/repository.py` (curated layer), `audit_chain.py`, `approvals.py`, `correlation.py`, `metrics.py`, `resilience.py` (timeout, retry, breaker, bulkhead primitive), `integration/carrier_saga.py`, `kpis.py`; `etl/` (validation, quarantine, curated load); legacy shims `services/*` kept for one release (DEBT-12). Runtime: Python 3.11 minimum; CI green on 3.11 and 3.14.

Decisions: ADR-0002..0010 (`docs/10-architecture/architecture-decision-summary.md` (sha256 `5086514f77705cb72310e397f890123eb4507251c2797808568b4cf4cba9256e`)). Not built: tracing, external audit sink, bulkhead wiring, platform.
