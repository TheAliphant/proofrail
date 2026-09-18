# Base / x402 verification

ProofRail separates payment-route validation from settlement proof. A valid x402 challenge shows where and how a resource expects payment; it does **not** prove payment occurred.

```bash
proofrail x402-verify https://example.com/challenge --network eip155:8453
```

For a real Base USDC settlement, verify the transaction receipt against the expected token, recipient and exact base-unit amount:

```bash
proofrail evm-verify "$BASE_RPC" 0xTRANSACTION_HASH \
  --chain-id 8453 \
  --token 0xTOKEN \
  --pay-to 0xRECIPIENT \
  --amount 250000
```

A verifier checks `eth_chainId`, transaction success, ERC-20 `Transfer` topic, token contract, recipient and amount. The resulting evidence can then be attached to a ProofRail receipt. No private key is required for verification.
