"""LEGACY audit writer (v1). Superseded by apps.api.audit_chain (H8, F-43..F-45); not called by the API any more.

Kept for one release so old audit.log files remain interpretable; retire per docs/14-transformation/coexistence-strategy.md.
"""

import json
from datetime import datetime
from pathlib import Path

LOG = Path(__file__).resolve().parents[3] / "logs" / "audit.log"


def write_event(action, details):
    LOG.parent.mkdir(exist_ok=True)
    event = {"ts": datetime.utcnow().isoformat(), "action": action, "details": details}
    # Brownfield issue: no actor identity, no request correlation id, no retention classification.
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
