#!/usr/bin/env python3
"""Crawl the official NCI MH370 Phase-2 THREDDS catalogue.

Purpose: enumerate real Phase-2 files before any sonar-coverage inference.
This tool deliberately does NOT turn file presence into a probability of detection.

Authoritative dataset: GA Phase 2 Raw and Processed Data
DOI: 10.4225/25/5B0CD2B84A2DC
Historic NCI project exposed by the GA MH370 database search: iy57.

Usage:
  python src/crawl_nci_phase2.py --out data/nci_phase2_manifest.json

Fails closed on DNS/network/catalogue errors and never fabricates geometry.
"""
from __future__ import annotations
import argparse, json, sys, urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

ROOT = "https://dapds00.nci.org.au/thredds/catalog/iy57/catalog.html"

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            d=dict(attrs); href=d.get("href")
            if href: self.links.append(href)

def fetch(url: str) -> bytes:
    req=urllib.request.Request(url, headers={"User-Agent":"MH370-research/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        if r.status != 200: raise RuntimeError(f"HTTP {r.status}: {url}")
        return r.read()

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--out", default="data/nci_phase2_manifest.json")
    args=ap.parse_args()
    try: raw=fetch(ROOT)
    except Exception as e:
        print(f"FAIL_CLOSED: cannot access official NCI catalogue: {e}", file=sys.stderr); return 2
    p=Links(); p.feed(raw.decode("utf-8", "replace"))
    links=sorted(set(urljoin(ROOT,h) for h in p.links if "iy57" in h))
    if not links:
        print("FAIL_CLOSED: catalogue returned no iy57 links", file=sys.stderr); return 3
    manifest={
      "source":"Geoscience Australia / NCI",
      "doi":"10.4225/25/5B0CD2B84A2DC",
      "catalogue":ROOT,
      "inference_warning":"File listing is provenance only; do not infer sonar Pd or searched geometry without georeferenced content/metadata.",
      "links":links,
    }
    with open(args.out,"w",encoding="utf-8") as f: json.dump(manifest,f,indent=2)
    print(f"wrote {args.out}: {len(links)} catalogue links")
    return 0
if __name__ == "__main__": raise SystemExit(main())
