# Official ArcGIS layer audit — 2026-09-17

## Verified services

### 7thArc_SingleLine
- Official ArcGIS FeatureServer identified.
- Service item: `4c94d33cfc144f7d8b78943dee56e29b`.
- CRS: EPSG:4326.
- Copyright/provenance: ATSB; satellite and aircraft specialists.
- Description states the arc extends approximately 20°S–39°S and that independent satellite/aircraft-performance analysis placed the expected loss close to the 7th Arc.

### Generalised_Flight_Path_Probabilities
- Service item: `994e4014ef9944c48f4cf8754314afbc`.
- Layer: `Flight_Path_Probabilities_Generalised`.
- CRS: EPSG:4326.
- Copyright/provenance: ATSB DSTG.
- IMPORTANT: service metadata explicitly calls this a *cartographic dataset* created for a GA Story Map and says the position of each line is indicative.
- Consequence: DO NOT treat this layer as a numerical DSTG posterior or use line density/geometry as quantitative probability mass. The numerical DSTG Bayesian distribution must come from the underlying DSTG analysis/data, not this generalized display layer.

### MH370_Phase_2_contacts
- Service item: `53b12c81b3024726936859b84fa6692a`.
- Layer geometry: point.
- Service CRS: Web Mercator EPSG:3857.
- Query formats include JSON, GeoJSON and PBF.
- Fields exposed by the official service include contact class, description/name/reference, width/height/length, easting/northing, time, ping number, range, fish height, heading, acoustic source, block number and reacquisition status.
- This is contact evidence, not a search-coverage polygon and not a data-holiday/LPD mask.

## Model consequences

1. The generalized flight-path layer is visualization evidence only. It is excluded from quantitative posterior multiplication.
2. Phase-2 contact points can later be used as a consistency/audit layer, but they cannot define `P_D(L)` without coverage/pass/sensor/terrain information.
3. Candidate residual cells remain gated on authoritative search coverage plus data-holiday/LPD geometry.
4. The official 7th Arc remains the geometric reference once its actual feature geometry is ingested.

## Fail-closed rule

No coordinate or residual search box may be promoted merely because it falls between generalized flight-path lines or near a Phase-2 contact. Any such promotion requires an independent physics/drift prior and defensible local non-detection likelihood.
