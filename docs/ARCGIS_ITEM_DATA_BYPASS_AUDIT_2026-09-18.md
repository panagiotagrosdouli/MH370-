# ArcGIS item-data bypass audit — 2026-09-18

## Attempted bypasses

The verified 7th-Arc item ID is:
4c94d33cfc144f7d8b78943dee56e29b

Fresh retrieval attempts targeted both ArcGIS Online sharing REST routes:
- /sharing/rest/content/items/{itemId}?f=json
- /sharing/rest/content/items/{itemId}/data?f=json

and the authoritative child FeatureServer layer/query routes.

## Result

The current web runtime rejected direct access to the ArcGIS Online item/item-data URLs and to the child layer/query payload. A separate container-network request failed DNS resolution for services1.arcgis.com.

The parent GA FeatureServer remains publicly indexed and returns the verified service metadata through web search.

This isolates the failure as environment/network-path specific. It does not justify declaring the service offline.

## Important correction

The service extent is not the 7th-Arc polyline and must never be buffered as if it were the line.

## Reproducible external commands

The repository fetcher remains the canonical route when run in a network environment that can reach ArcGIS. A successful response must contain one or more features and actual line geometry before any corridor is generated.

## Evidence state

Item identity: VERIFIED.
Parent service metadata: VERIFIED.
Sharing REST item-data bytes: BLOCKED BY CURRENT RUNTIME.
Layer vertices: BLOCKED BY CURRENT RUNTIME.
Authoritative corridor: PENDING.

The next research branch should proceed in parallel on recoverable Phase-2 geometry rather than repeatedly hitting the same network restriction.
