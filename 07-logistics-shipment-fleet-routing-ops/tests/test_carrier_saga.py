"""AC-27 / J-X6: carrier saga: duplicate suppression, retry ceiling, compensation, durability."""

import threading
from pathlib import Path

import pytest

from apps.api.integration.carrier_saga import (
    COMPENSATED,
    COMPENSATION_FAILED,
    CONFIRMED,
    FAILED,
    HARD_RETRY_CEILING,
    BookingStore,
    CarrierSaga,
    InFlightError,
    SagaConfig,
    SimulatedCarrier,
    idempotency_key,
)


def _saga(carrier: SimulatedCarrier, store: BookingStore | None = None, **cfg: float) -> tuple[CarrierSaga, list[float]]:
    slept: list[float] = []
    saga = CarrierSaga(
        carrier,
        store or BookingStore(),
        SagaConfig(**cfg),
        sleep=slept.append,
        jitter=lambda: 1.0,  # type: ignore[arg-type]
    )
    return saga, slept


def test_happy_path_books_once() -> None:
    c = SimulatedCarrier()
    saga, _ = _saga(c)
    o = saga.book("SHI-00001", "CarrierX")
    assert o.state == CONFIRMED and o.attempts == 1 and o.partner_ref in c.live


def test_duplicate_request_never_calls_the_carrier_again() -> None:
    c = SimulatedCarrier()
    saga, _ = _saga(c)
    first = saga.book("SHI-00001", "CarrierX")
    second = saga.book("SHI-00001", "CarrierX")
    assert c.calls == 1 and len(c.live) == 1
    assert second.duplicate_suppressed and second.partner_ref == first.partner_ref


def test_same_shipment_other_carrier_is_a_different_booking() -> None:
    c = SimulatedCarrier()
    saga, _ = _saga(c)
    saga.book("SHI-00001", "CarrierX")
    saga.book("SHI-00001", "CarrierY")
    assert c.calls == 2


def test_concurrent_duplicates_create_exactly_one_booking() -> None:
    c = SimulatedCarrier()
    saga, _ = _saga(c)
    results: list[object] = []

    def work() -> None:
        try:
            results.append(saga.book("SHI-00002", "CarrierX"))
        except InFlightError as exc:
            results.append(exc)

    threads = [threading.Thread(target=work) for _ in range(20)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    assert c.calls == 1 and len(c.live) == 1


def test_transient_failures_are_retried_with_growing_backoff() -> None:
    c = SimulatedCarrier(transient_failures=2)
    saga, slept = _saga(c, max_attempts=4, base_delay_s=0.1, max_delay_s=10)
    o = saga.book("SHI-00003", "CarrierX")
    assert o.state == CONFIRMED and o.attempts == 3 and c.calls == 3
    assert slept == [0.1, 0.2]  # jitter fixed at 1.0 -> full delay; doubles each attempt


def test_retry_ceiling_stops_the_storm() -> None:
    c = SimulatedCarrier(transient_failures=10_000)
    saga, slept = _saga(c, max_attempts=3)
    o = saga.book("SHI-00004", "CarrierX")
    assert o.state == FAILED and o.attempts == 3 and c.calls == 3 and "retry_ceiling" in (o.reason or "")
    assert len(slept) == 2  # no sleep after the last attempt
    again = saga.book("SHI-00004", "CarrierX")  # a failed booking is not retried by a repeat request
    assert again.duplicate_suppressed and c.calls == 3


@pytest.mark.parametrize("bad", [0, HARD_RETRY_CEILING + 1, 4995])
def test_configured_ceiling_cannot_exceed_the_hard_ceiling(bad: int) -> None:
    with pytest.raises(ValueError):
        CarrierSaga(SimulatedCarrier(), BookingStore(), SagaConfig(max_attempts=bad))


def test_permanent_error_fails_immediately_without_retry() -> None:
    c = SimulatedCarrier(permanent=True)
    saga, slept = _saga(c, max_attempts=5)
    o = saga.book("SHI-00005", "CarrierX")
    assert o.state == FAILED and o.attempts == 1 and c.calls == 1 and not slept


def test_failure_after_confirmation_compensates() -> None:
    c = SimulatedCarrier()
    saga, _ = _saga(c)

    def boom(_o: object) -> None:
        raise RuntimeError("ledger down")

    o = saga.book("SHI-00006", "CarrierX", on_confirm=boom)
    assert o.state == COMPENSATED and c.cancels == 1 and not c.live


def test_failed_compensation_is_flagged_for_a_person() -> None:
    c = SimulatedCarrier(fail_cancel=99)
    saga, _ = _saga(c, cancel_attempts=2)

    def boom(_o: object) -> None:
        raise RuntimeError("ledger down")

    o = saga.book("SHI-00007", "CarrierX", on_confirm=boom)
    assert o.state == COMPENSATION_FAILED and o.compensation_required and c.cancels == 2


def test_state_survives_a_restart(tmp_path: Path) -> None:
    path = tmp_path / "bookings.jsonl"
    c = SimulatedCarrier()
    saga, _ = _saga(c, BookingStore(path))
    saga.book("SHI-00008", "CarrierX")
    c2 = SimulatedCarrier()
    saga2, _ = _saga(c2, BookingStore(path))  # new process, same log
    o = saga2.book("SHI-00008", "CarrierX")
    assert o.duplicate_suppressed and c2.calls == 0


def test_every_transition_is_emitted() -> None:
    events: list[dict[str, object]] = []
    saga = CarrierSaga(SimulatedCarrier(), BookingStore(), emit=events.append)
    saga.book("SHI-00009", "CarrierX")
    assert [e["state"] for e in events] == ["PENDING", "CONFIRMED"]


def test_idempotency_key_is_stable() -> None:
    assert idempotency_key("SHI-1", "A") == idempotency_key("SHI-1", "A") != idempotency_key("SHI-1", "B")
