#!/usr/bin/env python3
"""Linear interpolation of published Inmarsat ECEF state vectors.
For validation/arc reconstruction only; does not claim sub-second operator ephemeris.
"""
import csv,argparse,datetime as dt
def sec(s):
 h,m,z=map(int,s.split(":")); return h*3600+m*60+z+(86400 if h<12 else 0)
def main():
 p=argparse.ArgumentParser();p.add_argument("states");p.add_argument("time");a=p.parse_args()
 rows=list(csv.DictReader(open(a.states,encoding="utf-8"))); t=sec(a.time)
 rows.sort(key=lambda r:sec(r["time_utc"]))
 lo=hi=None
 for x,y in zip(rows,rows[1:]):
  if sec(x["time_utc"])<=t<=sec(y["time_utc"]):lo,hi=x,y;break
 if lo is None:raise SystemExit("FAIL_CLOSED outside published state interval")
 f=(t-sec(lo["time_utc"]))/(sec(hi["time_utc"])-sec(lo["time_utc"]))
 keys=("x_km","y_km","z_km","vx_km_s","vy_km_s","vz_km_s")
 print("time_utc,"+",".join(keys))
 print(a.time+","+",".join(str(float(lo[k])+f*(float(hi[k])-float(lo[k]))) for k in keys))
if __name__=="__main__":main()
