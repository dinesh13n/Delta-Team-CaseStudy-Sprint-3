# System card

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/25-governance/model-card.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Item | Value |
|---|---|
| System | Logistics: Shipment, Fleet, Routing & Exception Operations, version 1.1.0 (FastAPI) |
| Architecture | modular monolith, ports and adapters; policy engine from `access-semantics.yaml`; curated + quarantine data; AI gateway; hash-chained audit; static operations view |
| Components that use AI | one: `AiGateway` (summary). Everything else is deterministic. |
| Data | synthetic CSV fixture, 2124 shipment rows, quarantine ratio 1.41 % |
| Interfaces | 10 HTTP routes (6 data/AI, 2 platform-gated, 2 public: health and ready) + the generated OpenAPI document + `/ops` |
| Safeguards | token identity, policy, masking, sanitiser, enum allow-list, output leak check, prompt lock, rate limit, body cap, timeout, breaker, kill switch, approval record, audit chain |
| Tested by | 159 automated tests incl. 25 security, 9 human-control, 9 resilience; 192 evaluation cases; 12 red-team attacks |
| Known failure modes | model unavailable -> deterministic fallback; policy denies -> 403; unknown enum -> `[unrecognised]`; circuit open -> fallback `circuit_open` |
| Not built | real identity provider, real carrier integration, real model, deployment, agent features |
| Human oversight | required per suggestion; no autonomous action |
| Monitoring | `/metrics`, JSON logs with correlation id, audit chain verification |

[VF] Matches the model card and the J1 configuration (prompt sha and config hash identical in both).
