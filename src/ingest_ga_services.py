"""Discover and validate Geoscience Australia/AusSeabed MH370 layers.

This utility intentionally fails closed: it never fabricates coverage when the
remote service is unavailable. It parses WMS capabilities and records layer
names/bounds for subsequent raster requests.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

WMS = "https://warehouse.ausseabed.gov.au/geoserver/ows?REQUEST=GetCapabilities&SERVICE=WMS"
TARGET_TOKENS = ("MH370", "Fugro_DT", "Fugro_AUV", "SAS", "Southern Indian Ocean")


def fetch(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "MH370-research/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def parse_wms(xml: bytes) -> list[dict]:
    root = ET.fromstring(xml)
    out = []
    for layer in root.iter():
        if not layer.tag.endswith("Layer"):
            continue
        name = title = None
        bounds = None
        for child in list(layer):
            tag = child.tag.split("}")[-1]
            if tag == "Name": name = child.text
            elif tag == "Title": title = child.text
            elif tag in {"EX_GeographicBoundingBox", "LatLonBoundingBox"}:
                bounds = ET.tostring(child, encoding="unicode")
        text = f"{name or ''} {title or ''}"
        if any(t.lower() in text.lower() for t in TARGET_TOKENS):
            out.append({"name": name, "title": title, "bounds_xml": bounds})
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/derived/ga_wms_layers.json")
    args = ap.parse_args()
    try:
        xml = fetch(WMS)
    except Exception as exc:
        raise SystemExit(
            "GA/AusSeabed WMS unavailable from this runtime; refusing to create "
            f"synthetic coverage. Error: {exc}"
        )
    layers = parse_wms(xml)
    if not layers:
        raise SystemExit("Capabilities loaded but no MH370-related layers resolved.")
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"source": WMS, "layers": layers}, indent=2), encoding="utf-8")
    print(f"Wrote {len(layers)} candidate layers to {p}")


if __name__ == "__main__":
    main()
