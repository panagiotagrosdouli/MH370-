#!/usr/bin/env python3
"""First-principles ECEF Doppler primitives for MH370 BFO reconstruction."""
import math
C=299792.458
FU=1646.6525e6
FD=3615.1525e6
A=6378.137
F=1/298.257223563
E2=F*(2-F)
OMEGA=7.2921150e-5
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def unit(a):
 n=norm(a); return tuple(x/n for x in a)
def geodetic_ecef(lat,lon,h_km):
 p=math.radians(lat);l=math.radians(lon);N=A/math.sqrt(1-E2*math.sin(p)**2)
 return ((N+h_km)*math.cos(p)*math.cos(l),(N+h_km)*math.cos(p)*math.sin(l),(N*(1-E2)+h_km)*math.sin(p))
def aircraft_ecef_velocity(lat,lon,track_deg,speed_kph,vertical_kph=0):
 p=math.radians(lat);l=math.radians(lon);t=math.radians(track_deg)
 vn=speed_kph/3600*math.cos(t); ve=speed_kph/3600*math.sin(t); vu=vertical_kph/3600
 east=(-math.sin(l),math.cos(l),0)
 north=(-math.sin(p)*math.cos(l),-math.sin(p)*math.sin(l),math.cos(p))
 up=(math.cos(p)*math.cos(l),math.cos(p)*math.sin(l),math.sin(p))
 return tuple(vn*north[i]+ve*east[i]+vu*up[i] for i in range(3))
def doppler(receiver_pos,receiver_vel,transmitter_pos,transmitter_vel,freq):
 los=unit(sub(receiver_pos,transmitter_pos))
 closing=dot(sub(receiver_vel,transmitter_vel),los)
 return -freq*closing/C
def uplink(air_pos,air_vel,sat_pos,sat_vel): return doppler(sat_pos,sat_vel,air_pos,air_vel,FU)
def downlink(sat_pos,sat_vel,ges_pos): return doppler(ges_pos,(0,0,0),sat_pos,sat_vel,FD)
