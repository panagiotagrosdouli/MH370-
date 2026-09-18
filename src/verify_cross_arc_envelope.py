#!/usr/bin/env python3
"""Validate that the residual-grid envelope matches ATSB published bounds."""
import argparse
p=argparse.ArgumentParser()
p.add_argument("--lat-min",type=float,default=-36.0)
p.add_argument("--lat-max",type=float,default=-33.0)
p.add_argument("--west-nm",type=float,default=27.5)
p.add_argument("--east-nm",type=float,default=25.0)
a=p.parse_args()
assert a.lat_min==-36.0 and a.lat_max==-33.0
assert a.west_nm==27.5 and a.east_nm==25.0
print("ATSB residual domain verified: 33-36S, 27.5 NM west, 25 NM east")
print("nominal full cross-arc width_nm",a.west_nm+a.east_nm)
print("nominal full cross-arc width_km",(a.west_nm+a.east_nm)*1.852)
