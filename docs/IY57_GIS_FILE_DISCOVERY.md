# IY57 GIS file discovery — 2026-09-17

## Evidence recovered

The archived Geoscience Australia Phase-2 README identifies NCI project `iy57` and states that the top-level `gis` directory contains derived geospatial datasets including contact locations, coverages, a data-holiday database, and generalised deep-tow/AUV tracklines. The Phase-2 dataset DOI is 10.4225/25/5B0CD2B84A2DC.

Historical catalogue root: `dapds00.nci.org.au/thredds/catalog/iy57/catalog.html`.

NCI documentation establishes the corresponding HTTP-file pattern as `.../thredds/fileServer/{FILE_ID}`. Therefore, once an exact `iy57/gis/...` file path is recovered from a catalogue/mirror, it can be converted mechanically to an HTTP download path; no filename guessing is permitted.

## Third-party repository audit

`mkmyhre/mh370-analysis-tool` was inspected as a possible mirror. It contains `src/data/data_holidays.json`, but those geometries are four deliberately approximate rectangles. Its own reviewer notes explicitly describe the data-holiday polygons as approximate rectangles. They MUST NOT be used as evidence-grade search polygons, candidate coordinates, or cell-level detection probability.

The same repository contains useful *derived* sonar coverage footprints extracted from the official AusSeabed WMS. Its README reports 43 AUV polygons, 2 deep-tow polygons and 12 DHJ/Go-Phoenix polygons. However, extraction uses a single rasterized GetMap plus morphological closing and ~0.02 degree simplification. This can erase precisely the small gaps/holidays relevant to residual-search inference. These footprints are therefore REFERENCE_NONAUTHORITATIVE and may be used only for debugging/coverage-envelope checks.

## Fail-closed rule

Do not create a spatial `P_D(L)` from:

1. approximate holiday rectangles;
2. aggregate ATSB holiday/LPD areas without geometry;
3. WMS alpha-mask polygons that have been morphologically closed/simplified;
4. 2025/26 Ocean Infinity area totals without exact tracks/polygons.

The next evidence gate remains recovery of the authoritative `iy57/gis` vector/database files or an official mirror exposing equivalent geometry.
