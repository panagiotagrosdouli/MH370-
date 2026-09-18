#!/usr/bin/env python3
"""End-to-end BFO forward validation on the Inmarsat Table-9 example path."""
import math
from bfo_ecef_kernel import geodetic_ecef,aircraft_ecef_velocity,uplink,downlink
from bfo_aes_compensation import compensation
from bfo_eafc_primary import correction
# Published I-3F1 states at 10-minute grid are interpolated elsewhere; this test
# consumes state vectors supplied by caller to avoid hiding ephemeris assumptions.
BIAS=150.0
ROWS=[
("19:41:03",0.0,93.7,186,800,111),
("20:41:05",-7.5,92.9,182,829,141),
("21:41:27",-15.0,92.7,180,829,168),
("22:41:22",-22.5,92.9,179,829,204),
("00:11:00",-33.7,93.0,180,829,252)]
def predict(row,sat_pos,sat_vel,ges_pos):
 t,lat,lon,trk,spd,meas=row
 ap=geodetic_ecef(lat,lon,10.0); av=aircraft_ecef_velocity(lat,lon,trk,spd)
 return uplink(ap,av,sat_pos,sat_vel)+downlink(sat_pos,sat_vel,ges_pos)+compensation(lat,lon,trk,spd)+correction(t)+BIAS
def rms(xs):return math.sqrt(sum(x*x for x in xs)/len(xs))
