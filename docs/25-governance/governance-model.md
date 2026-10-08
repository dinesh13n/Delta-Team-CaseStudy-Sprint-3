# Governance model

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | .github/CODEOWNERS, tests/test_prompt_lock.py |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Body / role | Decides | Cadence | Input | Status |
|---|---|---|---|---|
| Sponsor | scope, accepts business risk | per release | R1 decision pack | [UNK] person |
| Product owner | backlog, KPI definitions | sprint | KPI reports | [UNK] |
| Architecture owner | ADRs, platform | per change | ADRs | [UNK] |
| Security owner | access rules, risk acceptance for security items | per change | K2 | [UNK] |
| AI governance owner | prompt/model changes, AI register, model card | per change | eval, TEVV | [UNK] |
| Data owner | enum vocab, quarantine, BR-04/BR-06 rulings, retention | monthly | quarantine report | [UNK] |
| Compliance owner | CO-01..CO-09 validation | quarterly | obligations | [UNK] |
| Release approver | go/no-go | per release | gates | [UNK] |
| Independent reviewer | re-run evaluation, review gates | per release | evidence pack | [UNK] |

## Change control
| Change | Path |
|---|---|
| code | pull request, CODEOWNERS review, CI (tests, lint, types, secret scan) |
| prompt | edit + `lock_prompts.py` + eval re-run + AI governance review |
| access rules | edit YAML + regenerate Rego + parity test + security review |
| thresholds | change only through a new versioned file, never in place; reasons recorded |
| model | model card update + TEVV re-run + register update |

[ASM] The cadence values are proposals. [VF] The change paths for code, prompt and access rules are enforced mechanically by tests; the review steps depend on CODEOWNERS and branch protection which have not run on GitHub.
