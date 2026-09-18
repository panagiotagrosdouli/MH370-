# AusSeabed MH370 API breakthrough — 2026-09-18

## Finding

The AusSeabed open-source `product-catalogue` repository contains the implementation of the public MH370 Database Search API. This is a stronger and more direct discovery path than reconstructing the retired NCI THREDDS catalogue.

Production API documented by AusSeabed:
`https://mh370-api.ausseabed.gov.au`

Documented routes:
- `GET /products`
- `GET /products/:id`
- `GET /products/:id/query`
- `GET /products/:id/download-url-list`
- `GET /products/:id/features`

The API is documented by its own README as publicly accessible.

## Database structure

The backend uses PostgreSQL/PostGIS schema `marine_mh370`. Product families include:
- Bathymetry
- Backscatter
- Hillshade
- Sidescan
- Sub-bottom Profile
- Water Column
- Camera
- Sound Velocity Profile
- Unprocessed Multibeam
- Unprocessed Sidescan
- Navigation
- Visualisation and Coverage Summaries
- Phase 1 Data
- other ancillary products.

Most Phase-2 products use NCI path prefix `iy57/`.

For spatial products the database stores dedicated WGS84/PostGIS geometry tables, e.g.
`bathymetry_geoms`, `backscatter_geoms`, `sidescan_geoms`, `vis_summary_geoms`.

## Spatial query mechanism

The public API accepts a `geom` query parameter. The backend evaluates:

`ST_Intersects(g.geom, ST_GeometryFromText(<geom>, 4326))`

Therefore an AOI around the evidence-supported 33–36S / Arc-7 corridor can be sent directly to the authoritative catalogue index rather than downloading the complete >121,000 km2 archive.

The `/features` endpoint returns the matching database geometries as GeoJSON via `ST_AsGeoJSON(g.geom)`.

The `/download-url-list` endpoint resolves matching database bundles into the original file URIs.

## Why this matters

This provides a reproducible path:

official Arc-7 AOI
→ API spatial intersection
→ matching Phase-2 product geometries
→ matching original file URIs
→ targeted download
→ inspect coverage/GIS bundles
→ assign search-negative evidence only from documented classes.

It also avoids treating the 5 m visualisation product or WMS raster envelopes as cell-level probability of detection.

## Important limitation

The API product geometry is a catalogue footprint/index. A footprint establishes that a product intersects an AOI; it does **not** by itself establish sonar detection probability or prove every point inside the footprint was searched effectively.

Final Pd still requires authoritative coverage/holiday/LPD semantics.

## Runtime status

The production hostname is documented in the AusSeabed source repository. The current research runtime could not directly open the production host, so no live API response is claimed here. The API implementation, routes, database schema, PostGIS intersection semantics, and product catalogue structure are nevertheless directly recoverable from AusSeabed's source.

## Next executable step

Add a fail-closed client that:
1. queries `/products`;
2. submits a WKT polygon for the 33–36S Arc-7 AOI to Sidescan and Visualisation/Coverage products;
3. saves returned GeoJSON geometries;
4. requests matching original URL lists;
5. refuses to create Pd values from catalogue footprints alone.
