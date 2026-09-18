# IY57 exact-path archival recovery — 2026-09-18

## New exact historical path recovered

A web-indexed archival discussion quotes the official Phase-2 README and preserves an exact historical THREDDS catalogue path for an AUV camera branch:

`iy57/camera/Fugro_Supporter/auv/processed/jpg/`

This is valuable because it demonstrates the actual directory naming convention and confirms that `Fugro_Supporter` + `auv` existed as concrete path components in the old NCI tree.

The same indexed README confirms:
- root folder `gis`: contact locations, coverages, data holiday database, generalized deep-tow/AUV tracklines;
- root `File_Links.txt` intended for bulk filtering/download;
- `nav` includes deep-tow and AUV navigation;
- `sidescan` and `mbes` contain AUV/deep-tow processed products.

## What was NOT recovered

Targeted searches still did not expose an indexed exact path/filename beneath `iy57/gis`, nor a cached copy of `File_Links.txt`.

Therefore no holiday/coverage filename is guessed.

## Path-enumeration strategy

Use only path components evidenced by the archived tree and README. Candidate recovery searches should combine:
- `iy57/gis/`
- vessel/platform tokens evidenced elsewhere in the archive
- semantic tokens: coverage, holiday, trackline, contact
- geospatial extensions: gdb, shp, kml, kmz

The recovered camera path is a directory-structure clue, not evidence that GIS uses the same vessel nesting.

## Evidence status

Exact old AUV directory path: RECOVERED.
Exact GIS filename: NOT RECOVERED.
File_Links contents: NOT RECOVERED.
Spatial Pd: BLOCKED.
