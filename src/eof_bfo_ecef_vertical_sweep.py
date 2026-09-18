#!/usr/bin/env python3
"""Held-out 00:19:29 vertical-speed sweep using the verified ECEF BFO kernel.

Illustrative Ashton Table-9 endpoint geometry only; not a location estimator.
"""
from bfo_ecef_kernel import geodetic_ecef,aircraft_ecef_velocity,uplink,downlink
from bfo_aes_compensation import compensation
from bfo_eafc_primary import correction
BIAS=150.0; MEASURED=182.0
GES=(-2368.8,4881.1,-3342.0)
P0=(18177.5,38051.7,440.0); P1=(18178.4,38050.8,390.5)
V0=(0.00160,-0.00151,-0.08188); V1=(0.00150,-0.00158,-0.08321)
F=569.0/600.0
SAT_POS=tuple(P0[i]+F*(P1[i]-P0[i]) for i in range(3))
SAT_VEL=tuple(V0[i]+F*(V1[i]-V0[i]) for i in range(3))
LAT,LON,TRACK,SPEED=-34.7,93.0,180.0,829.0
AP=geodetic_ecef(LAT,LON,10.0)
def predict(descent_fpm):
    # positive descent_fpm means downward; kernel vertical velocity is positive up.
    vertical_kph=-descent_fpm*0.3048*60.0/1000.0
    av=aircraft_ecef_velocity(LAT,LON,TRACK,SPEED,vertical_kph)
    return (uplink(AP,av,SAT_POS,SAT_VEL)+downlink(SAT_POS,SAT_VEL,GES)
            +compensation(LAT,LON,TRACK,SPEED)+correction("00:19:29")+BIAS)
if __name__=="__main__":
    p0=predict(0.0); p100=predict(100.0)
    sensitivity=p0-p100
    central=(p0-MEASURED)/sensitivity*100.0
    print("level_pred_hz",round(p0,6))
    print("vertical_sensitivity_hz_per_100fpm",round(sensitivity,6))
    print("central_descent_fpm",round(central,3))
    for d in (0,3800,central,4400,14200):
        print(round(d,3),round(predict(d),6),round(MEASURED-predict(d),6))
