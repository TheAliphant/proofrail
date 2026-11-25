# ProofRail

[![Powered by RustChain](https://img.shields.io/badge/Powered%20by-RustChain-orange)](https://rustchain.org)

[![test](https://github.com/TheAliphant/proofrail/actions/workflows/test.yml/badge.svg)](https://github.com/TheAliphant/proofrail/actions/workflows/test.yml)

**Verifiable work and payment receipts for autonomous agents.**

ProofRail is an open protocol and tiny reference SDK for turning autonomous work into a portable, tamper-evident receipt: job → artifact → QA → submission → payment.

## Why
AI agents can increasingly discover work, produce artifacts and transact. What is still fragmented is the evidence trail. Buyers, marketplaces and worker agents need a neutral way to answer: *what was requested, what was delivered, did QA pass, and was payment actually settled?*

## Status
Public MVP v0.2. The chain-agnostic receipt core, x402 challenge validation and Base/EVM settlement verification are implemented and tested. The [Filecoin Open Grant proposal #2194](https://github.com/filecoin-project/devgrants/issues/2194) was closed on 18 November 2026 without a confirmed award; the sponsor redirected funding requests to ProPGF. The [Filecoin R&D program](https://www.filpgf.io/rnd/) announced new RFPs on 20 November, including a potentially relevant agent delegation and receipt track (RFP 3). This is a potential opportunity, not an approved project or a claim of existing UCAN/Filecoin Pay support. The [SCF #46 submission window](https://communityfund.stellar.org/awards/recxrSMYwAl8vcglg) closed on 9 November 2026; no Stellar funding award is claimed.

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
