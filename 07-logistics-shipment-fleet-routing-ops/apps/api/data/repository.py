"""DataRepository port and CSV adapter (ADR-0006, F-31, F-32).

Lookup is an exact match on the declared business key only. A miss returns None; it never falls back.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

import yaml

INTERNAL_COLUMNS = {"load_id", "source_row"}


@dataclass(frozen=True)
class EntityDef:
    name: str
    dataset: str
    key: str
    key_pattern: re.Pattern[str]
    types: dict[str, str]


class DataRepository(Protocol):
    def get(self, entity: str, key: str) -> dict[str, Any] | None: ...
    def list_page(self, entity: str, limit: int, offset: int, status: str | None = None) -> tuple[list[dict[str, Any]], int]: ...
    def events_for(self, shipment_id: str) -> list[dict[str, Any]]: ...
    def related(self, entity: str, field: str, value: str) -> list[dict[str, Any]]: ...
    def ready(self) -> dict[str, bool]: ...


def load_entities(semantic_dir: Path) -> dict[str, EntityDef]:
    ents = yaml.safe_load((semantic_dir / "entities.yaml").read_text(encoding="utf-8"))["entities"]
    rules = yaml.safe_load((semantic_dir / "business-rules.yaml").read_text(encoding="utf-8"))["rules"]
    pats = {r["entity"]: r["pattern"] for r in rules if r["id"].startswith("BR-P-")}
    out: dict[str, EntityDef] = {}
    for name, e in ents.items():
        out[name] = EntityDef(name, e["dataset"], e["business_key"], re.compile(pats.get(name, ".+")),
                              {f: d.get("type", "string") for f, d in e["fields"].items()})
    return out


def _convert(value: str, typ: str) -> Any:
    if typ in ("decimal", "integer"):
        try:
            return int(value) if typ == "integer" else float(value)
        except ValueError:
            return value
    if typ == "boolean":
        return {"true": True, "false": False}.get(value.lower(), value)
    return value


class CsvRepository:
    def __init__(self, data_dir: Path, layer: str, entities: dict[str, EntityDef]) -> None:
        self.entities = entities
        self.layer = layer
        self.dir = data_dir / ("curated" if layer == "curated" else "synthetic")
        self._cache: dict[str, tuple[float, list[dict[str, str]]]] = {}

    def _rows(self, entity: str) -> list[dict[str, str]]:
        path = self.dir / self.entities[entity].dataset
        mtime = path.stat().st_mtime
        hit = self._cache.get(entity)
        if hit and hit[0] == mtime:
            return hit[1]
        with path.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        self._cache[entity] = (mtime, rows)
        return rows

    def _shape(self, entity: str, row: dict[str, str]) -> dict[str, Any]:
        types = self.entities[entity].types
        out: dict[str, Any] = {k: _convert(v, types.get(k, "string")) for k, v in row.items()
                               if k not in INTERNAL_COLUMNS and k != "data_quality_flags"}
        flags = row.get("data_quality_flags", "")
        out["data_quality_flags"] = [f for f in flags.split(";") if f]
        return out

    def get(self, entity: str, key: str) -> dict[str, Any] | None:
        kf = self.entities[entity].key
        for row in self._rows(entity):
            if row.get(kf) == key:
                return self._shape(entity, row)
        return None

    def list_page(self, entity: str, limit: int, offset: int, status: str | None = None) -> tuple[list[dict[str, Any]], int]:
        rows = self._rows(entity)
        if status is not None:
            rows = [r for r in rows if r.get("status") == status]
        return [self._shape(entity, r) for r in rows[offset: offset + limit]], len(rows)

    def events_for(self, shipment_id: str) -> list[dict[str, Any]]:
        return [self._shape("tracking_events", r) for r in self._rows("tracking_events")
                if r.get("shipment_id") == shipment_id]

    def related(self, entity: str, field: str, value: str) -> list[dict[str, Any]]:
        return [self._shape(entity, r) for r in self._rows(entity) if r.get(field) == value]

    def ready(self) -> dict[str, bool]:
        return {f"{n}": (self.dir / e.dataset).is_file() for n, e in self.entities.items()}
