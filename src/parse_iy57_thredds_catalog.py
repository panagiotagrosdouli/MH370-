#!/usr/bin/env python3
"""Parse a recovered THREDDS catalog.xml without guessing child filenames.

Usage:
  python src/parse_iy57_thredds_catalog.py catalog.xml

Prints catalogRef targets and dataset urlPath values, prioritising GIS/holiday/
coverage/trackline/geodatabase candidates.
"""
import sys, xml.etree.ElementTree as ET
KEYS=("gis","holiday","coverage","trackline",".gdb",".shp","contact")
def score(s):
    x=s.lower()
    return sum(1 for k in KEYS if k in x)
def main(path):
    root=ET.parse(path).getroot()
    rows=[]
    for e in root.iter():
        a=e.attrib
        vals=[a.get("name",""),a.get("urlPath",""),a.get("{http://www.w3.org/1999/xlink}href","")]
        joined=" | ".join(v for v in vals if v)
        if joined:
            rows.append((score(joined),e.tag.split("}")[-1],joined))
    for s,t,v in sorted(rows,key=lambda x:(-x[0],x[1],x[2])):
        if s or t=="catalogRef": print(s,t,v)
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: parse_iy57_thredds_catalog.py catalog.xml")
    main(sys.argv[1])
