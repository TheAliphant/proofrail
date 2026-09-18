import unittest
from proofrail.adapters.x402 import verify_challenge

CHALLENGE = {
    "scheme": "exact", "network": "eip155:8453",
    "requirement": {"scheme": "exact", "network": "eip155:8453",
                    "amount": "250000", "asset": "0xUSDC", "payTo": "0xPAY"}
}

class X402Tests(unittest.TestCase):
    def test_valid(self):
        ok, errors = verify_challenge(CHALLENGE, network="eip155:8453", amount="250000")
        self.assertTrue(ok, errors)

    def test_wrong_amount(self):
        ok, errors = verify_challenge(CHALLENGE, amount="1")
        self.assertFalse(ok)
        self.assertIn("amount_mismatch", errors)

if __name__ == "__main__": unittest.main()
