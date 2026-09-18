# Direct iy57/gis web-index recovery — 2026-09-18

A fresh exact-path web-index search for `iy57/gis`, data-holiday, coverage, GDB and SHP artifacts produced one substantive indexed remnant: an archived reproduction of the historical Phase-2 README. No trustworthy indexed child filename under `iy57/gis` was recovered.

The recovered README text states that the `gis` directory contains derived geospatial datasets including contact locations, coverages, a data-holiday database, and generalized deep-tow/AUV tracklines. It also states that not all files were searchable through the DB Query Search by Area tool; non-spatial or specialised-reader files had to be found by attribute or accessed directly via NCI THREDDS. The root collection also contained `File_Links.txt` for bulk-download filtering.

Evidence classification:
- existence/role of `iy57/gis`: DISCOVERY_EVIDENCE from archived reproduction, consistent with prior GA/AusSeabed material;
- exact holiday database filename: NOT RECOVERED;
- polygon geometry: NOT RECOVERED;
- cell-level Pd: NOT ASSIGNED.

New high-value recovery target: the historical root `File_Links.txt`. If an archived/indexed copy can be recovered, filtering it for `/gis/`, `holiday`, `.gdb`, `.shp`, `coverage` can reveal exact original NCI paths without filename guessing.

Stop rule: do not infer filenames from directory semantics. Continue only with exact indexed strings, official API records, archived root listings, or recovered official bytes.

Status: IY57_GIS_DIRECTORY_CONFIRMED_AS_DISCOVERY_LEAD / CHILD_FILENAME_UNRESOLVED / FILE_LINKS_TXT_PROMOTED_TO_PRIMARY_TARGET.
