> **Status: Interest Form submitted via official SCF UI on 2026-09-18. Awaiting eligibility/invitation.**

# SCF #46 Interest Package — ProofRail / Stellar x402 Bazaar

## Track
**SCF Build — RFP Track**

## Target RFP (SCF #46 applicability pending confirmation)
**X402 Facilitator with Bazaar (discovery) support**

## Application state and SCF #46 deadline
The **Interest Form was submitted on 2026-09-18** via the official SCF UI and **eligibility/invitation remains pending** in the submission record. The [official SCF #46 page](https://communityfund.stellar.org/awards) lists **2026-11-08** as the Build-submission deadline. Only eligible, **invited** teams proceed to a full RFP Track Build submission. The [RFP Track handbook](https://stellar.gitbook.io/scf-handbook/scf-awards/build-award/rfp-track) introduces this x402/Bazaar RFP in the **SCF #45** section; **SCF confirmation that it remains eligible for #46 is required** before treating it as an active #46 submission opportunity. The deadline alone does not establish eligibility. This is an updated preparation package, **not** a second Interest Form, a claim of invitation, or a filed Build submission.

## One-line
Build a production-ready, permissively licensed Stellar x402 facilitator and native Bazaar so autonomous agents can discover, price and pay for HTTP and MCP services on Stellar without pre-baked integrations.

## Why this team / existing proof
ProofRail is already public and working: deterministic economic-work receipts, SHA-256 tamper detection, CLI verification, x402 exact-payment challenge validation, and EVM/Base ERC-20 settlement verification. Separately, the private autonomous labour runtime already operates against real machine-executable work providers and a live Base USDC/x402 receive route. The grant project would not expose the private commercial routing engine; it would build the open Stellar infrastructure requested by the RFP.

## RFP implementation plan
We will build on `@x402/stellar`, not reimplement Stellar settlement primitives. The funded scope is:

1. **Facilitator** — standard `/verify`, `/settle`, `/supported` on both `stellar:testnet` and `stellar:pubnet`, building on a runtime-validated official `@x402/stellar` version. Strict auth-entry validation (classic and custom `__check_auth`, asset/amount/recipient, expiration and replay); `exact` payments; SEP-41 USDC default with 7-decimal amounts; non-custodial fee sponsorship and `/supported` `extra.areFeesSponsored`. **Free/frictionless testnet**, **configurable mainnet fees with documented business model**, configurable caller authentication/metering/rate limits, managed + self-hosted + embedded self-facilitation.
2. **Stellar Bazaar** — `/discovery/resources` with `type`, `payTo`, `network`, `extensions`, `limit`, `offset`; ranked natural-language `/discovery/search` with `query`, cursor and `partialResults`, measured search relevance. Auto-catalog valid discovery `info`/`schema` from `PaymentPayload` **without separate seller registration**. Index HTTP and MCP tools (MCP key `resource.url` + `input.toolName`); soft-drop spoofed/invalid metadata and percent-encoded `routeTemplate` traversal; report results and reasons in **`EXTENSION-RESPONSES`**; keep an off-chain index and maintain spec/interoperability through the grant.
3. **Agent MCP interface** — deterministic search and paid-call tools wrapping discover → authorize → pay → retry, with stable machine-readable error codes and a **non-null reason** for every rejection.
4. **`upto` scheme** — check the current official upstream/TSC state before implementing. If missing, author `scheme_upto_stellar.md` and implement metered capped settlement, coordinated through the x402 Technical Steering Committee; if already accepted upstream, avoid duplicating it and provide conformance/integration work instead. Explain agent smart-account budget policies. **Decide and document whether a Soroban contract enforces recipient binding and single settlement**; SEP-41 allowances alone do not ensure those properties. If contract-free, explicitly disclose the weaker trust model. `batch-settlement` and `auth-capture` are deferred.
5. **Conformance + operations** — unmodified canonical-client plus upstream x402 E2E on **both** networks, exact `payload: {transaction}` wire compatibility, `/supported` Stellar extras, published settled hashes **per network per scheme**, third-party security review and remediation before mainnet production, ≥99% uptime target, telemetry, degraded-mode runbook and post-launch conformance maintenance.

6. **Seller and buyer tooling** — OSS seller helpers for discovery metadata with per-parameter descriptions, buyer/agent query-and-pay helpers, role-based seller/buyer/operator guides with live testnet examples, and two reproducible HTTP/MCP E2E integrations.

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

The proposed infrastructure is the official open-source x402 TypeScript stack with Soroban authorization and configurable Stellar RPC, plus an **off-chain** discovery/search index and MCP gateway. Managed hosting and an equivalent self-host path reduce dependency on a single operator. Specific hosting providers, costs and operating policies remain implementation choices; **none of this is a claim of an already deployed Stellar facilitator**. A future on-chain registry is optional and would require TTL/rent costing outside the settlement hot path. Payments stay non-custodial and ProofRail receipts supplement rather than replace wire conformance.

Operational design will document configurable caller authentication, metering and rate limits, minimal retention of user data without storing keys, public health metrics, incident response, and milestone-based community updates. Build in the open with a permissive OSI-compatible license path (exclude AGPL OpenZeppelin Relayer components); track x402 discovery changes and maintain conformance through the grant period and after launch.

## SDK version and evidence gate (checked 2026-10-07)
- [npm version history](https://www.npmjs.com/package/%40x402/stellar?activeTab=versions) lists **`@x402/stellar` 2.27.0** as latest. The public package describes Stellar **`exact`** support; `upto` remains grant/upstream work, not a present capability claim.
- The earlier ProofRail spike recorded **2.26.0** as pinned and import-tested. **No 2.27.0 installation, import or E2E run was completed in this documentation update**, so the older evidence is not silently promoted to a new-version verification.
- Before changing readiness claims, capture a compatible official dependency lock, inspect licenses, import-test 2.27.0 client/server/facilitator exports and network/token constants, verify `/supported` and `payload: {transaction}` wire shapes, run negative vectors and the canonical testnet suite, and separately authorize any mainnet E2E spend. Archive versions, commands, logs and on-chain hashes.

## Proposed award size
**$90,000 in XLM** over the standard SCF 7.0 10/20/30/40 payment structure.

- **Tranche 0 — $9,000 (10%)**: award acceptance, detailed threat model, conformance matrix, implementation plan and upstream coordination.
- **Tranche 1 — $18,000 (20%) MVP**: `exact` testnet facilitator; `/verify`, `/settle`, `/supported`, sponsored fees, documented configurable operator pricing/auth/metering/rate limits and self-facilitation; first canonical-client payment proof. Bazaar **`/discovery/resources`, automatic validated cataloging (HTTP + MCP), route-template/integrity tests and seller metadata helpers**.
- **Tranche 2 — $27,000 (30%) Testnet**: **ranked natural-language `/discovery/search`** with cursor/`partialResults`, published relevance metrics and `EXTENSION-RESPONSES` conformance; agent MCP search/pay and buyer helpers; independent catalog interoperability test; `upto` spec/upstream gap check, explicit contract/trust-model decision and candidate with conformance evidence.
- **Tranche 3 — $36,000 (40%) Mainnet**: pubnet facilitator/Bazaar; upstream `upto` contribution; two E2E integrations; third-party security-review remediation before production; role-based docs, maintenance, monitoring/runbook and canonical conformance with transaction hashes per network/scheme.

Audit fees themselves are not included; we will use the SCF Audit Bank path specified by the RFP if accepted.

## Success evidence
- unmodified canonical client completes payments on Stellar testnet and pubnet with spec `payload: {transaction}` wire format
- exact and `upto` conformance tests pass
- public settled transaction hash per network and scheme
- `/supported` advertises fee sponsorship via `extra.areFeesSponsored`; all rejections include non-null reasons
- Bazaar auto-indexes HTTP and MCP resources, rejects seller spoofs and encoded traversal, and reports cataloging outcome via `EXTENSION-RESPONSES`
- natural-language search supports cursor/`partialResults`, offline evaluation and published ranking-quality metrics
- configured testnet/mainnet pricing, caller auth, metering and rate limits proven in hosted/self-host flows
- seller metadata helper and buyer/agent helper demonstrated without manual listing registration
- `upto` contract-or-weaker-trust-model decision documented and tested
- at least two independent end-to-end reference integrations
- public service target ≥99% availability during grant verification window

## Public links
Repo: https://github.com/TheAliphant/proofrail
Demo/spec: https://thealiphant.github.io/proofrail/

## Applicant contact
- Truls Indrearne
- hello@offerpath.eu
- SCF referral code: none

## Detailed requirement mapping
See [`stellar-rfp-conformance.md`](stellar-rfp-conformance.md) for a requirement-by-requirement readiness and acceptance matrix.
