from __future__ import annotations

import argparse
import json
from pathlib import Path
from .receipt import sha256_file, verify_receipt
from .adapters.x402 import fetch_challenge, verify_challenge
from .adapters.evm import verify_evm_payment

def main() -> int:
    parser = argparse.ArgumentParser(prog="proofrail")
    sub = parser.add_subparsers(dest="cmd", required=True)
    h = sub.add_parser("hash"); h.add_argument("path")
    v = sub.add_parser("verify"); v.add_argument("receipt")
    x = sub.add_parser("x402-verify"); x.add_argument("url"); x.add_argument("--network"); x.add_argument("--asset"); x.add_argument("--pay-to"); x.add_argument("--amount")
    e = sub.add_parser("evm-verify"); e.add_argument("rpc_url"); e.add_argument("tx_hash"); e.add_argument("--chain-id", type=int, required=True); e.add_argument("--token", required=True); e.add_argument("--pay-to", required=True); e.add_argument("--amount", type=int, required=True)
    args = parser.parse_args()
    if args.cmd == "hash": print(sha256_file(args.path)); return 0
    if args.cmd == "verify":
        ok, errors = verify_receipt(json.loads(Path(args.receipt).read_text()))
        print(json.dumps({"verified":ok,"errors":errors},indent=2)); return 0 if ok else 1
    if args.cmd == "x402-verify":
        c=fetch_challenge(args.url); ok, errors=verify_challenge(c,network=args.network,asset=args.asset,pay_to=args.pay_to,amount=args.amount)
        print(json.dumps({"verified":ok,"errors":errors,"network":(c.get("requirement") or {}).get("network") or c.get("network")},indent=2)); return 0 if ok else 1
    ok, errors, evidence=verify_evm_payment(args.rpc_url,args.tx_hash,chain_id=args.chain_id,token=args.token,pay_to=args.pay_to,amount_base_units=args.amount)
    print(json.dumps({"verified":ok,"errors":errors,"evidence":evidence},indent=2)); return 0 if ok else 1

if __name__ == "__main__": raise SystemExit(main())
