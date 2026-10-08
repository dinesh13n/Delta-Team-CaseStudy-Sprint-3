# Token leakage analysis

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (identified) / CONDITIONAL (unquantified) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | [UNK] model |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Where tokens, and therefore money, could be wasted. Quantified only where measured.

| Leak | Mechanism | Measured? | Control |
|---|---|---|---|
| Fallbacks after a model call | model called, answer discarded (invalid output, leak, schema violation) | 3 of 349 fell back (0.9%) in the deterministic run; model run not possible | fallback counter + AiFallbackRateHigh alert |
| Provider timeouts / errors | tokens may be billed for abandoned calls | no | timeout 5 s, breaker (5 failures, 30 s) |
| Repeat requests for the same record | same suggestion regenerated | no | cache design (cache-effectiveness.md) |
| Rejected suggestions | tokens spent, outcome not produced | no human decisions yet | AiSuggestionsRejectedHigh |
| Oversized context | long event history | bounded: last 10 events + exceptions, 2,000-token cap per record | `max_record_tokens` |
| Rate abuse | scripted calls | 429 after 30/min per subject | rate limit |
| Evaluation and red-team runs | development spend | evaluation run with a real model would cost tokens | not run with a model |
| Prompt bloat | system prompt grows | prompt is locked; version recorded | prompt lock |

Leakage cannot be sized until a model is wired. The detection and controls exist; the numbers do not.
