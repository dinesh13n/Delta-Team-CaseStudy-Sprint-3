"""Row-level validation driven by semantic-layer rules (FR-06; F-33..F-38, F-40, F-58..F-62).

Rule semantics mirror semantic-layer/tests/rule_eval.py (the oracle) so violation counts can be compared one to
one; this module additionally returns WHICH rows violate so they can be quarantined.
"""

from __future__ import annotations

import collections
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# ETL-level severity overrides (assumption [ASM], owner UNRESOLVED, OQ-05): BR-04 is declared severity "block" but
# every fixture row violates it (the timezone column holds categorical noise, F-37). Quarantining 100% of
# tracking_events would make the dataset unusable, so it is flagged until the Data Owner confirms the domain.
SEVERITY_OVERRIDE = {"BR-04": "flag"}
SKIP_TYPES = {"field_exposure", "freshness", "forbid_unless"}


@dataclass
class RowVerdict:
    rules_block: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)


def _blank(v: Any) -> bool:
    return v is None or str(v).strip() == ""


def load_semantics(semantic_dir: Path) -> dict[str, Any]:
    def y(name: str) -> Any:
        return yaml.safe_load((semantic_dir / name).read_text(encoding="utf-8"))

    return {
        "entities": y("entities.yaml")["entities"],
        "rules": y("business-rules.yaml")["rules"],
        "relationships": y("relationships.yaml")["relationships"],
        "enums": y("status-taxonomy.yaml")["enums"],
    }


def violating_rows(rule: dict[str, Any], rows: list[dict[str, str]], data: dict[str, list[dict[str, str]]]) -> set[int]:
    """Indexes of rows offending the rule, with the same counting as the oracle (all rows of a duplicate group)."""
    t = rule["type"]
    if rule.get("data_gap") or t in SKIP_TYPES:
        return set()
    if t == "unique":
        groups: dict[tuple[Any, ...], list[int]] = collections.defaultdict(list)
        for i, r in enumerate(rows):
            groups[tuple(r.get(f) for f in rule["fields"])].append(i)
        return {i for g in groups.values() if len(g) > 1 for i in g}
    if t == "pattern":
        p = re.compile(rule["pattern"])
        return {i for i, r in enumerate(rows) if not p.fullmatch(r.get(rule["field"]) or "")}
    if t == "range":
        out = set()
        for i, r in enumerate(rows):
            try:
                v = float(r[rule["field"]])
            except (ValueError, KeyError):
                continue
            if v < rule["min"] or v > rule["max"]:
                out.add(i)
        return out
    if t == "not_blank":
        return {i for i, r in enumerate(rows) if any(_blank(r.get(f)) for f in rule["fields"])}
    if t == "timestamp_after":
        return {i for i, r in enumerate(rows) if r.get(rule["field"]) and r[rule["field"]] <= rule["after"]}
    if t == "reference_exists":
        te, tf = rule["to"].split(".")
        keys = {r[tf] for r in data.get(te, [])}
        return {i for i, r in enumerate(rows) if r.get(rule["field"]) not in keys}
    if t == "at_most_one_active":
        seen: set[str] = set()
        out = set()
        for i, r in enumerate(rows):
            g = r.get(rule["group_by"])
            if r.get("status") in rule["inactive_statuses"] or not g:
                continue
            if g in seen:
                out.add(i)
            seen.add(g)
        return out
    if t == "enum_or_reference":
        p = re.compile(r"[A-Za-z_]+/[A-Za-z_]+")
        return {i for i, r in enumerate(rows) if not p.fullmatch(r.get(rule["field"]) or "")}
    raise ValueError("unsupported rule type " + t)


def later_duplicates(rule: dict[str, Any], rows: list[dict[str, str]]) -> set[int]:
    """For unique rules the first occurrence is kept; only later occurrences are quarantined."""
    first: dict[tuple[Any, ...], int] = {}
    out = set()
    for i, r in enumerate(rows):
        k = tuple(r.get(f) for f in rule["fields"])
        if k in first:
            out.add(i)
        else:
            first[k] = i
    return out


def evaluate_entity(
    entity: str, rows: list[dict[str, str]], data: dict[str, list[dict[str, str]]], sem: dict[str, Any]
) -> tuple[list[RowVerdict], dict[str, int], dict[str, int]]:
    """Returns verdict per row, per-rule offending-row counts (oracle-comparable), and per-flag counts."""
    verdicts = [RowVerdict() for _ in rows]
    counts: dict[str, int] = {}
    for rule in sem["rules"]:
        if rule["entity"] != entity:
            continue
        sev = SEVERITY_OVERRIDE.get(rule["id"], rule.get("severity", "flag"))
        bad = violating_rows(rule, rows, data)
        if rule.get("data_gap") or rule["type"] in SKIP_TYPES:
            continue
        counts[rule["id"]] = len(bad)
        target = later_duplicates(rule, rows) if rule["type"] == "unique" else bad
        for i in target:
            if sev == "block":
                verdicts[i].rules_block.append(rule["id"])
            else:
                verdicts[i].flags.append(f"rule:{rule['id']}")
    for rel in sem["relationships"]:
        fe, ff = rel["from"].split(".")
        te_tf = rel["to"]
        if fe != entity or "(" in te_tf or rel.get("on_missing") != "quarantine":
            continue
        te, tf = te_tf.split(".")
        keys = {r[tf] for r in data.get(te, [])}
        bad = {i for i, r in enumerate(rows) if r.get(ff) not in keys}
        counts[rel["id"]] = len(bad)
        for i in bad:
            if rel["id"] not in verdicts[i].rules_block and not _covered_by_br12(entity, ff):
                verdicts[i].rules_block.append(rel["id"])
    flag_counts: collections.Counter[str] = collections.Counter()
    fields = sem["entities"][entity]["fields"]
    for i, r in enumerate(rows):
        for fname, fdef in fields.items():
            dom = fdef.get("domain")
            v = r.get(fname)
            if dom and dom in sem["enums"] and not _blank(v) and v not in [str(x) for x in sem["enums"][dom]["values"]]:
                verdicts[i].flags.append(f"enum_violation:{fname}")
        if entity == "shipments":
            try:
                if float(r["actual_weight_kg"]) > float(r["declared_weight_kg"]):
                    verdicts[i].flags.append("actual_gt_declared")
            except (ValueError, KeyError):
                pass
    for verdict in verdicts:
        verdict.flags = sorted(set(verdict.flags))
        flag_counts.update(verdict.flags)
    return verdicts, counts, dict(flag_counts)


def _covered_by_br12(entity: str, field_name: str) -> bool:
    # BR-12 already quarantines carrier_bookings.shipment_id orphans; avoid a duplicate reason for the same defect.
    return entity == "carrier_bookings" and field_name == "shipment_id"
