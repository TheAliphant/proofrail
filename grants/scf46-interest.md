# SCF #46 Interest Package — ProofRail / Stellar x402 Bazaar

## Track
**SCF Build — RFP Track**

## Active RFP
**X402 Facilitator with Bazaar (discovery) support**

## One-line
Build a production-ready, permissively licensed Stellar x402 facilitator and native Bazaar so autonomous agents can discover, price and pay for HTTP and MCP services on Stellar without pre-baked integrations.

## Why this team / existing proof
ProofRail is already public and working: deterministic economic-work receipts, SHA-256 tamper detection, CLI verification, x402 exact-payment challenge validation, and EVM/Base ERC-20 settlement verification. Separately, the private autonomous labour runtime already operates against real machine-executable work providers and a live Base USDC/x402 receive route. The grant project would not expose the private commercial routing engine; it would build the open Stellar infrastructure requested by the RFP.

## RFP implementation plan
We will build on `@x402/stellar`, not reimplement Stellar settlement primitives. The funded scope is:

1. **Facilitator** — `/verify`, `/settle`, `/supported`; strict Soroban auth-entry validation; exact scheme; SEP-41 tokens with USDC default; sponsored fees; self-hostable + hosted paths.
2. **Stellar Bazaar** — `/discovery/resources`, natural-language `/discovery/search`, automatic cataloging from discovery extension payloads, HTTP + MCP resource types, route-template/integrity validation, `EXTENSION-RESPONSES`.
3. **Agent MCP interface** — deterministic search and paid-call tools wrapping discover → authorize → pay → retry, with machine-readable errors.
4. **`upto` scheme** — author Stellar network spec, implement it, test it, and coordinate upstream contribution with the x402 project.
5. **Conformance + operations** — canonical-client E2E on testnet and pubnet, published settlement hashes, 99% availability target, monitoring, runbook, security-review remediation and role-based developer docs.

## Architecture
```mermaid
graph LR
  A[Agent / canonical x402 client] --> B[MCP discovery tools]
  B --> C[Stellar Bazaar]
  C --> D[Paid HTTP or MCP resource]
  D -->|402 terms| A
  A -->|signed auth entry| E[Stellar x402 facilitator]
  E --> F[@x402/stellar]
  F --> G[Stellar testnet / pubnet]
  E -->|settlement evidence| H[ProofRail receipt]
```

The Bazaar index remains off-chain by default. Payment settlement stays non-custodial. ProofRail receipts are additive evidence, not a replacement for x402 wire-level conformance.

## Proposed award size
**$90,000 in XLM** over the standard SCF 7.0 10/20/30/40 payment structure.

- **Tranche 0 — $9,000 (10%)**: award acceptance, detailed threat model, conformance matrix, implementation plan and upstream coordination.
- **Tranche 1 — $18,000 (20%) MVP**: exact facilitator on Stellar testnet; `/verify`, `/settle`, `/supported`; fee sponsorship; self-host path; first canonical-client E2E.
- **Tranche 2 — $27,000 (30%) Testnet**: full Bazaar resources/search/automatic cataloging; HTTP + MCP; agent-facing MCP server; `upto` spec + implementation candidate; conformance suite and public testnet service.
- **Tranche 3 — $36,000 (40%) Mainnet**: pubnet facilitator/Bazaar; upstream `upto` contribution; two E2E integrations; security-review remediation; role-based docs; public monitoring/runbook; published transaction hashes and canonical conformance report.

Audit fees themselves are not included; we will use the SCF Audit Bank path specified by the RFP if accepted.

## Success evidence
- unmodified canonical client completes payments on Stellar testnet and pubnet
- exact and `upto` conformance tests pass
- public settled transaction hash per network and scheme
- `/supported` advertises required Stellar extras including fee sponsorship
- Bazaar indexes HTTP and MCP resources automatically and rejects poisoned metadata
- natural-language search has an explicit offline evaluation set and published quality metrics
- at least two independent end-to-end reference integrations
- public service target ≥99% availability during grant verification window

## Public links
Repo: https://github.com/TheAliphant/proofrail
Demo/spec: https://thealiphant.github.io/proofrail/

## Owner-only fields before Interest Form submission
- applicant/contact name
- contact email
- optional SCF referral code (not mandatory)
