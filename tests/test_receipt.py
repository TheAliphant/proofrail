import unittest
from proofrail.receipt import create_receipt, verify_receipt

class ReceiptTests(unittest.TestCase):
    def test_round_trip(self):
        r = create_receipt(job_id="job-1", worker="agent:test", artifact_hash="sha256:abc", qa_status="PASS")
        ok, errors = verify_receipt(r)
        self.assertTrue(ok, errors)

    def test_tamper_detection(self):
        r = create_receipt(job_id="job-1", worker="agent:test", artifact_hash="sha256:abc", qa_status="PASS")
        r["job_id"] = "job-2"
        ok, errors = verify_receipt(r)
        self.assertFalse(ok)
        self.assertIn("receipt_hash_mismatch", errors)

if __name__ == "__main__": unittest.main()
