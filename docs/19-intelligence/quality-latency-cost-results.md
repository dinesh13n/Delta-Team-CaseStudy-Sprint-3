# Quality, latency and cost vs the envelope

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PARTIAL (no model) |
| Evidence sources | EVD-J-03, EVD-H-07, docs/00-preflight/ai-economics/ |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Dimension | Envelope (A6, ASM) | Measured | Result |
|---|---|---|---|
| AI latency p95 | <= 3,000 ms | 1.04 ms in-process, deterministic; p50 0.52 ms | MET for the deterministic path; **model/network latency UNMEASURED** |
| Non-AI API latency p95 | <= 500 ms | in-process only (EVD-H-07: 11.4 ms p95 including HTTP stack in TestClient) | MET in test; no load test (see L2) |
| Tokens per request | A6 scenario S3 about 2,562 | estimate mean 277.0, max 524 (192 cases); 267.6 mean over the 349 real shipments (EVD-H-07) | estimate only; `token_source: estimate` |
| Cost per request | <= 2.25 cost units [ASM] | 0 model cost (no call) | not comparable until OQ-02 gives prices |
| Quality | none defined at baseline | pass rates above | first defensible measurement (answers F-29) |

Cost formula for a future model: (T_in x P_in + T_out x P_out)/1e6; with estimated T_in about 277 tokens per request and the A6 volume (354 requests per period) that is about 98k input-equivalent tokens per period before output [INF]; prices UNKNOWN.
