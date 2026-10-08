# Lessons learned (including failures)

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | decision-log D-007..D-014; stage gates |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | What went wrong | How found | Lesson |
|---|---|---|---|
| 1 | Runbook F-42 "corrected" from 66.4% to 32.8% (null-only count), then restored | Stage H8 re-profile by value class (null, empty, present) | a one-pattern grep is not an independent count (D-007 → D-012) |
| 2 | CI had never run; first run failed at the coverage gate (51% vs 80%) | first real GitHub run | a gate not executed in its real environment is not evidence (D-013) |
| 3 | 58 of 107 evidence files had no manifest row | hash verification at R2 | register evidence when produced; late registration proves only "unchanged since R2" |
| 4 | First red-team baseline invalid (stale poison key) | L3 review | check the attack can fire before counting a failed attack |
| 5 | Doc claimed "12 of 12" baseline attacks | recount | 10 of 12; RT-08 not applicable to baseline |
| 6 | Import from a Windows working tree marked 876 files executable | baseline diff at R | normalise modes (D-014) |
| 7 | Container recipe defect found only when exercised from a clean copy (P2) | operator exercise | write runbooks, then run them cold |
| 8 | AI incident playbook named the wrong counter | N review | align docs with metrics at the end of run |
| 9 | Builder graded own work throughout | by design of a single-agent run | independent review is a gate, not a courtesy |
| 10 | Second model never run | OQ-02 unresolved | pre-register the protocol so the later run cannot be shaped by results |

Trade-offs accepted: platform-neutral over platform-specific; HS256 over a stub IdP; deterministic provider over a model; thin operations view over an Angular portal that never existed.
