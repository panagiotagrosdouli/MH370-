#!/usr/bin/env python3
"""Attach explicit falsification tests to residual components."""
import argparse,csv,os
TESTS=[
 ("AUTHORITATIVE_RESEARCH","Authoritative sonar coverage shows the component was searched at documented high Pd","recompute search non-detection likelihood"),
 ("OI_OVERLAP","Authoritative OI AUV/sonar geometry overlaps the component","apply documented OI Pd only after sensor/coverage validation"),
 ("DRIFT","Independent drift forcing materially suppresses the component across confirmed debris sites","rerun drift likelihood and ablation"),
 ("EOF","End-of-flight hypothesis incompatible with component's cross-arc displacement","set incompatible EOF branch likelihood to zero, retain other branches"),
 ("SATCOM_PHYSICS","Authoritative SATCOM/trajectory reconstruction excludes the component","remove excluded physics support"),
 ("SONAR_TARGET","Reacquired sonar target is physically confirmed elsewhere","terminate location ranking after physical confirmation")
]
def main():
 ap=argparse.ArgumentParser();ap.add_argument("components");ap.add_argument("--out",default="results/component_falsification_register.csv");a=ap.parse_args()
 with open(a.components,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f)
  if "component_id" not in (r.fieldnames or []):raise SystemExit("FAIL_CLOSED missing component_id")
  ids=sorted({x["component_id"].strip() for x in r if x["component_id"].strip()})
 if not ids:raise SystemExit("FAIL_CLOSED no components")
 out=[]
 for cid in ids:
  for tid,obs,action in TESTS:
   out.append({"component_id":cid,"test_id":tid,"falsifying_or_downweighting_observation":obs,"required_action":action,"status":"UNTESTED"})
 os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
if __name__=="__main__":main()
