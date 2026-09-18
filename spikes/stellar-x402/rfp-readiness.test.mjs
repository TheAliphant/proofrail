import test from "node:test";
import assert from "node:assert/strict";
import {
  ExactStellarScheme,
  STELLAR_TESTNET_CAIP2,
  STELLAR_PUBNET_CAIP2,
  USDC_TESTNET_ADDRESS,
  USDC_PUBNET_ADDRESS,
} from "@x402/stellar";
import { ExactStellarScheme as FacilitatorExact } from "@x402/stellar/exact/facilitator";
import {
  createToolResourceUrl,
  createx402MCPClient,
  wrapMCPClientWithPayment,
} from "@x402/mcp";

test("official Stellar x402 package exposes both required networks", () => {
  assert.match(STELLAR_TESTNET_CAIP2, /^stellar:/);
  assert.match(STELLAR_PUBNET_CAIP2, /^stellar:/);
  assert.notEqual(STELLAR_TESTNET_CAIP2, STELLAR_PUBNET_CAIP2);
  assert.ok(USDC_TESTNET_ADDRESS);
  assert.ok(USDC_PUBNET_ADDRESS);
});

test("facilitator exact scheme is available from official package", () => {
  assert.equal(typeof ExactStellarScheme, "function");
  assert.equal(typeof FacilitatorExact, "function");
  assert.equal(ExactStellarScheme.name, "ExactStellarScheme");
  assert.equal(FacilitatorExact.name, "ExactStellarScheme");
});

test("official MCP package exposes agent-payment primitives", () => {
  assert.equal(typeof createToolResourceUrl, "function");
  assert.equal(typeof createx402MCPClient, "function");
  assert.equal(typeof wrapMCPClientWithPayment, "function");
});
