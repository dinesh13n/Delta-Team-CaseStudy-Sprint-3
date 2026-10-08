# Final capability map

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/09-initial-prd/capability-map.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Capability | State |
|---|---|
| Exact record and shipment lookup | Delivered |
| Identity and policy-based access | Delivered locally (HS256) |
| Data intake validation and quarantine | Delivered |
| Exception summary (suggest-only) | Delivered with deterministic provider |
| Human approval record | Delivered (no four-eyes) |
| Tamper-evident audit and reconstruction | Delivered (local file) |
| Metrics, dashboards and alerts as code | Delivered as files; never run |
| Carrier booking saga (idempotent, bounded retry) | Delivered as library vs simulated carrier |
| Thin operations view | Delivered |
| ETA prediction, route optimisation, exception copilot | **Not implemented** |
| Distributed tracing | **Not implemented** |
| Deployment, IaC, IdP | **Not implemented** |
