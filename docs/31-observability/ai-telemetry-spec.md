# AI telemetry specification

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485); evidence/26-tevv/EVD-L-02-final-eval-run.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-05 estimates only; no recorded model text |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What is recorded for every AI request [VF]
Audit detail (hash-chained, per request): `generated_by` (model or deterministic or fallback), `fallback_reason`, `guardrail_status`, `prompt_version`, `data_load_id`, `latency_ms`, token estimate, `summary_id`; plus actor, role, correlation id, policy decision. Metrics: counts by producer and reason, latency histogram, estimated tokens, human decisions.

## Fields that are NOT recorded, by design
Prompt text, model output text and record values. The audit proves *that* a suggestion was made, *by what*, *from which data load* and *who decided*; the suggestion text is held with the approval record only as far as the existing store does. A reconstruction therefore cannot replay the exact model answer from audit alone. If the owner needs that, it is a retention and privacy decision (ai-context-policy), not a logging switch.

## Token numbers are estimates
`ai_tokens_total` uses the gateway's own character-based estimate, not provider-reported usage. No provider is wired, so no billed token count exists. Any cost figure derived from it is an estimate (N4).

## Quality signals available
| Signal | Source | Reading |
|---|---|---|
| Fallback rate | ai_fallback_total / ai_requests_total | model unreliability or guardrail pressure |
| Output leak blocks | ai_fallback_total{reason=output_policy_violation} | any non-zero is an incident candidate |
| Schema violations | ai_guardrail_blocked_total | prompt or model drift |
| Human reject share | ai_decisions_total | usefulness / drift proxy; only meaningful when approvals actually happen |
| Abstain share | ai_requests_total{abstained="true"} | no abstains were produced by the validation workload (deterministic provider does not abstain on this fixture) |

## Limits
- No drift metric against the J2 evaluation sets in production; P-stage defines the check.
- Only one prompt version exists and it is locked; `prompt_version` is recorded so a change is visible.
