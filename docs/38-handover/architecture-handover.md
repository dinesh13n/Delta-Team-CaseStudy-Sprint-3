# Architecture handover

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (content) |
| Evidence sources | docs/10-architecture; docs/20-application |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Modular monolith with ports and adapters: API routes → services (policy, repo, AI gateway, audit) → file-based adapters. Policy source of truth is `semantic-layer/access-semantics.yaml` with generated Rego and parity tests. AI is suggest-only behind a gateway with sanitiser, enum allow-list, schema validation, leak check, prompt and model locks, timeout and circuit breaker. Audit is a hash-chained JSONL file; approvals a JSONL store. Known structural limits: single replica (the audit file), no IdP, no scheduler, no tracing, container recipe unbuilt.
