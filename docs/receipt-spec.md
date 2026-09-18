# Receipt spec v0.1

Required fields: `version`, `job_id`, `worker`, `artifact_hash`, `qa_status`, `created_at`, `receipt_hash`.

Optional fields: `provider`, `buyer`, `task_hash`, `submission_ref`, `payment`, `metadata`.

`receipt_hash` is SHA-256 over canonical JSON of every field except `receipt_hash` itself. Canonical JSON uses lexicographically sorted keys, UTF-8, no insignificant whitespace.

`payment` is adapter-defined but SHOULD include `network`, `asset`, `amount`, `transaction_ref` and `verification_status` when available.

A verifier MUST fail if the receipt hash differs. Network-specific verification is additive: a valid core receipt does not by itself prove an external payment occurred.
