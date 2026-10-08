# Agent telemetry specification

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (scope: suggest-only agent) |
| Evidence sources | tests/test_human_control.py (10 tests) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | HC-R-01 no four-eyes on approvals |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The system's only agent-like component is the AI gateway: it chooses nothing and acts on nothing (HC-controls, K stage). Its telemetry is therefore the AI telemetry; there is no tool-calling loop, planner or multi-step state to observe.

| Agent concern | Telemetry |
|---|---|
| What did it propose | `ai.summary` audit event with summary id |
| What data did it see | `data_load_id`, allow-listed facts only (source tracked in the gateway output) |
| Did it try something forbidden | guardrail and leak counters; sanitiser signals in audit |
| Who accepted it | `ai.decision` audit event, approval record (`decided_by`) |
| Did it act without approval | structurally impossible: no write route exists except the decision record (test `test_human_control.py`) |
| Is it stuck or flapping | `ai_circuit_open`, fallback rate |

## If agency is added later
Tool-call telemetry (tool name, argument hash, result class, approver) and a per-run budget metric are required before any write-capable tool is allowed. Not designed in detail: there is no such tool.
