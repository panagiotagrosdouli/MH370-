#!/usr/bin/env python3
"""Acceptance gate for authoritative Phase-2 residual polygon exports."""
EXPECTED={"Equipment Failure":(88,17.10),"Offtracks":(8,19.20),"Shadow":(5026,312.94),"Terrain Avoidance":(146,218.79),"LPD":(7440,2510.09)}
TOTAL_N=12708; TOTAL_A=3078.12
def audit(rows,count_key="count",area_key="area_km2",class_key="class"):
 got={}
 for r in rows:
  k=r[class_key]; n=int(r[count_key]); a=float(r[area_key])
  N,A=got.get(k,(0,0.0)); got[k]=(N+n,A+a)
 failures=[]
 for k,(en,ea) in EXPECTED.items():
  n,a=got.get(k,(0,0.0))
  if n!=en: failures.append(f"{k}: count {n} != {en}")
  if abs(a-ea)>0.05: failures.append(f"{k}: area {a:.2f} != {ea:.2f}")
 n=sum(x[0] for x in got.values()); a=sum(x[1] for x in got.values())
 if n!=TOTAL_N: failures.append(f"total count {n} != {TOTAL_N}")
 if abs(a-TOTAL_A)>0.10: failures.append(f"total area {a:.2f} != {TOTAL_A:.2f}")
 return failures
