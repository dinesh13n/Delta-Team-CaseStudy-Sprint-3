# ruff: noqa: E501
"""Observability validation (runbook N1). Two phases because the PromQL parser lives in a different interpreter than the app.

    python -m scripts.validate_observability workload --out /tmp/obs-workload.json     # app interpreter: drives every path, records /metrics
    python -m scripts.validate_observability check --workload /tmp/obs-workload.json --out evidence/31-observability/EVD-N-01-observability-validation.json

check: parses alerts/dashboards, validates PromQL syntax (promql-parser), and verifies every referenced metric, label and
literal label value against what the running service actually exported. A reference to a metric the service never emits is a FAIL.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SECRET = "obs-validation-secret-" + "x" * 40  # secret-scan: allow (throw-away value for an in-process run)
FAMILY_SUFFIX = ("_bucket", "_count", "_sum")


def _parse_exposition(text: str) -> dict[str, dict[str, set[str]]]:
    fam: dict[str, dict[str, set[str]]] = {}
    for ln in text.splitlines():
        m = re.match(r"^([a-zA-Z_:][a-zA-Z0-9_:]*)(\{(.*)\})? ", ln)
        if not m:
            continue
        labels = dict(re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)="([^"]*)"', m.group(3) or ""))
        f = fam.setdefault(m.group(1), {})
        for k, v in labels.items():
            f.setdefault(k, set()).add(v)
        f.setdefault("__series__", set()).add("1")
    return fam


def workload(out: Path) -> int:
    import json as _json

    from fastapi.testclient import TestClient

    import etl.run_daily_batch as batch
    from apps.api.ai.providers import PromptParts, ProviderResult
    from apps.api.config import Settings, _semantic_dir
    from apps.api.main import create_app
    from apps.api.security.tokens import issue_dev_token

    class Leaky:
        name, version = "leaky", "1"

        def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
            return ProviderResult(
                _json.dumps(
                    {"summary": "Call customer CUS-00027 back.", "recommendation": "x", "confidence": 0.9, "abstained": False}
                )
            )

    class Garbage:
        name, version = "garbage", "1"

        def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
            return ProviderResult("not json at all")

    class Down:
        name, version = "down", "1"

        def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
            raise RuntimeError("503 upstream unavailable")

    def hdr(role: str, sub: str) -> dict[str, str]:
        return {"Authorization": "Bearer " + issue_dev_token(SECRET, sub, role, ttl=3600)}

    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        data = tmp / "data"
        shutil.copytree(ROOT / "data" / "synthetic", data / "synthetic")
        batch.run(data, data, _semantic_dir(), 0.05, False)
        st = Settings(
            app_env="local",
            auth_mode="hs256",
            auth_secret=SECRET,
            data_dir=data,
            audit_path=tmp / "audit.log",
            approvals_path=tmp / "approvals.jsonl",
            semantic_dir=_semantic_dir(),
            ai_rate_per_minute=6,
        )
        app = create_app(st)
        c = TestClient(app)
        gw = app.state.svc.gateway
        paths: list[tuple[str, str]] = []

        def hit(name: str, r: Any) -> None:
            paths.append((name, str(r.status_code)))

        d = hdr("dispatcher", "alice")
        hit("ok record", c.get("/records/SHI-00027", headers=d))
        hit("ok list", c.get("/shipments?limit=5", headers=d))
        hit("not found", c.get("/records/NOPE", headers=d))
        hit("auth denied: no token", c.get("/records/SHI-00027"))
        hit("auth denied: bad token", c.get("/records/SHI-00027", headers={"Authorization": "Bearer abc.def.ghi"}))
        hit("policy denied", c.get("/records/SHI-00002", headers=hdr("clinician", "mallory")))
        r = c.post("/ai/summarize/SHI-00027", headers=d)
        hit("ai deterministic", r)
        sid = r.json()["summary_id"]
        hit(
            "human decision",
            c.post(f"/ai/summaries/{sid}/decision", headers=d, json={"decision": "reject", "reason": "validation"}),
        )
        gw.provider = Garbage()
        hit("ai schema violation", c.post("/ai/summarize/SHI-00027", headers=d))
        gw.provider = Leaky()
        hit("ai output leak", c.post("/ai/summarize/SHI-00027", headers=d))
        gw.provider = Down()
        for _ in range(2):
            hit("ai provider down", c.post("/ai/summarize/SHI-00027", headers=d))
        for _ in range(3):
            hit("ai rate limited (limit 6/min)", c.post("/ai/summarize/SHI-00027", headers=d))
        m = c.get("/metrics", headers=hdr("ops", "oncall"))
        hit("metrics scrape", m)
        out.write_text(
            json.dumps(
                {"run_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "paths": paths, "metrics_text": m.text}, indent=2
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        for p in paths:
            print(*p)
    return 0


SELECTOR = re.compile(r"\b([a-zA-Z_:][a-zA-Z0-9_:]*)\s*(\{([^}]*)\})?")
KEYWORDS = {
    "sum",
    "rate",
    "increase",
    "histogram_quantile",
    "by",
    "without",
    "absent",
    "avg",
    "max",
    "min",
    "count",
    "le",
    "on",
    "ignoring",
    "and",
    "or",
    "unless",
    "bool",
    "irate",
    "label_replace",
}


def exprs_from_alerts(path: Path) -> list[tuple[str, str]]:
    import yaml

    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [(r["alert"], r["expr"]) for g in doc["groups"] for r in g["rules"]]


def exprs_from_dashboards(d: Path) -> list[tuple[str, str]]:
    out = []
    for f in sorted(d.glob("*.json")):
        j = json.loads(f.read_text(encoding="utf-8"))
        out += [(f"{f.stem}/{p['title']}", t["expr"]) for p in j["panels"] for t in p["targets"]]
    return out


def refs(expr: str) -> tuple[set[str], list[tuple[str, str, str, str]], set[str]]:
    """metric names, (metric,label,op,value) matchers, labels used in by()/without()."""
    scrub = re.sub(r'"[^"]*"', '""', expr)
    scrub = re.sub(r"\[[^\]]*\]", "", scrub)
    by = {x.strip() for g in re.findall(r"\b(?:by|without)\s*\(([^)]*)\)", scrub) for x in g.split(",") if x.strip()}
    scrub_nobylabels = re.sub(r"\b(?:by|without)\s*\([^)]*\)", "", scrub)
    names = {
        m.group(1)
        for m in SELECTOR.finditer(scrub_nobylabels)
        if m.group(1) not in KEYWORDS and not re.fullmatch(r"\d+(\.\d+)?", m.group(1))
    }
    matchers = []
    for m in SELECTOR.finditer(re.sub(r"\[[^\]]*\]", "", expr)):
        if m.group(3) and m.group(1) not in KEYWORDS:
            for lab, op, val in re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*(=~|!~|!=|=)\s*"([^"]*)"', m.group(3)):
                matchers.append((m.group(1), lab, op, val))
    return names, matchers, by


def check(workload_path: Path, out: Path) -> int:
    try:
        import promql_parser
    except ImportError:
        promql_parser = None
    w = json.loads(workload_path.read_text(encoding="utf-8"))
    fam = _parse_exposition(w["metrics_text"])
    base = {f[: -len(s)] if f.endswith(s) else f for f in fam for s in FAMILY_SUFFIX if f.endswith(s)}
    known = set(fam) | base
    rows: list[dict[str, Any]] = []
    for source, items in (
        ("alert", exprs_from_alerts(ROOT / "observability/alerts/alerts.yaml")),
        ("dashboard", exprs_from_dashboards(ROOT / "observability/dashboards")),
    ):
        for name, expr in items:
            problems: list[str] = []
            notes: list[str] = []
            if promql_parser is None:
                problems.append("promql-parser not installed: syntax NOT checked")
            else:
                try:
                    promql_parser.parse(expr)
                except ValueError as exc:
                    problems.append(f"PromQL syntax: {exc}")
            names, matchers, by = refs(expr)
            for n in sorted(names):
                if n not in known:
                    problems.append(f"metric '{n}' is not exported by the service")
            for metric, lab, op, val in matchers:
                labelset = fam.get(metric) or fam.get(metric + "_bucket") or {}
                if metric in known and lab not in labelset:
                    problems.append(f"{metric} has no label '{lab}'")
                elif op == "=" and metric in known and val not in labelset.get(lab, set()):
                    notes.append(f'{metric}{{{lab}="{val}"}} not produced by this workload')
                elif op == "=~" and metric in known and not any(re.fullmatch(val, v) for v in labelset.get(lab, set())):
                    notes.append(f'{metric}{{{lab}=~"{val}"}} matched no series in this workload')
            for lab in sorted(by - {"le"}):
                if not any(lab in (fam.get(n) or fam.get(n + "_bucket") or {}) for n in names if n in known):
                    problems.append(f"grouping label '{lab}' exists on none of the metrics used")
            rows.append(
                {
                    "source": source,
                    "name": name,
                    "expr": expr,
                    "metrics": sorted(names),
                    "problems": problems,
                    "notes": notes,
                    "ok": not problems,
                }
            )
    failed = [r for r in rows if not r["ok"]]
    unexercised = sorted({n for r in rows for n in r["notes"]})
    required = [
        "http_requests_total",
        "http_request_duration_seconds",
        "auth_denied_total",
        "policy_denied_total",
        "ai_requests_total",
        "ai_fallback_total",
        "ai_guardrail_blocked_total",
        "ai_decisions_total",
        "ai_tokens_total",
        "ai_request_duration_seconds",
        "audit_chain_valid",
        "data_load_age_seconds",
        "ai_circuit_open",
    ]
    missing_families = [m for m in required if m not in known]
    res = {
        "validated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "workload_run_utc": w["run_utc"],
        "workload_paths": w["paths"],
        "promql_syntax_checked": promql_parser is not None,
        "families_exported": sorted(known),
        "required_families_missing": missing_families,
        "rules_checked": len(rows),
        "rules_failed": len(failed),
        "label_values_not_exercised": unexercised,
        "rows": rows,
        "limits": [
            "Syntax and reference checks only: no Prometheus or Grafana instance evaluated these rules, so no alert has been seen to FIRE or to route.",
            "Thresholds are proposed starting values, not tuned on production traffic.",
            "Exposition has no # HELP / # TYPE lines (hand-rolled renderer); a real Prometheus accepts this but typed tooling will not know counters from gauges.",
        ],
        "all_ok": not failed and not missing_families and promql_parser is not None,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        f"rules={len(rows)} failed={len(failed)} missing_families={missing_families} syntax_checked={promql_parser is not None}"
    )
    for r in failed:
        print("FAIL", r["name"], r["problems"])
    for n in unexercised:
        print("note", n)
    return 0 if res["all_ok"] else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("workload")
    a.add_argument("--out", type=Path, required=True)
    b = sub.add_parser("check")
    b.add_argument("--workload", type=Path, required=True)
    b.add_argument("--out", type=Path, required=True)
    n = ap.parse_args()
    return workload(n.out) if n.cmd == "workload" else check(n.workload, n.out)


if __name__ == "__main__":
    sys.exit(main())
