"""Token verification port and adapters (ADR-0004, F-17). The role comes only from a verified token."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Protocol

import jwt

ALGORITHM = "HS256"
LEEWAY_SECONDS = 60


class TokenError(Exception):
    """Token missing, malformed, expired, or not verifiable."""


@dataclass(frozen=True)
class Claims:
    subject: str
    role: str
    tenant: str
    purpose: str | None = None


class TokenVerifier(Protocol):
    def verify(self, token: str) -> Claims: ...


class Hs256Verifier:
    def __init__(self, secret: str, leeway: int = LEEWAY_SECONDS) -> None:
        self._secret, self._leeway = secret, leeway

    def verify(self, token: str) -> Claims:
        try:
            p = jwt.decode(token, self._secret, algorithms=[ALGORITHM], leeway=self._leeway, options={"require": ["exp", "sub"]})
        except jwt.PyJWTError as exc:
            raise TokenError(type(exc).__name__) from exc
        role = p.get("role")
        if not isinstance(role, str) or not role:
            raise TokenError("MissingRole")
        return Claims(subject=str(p["sub"]), role=role, tenant=str(p.get("tenant", "default")), purpose=p.get("purpose"))


class JwksVerifier:
    """Placeholder for the identity-provider adapter (OQ-07 unresolved): always fails closed."""

    def verify(self, token: str) -> Claims:
        raise TokenError("JwksNotConfigured")


def issue_dev_token(
    secret: str,
    subject: str,
    role: str,
    tenant: str = "default",
    ttl: int = 3600,
    purpose: str | None = None,
    now: float | None = None,
) -> str:
    t = int(now if now is not None else time.time())
    payload: dict[str, object] = {"sub": subject, "role": role, "tenant": tenant, "iat": t, "exp": t + ttl}
    if purpose:
        payload["purpose"] = purpose
    return jwt.encode(payload, secret, algorithm=ALGORITHM)
