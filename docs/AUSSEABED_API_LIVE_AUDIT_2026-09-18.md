# AusSeabed API live-endpoint audit — 2026-09-18

## Live access result

Direct public retrieval attempts were made against the production MH370 API health, product-list, and Visualisation and Coverage Summaries product-detail paths.

The current web runtime could not access those endpoints. This is an access/runtime result only; it is not evidence that the service is offline.

## Source-code result

A fresh search of the official AusSeabed product-catalogue repository found no committed File_Links.txt, data-holiday file, trackline file, or iy57 coverage payload. The repository contains the API/database implementation and product definitions, but not the underlying Phase-2 catalogue contents.

The Visualisation and Coverage Summaries product remains the strongest official catalogue lead:
- vis_summary
- vis_summary_bundle
- vis_summary_geoms
- iy57/

## Consequence

There are now two independent blockers:
1. production API payload is not reachable from the current web runtime;
2. the open-source repository does not embed the underlying iy57 source-file inventory.

Therefore exact holiday/coverage filenames cannot be honestly inferred from the code.

## Recovery strategy

The next acceptable recovery paths are:
- a live response from the production API;
- an archived/cached API response;
- recovery of iy57/File_Links.txt;
- recovery of the iy57/gis catalogue or original archive;
- an official AusSeabed/GA export containing the linked source filenames.

Filename guessing is prohibited.

## Evidence status

API implementation/provenance: PASS.
Live production payload: NOT RECOVERED.
Exact source URI/file inventory: NOT RECOVERED.
Cell-level Pd geometry: NOT RECOVERED.
