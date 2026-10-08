# RAG design decision

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT APPLICABLE (justified) |
| Evidence sources | EVD-J-03 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Decision: **no RAG**. Reasons: (1) record-scoped context fits the 2,000-token budget (golden-set max 524 estimated tokens); (2) grounding comes from the allow-listed record, not a corpus; (3) every source is listed in the output (`sources`), which gives provenance without a retriever. `rag-evaluation-results.md` therefore reports "not measured, not applicable".
