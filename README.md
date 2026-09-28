# Writer Retrieval Audit Data

Supporting aggregate data and arithmetic verification for **Auditing Self-Supervised Writer Retrieval: Metric Semantics, Provenance, and Shortcut Controls**.

This release contains eight sanitized JSON records, an archived evaluator excerpt, and a standard-library verification program. It preserves all numeric and Boolean values in the input records while removing operational and internal-workflow metadata.

## Verify

With Python 3.9 or newer, run:

```sh
python verify_correction.py
```

Expected output:

```text
PASS: 44551 rank-pair identities and all retained aggregate corrections verified
```

No GPU, model download, network connection, or third-party package is needed for this verification. `evaluator_excerpt.py` documents the historical defective logic; it is not a corrected evaluation implementation and should not be reused for new experiments.

## Contents

| Record in `raw/` | Contents |
| --- | --- |
| `derived_corrected_map.json` | Correction formula, protocol, and corrected aggregates |
| `salvage_results.json` | Controlled I-JEPA, C-JEPA, MAE, and VICReg aggregates |
| `dino_results.json` | Controlled DINO aggregates |
| `sota_color_4exec.json` | Four historical colour executions and archived summaries |
| `fullconfig_determinism.json` | Retained AMP/fp32 diagnostic rows |
| `pretrained_calibration.json` | Frozen pretrained encoder calibration |
| `pilot_results.json` | Erase-control pilot aggregates |
| `scramble_summary.json` | Two scramble-control execution rows |

See `DATA_NOTES.md` for interpretation and `SANITIZATION.md` for the release procedure. `SHA256SUMS.txt` records the SHA-256 checksum of each release file except itself.

## Scope and limitations

The package verifies the analytic correction and retained aggregate arithmetic. It does not reproduce model training or recover missing checkpoints, features, per-query scores, or per-seed controlled rows. Historical executions are not independent seed replicates. The retained precision records cannot establish a precision effect.

The local Historical-WI retrieval protocol is transductive and uses a subset of the training partition, not the official held-out test partition. Frozen-model calibration uses a different crop sampler and is an orientation reference only. Erase and scramble controls change multiple image properties and do not isolate a causal mechanism.

This repository distributes experiment aggregates and verification code. It does not redistribute the Historical-WI images, synthetic image corpus, pretrained weights, or trained checkpoints. No license for the original image dataset is granted here.
