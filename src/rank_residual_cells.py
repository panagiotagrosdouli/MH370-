"""Rank MH370 residual search cells without inventing missing search geometry.

Inputs are machine-readable cell tables assembled from authoritative geometry.
The engine intentionally separates evidence families and refuses to allocate
Ocean Infinity negative evidence unless cell-level coverage is supplied.
"""
from __future__ import annotations
import argparse
import csv
import math
from pathlib import Path

REQUIRED = {"lat","lon","physics","drift","eof","pd_atsb_ga"}
OPTIONAL_PD = ("pd_oi2018","pd_oi2025_26")

def f(row, key, default=None):
    v = row.get(key, "")
    if v in ("", None):
        return default
    return float(v)

def validate_prob(x, name):
    if x is None: return
    if not 0 <= x <= 1: raise ValueError(f"{name} outside [0,1]: {x}")

def score(row):
    base = f(row,"physics") * f(row,"drift") * f(row,"eof")
    pd = f(row,"pd_atsb_ga")
    validate_prob(pd,"pd_atsb_ga")
    nd = 1-pd
    for key in OPTIONAL_PD:
        x=f(row,key,None)
        # Missing geometry => neutral likelihood, never guessed coverage.
        if x is not None:
            validate_prob(x,key); nd *= (1-x)
    return base*nd

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--out",default="results/ranked_residual_cells.csv")
    args=ap.parse_args()
    with open(args.input,newline="",encoding="utf-8") as h:
        r=csv.DictReader(h); fields=set(r.fieldnames or [])
        miss=REQUIRED-fields
        if miss: raise SystemExit(f"Missing required columns: {sorted(miss)}")
        rows=list(r)
    for row in rows: row["raw_residual_score"]=score(row)
    z=sum(x["raw_residual_score"] for x in rows)
    if not math.isfinite(z) or z<=0: raise SystemExit("Residual posterior has zero/non-finite mass")
    for row in rows: row["posterior_residual"]=row["raw_residual_score"]/z
    rows.sort(key=lambda x:x["posterior_residual"],reverse=True)
    cum=0.0
    for i,row in enumerate(rows,1):
        cum += row["posterior_residual"]
        row["rank"]=i; row["cumulative_mass"]=cum
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    names=list(rows[0].keys())
    with out.open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=names); w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} ranked cells; top cumulative mass={cum:.6f}")

if __name__ == "__main__": main()
