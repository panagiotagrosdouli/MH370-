# Archived iy57 README recovery — 2026-09-18

## Breakthrough

A web-indexed archived copy of the official Phase-2 README preserves substantially more of the original NCI catalogue description than our previous notes.

The README explicitly says the top-level dataset folders included:
camera, documents, gis, heave, mbes, nav, platform_raw, sbp, sidescan, sniffer, svp, tides, water_column, weather.

Most importantly:

- `gis` contained derived geospatial datasets including **contact locations, coverages, a data holiday database, and generalised tracklines of deep-tow and AUV vehicles**.
- `nav` contained raw/processed navigation for vessels, deep tow, AUV, ROV, position and USBL data, with formats including **KML, KMZ, SHP, TXT, DXF, POS**.
- `sidescan` contained processed/raw side-scan and synthetic-aperture-sonar data from deep tow and AUV systems, including **PNG, TIFF, IMG, XTF, GDB, JSF**.
- `mbes` included processed/raw bathymetry/backscatter and AUV-mounted MBES, including **TIF, PNG, XTF, TXT, LAZ, XYZ, BIL, ALL, GSF, GDB, XYI**.
- coordinate systems included WGS84 and UTM WGS84 zones 45S/46S; README says unlabeled files can generally be assumed WGS84.
- bulk download was explicitly supported by filtering root `File_Links.txt` and feeding selected links to wget.

## Why this matters

We no longer need to treat the existence of a spatial data-holiday database as an inference from reports. The archived official README explicitly names it as content of `iy57/gis`.

The same README confirms that exact underwater navigation data existed separately from vessel navigation, including AUV/deep-tow navigation products. This is exactly the distinction required for defensible search-coverage reconstruction.

## Highest-value recovery targets

1. `iy57/File_Links.txt`
2. any `iy57/gis/*` GDB/SHP/KML/KMZ
3. `iy57/nav/*auv*` and `iy57/nav/*deep*tow*` navigation files
4. source coverage products linked by the AusSeabed Visualisation and Coverage Summaries catalogue

## Search semantics

A recovered GIS object must still be inspected before Pd assignment:
- coverage polygon -> search footprint candidate;
- data-holiday database -> unresolved/low-quality candidate;
- generalised trackline -> activity/navigation geometry, not automatically swath;
- nav AUV/deep-tow -> trajectory; requires sensor/swath semantics;
- sidescan raster/GDB -> sensor product; may support direct coverage reconstruction.

## Provenance caution

The current recovery is an archived/indexed reproduction of the official README text, not the geometry bytes themselves. It upgrades the existence and file-type evidence, but cell-level Pd remains blocked until files are recovered.
