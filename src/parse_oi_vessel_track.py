#!/usr/bin/env python3
"""Parse Ocean Infinity vessel-track KML/KMZ as PROXY geometry only.

Output is a CSV of coordinates and provenance. It deliberately contains no
buffering and no Pd calculation because vessel track != AUV sonar coverage.
"""
import argparse,csv,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
def read_bytes(p):
 p=Path(p)
 if p.suffix.lower() in {".kmz",".zip"}:
  with zipfile.ZipFile(p) as z:
   names=[n for n in z.namelist() if n.lower().endswith(".kml")]
   if not names: raise SystemExit("no KML in archive")
   return z.read(names[0])
 return p.read_bytes()
def main():
 ap=argparse.ArgumentParser();ap.add_argument("input");ap.add_argument("output");a=ap.parse_args()
 root=ET.fromstring(read_bytes(a.input)); rows=[]
 for e in root.iter():
  if e.tag.endswith("coordinates") and e.text:
   for token in e.text.replace("\n"," ").split():
    parts=token.split(",")
    if len(parts)>=2:
     rows.append({"lon":parts[0],"lat":parts[1],"alt":parts[2] if len(parts)>2 else "",
      "classification":"OI_VESSEL_TRACK_PROXY","pd_allowed":"false"})
 if not rows: raise SystemExit("no coordinates found")
 with open(a.output,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print("points",len(rows));print("WARNING: vessel track is not sonar coverage; Pd assignment prohibited")
if __name__=="__main__":main()
