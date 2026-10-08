# EVD-H-05: record lookup behaviour change (before / after)

Producing step: H5. Source: `~/fde/probe.py` against tag baseline/v0.1-as-delivered-bytes (py3.11) and the transformed app (py3.14). UTC 2026-10-08. Operator: Dinesh (agent-run).

| Request | Before | After |
|---|---|---|
| GET /records/SHI-00002 | 200, row SHI-00002 | 200 (token), customer_id masked |
| GET /records/DOES-NOT-EXIST | 200, row REC-0001 (first row) | 422 identifier pattern; token required |
| GET /records/REC-0001 | 200, REC-0001 (planted bad key) | 422 (key is not `SHI-[0-9]{5}`) |
| GET /records/CUS-00002 | 200, SHI-00002 found by a non-key column | 422 |
| Well-formed missing id (tests) | n/a | 404 |

Raw rows: evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv
