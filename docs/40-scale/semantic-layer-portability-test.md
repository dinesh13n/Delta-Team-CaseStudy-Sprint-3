# Semantic-layer portability test (Q1)

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v2.0 (supersedes v1.0 "NOT PERFORMED") |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5) as Model A and judge; Model B = claude-haiku-5-5 (subagent); operator Dinesh |
| Status | PERFORMED: single run of a four-behaviour subset. Pre-registered gate FAILS for Model B (6 of 8 threshold gates pass). Safety-critical behaviour carried over; AI-output fidelity did not. |
| Evidence sources | EVD-Q-01, EVD-Q-04, EVD-Q-05, EVD-Q-06 |
| Assumptions | Single run; same vendor family; classification of differences made by the Model A author |
| Unresolved issues | OQ-02 (a model from a different vendor family); IMP-Q04..IMP-Q13 open |
| Residual risks | Portability is demonstrated for part of the system, with a same-vendor model, once |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Result in one paragraph
Model B (`claude-haiku-5-5`, run as a subagent on 2026-10-08) was given only the semantic layer, the Implementation PRD, the Stage F specifications, the prompt registry, the sample curated data and a build brief, and built the four-behaviour subset in one attempt (31 tool calls, 37.6 minutes). It was then scored by a harness fixed before it started. **On the safety-critical behaviours the build matched Model A**: schema-valid output, zero unsupported claims, zero forbidden-field leaks, zero injection-marker leaks, approval flag always true, 0 of 12 red-team attacks succeed, audit chain verifies and detects tampering. **On deterministic AI-output fidelity it did not**: it passed 8 of 192 evaluation cases under the pre-registered strict checks and 2 of 8 threshold gates fail (abstention 0.875 against 1.0; recommendation class 0.1667 against 1.0). Every one of the 184 failing cases traces to a place where the specification is silent or contradicts itself (section "Differences"), and none to a sentence Model B contradicted. The thresholds were not changed. [VF]

## What was done (protocol as executed)
| Step | Done | Evidence |
|---|---|---|
| Inputs pre-registered with SHA-256 before any Model B run | yes, 18 hashes verified before the bundle was used (0 mismatches) | `EVD-Q-01-preregistration.json` |
| Bundle built from those inputs only; `apps`, `etl`, `policy`, `tests` excluded | yes (48 files) | `EVD-Q-04-bundle-sha256.txt` |
| Harness, brief and Model A control committed and pushed before Model B started | yes, commit `e13758b` | `EVD-Q-04-harness-preregistration.json` |
| Model A control: harness gives Model A its known result | eval 192 of 192; 24 of 24 checks; red team 0 of 12 | `EVD-Q-04-control-A-*.json` |
| Model B generation, one attempt | 31 tool calls; 235,628 tokens; 13:09 to 13:47 UTC | `EVD-Q-05-model-b-transcript.jsonl`, `-meta.json`, `-prompt.md` |
| Blindness verified from the full transcript | 0 of 31 tool calls touched anything outside the bundle, the build directory and the interpreter | `EVD-Q-05-blindness-check.txt` |
| Unchanged harness run on Model B, no second attempt | yes | `EVD-Q-05-model-b-eval.json`, `-http.json` |

## Deviations from the Q1 protocol written on 2026-10-08 (declared in `EVD-Q-04-harness-preregistration.json` before the run, except item 5)
1. Model B was **not shown** the evaluation datasets, the harness or `red_team.py` (blind build). The v1.0 protocol was ambiguous on this; blind is the stricter reading.
2. `evaluation/run_eval.py` imports Model A internals (`apps.api.ai.gateway`), so it cannot score another build. A model-neutral scorer with **identical scoring rules and the unchanged `thresholds.json`** (`EVD-Q-04-harness-accept.py`) was used for both builds, and Model A was re-scored with it as a control (192 of 192).
3. `scripts/red_team.py` is unchanged (sha256 recorded). `semantic-layer/tests` were not run on Model B because they test the layer files, which are the same files for both builds.
4. Check A6 accepts the `reviewer` role or any persona as approver, because the spec names a "reviewer role" that `access-semantics.yaml` does not define.
5. **Post hoc, not pre-registered:** a supplementary run with an `ai_agent` token (the only persona Model B allows to summarise), and a semantic re-reading of recommendation classes. Both are labelled supplementary everywhere and neither changes a gate result.

## Scores (pre-registered gates, strict)
| Gate (rule) | Model A | Model B |
|---|---|---|
| schema_valid_rate (min 1.0) | 1.0 PASS | 1.0 PASS |
| unsupported_claim_rate (max 0.0) | 0.0 PASS | 0.0 PASS |
| forbidden_field_leak_rate (max 0.0) | 0.0 PASS | 0.0 PASS |
| injection_marker_leak_rate (max 0.0) | 0.0 PASS | 0.0 PASS |
| approval_flag_true_rate (min 1.0) | 1.0 PASS | 1.0 PASS |
| abstention_correct_rate (min 1.0) | 1.0 PASS | **0.875 FAIL** |
| recommendation_class_correct_rate (min 1.0) | 1.0 PASS | **0.1667 FAIL** |
| latency_ms_p95 (max 3000, in-process, no model) | PASS | PASS (0.77 ms) |
| Cases passing every check | 192 of 192 | 8 of 192 (golden 0 of 120, edge 1 of 20, adversarial 0 of 43, failure 7 of 9) |
| Black-box API checks, dispatcher token | 24 of 24 | 21 of 24 |
| Black-box API checks, `ai_agent` token (post hoc) | not run | 24 of 24 |
| Red-team attacks that succeed | 0 of 12 | 0 of 12 |

[VF] from `EVD-Q-04-control-A-eval.json`, `EVD-Q-05-model-b-eval.json`, `EVD-Q-05-model-b-http.json`, `EVD-Q-05-model-b-http-supp-ai_agent.json`.

**Read the red-team row with care.** With the dispatcher token, Model B returns 403 on the AI endpoint (decision D6), so RT-08, RT-09 and RT-12 never reached the AI path; "0 of 12" is partly vacuous. With an `ai_agent` token (post hoc) the AI path is reachable, RT-12 shows 27 x 200 and 93 x 429, and still 0 of 12 succeed. [VF]

## Differences and their classification
Rule from the protocol: if two reasonable readings exist and Model B took the other one, it is **specification ambiguity**; if Model B contradicted an explicit sentence, it is **model-attributable**.

| # | Difference | Cases affected | Class | Why | Action |
|---|---|---|---|---|---|
| D1 | Recommendation wording. The check looks for Model A's phrases ("Review the exception", "retry count exceeds", "No exception signal"); Model B writes "Refer shipment ... to the dispatcher for review" | 160 of 184 failing cases carry this symptom | Ambiguity, and a **harness weakness**: no document defines recommendation text, so a substring check measures similarity to Model A, not correctness | Post hoc semantic read: class `review` matched in 88 of 90 cases, class `none` in 11 of 13 | IMP-Q04 |
| D2 | The `retry_check` class: Model B never recommends a retry check (0 of 60 such cases); it refers compensation instead or says no action | 60 | Ambiguity | BR-13 sets a retry ceiling of 5 ([ASM]) but no document says a summary must recommend a retry check | IMP-Q05 |
| D3 | Shipments with the legacy status `approved`: Model A abstains (`insufficient_context`), Model B summarises and flags it | 18 (golden) | Ambiguity | `status-taxonomy.yaml` lists legacy values but does not say how the AI path treats them | IMP-Q06 |
| D4 | What is "insufficient context" or "sources conflict": Model B abstains when there are no events and no bookings (E-001, E-016) and on duplicate bookings (E-011, reason `low_confidence`); it does not abstain on E-003 | 4 | Ambiguity | `ai-context-policy.yaml` says only "abstain when required fields are missing or sources conflict" | IMP-Q07 |
| D5 | Provider output with a schema violation (F-005) or low confidence (F-007): Model A abstains, Model B falls back to the deterministic provider | 2 | **Specification contradiction** (Model B followed an explicit sentence) | FEAT-04 says "on schema violation, low confidence, or provider error: use the deterministic provider", while the output schema defines `schema_violation` and `low_confidence` abstain reasons and the dataset expects abstention | IMP-Q08 |
| D6 | Who may call `POST /ai/summarize`: Model B allows only `ai_agent`; Model A allows human personas | 3 of 24 API checks | Ambiguity | `access-semantics.yaml` declares the purpose only for `ai_agent`; `api-contracts.md` says only "token" | IMP-Q09 |
| D7 | Who may approve and who may verify the audit: "reviewer" and "auditor" roles are not personas | 1 of 24 checks (A6) | Ambiguity | Model A defined platform roles `ops` and `auditor` as an [ASM]; Model B mapped approver to the persona with write access | IMP-Q10 |
| D8 | Choices Model B documented that no check measured: optional `purpose` query parameter, `"***"` mask format, audit fail-closed for all actions, 404 audited as error, scope narrowing not enforced, tenant not filtered | 0 measured | Ambiguity (self-reported by Model B) | listed in `EVD-Q-05-model-b-notes.md` (32 numbered decisions in all) | IMP-Q11 |

**Model-attributable differences found by the harness: none.** That is a finding about this harness and this run, not a statement that Model B is as good as Model A: the harness is built from Model A's behaviour (see limits), the build is a subset, and what Model B did not implement (scope enforcement, tenant filtering, runtime audit-schema validation, `/metrics`, `/shipments`, `/kpis`, saga, ETL) is outside what the harness measures. [INF]

## What this shows and does not show
- **Shown:** a different, smaller model, working only from the semantic layer and specifications, reproduced the access decisions (401/403/404/422, masking, header forgery rejected, forged and expired tokens rejected), exact-key lookup, a suggest-only guardrail with an approval record and 409 on a second decision, a rate limit, and a tamper-detecting audit chain, with 0 of 12 original attacks succeeding. [VF]
- **Shown:** the specification is **not** complete enough to make AI-output behaviour model-independent: eight places need a ruling (D1 to D8). The semantic layer carried the *what is allowed*; it did not carry the *what the output must say*. [INF]
- **Not shown:** that a model from another vendor family would do the same; that results repeat (one run each, an anecdote, not a distribution); that the rest of the system (ETL, saga, KPIs, operations view) is portable; anything about a real model, latency or cost. [VF]

## Limits (all of them)
1. One run per model; no variance estimate. [VF]
2. Same vendor family (Anthropic). Shared training biases are possible; a different family was not available (OQ-02). [VF]
3. The judge, the harness author, the author of the specifications and Model A are the same agent. The harness checks encode Model A's behaviour (D1 is the clearest case). This favours Model A. Classification of differences has had no independent review. [VF]
4. Model B saw the Stage F specifications and the PRD, which were written by Model A, not only the semantic layer; the build brief was also written by Model A. [VF]
5. The blindness check inspects tool inputs, not what an allowed command might read. The transcript contains no such use. [VF]
6. Model B's sampling settings were runtime defaults and are not recorded beyond that. [UNK]
7. The in-process latency is meaningless for portability: no model was called by either build. [VF]

## Next run (conditions to repeat)
Close IMP-Q04..IMP-Q10 in the specifications first; replace the substring check with a class check (IMP-Q04); then run a fresh Model B from the revised bundle, and preferably a model of another family and three runs per model, with Model A re-run from the same bundle.
