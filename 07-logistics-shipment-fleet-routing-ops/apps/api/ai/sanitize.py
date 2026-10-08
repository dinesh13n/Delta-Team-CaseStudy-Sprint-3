"""Input sanitisation and injection signals for untrusted text (F-22, F-23). Values are data, never instructions."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml

MAX_VALUE_CHARS = 200
_INJECTION = re.compile(
    r"(ignore|disregard|forget)\s+(all\s+|any\s+|the\s+)?(previous|prior|above|earlier)\s+(instructions?|rules?|prompts?)"
    r"|system\s+prompt|you\s+are\s+now|reveal\s+(the\s+)?(prompt|secret|key)|developer\s+mode",
    re.IGNORECASE,
)
_TEMPLATE = re.compile(r"[{}$]|<\s*/?\s*data\s*>", re.IGNORECASE)
REDACTED = "[redacted: instruction-like text]"


UNRECOGNISED = "[unrecognised]"
# entity -> field -> enum name in semantic-layer/status-taxonomy.yaml. These values are echoed into summaries, so they must be
# members of the declared vocabulary; anything else is untrusted text and is never repeated (J3/L3 finding DEF-L-01).
ENUM_FIELDS: dict[str, dict[str, str]] = {
    "shipments": {"status": "shipment_status", "service_tier": "service_tier"},
    "tracking_events": {"event_type": "tracking_event_type", "source_system": "source_system"},
}


def load_enums(semantic_dir: Path) -> dict[str, set[str]]:
    doc = yaml.safe_load((semantic_dir / "status-taxonomy.yaml").read_text(encoding="utf-8"))["enums"]
    return {name: {str(v) for v in spec["values"]} for name, spec in doc.items()}


def clean_text(value: str, signals: list[str]) -> str:
    value = unicodedata.normalize("NFKC", value)
    # format characters (zero-width joiners etc.) are removed, not replaced, so split keywords re-join before matching
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Cf")
    s = "".join(" " if unicodedata.category(ch).startswith("C") else ch for ch in value)
    s = re.sub(r"\s+", " ", s).strip()[:MAX_VALUE_CHARS]
    if _TEMPLATE.search(s):
        signals.append("template_syntax")
        s = _TEMPLATE.sub("", s)
    if _INJECTION.search(s):
        signals.append("injection_marker")
        return REDACTED
    return s


def clean_value(value: Any, signals: list[str]) -> Any:
    return clean_text(value, signals) if isinstance(value, str) else value


def clean_enum(value: Any, allowed: set[str] | None, signals: list[str]) -> Any:
    """Echo an enumerated field only if it is in the declared vocabulary."""
    if value is None or value == "" or allowed is None:
        return clean_value(value, signals)
    if str(value) in allowed:
        return value
    signals.append("enum_violation")
    return UNRECOGNISED
