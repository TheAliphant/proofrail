# Stellar x402 RFP readiness spike

This deliberately small spike proves ProofRail is building against the current official x402 packages rather than inventing a parallel Stellar payment implementation.

It pins `@x402/stellar`, `@x402/mcp`, and `@x402/core` at 2.26.0 and tests that the official SDK exposes:

- Stellar testnet and pubnet CAIP-2 identifiers and USDC assets;
- the official `exact` facilitator scheme;
- MCP payment primitives suitable for the RFP's agent-facing discovery/payment interface.

It does **not** implement the grant-funded facilitator or Bazaar. Those remain the proposed SCF RFP deliverables.

```bash
npm ci
npm test
```

## 2.27.0 PR smoke gate (separate from the pinned baseline)

The repository's [pull-request CI](../../.github/workflows/test.yml) now adds a non-settling compatibility check for the npm-published **2.27.0** versions of `@x402/core`, `@x402/mcp`, and `@x402/stellar`. It starts with `npm ci` against the **unchanged 2.26.0 lockfile**, temporarily overlays aligned 2.27.0 packages without updating package/lock files, asserts the installed versions, and runs the existing readiness tests on Node 22.

**Evidence boundary:** A green PR smoke check verifies only the tested exports/network constants and MCP primitives on 2.27.0. It **does not** verify deployed facilitator routes, `/supported`, Stellar testnet/pubnet payments, `payload: {transaction}` wire compatibility, the Bazaar, `upto`, security audit, or the canonical x402 E2E suite. Those remain separate gates in [the SCF conformance matrix](../../grants/stellar-rfp-conformance.md). Do **not** relabel the previous pinned 2.26.0 test as proof that 2.27.0 passed unless the new CI job has actually completed successfully.

For a local equivalent with working npm registry access (without changing the tracked lockfile), run from this directory:

```bash
npm ci
npm install --no-save --package-lock=false --ignore-scripts @x402/core@2.27.0 @x402/mcp@2.27.0 @x402/stellar@2.27.0
npm test
```
