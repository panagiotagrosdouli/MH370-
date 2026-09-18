# Official seventh-arc geometry retrieval recheck — 2026-09-18

Fresh public indexing reconfirms the Geoscience Australia/ATSB ArcGIS service named 7thArc_SingleLine, FeatureServer layer 0, item 4c94d33cfc144f7d8b78943dee56e29b, EPSG:4326. Direct feature-query requests from the current runtime still fail before returning the geometry payload. This is treated as a runtime transport limitation, not evidence that the layer is offline.

The ATSB maps material independently retains the published cross-arc envelope of 27.5 NM west and 25 NM east. First Principles material retains the high-value residual corridor around 33S–36S and close to the seventh arc.

A separate public computational implementation exposes high-resolution satellite-state values and an independent arc reconstruction. It is useful only as an adversarial numerical benchmark; it is not authoritative GA/ATSB linework.

Decision: keep our line RECONSTRUCTED_PRIMARY_INPUTS; keep the ArcGIS entry AUTHORITATIVE_SERVICE_METADATA; do not promote third-party linework to authoritative vertices.

Status: OFFICIAL_SERVICE_RECONFIRMED / FEATURE_VERTICES_RUNTIME_BLOCKED / INDEPENDENT_NUMERIC_BENCHMARK_IDENTIFIED.
