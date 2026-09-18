#!/usr/bin/env python3
"""Validate ECEF Doppler kernel against the stationary 16:30 primary calibration row."""
from bfo_ecef_kernel import geodetic_ecef,uplink,downlink
SAT=(18122.9,38080.0,828.5)
SATV=(0.00216,-0.00107,0.06390)
AIR=geodetic_ecef(2.75,101.71,0.0)
AIRV=(0.0,0.0,0.0)
GES=(-2368.8,4881.1,-3342.0)
u=uplink(AIR,AIRV,SAT,SATV)
d=downlink(SAT,SATV,GES)
print("uplink_hz",u,"target",-6)
print("downlink_hz",d,"target",-85)
print("uplink_error_hz",u+6)
print("downlink_error_hz",d+85)
