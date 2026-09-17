# Official GIS discovery

## Key advance

The project no longer needs to approximate the Seventh Arc from screenshots. A public ArcGIS FeatureServer exists for the Seventh Arc with ATSB attribution and WGS84 geometry.

- Seventh Arc service item: `4c94d33cfc144f7d8b78943dee56e29b`
- Geometry service: `services1.arcgis.com/wfNKYeHsOyaFyPw3/.../7thArc_SingleLine/FeatureServer/0`
- Spatial reference: EPSG:4326 / WGS84
- Service description attributes the arc to ATSB / satellite and aircraft specialists.

A separate ATSB-attributed Wide Search Area FeatureServer is also public. Its description states it represents ±100 NM around the Seventh Arc based on maximum aircraft glide range. It is useful as a historical/sensitivity layer, not as the baseline end-of-flight posterior.

The Geoscience Australia story-map ecosystem also exposes a public Possible MH370 Debris Recovered point layer. These records are not all confirmed debris and must be joined to Malaysian investigation classifications before they receive evidential weight.

## Phase 2 sonar

GA's Phase 2 visualisation product DOI is `10.4225/25/5B0CD3B139DEF`. It provides 5 m overview imagery from sidescan sonar, synthetic-aperture sonar and multibeam backscatter. GA explicitly recommends the higher-resolution raw/processed product for detailed interrogation.

## Modelling consequence

The Seventh Arc geometry can now be ingested directly instead of locally approximating longitude as a function of latitude. This removes one avoidable source of geometric error in the residual-search model.

The remaining decisive task is to ingest authoritative Phase 2 sonar coverage/data-quality geometry or rasters and convert them to a spatial probability-of-detection field. The model must continue to fail closed when those data are unavailable.

## Baseline corridor

ATSB's current public investigation material states that updated independent SATCOM and drift analysis consistently identified the most likely impact close to the Seventh Arc, approximately within 25 NM, bounded approximately by 33S–36S. The ATSB maps page states the aircraft was considered unlikely to be more than 27.5 NM west or 25 NM east of the arc.

Therefore the primary computation remains the intersection of the official arc, the physics/drift density, and real low-Pd/unsearched seabed cells. The ±100 NM layer is retained only for end-of-flight sensitivity analysis.
