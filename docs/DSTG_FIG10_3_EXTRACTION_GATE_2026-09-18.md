# DSTG Figure 10.3 extraction gate — 2026-09-18

A fresh public-index search did not recover a trustworthy vector/table representation of the Figure 10.3 BTO+BFO curve. Search results were dominated by unrelated documents and do not justify fabricating curve samples.

Therefore the project records a hard extraction gate:

- ACCEPT: original ATSB/DSTG PDF vector path, embedded figure object, or calibrated manual digitisation from the original PDF.
- REJECT: search-engine thumbnails, third-party redraws, guessed peak coordinates, Gaussian fits chosen by eye, or values copied from unrelated web snippets.
- REQUIRED metadata per point: latitude_deg, relative_frequency, panel=BTO_BFO, source_page, provenance, extraction_method.
- REQUIRED validation: monotonic x-axis calibration check; y=0 baseline check; at least two independent axis control points; overlay residual inspection; normalization only after extraction.

The existing digitisation runner remains ready but no numerical curve is committed until one of the accepted extraction routes succeeds.

Current conclusion: the Gaussian latitude proxy is still not evidence-grade, but replacing it with invented Figure 10.3 samples would be worse. Status remains BLOCKED_ON_SOURCE_RENDERING.
