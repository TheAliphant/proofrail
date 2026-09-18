from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RECEIPT_VERSION = "proofrail/0.1"

def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()

def sha256_file(path: str | Path) -> str:
    with open(path, "rb") as handle:
        return sha256_bytes(handle.read())

def create_receipt(*, job_id: str, worker: str, artifact_hash: str, qa_status: str,
                   provider: str | None = None, buyer: str | None = None,
                   task_hash: str | None = None, submission_ref: str | None = None,
                   payment: dict[str, Any] | None = None, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    payload = {
        "version": RECEIPT_VERSION, "job_id": job_id, "worker": worker,
        "provider": provider, "buyer": buyer, "task_hash": task_hash,
        "artifact_hash": artifact_hash, "qa_status": qa_status,
        "submission_ref": submission_ref, "payment": payment,
        "metadata": metadata or {},
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    payload["receipt_hash"] = sha256_bytes(canonical_json(payload))
    return payload

def verify_receipt(receipt: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    expected = receipt.get("receipt_hash")
    unsigned = {k: v for k, v in receipt.items() if k != "receipt_hash"}
    actual = sha256_bytes(canonical_json(unsigned))
    if expected != actual: errors.append("receipt_hash_mismatch")
    if receipt.get("version") != RECEIPT_VERSION: errors.append("unsupported_version")
    if not receipt.get("job_id"): errors.append("missing_job_id")
    if not receipt.get("worker"): errors.append("missing_worker")
    if not receipt.get("artifact_hash"): errors.append("missing_artifact_hash")
    if receipt.get("qa_status") not in {"PASS", "FAIL", "UNKNOWN"}: errors.append("invalid_qa_status")
    return not errors, errors
