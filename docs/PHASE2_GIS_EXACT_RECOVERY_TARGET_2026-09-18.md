# Authoritative Phase-2 GIS recovery target — 2026-09-18

## What is now established

ATSB's operational report says data holidays were collated and grouped into polygons specifically so AUVs could acquire missing Deep-Tow coverage. The holiday mechanisms include acoustic shadow, off-track gaps, equipment failure, and terrain avoidance.

GA's 2022 review independently confirms that Phase-2 holiday/LPD geometry exists and reports a local accounting of 72.79 km2 in the reviewed footprint.

Historical archive metadata identifies the Phase-2 'gis' collection as containing derived geospatial datasets including coverages, a data-holiday database, contact locations, and generalized Deep-Tow/AUV tracklines. This archive description is discovery evidence until the original GIS bytes are recovered.

## Exact artifact priority

The next highest-value missing artifact is not another sonar image. It is the authoritative Phase-2 GIS holiday/coverage database itself, or an exact export of its polygon layers with attributes.

Recovery order:
1. original iy57/gis geodatabase or shapefile package;
2. authoritative GA/AusSeabed spatial-query export of the same layers;
3. authoritative raster-derived polygons only if layer equivalence can be demonstrated;
4. no hand-drawn reconstruction.

## Acceptance tests

A recovered layer is evidence-grade only if:
- CRS is explicit or recoverable from authoritative metadata;
- geometry is polygon/multipolygon for coverage/holidays;
- feature attributes preserve mechanism/class where available;
- provenance resolves to GA/ATSB Phase-2 material;
- geometry validity passes;
- aggregate area/count can be reconciled against official reports within projection/tolerance limits.

Generalised vehicle tracklines are useful for audit but are not sonar coverage polygons and must not be substituted.

## Computational consequence

Once recovered, intersect authoritative polygons with the official 7th-arc corridor and the physics/drift/EOF grid. Only then run residual-polygon ranking.

Status: EXACT_MISSING_ARTIFACT_IDENTIFIED / AUTHORITATIVE_BYTES_NOT_YET_RECOVERED.
