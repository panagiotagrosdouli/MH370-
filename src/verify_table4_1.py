#!/usr/bin/env python3
"""Verify arithmetic in ATSB/Fugro Table 4.1 transcription."""
import csv,sys
from decimal import Decimal
p=sys.argv[1] if len(sys.argv)>1 else "data/GA_REMAINING_HOLIDAYS_TABLE4_1.csv"
rows=[]
with open(p,newline="",encoding="utf-8") as f:
 for r in csv.DictReader(line for line in f if not line.startswith("#")):
  if r["category"].startswith("TOTAL_"): continue
  rows.append(r)
count=sum(int(r["polygon_count"]) for r in rows)
area=sum(Decimal(r["area_km2"]) for r in rows)
lpd=next(r for r in rows if r["category"]=="Lower Probability of Detection")
lpd_area=Decimal(lpd["area_km2"]); lpd_count=int(lpd["polygon_count"])
print("total_count",count)
print("total_area_km2",area)
print("non_lpd_count",count-lpd_count)
print("non_lpd_area_km2",area-lpd_area)
print("lpd_area_share_pct",(lpd_area/area*100).quantize(Decimal("0.0001")))
assert count==12708
assert area==Decimal("3078.12")
assert count-lpd_count==5268
assert area-lpd_area==Decimal("568.03")
