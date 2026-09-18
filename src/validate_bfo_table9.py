#!/usr/bin/env python3
"""Validate BFO bookkeeping against Inmarsat Table 9 before coding geometry."""
import math
ROWS=[
("19:41:03",32,-1,0,-72,-1,150,108,111),
("20:41:05",-182,5,29,143,-1,150,143,141),
("21:41:27",-365,16,55,331,-18,150,170,168),
("22:41:22",-522,29,78,497,-29,150,203,204),
("23:14:00",-595,37,88,575,-33,150,222,217),
("00:11:00",-702,50,101,691,-38,150,252,252),
("00:19:29",-717,52,102,708,-38,150,256,182),
]
stable=[]
for t,up_air,up_sat,down,comp,afc_sat,bias,pub,meas in ROWS:
 calc=up_air+up_sat+down+comp+afc_sat+bias
 assert calc==pub,(t,calc,pub)
 resid=meas-calc
 if t!="00:19:29": stable.append(resid)
 print(t,calc,meas,resid)
print("pre_eof_rms_hz",math.sqrt(sum(x*x for x in stable)/len(stable)))
