#!/usr/bin/env python3
"""Validate provenance contract for digitised DSTG/ATSB posterior grids."""
import argparse,csv
def main():
 ap=argparse.ArgumentParser();ap.add_argument("input");ap.add_argument("--product",required=True,choices=["DSTG_ONLY","ATSB_DSTG_PLUS_EOF"]);ap.add_argument("--apply-eof",action="store_true");a=ap.parse_args()
 if a.product=="ATSB_DSTG_PLUS_EOF" and a.apply_eof:
  raise SystemExit("FAIL_CLOSED: EOF double counting")
 with open(a.input,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f);req={"lat","lon","density","source_page","provenance"}
  if not req<=set(r.fieldnames or []):raise SystemExit("FAIL_CLOSED missing digitisation metadata")
  rows=list(r)
 if not rows:raise SystemExit("FAIL_CLOSED empty grid")
 vals=[float(x["density"]) for x in rows]
 if any(v<0 for v in vals) or sum(vals)<=0:raise SystemExit("FAIL_CLOSED invalid density")
 prov={x["provenance"] for x in rows}
 if len(prov)!=1:raise SystemExit("FAIL_CLOSED mixed provenance")
 print("PASS",a.product,"rows",len(rows),"apply_eof",a.apply_eof)
if __name__=="__main__":main()
