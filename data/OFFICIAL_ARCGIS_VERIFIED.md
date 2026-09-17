# Verified official ArcGIS geometry endpoints

Verified 2026-09-17 against the public ArcGIS REST directory associated with Geoscience Australia/ATSB MH370 mapping.

## 7th Arc

Service: `7thArc_SingleLine` FeatureServer

- Item ID: `4c94d33cfc144f7d8b78943dee56e29b`
- Layer: 0 (`7thArc_SingleLine`)
- Spatial reference: EPSG:4326 / WGS84
- Service description states that independent satellite-communications and aircraft-performance analysis places MH370 in close proximity to the 7th Arc and describes the arc as extending from 20°S to 39°S.
- Copyright/attribution shown by service: ATSB; Satellite and aircraft specialists.

REST service:
`https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/7thArc_SingleLine/FeatureServer`

## Wide Search Area

Service: `WideSearchArea` FeatureServer

- Item ID: `a738c2c44c024b04b5db0a4209f70bb2`
- Layer: 0
- Geometry: polygon
- Spatial reference: EPSG:4326 / WGS84
- Service description: ATSB defined the area from an aggregate of five independent analyses along the 7th Arc; the wide area is ±100 NM either side of the arc based on maximum aircraft glide range.
- Copyright/attribution shown by service: ATSB; Search Strategy Working Group; Satellite and Aircraft Specialists.

REST service:
`https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/WideSearchArea/FeatureServer`

## Phase-2 5 m sonar visualization

Geoscience Australia's public catalogue confirms four 5 m WGS84 GeoTIFF visualization layers:

1. Fugro Deep Tow SSS
2. Fugro AUV SSS
3. Go Phoenix SAS
4. Dong Hai Jiu 101 sonar

The catalogue explicitly recommends the higher-resolution raw/processed dataset for detailed interrogation because the 5 m mosaic can obscure overlap regions.

## Evidence rule

These endpoints establish authoritative arc/wide-area geometry provenance. They do **not** by themselves establish cell-level probability of detection. Search-negative likelihood must remain unset until actual Phase-2 coverage/holiday/LPD geometry is ingested.

Do not substitute approximate third-party `data_holidays.geojson` polygons for authoritative geometry.
