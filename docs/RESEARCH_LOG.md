# MH370 Research Log

## 2026-09-17 — V4 evidence audit

### Objective
Execute the adversarial research plan with primary-source verification before producing any new candidate search box.

### Primary-source findings verified

1. ATSB First Principles Review: updated independent SATCOM and drift analyses place the most likely impact close to the 7th arc, approximately within 25 NM, bounded roughly by 33S–36S. The 2016 residual area was approximately 25,000 km2.
2. The same report documents that deep-tow sonar achieved approximately 97% coverage. Residual limitations included terrain shadowing, terrain avoidance, equipment gaps, and Lower Probability of Detection (LPD) geology.
3. LPD areas could be excluded only with varying confidence, approximately 50–90%; about 35% had multiple sonar passes. Overall confidence within the then-current main search area was >95%.
4. Crucially, north of 36S the historical search width was not a complete ±25 NM corridor: ATSB states approximately 12–17 NM east and 10–21 NM west of the 7th arc had been searched, varying with latitude.
5. Geoscience Australia publicly released Phase One bathymetry and Phase Two high-resolution sidescan/multibeam sonar. Phase Two also contains derived GIS material including coverage, contacts, data holidays and generalized vehicle tracklines; the authoritative large datasets are hosted through GA/AusSeabed/NCI.
6. CSIRO drift work identifies 36S–32S, especially near 35S, as the strongest drift-compatible segment. Part III gives a model maximum at 35.6S, 92.8E, with nearby alternatives. This is model-derived evidence, not a wreckage location.
7. Malaysia MOT states that the 2025/26 Ocean Infinity operation surveyed approximately 7,571 km2 within a new ~15,000 km2 search area and found no evidence confirming the wreckage location. The public MOT update does not provide cell-level/AUV-track geometry; this negative evidence must remain spatially unallocated until authoritative geometry is obtained.

### Important correction to V4 controlled-glide interpretation
Earlier ATSB search-area work considered maximum glide after fuel exhaustion and produced decreasing-priority widths out to 100+ NM. Later evidence — final BFOs, flap configuration and simulations — shifted substantially more weight toward an impact close to the 7th arc. The First Principles Review states 99% of DST Group analysis outcomes lie within 25 NM east/west of the arc. Therefore the 25–120 NM envelope is retained only as a low-prior sensitivity hypothesis, never as the baseline.

### Preliminary sensitivity test
A deliberately simplified proxy model was run only to test whether a controlled-glide prior by itself can move substantial probability outside 25 NM. It cannot be used as a final localization because it uses a local arc approximation and CSIRO-centered drift proxy rather than the published DSTG trajectory density and real GIS coverage.

For controlled-glide mixture priors of 1%, 5%, 10%, and 25%, the proxy retained approximately 96.0%, 94.0%, 91.7%, and 85.6% of probability respectively inside 25 NM. At 10% glide prior, about 7.1% fell in 25–50 NM, 1.1% in 50–80 NM, and 0.1% in 80–120 NM. This reinforces that far-glide territory is a sensitivity tail, not the dominant solution.

### Failed/invalid shortcut discovered
Applying a hand-drawn search mask from the published minimum/maximum search widths produces boundary artifacts and false posterior maxima. This method is rejected. Final search-negative evidence must use the actual Phase Two GIS coverage/holiday layers.

## 2026-09-17 — Machine-readable GA dataset discovery

The authoritative machine-readable path was resolved further:

- GA Phase 2 raw/processed dataset: DOI `10.4225/25/5B0CD2B84A2DC`, GA id `120962`, >121,000 km² of high-resolution Phase 2 data.
- GA Phase 2 5 m visualisation dataset: DOI `10.4225/25/5B0CD3B139DEF`, GA id `120969`.
- Documented 5 m layers include `Fugro_DT_5m_WGS84`, `Fugro_AUV_5m_WGS84`, `DHJ_SAS_5m_WGS84`; Go Phoenix is the fourth Phase 2 layer and must be resolved from capabilities.
- GA/AusSeabed publishes current WMS and WCS services containing MH370 Phase 1 bathymetry and Phase 2 sonar.
- Phase 1 150 m bathymetry has a documented direct ~193.5 MB ZIP download.

A fail-closed ingestion utility (`src/ingest_ga_services.py`) was added. The local computation runtime could not resolve the AusSeabed host, while public web indexing could verify the service and layer metadata. No synthetic raster or inferred global-bounding-box coverage was substituted.

### Current blocker
The decisive missing input remains the actual raster/coverage bytes inside the computation runtime, plus authoritative Ocean Infinity 2018 and 2025/26 cell geometry where publicly obtainable. This is now an access/runtime blocker rather than a dataset-identification blocker.

### Current scientific conclusion
No new coordinate is defensible yet. The strongest supported residual domain is the intersection of the 32.5/33S–36S SATCOM/drift corridor, within roughly ±25 NM of the 7th arc, with genuinely unsearched or low-Pd seabed. ATSB explicitly reports that the older search north of 36S covered varying widths of only ~12–17 NM east and ~10–21 NM west, so residual strips existed historically. Exact modern residual cells cannot be ranked without the real coverage geometry, especially after later Ocean Infinity searches.
