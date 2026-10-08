# Business Workflow Map

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 5 current state) |
| Runbook step | C4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/discovery/; evidence/05-current-state/EVD-C-04-flow-to-code-trace.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Flow-to-code trace (also in evidence/05-current-state/EVD-C-04-flow-to-code-trace.md):

| Declared flow | Implementing files | Status |
|---|---|---|
| Booking to pickup | none | **NOT IMPLEMENTED** (data columns only: shipments.status, promised_at) |
| Hub scan to route assignment | none | **NOT IMPLEMENTED** (tracking_events, routes data only) |
| Carrier booking saga | none | **NOT IMPLEMENTED**; compensation exists only as the column `compensation_required`; retry_count 51 to 4,995 in data (F-38, F-39) |
| Exception investigation to delivery evidence | apps/api/main.py `/records/{id}`, `/ai/summarize/{id}`; domain_service.py | **PARTIAL**: single-record read and a simulated summary; no evidence assembly |
| AI: ETA prediction, route optimisation, exception copilot | ai_gateway.py (one summary function) | 3 declared, **0 implemented** (F-29) |
