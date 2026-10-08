# Model card

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (no real model) |
| Evidence sources | docs/19-intelligence/model-configuration.md, EVD-L-02 |
| Assumptions | See body |
| Unresolved issues | OQ-02 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Model
| Item | Value |
|---|---|
| Name / version | `deterministic` provider 1.0 (rule-based template). `local-sim-v1` was the legacy echo. |
| Type | not a learned model |
| Trained on | n/a |
| Real model | **none configured**; `UnconfiguredModelProvider` raises, the gateway falls back |

## Intended use
Produce a structured, factual summary of one shipment's status and recent events with a recommended review step, for a human dispatcher.

## Out-of-scope use
Assigning, re-routing or booking; handling personal data of drivers; legal or customs determinations; any use without human review.

## Configuration (matches J1)
Prompt `exception_summary_v1` sha256 `96b454af407d1b72d729d86b7727fb43cf053bf6fa6076fd4c4d72af4cc35155`; `config_hash` `b397c28d74371723ecf697c92ce1c6e896d0f424c5893d13865213bf91e0d5a8`; max_record_tokens 2000; max_context_tokens 8000; confidence floor 0.5; provider timeout default 5 s; breaker 5 failures / 30 s; rate limit 30 per minute per subject.

## Performance (evaluation set, 192 cases, 2026-10-08)
Schema valid 1.0; unsupported claims 0.0; forbidden-field leak 0.0; injection marker leak 0.0; abstention correct 1.0; recommendation class correct 1.0; p95 0.95 ms (in-process).

## Limitations
The numbers describe a template, not a language model, and say nothing about model hallucination. Enumerated fields in the fixture are workflow words, so summaries show `[unrecognised]` for them.

## Ethical and safety notes
Suggest-only with a mandatory human decision. No demographic data processed. Model-specific bias evaluation is not meaningful for this provider and is **not done**.

## Update rule
A real model requires: new section here, TEVV re-run with statistical thresholds, red team on the model, register update, owner approval.
