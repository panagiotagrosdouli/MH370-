# Phase-2 recovery: non-spatial-file gap — 2026-09-18

Primary AusSeabed documentation confirms that MH370 Database Search spatially queries and downloads the full Phase-2 collection on NCI. Historical Phase-2 README evidence adds a crucial caveat: not every file is searchable by the spatial DB tool; files that cannot be represented spatially or require specialised readers must be found by attributes or accessed directly through NCI/THREDDS.

This explains a plausible failure mode in the current API-first strategy. The authoritative data-holiday database may live under the historical `iy57/gis` tree yet not appear as a normal spatial `vis_summary` record, especially if it is a geodatabase/container whose internal feature classes, rather than the container itself, carry geometry.

Recovery is therefore bifurcated:
A) spatial API route: enumerate `Visualisation and Coverage Summaries`, preserve original URIs, inspect candidate geometry products;
B) direct NCI route: enumerate `iy57/gis` and search filenames/metadata for holiday, coverage, geodatabase, GDB, SHP, trackline and database artifacts, including objects omitted from DB Query Search by Area.

Evidence policy is unchanged: archived forum reproduction is discovery evidence only. A candidate becomes evidence-grade only when its bytes/metadata are recovered from an official GA/AusSeabed/NCI route and its residual polygons reconcile with ATSB Table 4.1.

Status: TWO_ROUTE_RECOVERY_MODEL / NON_SPATIAL_DB_BLIND_SPOT_IDENTIFIED / NO_PD_ASSIGNED.
