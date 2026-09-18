# MH370 API enumeration result — 2026-09-18

Primary AusSeabed source-code enumeration resolves an important ambiguity. The public MH370 API product list does NOT expose a standalone `gis` product. The exposed Phase-2 families include Bathymetry, Backscatter, Hillshade, Sidescan, Sub-bottom Profile, Tides, Water Column, Camera, Sound Velocity Profile, Unprocessed Multibeam, Unprocessed Sidescan, Navigation, Platform Raw, Heave, Weather, Sniffer, and `Visualisation and Coverage Summaries`.

The highest-value API family for geometry recovery is therefore `Visualisation and Coverage Summaries`, mapped to `marine_mh370.vis_summary`, `vis_summary_bundle`, and `vis_summary_geoms`, with `pathStart: iy57/`.

The API query implementation confirms that spatial filtering uses `ST_Intersects` against EPSG:4326 geometries. Feature output is generated with `ST_AsGeoJSON(g.geom)`. File-list queries resolve matching bundles to original `name`, `uri`, and `file_size`. This gives a provenance-preserving route from spatial geometry to original NCI objects.

Critical limitation: these database geometries are catalogue/index geometries. They are not automatically the ATSB data-holiday polygons and must not be interpreted as detection probability. The recovery sequence is now: enumerate `Visualisation and Coverage Summaries` bundle names/extensions -> identify candidate coverage/holiday/database files by original URI -> retrieve authoritative object -> reconcile polygon counts/classes/areas against Table 4.1 -> only then assign search nondetection semantics.

This corrects the earlier plan to query a nonexistent public `gis` API product directly. The archived NCI filesystem may contain a `gis` directory, while the public API maps its accessible material into product categories rather than exposing that directory name as a product.

Status: API_PRODUCT_ENUMERATION_COMPLETE / VIS_SUMMARY_IS_PRIMARY_DISCOVERY_FAMILY / GIS_PRODUCT_ASSUMPTION_CORRECTED / PD_STILL_FAIL_CLOSED.
