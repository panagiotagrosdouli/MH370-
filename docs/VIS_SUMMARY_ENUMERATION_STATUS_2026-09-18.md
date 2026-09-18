# vis_summary candidate classifier — 2026-09-18

The official AusSeabed source tree has now been searched for every reference to `vis_summary`. Only the API environment mapping and SQL schema define it; no static bundle inventory or seeded filename list is present in the public repository. Therefore bundle names cannot be recovered from source code alone.

A fail-closed classifier has been added for live/API-exported file records. It promotes names/URIs containing holiday, database, geodatabase/GDB to high-priority authoritative candidates; coverage/SHP/trackline records to review candidates; all others remain index/other. Classification is discovery-only and never assigns Pd.

The production `/products` endpoint remains inaccessible from the current web runtime, so no live bundle names are claimed. This is a runtime-access limitation, not evidence that the service or records are absent.

Status: SOURCE_STATIC_ENUMERATION_EXHAUSTED / LIVE_RECORD_CLASSIFIER_READY / NO_FILENAME_FABRICATION.
