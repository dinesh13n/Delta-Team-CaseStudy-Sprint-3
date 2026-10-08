# Evidence index notes

| Field | Value |
|---|---|
| Stage | S: Evidence index and rubric traceability (runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md) |
| Runbook step | 03-3 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROVISIONAL |
| Evidence sources | evidence/EVIDENCE-INDEX.md; evidence/EVIDENCE-INDEX.csv |
| Assumptions | Self-assessment by the same agent that built the evidence; no independent reviewer |
| Unresolved issues | None |
| Residual risks | See verification.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- The Stage R2 index (5 columns) is replaced by the 10-column index Document 03 section 5 asks for, plus an 11th column `Rubric basis`. The R2 index remains in git history.
- 140 evidence files; this run added the `EVD-S-*` files (stage S = Runbook 03) and the Stage Q portability files.
- **Findings addressed** come from two sources: the evidence column of `EVD-F-04b` and `EVD-F-04` (by evidence ID or path), and `EVD-S-03-finding-evidence-links.csv` for findings whose disposition cites code and tests.
- **Rubric criteria** come from the Document 03 matrix where the file is named there; otherwise from the stage (A,B,C,O: R1; D,H,M: R2; E,I: R4; G,K,N,P: R3; J: R2 and R4; L: R3 and R4; Q: R2 and R5; F: R4; R and S: R5).
- The index files themselves are derived and are not listed in a manifest. The verifier treats them as exempt.
- Order of operations: `EVD-S-04` verified an index of 140 rows. It then registered itself, its script and the index generator, and the index was regenerated to 143 rows. Those last three rows are not covered by `EVD-S-04`; a final run over all 143 is recorded at the end of `verification.md`.
