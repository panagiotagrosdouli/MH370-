# MH370 Computational Search

Reproducible evidence-synthesis project for estimating a **geographic posterior probability distribution** for the likely MH370 wreckage field.

## Goal

Estimate

\[
P(L\mid D)
\]

where `L` is the candidate main-wreckage location and `D` is the set of reliable observations.

This repository does **not** claim that MH370 has been found. It is intended to reduce the physical search area while preserving uncertainty and avoiding confirmation bias.

## Baseline evidence policy

- **A — Direct measurements:** radar/SATCOM observations and directly identified debris.
- **B — Official model-derived evidence:** ATSB/DSTG trajectory inference, CSIRO drift modelling, end-of-flight analyses.
- **C — Contextual evidence:** e.g. simulator material. Excluded from the baseline posterior.
- **D — Experimental/unvalidated:** e.g. WSPR proposals. Excluded from the baseline posterior.

## Current baseline

The current evidence-synthesis model concentrates the principal search corridor near the 7th Arc, broadly around **33°S–36°S**, with strong ocean-drift interest near ~35°S. A current proxy model has a mode near **35.6°S, 92.8°E**, but that coordinate is **not a discovery claim** and is influenced by the official CSIRO drift result.

The main unresolved problem is to combine the physical posterior with **cell-level probability of detection** from historical sonar/AUV coverage:

\[
P_{remaining}(L) \propto P_{physics}(L)\prod_k[1-P_{D,k}(L)]
\]

The highest-value next target is therefore not simply the old maximum, but any **high-posterior / low-detection-probability residual cell**.

## Repository structure

- `docs/METHODOLOGY.md` — modelling design and anti-double-counting rules.
- `docs/SOURCES.md` — primary official/scientific source registry.
- `src/baseline_posterior.py` — reproducible baseline grid model.
- `data/README.md` — data provenance and artifact notes.

## Scientific safeguards

1. No invented radar coordinates.
2. No zero-width Inmarsat arcs.
3. No fixed single fuel-burn rate.
4. No double-counting DSTG inputs as independent likelihoods.
5. WSPR and simulator evidence remain outside the baseline model.
6. Previously searched areas are not automatically assigned zero probability.
7. A point estimate is never reported without a credible region and model assumptions.

## Status

Current stage: evidence synthesis + search-negative-evidence reconstruction. The next major upgrade is ingestion of official Geoscience Australia/ATSB sonar and bathymetry coverage to build a spatial `P_detection(x,y)` layer, followed by updated posterior and ablation tests.
