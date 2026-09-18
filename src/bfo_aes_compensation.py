#!/usr/bin/env python3
"""AES Doppler compensation geometry for the Inmarsat Table-9 validation path."""
import math
C=299792.458
FU=1646.6525e6
RE=6378.137
H_NOM=35788.12
SAT_NOM_LON=64.5
def gc_distance(lat1,lon1,lat2,lon2):
 a,b,c,d=map(math.radians,(lat1,lon1,lat2,lon2))
 return RE*math.acos(max(-1,min(1,math.sin(a)*math.sin(c)+math.cos(a)*math.cos(c)*math.cos(b-d))))
def nominal_slant(lat,lon):
 theta=gc_distance(lat,lon,0,SAT_NOM_LON)/RE
 return math.sqrt(RE*RE+(RE+H_NOM)**2-2*RE*(RE+H_NOM)*math.cos(theta))
def compensation(lat,lon,track_deg,speed_kph,dt=0.1):
 # AES assumes zero vertical speed and nominal GEO satellite.
 d=speed_kph*dt/3600
 br=math.radians(track_deg);p=math.radians(lat);l=math.radians(lon)
 delta=d/RE
 p2=math.asin(math.sin(p)*math.cos(delta)+math.cos(p)*math.sin(delta)*math.cos(br))
 l2=l+math.atan2(math.sin(br)*math.sin(delta)*math.cos(p),math.cos(delta)-math.sin(p)*math.sin(p2))
 rr=(nominal_slant(math.degrees(p2),math.degrees(l2))-nominal_slant(lat,lon))/dt
 return FU*rr/C
if __name__=="__main__":
 rows=[("19:41",0,93.7,186,800,-72),("20:41",-7.5,92.9,182,829,143),("21:41",-15,92.7,180,829,331),("22:41",-22.5,92.9,179,829,497),("00:11",-33.7,93,180,829,691)]
 for r in rows: print(r[0],compensation(*r[1:5]),"target",r[5])
