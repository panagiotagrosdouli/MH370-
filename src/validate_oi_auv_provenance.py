#!/usr/bin/env python3
"""Validate provenance fields for future OI AUV coverage imports."""
import argparse,json
p=argparse.ArgumentParser();p.add_argument("metadata_json");a=p.parse_args()
m=json.load(open(a.metadata_json,encoding="utf-8"))
src=m.get("source_type","").upper()
if src=="VESSEL_AIS" or src=="VESSEL_KML":
 raise SystemExit("REJECT: surface-vessel track cannot establish AUV sonar coverage")
if src not in {"OI_AUV_MISSION","MOT_AUV_MISSION","AUTHORITATIVE_SONAR_FOOTPRINT"}:
 raise SystemExit("REJECT: unsupported provenance")
required=["source_url_or_file","platform","geometry_semantics"]
missing=[k for k in required if not m.get(k)]
if missing: raise SystemExit("REJECT: missing "+",".join(missing))
print("PROVENANCE_GATE_PASS")
print("NOTE: sensor/Pd semantics still require separate validation")
