#!/usr/bin/env python3
"""Query the public AusSeabed MH370 catalogue for an AOI.

Fail-closed:
- catalogue footprints are discovery geometry, not detection probability;
- no Pd values are generated;
- saves raw JSON for provenance.
"""
import argparse, json, urllib.parse, urllib.request
from pathlib import Path

DEFAULT_BASE = "https://mh370-api.ausseabed.gov.au"

def get_json(url, timeout=60):
    req=urllib.request.Request(url, headers={"User-Agent":"mh370-residual-research/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--base", default=DEFAULT_BASE)
    p.add_argument("--product", default="Sidescan")
    p.add_argument("--wkt", required=True, help="AOI WKT in EPSG:4326")
    p.add_argument("--out", default="data/derived/ausseabed_mh370_api_features.json")
    a=p.parse_args()
    base=a.base.rstrip("/")
    product=urllib.parse.quote(a.product, safe="")
    qs=urllib.parse.urlencode({"geom":a.wkt})
    url=f"{base}/products/{product}/features?{qs}"
    data=get_json(url)
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({
        "source_url":url,
        "product":a.product,
        "aoi_wkt":a.wkt,
        "classification":"CATALOGUE_FOOTPRINT_NOT_PD",
        "response":data
    },indent=2),encoding="utf-8")
    print(f"saved {out}; catalogue footprints MUST NOT be converted directly to Pd")

if __name__=="__main__":
    main()
