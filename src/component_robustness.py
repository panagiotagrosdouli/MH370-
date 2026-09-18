#!/usr/bin/env python3
"""Robustness score for residual components across sensitivity/ablation scenarios."""
import argparse,csv,collections,statistics,math,os
def main():
 ap=argparse.ArgumentParser();ap.add_argument("input");ap.add_argument("--out",default="results/component_robustness.csv");a=ap.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f); req={"scenario","component_id","rank","posterior_mass"}
  if not req<=set(r.fieldnames or []):raise SystemExit("FAIL_CLOSED missing required columns")
  rows=list(r)
 scenarios=sorted({x["scenario"] for x in rows}); n=len(scenarios)
 if n<2:raise SystemExit("FAIL_CLOSED need >=2 scenarios")
 by=collections.defaultdict(dict)
 for x in rows:
  by[x["component_id"]][x["scenario"]]=(int(x["rank"]),float(x["posterior_mass"]))
 out=[]
 for cid,d in by.items():
  if len(d)!=n:raise SystemExit("FAIL_CLOSED incomplete scenario coverage for "+cid)
  ranks=[d[s][0] for s in scenarios]; masses=[d[s][1] for s in scenarios]
  # Stability descriptors, not a new posterior probability.
  med=statistics.median(ranks); worst=max(ranks); best=min(ranks)
  top3=sum(r<=3 for r in ranks)/n
  cv=statistics.pstdev(masses)/statistics.mean(masses) if statistics.mean(masses)>0 else math.inf
  out.append({"component_id":cid,"scenarios":n,"median_rank":med,"best_rank":best,"worst_rank":worst,
              "top3_fraction":top3,"mass_mean":statistics.mean(masses),"mass_min":min(masses),
              "mass_max":max(masses),"mass_cv":cv})
 out.sort(key=lambda x:(x["median_rank"],x["worst_rank"],-x["top3_fraction"],x["mass_cv"]))
 os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  cols=list(out[0]);w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
