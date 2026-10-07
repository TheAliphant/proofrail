# SCF #46 Build — RFP Track Full Submission Draft

> **Pre-invitation draft. Updated 2026-10-07. Not yet submitted as a full application.** Interest Form submitted through official SCF UI on 2026-09-18 without a confirmation number; still awaiting eligibility/invitation. The SCF #46 Build deadline is **2026-11-08**. The current handbook labels the x402/Bazaar RFP as first issued for **SCF #45**; whether it remains eligible for #46 requires explicit confirmation by SCF before submission.

## Applicant
**Name:** Truls Indrearne  
**Contact:** hello@offerpath.eu  
**GitHub:** TheAliphant  
**Project:** ProofRail  
**Repository:** https://github.com/TheAliphant/proofrail  
**Live docs:** https://thealiphant.github.io/proofrail/

## RFP
**X402 Facilitator with Bazaar (discovery) support**

## Abstract
ProofRail proposes a conformance-first Stellar x402 stack centered on the RFP's highest-value gap: a Stellar-native Bazaar and agent-facing MCP interface that can be exercised by a real autonomous economic worker rather than only by synthetic demos. A thin facilitator layer will build directly on the official Apache-2.0 `@x402/stellar` package for `verify`, `settle`, and `supported`; we will not reimplement already-solved Stellar settlement primitives.

The distinguishing layer is evidence and interoperability. ProofRail already turns machine work into tamper-evident receipts that bind job, artifact, QA, submission and settlement evidence. For Stellar, the Bazaar/MCP flow will emit optional ProofRail receipts after successful paid calls, so an agent can both discover and pay for a resource and retain portable evidence of what was purchased and how settlement was verified. This remains additive to x402 wire conformance: canonical clients need no ProofRail awareness.

## Problem
Stellar already has exact x402 settlement, but isolated paid endpoints are not enough for an agent economy. Agents need a catalog they can query without pre-baked integrations, natural-language retrieval with measurable quality, deterministic MCP tools, and wire-level conformance that stays current as the x402 discovery extension evolves. The failure mode is not only missing functionality; it is drift between hosted facilitators, SDK behavior, discovery metadata, wallets, and canonical clients.

Existing Stellar x402 projects are a positive signal, not something this proposal ignores. ProofRail will explicitly test interoperability across independently operated facilitators/catalogs and will avoid designing a walled garden. The goal is to increase usable common infrastructure, not duplicate settlement logic.

**Eligibility/non-duplication gate:** Compare SCF #45-funded and upstream x402/Bazaar deliverables with this proposal before an invited #46 filing. Coordinate with SCF/SDF to establish whether this RFP remains open and which specific gaps are unfunded. Do not repackage work already funded elsewhere as novel or assume a #46 invitation. Revise or withhold the full submission if SCF finds this scope ineligible.

## Why this team
ProofRail emerged from operating an autonomous labour system that discovers machine-executable paid work, creates artifacts, applies QA gates, submits work, reconciles provider outcomes and independently verifies payment evidence. A real worker payout has already been reconciled provider-side and chain-side in the private runtime. The private commercial routing engine remains private, while the reusable evidence layer has been extracted as ProofRail under MIT OR Apache-2.0.

Public readiness today:
- deterministic canonical JSON economic-work receipts;
- SHA-256 tamper detection;
- CLI verification;
- x402 exact-payment challenge validation;
- Base/EVM ERC-20 settlement verification;
- The public lockfile still pins `@x402/stellar`, `@x402/mcp` and `@x402/core` **2.26.0** (limited import tests only). npm lists **2.27.0** as latest on 2026-10-07; [PR #4 CI run](https://github.com/TheAliphant/proofrail/actions/runs/37692829203) temporarily installed all three at **2.27.0** and passed **3/3 import/network/MCP-readiness tests** on Node 22, without modifying the lockfile. A permanent compatible version upgrade, dependency/license audit, canonical both-network E2E and settlement evidence are **still pending**;
- Filecoin Open Grant proposal #2194 for a separate archival adapter;
- requirement-by-requirement Stellar RFP conformance matrix.

## Technical approach

```mermaid
graph LR
  A[Agent runtime] --> B[ProofRail MCP tools]
  B --> C[Stellar Bazaar]
  C --> D[HTTP / MCP paid resource]
  D -->|402 + discovery metadata| A
  A -->|signed Stellar auth entry| E[Thin x402 Facilitator]
  E --> F[@x402/stellar]
  F --> G[Stellar testnet / pubnet]
  E -->|settlement result| H[Optional ProofRail receipt]
  C <--> I[Other Bazaar-compatible facilitators]
```

### Facilitator
**Proposed, not deployed:** A TypeScript wrapper built on the latest compatible official `@x402/stellar` will expose x402 v2 `verify`, `settle`, and `supported` on both `stellar:testnet` and `stellar:pubnet`, preserving the canonical CAIP-2 and `payload: {transaction}` wire shapes. Verify Soroban **auth entries, not presigned transactions**: exact call, asset, atomic 7-decimal amount, recipient, signer, ledger expiry/replay protection, classic accounts and `__check_auth` smart accounts. Use SEP-41 assets with USDC default, validate trustlines, sponsor network fees, and accurately declare `extra.areFeesSponsored`. Payment comes from the buyer, never ProofRail custody; every rejection includes a non-null structured reason.

**Testnet economics:** Hosted testnet facilitation will be **free and usable without paid onboarding or mandatory production keys**, with usable faucet/trustline/auth-entry-signing examples. Transparent configurable abuse limits may still apply.

**Mainnet economics:** A hosted operator may charge an optional, published per-call/processing or support fee. Provide configuration for **zero fee**, fee amount/rate and exemptions, no baked-in protocol tariff; self-hosters can remove any operator surcharge. Document quoted fee and separate operating costs, without describing projected income as revenue already earned.

**Caller auth, metering and limits:** Document and configure anonymous/credentialed modes (e.g. scoped API keys or signed caller identity), per-caller/network request and settlement counters, rate/burst ceilings, error codes for missing auth/over-quota, and how retries/failed calls are counted. Meter without storing sensitive signed payloads or agent content. Keep the free-testnet path frictionless.

**Hosting modes:** Supply reproducible managed and independent self-hostable deployment instructions **plus self-facilitation inside a resource server** without relying on a hosted ProofRail account. Canonical integration tests will exercise each mode.

### Bazaar
The planned off-chain Bazaar will implement `GET /discovery/resources` with `type`, `payTo`, `network`, `extensions`, `limit` and `offset` filters, and `GET /discovery/search` with natural-language `query`, cursor and `partialResults`. A received `PaymentPayload` carrying the discovery extension will have its `info` validated against the supplied `schema`, then be automatically indexed without another seller action; any manual registration is auxiliary. Catalog HTTP and MCP resources (MCP identity is the pair `resource.url` + `input.toolName`). Validate service identity, `payTo` and routeTemplate including percent-decoding before traversal detection; forged/invalid metadata must soft-drop with a reason.

**`EXTENSION-RESPONSES` reporting:** On the spec-defined payment response, emit a conformant indexed/ignored/rejected outcome and machine-readable reason for catalog ingestion so a seller can see whether its listing landed; test both accepted and soft-dropped entries and follow the then-current wire format.

Search starts with a deterministic hybrid retrieval baseline: structured filters + lexical retrieval + optional embedding rerank. We will publish a labeled offline evaluation set, repeatable nDCG@10 and recall@10 trends, cursor and `partialResults` tests. Search-model choice remains replaceable so the public service is not locked to one proprietary embedding vendor.

**Seller-side helper:** A minimal HTTP/MCP descriptor and validation API will support service, endpoint and tool descriptions, plus **per-parameter** name, type, description/purpose, required status and examples. The example seller will appear via automatic cataloging, not a manual listing step.

**Spec drift and interop:** Review Foundation x402/Bazaar specs, x402 TSC discussions, active PRs and latest stable Stellar SDK changelogs **at least weekly** through the grant. Version fixtures and run canonical conformance/e2e against pinned and latest-compatible releases before releases; publish change logs and cross-catalog tests against independent operators. Preserve common x402 representation, not a ProofRail-specific walled garden. The index stays off-chain by default; an on-chain registry and its rent are outside baseline.

### Agent-facing MCP
The MCP server exposes deterministic tools for resource search, quote inspection and a bounded `paid_call` flow. Payment failures, unsupported networks/assets, stale auth entries, search partials and cataloging failures return typed errors rather than prose-only messages.

### `upto`
**Proposed design: YES, a minimal Soroban contract for `upto`; none exists or is audited in ProofRail today.** The baseline `exact` facilitator uses official settlement and requires no new contract. But metered `upto` must authorize an upper cap, settle only actual usage, bind recipient and prevent double capture. SEP-41 allowances alone (`approve` / `transfer_from`) cannot enforce recipient binding and once-only settlement; we will **not** claim that a contract-free path offers equivalent guarantees. The planned contract will enforce cap, designated recipient and single settlement, with explicit replay state, TTL/rent and resource limits to be designed and reviewed.

**Agent budget policy:** A smart account's `__check_auth` spending policy may cap cumulative spend and bind network/payee/scheme/expiry before signing, but the on-chain settlement contract must independently uphold recipient binding, cap and one-time capture. Test over-cap use, changed payee, expiration, policy-budget exhaustion and repeat capture. Do not count an authorization as a settled transaction or as income.

**Upstream and security gate:** Inspect existing `scheme_upto_stellar.md` proposals and x402 TSC/SDF PRs before authoring competing work. If not implemented upstream, contribute a network spec, secure contract/scheme implementation and regression vectors. If it is already accepted, redirect effort to missing canonical conformance, smart-account interop and integration rather than duplicate funded work. Track PR, review and merge separately; do not claim acceptance until verified. A contract-specific third-party audit/review must be secured **before mainnet activation**. `batch-settlement` and `auth-capture` remain deferred.

### ProofRail evidence
After a paid call settles, integrations may create a portable receipt containing resource identifier/hash, output artifact hash where applicable, network/asset/amount, settlement reference and verification state. This is optional and does not change canonical x402 payloads. It creates a useful bridge between payment infrastructure and autonomous economic work.

## Decentralization and infrastructure
The baseline registry is deliberately off-chain to avoid per-payment rent and a second on-chain transaction. Decentralization comes from protocol interoperability and operator plurality: permissive code, self-hostable facilitator and Bazaar, portable resource metadata, no custody, and the ability to query/compare independently operated catalogs. Hosted reference services will run on conventional replicated infrastructure with reproducible deployment manifests.

**Planned (not currently running) infrastructure:** Containerized API/MCP front ends, an independently restorable off-chain catalog/index, validated ingestion queue, network-specific RPC connections, and isolated fee-sponsoring submission keys. Publish config/secrets and key-rotation guidance, storage backups, resource-budget/sequence-number load tests and channel-account or equivalent concurrency strategy.

**Failure behavior:** If RPC is unavailable or settlement is ambiguous, fail closed and never return a fabricated paid result/receipt. If indexing lags, return bounded stale/partial discovery with explicit status, not a silent full-results claim. Public targets are ≥99% measured availability, p50/p95 latency, error rates, and a documented incident/rollback/runbook process.

## Privacy and user protection
The Bazaar stores public service metadata, not private agent prompts or purchased content. ProofRail receipts default to hashes/references rather than raw task content. Do not log private keys, signed payment payload bodies, authentication tokens, purchased content or raw prompts. Operational telemetry uses aggregate counters and minimally identifying/pseudonymized caller IDs where possible; no profiling or resale. Proposed default sanitized request-level retention is **at most seven days**, shorter by configuration; publish retention by data class, deletion access and incident response before launch. Abuse protections include configurable request authentication, rate limiting, resource validation and poison/identity-spoof defenses. Redaction and retention tests are production gates.

## Product-market fit and adoption
The direct user is software: agent runtimes, paid API/MCP sellers, marketplaces and facilitator operators. ProofRail's own autonomous-work environment provides an immediate consumer for discovery/pay/retry integration testing, while public reference consumers will be published so adoption does not depend on the private runtime.

The first adoption target is ten paid/discoverable endpoints across at least three independent operators or sellers, followed by two independent agent runtimes completing discovery → payment → retry without pre-baked endpoint knowledge. Interoperability with pre-existing Stellar x402 operators is explicitly part of the plan.

## Milestones and tranches

### Tranche 0 — Award acceptance / design lock — $9,000 (10%)
- current x402/Stellar dependency/license audit, upgrading the limited 2.26.0 spike to the latest compatible stable release (2.27.0 was npm latest as checked 2026-10-07);
- threat model and conformance matrix;
- Bazaar data model, poisoning defenses and search evaluation corpus design;
- explicit interop plan covering other Stellar x402 implementations;
- upstream `upto` state review with TSC/SDF coordination, a contract/smart-account budget security design and an explicit contract-audit dependency;
- reproducible local stack;
- draft free-testnet, operator-configurable mainnet-fee, caller-access/metering/rate, privacy/retention and maintenance policies;
- confirm #46 RFP eligibility and no duplicate funding **before full submission**.

**Acceptance:** public architecture + threat model + license/SBOM report + green readiness suite.

### Tranche 1 — MVP / testnet facilitator + Bazaar core — $18,000 (20%)
- `verify`, `settle`, `supported` on Stellar testnet built on `@x402/stellar`;
- sponsored-fee support and advertised `areFeesSponsored`, a publicly usable **free testnet** flow and explicit auth-entry negative tests;
- `/discovery/resources` filters/pagination;
- automatic discovery-extension cataloging for HTTP + MCP resources;
- routeTemplate/integrity negative vectors with `EXTENSION-RESPONSES` accepted/soft-dropped outcomes;
- seller metadata helpers with per-parameter descriptions and no extra registration;
- configurable auth/metering/rate limits, published fee settings and hosted/self-host/self-facilitation examples.

**Acceptance:** unmodified canonical client completes exact payment on testnet; public settled tx hash; stock SDK can query the catalog.

### Tranche 2 — Search + MCP + `upto` + interoperability — $27,000 (30%)
- `/discovery/search` with cursor pagination + `partialResults`;
- published retrieval evaluation set and nDCG@10/recall@10 baseline;
- deterministic MCP search + paid-call tools;
- buyer/agent helpers;
- `upto` spec and scheme/contract candidate with smart-account spending-policy regression vectors, coordinated upstream, **or** non-duplicative integration/conformance work if the upstream scheme is already accepted;
- at least one cross-operator interoperability test and ongoing x402 spec-change compatibility fixtures;
- ProofRail settlement-receipt adapter.

**Acceptance:** agent completes discover → pay → retry on testnet with no endpoint preconfiguration; search metrics published; `upto` integration status linked to actual upstream state.

### Tranche 3 — Pubnet / conformance / audit remediation — $36,000 (40%)
- pubnet facilitator and Bazaar reference services, published operator-configurable fee/business model, per-caller controls and non-custodial deployment guide;
- exact + `upto` canonical E2E on required networks once the `upto` contract and wire design are independently reviewed; no production claim for unreviewed code;
- published settlement hashes per required network/scheme;
- two clean-clone example integrations;
- independently funded/approved third-party security review through the applicable SCF audit route, including any new `upto` contract, with remediation before pubnet activation;
- ≥99% availability target with monitoring/runbook;
- role-based seller, buyer/agent and operator documentation with live free-testnet examples, a measured <1-hour clean-machine path and a **Stellar Developer Docs** contribution PR (not a promised maintainer merge);
- ongoing discovery-spec change tracking and regression process, uptime/performance dashboard, privacy policy, retention checks, failed-settlement drills and self-facilitation evidence.

**Acceptance:** RFP conformance report with direct links/hashes, unmodified canonical clients on required networks, public operational docs, and resolved review findings.

## Budget
**Requested: $90,000 in XLM equivalent**

The budget weights discovery/search/MCP/conformance more heavily than settlement because the RFP itself identifies Bazaar and ongoing conformance as the novel work. No budget is allocated to reimplementing functionality already supplied by `@x402/stellar`. Security-review fees are **not** assumed to be awarded by SCF's Audit Bank. An Audit Bank application/approval and independent contract-specific review scope must be verified before including the `upto` contract in a production milestone. If not funded there, revise the audit budget or milestones with SCF before an invited submission; never ship an unaudited new contract on pubnet.

## Maintenance
For at least 12 months after mainnet completion, review upstream discovery/TSC changes and current stable Stellar packages **weekly**, maintain versioned compatibility fixtures, rerun canonical suites per release, and publish tested-version notes and conformance-impacting fixes. Post at least biweekly public milestone updates during active grant work; publish self-hosting and handoff instructions so maintenance does not rely on one hosted operator. The hosted service remains reference infrastructure, while portable code, tests and operator documents are the durable asset.

## Risks and mitigations
- **Discovery spec drift:** pinned plus current-compatible conformance fixtures, weekly upstream reviews and published release notes.
- **SCF eligibility and duplicate funding:** handbook's RFP references #45; invitation and acceptance for #46 remain pending. Confirm remaining unfunded gaps before filing.
- **Duplicate ecosystem work:** explicit interoperability and upstream coordination; no fork when compatible work is already accepted.
- **Search quality:** published evaluation corpus/metrics, not subjective demo queries.
- **Catalog poisoning:** schema validation, routeTemplate defenses, seller/resource identity checks, soft-drop reasons.
- **Sequence bottlenecks under bursty agent traffic:** benchmark channel-account or equivalent transaction-submission strategy and document capacity limits.
- **Wallet/auth-entry compatibility:** canonical clients plus custom-account, payee, spending-cap and ledger-expiry vectors.
- **`upto` audit and contract maturity:** no built/audited candidate yet; secure independent review, upstream alignment and a mainnet-safe schedule before presenting it as delivered.
- **Hosted operator dependency:** permissive license, reproducible self-host path, no custody, portable metadata.

## Open source and communication
All grant-funded work will be under a permissive OSI-approved license compatible with the x402 dependency path. Development, issues, conformance failures and milestone evidence will be public. Status updates will be posted at least biweekly during active grant execution.

## Submission readiness / external proof gates

| Item | Verified now (2026-10-07) | Needed next |
|---|---|---|
| SCF #46 eligibility | Interest Form submitted in official UI, 2026-09-18; no confirmation number | Written eligibility/invitation and confirmation that this #45-origin RFP is eligible for #46 |
| Full proposal | **Draft only; not submitted** | Approved non-duplicative scope and invited submission before 2026-11-08 |
| Dependency compatibility | Limited 2.26.0 SDK import spike; npm now shows 2.27.0 | Upgrade/pin latest compatible stable; rerun and publish test evidence |
| Stellar facilitator, Bazaar, MCP | **Not implemented or production-verified** | Public service and canonical client E2E, discovery fixtures and seller-side helpers |
| `upto` Soroban contract and upstream | **Not built, audited, merged or settled in ProofRail** | Spec/contract design, upstream review, policy and on-chain security tests, live hashes |
| Docs and operations | **Planned** | Privacy/retention and operations evidence, two examples, live testnet guides and Stellar Developer Docs contribution |

## Current evidence
- ProofRail repo: https://github.com/TheAliphant/proofrail
- v0.2.0: https://github.com/TheAliphant/proofrail/releases/tag/v0.2.0
- public docs: https://thealiphant.github.io/proofrail/
- Stellar readiness spike: `spikes/stellar-x402/`
- RFP conformance matrix: `grants/stellar-rfp-conformance.md`
- Filecoin proposal (separate scope): https://github.com/filecoin-project/devgrants/issues/2194
