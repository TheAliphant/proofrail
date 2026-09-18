from __future__ import annotations

import json
from typing import Any
from urllib.request import Request, urlopen


def fetch_challenge(url: str, timeout: float = 10.0) -> dict[str, Any]:
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "ProofRail/0.1"})
    with urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))

def verify_challenge(challenge: dict[str, Any], *, network: str | None = None,
                     asset: str | None = None, pay_to: str | None = None,
                     amount: str | None = None) -> tuple[bool, list[str]]:
    errors: list[str] = []
    requirement = challenge.get("requirement") or {}
    if challenge.get("scheme") != "exact": errors.append("unsupported_scheme")
    actual_network = requirement.get("network") or challenge.get("network")
    if not actual_network: errors.append("missing_network")
    if not requirement.get("asset"): errors.append("missing_asset")
    if not requirement.get("payTo"): errors.append("missing_pay_to")
    if not requirement.get("amount"): errors.append("missing_amount")
    if network and actual_network != network: errors.append("network_mismatch")
    if asset and str(requirement.get("asset", "")).lower() != asset.lower(): errors.append("asset_mismatch")
    if pay_to and str(requirement.get("payTo", "")).lower() != pay_to.lower(): errors.append("pay_to_mismatch")
    if amount and str(requirement.get("amount")) != str(amount): errors.append("amount_mismatch")
    return not errors, errors
