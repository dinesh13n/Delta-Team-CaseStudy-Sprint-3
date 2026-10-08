# Lock-in analysis

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (assessment) |
| Evidence sources | apps/api/ai/providers.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Layer | Lock-in today | Why |
|---|---|---|
| Application code | low | plain Python/FastAPI, no cloud SDK |
| Policy | low | YAML source; Rego generated; either can be replaced |
| AI interface | low-medium | `ModelProvider.complete(parts, facts)` is provider-neutral; prompts are provider-neutral text with a schema |
| Audit/approval store | low | JSONL files; but multi-replica needs a shared store (design open) |
| Observability | low | Prometheus text format, PromQL; dashboards Grafana-style JSON |
| CI | medium | GitHub Actions YAML |
| Infrastructure | **n/a: no IaC exists** | lock-in cannot be assessed without a platform |

Future lock-in risk is in the model provider's response format, tool-use features and prompt-caching, none of which are used.
