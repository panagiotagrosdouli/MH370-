#!/usr/bin/env python3
"""Detect SATCOM metadata contradictions before likelihood construction."""
import csv,argparse
def rows(path):
 with open(path,encoding="utf-8") as f:
  lines=[x for x in f if not x.startswith("#")]
 return list(csv.DictReader(lines))
def main():
 p=argparse.ArgumentParser();p.add_argument("csv");a=p.parse_args();bad=0
 for r in rows(a.csv):
  ev=r.get("event","").lower(); ch=r.get("channel",""); sig=r.get("bto_sigma_us","")
  if "logon" in ev and r.get("bto_raw_us",""):
   if ch=="R1200" and sig=="29":
    print("WARN logon row uses R1200/29us metadata:",r.get("time_utc"));bad+=1
 print("metadata_warnings",bad)
if __name__=="__main__":main()
