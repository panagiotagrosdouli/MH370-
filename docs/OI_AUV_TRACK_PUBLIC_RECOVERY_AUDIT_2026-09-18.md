# OI AUV-track public-recovery audit — 2026-09-18

## Search result

Targeted public-web and GitHub searches were run for exact HUGIN/AUV mission tracks, coordinates, KML/KMZ/GeoJSON and Armada 78-06 / 86-05 mission geometry.

Recovered:
- public surface-vessel track archives for Armada 78-06 and 86-05;
- operational reports that two HUGIN AUVs were on mission on 31 Dec 2025 and up to three were used during 6–15 Jan 2026;
- technical reporting that Armada 78-06 carried containerised AUV garages;
- independent commentary explicitly warning that exact AUV-scanned area/track is unknown.

Not recovered:
- any public HUGIN mission coordinate sequence;
- AUV KML/KMZ/GPX/GeoJSON;
- mission-plan line files;
- processed OI sonar footprint GIS;
- documented per-mission swath geometry.

## Negative discovery result

This is a useful negative discovery result: the public indexing currently exposes vessel movement and textual AUV operations, but not the underwater trajectories required to allocate search non-detection.

No spatial OI Pd is therefore introduced.

## Reproducible discovery protocol

Future searches should require a candidate artifact to contain at least one of:
- timestamped underwater AUV positions;
- named HUGIN mission route/line sequence;
- processed sonar swath polygon;
- mission plan with coordinate geometry.

A vessel AIS/KML artifact is automatically rejected.

## Implication for current ranking

The 2025–26 search can be used only as:
- aggregate searched-area evidence (official 7,571 km2);
- qualitative/proxy evidence of search activity in the southern / outside-arc sector.

It cannot yet be used to say that a specific residual cell has been cleared.

This preserves the baseline posterior from false precision.
