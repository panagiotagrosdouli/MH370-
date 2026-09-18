# Phase-2 coordinate-first recovery pivot — 2026-09-18

## Why the retrieval strategy changes

The archived official Phase-2 README says that not all files were searchable through the historical DB Query Search by Area. Files that could not be represented spatially, or required specialised readers, could be absent from that spatial frontend and had to be accessed through NCI THREDDS.

At the same time, the official AusSeabed SQL schema shows that final_processed rows were designed to carry both source URI and EPSG:4326 geometry.

Therefore the correct recovery order is coordinate-first, not filename-first.

## Two authoritative data classes

A. Spatially indexed products
- query by AOI/geometry;
- recover path/name/URI;
- inspect the source product;
- use geometry only according to documented semantics.

B. Non-spatial/special-reader products
- recover through File_Links/THREDDS catalogue;
- use filenames as retrieval keys only;
- require embedded or sidecar georeferencing before spatial use.

## Target AOI

The project target remains the official end-of-flight envelope intersected with approximately 33–36S. The AOI must ultimately be constructed from the authoritative 7th-arc geometry plus the verified 27.5 NM west / 25 NM east cross-arc limits, rather than a rectangular longitude guess.

## Immediate recovery targets

1. Restore/query a spatial catalogue capable of exposing final_processed geometry + URI.
2. Recover cached historical DB-Query/Search-by-Area metadata.
3. Recover File_Links.txt only for products omitted from spatial indexing.
4. Recover iy57/gis coverage/data-holiday objects as the preferred direct negative-evidence layer.

## Important distinction

An exact Mission### product filename is useful for provenance but is not itself a coordinate. Repeating filename searches cannot rank residual cells.

This closes the filename-first branch and moves the project back to geometry-first retrieval.
