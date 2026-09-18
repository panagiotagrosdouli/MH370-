#!/usr/bin/env python3
"""Rank authoritative residual polygons only after spatial evidence is attached."""
import csv,argparse,math
ALLOWED={"DATA_GAP","EQUIPMENT_FAILURE","OFF_TRACK","SHADOW_ZONE","TERRAIN_AVOIDANCE","LOWER_PD"}
def main():
 p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("--output",required=True);a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f:r=list(csv.DictReader(f))
 req={"polygon_id","area_km2","class","physics","drift","eof","p_non_detection","geometry_provenance"}
 if not r or not req<=set(r[0]):raise SystemExit("FAIL_CLOSED missing columns")
 out=[]
 for x in r:
  if x["class"] not in ALLOWED:raise SystemExit("FAIL_CLOSED unknown class")
  if x["geometry_provenance"] not in {"GA_AUTHORITATIVE_GIS","ATSB_AUTHORITATIVE_GIS","AUTHORITATIVE_DERIVED_FROM_SOURCE_RASTER"}:raise SystemExit("FAIL_CLOSED non-authoritative geometry")
  vals=[float(x[k]) for k in ("area_km2","physics","drift","eof","p_non_detection")]
  if any((not math.isfinite(v) or v<0) for v in vals):raise SystemExit("FAIL_CLOSED invalid numeric")
  x["residual_mass_proxy"]=vals[0]*vals[1]*vals[2]*vals[3]*vals[4];out.append(x)
 z=sum(float(x["residual_mass_proxy"]) for x in out)
 if z<=0:raise SystemExit("FAIL_CLOSED zero residual mass")
 for x in out:x["normalized_residual_mass"]=float(x["residual_mass_proxy"])/z
 out.sort(key=lambda x:float(x["normalized_residual_mass"]),reverse=True)
 fields=list(out[0])
 with open(a.output,"w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
