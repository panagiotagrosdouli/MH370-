# MH370 Analysis State — 2026-09-18

## Current evidence-backed state

This repository does **not** claim a wreckage location.

The most defensible residual domain remains the intersection of:
- the official 7th Arc;
- the approximately 33S–36S SATCOM/drift corridor;
- a close-to-arc end-of-flight envelope;
- genuine low-probability-of-detection or unsearched seabed.

## New verification completed

### Official 7th Arc
The official Geoscience Australia / ATSB ArcGIS service is:
`7thArc_SingleLine`, service item `4c94d33cfc144f7d8b78943dee56e29b`, spatial reference EPSG:4326.
The service description states that independent satellite-communications and aircraft-performance analysis places MH370 in close proximity to the 7th Arc.

### Phase-2 sonar source
The current AusSeabed portal explicitly exposes MH370 Phase 2 data and its user guide documents an **MH370 Database Search** tool for spatially querying and downloading the full Phase-2 collection stored on NCI.

Authoritative Phase-2 raw/processed record:
- DOI: `10.4225/25/5B0CD2B84A2DC`
- GA dataset id: 120962
- >121,000 km2 high-resolution data
- acquisition period: 2014-09-01 to 2017-01-31

The 5 m visualisation product is useful for coverage-envelope checks but is not sufficient for small-gap / holiday inference; GA recommends the raw/processed product for detailed interrogation.

### Public WMS-derived coverage
A public reproducible implementation has identified live AusSeabed WMS layer names for:
- AUV side-scan sonar, 5 m;
- deep-tow side-scan sonar, 5 m;
- DHJ synthetic-aperture sonar, 5 m;
- Phase-1 bathymetry, 150 m.

Its published derived polygons are **reference-only** because the method rasterises a broad WMS GetMap, applies morphological closing, filters small contours, then simplifies polygons by about 0.02 degrees (~2 km). That process can erase precisely the small holes relevant to residual-search inference.

Therefore:
- WMS-derived polygons may define coarse searched-envelope geometry;
- they must not be interpreted as authoritative cell-level detection probability;
- original GA/NCI holiday/LPD geometry remains required for final negative-evidence likelihood.

## Critical pipeline defect identified

`src/build_residual_grid.py` currently creates a latitude × cross-arc proxy lattice and does not transform official 7th-Arc geometry into real latitude/longitude cells.

`src/rank_residual_cells.py` already expects real `lat,lon` rows.

Until this mismatch is removed, no ranked output should be called a spatial wreckage candidate.

## Required computation sequence

1. Fetch official 7th Arc GeoJSON in EPSG:4326.
2. Restrict it to the 33S–36S corridor.
3. Densify the line geodesically.
4. Generate cross-track destination points for the accepted end-of-flight envelope.
5. Attach physics/drift/EOF likelihoods without double-counting DSTG evidence.
6. Overlay authoritative GA Phase-2 coverage/holiday/LPD geometry.
7. Keep Ocean Infinity 2025/26 negative evidence neutral unless exact coverage geometry becomes public.
8. Rank only then.

## Evidence gate

A coordinate becomes reportable only as a **model candidate**, never as a discovery, after the real-geometry pipeline passes. Physical discovery still requires sonar/ROV/recovery confirmation.
