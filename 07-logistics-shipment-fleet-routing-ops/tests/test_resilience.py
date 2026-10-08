"""M2 / M-X3 / M-X4: timeouts, circuit breaker, bulkhead, AI-disabled mode, graceful degradation."""

import threading
import time
from typing import Any

import pytest
from fastapi.testclient import TestClient

from apps.api.ai.gateway import AiGateway
from apps.api.ai.providers import PromptParts, ProviderResult
from apps.api.config import Settings
from apps.api.main import create_app
from apps.api.resilience import (
    CLOSED,
    HALF_OPEN,
    OPEN,
    Bulkhead,
    BulkheadFullError,
    CallTimeoutError,
    CircuitBreaker,
    CircuitOpenError,
    call_with_timeout,
)
from evaluation.run_eval import MemRepo
from tests.conftest import auth


class Clock:
    def __init__(self) -> None:
        self.t = 0.0

    def __call__(self) -> float:
        return self.t


def _boom() -> None:
    raise RuntimeError("down")


def test_breaker_opens_after_threshold_and_rejects_without_calling() -> None:
    clk, calls = Clock(), []
    b = CircuitBreaker(3, 30, clk)
    for _ in range(3):
        with pytest.raises(RuntimeError):
            b.call(lambda: (calls.append(1), _boom())[1])
    assert b.state == OPEN
    with pytest.raises(CircuitOpenError):
        b.call(lambda: calls.append(1))
    assert len(calls) == 3  # the open breaker did not call the dependency


def test_breaker_half_open_probe_then_close_or_reopen() -> None:
    clk = Clock()
    b = CircuitBreaker(1, 10, clk)
    with pytest.raises(RuntimeError):
        b.call(_boom)
    clk.t = 11
    assert b.state == HALF_OPEN
    assert b.call(lambda: "ok") == "ok" and b.state == CLOSED
    with pytest.raises(RuntimeError):
        b.call(_boom)
    clk.t = 30
    with pytest.raises(RuntimeError):  # failing probe re-opens immediately
        b.call(_boom)
    assert b.state == OPEN


def test_success_resets_failure_count() -> None:
    b = CircuitBreaker(3, 30, Clock())
    for _ in range(2):
        with pytest.raises(RuntimeError):
            b.call(_boom)
    b.call(lambda: 1)
    for _ in range(2):
        with pytest.raises(RuntimeError):
            b.call(_boom)
    assert b.state == CLOSED


def test_timeout_stops_waiting() -> None:
    t0 = time.perf_counter()
    with pytest.raises(CallTimeoutError):
        call_with_timeout(lambda: time.sleep(1.0), 0.05)
    assert time.perf_counter() - t0 < 0.6


def test_bulkhead_limits_concurrency() -> None:
    bh = Bulkhead(1)
    gate, started = threading.Event(), threading.Event()

    def hold() -> None:
        started.set()
        gate.wait(2)

    t = threading.Thread(target=lambda: bh.call(hold))
    t.start()
    started.wait(2)
    with pytest.raises(BulkheadFullError):
        bh.call(lambda: 1)
    gate.set()
    t.join()
    assert bh.call(lambda: 2) == 2


class _Slow:
    name, version = "slow", "1"

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        time.sleep(1.0)
        return ProviderResult("{}")


class _Down:
    name, version = "down", "1"

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        raise RuntimeError("503")


def _case() -> dict[str, Any]:
    return {
        "shipment": {"shipment_id": "SHI-90001", "status": "exception", "service_tier": "express", "customer_id": "CUS-1"},
        "events": [],
        "bookings": [],
    }


def _gw(provider: Any, **kw: Any) -> AiGateway:
    from apps.api.config import _semantic_dir
    from apps.api.data.repository import load_entities
    from apps.api.security.policy import PolicyEngine

    sem = _semantic_dir()
    return AiGateway(MemRepo(_case(), load_entities(sem)), PolicyEngine.from_dir(sem).ai_policy, provider, **kw)


def test_slow_model_times_out_and_falls_back() -> None:
    out = _gw(_Slow(), timeout_s=0.05).summarize("SHI-90001", "corr-test-0001").output
    assert out["generated_by"] == "fallback" and out["fallback_reason"] == "provider_timeout"


def test_repeated_model_failure_opens_the_breaker_and_stops_calling_it() -> None:
    calls = []

    class Counting(_Down):
        def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
            calls.append(1)
            raise RuntimeError("503")

    gw = _gw(Counting(), breaker=CircuitBreaker(3, 60, Clock()))
    reasons = [gw.summarize("SHI-90001", "corr-test-0001").output["fallback_reason"] for _ in range(6)]
    assert reasons[:3] == ["provider_error"] * 3 and reasons[3:] == ["circuit_open"] * 3
    assert len(calls) == 3  # no retry storm against a failing dependency


def test_ai_disabled_mode_keeps_the_core_workflow(settings: Settings) -> None:
    c = TestClient(create_app(Settings(**{**settings.__dict__, "ai_enabled": False})))
    h = auth("dispatcher")
    assert c.post("/ai/summarize/SHI-00027", headers=h).status_code == 503
    assert c.get("/records/SHI-00027", headers=h).status_code == 200
    assert c.get("/shipments", headers=h).status_code == 200
    assert c.get("/shipments/SHI-00027/events", headers=h).status_code == 200
    assert c.get("/ready").status_code == 200


def test_model_provider_unconfigured_still_serves_a_summary(settings: Settings) -> None:
    c = TestClient(create_app(Settings(**{**settings.__dict__, "ai_provider": "model"})))
    r = c.post("/ai/summarize/SHI-00027", headers=auth("dispatcher"))
    assert r.status_code == 200 and r.json()["generated_by"] == "fallback"
    assert r.json()["fallback_reason"] == "provider_unavailable"
