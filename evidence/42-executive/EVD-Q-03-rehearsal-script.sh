#!/usr/bin/env bash
# EVD-Q-03 producer. Author-run rehearsal of the demo beats that can run offline. No audience, no recording of a person.
R=/home/claude/delta-team-casestudy-sprint-3; APP=$R/07-logistics-shipment-fleet-routing-ops; PY=/tmp/v311/bin/python
T0=$(date +%s); beat(){ echo; echo "=== BEAT $1 | t+$(( $(date +%s)-T0 ))s | $2"; }
echo "# Q3 demo rehearsal | $(date -u +%FT%TZ) | author-run (one person), no audience"
beat 1 "Quick-start on the as-delivered baseline fails (C2), then succeeds on v2 (H2)"
( cd /tmp/c2work && . .venv/bin/activate && pip uninstall -q -y httpx pytest-cov >/dev/null 2>&1; pytest -q 2>&1 | tail -3; echo "[baseline pytest exit: ${PIPESTATUS[0]}]" )
( cd $APP && $PY -m pytest -q -p no:cacheprovider 2>&1 | tail -2 ; echo "[v2 pytest exit: ${PIPESTATUS[0]}]" )
beat 2 "Red team: 12 attacks, baseline vs v2 (stored campaign, L3)"
$PY - <<PYEOF
import json
for l in ("baseline","v2"):
    d=json.load(open("$R/evidence/26-tevv/EVD-L-03-redteam-%s.json"%l)); print(l, d["summary"], d["run_utc"])
PYEOF
beat 3 "End-to-end reconstruction (N2), run again now"
( cd $APP && $PY -m scripts.reconstruction_evidence --out /tmp/q3-recon.json 2>&1 | tail -6; echo "[exit ${PIPESTATUS[0]}]" )
beat 4 "AI-disabled / timeout degraded mode drills (M3), run again now"
( cd $APP && $PY -m scripts.failure_drills --out-dir /tmp/q3-drills 2>&1 | tail -8; echo "[exit ${PIPESTATUS[0]}]" )
beat 5 "Model comparison (Q2): NOT PERFORMED, see model-comparison.md"
beat 6 "Cost per outcome (N4): formula and unknowns, see cost-per-outcome.md"
echo; echo "TOTAL elapsed: $(( $(date +%s)-T0 )) s"
