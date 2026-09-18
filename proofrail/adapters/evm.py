from __future__ import annotations

import json
from typing import Any
from urllib.request import Request, urlopen

TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"

def rpc_call(rpc_url: str, method: str, params: list[Any], timeout: float = 10.0) -> Any:
    payload = json.dumps({"jsonrpc":"2.0","id":1,"method":method,"params":params}).encode()
    req = Request(rpc_url, data=payload, headers={"Content-Type":"application/json","User-Agent":"ProofRail/0.2"})
    with urlopen(req, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8"))
    if data.get("error"): raise RuntimeError(data["error"])
    return data.get("result")

def fetch_transaction_receipt(rpc_url: str, tx_hash: str) -> dict[str, Any] | None:
    return rpc_call(rpc_url, "eth_getTransactionReceipt", [tx_hash])

def fetch_chain_id(rpc_url: str) -> int:
    return int(rpc_call(rpc_url, "eth_chainId", []), 16)

def _topic_address(topic: str) -> str:
    return "0x" + topic.lower().removeprefix("0x")[-40:]

def verify_erc20_transfer(receipt: dict[str, Any] | None, *, token: str, pay_to: str,
                          amount_base_units: int) -> tuple[bool, list[str], dict[str, Any] | None]:
    if not receipt: return False, ["transaction_not_found"], None
    errors: list[str] = []
    if receipt.get("status") != "0x1": errors.append("transaction_failed")
    token_l = token.lower(); pay_l = pay_to.lower()
    match = None
    for log in receipt.get("logs", []):
        topics = log.get("topics") or []
        if str(log.get("address", "")).lower() != token_l or len(topics) < 3: continue
        if str(topics[0]).lower() != TRANSFER_TOPIC: continue
        try:
            to_addr = _topic_address(topics[2])
            value = int(log.get("data", "0x0"), 16)
        except (TypeError, ValueError):
            continue
        if to_addr == pay_l and value == int(amount_base_units):
            match = {"token": token, "pay_to": pay_to, "amount_base_units": value, "log_index": log.get("logIndex")}
            break
    if match is None: errors.append("matching_transfer_not_found")
    return not errors, errors, match

def verify_evm_payment(rpc_url: str, tx_hash: str, *, chain_id: int, token: str,
                       pay_to: str, amount_base_units: int) -> tuple[bool, list[str], dict[str, Any]]:
    errors: list[str] = []
    actual_chain = fetch_chain_id(rpc_url)
    if actual_chain != int(chain_id): errors.append("chain_id_mismatch")
    receipt = fetch_transaction_receipt(rpc_url, tx_hash)
    ok, transfer_errors, match = verify_erc20_transfer(receipt, token=token, pay_to=pay_to, amount_base_units=amount_base_units)
    errors.extend(transfer_errors)
    evidence = {"chain_id": actual_chain, "tx_hash": tx_hash, "block_number": receipt.get("blockNumber") if receipt else None, "transfer": match}
    return not errors and ok, errors, evidence
