#!/usr/bin/env python3
"""
scripts/dev_tools/calibrate_phason_basis.py

One-time calibration:
  center = M_par @ lattice_coords + origin

Saves a JSON calibration file used by PhasonStrainCalculator.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import numpy as np

try:
    import tomllib  # py3.11+
except Exception:
    tomllib = None


def _load_toml(path: str) -> dict:
    if tomllib is None:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    return tomllib.loads(p.read_text(encoding="utf-8"))


def calibrate(tiling_path: str, *, exclude_boundary: bool) -> dict:
    with open(tiling_path, "r", encoding="utf-8") as f:
        tiling = json.load(f)

    centers = []
    coords = []

    for t in tiling["tiles"]:
        if t.get("removed", False) or t.get("obstacle_type") == "pore":
            continue
        if exclude_boundary and t.get("is_boundary", False):
            continue
        lc = t.get("lattice_coords", None)
        if lc is None or len(lc) != 5:
            continue

        centers.append([float(t["center"][0]), float(t["center"][1])])
        coords.append([int(x) for x in lc])

    if not centers:
        raise ValueError("No valid tiles found for calibration (check your filters).")

    R = np.array(centers, dtype=float).T     # 2xN
    N5 = np.array(coords, dtype=float).T     # 5xN

    # Fit affine map: R ≈ M_par @ N5 + origin
    # --- build strip-pair index (10 unordered pairs) ---
    pairs = [(a, b) for a in range(5) for b in range(a + 1, 5)]
    pair_to_idx = {p: i for i, p in enumerate(pairs)}

    pair_ids = []
    for t in tiling["tiles"]:
        if t.get("removed", False) or t.get("obstacle_type") == "pore":
            continue
        if exclude_boundary and t.get("is_boundary", False):
            continue
        lc = t.get("lattice_coords", None)
        if lc is None or len(lc) != 5:
            continue

        fams = sorted([int(s["family"]) for s in t.get("strips", [])])
        if len(fams) != 2:
            raise ValueError(f"Tile {t.get('id')} missing 2 strips")
        pair = (fams[0], fams[1])
        pair_ids.append(pair_to_idx[pair])

    # pair one-hot: 10 x N
    P = np.zeros((10, N5.shape[1]), dtype=float)
    for col, pid in enumerate(pair_ids):
        P[pid, col] = 1.0

    # Fit affine + pair offsets:  R = M_par @ N5 + D @ P + origin
    ones = np.ones((1, N5.shape[1]), dtype=float)
    X = np.vstack([N5, P, ones])          # (5+10+1)=16 x N
    A = R @ np.linalg.pinv(X)             # 2 x 16

    M_par = A[:, :5]                      # 2x5
    D = A[:, 5:15]                        # 2x10  (pair offsets)
    origin = A[:, 15]                     # 2,


    R_rec = (M_par @ N5) + (D @ P) + origin.reshape(2, 1)
    res = (R - R_rec)

    fro_err = float(np.linalg.norm(res, ord="fro"))
    tile_errs = np.linalg.norm(res, axis=0)  # per tile (euclidean)
    per_tile = float(np.mean(tile_errs))
    max_tile = float(np.max(tile_errs))

    pid_arr = np.array(pair_ids, dtype=int)
    per_pair_error = {}
    for (a, b) in pairs:
        pid = pair_to_idx[(a, b)]
        mask = (pid_arr == pid)
        if not np.any(mask):
            continue
        e = tile_errs[mask]
        per_pair_error[f"{a},{b}"] = {
            "count": int(mask.sum()),
            "mean": float(e.mean()),
            "max": float(e.max()),
        }


    # Nullspace basis of M_par gives 3D perp subspace
    # M_par = U S Vh; nullspace basis = last 3 rows of Vh (as columns => transpose)
    _, svals, Vh = np.linalg.svd(M_par)
    M_perp = Vh[2:, :].T                     # 5x3 (orthonormal columns)

    pinv_M_par = np.linalg.pinv(M_par)       # 5x2

    sums = np.sum(N5, axis=0).astype(int)
    uniq, counts = np.unique(sums, return_counts=True)
    target_sum = int(uniq[np.argmax(counts)])

    pair_offsets = {f"{a},{b}": D[:, pair_to_idx[(a, b)]].tolist() for (a, b) in pairs}


    return {
        "source_tiling": str(tiling_path),
        "M_par": M_par.tolist(),
        "origin": origin.tolist(),
        "pair_offsets": pair_offsets,
        "M_perp": M_perp.tolist(),
        "pinv_M_par": pinv_M_par.tolist(),
        "target_sum": target_sum,
        "singular_values_M_par": [float(x) for x in svals.tolist()],
        "reconstruction_error_fro": fro_err,
        "reconstruction_error_mean_per_tile": per_tile,
        "reconstruction_error_max_per_tile": max_tile,
        "per_pair_error": per_pair_error,
        "num_tiles_used": int(N5.shape[1]),
        "gauge_sum_distribution": {int(u): int(c) for u, c in zip(uniq.tolist(), counts.tolist())},

    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/phase2_experiments.toml")
    ap.add_argument("--input", default=None, help="tiling JSON with lattice_coords")
    ap.add_argument("--output", default=None, help="calibration JSON output")
    ap.add_argument("--exclude-boundary", action="store_true")
    ap.add_argument("--debug", action="store_true", help="Print extra calibration diagnostics")
    args = ap.parse_args()


    cfg = _load_toml(args.config)
    cal_cfg = cfg.get("phason_calibration", {})

    input_path = args.input or cal_cfg.get("input_tiling") or "data/processed/penrose_tiling_energy_initialized.json"
    output_path = args.output or cal_cfg.get("output_file") or "configs/phason_calibration.json"

    calib = calibrate(input_path, exclude_boundary=bool(args.exclude_boundary or cal_cfg.get("exclude_boundary", False)))

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(calib, f, indent=2)

    

    print("   Phason calibration saved")
    print(f"   input : {input_path}")
    print(f"   output: {output_path}")
    print(f"   tiles : {calib['num_tiles_used']}")
    print(f"   mean reconstruction error: {calib['reconstruction_error_mean_per_tile']:.6g}")
    print(f"   target_sum (gauge): {calib['target_sum']}")
    
    if args.debug:
        print(f"   max reconstruction error: {calib.get('reconstruction_error_max_per_tile', float('nan')):.6g}")
        print(f"   gauge_sum_distribution: {calib.get('gauge_sum_distribution', {})}")
        gsd = calib.get("gauge_sum_distribution", {})
        if isinstance(gsd, dict) and len(gsd) > 1:
            print("   WARNING: multiple gauge sums exist -> a single enforced target_sum can cause lift mismatch.")


if __name__ == "__main__":
    main()
