# SATCOM physics evidence contract — 2026-09-18

The project now enforces two mutually exclusive physics routes.

Route A — DSTG_POSTERIOR:
Use a digitised/reproduced DSTG spatial density as the combined physics input. Do not multiply it again by raw BTO or BFO likelihoods.

Route B — RAW_SATCOM:
Reconstruct the SATCOM likelihood independently from raw BTO/BFO plus satellite/ground-station geometry, calibration terms, aircraft dynamics and required meteorology. Do not multiply the result by DSTG density.

This prevents evidence double counting.

The DSTG Bayesian analysis is not a bare BTO likelihood. Its published methodology uses Bayesian trajectory modelling with aircraft dynamics and satellite communications measurements, with calibration/model-error treatment. Therefore DSTG density belongs on the physics side as an already-integrated model product.

The current repository does not yet contain an evidence-grade digitisation of the DSTG posterior and does not claim a complete raw SATCOM reconstruction. Existing Gaussian latitude proxies remain non-evidence-grade.

The guard script rejects files that contain DSTG density together with BTO/BFO/raw-SATCOM likelihood columns in DSTG mode, and rejects DSTG density in RAW_SATCOM mode.
