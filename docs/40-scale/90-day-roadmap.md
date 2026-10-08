# 90-day roadmap

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROPOSED |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Days | Goal | Exit evidence |
|---|---|---|
| 0 to 30 | Owners named; credentials revoked; platform and IdP chosen; first CI run on GitHub; image built and scanned | named RACI; revocation log; green CI; image digest |
| 31 to 60 | Deploy to a test environment; collector and alert routing; ETL scheduler; pilot with named reviewers on synthetic then masked data; first independent review | scrape of deployed instance; alert fired in a drill; reviewer report |
| 61 to 90 | Model chosen and evaluated (Stage Q pattern across vendors, not only within one); four-eyes and expiry; measured review time and approval rate; go/no-go for a production pilot | evaluation on that model; benefit model rerun with measured inputs |
Dependencies on people, not on the repository. Nothing here is committed to by anyone.
