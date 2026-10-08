# ruff: noqa: E501
"""Backup and restore verification (runbook N3). Creates a backup of the state the service owns, restores it to a fresh location,
and proves the restored copy is the same by hash, by audit-chain verification and by answering the same requests.

    python -m scripts.backup_restore --out ../evidence/30-release/EVD-N-03-backup-restore.json

State covered: data/curated, data/quarantine, data/reports (the published layers), the audit log and the approval store.
Not covered: secrets (never in a backup), the source CSVs (they live in version control), anything on a platform that does not exist.
Measured on one machine with a 354-row-per-entity fixture: the timings say nothing about a production volume.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tarfile
import tempfile
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from fastapi.testclient import TestClient

import etl.run_daily_batch as batch
from apps.api.audit_chain import JsonlAuditSink
from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.main import create_app
from apps.api.security.tokens import issue_dev_token

SECRET = "backup-restore-secret-" + "x" * 40  # secret-scan: allow (throw-away value for an in-process run)
LAYERS = ("curated", "quarantine", "reports")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def hdr(role: str, sub: str) -> dict[str, str]:
    return {"Authorization": "Bearer " + issue_dev_token(SECRET, sub, role, ttl=3600)}


def inventory(data: Path, audit: Path, approvals: Path) -> dict[str, str]:
    inv: dict[str, str] = {}
    for layer in LAYERS:
        for p in sorted(x for x in (data / layer).rglob("*") if x.is_file()):
            inv[f"data/{p.relative_to(data).as_posix()}"] = sha(p)
    inv["audit.log"] = sha(audit)
    inv["approvals.jsonl"] = sha(approvals)
    return inv


def backup(data: Path, audit: Path, approvals: Path, dest: Path) -> dict[str, Any]:
    inv = inventory(data, audit, approvals)
    tip = JsonlAuditSink(audit).verify()
    with tarfile.open(dest, "w:gz") as tf:
        for layer in LAYERS:
            tf.add(data / layer, arcname=f"data/{layer}")
        tf.add(audit, arcname="audit.log")
        tf.add(approvals, arcname="approvals.jsonl")
        meta = json.dumps({"files": inv, "audit_records": tip["records"]}, indent=1, sort_keys=True).encode()
        info = tarfile.TarInfo("BACKUP-MANIFEST.json")
        info.size = len(meta)
        import io

        tf.addfile(info, io.BytesIO(meta))
    return {"files": len(inv), "bytes": dest.stat().st_size, "archive_sha256": sha(dest), "audit_records": tip["records"]}


def restore(archive: Path, target: Path) -> dict[str, Any]:
    with tarfile.open(archive, "r:gz") as tf:
        tf.extractall(target, filter="data")
    manifest: dict[str, Any] = json.loads((target / "BACKUP-MANIFEST.json").read_text(encoding="utf-8"))
    return manifest


def settings(data: Path, audit: Path, approvals: Path) -> Settings:
    return Settings(
        app_env="local",
        auth_mode="hs256",
        auth_secret=SECRET,
        data_dir=data,
        audit_path=audit,
        approvals_path=approvals,
        semantic_dir=_semantic_dir(),
        ai_rate_per_minute=1000,
    )


def snapshot(c: TestClient) -> dict[str, Any]:
    d = hdr("dispatcher", "alice")
    r1 = c.get("/records/SHI-00027", headers=d)
    r2 = c.get("/shipments?limit=10", headers=d)
    r3 = c.get("/audit/verify", headers=hdr("auditor", "aud"))
    return {
        "record": hashlib.sha256(r1.content).hexdigest(),
        "list": hashlib.sha256(r2.content).hexdigest(),
        "data_load_id": r1.headers.get("X-Data-Load-Id"),
        "audit_verify": r3.json(),
        "ready": c.get("/ready").status_code,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        data = tmp / "live" / "data"
        shutil.copytree(ROOT / "data" / "synthetic", data / "synthetic")
        batch.run(data, data, _semantic_dir(), 0.05, False)
        audit, appr = tmp / "live" / "audit.log", tmp / "live" / "approvals.jsonl"
        c = TestClient(create_app(settings(data, audit, appr)))
        s = c.post("/ai/summarize/SHI-00027", headers=hdr("dispatcher", "alice")).json()
        c.post(
            f"/ai/summaries/{s['summary_id']}/decision",
            headers=hdr("dispatcher", "alice"),
            json={"decision": "approve", "reason": "n3 backup test"},
        )
        c.get("/records/SHI-00002", headers=hdr("clinician", "mallory"))
        before = snapshot(c)

        # --- backup
        t0 = time.perf_counter()
        arc = tmp / "backup.tar.gz"
        b = backup(data, audit, appr, arc)
        backup_s = time.perf_counter() - t0

        # --- disaster: the live state is gone
        shutil.rmtree(tmp / "live")

        # --- restore to a fresh location and bring a new instance up on it
        t1 = time.perf_counter()
        rt = tmp / "restored"
        rt.mkdir()
        man = restore(arc, rt)
        restored_inv = inventory(rt / "data", rt / "audit.log", rt / "approvals.jsonl")  # before the new instance writes anything
        c2 = TestClient(create_app(settings(rt / "data", rt / "audit.log", rt / "approvals.jsonl")))
        after = snapshot(c2)
        restore_s = time.perf_counter() - t1
        hash_mismatch = [k for k in man["files"] if restored_inv.get(k) != man["files"][k]]
        # the restored audit must still extend: a new event after the restore chains onto the old tip
        c2.get("/records/SHI-00003", headers=hdr("dispatcher", "alice"))
        extended = JsonlAuditSink(rt / "audit.log").verify()

        # --- negative test: a corrupted backup must be detected, not served
        bad = tmp / "bad"
        bad.mkdir()
        restore(arc, bad)
        lines = (bad / "audit.log").read_text(encoding="utf-8").splitlines()
        rec = json.loads(lines[0])
        rec["actor"]["subject"] = "forged"
        lines[0] = json.dumps(rec)
        (bad / "audit.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
        bad_hash = [
            k
            for k in man["files"]
            if inventory(bad / "data", bad / "audit.log", bad / "approvals.jsonl").get(k) != man["files"][k]
        ]
        bad_chain = JsonlAuditSink(bad / "audit.log").verify()

        checks = {
            "all_file_hashes_match": not hash_mismatch,
            "same_record_response": before["record"] == after["record"],
            "same_list_response": before["list"] == after["list"],
            "same_data_load_id": before["data_load_id"] == after["data_load_id"],
            "audit_chain_valid_after_restore": bool(after["audit_verify"].get("valid")),
            "audit_record_count_preserved": after["audit_verify"].get("records", -1) >= before["audit_verify"].get("records", 0),
            "audit_extends_after_restore": bool(extended["valid"]),
            "ready_after_restore": after["ready"] == 200,
            "corrupted_backup_detected_by_hash": bool(bad_hash),
            "corrupted_backup_detected_by_chain": not bad_chain["valid"],
        }
        out = {
            "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "scope": "published data layers, audit log, approval store; one process; fixture volume",
            "backup": {**b, "seconds": round(backup_s, 3)},
            "restore": {
                "seconds_to_serving": round(restore_s, 3),
                "files_restored": len(man["files"]),
                "hash_mismatches": hash_mismatch,
            },
            "before": before,
            "after": after,
            "checks": checks,
            "all_ok": all(checks.values()),
            "not_proven": [
                "restore on a platform, from remote storage, or by a person other than the author",
                "backup encryption, retention and offsite copy (no storage exists; OQ-01)",
                "RTO/RPO at production volume: timings are for a 354-row fixture",
                "restore of secrets or identity configuration (excluded by design)",
                "point-in-time recovery: only whole-state snapshots exist, so the RPO is the interval between snapshots, which is undefined until a schedule exists",
            ],
        }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(checks, indent=1), f"backup {backup_s:.2f}s restore-to-serving {restore_s:.2f}s")
    return 0 if out["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
