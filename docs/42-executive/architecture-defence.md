# Architecture defence

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/10-architecture |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Decision
Modular monolith with ports (Option B) over hardening the old monolith (A) or microservices (C). The delivered system is about 140 lines of application code; microservices would add network failure modes larger than the system (`docs/10-architecture/architecture-options.md` (sha256 `50880e35e33949093985444f22eb68fd53e52683a316e468c1aca2064f1a5c7a`)). ADR-0001 ("keep legacy batch beside FastAPI", never revisited) is superseded by ADR-0002, because its recorded consequence was the root cause of divergent rules and audit behaviour.

## ADRs
0002 supersede 0001; 0003 runtime and dependencies; 0004 identity; 0005 policy as code; 0006 data layer and quarantine; 0007 AI gateway boundary; 0008 audit and correlation; 0009 platform-neutral deployment; 0010 observability.

## Defence of the contentious choices
- **HS256 shared-secret tokens**: chosen because no identity provider exists (OQ-07); fail-closed JWKS verifier is a stub. This is a local-pilot choice, accepted by nobody (RA-02).
- **Platform-neutral container recipe**: OQ-01 is unresolved; we did not pick a cloud to look decisive. Cost: IaC provisions nothing.
- **Deterministic provider as default**: a model is an option behind the gateway, not a dependency.

## Where it is weak
Local file audit sink; in-memory rate limit; single replica; no tracing; bulkhead exists but is not wired to the gateway (F-M3-02). All registered in `docs/42-executive/residual-risks.md` (sha256 `2dc0588056838f047b74c9026ed238f825059c9c3c9fd7a4ccad595cfe3557b2`).
