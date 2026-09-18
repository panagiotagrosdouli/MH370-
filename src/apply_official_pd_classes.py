#!/usr/bin/env python3
"""Apply official ATSB detection-class semantics to already classified cells.

Input must already contain an authoritative 'coverage_class'. This program
refuses to infer a class from WMS/catalogue footprints.
"""
import argparse,csv
CLASSES={
 "HIGH_CONFIDENCE":{"pd_min":0.95,"pd_ref":"","note":"ATSB definition >95%; exact Pd not specified"},
 "LOWER_CONFIDENCE":{"pd_min":"","pd_ref":0.70,"note":"ATSB reports ~70% average; use sensitivity"},
 "DATA_GAP":{"pd_min":0.0,"pd_ref":0.0,"note":"ATSB definition zero confidence"},
}
def main():
 p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output"); a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
 if not rows or "coverage_class" not in rows[0]: raise SystemExit("coverage_class required; refusing to infer class")
 out=[]
 for r in rows:
  c=r["coverage_class"].strip().upper()
  if c not in CLASSES: raise SystemExit(f"unrecognized/unclassified coverage_class: {c!r}")
  z=CLASSES[c]; r.update({"pd_min":z["pd_min"],"pd_reference":z["pd_ref"],"pd_note":z["note"]}); out.append(r)
 with open(a.output,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
if __name__=="__main__": main()
