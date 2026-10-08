# Target Architecture

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

```
client -> API layer (routers, auth dependency, correlation middleware)
          -> application services (lookup, summary, approval, intake)
              -> domain core (identity rules, policy engine, validation rules, audit events)
                  -> ports: DataRepository | AuditSink | ModelProvider | TokenVerifier | Clock
                      -> adapters: curated CSV repository | hash-chained file sink | deterministic + HTTP providers | HS256/JWKS verifier
batch: intake CLI -> domain validation (same rules) -> curated + quarantine layers
```
Principles from the subtree's target-state-principles.md are all honoured: incremental, AI as governed subsystem, policy-as-code, evidence by-product, explicit failure modes, cost tied to outcomes.
