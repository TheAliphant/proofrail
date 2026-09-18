# Architecture

ProofRail separates evidence from execution. It does not decide which job to take, run an LLM, custody funds, or own a marketplace.

```text
job source -> worker agent -> artifact -> QA -> submission -> settlement
                 |             |       |        |            |
                 +-------------+-------+--------+------------+
                                      ProofRail receipt
```

The core produces and verifies deterministic JSON receipts. Adapters can attach independently verifiable evidence for a payment network, decentralized storage system, marketplace or attestation layer.

## Planned adapters
1. Base/x402 + USDC settlement evidence
2. Filecoin/IPFS archival of receipt bundles
3. Stellar escrow/settlement evidence
4. optional counterparty-risk attestations

Private source material is not required in a public receipt. Hashes and external references are sufficient for integrity checks.
