#!/usr/bin/env python3
"""Evidence gate for OI geometry provenance."""
import argparse
ALLOWED_PD={"OI_AUTHORITATIVE_AUV_TRACK","OI_AUTHORITATIVE_SONAR_FOOTPRINT"}
ZERO_WEIGHT={"OI_VESSEL_TRACK_PROXY","OI_PRESENTATION_SEARCH_BAND_PROXY","OI_AGGREGATE_AREA_ONLY"}
p=argparse.ArgumentParser();p.add_argument("classification");a=p.parse_args()
c=a.classification.strip().upper()
if c in ALLOWED_PD:
 print("PD_ELIGIBLE_AFTER_SENSOR_SEMANTICS_VALIDATION")
elif c in ZERO_WEIGHT:
 print("PD_PROHIBITED_BASELINE")
else:
 raise SystemExit("UNKNOWN_PROVENANCE_FAIL_CLOSED")
