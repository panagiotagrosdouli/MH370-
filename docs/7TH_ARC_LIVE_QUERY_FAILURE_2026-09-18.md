# 7th-Arc live-query failure characterization — 2026-09-18

## Fresh verification

The authoritative Geoscience Australia ArcGIS service directory remains publicly indexed and exposes 7thArc_SingleLine as a FeatureServer. The indexed service metadata provides:
- item ID 4c94d33cfc144f7d8b78943dee56e29b
- layer 0
- EPSG:4326
- JSON query support
- ATSB / satellite-and-aircraft-specialist provenance
- description placing the relevant arc approximately 20S to 39S.

## Direct geometry attempt

A direct request was made to the authoritative layer query endpoint with where=1=1, all fields, returnGeometry=true, outSR=4326 and GeoJSON output.

The current web runtime returned an access/internal error rather than a FeatureCollection. A direct request to layer 0 itself produced the same runtime-access failure.

This is NOT evidence that the ArcGIS service or layer is offline. The parent FeatureServer is still indexed and the GA ArcGIS service directory currently lists 7thArc_SingleLine.

## Consequence

The blocker is now isolated to retrieval of the child layer/query payload in this runtime, not uncertainty over service identity.

Do not digitize the arc from a map screenshot and do not substitute the service extent for line geometry.

## Next independent retrieval routes

1. ArcGIS item-data endpoint for item 4c94d33cfc144f7d8b78943dee56e29b.
2. ArcGIS Online sharing REST item metadata/data.
3. cached/exported FeatureCollection or shapefile linked to the item.
4. execute src/fetch_official_7th_arc.py in a network environment that permits the child query endpoint.

Only recovered vertices may be used to build the asymmetric 27.5 NM west / 25 NM east corridor.
