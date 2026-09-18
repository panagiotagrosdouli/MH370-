#!/usr/bin/env python3
"""Classify cross-arc cells using only published ATSB width bounds.

Sensitivity diagnostic only: this is NOT a substitute for actual search polygons.
Sign convention: negative=west, positive=east.
"""
import argparse,csv
def cls(d):
    if d < 0:
        a=abs(d)
        if a>21: return "DEFINITELY_OUTSIDE_2016_WIDTH_BOUND"
        if a>10: return "POSSIBLY_OUTSIDE_2016_WIDTH_BOUND"
        return "WITHIN_PUBLISHED_MIN_SEARCH_WIDTH"
    else:
        if d>17: return "DEFINITELY_OUTSIDE_2016_WIDTH_BOUND"
        if d>12: return "POSSIBLY_OUTSIDE_2016_WIDTH_BOUND"
        return "WITHIN_PUBLISHED_MIN_SEARCH_WIDTH"
def main():
 p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output");a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
 if not rows or "cross_arc_nm" not in rows[0]: raise SystemExit("cross_arc_nm required")
 for r in rows:
  r["historical_width_bound_status"]=cls(float(r["cross_arc_nm"]))
  r["historical_width_bound_provenance"]="ATSB_FIRST_PRINCIPLES_RANGE_ONLY"
 with open(a.output,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
if __name__=="__main__":main()
