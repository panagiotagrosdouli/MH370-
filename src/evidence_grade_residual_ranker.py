#!/usr/bin/env python3
"""Evidence-gated MH370 residual ranking engine.

Inputs are authoritative cell-level CSVs. Missing required evidence fails closed.
No proxy geometry is accepted as evidence-grade.
"""
import argparse, csv, math, sys

REQ = ["cell_id","lat","lon","physics","drift","eof","coverage_class","geometry_provenance"]

def pd_nd(cls, high_pd):
    c=cls.strip().upper()
    if c=="DATA_GAP": return 1.0
    if c=="LOWER_CONFIDENCE": return 0.30
    if c=="HIGH_CONFIDENCE": return 1.0-high_pd
    raise ValueError("unrecognised coverage_class: "+cls)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--out",default="results/evidence_grade_residual_ranking.csv")
    ap.add_argument("--high-pd",type=float,default=0.95)
    a=ap.parse_args()
    if not (0.95 <= a.high_pd < 1): raise SystemExit("high-pd must be >=0.95 and <1")
    with open(a.input,newline="",encoding="utf-8") as f:
        r=csv.DictReader(f)
        missing=[x for x in REQ if x not in (r.fieldnames or [])]
        if missing: raise SystemExit("FAIL_CLOSED missing columns: "+",".join(missing))
        rows=list(r)
    out=[]
    for x in rows:
        prov=x["geometry_provenance"].strip().upper()
        if prov not in {"GA_AUTHORITATIVE_GIS","ATSB_AUTHORITATIVE_GIS","AUTHORITATIVE_DERIVED_FROM_SOURCE_RASTER"}:
            raise SystemExit("FAIL_CLOSED non-authoritative geometry in cell "+x["cell_id"])
        vals=[float(x[k]) for k in ("physics","drift","eof")]
        if any(v<0 for v in vals): raise SystemExit("negative likelihood/prior term")
        nd=pd_nd(x["coverage_class"],a.high_pd)
        score=math.prod(vals)*nd
        y=dict(x); y["p_nd"]=f"{nd:.8g}"; y["score_raw"]=f"{score:.12g}"; out.append(y)
    z=sum(float(x["score_raw"]) for x in out)
    if z<=0: raise SystemExit("FAIL_CLOSED zero posterior mass")
    out.sort(key=lambda x:float(x["score_raw"]),reverse=True)
    cum=0
    for rank,x in enumerate(out,1):
        p=float(x["score_raw"])/z; cum+=p
        x["rank"]=rank; x["posterior_mass"]=f"{p:.12g}"; x["cumulative_mass"]=f"{cum:.12g}"
    fields=list(out[0].keys())
    with open(a.out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(out)
    print("ranked",len(out),"cells; output",a.out)

if __name__=="__main__": main()
