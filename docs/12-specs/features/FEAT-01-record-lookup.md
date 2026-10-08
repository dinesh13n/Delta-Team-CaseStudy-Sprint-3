# Record lookup and operations view

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/functional-requirements.md; openapi.yaml |
| Assumptions | See body |
| Unresolved issues | See spec-readiness.md |
| Residual risks | Provisional |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Behaviour.** GET /records/{id}, GET /shipments, GET /shipments/{id}/events. Lookup is exact on the business key column only (never any column value). Key pattern `SHI-[0-9]{5}` for shipments (semantic layer BR-K-shipments). Non-matching shape -> 422; well-formed but absent -> 404. Rows with data-quality flags are returned with `data_quality_flags`. The thin operations view (OQ-06) is a read-only page or the OpenAPI UI over these endpoints; the Angular portal is deferred.
**Pre-conditions.** Valid token, policy allow. **Post-conditions.** One audit event `record.read`.
**State.** None.

**Requirements.** FR-01, FR-02, FR-18. **Findings addressed.** F-16, F-30, F-31, F-32. **Acceptance criteria.** see `../acceptance-criteria.md`.
