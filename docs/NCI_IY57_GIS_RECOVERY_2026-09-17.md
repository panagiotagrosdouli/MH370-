# NCI iy57 GIS recovery — 2026-09-17

## New evidence

Web-indexed archival material preserves the former NCI THREDDS Phase-2 README for project `iy57`. It states that the root contained `File_Links.txt` for bulk retrieval and that the `gis` directory contained derived geospatial datasets including contact locations, coverages, a data-holiday database, and generalised deep-tow/AUV tracklines.

Historical THREDDS root:
`https://dapds00.nci.org.au/thredds/catalog/iy57/catalog.html`

Historical README dataset URL:
`https://dapds00.nci.org.au/thredds/catalog/iy57/catalog.html?dataset=iy57/READ_ME.txt`

Historical root bulk-link mechanism: filter `File_Links.txt` by path/type and download the selected HTTPServer URLs.

## Runtime test

A direct request from the current execution container to:
`https://dapds00.nci.org.au/thredds/catalog/iy57/gis/catalog.xml`
failed at DNS resolution (`Temporary failure in name resolution`). Therefore no GIS bytes were retrieved in this run.

## Provenance rule

The archived README is discovery evidence for the existence and structure of the official GA/NCI GIS archive. It is NOT itself geometry. No coordinates, polygons, coverage classes, or detection probabilities may be inferred from the archived text.

The production posterior remains fail-closed until one of the following is obtained:
1. authoritative `iy57/gis` files or an official successor copy;
2. authoritative GA service exposing the same coverage/holiday features;
3. a cryptographically or metadata-verifiable mirror of those files.

## Recovery sequence

1. Recover `File_Links.txt` or the `iy57/gis` THREDDS catalogue from NCI/GA or an archival copy.
2. Filter for GIS/file-geodatabase/shapefile/KML/KMZ entries and preserve original filenames/checksums/metadata.
3. Inspect CRS; expected archive CRS families include WGS84 and UTM WGS84 zones 45S/46S, but determine CRS per file rather than assume it.
4. Convert losslessly to analysis GeoPackage/GeoJSON while preserving source attributes.
5. Separate final coverage, unresolved holidays, LPD, terrain/shadow/avoidance, AUV infill and generalized tracks.
6. Intersect only then with the authoritative 7th Arc and the 33–36°S physics/drift corridor.
7. Assign search non-detection likelihood from documented coverage classes; do not equate historical holiday status with final no-detection status.

## Current conclusion

We have identified the archive mechanism and exact GIS directory class, but have not yet recovered the vector geometry. No residual search coordinate is evidence-grade yet.