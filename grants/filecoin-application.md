# Open Grant Proposal: ProofRail Archive — Verifiable Economic Work Receipts for Autonomous Agents

**Project Name:** ProofRail Archive

**Proposal Category:** Developer and data tooling / Integrations

**Individual or Entity Name:** Individual applicant

**Proposer:** TheAliphant

**Project Repo(s):** https://github.com/TheAliphant/proofrail

**Filecoin ecosystem affiliations:** None.

**Technical Sponsor:** None.

**Do you agree to open source all work you do on behalf of this RFP under the MIT/Apache-2 dual-license?:** Yes.

# Project Summary

Autonomous agents can now discover paid work, produce artifacts, pass QA and transact, but the evidence trail is fragmented across local logs, marketplace databases and chain-specific payment records. ProofRail is a small open protocol and reference SDK for portable, tamper-evident economic work receipts: job → artifact → QA → submission → settlement. The chain-agnostic core is already public and tested; grant work would add a Filecoin-native archival and retrieval layer after a grant agreement is signed.

ProofRail Archive will package receipts, selected artifacts and external verification references into content-addressed evidence bundles stored through Filecoin-compatible storage. Any marketplace, buyer or worker agent will be able to resolve a receipt CID and independently verify what was requested, what artifact hash was delivered, whether QA passed, what submission reference was recorded, and what externally verifiable settlement evidence was attached. This is deliberately distinct from agent memory, model storage or generic evaluation logs: the unit of data is a completed or attempted economic work event.

## Impact

Agent commerce needs durable evidence. A payment transaction can prove value moved, but not what work it paid for; a marketplace database can show task state, but creates a centralized trust dependency; a local agent log is not portable. ProofRail joins these layers without requiring Filecoin to execute the work or custody funds. Filecoin becomes the durable, content-addressed evidence layer for an emerging class of machine-to-machine commerce.

Success means a developer can add ProofRail Archive to an existing agent worker or marketplace, write a receipt bundle after a task lifecycle event, receive a CID, and later verify that bundle from another machine using an open CLI/SDK. The target audience is agent marketplaces, autonomous worker frameworks, x402/payment-enabled agents and teams operating fleets of economic agents.

## Outcomes

The grant-funded deliverables will be:
- a versioned ProofRail receipt-bundle specification for Filecoin archival;
- a Python storage/retrieval adapter with pluggable Filecoin-compatible backend configuration;
- `proofrail archive` and `proofrail resolve` CLI flows;
- integrity verification for receipt JSON, artifact manifests and external payment references;
- an MCP-facing integration example for agent frameworks;
- end-to-end examples covering at least Base/x402 payment evidence plus a chain-agnostic receipt;
- test vectors, documentation and a public interoperability guide;
- adoption instrumentation that counts archived bundles, retrievals and unique integrating applications without collecting private task content.

Success metrics during the grant period: 100+ valid test/economic receipt bundles archived; 95%+ automated conformance-test pass rate; 3 external developer integrations or pilots; and reproducible retrieval/verification from a clean environment.

## Data Onboarding

Initial data volume is intentionally modest because receipts are compact, high-value records. The project optimizes for recurring writes and verifiable retrieval rather than artificial storage volume. Expected first-year growth is from KB/MB-scale receipt bundles toward GB-scale archives as artifact manifests and selected deliverables are included. The more important Filecoin metric for this project is the number of independent economic events archived and retrieved.

## Adoption, Reach, and Growth Strategies

ProofRail starts from a working agent-labour use case rather than a speculative consumer app. The public core already implements deterministic receipts and Base/x402 challenge validation. The first integrations will target agent workers and marketplaces where payment and delivery evidence already exist but are fragmented.

The first 10 developers will be recruited through the open repository, agent-commerce communities and direct integration examples. Growth will focus on adapters rather than a closed hosted service: developers should be able to adopt the receipt format without adopting a specific agent framework.

## Development Roadmap

### Milestone 1 — Filecoin evidence bundle + archive/resolve adapter
**Target completion:** November 20, 2026
**Funding:** $8,000

Deliverables: versioned bundle spec; storage/retrieval adapter; CID returned and persisted in receipts; `archive` and `resolve` CLI commands; deterministic test vectors; unit/integration tests; documentation for local reproduction. One developer/maintainer plus AI-assisted implementation and QA.

### Milestone 2 — Agent integration + independent verification
**Target completion:** December 18, 2026
**Funding:** $12,000

Deliverables: MCP-facing integration example; artifact-manifest support; external payment-reference verifier interface; end-to-end example from task receipt to Filecoin archive to clean-machine verification; failure/tamper cases; security and privacy guidance. One developer/maintainer plus AI-assisted implementation and QA.

### Milestone 3 — Interoperability release + pilot adoption
**Target completion:** January 22, 2027
**Funding:** $10,000

Deliverables: v1 public SDK/CLI release; complete integration guide; compatibility test suite; public metrics for archived bundles/retrievals; at least three external developer pilots/integrations; maintenance roadmap and issue triage process.

## Total Budget Requested

| Milestone # | Description | Deliverables | Completion Date | Funding |
|---|---|---|---|---:|
| 1 | Archive core | Bundle spec, storage/retrieval adapter, CLI, tests | Nov 20, 2026 | $8,000 |
| 2 | Agent verification | MCP example, manifests, verification, E2E demo | Dec 18, 2026 | $12,000 |
| 3 | Interoperability | v1 release, docs, pilots, metrics | Jan 22, 2027 | $10,000 |
| **Total** | | | | **$30,000** |

## Maintenance and Upgrade Plans

ProofRail is designed as infrastructure used by its maintainers' own autonomous-work systems, creating a direct incentive to maintain the core. After the grant, maintenance will include schema compatibility, Filecoin adapter updates, test vectors, security fixes and integration support. Additional chain/payment adapters remain outside the Filecoin grant scope unless specifically agreed.

# Team

## Team Members
- TheAliphant — maintainer / product and systems implementation.

## Team Website
https://thealiphant.github.io/proofrail/

## Relevant Experience

The maintainer operates a local-first autonomous labour engine that discovers machine-executable paid work, creates artifacts, applies deterministic/AI QA gates, records durable receipts and integrates multiple payment/job providers. ProofRail extracts only the portable evidence layer into a public protocol; the private commercial routing engine is not part of the grant.

The existing public ProofRail core includes deterministic canonical JSON receipts, SHA-256 tamper detection, a CLI, test suite and an x402 exact-payment challenge validator targeting Base-compatible payment routes. This pre-existing work is explicitly outside the requested Filecoin-funded milestones.

## Team code repositories
- https://github.com/TheAliphant/proofrail

# Additional Information

ProofRail Archive is intentionally narrower than agent-memory and agent-evaluation storage projects. It addresses completed economic work: a portable relationship between task, artifact, QA, submission and settlement evidence. No Filecoin-specific grant deliverable will begin before a grant agreement is signed.
