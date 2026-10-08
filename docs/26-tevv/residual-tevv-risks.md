# Residual TEVV risks

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | tevv-results.md, red-team-findings.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | Owner | Status |
|---|---|---|---|
| TEVV-R-01 | The agent wrote and graded the system, datasets and tests. No independent review. | [UNK] named reviewer (OQ-05) | OPEN, blocks an unconditional GO |
| TEVV-R-02 | Zero-tolerance thresholds are valid for a deterministic provider; a real model needs statistical thresholds with confidence bounds | [UNK] model owner | OPEN until OQ-02 |
| TEVV-R-03 | Latency is in-process; real model/network latency and cost are unmeasured | [UNK] platform owner | OPEN |
| TEVV-R-04 | Datasets are constructed, not sampled from production; adversarial coverage is what the author imagined | Delta-Team lead | ACCEPTED for pilot |
| TEVV-R-05 | `[unrecognised]` degradation (RL-01) means summary usefulness is unproven on real vocabulary | [UNK] business owner | OPEN |
| TEVV-R-06 | Purpose defaulting (RL-02) | [UNK] security owner | ACCEPTED, see risk-acceptance-register |
| TEVV-R-07 | Playwright spec was exercised through its Python equivalent, not via `npx playwright test` | Delta-Team lead | OPEN, run in CI |
| TEVV-R-08 | No accessibility audit was done on the operations view | [UNK] | OPEN |

[VF] "Owner" is the role that must accept or close the item. No person has been named by the engagement; those are marked [UNK] rather than invented.
