#!/usr/bin/env python3
"""Pd sensitivity + leave-one-evidence-out ablations for ranked MH370 cells."""
import argparse,csv,math,os

def read(p):
    with open(p,newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def nd(c,h,l):
    c=c.upper().strip()
    if c=="DATA_GAP":return 1.
    if c=="LOWER_CONFIDENCE":return 1-l
    if c=="HIGH_CONFIDENCE":return 1-h
    raise ValueError(c)
def score(rows,h,l,drop):
    z=[]; total=0.
    for r in rows:
        terms={k:float(r[k]) for k in ("physics","drift","eof")}
        s=1.
        for k,v in terms.items():
            if k not in drop:s*=v
        if "search" not in drop:s*=nd(r["coverage_class"],h,l)
        z.append((r["cell_id"],s));total+=s
    if total<=0:raise ValueError("zero mass")
    z.sort(key=lambda x:x[1],reverse=True)
    return {cid:(i+1,s/total) for i,(cid,s) in enumerate(z)}
def main():
    a=argparse.ArgumentParser();a.add_argument("input");a.add_argument("--out",default="results/pd_ablation_sensitivity.csv");x=a.parse_args()
    rows=read(x.input)
    scenarios=[]
    for h in (.95,.97,.99):
      for l in (.50,.70,.90): scenarios.append((f"pd_h{h:.2f}_l{l:.2f}",h,l,set()))
    scenarios += [("drop_drift",.95,.70,{"drift"}),("drop_eof",.95,.70,{"eof"}),("drop_search",.95,.70,{"search"})]
    out=[]
    for name,h,l,drop in scenarios:
      rr=score(rows,h,l,drop)
      for cid,(rank,p) in rr.items():out.append({"scenario":name,"cell_id":cid,"rank":rank,"posterior_mass":f"{p:.12g}"})
    os.makedirs(os.path.dirname(x.out) or ".",exist_ok=True)
    with open(x.out,"w",newline="",encoding="utf-8") as f:
      w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
