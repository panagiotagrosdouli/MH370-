# Geoscience Australia / NCI MH370 Data Manifest

## Purpose
These are the authoritative geospatial inputs required before issuing a V4 residual search box.

## Phase One
- Bathymetric survey / processed bathymetry.
- GA states Phase One mapped the seafloor to guide the high-resolution search.
- Available in processed forms including 150 m GeoTIFF/ASCII XYZ and higher-volume point-cloud/raw products through GA/NCI.

## Phase Two
GA describes Phase Two as high-resolution sidescan and multibeam sonar collected from towed and autonomous underwater vehicles.

The NCI collection is described as containing raw and processed data. The Phase Two collection includes data families such as camera, documents, GIS, multibeam, navigation, sidescan, platform data and final processed products.

The GIS material is the priority because it can encode search coverage, contact locations, data holidays and generalized deep-tow/AUV tracklines. These are needed to replace proxy masks with measured search geometry.

## Authoritative discovery points
- Geoscience Australia MH370 data release: https://www.ga.gov.au/scientific-topics/marine-and-coastal/showcase/mh370-data-release
- GA Marine portal: https://portal.ga.gov.au/persona/marine
- Phase Two dataset persistent identifier reported by GA metadata: https://pid.geoscience.gov.au/dataset/ga/120962

## Ingestion policy
1. Prefer processed GIS/coverage layers before multi-terabyte/raw imagery.
2. Preserve source CRS and metadata; reproject only into derived products.
3. Record checksums for downloaded files.
4. Do not commit huge raw files to GitHub. Commit manifests, scripts, metadata and compact derived grids where licensing permits.
5. Never convert a published total searched area into a fabricated polygon.
6. 2025/26 Ocean Infinity negative evidence remains `GEOMETRY_UNKNOWN` until authoritative track/polygon geometry is obtained.

## Required derived cell fields
- lat, lon
- depth_m
- slope / roughness if derivable
- coverage class
- sensor / platform
- pass count if available
- holiday / terrain shadow / terrain avoidance / LPD indicators
- Pd_low, Pd_central, Pd_high
- provenance/source feature id
