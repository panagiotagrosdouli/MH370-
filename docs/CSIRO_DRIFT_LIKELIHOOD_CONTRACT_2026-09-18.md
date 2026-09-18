# CSIRO drift likelihood contract — 2026-09-18

The Gaussian drift proxy is now prohibited as an evidence-grade input.

Official ATSB/CSIRO material supports a broad 36–32S prospective segment, with the region near 35S more consistent with the combined debris observations, surface-search non-detections, lack of Western Australian debris, and African arrival timing. CSIRO explicitly says other locations cannot be ruled out, including the 33–32S shoulder.

A critical dependency split is required:
- DEBRIS_ONLY: debris drift + arrival timing + surface-search/Australian non-detection evidence.
- PLEIADES_CONDITIONED: Part III evidence that additionally conditions on possible objects in March-2014 satellite imagery.

The Part-III ~35.6S,92.8E result must NOT be multiplied as an independent likelihood on top of the debris-only CSIRO likelihood because Part III inherits earlier drift evidence and adds the imagery constraint.

Part IV also warns that its earlier surface-search treatment followed parcels through search boxes and used day-dependent assumed detection probabilities; it was not an item-by-item exact detection model. Therefore the project must not turn the published figures into falsely precise per-cell probabilities.

The new runner accepts only explicit source-derived latitude support values with evidence-family and provenance metadata. It normalises them without imposing a Gaussian shape. No numerical support table is committed until the official report figures/tables can be extracted reproducibly.

Status: DRIFT_PROXY_RETIRED_FOR_EVIDENCE_GRADE_USE / NUMERIC_EXTRACTION_PENDING.
