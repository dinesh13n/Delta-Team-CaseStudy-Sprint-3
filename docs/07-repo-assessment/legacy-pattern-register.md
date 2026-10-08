# Legacy Pattern Register

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 7 repository assessment) |
| Runbook step | C7 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | C2-C6 documents; runbook/01-BASELINE-ASSESSMENT.md findings register; direct reading of the subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Pattern | Where | Note |
|---|---|---|
| Hardcoded shared credential | legacy/reconcile_legacy.py | F-09 |
| Script-as-module with print output | etl, legacy | no logging, no exit code on defects |
| Row-scan lookup over flat file | domain_service.py | F-31 |
| Silent fallback | domain_service.py | F-32 |
| Local-file audit | audit.py | F-44 |
