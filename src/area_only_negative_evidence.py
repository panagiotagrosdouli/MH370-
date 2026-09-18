#!/usr/bin/env python3
"""Area-only posterior bounds for ATSB sonar classes.

This is deliberately NOT a geographic posterior. It answers a narrower
question: under equal prior density inside an already-selected search area,
how much surviving mass can each coverage class retain after a non-detection?
"""
import argparse,csv
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--high-area",type=float,default=97.4)
 p.add_argument("--low-area",type=float,default=2.1)
 p.add_argument("--gap-area",type=float,default=.5)
 p.add_argument("--high-pd",type=float,default=.95)
 p.add_argument("--low-pd",type=float,default=.70)
 a=p.parse_args()
 if not (.95<=a.high_pd<1): raise SystemExit("high Pd must be >=.95 and <1")
 if not (0<=a.low_pd<=1): raise SystemExit("bad low Pd")
 raw={"HIGH_CONFIDENCE":a.high_area*(1-a.high_pd),
      "LOWER_CONFIDENCE":a.low_area*(1-a.low_pd),
      "DATA_GAP":a.gap_area}
 z=sum(raw.values())
 w=csv.writer(__import__("sys").stdout)
 w.writerow(["class","area_share_pct","pd_assumption","surviving_mass_share"])
 areas={"HIGH_CONFIDENCE":a.high_area,"LOWER_CONFIDENCE":a.low_area,"DATA_GAP":a.gap_area}
 pds={"HIGH_CONFIDENCE":a.high_pd,"LOWER_CONFIDENCE":a.low_pd,"DATA_GAP":0}
 for k in raw:w.writerow([k,areas[k],pds[k],raw[k]/z])
if __name__=="__main__":main()
