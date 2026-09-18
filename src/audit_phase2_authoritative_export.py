#!/usr/bin/env python3
"""Acceptance gate for an authoritative Phase-2 residual export.

The 2022 GA/ATSB review is the currently verified primary aggregate benchmark:
72.79 km2 of holidays/LPDs within the reviewed 40-NM area, including 71.22
km2 documented during the original Phase-2 search plus 1.57 km2 of additional
holidays identified in the 2022 review.

Class areas are not a polygon-count checksum for the entire Phase-2 archive.
Use them only when the imported dataset declares the same spatial scope.
"""
EXPECTED_AREA={"Additional missing data":1.57,"Equipment Failure":5.37,
               "LPD":48.91,"Off-tracks":0.17,"Terrain avoidance":8.44,
               "Shadow zones":8.33}
TOTAL_AREA=72.79
def audit_areas(rows, class_key="class", area_key="area_km2", tolerance=0.10):
    got={}
    for r in rows:
        k=r[class_key]; got[k]=got.get(k,0.0)+float(r[area_key])
    failures=[]
    for k,e in EXPECTED_AREA.items():
        if k in got and abs(got[k]-e)>tolerance:
            failures.append(f"{k}: area {got[k]:.2f} != benchmark {e:.2f}")
    total=sum(got.values())
    if abs(total-TOTAL_AREA)>tolerance:
        failures.append(f"total area {total:.2f} != benchmark {TOTAL_AREA:.2f}")
    return failures
