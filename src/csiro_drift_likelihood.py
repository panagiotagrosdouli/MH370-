#!/usr/bin/env python3
"""Evidence-safe CSIRO drift latitude likelihood.

Consumes explicit, source-derived support values by latitude. It does not
invent a Gaussian around 35S and it keeps Part-III imagery-conditioned
evidence separable from debris-only drift evidence.
"""
import argparse,csv,os,math
def main():
 p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("--out",default="results/csiro_drift_latitude_likelihood.csv")
 p.add_argument("--include-imagery-conditioned",action="store_true");a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f); req={"latitude_deg","support","evidence_family","source","provenance"}
  if not req<=set(r.fieldnames or []): raise SystemExit("FAIL_CLOSED missing required columns")
  rows=list(r)
 allowed={"DEBRIS_DRIFT","SURFACE_SEARCH","AFRICA_TIMING","AUSTRALIA_NONDETECTION"}
 if a.include_imagery_conditioned: allowed.add("PLEIADES_CONDITIONED")
 rows=[x for x in rows if x["evidence_family"] in allowed]
 if not rows: raise SystemExit("FAIL_CLOSED no admissible rows")
 by={}
 for x in rows:
  lat=float(x["latitude_deg"]); v=float(x["support"])
  if not math.isfinite(lat) or not math.isfinite(v) or v<0: raise SystemExit("FAIL_CLOSED invalid value")
  by[lat]=by.get(lat,0.0)+v
 z=sum(by.values())
 if z<=0: raise SystemExit("FAIL_CLOSED zero support")
 out=[{"latitude_deg":lat,"drift_likelihood":v/z,"mode":"WITH_PLEIADES" if a.include_imagery_conditioned else "DEBRIS_ONLY"}
      for lat,v in sorted(by.items())]
 os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
