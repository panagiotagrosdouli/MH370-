"""MH370 baseline spatial evidence-synthesis model.

This script intentionally implements a transparent proxy model rather than
pretending to reconstruct the full DSTG raw SATCOM solution without all
required ephemerides/calibration inputs.

Outputs a gridded posterior CSV suitable for mapping and sensitivity tests.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelConfig:
    lat_min: float = -36.5
    lat_max: float = -32.0
    lon_min: float = 90.5
    lon_max: float = 96.5
    step_deg: float = 0.05

    # CSIRO Part III drift-model mode, used as a model-derived anchor only.
    anchor_lat: float = -35.6
    anchor_lon: float = 92.8

    # Proxy widths for the current evidence-synthesis stage.
    sigma_along_km: float = 70.0
    sigma_cross_km: float = 20.0

    # Soft official core latitude range.
    core_north: float = -33.0
    core_south: float = -36.0
    latitude_taper_sigma_deg: float = 0.15

    # Conservative GA 2022 negative-evidence core around the reviewed
    # WSPR-centred region. This is not the full 4,900 km² footprint.
    ga_center_lat: float = -33.177
    ga_center_lon: float = 95.3
    ga_core_radius_km: float = 18.52  # 10 NM
    ga_core_pd: float = 0.99


def frange(start: float, stop: float, step: float):
    x = start
    while x <= stop + step * 0.1:
        yield round(x, 10)
        x += step


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0088
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def tangent_frame() -> tuple[float, float, float, float]:
    """Approximate local along/cross-arc basis from official candidate geometry.

    The direction is deliberately approximate. It is a proxy until a machine-
    readable official Seventh Arc geometry is ingested.
    """
    mid_lat = -35.15
    dx = (92.8 - 92.6) * 111.32 * math.cos(math.radians(mid_lat))
    dy = (-35.6 + 34.7) * 111.32
    n = math.hypot(dx, dy)
    tx, ty = dx / n, dy / n
    nx, ny = ty, -tx
    return tx, ty, nx, ny


def latitude_weight(lat: float, cfg: ModelConfig) -> float:
    if lat < cfg.core_south:
        z = (lat - cfg.core_south) / cfg.latitude_taper_sigma_deg
        return math.exp(-0.5 * z * z)
    if lat > cfg.core_north:
        z = (lat - cfg.core_north) / cfg.latitude_taper_sigma_deg
        return math.exp(-0.5 * z * z)
    return 1.0


def build_grid(cfg: ModelConfig):
    tx, ty, nx, ny = tangent_frame()
    rows = []

    for lat in frange(cfg.lat_min, cfg.lat_max, cfg.step_deg):
        for lon in frange(cfg.lon_min, cfg.lon_max, cfg.step_deg):
            dy = (lat - cfg.anchor_lat) * 111.32
            dx = (lon - cfg.anchor_lon) * 111.32 * math.cos(math.radians(cfg.anchor_lat))

            along = dx * tx + dy * ty
            cross = dx * nx + dy * ny

            satcom_eof_proxy = math.exp(-0.5 * (cross / cfg.sigma_cross_km) ** 2)
            drift_proxy = math.exp(-0.5 * (along / cfg.sigma_along_km) ** 2)
            lat_weight = latitude_weight(lat, cfg)

            ga_distance = haversine_km(lat, lon, cfg.ga_center_lat, cfg.ga_center_lon)
            pd_ga = cfg.ga_core_pd if ga_distance <= cfg.ga_core_radius_km else 0.0
            nondetection_ga = 1.0 - pd_ga

            cell_area = (
                111.32 * cfg.step_deg
                * 111.32 * cfg.step_deg
                * math.cos(math.radians(lat))
            )

            unnorm = (
                satcom_eof_proxy
                * drift_proxy
                * lat_weight
                * nondetection_ga
                * cell_area
            )

            rows.append(
                {
                    "latitude": lat,
                    "longitude": lon,
                    "along_arc_km": along,
                    "cross_arc_km": cross,
                    "satcom_eof_proxy": satcom_eof_proxy,
                    "drift_proxy": drift_proxy,
                    "latitude_weight": lat_weight,
                    "ga_distance_km": ga_distance,
                    "ga_detection_probability": pd_ga,
                    "ga_nondetection_likelihood": nondetection_ga,
                    "cell_area_km2": cell_area,
                    "unnormalized_mass": unnorm,
                }
            )

    total = sum(r["unnormalized_mass"] for r in rows)
    for r in rows:
        r["posterior_mass"] = r["unnormalized_mass"] / total

    ranked = sorted(range(len(rows)), key=lambda i: rows[i]["posterior_mass"], reverse=True)
    cumulative = 0.0
    for idx in ranked:
        cumulative += rows[idx]["posterior_mass"]
        rows[idx]["hpd_cumulative"] = cumulative
        rows[idx]["credible_class"] = (
            "50%" if cumulative <= 0.5 else "90%" if cumulative <= 0.9 else "outside90"
        )

    return rows


def summarize(rows):
    mode = max(rows, key=lambda r: r["posterior_mass"])
    centroid_lat = sum(r["latitude"] * r["posterior_mass"] for r in rows)
    centroid_lon = sum(r["longitude"] * r["posterior_mass"] for r in rows)
    area50 = sum(r["cell_area_km2"] for r in rows if r["hpd_cumulative"] <= 0.5)
    area90 = sum(r["cell_area_km2"] for r in rows if r["hpd_cumulative"] <= 0.9)
    return {
        "mode_lat": mode["latitude"],
        "mode_lon": mode["longitude"],
        "centroid_lat": centroid_lat,
        "centroid_lon": centroid_lon,
        "area50_km2": area50,
        "area90_km2": area90,
    }


def write_csv(rows, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    cfg = ModelConfig()
    rows = build_grid(cfg)
    summary = summarize(rows)
    output = Path("outputs/baseline_posterior_grid.csv")
    write_csv(rows, output)

    print("MH370 baseline proxy posterior")
    for k, v in summary.items():
        print(f"{k}: {v}")
    print(f"wrote: {output}")
    print("STATUS: search-prior model, not a wreckage-location claim")


if __name__ == "__main__":
    main()
