"""Carrier booking saga (runbook J5; AC-27).

Closes the integration side of the retry storm and duplicate bookings seen in the data
(carrier_bookings.retry_count up to 4,995; three duplicate booking keys).

Guarantees (each one is a test in tests/test_carrier_saga.py):
- Idempotency: one booking per idempotency key. A repeated request returns the stored outcome and never calls the carrier again.
- Retry ceiling: at most `max_attempts` carrier calls per booking, never more than HARD_RETRY_CEILING (5, the BR rule ceiling).
  Only transient errors are retried, with capped exponential backoff and jitter. Permanent errors fail at once.
- Compensation: if the step after confirmation fails, the carrier booking is cancelled (also bounded). If cancel cannot be
  done the state is COMPENSATION_FAILED and the record is flagged for a person (`compensation_required`).
- Durability: every transition is an append-only JSONL record, so a restart does not forget a CONFIRMED booking.
The carrier itself is a port. No live carrier exists in this repository; `SimulatedCarrier` is for tests and the simulation.
"""

from __future__ import annotations

import hashlib
import json
import random
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

HARD_RETRY_CEILING = 5
PENDING, CONFIRMED, FAILED, COMPENSATED, COMPENSATION_FAILED = (
    "PENDING",
    "CONFIRMED",
    "FAILED",
    "COMPENSATED",
    "COMPENSATION_FAILED",
)
TERMINAL = {CONFIRMED, FAILED, COMPENSATED, COMPENSATION_FAILED}


class TransientCarrierError(Exception):
    """Timeout, 5xx, rate limit: worth retrying within the ceiling."""


class PermanentCarrierError(Exception):
    """Rejection that a retry cannot fix."""


class InFlightError(Exception):
    """The same idempotency key is being processed right now."""


class CarrierPort(Protocol):
    def book(self, shipment_id: str, carrier: str, idempotency_key: str) -> str: ...
    def cancel(self, partner_ref: str) -> None: ...


@dataclass
class BookingOutcome:
    key: str
    shipment_id: str
    carrier: str
    state: str
    partner_ref: str | None = None
    attempts: int = 0
    reason: str | None = None
    duplicate_suppressed: bool = False
    compensation_required: bool = False

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


def idempotency_key(shipment_id: str, carrier: str) -> str:
    return hashlib.sha256(f"{shipment_id}|{carrier}".encode()).hexdigest()[:32]


class BookingStore:
    """Append-only JSONL log folded to the latest record per key."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path
        self._lock = threading.RLock()
        self._state: dict[str, dict[str, Any]] = {}
        if path and path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    rec = json.loads(line)
                    self._state[rec["key"]] = rec

    @property
    def lock(self) -> threading.RLock:
        return self._lock

    def get(self, key: str) -> dict[str, Any] | None:
        with self._lock:
            rec = self._state.get(key)
            return dict(rec) if rec else None

    def put(self, rec: dict[str, Any]) -> None:
        with self._lock:
            self._state[rec["key"]] = dict(rec)
            if self.path:
                self.path.parent.mkdir(parents=True, exist_ok=True)
                with self.path.open("a", encoding="utf-8", newline="\n") as fh:
                    fh.write(json.dumps(rec, sort_keys=True) + "\n")


@dataclass
class SagaConfig:
    max_attempts: int = 3
    base_delay_s: float = 0.2
    max_delay_s: float = 5.0
    cancel_attempts: int = 3

    def validate(self) -> None:
        if not 1 <= self.max_attempts <= HARD_RETRY_CEILING:
            raise ValueError(f"max_attempts must be 1..{HARD_RETRY_CEILING} (retry ceiling), got {self.max_attempts}")
        if not 1 <= self.cancel_attempts <= HARD_RETRY_CEILING:
            raise ValueError(f"cancel_attempts must be 1..{HARD_RETRY_CEILING}, got {self.cancel_attempts}")


@dataclass
class CarrierSaga:
    carrier: CarrierPort
    store: BookingStore
    config: SagaConfig = field(default_factory=SagaConfig)
    sleep: Callable[[float], None] = time.sleep
    jitter: Callable[[], float] = random.random
    emit: Callable[[dict[str, Any]], None] = lambda _e: None

    def __post_init__(self) -> None:
        self.config.validate()

    def _delay(self, attempt: int) -> float:
        capped = float(min(self.config.max_delay_s, self.config.base_delay_s * (2 ** (attempt - 1))))
        return capped * (0.5 + 0.5 * self.jitter())  # equal jitter: never zero, never above the cap

    def _save(self, o: BookingOutcome) -> None:
        self.store.put(o.as_dict())
        self.emit(
            {"action": "carrier.booking", "state": o.state, "key": o.key, "shipment_id": o.shipment_id, "attempts": o.attempts}
        )

    def book(self, shipment_id: str, carrier: str, on_confirm: Callable[[BookingOutcome], None] | None = None) -> BookingOutcome:
        key = idempotency_key(shipment_id, carrier)
        with self.store.lock:
            prev = self.store.get(key)
            if prev:
                if prev["state"] == PENDING:
                    raise InFlightError(key)
                prev["duplicate_suppressed"] = True
                return BookingOutcome(**prev)
            out = BookingOutcome(key, shipment_id, carrier, PENDING)
            self._save(out)
        while out.attempts < self.config.max_attempts:
            out.attempts += 1
            try:
                out.partner_ref = self.carrier.book(shipment_id, carrier, key)
                out.state = CONFIRMED
                break
            except PermanentCarrierError as exc:
                out.state, out.reason = FAILED, f"permanent: {exc}"
                break
            except TransientCarrierError as exc:
                out.reason = f"transient: {exc}"
                if out.attempts < self.config.max_attempts:
                    self.sleep(self._delay(out.attempts))
        if out.state == PENDING:
            out.state, out.reason = FAILED, f"retry_ceiling_reached after {out.attempts} attempts ({out.reason})"
        if out.state == CONFIRMED and on_confirm is not None:
            try:
                on_confirm(out)
            except Exception as exc:  # any failure after the carrier confirmed must undo the carrier booking
                self._compensate(out, f"post-confirm step failed: {type(exc).__name__}")
        self._save(out)
        return out

    def _compensate(self, out: BookingOutcome, why: str) -> None:
        if not out.partner_ref:  # explicit check: an assert would be stripped under python -O (bandit B101)
            raise ValueError("compensation requires a partner reference")
        for i in range(1, self.config.cancel_attempts + 1):
            try:
                self.carrier.cancel(out.partner_ref)
                out.state, out.reason = COMPENSATED, why
                return
            except (TransientCarrierError, PermanentCarrierError):
                if i < self.config.cancel_attempts:
                    self.sleep(self._delay(i))
        out.state, out.reason, out.compensation_required = (
            COMPENSATION_FAILED,
            why + "; cancel failed, manual action required",
            True,
        )


class SimulatedCarrier:
    """Deterministic test double. `calls` counts every carrier call, `live` holds bookings that exist at the carrier."""

    def __init__(
        self,
        transient_failures: int = 0,
        permanent: bool = False,
        fail_cancel: int = 0,
        rng: random.Random | None = None,
        p_transient: float = 0.0,
    ) -> None:
        self.transient_failures, self.permanent, self.fail_cancel = transient_failures, permanent, fail_cancel
        self.p_transient, self.rng = p_transient, rng or random.Random(7)  # noqa: S311 (seeded test double, not security)
        self.calls = 0
        self.cancels = 0
        self.live: dict[str, str] = {}
        self._lock = threading.Lock()

    def book(self, shipment_id: str, carrier: str, idempotency_key: str) -> str:
        with self._lock:
            self.calls += 1
            if self.permanent:
                raise PermanentCarrierError("carrier rejected the request")
            if self.transient_failures > 0:
                self.transient_failures -= 1
                raise TransientCarrierError("carrier timeout")
            if self.p_transient and self.rng.random() < self.p_transient:
                raise TransientCarrierError("carrier 503")
            ref = "PRT-" + hashlib.sha256(f"{idempotency_key}{self.calls}".encode()).hexdigest()[:10]
            self.live[ref] = shipment_id
            return ref

    def cancel(self, partner_ref: str) -> None:
        with self._lock:
            self.cancels += 1
            if self.fail_cancel > 0:
                self.fail_cancel -= 1
                raise TransientCarrierError("cancel timeout")
            self.live.pop(partner_ref, None)
