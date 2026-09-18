# ProofRail

**Verifiable work and payment receipts for autonomous agents.**

ProofRail is an open protocol and tiny reference SDK for turning autonomous work into a portable, tamper-evident receipt: job → artifact → QA → submission → payment.

## Why
AI agents can increasingly discover work, produce artifacts and transact. What is still fragmented is the evidence trail. Buyers, marketplaces and worker agents need a neutral way to answer: *what was requested, what was delivered, did QA pass, and was payment actually settled?*

## Status
Public MVP v0.2. The chain-agnostic receipt core, x402 challenge validation and Base/EVM settlement verification are implemented and tested. A Filecoin Open Grant proposal is under review, and the Stellar track targets the active SCF x402 Facilitator + Bazaar RFP.

- Live docs: https://thealiphant.github.io/proofrail/
- Filecoin Open Grant #2194: https://github.com/filecoin-project/devgrants/issues/2194

## Quick start
```bash
python -m unittest discover -s tests -v
python -m proofrail.cli hash README.md
python -m proofrail.cli verify examples/receipt.json
```

## Design principles
- portable JSON receipts, deterministic canonicalization
- artifact and task hashes instead of private content
- explicit QA and settlement state
- chain/provider adapters stay outside the core
- no private keys, custody or hidden signing fallback
- verification should be possible without trusting the worker agent

See [docs/architecture.md](docs/architecture.md) and [docs/receipt-spec.md](docs/receipt-spec.md).

## License
MIT OR Apache-2.0. See `LICENSE-MIT` and `LICENSE-APACHE`.
