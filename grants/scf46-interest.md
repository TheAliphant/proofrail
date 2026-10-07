> **Status (2026-10-07): Interest Form submitted via the official SCF UI on 2026-09-18 (no confirmation number shown). Eligibility/invitation pending. This is an interest-package draft, not an invited or filed full application and not an award.**

> **Round/RFP check:** SCF #46 lists **2026-11-08** as its Build submission deadline; the x402/Bazaar RFP in the current handbook was introduced for **SCF #45**. Confirm with SCF that it is eligible for #46, review already-funded related work and obtain the invitation before submitting the full draft.

# SCF #46 Interest Package — ProofRail / Stellar x402 Bazaar

## Track
**SCF Build — RFP Track**

## RFP basis (eligibility for SCF #46 not yet confirmed)
**X402 Facilitator with Bazaar (discovery) support**

## One-line
Build a production-ready, permissively licensed Stellar x402 facilitator and native Bazaar so autonomous agents can discover, price and pay for HTTP and MCP services on Stellar without pre-baked integrations.

## Why this team / existing proof
ProofRail is already public and working: deterministic economic-work receipts, SHA-256 tamper detection, CLI verification, x402 exact-payment challenge validation, and EVM/Base ERC-20 settlement verification. Separately, the private autonomous labour runtime already operates against real machine-executable work providers and a live Base USDC/x402 receive route. The grant project would not expose the private commercial routing engine; it would build the open Stellar infrastructure requested by the RFP.

## RFP implementation plan
The *proposed* work will build on the official `@x402/stellar`, not reimplement Stellar settlement primitives. The public readiness spike pins/import-tests version **2.26.0** only; npm listed **2.27.0** as latest on 2026-10-07. Latest-compatible-stable repinning and full integration tests are still outstanding. No grant-funded Stellar infrastructure is claimed as deployed. Proposed scope:

1. **Facilitator** — `/verify`, `/settle`, `/supported` on testnet and pubnet; strict Soroban auth-entry and `__check_auth` validation, ledger expiry, non-custodial exact settlement, SEP-41/USDC (7 decimals) and accurate `extra.areFeesSponsored`. Make testnet **free/frictionless**, mainnet operator fees **configurable including zero**, and caller auth/metering/rate limits **configurable and documented**. Package hosted, self-hosted and in-resource-server **self-facilitation** paths.
2. **Stellar Bazaar** — `/discovery/resources` with `type`, `payTo`, `network`, `extensions`, `limit`, `offset`; natural-language `/discovery/search` with cursors, `partialResults` and published ranking evaluation. Automatically schema-validate/index discovery payloads for HTTP and MCP, verify seller identity/route templates, soft-drop poisoning, report indexing outcome/reason in **`EXTENSION-RESPONSES`**. Provide low-boilerplate seller helpers, including **per-parameter descriptions**, and interoperable off-chain metadata.
3. **Agent MCP interface** — deterministic search, quote and paid-call tools wrapping discover → authorize → pay → retry, with non-null machine-readable rejection reasons and canonical x402 interoperability.
4. **`upto` scheme** — check the current upstream TSC/PR state first, then contribute `scheme_upto_stellar.md` and the missing implementation/conformance. **Proposed design includes a minimal new Soroban contract** (not built/audited) to bind recipient, cap and single settlement; smart-account spending policies additionally bound an agent's budget. SEP-41 allowances alone do **not** provide equivalent guarantees. If already implemented upstream, contribute only documented non-duplicative tests/integration. Keep batch-settlement/auth-capture out of scope.
5. **Conformance + operations** — maintain current-spec wire fixtures as x402 evolves; unmodified canonical-client E2E on both Stellar networks for required schemes, public settled tx hashes, external security review **including any new Soroban contract before mainnet**, ≥99% availability target, safe degraded modes, monitoring/runbook, documented privacy/tracking/retention, and role-based seller, buyer/agent and operator guides **contributed to Stellar Developer Docs**.

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

**Implementation boundary:** Existing public evidence covers receipts, tamper detection, CLI, Base/EVM verification and limited import-only Stellar SDK readiness. There are **no** verified ProofRail Stellar facilitator/Bazaar deployments, `upto` contract, Stellar settled tx hashes, full canonical conformance results, independent audit or SCF award at this stage. Existing independently funded x402/Bazaar projects must be compared before committing to overlapping milestones.

## Proposed award size
**$90,000 in XLM** over the standard SCF 7.0 10/20/30/40 payment structure.

- **Tranche 0 — $9,000 (10%)**: only after award acceptance; threat model, latest-compatible-stable SDK/license audit, requirement matrix, RFP overlap/eligibility review, fee/auth/privacy policy, `upto` contract/policy design and upstream coordination.
- **Tranche 1 — $18,000 (20%) MVP**: free public testnet exact facilitator; `/verify`, `/settle`, `/supported`, fee sponsorship, configurable caller controls/fee settings and self-facilitation example; Bazaar core with automatic indexing, `EXTENSION-RESPONSES`, seller parameter helpers and canonical E2E proof.
- **Tranche 2 — $27,000 (30%) Testnet**: evaluated Bazaar browse/search, HTTP+MCP automatic cataloging, agent MCP tools, interop tests and `upto` upstream-aligned spec/contract candidate with smart-account budget tests; public testnet conformance evidence.
- **Tranche 3 — $36,000 (40%) Mainnet**: pubnet facilitator/Bazaar, configurable mainnet business model, upstream `upto` contribution/conformance, independent audit and contract review **before** live activation, two E2E integrations, Stellar Developer Docs contribution, public privacy/retention/runbook/monitoring and required transaction hashes/conformance report.

Audit fees are not presumed awarded; use the SCF Audit Bank process **if approved**. Before a production Soroban `upto` contract, secure contract-specific review scope/funding or revise the budget/milestones with SCF. No review or award is claimed yet.

## Success evidence
- unmodified canonical client completes payments on Stellar testnet and pubnet
- exact and `upto` canonical conformance tests pass **after implementation and required review**
- public settled transaction hash per network and scheme
- `/supported` advertises required Stellar extras including fee sponsorship
- Bazaar indexes HTTP and MCP resources automatically, rejects poisoned metadata and reports acceptance/rejection in `EXTENSION-RESPONSES`
- natural-language search has an explicit offline evaluation set and published quality metrics
- at least two independent end-to-end reference integrations
- free, usable testnet and configurable mainnet fees/access controls with self-facilitation example
- public service target ≥99% availability during grant verification window, privacy/retention policy and safe degraded-mode drill
- role-based guides and a public Stellar Developer Docs contribution PR (upstream merge subject to review)

## Public links
Repo: https://github.com/TheAliphant/proofrail
Demo/spec: https://thealiphant.github.io/proofrail/

## Applicant contact
- Truls Indrearne
- hello@offerpath.eu
- SCF referral code: none

## Delivery and upkeep commitments

During an approved grant, track x402 Bazaar/SDK/TSC changes at least weekly, publish conformance-impacting changes and at least biweekly public progress reports, and maintain compatibility/test infrastructure for at least 12 months after mainnet completion. Public runbooks, container/config templates and portable metadata aim to make continued self-hosting viable if ProofRail stops hosting the reference service. All commitments here are **plans contingent on eligibility and grant award**, not evidence of work delivered.

## Detailed requirement mapping
See [`stellar-rfp-conformance.md`](stellar-rfp-conformance.md) for a requirement-by-requirement readiness and acceptance matrix.
