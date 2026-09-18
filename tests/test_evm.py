import unittest
from proofrail.adapters.evm import TRANSFER_TOPIC, verify_erc20_transfer

TOKEN="0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
PAY="0x1111111111111111111111111111111111111111"

def topic_address(addr): return "0x" + "0"*24 + addr.lower().removeprefix("0x")

class EVMTests(unittest.TestCase):
    def test_transfer_match(self):
        receipt={"status":"0x1","logs":[{"address":TOKEN,"topics":[TRANSFER_TOPIC,topic_address("0x2222222222222222222222222222222222222222"),topic_address(PAY)],"data":hex(250000),"logIndex":"0x2"}]}
        ok, errors, match=verify_erc20_transfer(receipt,token=TOKEN,pay_to=PAY,amount_base_units=250000)
        self.assertTrue(ok, errors); self.assertEqual(match["amount_base_units"],250000)

    def test_wrong_recipient(self):
        receipt={"status":"0x1","logs":[{"address":TOKEN,"topics":[TRANSFER_TOPIC,topic_address("0x2222222222222222222222222222222222222222"),topic_address("0x3333333333333333333333333333333333333333")],"data":hex(250000)}]}
        ok, errors, _=verify_erc20_transfer(receipt,token=TOKEN,pay_to=PAY,amount_base_units=250000)
        self.assertFalse(ok); self.assertIn("matching_transfer_not_found",errors)

if __name__ == "__main__": unittest.main()
