"""ModelProvider port and adapters (ADR-0007). The deterministic provider is the default and the fallback."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from typing import Any, Protocol

EXCEPTION_STATUSES = {"exception", "failed", "manual_hold"}
IN_DOMAIN_OK = {"new", "queued", "in_progress", "closed"}
RETRY_CEILING = 5


class ProviderUnavailable(Exception):
    """The provider cannot answer (not configured, timeout, transport error)."""


@dataclass(frozen=True)
class PromptParts:
    system: str
    data_json: str

    def render(self) -> str:
        safe = self.data_json.replace("<", "\\u003c").replace(">", "\\u003e")
        return f"{self.system}\n<data>\n{safe}\n</data>"


@dataclass(frozen=True)
class ProviderResult:
    text: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None


class ModelProvider(Protocol):
    name: str
    version: str

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult: ...


class DeterministicProvider:
    """Rule-based summary built only from the allow-listed facts. No invented content."""

    name = "deterministic"
    version = "1.0"

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        ship = facts.get("shipment", {})
        status = ship.get("status")
        events = facts.get("events", [])
        bookings = facts.get("carrier_bookings", [])
        if not status or (status not in EXCEPTION_STATUSES and status not in IN_DOMAIN_OK):
            return ProviderResult(
                json.dumps(
                    {
                        "summary": None,
                        "recommendation": None,
                        "confidence": None,
                        "abstained": True,
                        "abstain_reason": "insufficient_context",
                    }
                )
            )
        counts = Counter(str(e.get("event_type")) for e in events)
        parts_txt = [
            f"Shipment {ship.get('shipment_id')} has status '{status}' (service tier "
            f"'{ship.get('service_tier')}', promised {ship.get('promised_at')})."
        ]
        if events:
            latest = max(events, key=lambda e: str(e.get("event_time")))
            parts_txt.append(
                f"{facts.get('event_total', len(events))} tracking events recorded "
                f"({', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))}); latest is "
                f"'{latest.get('event_type')}' at {latest.get('event_time')}."
            )
        else:
            parts_txt.append("No tracking events recorded.")
        retries = [b.get("retry_count") for b in bookings if isinstance(b.get("retry_count"), int | float)]
        if bookings:
            parts_txt.append(f"{len(bookings)} carrier booking(s); highest retry_count {max(retries) if retries else 'unknown'}.")
        exception_signal = status in EXCEPTION_STATUSES or counts.get("exception", 0) > 0
        if exception_signal:
            rec = (
                "Review the exception with the dispatcher, confirm the carrier booking and decide on "
                "re-booking or re-routing. Suggestion only; no action has been taken."
            )
        elif retries and max(retries) > RETRY_CEILING:
            rec = (
                f"Carrier retry count exceeds the ceiling of {RETRY_CEILING}; check the carrier booking "
                "before the next attempt. Suggestion only."
            )
        else:
            rec = "No exception signal found in the available data; no action suggested."
        return ProviderResult(
            json.dumps(
                {
                    "summary": " ".join(parts_txt)[:1200],
                    "recommendation": rec[:400],
                    "confidence": None,
                    "abstained": False,
                    "abstain_reason": None,
                }
            )
        )


class UnconfiguredModelProvider:
    """Stands in for a real vendor model (OQ-02 unresolved). Always raises, so the gateway falls back."""

    name = "model-unconfigured"
    version = "0"

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        raise ProviderUnavailable("no model provider is configured")
