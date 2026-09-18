#!/usr/bin/env python3
"""Reconstruct a BTO constant-range arc on WGS84 from published satellite ECEF."""
import argparse,csv,math
A=6378.137; F=1/298.257223563; E2=F*(2-F); C=299792.458
GES=(-2368.8,4881.1,-3342.0); BIAS=-495679.0
def ecef(lat,lon,h=10.0):
 p=math.radians(lat);l=math.radians(lon);n=A/math.sqrt(1-E2*math.sin(p)**2)
 return ((n+h)*math.cos(p)*math.cos(l),(n+h)*math.cos(p)*math.sin(l),(n*(1-E2)+h)*math.sin(p))
def d(a,b):return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def target(bto,sat):
 # Ashton convention: total GES-SAT-AES path = c*(BTO-bias)/2
 return .5*C*(bto-BIAS)*1e-6-d(sat,GES)
def root(lat,sat,r,lo=70,hi=110):
 def f(lon):return d(ecef(lat,lon),sat)-r
 step=.1;x=lo;fx=f(x)
 while x<hi:
  y=min(x+step,hi);fy=f(y)
  if fx*fy<=0:
   a,b=x,y
   for _ in range(60):
    m=(a+b)/2;fm=f(m)
    if f(a)*fm<=0:b=m
    else:a=m
   return (a+b)/2
  x,fx=y,fy
 return None
def main():
 p=argparse.ArgumentParser();p.add_argument("--bto",type=float,default=18400);p.add_argument("--sat",nargs=3,type=float,required=True);p.add_argument("--out",required=True);a=p.parse_args()
 sat=tuple(a.sat);r=target(a.bto,sat)
 with open(a.out,"w",newline="") as f:
  w=csv.writer(f);w.writerow(["latitude_deg","longitude_deg","altitude_km","target_sat_aircraft_km"])
  lat=-45
  while lat<=-20:
   lon=root(lat,sat,r)
   if lon is not None:w.writerow([round(lat,3),round(lon,6),10.0,round(r,3)])
   lat+=.05
 print("target_sat_aircraft_km",r)
if __name__=="__main__":main()
