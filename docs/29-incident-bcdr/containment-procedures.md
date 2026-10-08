# Containment procedures

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | tests/test_resilience.py, drills |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Action | How | Effect | Reversible | Verified |
|---|---|---|---|---|
| Switch AI off | `AI_ENABLED=false`, restart | AI route 503; core up | yes | drill 2, tabletop |
| Force deterministic only | `AI_PROVIDER=deterministic` | no model calls | yes | tests |
| Cut one subject | rotate `AUTH_SECRET` (all tokens) or remove the persona rule | blanket, no per-token revocation | yes | design only |
| Stop data publication | do not run the ETL; previous load keeps serving | stale but consistent | yes | drill 4/5 |
| Lower AI rate | `AI_RATE_PER_MINUTE` | throttles | yes | tests |
| Take the service out | platform: stop routing on `/ready` | all traffic stops | yes | platform [UNK] |
| Block an origin | platform firewall/WAF | per source | yes | platform [UNK] |

Gaps: there is **no per-token revocation** and no per-user block; the only identity kill is rotating the shared secret (all users lose access). This is part of R-SEC-01 and is the strongest argument for an IdP.
