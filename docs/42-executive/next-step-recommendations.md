# Next-step recommendations

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/40-scale/90-day-roadmap.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

In order of cost to the CTO, cheapest first:
1. **Today**: decide repository visibility (public, holds planted credential-shaped values and the training PDFs); enable branch protection and required checks on `main` (CI is green).
2. **This week**: name sponsor, repository owner, security owner, SRE; sign or reject RA-01..RA-12; assign one independent reviewer to this pack (closes G9, G11 in part).
3. **Days 0-30**: revoke or confirm-fake the five credentials in history; choose platform and identity provider; build and scan the image.
4. **Days 31-60**: deploy to a test environment; stand up a collector and alert routing; pilot on synthetic then masked data with named reviewers; human tabletop.
5. **Days 61-90**: choose and evaluate a real model, then run the pre-registered portability protocol (IMP-Q01) with a second model; measure review time and approval rate; rerun the benefit model; go/no-go for a production pilot.
Roadmap detail: `docs/40-scale/90-day-roadmap.md` (sha256 `428ef07a427c9f801ff4ff0f194296f9051ac2e8d398f3cfff7eefad97038da5`). Nobody has committed to any of this.
