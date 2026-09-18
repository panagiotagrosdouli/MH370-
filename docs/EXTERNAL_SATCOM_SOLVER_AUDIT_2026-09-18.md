# External SATCOM solver audit — 2026-09-18

A public independent repository, mkmyhre/mh370-analysis-tool, was inspected as an adversarial/reproducibility reference. It contains source-attributed SATCOM datasets, a solver, satellite-state inputs, candidate paths and derived search layers.

## Potentially reusable material

Its DATA-GUIDE documents machine-readable handshake fields including raw/corrected BTO, BFO, channel, usability flags, BTO sigma, satellite/AFC corrections and source attribution. It also documents model constants and satellite state vectors. These are useful as an independent implementation benchmark and as discovery pointers back to primary DSTG/ATSB/Inmarsat sources.

## Evidence rule

None of those independent outputs become baseline evidence merely because they are computationally sophisticated. Before reuse, every numeric input must be cross-checked against the cited primary source, and solver output must be compared with DSTG reference behaviour.

The repository's own derived sonar coverage is explicitly approximate WMS raster extraction, and its coarse holiday rectangles failed our geometry audit. Therefore SATCOM code/data and sonar/search geometry from the same repository receive different evidentiary treatment.

## Benchmark protocol

1. Recover primary-source SATCOM rows for arcs 1–7.
2. Compare raw and corrected BTO values event-by-event.
3. Compare BFO values and usability caveats.
4. Compare BTO/BFO noise assumptions.
5. Compare satellite state/ephemeris inputs.
6. Run the independent solver and compare seventh-arc/path-density behaviour with official DSTG published products.
7. Treat disagreement as an audit target, not choose whichever result is preferred.

## Important semantic guard

If the independent solver reconstructs raw SATCOM likelihood, it belongs to RAW_SATCOM route B. Its result must not be multiplied by DSTG posterior as independent evidence.

Status: INDEPENDENT_SOLVER_IDENTIFIED / PRIMARY_INPUT_CROSSCHECK_PENDING.
