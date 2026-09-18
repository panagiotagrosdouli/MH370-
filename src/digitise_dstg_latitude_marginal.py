#!/usr/bin/env python3
"""Validate a digitised DSTG Fig 10.3 latitude marginal.

Input points are manual/vector-extracted samples of the published curve.
No image-colour probability inference is performed.
"""
import argparse,csv,math,os
def main():
 p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("--out",default="results/dstg_latitude_marginal.csv");a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f); req={"latitude_deg","relative_frequency","panel","source_page","provenance"}
  if not req<=set(r.fieldnames or []):raise SystemExit("FAIL_CLOSED missing digitisation fields")
  rows=[x for x in r if x["panel"]=="BTO_BFO"]
 if len(rows)<3:raise SystemExit("FAIL_CLOSED insufficient BTO+BFO curve samples")
 pts=sorted((float(x["latitude_deg"]),float(x["relative_frequency"])) for x in rows)
 if any(not math.isfinite(y) or y<0 for _,y in pts):raise SystemExit("FAIL_CLOSED invalid relative frequency")
 # trapezoidal normalization in latitude; preserves the published 1-D marginal semantics
 area=sum((pts[i+1][0]-pts[i][0])*(pts[i+1][1]+pts[i][1])/2 for i in range(len(pts)-1))
 if area<=0:raise SystemExit("FAIL_CLOSED non-positive curve integral")
 out=[{"latitude_deg":x,"density_per_degree":y/area,"source":"DSTG_FIG10_3_BTO_BFO"} for x,y in pts]
 os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
