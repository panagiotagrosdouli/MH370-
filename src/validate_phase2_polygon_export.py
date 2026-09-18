#!/usr/bin/env python3
"""Fail-closed validator for recovered Phase-2 polygon exports."""
import argparse,json
def main():
 p=argparse.ArgumentParser();p.add_argument("geojson");a=p.parse_args()
 d=json.load(open(a.geojson,encoding="utf-8"))
 if d.get("type")!="FeatureCollection":raise SystemExit("FAIL_CLOSED not FeatureCollection")
 fs=d.get("features",[])
 if not fs:raise SystemExit("FAIL_CLOSED empty layer")
 allowed={"Polygon","MultiPolygon"}
 bad=[i for i,f in enumerate(fs) if (f.get("geometry") or {}).get("type") not in allowed]
 if bad:raise SystemExit("FAIL_CLOSED non-polygon features present")
 for f in fs:
  p=f.get("properties") or {}
  prov=str(p.get("provenance",""))
  if prov not in {"GA_AUTHORITATIVE_GIS","ATSB_AUTHORITATIVE_GIS"}:
   raise SystemExit("FAIL_CLOSED missing authoritative provenance")
 print("PASS",len(fs),"authoritative polygon features")
if __name__=="__main__":main()
