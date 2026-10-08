# Evidence Confidence Matrix

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

| Cause | Supporting evidence | Contradictory evidence | Confidence | Validation method |
|---|---|---|---|---|
| RC-1 No governance by design | ADR-0001 text; no CODEOWNERS or CONTRIBUTING (F-08) | `docs/transformation-roadmap.md` lists modernisation themes | Medium | interview Repository Owner (UNRESOLVED) |
| RC-2 Identity not modelled | main.py:11-17; domain_service.py:12-15; EVD-C-08 tests | none found | High | characterization tests (C8) |
| RC-3 No data contracts | EVD-C-05 profile: defects in all 6 datasets | `data/manifest.json` declares the defects as seeded, so intentional | High (as fixture) | H-stage validation tests |
| RC-4 AI unguarded by design | ai_gateway.py; guardrail_status not_enforced | Code comment shows awareness of issues | High | red team in Stage L |
| RC-5 No evidence by-product | CI runs only pytest; EVD-C-02 failure | none | High | CI redesign (H1/H11) |
Note: injection payloads are NOT present in the data (no free-text field longer than 19 characters), contrary to data/README.md; this weakens "data contains injection samples" but not RC-4.
