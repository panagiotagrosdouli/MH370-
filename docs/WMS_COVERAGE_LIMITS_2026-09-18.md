# AusSeabed WMS coverage — use and limits

The current AusSeabed portal publicly lists MH370 Phase 2 5 m data and the portal guide documents the MH370 Database Search tool for querying/downloading the Phase-2 collection on NCI.

A reproducible public extraction script currently uses these WMS layers:
- AUV SSS 5 m
- Deep Tow SSS 5 m
- DHJ SAS 5 m
- Southern Indian Ocean MH370 bathymetry 150 m

This is valuable discovery evidence because it confirms layer naming and an accessible visualization path.

However, the derived public coverage polygons are generated from a single large WMS raster mask, with:
- alpha/non-transparent pixel classification;
- morphological closing;
- minimum contour-size filtering;
- ~0.02 degree sonar-polygon simplification.

Those transformations can remove small holes and merge adjacent swaths. Therefore this repository classifies the polygons as:

`REFERENCE_COVERAGE_ENVELOPE_ONLY`

They must not be used as:
- data-holiday geometry;
- Lower Probability of Detection geometry;
- cell-level Pd;
- proof that a small region was or was not adequately searched.

Final search-negative evidence requires the authoritative GA/NCI raw/processed / GIS products or an official equivalent derivative.
