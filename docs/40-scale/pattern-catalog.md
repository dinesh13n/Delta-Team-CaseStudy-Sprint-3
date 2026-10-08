# Pattern catalogue

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. **Suggest-only AI with an approval record.** The model proposes; a person decides; the audit links both.
2. **Policy as data.** One YAML source generates the enforced rules and the independent policy engine's rules; a test proves equivalence.
3. **Quarantine, don't block.** Bad rows leave the served layer with a reason and a source row; the run fails only above a ratio.
4. **Atomic publish.** Write to staging, rename per file, marker file last.
5. **Fail-closed integration stubs.** An unconfigured IdP or model refuses everything rather than falling back to open.
6. **Locks for prompts and models.** Hash/identity compared at start-up.
7. **Kill switch plus deterministic fallback.** The core workflow never depends on the model.
8. **Evidence-first delivery.** Thresholds committed before results; manifests with hashes; each claim tagged verified / inferred / assumed / unknown.
