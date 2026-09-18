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
