"""Resilience primitives (runbook M2; F-39): circuit breaker, call timeout, bulkhead.

They are small and dependency-free so they can wrap any outbound call (model provider today, carrier or IdP later).
A clock is injectable so state transitions are testable without sleeping.
"""

from __future__ import annotations

import threading
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeout
from typing import TypeVar

T = TypeVar("T")
CLOSED, OPEN, HALF_OPEN = "closed", "open", "half_open"


class CircuitOpenError(Exception):
    """The breaker is open: the call was not attempted."""


class CallTimeoutError(Exception):
    """The call did not finish within its time limit."""


class BulkheadFullError(Exception):
    """Too many concurrent calls to this dependency."""


class CircuitBreaker:
    """closed -> (N consecutive failures) -> open -> (after reset_after_s) -> half_open -> success: closed | failure: open."""

    def __init__(
        self, failure_threshold: int = 5, reset_after_s: float = 30.0, clock: Callable[[], float] = time.monotonic
    ) -> None:
        if failure_threshold < 1:
            raise ValueError("failure_threshold must be >= 1")
        self.failure_threshold, self.reset_after_s, self._clock = failure_threshold, reset_after_s, clock
        self._failures, self._opened_at, self._state = 0, 0.0, CLOSED
        self._probe_in_flight = False
        self._lock = threading.Lock()

    @property
    def state(self) -> str:
        with self._lock:
            return self._peek()

    def _peek(self) -> str:
        if self._state == OPEN and self._clock() - self._opened_at >= self.reset_after_s:
            self._state = HALF_OPEN
        return self._state

    def call(self, fn: Callable[[], T]) -> T:
        with self._lock:
            st = self._peek()
            if st == OPEN or (st == HALF_OPEN and self._probe_in_flight):
                raise CircuitOpenError(st)
            if st == HALF_OPEN:
                self._probe_in_flight = True  # exactly one probe call while half open
        try:
            result = fn()
        except Exception:
            with self._lock:
                self._probe_in_flight = False
                self._failures += 1
                if self._state == HALF_OPEN or self._failures >= self.failure_threshold:
                    self._state, self._opened_at = OPEN, self._clock()
            raise
        with self._lock:
            self._probe_in_flight = False
            self._failures, self._state = 0, CLOSED
        return result


_POOL = ThreadPoolExecutor(max_workers=8, thread_name_prefix="timeout-call")


def call_with_timeout(fn: Callable[[], T], timeout_s: float) -> T:
    """Run fn in a worker thread and stop waiting after timeout_s. The worker cannot be killed; it is abandoned (bounded pool)."""
    fut = _POOL.submit(fn)
    try:
        return fut.result(timeout=timeout_s)
    except FutureTimeout as exc:
        fut.cancel()
        raise CallTimeoutError(f"no answer within {timeout_s}s") from exc


class Bulkhead:
    def __init__(self, max_concurrent: int) -> None:
        self._sem = threading.BoundedSemaphore(max_concurrent)

    def call(self, fn: Callable[[], T]) -> T:
        if not self._sem.acquire(blocking=False):
            raise BulkheadFullError("concurrency limit reached")
        try:
            return fn()
        finally:
            self._sem.release()


def guarded(fn: Callable[[], T], breaker: CircuitBreaker | None, timeout_s: float | None) -> T:
    """Compose: breaker(timeout(fn)). Timeouts count as failures of the breaker."""
    inner: Callable[[], T] = (lambda: call_with_timeout(fn, timeout_s)) if timeout_s else fn
    return breaker.call(inner) if breaker else inner()
