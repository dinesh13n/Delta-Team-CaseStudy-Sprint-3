# ADR 0001: Partial Modernization

Decision: Keep legacy batch jobs while introducing FastAPI services.

Status: SUPERSEDED by ADR-0002 (modular monolith with ports and adapters), 2026-10-08. See docs/10-architecture/adrs/ADR-0002 in the repository root and docs/14-transformation/coexistence-strategy.md.

Previous status: Accepted, but never revisited.

Consequence: Business rules and audit behavior now differ across code paths.

Supersession note (runbook step H12, F-53): the divergence this ADR created is managed, not deleted. The legacy audit writer, lookup function and reconcile script remain until their retirement triggers are met; the API no longer calls them.
