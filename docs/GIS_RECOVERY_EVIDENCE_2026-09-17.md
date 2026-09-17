# Phase-2 GIS recovery evidence — 2026-09-17

## Result

Targeted web and GitHub searches did not recover an indexed copy of the authoritative `iy57/File_Links.txt` or the original Phase-2 holiday geodatabase filename. This is a negative retrieval result, not evidence that the archive no longer exists.

The strongest surviving archive description states that the NCI `iy57` dataset contained a top-level `gis` directory with derived geospatial datasets including **contact locations, coverages, a data-holiday database, and generalised deep-tow/AUV tracklines**. It also states that bulk download was intended to use the root `File_Links.txt` manifest.

Source discovered through web indexing:
- archived GA/NCI README reproduced at Allmystery, thread page 2628: https://www.allmystery.de/themen/gg110370-2627
- authoritative dataset DOI remains: 10.4225/25/5B0CD2B84A2DC

## Third-party geometry audit

The public `mkmyhre/mh370-analysis-tool` repository contains `src/data/data_holidays.json`, but this is **not** accepted as authoritative Phase-2 holiday geometry.

Its own project documentation describes the data-holiday polygons as approximate rectangles. Inspection confirms four coarse rectangular polygons, including a nominal LEP-slope rectangle from 93.6–94.1 E and 34.7–35.0 S. These geometries are therefore suitable only as visual/debug references and MUST NOT populate cell-level sonar probability of detection or residual-search rankings.

Rejected quantitative use:

```
third_party_approximate_holidays -> P_D(x)
```

Allowed use:

```
third_party_approximate_holidays -> visual cross-check / hypothesis debugging only
```

## Evidence gate

The search-negative-evidence gate remains closed until at least one of the following is recovered with provenance:

1. original GA/NCI Phase-2 GIS vectors/geodatabase;
2. an authoritative GA/ATSB derivative containing final coverage, unresolved holidays and/or LPD polygons;
3. a transport copy whose coordinates can be demonstrated to be byte-for-byte or geometrically equivalent to an authoritative source.

Do not infer `P_D=0` merely from an initial holiday. AUV infill and repeat passes must be represented where known.

## Current posterior rule

Until authoritative geometry is recovered:

`P(L | D, ND) ∝ P0(L) × L_drift(L) × L_EOF(L) × L_search(L)`

but `L_search(L)` must remain unallocated at cell level wherever only approximate/non-authoritative geometry is available. Ocean Infinity 2025/26 coverage also remains spatially unallocated without public exact AUV/coverage geometry.

## Retrieval target

Highest-value exact targets remain:

- `iy57/File_Links.txt` / `File_links.txt`
- `iy57/gis/*`
- filenames containing `holiday`, `coverage`, `trackline`, `contact`
- Esri file geodatabase (`.gdb`) or equivalent exported vectors

No wreckage location is claimed by this evidence audit.