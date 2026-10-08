# Incident reconstruction example

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (author-run) / CONDITIONAL (no second reader) |
| Evidence sources | evidence/31-observability/EVD-N-02-reconstruction.json (SHA-256 1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241) |
| Assumptions | See body |
| Unresolved issues | F-M3-01 source correlation; HC-R-01 |
| Residual risks | N-R-08 reconstruction unproven by a second person |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Question
"Alice approved an AI summary for SHI-00027. Show who did what, under which rule, from which data, produced by what, and who decided." Answered from the audit chain and the approval store only, without application logs. [VF]

## Command
`python -m scripts.reconstruct --audit <audit.log> --approvals <approvals.jsonl> --correlation-id trace-n2-0001`
(or `--summary-id`, `--subject`, `--resource`). The chain is verified first; a broken chain marks the timeline UNTRUSTED.

## Result (EVD-N-02, 10 audit events in the run, 7 of them noise from other callers)
| # | Link | Found | Where |
|---|---|---|---|
| 1 | Actor | alice, role dispatcher, auth_method jwt | audit `actor` |
| 2 | Request | `record.read`, `ai.summary`, `ai.decision`, all with correlation id `trace-n2-0001`, echoed in the response header | audit, header |
| 3 | Policy decision | allow, rule `access:dispatcher.shipments`, decision id `pd-737b9b9e40f8` | audit `policy_decision` |
| 4 | Data load | `ld-89446323a790`, equal to the `X-Data-Load-Id` header the caller received | audit detail, header |
| 5 | Producer | deterministic provider, guardrail enforced, prompt `exception_summary_v1`, no fallback | audit detail |
| 6 | Recommendation | suggestion `sum-…`, `requires_human_approval: true` | response, approval store |
| 7 | Human decision | `kind: decision`, approve, decided_by alice | approval store; audit `ai.decision` with `approval_id` |
| 8 | Integrity | chain valid over 10 records; tip hash recorded | `chain` |
| 9 | Trace id | `trace-n2-0001` (correlation id) | every link above |

The script's check `chain_complete` was true. Editing the actor of one past record flipped the chain to invalid and `trusted` to false (tamper test in the same evidence file).

## What the example also exposes [VF]
- **Self-approval is possible.** Requester and decider are both alice. Four-eyes is not implemented (HC-R-01; risk-acceptance RA unsigned).
- **The decision record has no correlation id of its own** (null). It is joined by suggestion id and by the `ai.decision` audit event. The reconstruction script was changed during N2 to follow that join; before the change the decision was not found by correlation id.
- **The model text is not in the audit.** For the deterministic provider the text can be regenerated; for a real model it could not. See ai-telemetry-spec.md.
- **Stored events still have no end-to-end id.** See comparison below.

## Before and after
| Question | Baseline | Now |
|---|---|---|
| Does the record say who acted? | no actor in baseline audit (F-43) | 10 of 10 events carry actor subject and role |
| Does it carry a correlation id? | source stream usable on 1,008 of 3,000 events (33.6%) | 10 of 10 API audit events |
| Does it carry the policy decision? | no | 10 of 10 |
| Can a past edit be detected? | no | yes: hash chain, tested |
| Can the data version be tied to a response? | no | yes: `data_load_id` |
| Can the **source** event stream be correlated? | no | **no change**: the producing system emits no id (F-M3-01) |

The "after" numbers come from a 10-event in-process run, not from production traffic. They show the fields are populated by construction, not what a deployed system will see.

## Limits
Author-run on a single process. Nobody else has tried to reconstruct an incident from this evidence. The first real test is an auditor or on-call engineer doing it unaided.
