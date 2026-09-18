#!/usr/bin/env python3
"""Guard against SATCOM evidence double counting.

Exactly one physics route is allowed:
A) DSTG_POSTERIOR: already combines SATCOM/dynamics/met/calibration.
B) RAW_SATCOM: independently reconstructed BTO/BFO likelihood.
"""
import argparse,csv,os
def main():
 ap=argparse.ArgumentParser();ap.add_argument("input");ap.add_argument("--mode",required=True,choices=["DSTG_POSTERIOR","RAW_SATCOM"]);ap.add_argument("--out",default="results/physics_input.csv");a=ap.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f); fields=set(r.fieldnames or []); rows=list(r)
 if "cell_id" not in fields:raise SystemExit("FAIL_CLOSED missing cell_id")
 if a.mode=="DSTG_POSTERIOR":
  if "dstg_density" not in fields:raise SystemExit("FAIL_CLOSED missing dstg_density")
  forbidden={"bto_likelihood","bfo_likelihood","raw_satcom_likelihood"}&fields
  if forbidden:raise SystemExit("FAIL_CLOSED double-count risk: "+",".join(sorted(forbidden)))
  key="dstg_density"
 else:
  if "raw_satcom_likelihood" not in fields:raise SystemExit("FAIL_CLOSED missing raw_satcom_likelihood")
  if "dstg_density" in fields:raise SystemExit("FAIL_CLOSED double-count risk: DSTG density present")
  key="raw_satcom_likelihood"
 out=[];z=0.
 for x in rows:
  v=float(x[key])
  if v<0:raise SystemExit("FAIL_CLOSED negative physics value")
  z+=v;out.append({"cell_id":x["cell_id"],"physics_raw":v,"physics_mode":a.mode})
 if z<=0:raise SystemExit("FAIL_CLOSED zero physics mass")
 for x in out:x["physics"]=x["physics_raw"]/z
 os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
