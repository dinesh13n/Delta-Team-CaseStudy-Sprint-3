"""Human approval record for AI suggestions (FR-12, F-26). Append-only JSONL; one decision per suggestion."""

from __future__ import annotations

import json
import threading
import uuid
from pathlib import Path
from typing import Any

from apps.api.audit_chain import utc_now


class AlreadyDecidedError(Exception):
    pass


class ApprovalStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = threading.Lock()
        self._suggested: dict[str, dict[str, Any]] = {}
        self._decided: dict[str, dict[str, Any]] = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    self._apply(json.loads(line))

    def _apply(self, rec: dict[str, Any]) -> None:
        if rec["kind"] == "suggested":
            self._suggested[rec["summary_id"]] = rec
        elif rec["kind"] == "decision":
            self._decided[rec["summary_id"]] = rec

    def _write(self, rec: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, sort_keys=True) + "\n")
        self._apply(rec)

    def register(self, summary_id: str, shipment_id: str, requested_by: str, correlation_id: str) -> None:
        with self._lock:
            self._write(
                {
                    "kind": "suggested",
                    "summary_id": summary_id,
                    "shipment_id": shipment_id,
                    "requested_by": requested_by,
                    "correlation_id": correlation_id,
                    "ts": utc_now(),
                }
            )

    def known(self, summary_id: str) -> bool:
        return summary_id in self._suggested

    def decide(self, summary_id: str, decision: str, decided_by: str, reason: str | None) -> dict[str, Any]:
        with self._lock:
            if summary_id in self._decided:
                raise AlreadyDecidedError(summary_id)
            rec = {
                "kind": "decision",
                "approval_id": "apr-" + uuid.uuid4().hex[:16],
                "summary_id": summary_id,
                "decision": decision,
                "decided_by": decided_by,
                "decided_at": utc_now(),
                "reason": reason,
            }
            self._write(rec)
            return rec
