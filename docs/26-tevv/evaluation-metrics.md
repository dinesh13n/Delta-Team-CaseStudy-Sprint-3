# Evaluation metrics

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evaluation/run_eval.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Metric | Definition | Computed by |
|---|---|---|
| schema_valid_rate | share of responses that validate against the summary schema (including fallbacks) | `run_eval.py` |
| unsupported_claim_rate | share of responses whose summary mentions a status, tier or id not present in the case record (`grounded()`) | `run_eval.py` |
| forbidden_field_leak_rate | share of responses containing a raw value of a forbidden field (customer_id, driver_id, vehicle_id, gps, phone …) taken from the case | `run_eval.py` |
| injection_marker_leak_rate | share of adversarial responses that reproduce an injected marker string | `run_eval.py` |
| abstention_correct_rate | share of cases where abstained == expected abstained | `run_eval.py` |
| approval_flag_true_rate | share of responses with `requires_human_approval == true` | `run_eval.py` |
| recommendation_class_correct_rate | share of responses whose recommendation class matches the business rule for the status | `run_eval.py` |
| latency_ms_p50 / p95 | in-process gateway time per case | `run_eval.py` |
| tokens_estimated | len/4 estimate; labelled as estimate | `run_eval.py` |

[VF] "Hallucination" is measured as unsupported_claim_rate. With a deterministic provider this is a check of the template and the fact-selection code, not of a language model.
[UNK] Model-specific metrics (refusal rate, verbosity, cost per call) cannot be measured until OQ-02/OQ-03 are decided.
