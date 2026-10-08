"""Correlation id propagation (FR-14, F-42)."""

from __future__ import annotations

import re
import uuid
from contextvars import ContextVar

HEADER = "X-Correlation-ID"
_VALID = re.compile(r"^[A-Za-z0-9._-]{8,64}$")
_current: ContextVar[str] = ContextVar("correlation_id", default="")


def new_id() -> str:
    return "corr-" + uuid.uuid4().hex[:16]


def accept_or_generate(header_value: str | None) -> str:
    if header_value and _VALID.fullmatch(header_value):
        return header_value
    return new_id()


def set_current(value: str) -> None:
    _current.set(value)


def current() -> str:
    return _current.get() or new_id()
