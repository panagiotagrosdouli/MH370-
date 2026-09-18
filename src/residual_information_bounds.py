#!/usr/bin/env python3
"""Compute information-only residual inventory shares and Pd likelihood ratios."""
from decimal import Decimal
areas={
 "equipment_failure":Decimal("17.10"),
 "offtracks":Decimal("19.20"),
 "shadow_zones":Decimal("312.94"),
 "terrain_avoidance":Decimal("218.79"),
 "lpd":Decimal("2510.09"),
}
total=sum(areas.values())
for k,v in areas.items():
 print(k, "area_km2=",v, "share_pct=", (v/total*100).quantize(Decimal("0.0001")))
print("total",total)
# Reference comparisons only. High-confidence Pd is strictly >.95.
nd_high_upper=Decimal("0.05")
nd_lpd_ref=Decimal("0.30")
nd_gap=Decimal("1")
print("gap_vs_high_density_ratio_lower_bound", ">", nd_gap/nd_high_upper)
print("lpd_ref_vs_high_density_ratio_lower_bound", ">", nd_lpd_ref/nd_high_upper)
