# Dependency Map

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

```
main.py -> domain_service -> data/synthetic/shipments.csv
        -> ai_gateway (stdlib only)
        -> audit -> logs/audit.log
etl/run_daily_batch.py -> shipments.csv
legacy/reconcile_legacy.py -> shipments.csv
scripts/sanity_check.py -> manifest.json, all CSVs, events.jsonl, doc paths
tests -> fastapi.testclient (httpx, undeclared) -> main.py; domain_service
```
External packages: fastapi, uvicorn, pydantic (unused directly), pytest, python-dotenv (unused), PyYAML (unused). [VF imports grep]
