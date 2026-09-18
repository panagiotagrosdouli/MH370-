# Historical THREDDS recovery: exact directory semantics — 2026-09-18

A fresh indexed recovery surfaced a long archived reproduction of the Phase-2 READ_ME and contemporaneous THREDDS navigation notes.

Recovered exact historical facts useful for retrieval:
- root catalogue: iy57;
- root contained File_Links.txt for bulk filtering;
- files not spatially representable or needing specialised readers were explicitly directed to direct NCI THREDDS access;
- top-level gis was described as derived geospatial datasets: contact locations, coverages, data holiday database, and generalised deep-tow/AUV tracklines;
- coordinate systems included WGS84 and UTM WGS84 zones 45S/46S;
- historical catalogue navigation used nested catalog.html pages and an HTTPServer access link at the dataset leaf;
- an exact historical camera leaf was indexed: iy57/camera/Fugro_Supporter/auv/processed/jpg/catalog.html.

This does NOT recover the holiday database bytes or filename. It does, however, strengthen the retrieval model: the GIS artifact may be a non-spatial/special-reader object omitted from spatial DB query, so direct THREDDS catalogue traversal remains necessary.

No geometry/Pd is inferred from the archived reproduction. Discovery provenance remains secondary until official bytes are recovered.

Status: THREDDS_RETRIEVAL_MECHANICS_RECOVERED / GIS_FILENAME_UNRESOLVED / FAIL_CLOSED.
