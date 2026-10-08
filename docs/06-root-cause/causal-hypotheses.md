# Causal Hypotheses

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 6 root cause) |
| Runbook step | C6 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/07-repo-assessment/baseline-behaviour.md; docs/05-current-state/; EVD-C-02, EVD-C-03, EVD-C-05; docs/ADR in subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Hypothesis | Type |
|---|---|---|
| CH-1 | Partial modernisation without governance produced divergent rules across code paths | structural |
| CH-2 | Missing identity model causes wrong-record and wrong-actor outcomes | direct |
| CH-3 | Absent data contracts allow defects into every dataset | direct |
| CH-4 | Absent evidence by design causes unprovable claims | structural |
| CH-5 | AI was added before its controls | structural |
Correlation is not labelled causation: CH-1 and CH-4 are supported by documents and absence of artifacts, not by controlled observation.
