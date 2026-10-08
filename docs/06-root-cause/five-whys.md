# Five Whys

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

**Why can an operator receive a record they did not ask for?** (F-32)
1. `load_record` returns the first row when nothing matches. [VF domain_service.py:15]
2. Because it was written to never raise; the comment calls it "brownfield behavior". [VF]
3. Because no not-found contract exists in the API (no error models, OpenAPI documents only /health). [VF F-50]
4. Because the API contract was never defined before the code (contract-last). [INF]
5. Because modernisation was partial and unmanaged (ADR-0001). [VF]

**Why can a caller act as any role?** (F-17)
1. The role is read from a request header. 2. No authentication layer exists. 3. No identity provider chosen (OQ-07). 4. The service was built behind an assumed trusted network. [ASM, UNK]. 5. No security owner is assigned (OQ-05). [VF]
