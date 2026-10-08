"""Policy engine driven by semantic-layer/access-semantics.yaml (ADR-0005, F-18, F-19, F-21).

Deny by default. Decision inputs: persona (role), entity, action, purpose.
Scope (own hub, assigned only ...) is reported in the decision but NOT enforced: the data model has no
hub, fleet or customer attribute to enforce it with (declared gap, scope_enforced=false).
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

LEVEL = {"none": 0, "read": 1, "write": 2}
WIDE_SCOPES = {"all", "all active", "request-scoped"}
MASK = "***"


@dataclass(frozen=True)
class Decision:
    allow: bool
    rule: str
    reason: str
    persona: str
    entity: str
    action: str
    purpose: str | None
    scope: str | None = None
    scope_enforced: bool = True
    decision_id: str = field(default_factory=lambda: "pd-" + uuid.uuid4().hex[:12])


class PolicyEngine:
    def __init__(self, access: dict[str, Any], ai_policy: dict[str, Any] | None = None) -> None:
        self.personas: dict[str, dict[str, Any]] = access["personas"]
        self.sensitive: set[str] = set(access.get("sensitive_fields", []))
        self.ai_policy = ai_policy or {}

    @classmethod
    def from_dir(cls, semantic_dir: Path) -> PolicyEngine:
        access = yaml.safe_load((semantic_dir / "access-semantics.yaml").read_text(encoding="utf-8"))
        ai = yaml.safe_load((semantic_dir / "ai-context-policy.yaml").read_text(encoding="utf-8"))
        return cls(access, ai)

    def decide(self, persona: str, entity: str, action: str = "read", purpose: str | None = None) -> Decision:
        def deny(reason: str, rule: str = "default-deny") -> Decision:
            return Decision(False, rule, reason, persona, entity, action, purpose)

        if action not in ("read", "write"):
            return deny("unknown action")
        ent = self.personas.get(persona, {}).get(entity)
        if ent is None:
            return deny("persona or entity not declared")
        rule = f"access:{persona}.{entity}"
        if LEVEL.get(ent.get("access", "none"), 0) < LEVEL[action]:
            return Decision(False, rule, "access level too low", persona, entity, action, purpose)
        purposes = ent.get("purposes") or []
        chosen = purpose or (purposes[0] if purposes else None)
        if chosen not in purposes:
            return Decision(False, rule, "purpose not allowed", persona, entity, action, chosen)
        scope = ent.get("scope")
        return Decision(True, rule, "allowed", persona, entity, action, chosen, scope, scope in WIDE_SCOPES)

    def field_action(self, persona: str, entity: str, fld: str) -> str:
        """allow | mask | deny for one field. Sensitive fields are masked unless explicitly allowed."""
        overrides = (self.personas.get(persona, {}).get(entity, {}) or {}).get("field_overrides") or {}
        if fld in overrides:
            return str(overrides[fld])
        return "mask" if f"{entity}.{fld}" in self.sensitive else "allow"

    def filter_row(self, persona: str, entity: str, row: dict[str, Any]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for k, v in row.items():
            a = self.field_action(persona, entity, k)
            if a == "deny":
                continue
            out[k] = MASK if a == "mask" and v not in (None, "") else v
        return out

    def matrix(self) -> dict[str, dict[str, dict[str, Any]]]:
        """Machine-readable matrix, used to generate and test the Rego policy."""
        return {
            p: {e: {"access": x.get("access", "none"), "purposes": list(x.get("purposes") or [])} for e, x in ents.items()}
            for p, ents in self.personas.items()
        }
