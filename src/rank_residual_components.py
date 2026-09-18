#!/usr/bin/env python3
"""Rank connected residual components from evidence-grade cell ranking.

Input cells must have component_id, posterior_mass and area_km2.
The script aggregates mass/area and reports density; it does not invent adjacency.
"""
import argparse,csv,collections,os
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("--out",default="results/residual_components.csv"); a=ap.parse_args()
    with open(a.input,newline="",encoding="utf-8") as f:
        r=csv.DictReader(f); fields=set(r.fieldnames or [])
        req={"component_id","posterior_mass","area_km2"}
        if not req<=fields: raise SystemExit("FAIL_CLOSED missing: "+",".join(sorted(req-fields)))
        rows=list(r)
    agg=collections.defaultdict(lambda:{"mass":0.,"area":0.,"cells":0})
    for x in rows:
        cid=x["component_id"].strip()
        if not cid: raise SystemExit("FAIL_CLOSED blank component_id")
        p=float(x["posterior_mass"]); ar=float(x["area_km2"])
        if p<0 or ar<=0: raise SystemExit("FAIL_CLOSED invalid mass/area")
        agg[cid]["mass"]+=p; agg[cid]["area"]+=ar; agg[cid]["cells"]+=1
    out=[]
    for cid,v in agg.items():
        out.append({"component_id":cid,"posterior_mass":v["mass"],"area_km2":v["area"],"cells":v["cells"],"mass_per_km2":v["mass"]/v["area"]})
    out.sort(key=lambda x:x["posterior_mass"],reverse=True)
    cum=0.
    for i,x in enumerate(out,1):
        cum+=x["posterior_mass"]; x["rank"]=i; x["cumulative_mass"]=cum
    os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
    with open(a.out,"w",newline="",encoding="utf-8") as f:
        cols=["rank","component_id","posterior_mass","cumulative_mass","area_km2","mass_per_km2","cells"]
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(out)
if __name__=="__main__": main()
