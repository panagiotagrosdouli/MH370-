# Phase 2 GIS archive breakthrough

Date: 2026-09-17

## Finding

The Phase 2 raw/processed archive documentation for NCI project `iy57` explicitly describes a top-level `gis` directory containing derived geospatial datasets including:

- contact locations
- sonar coverages
- a **data holiday database**
- generalised tracklines of deep-tow and AUV vehicles

This is the exact evidence class required for the residual-search calculation. It means the authoritative archive is not limited to raster sonar mosaics; vector/derived GIS products were included in the Phase 2 collation.

Authoritative dataset DOI: `10.4225/25/5B0CD2B84A2DC` (Governments of Australia, Malaysia and the People's Republic of China / Geoscience Australia, 2018).

Historical NCI catalogue root: `dapds00.nci.org.au/thredds/catalog/iy57/catalog.html`.

## Detection model correction from ATSB final operational report

ATSB Figure 73 gives a useful evidence-grade three-class interpretation of the final search coverage:

- High Confidence Coverage: 97.4% of combined area, defined as >95% confidence of detection.
- Lower Confidence Coverage: 2.1%, approximately 70% confidence of detection on average.
- Data Gaps: 0.5%, zero confidence of detection.

These values are aggregate calibration constraints, not permission to assign the same Pd to every individual polygon. Cell-level Pd must inherit the actual geometry and category from the GIS archive.

For residual posterior work:

`P(x | D, ND) ∝ P0(x) * (1 - Pd(x))`

with categorical conservative bounds rather than invented precision.

## AUV infill evidence

The vessel summary report gives the combined AUV campaign outcome as approximately:

- 77.60% of targeted holidays filled with good AUV data
- 18.99% converted to LPD after AUV acquisition
- 2.84% no change
- 0.57% reduced below the 100 m holiday criterion

Therefore an original data-holiday map is not a final residual map. The solver must use final/post-infill status where available.

## Important scale criterion

ATSB reports that filtering gaps/LPD below 200 m × 200 m removes many individual features, and notes historical aircraft debris fields are typically larger than this scale. We will retain small features in the raw ingest for auditability but flag them separately instead of treating every tiny gap as an equal candidate wreckage region.

## Provenance rule

A third-party reconstructed `data_holidays.geojson` may be used only for debugging or cross-checking. It must not enter the evidence-grade posterior when the authoritative Phase 2 GIS database can be recovered.

## Remaining technical blocker

The current execution environment cannot resolve the historical NCI THREDDS host reliably. The next acquisition target is therefore the actual contents of `iy57/gis` through an active NCI/GA mirror, catalogue endpoint, archived catalogue, or official spatial-data service. No polygon coordinates are fabricated while that acquisition remains incomplete.

## Consequence

The primary missing object is now sharply specified: the authoritative Phase 2 GIS **data holiday database plus final coverage/infill geometry**. Once ingested, intersect it with the official 7th Arc / physics-drift corridor and rank surviving cells using non-detection likelihood.