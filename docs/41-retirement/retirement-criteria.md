# Retirement criteria

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (criteria defined) |
| Evidence sources | docs/14-transformation/coexistence-strategy.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Asset | Retire when | Not before |
|---|---|---|
| Legacy lookup (`LOOKUP_MODE=legacy`) | one release without regression after H10 acceptance | owner acceptance |
| Legacy audit writer shims (`services/audit.py`, `domain_service.py`) | after FF-02 sunset; v1 files remain readable | archive of v1 logs |
| Deterministic provider | never while it is the fallback | n/a |
| A model | replaced and evaluated successor exists; or vendor/policy trigger; or sustained drift | successor evaluated, kill switch tested |
| A prompt version | superseded and out of the rollback window | audit references remain resolvable (keep file in git) |
| API route | no callers for a set period (audit shows) and a deprecation notice | consumer sign-off |
| `legacy/reconcile_legacy.py` | owner decision on carrier saga scope | owner |
| Infrastructure | service retired | data exported/archived, keys revoked |
| Vendor | exit plan executed | data returned/deleted, contract ended |
| The whole service | sponsor decision | retention, legal hold, key revocation, evidence archive |
