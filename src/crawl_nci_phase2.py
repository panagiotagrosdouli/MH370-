#!/usr/bin/env python3
"""Recover authoritative GA/NCI MH370 Phase-2 GIS file inventory.

Dataset DOI: 10.4225/25/5B0CD2B84A2DC; historic NCI project: iy57.
The archived GA README states that root File_Links.txt is the intended bulk-download
manifest and that iy57/gis contains contacts, coverages, the data-holiday database,
and generalised deep-tow/AUV tracklines.

This program therefore prefers File_Links.txt over HTML scraping, filters GIS-related
objects, classifies likely vector/geodatabase assets, and fails closed. It never
converts file presence into sonar coverage or probability of detection.
"""
from __future__ import annotations
import argparse, json, re, sys, urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

CATALOG = "https://dapds00.nci.org.au/thredds/catalog/iy57/catalog.html"
FILE_LINK_CANDIDATES = [
    "https://dapds00.nci.org.au/thredds/fileServer/iy57/File_Links.txt",
    "https://dapds00.nci.org.au/thredds/fileServer/iy57/File_links.txt",
]
GIS_HINTS = ("/gis/", "holiday", "coverage", "trackline", "contact")
VECTOR_EXT = (".shp", ".shx", ".dbf", ".prj", ".gdb", ".gpkg", ".kml", ".kmz", ".geojson", ".json")

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=="a":
            href=dict(attrs).get("href")
            if href: self.links.append(href)

def fetch(url: str) -> bytes:
    req=urllib.request.Request(url, headers={"User-Agent":"MH370-evidence-research/2.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        if r.status != 200: raise RuntimeError(f"HTTP {r.status}: {url}")
        return r.read()

def normalise_lines(raw: bytes) -> list[str]:
    text=raw.decode("utf-8", "replace")
    urls=[]
    for line in text.splitlines():
        line=line.strip()
        if not line or line.startswith("#"): continue
        m=re.search(r"https?://\S+", line)
        if m: urls.append(m.group(0).rstrip("'\",;"))
    return sorted(set(urls))

def classify(url: str) -> dict:
    p=urlparse(url).path.lower()
    return {
        "url":url,
        "gis_related": any(h in p for h in GIS_HINTS),
        "vector_or_gdb": p.endswith(VECTOR_EXT) or ".gdb/" in p,
        "holiday_candidate": "holiday" in p,
        "coverage_candidate": "coverage" in p,
        "track_candidate": "track" in p,
    }

def recover_manifest() -> tuple[str,list[str]]:
    errors=[]
    for u in FILE_LINK_CANDIDATES:
        try:
            links=normalise_lines(fetch(u))
            if links: return u, links
            errors.append(f"empty {u}")
        except Exception as e: errors.append(f"{u}: {e}")
    # fallback only inventories catalogue links; it is not equivalent to File_Links.txt
    try:
        raw=fetch(CATALOG); p=Links(); p.feed(raw.decode("utf-8","replace"))
        links=sorted(set(urljoin(CATALOG,h) for h in p.links if "iy57" in h))
        if links: return CATALOG, links
    except Exception as e: errors.append(f"{CATALOG}: {e}")
    raise RuntimeError("; ".join(errors))

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--out", default="data/nci_phase2_manifest.json")
    ap.add_argument("--gis-out", default="data/nci_phase2_gis_candidates.json")
    args=ap.parse_args()
    try: source, links=recover_manifest()
    except Exception as e:
        print(f"FAIL_CLOSED: authoritative NCI inventory unavailable: {e}", file=sys.stderr); return 2
    records=[classify(u) for u in links]
    gis=[r for r in records if r["gis_related"]]
    base={
      "source":"Geoscience Australia / NCI",
      "doi":"10.4225/25/5B0CD2B84A2DC",
      "inventory_source":source,
      "warning":"Inventory/provenance only. Do not infer sonar Pd or geometry until geospatial assets are opened and CRS/attributes validated.",
    }
    with open(args.out,"w",encoding="utf-8") as f:
        json.dump(base|{"count":len(records),"records":records},f,indent=2)
    with open(args.gis_out,"w",encoding="utf-8") as f:
        json.dump(base|{"count":len(gis),"records":gis},f,indent=2)
    print(f"inventory={len(records)} gis_candidates={len(gis)} source={source}")
    if not gis:
        print("FAIL_CLOSED: inventory recovered but no GIS candidates identified", file=sys.stderr); return 3
    return 0
if __name__ == "__main__": raise SystemExit(main())
