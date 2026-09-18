#!/usr/bin/env python3
"""Filter a recovered historical iy57 File_Links.txt for GIS evidence targets."""
import sys
TOKENS=("/gis/","holiday",".gdb",".shp","coverage","trackline")
def hits(lines):
    out=[]
    for line in lines:
        s=line.strip()
        low=s.lower()
        score=sum(t in low for t in TOKENS)
        if score:
            out.append((score,s))
    return sorted(out,key=lambda x:(-x[0],x[1]))
if __name__=="__main__":
    for score,path in hits(sys.stdin):
        print(f"{score}\t{path}")
