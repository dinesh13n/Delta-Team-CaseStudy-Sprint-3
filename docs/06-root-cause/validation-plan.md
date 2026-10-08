# Root Cause Validation Plan

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

| Cause | Validation | Step |
|---|---|---|
| RC-1 | Interview owner; compare code-path audit behaviours | B2 follow-up (needs owner) |
| RC-2 | Characterization tests 1 to 6 | C8 |
| RC-3 | Re-run profile after intake validation | H6, H11 |
| RC-4 | Author injection payloads and test | L3 |
| RC-5 | Compare CI outputs before/after | H1, H11 |
