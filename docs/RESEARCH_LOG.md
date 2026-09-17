# MH370 Research Log

## 2026-09-17 — V4 evidence audit

### Objective
Execute the adversarial research plan with primary-source verification before producing any new candidate search box.

### Primary-source findings verified

1. ATSB First Principles Review: updated independent SATCOM and drift analyses place the most likely impact close to the 7th arc, approximately within 25 NM, bounded roughly by 33S–36S. The 2016 residual area was approximately 25,000 km2.
2. The same report documents that deep-tow sonar achieved approximately 97% coverage. Residual limitations included terrain shadowing, terrain avoidance, equipment gaps, and Lower Probability of Detection (LPD) geology.
3. LPD areas could be excluded only with varying confidence, approximately 50–90%; about 35% had multiple sonar passes. Overall confidence within the then-current main search area was >95%.
4. Crucially, north of 36S the historical search width was not a complete ±25 NM corridor: ATSB states approximately 12–17 NM east and 10–21 NM west of the 7th arc had been searched, varying with latitude.
5. Geoscience Australia publicly released Phase One bathymetry and Phase Two high-resolution sidescan/multibeam sonar. Phase Two also contains derived GIS material including coverage, contacts, data holidays and generalized vehicle tracklines; the authoritative large datasets are hosted through GA/NCI.
6. CSIRO drift work identifies 36S–32S, especially near 35S, as the strongest drift-compatible segment. Part III gives a model maximum at 35.6S, 92.8E, with nearby alternatives. This is model-derived evidence, not a wreckage location.
7. Malaysia MOT states that the 2025/26 Ocean Infinity operation surveyed approximately 7,571 km2 within a new ~15,000 km2 search area and found no evidence confirming the wreckage location. The public MOT update does not provide cell-level/AUV-track geometry; this negative evidence must remain spatially unallocated until authoritative geometry is obtained.

### Important correction to V4 controlled-glide interpretation
Earlier ATSB search-area work considered maximum glide after fuel exhaustion and produced decreasing-priority widths out to 100 NM. Later evidence — final BFOs, flap configuration and simulations — shifted substantially more weight toward an impact close to the 7th arc, probably within 25 NM and in simulations often within ~15 NM. Therefore the 25–120 NM envelope is retained only as a low-prior sensitivity hypothesis, never as the baseline.

### Preliminary sensitivity test
A deliberately simplified proxy model was run only to test whether a controlled-glide prior by itself can move substantial probability outside 25 NM. It cannot be used as a final localization because it uses a local arc approximation and CSIRO-centered drift proxy rather than the published DSTG trajectory density and real GIS coverage.

For controlled-glide mixture priors of 1%, 5%, 10%, and 25%, the proxy retained approximately 96.0%, 94.0%, 91.7%, and 85.6% of probability respectively inside 25 NM. At 10% glide prior, about 7.1% fell in 25–50 NM, 1.1% in 50–80 NM, and 0.1% in 80–120 NM. This reinforces that far-glide territory is a sensitivity tail, not the dominant solution.

### Failed/invalid shortcut discovered
Applying a hand-drawn search mask from the published minimum/maximum search widths produces boundary artifacts and false posterior maxima. This method is rejected. Final search-negative evidence must use the actual Phase Two GIS coverage/holiday layers.

### Current blocker
The decisive missing input is not another theory. It is authoritative machine-readable geometry for search coverage and probability-of-detection, especially:
- GA Phase Two GIS coverage/data-holiday layers (available via GA/NCI but not yet ingested here),
- exact Ocean Infinity 2018 geometry if publicly obtainable,
- exact Ocean Infinity 2025/26 geometry (not present in the Malaysian public update found so far).

### Current scientific conclusion
No new coordinate is defensible yet. The highest-value unresolved problem is the intersection of the 33S–36S physics/drift corridor with actual low-Pd or unsearched seabed cells. A final candidate box must not be issued until that GIS intersection is computed.
