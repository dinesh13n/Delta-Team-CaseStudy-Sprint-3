# Retrieval strategy

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-A-04b data profile; EVD-C-05 profile; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | OQ-14 ruling provisional; approvers UNRESOLVED |
| Residual risks | See data-context-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Decision [INF]: no vector retrieval. The only GenAI use case (I9 exception summary) needs structured facts about one shipment and its events; these are fetched by key through the DataRepository, filtered by access-semantics for the caller, then reduced by ai-context-policy to an allow-list. Alternatives rejected: embedding search (no unstructured corpus, adds cost, leakage surface), full-table prompt stuffing (cost, privacy).
