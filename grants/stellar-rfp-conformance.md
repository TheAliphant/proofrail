# Stellar x402 Facilitator + Bazaar RFP — Conformance Matrix

Source RFP: https://stellar.gitbook.io/scf-handbook/scf-awards/build-award/rfp-track

This matrix separates **pre-existing/readiness evidence** from **award deliverables**. It is intentionally not a claim that the RFP has already been implemented.

| RFP area | Requirement | Readiness evidence now | Award deliverable | Acceptance evidence |
|---|---|---|---|---|
| 3.1 Facilitator | `verify`, `settle`, `supported` on testnet + pubnet | Official `@x402/stellar` 2.26.0 pinned and import-tested | Build hosted + self-hostable service on official package | Canonical client E2E + public endpoints |
| 3.1 Facilitator | strict auth-entry validation / non-custodial settlement | ProofRail already treats settlement verification as fail-closed evidence | Implement official Stellar verification/settlement path; no custody | Negative vectors + settled tx hashes |
| 3.1 Facilitator | SEP-41 assets, USDC default, sponsored fees | Official SDK network/USDC constants verified in spike | Configurable token support + fee sponsorship | `/supported` wire output + E2E |
| 3.2 Bazaar | resource browsing + filters | Receipt/resource metadata model experience | Implement `/discovery/resources` | API conformance tests |
| 3.2 Bazaar | natural-language search + cursor pagination | Autonomous labour system already ranks machine-executable opportunities privately | Build independent OSS retrieval/ranking layer with evaluation corpus | Published relevance metrics + deterministic API tests |
| 3.2 Bazaar | automatic discovery-extension cataloging | x402 challenge validation already implemented | Validate discovery payload/schema and catalog without manual registration | Valid + poison/tamper vectors |
| 3.2 Bazaar | HTTP + MCP resources | `@x402/mcp` primitives pinned/import-tested | Index both resource types using x402 conventions | E2E examples for each type |
| 3.2 Bazaar | integrity + routeTemplate defenses | ProofRail core has deterministic hashing/tamper detection | Implement soft-drop, percent-decoding and traversal validation | Security regression suite |
| 3.3 MCP | agent search + paid-call proxy | Official MCP payment helpers verified in spike | Deterministic MCP search/pay/retry tools | Agent E2E with machine-readable failures |
| 3.4 Schemes | `exact` | Official facilitator exact scheme verified in spike | Wire-level testnet/pubnet facilitator support | x402 canonical E2E suite |
| 3.4 Schemes | Stellar `upto` spec + implementation | General x402/payment-verification experience | Author `scheme_upto_stellar.md`, implement, coordinate upstream | Upstream PR/merge + E2E vectors |
| 3.5 Stellar | auth entries / ledger expiry / trustlines / limits / throughput | Official Stellar SDK selected, no alternative settlement stack | Explicit handling in implementation + docs | Load tests + failure vectors + docs |
| 3.6 License | permissive OSI license | ProofRail dual MIT/Apache-2.0; x402 deps Apache-2.0 | Maintain compatible dependency path; reject AGPL dependency path | SBOM/license audit |
| 3.6 Conformance | canonical wire compatibility | x402 v2 concepts already represented; official packages pinned | Run canonical x402 E2E suite on both Stellar networks | Published report and transaction hashes |
| 3.6 Security | replay/front-running/index poisoning defenses | Tamper-evident receipts + exact EVM transfer validation exist | Threat model, tests, SCF Audit Bank review and remediation | Public report/remediation log |
| 3.6 UX | docs → paid discoverable endpoint <1h | Public ProofRail docs live | Role-based seller/buyer/operator docs + examples | Clean-machine onboarding run |
| 3.6 Ops | ≥99% target + degraded-mode story | Existing autonomous runtime uses durable fail-closed states | Monitoring, rate limits, runbook, incident modes | Public health/telemetry |
| 5 Examples | ≥2 end-to-end integrations | Existing Base/x402 and autonomous-work context inform examples | Paid HTTP API + MCP agent discovery/payment example | Reproducible repos/scripts |

## Boundary

The private Agent Labour Engine remains private. Grant work builds the requested open Stellar x402 infrastructure and ProofRail interoperability surfaces only; private provider ranking, commercial strategy, credentials and internal receipts are not grant deliverables.
