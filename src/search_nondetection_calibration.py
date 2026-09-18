#!/usr/bin/env python3
"""Search negative-evidence calibration without false cell precision."""
import argparse,csv,math
def nd(cls,pd_high,pd_low):
    if cls=="DATA_GAP": return 1.0
    if cls=="LOWER_CONFIDENCE": return 1.0-pd_low
    if cls=="HIGH_CONFIDENCE": return 1.0-pd_high
    raise ValueError("unknown coverage class")
def main():
    p=argparse.ArgumentParser()
    p.add_argument("input"); p.add_argument("--output",required=True)
    p.add_argument("--high-pd",type=float,default=.95)
    p.add_argument("--low-pd",type=float,default=.70)
    a=p.parse_args()
    if not (.95 <= a.high_pd < 1): raise SystemExit("high Pd must be >=.95 and <1")
    if not (0 <= a.low_pd <= 1): raise SystemExit("invalid lower-confidence Pd")
    with open(a.input,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    if not rows or "coverage_class" not in rows[0]: raise SystemExit("FAIL_CLOSED missing coverage_class")
    for r in rows: r["p_non_detection"]=nd(r["coverage_class"],a.high_pd,a.low_pd)
    fields=list(rows[0])+["p_non_detection"]
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
if __name__=="__main__": main()
