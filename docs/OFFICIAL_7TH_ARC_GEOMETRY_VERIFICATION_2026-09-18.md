# Official 7th-Arc geometry verification — 2026-09-18

## Authoritative service verified

The Geoscience Australia ArcGIS REST directory currently exposes:
- service: 7thArc_SingleLine
- type: FeatureServer
- layer: 7thArc_SingleLine (0)
- service item ID: 4c94d33cfc144f7d8b78943dee56e29b
- spatial reference: EPSG:4326
- supported query format: JSON
- copyright/provenance: ATSB; satellite and aircraft specialists

The service description states that independent satellite-communications and aircraft-performance analysis places MH370 close to the 7th Arc and describes the arc as extending approximately 20S to 39S.

## Retrieval result

The service itself is indexed and verified, but this runtime did not return the layer query payload when requesting the REST layer/query endpoints. Therefore this audit does NOT claim to have recovered the line vertices yet.

## Exact machine endpoint

Authoritative geometry should be requested from layer 0 with:
- where=1=1
- returnGeometry=true
- outSR=4326
- JSON or GeoJSON output where supported.

The exact FeatureServer identity is now verified, so future geometry retrieval no longer depends on an inferred service name or guessed item ID.

## Evidence gate

Service identity: VERIFIED.
ATSB provenance: VERIFIED.
EPSG:4326: VERIFIED.
Layer ID 0: VERIFIED.
Line vertices: NOT YET RETRIEVED IN CURRENT RUNTIME.
Buffered 27.5W/25E corridor: NOT YET GENERATED.

No hand-digitized arc may substitute for the authoritative geometry in the evidence-grade residual ranking.
