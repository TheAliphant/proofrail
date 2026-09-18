from __future__ import annotations

import argparse
import json
from pathlib import Path
from .receipt import sha256_file, verify_receipt

def main() -> int:
    parser = argparse.ArgumentParser(prog="proofrail")
    sub = parser.add_subparsers(dest="cmd", required=True)
    h = sub.add_parser("hash"); h.add_argument("path")
    v = sub.add_parser("verify"); v.add_argument("receipt")
    args = parser.parse_args()
    if args.cmd == "hash":
        print(sha256_file(args.path)); return 0
    receipt = json.loads(Path(args.receipt).read_text())
    ok, errors = verify_receipt(receipt)
    print(json.dumps({"verified": ok, "errors": errors}, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
