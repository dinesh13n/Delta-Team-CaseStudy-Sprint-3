"""Hash-chained, append-only audit sink (ADR-0008; F-43, F-44, F-45).

hash = SHA-256(canonical_json(event without hash) + prev_hash). Timestamps are timezone-aware UTC.
Tamper evidence only: the application can still append to or replace the file; an external append-only
store is deferred (Stage M) and recorded as PARTIAL for F-44.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import threading
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol

GENESIS = "0" * 64


def canonical(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chain_hash(body: dict[str, Any], prev_hash: str) -> str:
    return sha256_hex(canonical(body) + prev_hash)


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


class AuditSink(Protocol):
    def append(self, event: dict[str, Any]) -> dict[str, Any]: ...
    def verify(self) -> dict[str, Any]: ...


class JsonlAuditSink:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = threading.Lock()
        self._last = self._tail_hash()

    def _tail_hash(self) -> str:
        if not self.path.exists():
            return GENESIS
        last = GENESIS
        with self.path.open(encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    with contextlib.suppress(json.JSONDecodeError):
                        last = json.loads(line).get("hash", last)
        return last

    def append(self, event: dict[str, Any]) -> dict[str, Any]:
        with self._lock:
            body = dict(event)
            body.setdefault("event_id", "aud-" + uuid.uuid4().hex[:16])
            body.setdefault("ts", utc_now())
            body["prev_hash"] = self._last
            body["hash"] = chain_hash(body, self._last)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("a", encoding="utf-8") as fh:
                fh.write(canonical(body) + "\n")
                fh.flush()
                os.fsync(fh.fileno())
            self._last = body["hash"]
            return body

    def verify(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"valid": True, "records": 0, "first_bad_index": None}
        prev, n = GENESIS, 0
        with self.path.open(encoding="utf-8") as fh:
            for i, line in enumerate(fh):
                if not line.strip():
                    continue
                try:
                    rec = json.loads(line)
                    claimed = rec.pop("hash")
                except (json.JSONDecodeError, KeyError):
                    return {"valid": False, "records": n, "first_bad_index": i}
                if rec.get("prev_hash") != prev or chain_hash(rec, prev) != claimed:
                    return {"valid": False, "records": n, "first_bad_index": i}
                prev, n = claimed, n + 1
        return {"valid": True, "records": n, "first_bad_index": None}


def build_event(
    *,
    action: str,
    subject: str,
    role: str,
    correlation_id: str,
    tenant: str,
    resource_type: str,
    resource_id: str,
    decision: str,
    rule: str,
    decision_id: str | None,
    outcome: str,
    auth_method: str = "jwt",
    model: dict[str, Any] | None = None,
    input_hash: str | None = None,
    approval_id: str | None = None,
    retention_class: str = "operational",
    detail: dict[str, Any] | None = None,
) -> dict[str, Any]:
    pd: dict[str, Any] = {"decision": decision, "rule": rule}
    if decision_id:
        pd["decision_id"] = decision_id
    ev: dict[str, Any] = {
        "action": action,
        "actor": {"subject": subject, "role": role, "auth_method": auth_method},
        "correlation_id": correlation_id,
        "tenant": tenant,
        "resource": {"type": resource_type, "id": resource_id},
        "policy_decision": pd,
        "model": model,
        "input_hash": input_hash,
        "approval_id": approval_id,
        "outcome": outcome,
        "retention_class": retention_class,
    }
    if detail:
        ev["detail"] = detail
    return ev
