# Architecture Options

| Field | Value |
|---|---|
| Stage | F: Target Architecture, Data and Context Strategy, Specs, Traceability (Spine 10) |
| Runbook step | F1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/; docs/06-root-cause/; docs/07-repo-assessment/; semantic-layer/access-semantics.yaml; subtree docs/architecture/target-state-principles.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Dimension | Option A: harden current monolith | Option B (chosen): modular monolith with ports | Option C: microservices |
|---|---|---|---|
| Functional fit | partial | full | full |
| Security | weak (rules duplicated) | single policy/audit core | more surfaces |
| Portability | medium | high (ports) | medium |
| Cost | low | low | high |
| Latency | good | good | network hops |
| Scalability | limited | adequate for scope | high |
| Resilience | weak | timeouts, fallback | partial failures to manage |
| Maintainability | poor | good | overhead too high for 140 lines |
Chosen: B (ADR-0002). Evaluated against NFR-1..10 and root causes RC-1..RC-5.
