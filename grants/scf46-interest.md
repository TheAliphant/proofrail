# SCF #46 Interest Package — ProofRail Settlement

## One-line
ProofRail Settlement is an open receipt and settlement layer that lets buyer agents and worker agents bind a Stellar payment to independently verifiable evidence of the work that payment represents.

## Existing product
ProofRail core is public and working: deterministic JSON receipts, SHA-256 tamper detection, CLI verification and a Base/x402 challenge adapter. The project emerged from operating an autonomous labour engine where task, artifact, QA, submission and payment evidence already need to be reconciled.

## Why Stellar
Stellar is a strong settlement rail for autonomous work because the protocol is optimized for low-cost asset transfer and programmable applications. The Stellar integration would keep execution off-chain while using Stellar/Soroban for job funding, bounded escrow/release logic where appropriate, and durable settlement references attached to ProofRail receipts.

## Proposed Build Award scope
MVP: Stellar testnet payment adapter + receipt binding + CLI verification.
Testnet tranche: bounded job escrow/release reference implementation, end-to-end buyer-agent → worker-agent demo, failure/dispute state model.
Mainnet tranche: hardened SDK, security review remediation, mainnet settlement flow and reference integration for agent marketplaces.

## Differentiation
ProofRail does not attempt to become an agent marketplace. It is interoperable infrastructure that existing marketplaces and autonomous workers can adopt. The receipt remains portable even if a project later changes settlement networks.

## Public links
Repo: https://github.com/TheAliphant/proofrail
Demo/spec: https://thealiphant.github.io/proofrail/

## Owner-only fields before submission
- contracting individual/entity name
- best contact email
- requested SCF budget and tranche split after final Stellar implementation sizing
