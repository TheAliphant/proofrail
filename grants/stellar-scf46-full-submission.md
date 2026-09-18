# SCF #46 Build — RFP Track Full Submission Draft

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

## Why this team
ProofRail emerged from operating an autonomous labour system that discovers machine-executable paid work, creates artifacts, applies QA gates, submits work, reconciles provider outcomes and independently verifies payment evidence. A real worker payout has already been reconciled provider-side and chain-side in the private runtime. The private commercial routing engine remains private, while the reusable evidence layer has been extracted as ProofRail under MIT OR Apache-2.0.

Public readiness today:
- deterministic canonical JSON economic-work receipts;
- SHA-256 tamper detection;
- CLI verification;
- x402 exact-payment challenge validation;
- Base/EVM ERC-20 settlement verification;
- official `@x402/stellar`, `@x402/mcp`, and `@x402/core` 2.26.0 pinned and tested in a public readiness spike;
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
A TypeScript service built on `@x402/stellar` exposes the current x402 v2 `verify`, `settle`, and `supported` surfaces for testnet and pubnet. It supports SEP-41 assets, USDC defaults, sponsored fees, configurable authentication/rate limits, hosted/self-hosted/self-facilitated paths, classic keypairs and compatible `__check_auth` accounts. Every rejection has a non-null machine-readable reason.

### Bazaar
An off-chain index implements `GET /discovery/resources` with the required filters and `GET /discovery/search` with cursor pagination and `partialResults`. Cataloging occurs automatically from valid discovery extension payloads received through payment traffic. HTTP endpoints and MCP tools are first-class resources. Route templates are percent-decoded before traversal validation, hostile metadata soft-drops with explicit reasons, and cataloging outcomes are returned through `EXTENSION-RESPONSES`.

Search starts with a deterministic hybrid retrieval baseline: structured filters + lexical retrieval + optional embedding rerank. We will publish an offline relevance set and measure nDCG@10 and recall@10. Search-model choice remains replaceable so the public service is not locked to one proprietary embedding vendor.

### Agent-facing MCP
The MCP server exposes deterministic tools for resource search, quote inspection and a bounded `paid_call` flow. Payment failures, unsupported networks/assets, stale auth entries, search partials and cataloging failures return typed errors rather than prose-only messages.

### `upto`
We will coordinate rather than fork competing protocol work. The submission commits to an upstream Stellar `upto` contribution only after checking the current x402 TSC state and existing active PRs. If a compatible implementation is already accepted upstream before the milestone begins, grant effort moves to conformance, integration vectors, smart-account spending-policy composition and regression coverage rather than duplicating it. If not, we will author/complete the Stellar network spec and implementation, with a Soroban contract if required to preserve recipient binding and single-settlement guarantees.

### ProofRail evidence
After a paid call settles, integrations may create a portable receipt containing resource identifier/hash, output artifact hash where applicable, network/asset/amount, settlement reference and verification state. This is optional and does not change canonical x402 payloads. It creates a useful bridge between payment infrastructure and autonomous economic work.

## Decentralization and infrastructure
The baseline registry is deliberately off-chain to avoid per-payment rent and a second on-chain transaction. Decentralization comes from protocol interoperability and operator plurality: permissive code, self-hostable facilitator and Bazaar, portable resource metadata, no custody, and the ability to query/compare independently operated catalogs. Hosted reference services will run on conventional replicated infrastructure with reproducible deployment manifests.

## Privacy and user protection
The Bazaar stores public service metadata, not private agent prompts or purchased content. ProofRail receipts default to hashes/references rather than raw task content. Logs exclude private keys, auth-entry secrets and purchased payload bodies. Operational telemetry is aggregate and bounded. Abuse protections include configurable request authentication, rate limiting, resource validation, catalog poisoning defenses and explicit retention documentation.

## Product-market fit and adoption
The direct user is software: agent runtimes, paid API/MCP sellers, marketplaces and facilitator operators. ProofRail's own autonomous-work environment provides an immediate consumer for discovery/pay/retry integration testing, while public reference consumers will be published so adoption does not depend on the private runtime.

The first adoption target is ten paid/discoverable endpoints across at least three independent operators or sellers, followed by two independent agent runtimes completing discovery → payment → retry without pre-baked endpoint knowledge. Interoperability with pre-existing Stellar x402 operators is explicitly part of the plan.

## Milestones and tranches

### Tranche 0 — Award acceptance / design lock — $9,000 (10%)
- current x402/Stellar dependency and license audit;
- threat model and conformance matrix;
- Bazaar data model, poisoning defenses and search evaluation corpus design;
- explicit interop plan covering other Stellar x402 implementations;
- upstream `upto` state review with TSC/SDF coordination;
- reproducible local stack.

**Acceptance:** public architecture + threat model + license/SBOM report + green readiness suite.

### Tranche 1 — MVP / testnet facilitator + Bazaar core — $18,000 (20%)
- `verify`, `settle`, `supported` on Stellar testnet built on `@x402/stellar`;
- sponsored-fee support and advertised `areFeesSponsored`;
- `/discovery/resources` filters/pagination;
- automatic discovery-extension cataloging for HTTP + MCP resources;
- routeTemplate/integrity negative vectors;
- seller metadata helpers.

**Acceptance:** unmodified canonical client completes exact payment on testnet; public settled tx hash; stock SDK can query the catalog.

### Tranche 2 — Search + MCP + `upto` + interoperability — $27,000 (30%)
- `/discovery/search` with cursor pagination + `partialResults`;
- published retrieval evaluation set and nDCG@10/recall@10 baseline;
- deterministic MCP search + paid-call tools;
- buyer/agent helpers;
- `upto` upstream contribution or, if already upstream, a documented non-duplicative conformance/integration contribution;
- at least one cross-operator interoperability test;
- ProofRail settlement-receipt adapter.

**Acceptance:** agent completes discover → pay → retry on testnet with no endpoint preconfiguration; search metrics published; `upto` integration status linked to actual upstream state.

### Tranche 3 — Pubnet / conformance / audit remediation — $36,000 (40%)
- pubnet facilitator and Bazaar reference services;
- exact + `upto` canonical E2E where upstream scheme is available;
- published settlement hashes per required network/scheme;
- two clean-clone example integrations;
- third-party security review via the applicable SCF audit path and remediation;
- ≥99% availability target with monitoring/runbook;
- role-based seller, buyer/agent and operator documentation;
- ongoing discovery-spec change tracking and regression process.

**Acceptance:** RFP conformance report with direct links/hashes, unmodified canonical clients on required networks, public operational docs, and resolved review findings.

## Budget
**Requested: $90,000 in XLM equivalent**

The budget weights discovery/search/MCP/conformance more heavily than settlement because the RFP itself identifies Bazaar and ongoing conformance as the novel work. No budget is allocated to reimplementing functionality already supplied by `@x402/stellar`. Security review fees that are handled separately through SCF's audit mechanism are not double-counted.

## Maintenance
For at least 12 months after mainnet completion, the project will track x402 discovery/TSC changes, pin and test current stable Stellar packages, maintain compatibility vectors and publish release notes for conformance-impacting changes. The hosted service is reference infrastructure; the primary sustainability asset is the self-hostable code and tests. ProofRail's own ongoing use of payment verification and agent commerce provides a direct maintenance incentive.

## Risks and mitigations
- **Discovery spec drift:** pinned conformance fixtures + monitored upstream changes + release cadence.
- **Duplicate ecosystem work:** explicit interoperability and upstream coordination; no fork when compatible work is already accepted.
- **Search quality:** published evaluation corpus/metrics, not subjective demo queries.
- **Catalog poisoning:** schema validation, routeTemplate defenses, seller/resource identity checks, soft-drop reasons.
- **Sequence bottlenecks under bursty agent traffic:** benchmark channel-account or equivalent transaction-submission strategy and document capacity limits.
- **Wallet/auth-entry compatibility:** canonical test clients plus custom-account vectors and explicit expiration tests.
- **Hosted operator dependency:** permissive license, reproducible self-host path, no custody, portable metadata.

## Open source and communication
All grant-funded work will be under a permissive OSI-approved license compatible with the x402 dependency path. Development, issues, conformance failures and milestone evidence will be public. Status updates will be posted at least biweekly during active grant execution.

## Current evidence
- ProofRail repo: https://github.com/TheAliphant/proofrail
- v0.2.0: https://github.com/TheAliphant/proofrail/releases/tag/v0.2.0
- public docs: https://thealiphant.github.io/proofrail/
- Stellar readiness spike: `spikes/stellar-x402/`
- RFP conformance matrix: `grants/stellar-rfp-conformance.md`
- Filecoin proposal (separate scope): https://github.com/filecoin-project/devgrants/issues/2194
