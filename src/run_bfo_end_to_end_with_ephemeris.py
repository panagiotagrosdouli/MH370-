#!/usr/bin/env python3
"""Interpolate published I-3F1 ECEF states and feed end-to-end BFO validator."""
import csv,datetime,math
from validate_bfo_end_to_end import ROWS,predict,rms
GES=(-2368.8,4881.1,-3342.0)
def sec(t):
 h,m,s=map(int,t.split(":")); x=h*3600+m*60+s
 return x if h>=16 else x+86400
def load(path):
 out=[]
 for r in csv.DictReader(open(path,encoding="utf-8")):
  out.append((sec(r["time_utc"]),tuple(float(r[k]) for k in ("x_km","y_km","z_km")),tuple(float(r[k]) for k in ("vx_km_s","vy_km_s","vz_km_s"))))
 return sorted(out)
def interp(states,t):
 x=sec(t)
 for (a,p0,v0),(b,p1,v1) in zip(states,states[1:]):
  if a<=x<=b:
   f=(x-a)/(b-a)
   p=tuple(p0[i]+f*(p1[i]-p0[i]) for i in range(3))
   # Prefer linearly interpolated published velocity, not finite-difference position.
   v=tuple(v0[i]+f*(v1[i]-v0[i]) for i in range(3))
   return p,v
 raise ValueError(t)
def main(path="data/INMARSAT_3F1_ECEF_TABLE4.csv"):
 st=load(path); residuals=[]
 for row in ROWS:
  p,v=interp(st,row[0]); pred=predict(row,p,v,GES); res=row[-1]-pred
  residuals.append(res); print(row[0],"pred",round(pred,3),"meas",row[-1],"res",round(res,3))
 print("rms_hz",round(rms(residuals),3))
if __name__=="__main__":main()
