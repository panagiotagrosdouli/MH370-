# THREDDS catalog.xml recovery attempt — 2026-09-18

Direct retrieval of the historical official NCI endpoints was attempted:
- /thredds/catalog/iy57/catalog.xml
- /thredds/catalog/iy57/gis/catalog.xml

The current web runtime could not access either endpoint. This is a transport/runtime failure, not evidence that the historical catalogue or data are absent.

Fresh exact-index search still did not surface the XML itself. It did, however, recover the archived READ_ME reproduction containing the original instruction that non-spatial/special-reader files should be accessed directly through NCI THREDDS and that the root File_Links.txt was intended for filtered bulk download.

A deterministic XML parser is now committed. When any official or archived catalog.xml is recovered, it enumerates catalogRef hrefs and dataset urlPath values and ranks exact strings containing gis, holiday, coverage, trackline, .gdb, .shp or contact. It never invents child filenames.

This closes the catalogue parsing implementation gap. The remaining blocker is byte retrieval, not catalogue interpretation.

Status: OFFICIAL_XML_RUNTIME_BLOCKED / PARSER_READY / NO_FILENAME_GUESSING / POSTERIOR_UNCHANGED.
