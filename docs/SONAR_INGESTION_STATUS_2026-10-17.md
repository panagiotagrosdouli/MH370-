# Official Phase-2 sonar retrieval: evidence status (17 October 2026)

## Verified public source

Geoscience Australia released the MH370 Phase Two high-resolution sonar data on 28 June 2018. The raw and processed compilation covers more than 121,000 km² of acquisition undertaken between September 2014 and January 2017.

- GA dataset 120962, DOI: 10.4225/25/5B0CD2B84A2DC
- Data catalogue: https://researchdata.edu.au/the-search-flight-processed-data/3404148
- GA release: https://www.ga.gov.au/news/news-archive/the-data-behind-the-search-for-mh370-phase-two-data-released
- AusSeabed: https://www.ausseabed.gov.au/data
- Portal download instructions: https://asbdatamanagement.atlassian.net/wiki/spaces/AMDPUG/pages/956268789/How+to+download+data

The portal user guide describes an MH370 Database Search tool for accessing original files held at NCI. Its clip-and-download workflow can require an email and is distinct from the original full data archive.

## Independent warning from GA 2022 review

The 2022 data review (https://www.atsb.gov.au/sites/default/files/2024-02/mh370-data-review-2022-final-report-v2.pdf) documents data holidays and lower-probability-of-detection areas. In its **specific local review area**, a table reports a total of 72.79 km² of gaps and LPDs. **Do not extrapolate this area-wide statistic to the global search corridor** or interpret all raw coverage as successful detection.

## Retrieval result in this session

The official registry and portal were verified through public indexed records. Direct programmatic requests to ArcGIS from this compute runtime failed due to network connection restrictions. Therefore no full official sonar polygon or georeferenced raster was downloaded or interpreted in this session.

## New reproducibility tool

`src/audit_sonar_geojson.py` checks locally supplied GeoJSON polygon features, explicitly declared WGS84 coordinates, bounding boxes, and user-supplied provenance identifiers.

It **does not**:
- download raw sonar or certify that claimed sources are genuine;
- verify polygon topology, overlaps, holes, sonar quality or actual surveyed area;
- assign probability of detection or identify MH370;
- satisfy the `AUTHORITATIVE_GIS_VALIDATED` evidence gate.

## How to proceed

1. Acquire the appropriate raw/processed Phase-2 source archive through official NCI/AusSeabed channels.
2. Obtain original coverage and holiday polygons where present; preserve original formats and metadata.
3. Inspect native CRS, timestamp and resolution, then transform verified footprint polygons to EPSG:4326 using GIS software.
4. Run `python src/audit_sonar_geojson.py path/to/official.geojson --source-url https://... --dataset-id GA-120962 --out results/sonar_geojson_audit.json` with the actual source URL.
5. Conduct independent source and geometry review (CRS, holes, overlaps, acquisition footprints, LPD evidence). Only then consider cell-level search non-detection likelihoods.

**No new location or residual-search ranking is claimed.**
