# Phase-2 archive recovery stop-rule — 2026-09-18

## Search performed

Fresh public-index and GitHub searches targeted the exact archive primitives:
- iy57/gis
- data holiday database + iy57
- generalised tracklines + iy57
- iy57/File_Links.txt
- iy57/final_processed
- GP1500_6_Mission*

## Result

No new authoritative file inventory, GIS filename, File_Links payload, or mirrored final_processed row set was recovered.

The only substantive indexed archive evidence remains the historical reproduction of the Phase-2 README and exact historical THREDDS paths already recorded in this repository.

## Stop rule

Repeated public-index searches for these exact tokens are now considered saturated. They must not consume additional research cycles unless:
1. a new domain/archive/mirror appears;
2. an exact new filename/token is discovered;
3. live NCI/AusSeabed/ArcGIS access becomes available; or
4. a user-provided/connected dataset contains the missing inventory.

## Research pivot

The next computationally useful work should no longer be archive-string hunting. It should construct the residual-ranking engine so that authoritative geometry can be dropped in without redesign:
- official Arc geometry input;
- Phase-2 coverage-class polygons;
- unresolved holiday/LPD polygons;
- OI authoritative coverage when available;
- physics/drift/EOF surfaces;
- non-detection update and provenance gates;
- ablation/sensitivity outputs.

No coordinate is promoted while geometry gates remain unmet.
