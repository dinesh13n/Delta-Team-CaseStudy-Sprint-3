# Interface (port) contracts

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | openapi.yaml; schemas/; docs/09-initial-prd; docs/10-architecture; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; open items in docs/12-specs/spec-readiness.md |
| Residual risks | Specs are PROVISIONAL until OQ-01/02/03/05/11 are ruled |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Port | Methods | Adapters now | Adapters later |
|---|---|---|---|
| DataRepository | get(entity,key) -> Row or None; list(entity,filter,limit,offset); quarantine(entity) | CSV curated layer | database |
| AuditSink | append(event) -> hash; verify() -> result | local JSONL hash chain | external log store |
| ModelProvider | complete(prompt_parts, schema) -> text or error; name, version | deterministic | any LLM vendor (OQ-02) |
| TokenVerifier | verify(token) -> Claims(subject, role, tenant) or error | HS256 (dev) | JWKS/IdP |
| Clock | now() -> datetime (UTC) | system | fixed (tests) |
Rules: adapters never import API code; use cases depend on ports only; ports are typing.Protocol classes with contract tests run against every adapter.
