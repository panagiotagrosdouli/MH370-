#!/usr/bin/env python3
"""Audit candidate MH370 survey footprints without inventing detection probabilities.

Reads real, locally supplied GeoJSON FeatureCollections. Outputs ONLY metadata
and geometry diagnostics. Explicitly does NOT assign Pd, deduce survey success,
or rank MH370 candidates.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def points_of(geometry):
    kind = geometry.get("type")
    coords = geometry.get("coordinates")
    if kind == "Polygon":
        rings = coords
    elif kind == "MultiPolygon":
        rings = [ring for poly in coords for ring in poly]
    else:
        raise ValueError(f"Expected Polygon/MultiPolygon, got {kind}")
    if not rings:
        raise ValueError("Empty polygon")
    result = []
    for ring in rings:
        if not isinstance(ring, list) or len(ring) < 4:
            raise ValueError("Each polygon ring needs at least four vertices")
        if ring[0] != ring[-1]:
            raise ValueError("Polygon rings must close")
        for point in ring:
            if not isinstance(point, list) or len(point) < 2:
                raise ValueError("Invalid coordinate tuple")
            lon, lat = point[:2]
            if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in (lon, lat)):
                raise ValueError("Nonfinite or nonnumeric WGS84 coordinate")
            if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                raise ValueError("Coordinate outside WGS84 longitude/latitude bounds")
            result.append((lon, lat))
    return result


def audit(document, source_url, dataset_id, stated_crs):
    if stated_crs != "EPSG:4326":
        raise ValueError("Explicit WGS84/EPSG:4326 declaration required; reproject upstream")
    if not source_url.startswith("https://"):
        raise ValueError("Provenance requires an HTTPS source URL")
    if not dataset_id.strip():
        raise ValueError("Provide an authoritative dataset identifier")
    if document.get("type") != "FeatureCollection":
        raise ValueError("Expected GeoJSON FeatureCollection")
    features = document.get("features")
    if not isinstance(features, list) or not features:
        raise ValueError("No polygon features available")
    total = 0
    bounds = [180.0, 90.0, -180.0, -90.0]
    for i, feature in enumerate(features):
        if not isinstance(feature, dict) or not feature.get("geometry"):
            raise ValueError(f"Feature {i} has no geometry")
        coordinates = points_of(feature["geometry"])
        total += 1
        for lon, lat in coordinates:
            bounds[0] = min(bounds[0], lon)
            bounds[1] = min(bounds[1], lat)
            bounds[2] = max(bounds[2], lon)
            bounds[3] = max(bounds[3], lat)
    return {
        "dataset_id": dataset_id,
        "source_url": source_url,
        "declared_crs": stated_crs,
        "polygon_features": total,
        "bounding_box_lonlat": bounds,
        "coverage_interpretation": "UNVERIFIED_GEOMETRY_ONLY",
        "detection_probability": None,
        "candidate_rank": None,
        "cautions": [
            "Bounds are not the union of surveyed area.",
            "Valid coordinates do not establish authoritative provenance.",
            "A survey footprint does not establish local detection probability.",
            "No inference about MH370 location may be made from this audit."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("geojson", type=Path)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--crs", default="EPSG:4326")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    document = json.loads(args.geojson.read_text(encoding="utf-8"))
    result = audit(document, args.source_url, args.dataset_id, args.crs)
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
