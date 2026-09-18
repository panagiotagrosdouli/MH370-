#!/usr/bin/env python3
"""Generate the 00:19:29 BTO arc and altitude sensitivity from primary constants."""
import math,csv
A=6378.137;F=1/298.257223563;E2=F*(2-F);C=299792.458
BIAS=-495679.; BTO=18400.; GES=(-2368.8,4881.1,-3342.0)
# Linear interpolation 00:19:29 between published 00:10 and 00:20 I-3F1 states.
f=569/600
S0=(18177.5,38051.7,440.0); S1=(18178.4,38050.8,390.5)
SAT=tuple(x+f*(y-x) for x,y in zip(S0,S1))
def dist(p,q):return math.sqrt(sum((x-y)**2 for x,y in zip(p,q)))
def ecef(lat,lon,h):
 p=math.radians(lat);l=math.radians(lon);n=A/math.sqrt(1-E2*math.sin(p)**2)
 return ((n+h)*math.cos(p)*math.cos(l),(n+h)*math.cos(p)*math.sin(l),(n*(1-E2)+h)*math.sin(p))
R=.5*C*(BTO-BIAS)*1e-6-dist(SAT,GES)
def lon_at(lat,h):
 def z(lon):return dist(ecef(lat,lon,h),SAT)-R
 lo,step=70.,.05;flo=z(lo)
 while lo<110:
  hi=lo+step;fhi=z(hi)
  if flo*fhi<=0:
   for _ in range(70):
    m=(lo+hi)/2;fm=z(m)
    if flo*fm<=0:hi=m
    else:lo=m;flo=fm
   return (lo+hi)/2
  lo=hi;flo=fhi
 raise ValueError(lat)
with open("results_bto_arc7.csv","w",newline="") as f:
 w=csv.writer(f);w.writerow(["lat","lon_h0","lon_h10","lon_h12","spread_nm"])
 for i in range(251):
  lat=-45+i*.05; ls=[lon_at(lat,h) for h in (0,10,12)]
  km=(max(ls)-min(ls))*111.32*math.cos(math.radians(lat));w.writerow([lat,*ls,km/1.852])
print("sat",SAT,"range",R)
for lat in (-36,-35.6,-35,-34,-33):print(lat,lon_at(lat,10))
