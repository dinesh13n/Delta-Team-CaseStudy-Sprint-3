# Cost per request

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (tokens measured; price unknown) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | [UNK] price |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Measured per AI request (EVD-N-04): **271 estimated tokens** mean, 275 max; response 1.0 KB; **1.17 KB audit** and 0.19 KB approval record written; no outbound call.

`cost_request = tokens_in × p_in + tokens_out × p_out + audit_storage + compute`  where p_in, p_out are **unknown** (no model chosen).

Illustrative sensitivity only, using the estimate as total tokens and three spread prices that are **not quotes**:

| USD per million tokens | Cost per request |
|---|---|
| 1 | $0.00027 |
| 5 | $0.0014 |
| 15 | $0.0041 |

Interpretation: at these volumes the model token cost per request is a fraction of a cent. A real model's prompt overhead and output tokens may multiply it several times; it is unlikely to change the order of magnitude conclusion that **tokens are not the main cost** (see cost-per-outcome.md). That is an inference [INF], not a measurement.
