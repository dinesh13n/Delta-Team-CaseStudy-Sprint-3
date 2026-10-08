# Semantic-layer portability test (Q1)

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT PERFORMED; protocol pre-registered |
| Evidence sources | evidence/40-scale/EVD-Q-01-preregistration.json |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-02, OQ-03 |
| Residual risks | Portability is claimed by design, not demonstrated |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Result: NOT PERFORMED (BLOCKED)
**Q-X1 is not met.** No Model B build exists. OQ-02 (which two models) is unresolved, no second model is connected to this workspace, and the Model A work was produced by one agent (`claude-sonnet-5-5`). Regenerating the application with that same model would test nothing. This document therefore delivers the part that can be done honestly: a **pre-registered, ready-to-run protocol**, so the later run cannot be shaped by its results. [VF]

## Pre-registered inputs (sha256, declared 2026-10-08T12:12:28Z before any Model B run)
Model B may be shown **only** these inputs, plus the Implementation PRD (`docs/17-implementation-prd/`), the Stage F specs (`docs/12-specs/`) and the prompt registry (`docs/19-intelligence/prompt-registry.md`). It must **not** be shown anything under `07-logistics-shipment-fleet-routing-ops/apps`, `etl`, `policy` or `tests` (except the evaluation datasets used as acceptance inputs).

| File | SHA-256 |
|---|---|
| `semantic-layer/README.md` | `b38fc745d2ddfff755cbb7b92fac68b48d47ea2f7c4b6bae45b757a6de406ec2` |
| `semantic-layer/access-semantics.yaml` | `5082131647358b428f48d7122b8f043150a768a76b32d90031ce89e1540eef84` |
| `semantic-layer/ai-context-policy.yaml` | `b9e7285d1011e6cdad6b3983b83a28828408fd501dfeeb3b7555ca2a8d7ff214` |
| `semantic-layer/business-rules.yaml` | `e33b1d31d398865207a92903354eebc4ce7b78410eb0125d73543738260e900f` |
| `semantic-layer/entities.yaml` | `3d715cf088893a523d37b75fe8f917e9657f495c621478f61d718ce5f51ef8f3` |
| `semantic-layer/enum-violations.md` | `b9273f2c7acc51e258ef6f0cd17f4d7f948ba44752776796a67fb4645b71d8f0` |
| `semantic-layer/generated/semantic-layer.json` | `c5151ff1d4b61bc9e5ea9c058201a6abf946cc6641dc75e243c81cf9dac305e5` |
| `semantic-layer/glossary.md` | `9569ab5509b11aca5bda28195c9ca761c31bc1643a50338e36e66f50f4a1934c` |
| `semantic-layer/metrics.yaml` | `57461956c93b63cff61e57c025ddbaca3e8c690dfcd227c4ae3271a60884560c` |
| `semantic-layer/relationships.yaml` | `262e006b86d8965dc2b3ec36f5353c5f3cdd88fb3ae3673dd9debafd8a810b00` |
| `semantic-layer/schemas/semantic-layer.schema.json` | `cec90e145617f67da4559b1702cfdf19e6f537a37bec26b9d6161b790a4bf34d` |
| `semantic-layer/status-taxonomy.yaml` | `e1573d7580f16635294203c03974c905300f27a5fb5ac6439a083518d7e81008` |

Acceptance inputs (unchanged from Stage J/L; hashes in `EVD-Q-01-preregistration.json`): `evaluation/thresholds.json` (`6138f65a...`), and the four dataset files plus manifest.

## Protocol
1. Create an empty directory containing only the pre-registered inputs. Record the model name, version, date, sampling settings and the full prompt (use `docs/19-intelligence/prompt-registry.md` conventions) in `EVD-Q-01-generation-transcript.*`.
2. Ask Model B to build the agreed subset: **record lookup by exact key, identity and policy decision, AI summary with guardrail, audit v2 with hash chain** (the four behaviours that carry the original critical findings F-17, F-20, F-30/31/32, F-22/24, F-43).
3. Run the unchanged acceptance harness against Model B's build: `semantic-layer/tests`, the evaluation datasets with `evaluation/thresholds.json`, and `scripts/red_team.py` (12 attacks).
4. Fill `EVD-Q-02-comparison.csv` for both builds. Classify each difference as **model-attributable** or **specification ambiguity** (rule: if two reasonable readings of the spec exist and Model B took the other one, it is ambiguity; if Model B contradicted an explicit sentence, it is model-attributable).
5. Feed ambiguities back as corrective actions (`docs/39-continuous-improvement/improvement-backlog.md`, IMP-Q01..).

## Limits to state at the time of the run
A single run of each model is an anecdote, not a distribution. The subset is not the whole system. A second model from the same vendor family shares training biases; prefer a different family if OQ-02 allows. [INF]

## Self-check before any run (can be done now)
`semantic-layer/tests` passes in the repository suite today (176 passed). The layer contains no model-specific text; the generated JSON is validated against `schemas/semantic-layer.schema.json`. [VF, from the D6 gate and the 2026-10-08 re-run]
