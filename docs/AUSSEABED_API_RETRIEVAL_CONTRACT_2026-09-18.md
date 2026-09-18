# AusSeabed MH370 API retrieval contract — 2026-09-18

Official AusSeabed source code defines the MH370 PostGIS schema and a product named Visualisation and Coverage Summaries with vis_summary, vis_summary_bundle, vis_summary_geoms and iy57/ provenance.

Spatial filtering uses ST_Intersects against EPSG:4326 WKT. Feature retrieval serializes stored geometry as GeoJSON. File retrieval resolves matching bundles to original file names, URIs and sizes.

Retrieval chain:
AOI -> intersecting catalogue geometries -> matching bundles -> original source files -> semantic inspection.

Critical rule: catalogue/index geometry is not sonar Pd. A returned vis_summary geometry is CATALOGUE_INDEX_GEOMETRY_NOT_PD until the linked source file is inspected and shown to encode coverage-confidence, holiday, LPD, or equivalent search semantics.

The official test suite also exercises populated MH370 catalogue records, including geometry-linked Go Phoenix products. This is evidence that the API implementation targets a populated catalogue rather than merely defining an empty schema.

Next target: query Visualisation and Coverage Summaries over the official 33–36S arc envelope, recover matching source-file names/URIs, then inspect candidate GIS/coverage products.
