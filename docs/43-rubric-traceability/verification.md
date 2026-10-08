# Verification (Document 03 section 5, step R5 checks)

| Field | Value |
|---|---|
| Stage | S: Evidence index and rubric traceability (runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md) |
| Runbook step | 03-4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS on all mechanical checks; one defect found and fixed during the run |
| Evidence sources | EVD-S-04-verification.json; EVD-S-04-verify-r3.py |
| Assumptions | Self-assessment by the same agent that built the evidence; no independent reviewer |
| Unresolved issues | None |
| Residual risks | Mechanical checks prove links resolve; they do not prove the claims are true |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Check (from Document 03) | Result | Detail |
|---|---|---|---|
| V1 | Every index row's hash resolves | **PASS** | 140 of 140 rows: file exists and SHA-256 equals the manifest and the index |
| V1b | Index rows equal manifest rows | **PASS** | 140 manifest rows, 140 index rows |
| V1c | No evidence file outside the index | **PASS** | 0 unindexed files (the two index files and the manifests are exempt) |
| V2 | Every `docs/` citation resolves to a row or file | **PASS after one fix** | 344 evidence paths cited in docs; first run found 1 broken path (`docs/33-vendor-risk/third-party-risk-assessment.md` cited the audit result without its `EVD-M-01-` file-name prefix, so the path did not exist); fixed; rerun 0 unresolved |
| V3 | Every finding is in an index row or in the deferred/accepted register | **PASS** | 60 of 62 findings have at least one evidence row; F-16 and F-48 are DEFERRED and have repo files only (listed in `EVD-S-03`) |
| V4 | Every rubric criterion has at least one row or a stated blocker | **PASS** | rows per criterion (a file can serve several): {'R1': 30, 'R2': 71, 'R3': 19, 'R4': 20, 'R5': 36}; coverage matrix covers all 36 sub-dimensions |
| V5 | Inline citations with hashes match | see `cite_check` in the commit message of this step | 200 of 200 matched before this run; rechecked after the edits |

## What these checks do not prove
- A row linked to a finding shows the evidence is *about* that finding, not that the fix is correct. [VF]
- 116 of 140 rows get their rubric criteria from the stage they belong to (`stage-default`), only 24 from the Document 03 matrix. A file can support more criteria than its row lists. [VF]
- Finding links for 36 findings are a hand-written table (`EVD-S-03`), because their dispositions cite tests and code rather than evidence files. Each path was checked to exist; the pairing is the author's judgement. [VF]
- Nobody other than the author has reviewed any of this (no reviewer exists, OQ-05). [VF]

## Final run over all 143 rows (after every edit of this step)
result PASS: 143 of 143 rows, 143 manifest rows, 0 unindexed files, 347 evidence paths cited in docs and 0 unresolved, 60 of 62 findings in rows (F-16 and F-48 deferred), all five criteria have rows. Command: `python3 evidence/43-rubric-traceability/EVD-S-04-verify-r3.py . <out>`.

## Addendum 2026-10-08 (Runbook 04)
Runbook 04 added `EVD-T-01` (the operator decision record). The index was regenerated to 144 rows and the same verifier rerun: PASS, 144 of 144 rows, 0 unindexed files, 0 unresolved citations.
