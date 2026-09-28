# Data notes

## Logged versus corrected retrieval scores

The original evaluator ranked each query last but counted it as an additional relevant item. For the retained protocol, the corrected leave-one-out mAP is `1.5 * logged_mAP - 0.005`; the corresponding standard deviation is multiplied by `1.5`.

Values in `derived_corrected_map.json` are corrected values or explicitly labelled logged values. Other records retain historical logged metrics. No numbers have been recomputed or silently replaced during sanitization. Numeric metadata, including writer/page counts, seeds, model dimensions, training steps, batch sizes, and elapsed seconds, is retained.

## Statistical units

- Controlled records store mean and standard deviation over three seeds; per-seed rows are not available.
- The colour history contains four execution records, including two with nominal seed zero. Complete configurations are unavailable, so these are not four independent seed replicates.
- Precision data contain two identical AMP rows of unknown independence and one fp32 row per method.
- Pilot `auc_*_mean_std` fields contain mean and standard deviation, not token-level confidence intervals.
- Scramble data contain two rows. Columns 1-3 are learned-score, pixel-variance, and random-score AUC; columns 5-6 are destroyed-token and total-token counts. Other historical diagnostic columns are preserved, but are not used by the paper's reported AUC comparison and are not assigned undocumented meanings here.

Historical strings and summary fields are retained where they describe measurements; they are not new scientific conclusions. In particular, low-effective-rank annotations do not establish general model collapse, and published specialist scores are not directly comparable to this protocol. Consult the paper for the bounded interpretations.

## Data provenance

The real-document experiments use the ICDAR 2017 Historical Writer Identification (Historical-WI) training partition. Erase/scramble experiments also include generated manuscript-like data. A frozen pretrained vision encoder is used as a calibration reference. The public record keeps scientific dataset and model names, source-code fingerprints, and experimental values, without the original operational locations.
