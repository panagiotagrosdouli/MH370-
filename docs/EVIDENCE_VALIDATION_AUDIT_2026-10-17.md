# MH370 evidence gate and ranking audit — 17 October 2026

## Scope and status

This is a reproducibility and safety-engineering improvement, **not a new MH370 localization**. The official ATSB 2016 First Principles Review described a then-priority ~33°S–36°S region within approximately 25 NM of the seventh arc, approximately 25,000 km². The CSIRO drift work broadly favoured 32°S–36°S, particularly near 35°S. These are **historical scientific assessments** and do not identify today's unsearched cells.

The Malaysian Ministry of Transport's 2025/26 update states ~7,571 km² of seabed was surveyed in 28 operational days without confirming the wreckage. That aggregate area is **not a spatial detection mask**. Further search was enabled by the agreement extension to 30 June 2027, but no specific new survey footprint is assumed here.

## Source registry

| Authority | Source | Source URL | Data or assertion | Units / CRS | Evidence limits |
|---|---|---|---|---|---|
| ATSB | First Principles Review, 20 December 2016 | https://www.atsb.gov.au/investigations/ae-2014-054 | Historical preferred search area close to seventh arc, ~33°S–36°S | decimal degrees WGS84, NM, km² | Not present-day residual ranking |
| CSIRO via ATSB | MH370 ocean drift reports, 2016–2017 | https://www.atsb.gov.au/csiro-mh370-drift-reports | Drift compatibility ~32°S–36°S | latitude degrees | Model-dependent; not independent of the imported anchor |
| Geoscience Australia | Phase Two data release, 28 June 2018 | https://www.ga.gov.au/news/news-archive/the-data-behind-the-search-for-mh370-phase-two-data-released | Underwater sonar source documentation | sonar coverage / survey footprints; source CRS varies | Raw search geometry is not bundled into this audit |
| Malaysia MOT | MH370 Search Operation 2025/26, update to families | https://www.mot.gov.my/en/Kenyataan%20Media/Year%202026/MH370%20Search%20Operation%202025-2026%20-%20Update%20to%20Families.pdf | ~7,571 km² surveyed; no confirmed discovery | km² | No cell-level tracks in the cited update |
| Bernama / Malaysian government reporting | Agreement extension, 29 June 2026 | https://www.bernama.com/en/news.php?id=2574438 | Extension to 30 June 2027 | calendar dates | No geometry or sonar probability supplied |

Public sources checked on 17 October 2026. Do not interpret source publication dates as survey dates.

## Confirmed repository-level problems

1. `src/baseline_posterior.py` explicitly uses (-35.6, 92.8) as a **CSIRO-derived input anchor**, and later reports a posterior mode. This is not an independent localization. Its soft Gaussian likelihoods and WSPR-centered hard-coded geometry are proxy choices.
2. `src/build_residual_grid.py` outputs `lat` + `cross_arc_nm` but **no longitude**; it cannot be passed to a real geographical residual-cell ranker. The more appropriate geodesic builder is `src/build_geodesic_arc_grid.py`, conditioned on fetching the authoritative 7th Arc.
3. The earlier `src/rank_residual_cells.py` could attempt to compute scores from missing `pd_atsb_ga`, did not require an explicit validation gate, and normalized raw scores **without cell area**. For non-equal geographic cells this can distort posterior mass.
4. The pre-existing public search evidence documentation warns that authoritative coverage/holiday/LPD geometry is missing. Unknown 2025/26 Ocean Infinity footprints must remain unallocated.

## Code change

`src/rank_residual_cells.py` now demands explicit WGS84 coordinates, positive cell area, finite nonnegative likelihood factors, mandatory ATSB/GA probability of detection, and `evidence_gate=AUTHORITATIVE_GIS_VALIDATED`. Optional Ocean Infinity Pd may be empty (neutral). Invalid inputs fail before generating output.

**The gate string is not external validation by itself.** The operator must separately document provenance, polygon intersections, search coverage quality, model assumptions and independence of evidence families.

The area-weighted score approximates a posterior *cell mass* when likelihood factors represent spatial densities. Ensure grid topology has no overlaps/duplicate cells and units are consistent. Evidence correlations remain unresolved.

## Highest value next computation

Obtain official Phase-2 raw/processed spatial coverage and data-holiday geometry (and Ocean Infinity coverage where available). Intersect against cells generated from authoritative seventh-arc GeoJSON, then justify local Pd by sonar quality. Only after end-to-end source verification and ablation should cells be eligible for scientific ranking.

**No new geographic coordinate is defended or released by this audit.**
