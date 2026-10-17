"""Fail-closed residual search ranking.

Inputs MUST already be authoritative georeferenced cells with independently
justified physical likelihoods, sonar detection probabilities, and cell areas.
Unvalidated proxy lattices are deliberately rejected.
"""
from __future__ import annotations
import argparse
import csv
import math
from pathlib import Path

REQUIRED = {"lat", "lon", "physics", "drift", "eof",
            "pd_atsb_ga", "cell_area_km2", "evidence_gate"}
OPTIONAL_PD = ("pd_oi2018", "pd_oi2025_26")
ALLOWED_GATE = "AUTHORITATIVE_GIS_VALIDATED"


def value(row, key, required=True):
    raw = row.get(key)
    if raw is None or str(raw).strip() == "":
        if required:
            raise ValueError(f"Missing {key} in cell {row.get('cell_id', '?')}")
        return None
    try:
        v = float(raw)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid {key}: {raw}") from exc
    if not math.isfinite(v):
        raise ValueError(f"Nonfinite {key}: {raw}")
    return v


def probability(x, name):
    if x < 0.0 or x > 1.0:
        raise ValueError(f"{name} not in [0,1]: {x}")
    return x


def score(row):
    if row.get("evidence_gate", "").strip() != ALLOWED_GATE:
        raise ValueError("Refusing to rank unvalidated GIS cells")
    lat, lon = value(row, "lat"), value(row, "lon")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("Invalid geographic coordinate")
    area = value(row, "cell_area_km2")
    if area <= 0:
        raise ValueError("Cell area must be > 0 km2")
    base = area
    for key in ("physics", "drift", "eof"):
        x = value(row, key)
        if x < 0:
            raise ValueError(f"Negative {key}")
        base *= x
    pd = probability(value(row, "pd_atsb_ga"), "pd_atsb_ga")
    nd = 1.0 - pd
    for key in OPTIONAL_PD:
        x = value(row, key, required=False)
        if x is not None:
            nd *= 1.0 - probability(x, key)
    result = base * nd
    if not math.isfinite(result):
        raise ValueError("Nonfinite cell score")
    return result


def rank(rows):
    if not rows:
        raise ValueError("No cells")
    scored = []
    for row in rows:
        row = dict(row)
        row["raw_residual_score"] = score(row)
        scored.append(row)
    z = math.fsum(row["raw_residual_score"] for row in scored)
    if not math.isfinite(z) or z <= 0:
        raise ValueError("Zero or nonfinite residual mass")
    for row in scored:
        row["posterior_residual"] = row["raw_residual_score"] / z
    scored.sort(key=lambda x: x["posterior_residual"], reverse=True)
    cumulative = 0.0
    for i, row in enumerate(scored, 1):
        cumulative += row["posterior_residual"]
        row["rank"] = i
        row["cumulative_mass"] = min(1.0, cumulative)
    return scored


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input")
    ap.add_argument("--out", default="results/ranked_residual_cells.csv")
    args = ap.parse_args()
    with open(args.input, newline="", encoding="utf-8") as h:
        r = csv.DictReader(h)
        missing = REQUIRED - set(r.fieldnames or [])
        if missing:
            ap.error(f"Missing columns: {sorted(missing)}")
        rows = list(r)
    try:
        rows = rank(rows)
    except ValueError as exc:
        ap.error(str(exc))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    names = list(rows[0])
    with open(out, "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=names)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} validated cells; not a wreckage discovery")


if __name__ == "__main__":
    main()
