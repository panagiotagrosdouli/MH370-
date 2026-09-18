# Ocean Infinity 2018 / 2025–26 geometry status — 2026-09-18

## Official facts verified

Malaysia's Ministry of Transport states that the 2025/2026 contract covered a new area estimated at 15,000 km2. After contract signature, operations ran 25–28 March 2025 and 31 December 2025–23 January 2026, totalling 28 operational days and approximately 7,571 km2 of seabed surveyed inside the defined search area. MOT also states that additional survey activity occurred in the broader search area before formal signature.

Ocean Infinity states that since 2018 it has mapped more than 140,000 km2 of seafloor during MH370 efforts and that the latest search did not find the aircraft.

Neither public official statement provides cell/AUV-track polygons sufficient for Bayesian spatial non-detection.

## Newly recovered third-party geometry lead

MH370-CAPTION publishes downloadable Google Earth track archives for:
- Armada 78-06, 2025-02-08 to 2025-03-06;
- Armada 78-06, 2025-03-06 to 2025-04-08;
- Armada 86-05, 2025-12-30 to 2026-01-23.

The site explicitly warns that the precise coordinates of the white Ocean Infinity search bands are **not known**; its search-area bands were drawn from a public presentation. Therefore:
- vessel-track KML = useful navigation/search-activity proxy;
- hand-drawn search bands = not authoritative coverage;
- neither can be converted directly into seabed Pd.

The page also states that its displayed inner orange boundary represents the earlier 2014–2017 underwater search and the area between orange and red boundaries represents OI 2018. This is useful for visual cross-checking only unless original geometry provenance is recovered.

## Critical distinction

A surface-vessel track is not an AUV sonar footprint.

For OI operations the mother vessel can launch/recover autonomous vehicles whose seabed tracks and swaths differ materially from the vessel trajectory. Buffering the vessel KML by an assumed distance and calling it searched area would fabricate geometry.

Thus the project must maintain:
- OI_VESSEL_TRACK_PROXY
- OI_PRESENTATION_SEARCH_BAND_PROXY
- OI_AUTHORITATIVE_SEABED_COVERAGE

as separate provenance classes.

Only the third may enter P_D(x).

## Current conclusion

The public evidence is now strong enough to say that the 2025–26 7,571 km2 total cannot be spatially allocated from official public statements alone.

Third-party KML archives provide a route to reconstructing where search activity occurred, but not a defensible exact sonar non-detection mask.

Consequently OI 2018 and 2025–26 remain UNALLOCATED in the baseline posterior. A separate proxy/sensitivity overlay may use the KML tracks once downloaded and parsed, with explicit zero evidentiary weight in the baseline.

No present-day residual area or wreck coordinate is claimed.
