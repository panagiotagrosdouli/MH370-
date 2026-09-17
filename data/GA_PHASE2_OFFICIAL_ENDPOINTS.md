# Geoscience Australia MH370 Phase 2 — authoritative endpoints

Verified 2026-09-17.

## Primary Phase 2 dataset

Title: The Search for Flight MH370 - Phase 2 Raw and Processed Data
GA dataset identifier: `pid.geoscience.gov.au/dataset/ga/120962`
DOI: `10.4225/25/5B0CD2B84A2DC`
Coverage metadata: 80E–100E, 40S–25S.
Acquisition: September 2014–January 2017, >121,000 km² high-resolution data.
Platforms include Fugro Equator, Fugro Supporter, Fugro Discovery, Havila Harmony, Dong Hai Jiu 101 and Go Phoenix.

## 5 m visualisation dataset

Title: The Search for Flight MH370 – Phase 2 5 m resolution sonar images for data visualisation
GA dataset identifier: `pid.geoscience.gov.au/dataset/ga/120969`
DOI: `10.4225/25/5B0CD3B139DEF`

Four principal layers are documented:
- Fugro deep-tow SSS
- Fugro AUV SSS
- Go Phoenix SAS
- Dong Hai Jiu 101 SAS

The mosaics were standardized to GeoTIFF and reprojected from UTM 45S/46S to WGS84. The 5 m product is suitable for coverage screening; detailed target interrogation should use the higher-resolution raw/processed dataset.

## Marine geospatial services

Geoscience Australia/AusSeabed publishes Marine Data WMS/WCS services containing MH370 Phase 1 bathymetry and Phase 2 5 m sonar layers.

WMS GetCapabilities endpoint:
`https://warehouse.ausseabed.gov.au/geoserver/ows?REQUEST=GetCapabilities&SERVICE=WMS`

WCS GetCapabilities endpoint:
`https://warehouse.ausseabed.gov.au/geoserver/ows?REQUEST=GetCapabilities&SERVICE=WCS`

Known WMS layer names from the current service catalogue include:
- `Fugro_DT_5m_WGS84` — Deep Tow Side Scan Sonar 2014–2016
- `Fugro_AUV_5m_WGS84` — AUV Side Scan Sonar 2015–2017
- `DHJ_SAS_5m_WGS84` — Dong Hai Jiu 101 Synthetic Aperture Sonar 2016

The Go Phoenix layer is also part of the four-layer Phase 2 product and must be resolved from capabilities before automated ingestion.

## Phase 1 bathymetry

Dataset: MH370 Phase 1 150 m Bathymetry (GA-4421, GA-4422, GA-4430)
Direct public ZIP documented by GA/AusSeabed:
`https://files.ausseabed.gov.au/survey/Southern%20Indian%20Ocean%20(MH370)%20Bathymetry%202017%20150m.zip`
Approximate archive size: 193.5 MB.

## Runtime note

The research environment used on 2026-09-17 could discover and verify these endpoints through indexed public metadata, but direct network access from the local computation container could not resolve `warehouse.ausseabed.gov.au`. Therefore no fake raster was substituted. The ingestion code must fail closed until the actual WMS/WCS/GeoTIFF bytes are available.

## Provenance policy

Never infer a cell as searched solely from the global dataset bounding box. Coverage must come from actual imagery/coverage layers. Never convert the total 121,000 km² acquisition figure into a hand-drawn polygon.