#!/usr/bin/env python3
"""
scripts/validation/validate_phason_strain.py

Lightweight validation for phason calibration + lifting + energy term.

Goal:
- keep this script simple and high-signal (not a second energy framework)
- print diagnostics that quickly reveal mismatches (gauge, strips pair, lifted indices)
- optionally write a compact JSON report (so runs are reproducible)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np

# Ensure project root is on sys.path so `import src...` works
project_root = Path(__file__).resolve().parents[2]  # .../quasi-phason
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.energy.phason_strain import PhasonStrainCalculator  # noqa: E402

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


def _pair_key_hint_from_tile(tile: Dict[str, Any]) -> Optional[str]:
    strips = tile.get("strips", [])
    if not isinstance(strips, list) or len(strips) != 2:
        return None
    try:
        fams = sorted([int(strips[0]["family"]), int(strips[1]["family"])])
    except Exception:
        return None
    return f"{fams[0]},{fams[1]}"


def _forward_center_from_stored(
    tile: Dict[str, Any],
    cal: Dict[str, Any],
) -> tuple[Optional[np.ndarray], Optional[str]]:
    """
    Debug-only "forward" reconstruction using stored lattice_coords:
        center_pred = M_par @ lattice_coords + origin + pair_offset(pair from strips)
    """
    lc = tile.get("lattice_coords")
    if lc is None or not isinstance(lc, list) or len(lc) != 5:
        return None, None
    key = _pair_key_hint_from_tile(tile)
    M_par = np.asarray(cal.get("M_par"), dtype=float)  # (2,5)
    origin = np.asarray(cal.get("origin"), dtype=float).reshape(2,)
    pair_offsets = cal.get("pair_offsets") or {}
    off = np.asarray(pair_offsets.get(key, [0.0, 0.0]), dtype=float).reshape(2,)
    pred = (M_par @ np.asarray(lc, dtype=float)) + origin + off
    return pred, key


def main() -> None:
    # --- CLI + TOML defaults (minimal, no heavy config machinery) ---
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/phase2_experiments.toml")
    ap.add_argument("--tiling", default=None)
    ap.add_argument("--calibration", default=None)
    ap.add_argument("--samples", type=int, default=None)
    ap.add_argument("--tile", type=int, default=None)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--topk", type=int, default=None)
    ap.add_argument("--report", default=None)
    ap.add_argument("--forward-check", action="store_true", default=None)
    args = ap.parse_args()

    cfg = _load_toml(args.config)
    val_cfg = cfg.get("phason_validation", {})
    energy_cfg = cfg.get("energy", {})
    project_cfg = cfg.get("project", {})

    tiling_path = (
        args.tiling
        or val_cfg.get("tiling_path")
        or val_cfg.get("tiling")
        or "data/processed/penrose_tiling_energy_initialized.json"
    )

    calib_path = (
        args.calibration
        or val_cfg.get("calibration_file")
        or energy_cfg.get("phason_calibration_file")
        or "configs/phason_calibration.json"
    )

    tile_id = int(args.tile if args.tile is not None else val_cfg.get("tile_id", 100))
    samples = int(args.samples if args.samples is not None else val_cfg.get("samples", 200))

    seed = args.seed if args.seed is not None else val_cfg.get("rng_seed", project_cfg.get("random_seed", None))
    topk = int(args.topk if args.topk is not None else val_cfg.get("print_top_k_worst", 0))

    report_path = args.report if args.report is not None else val_cfg.get("report_file", None)

    warn_thr = float(val_cfg.get("warn_reconstruction_error", 1e-10))
    fail_thr = float(val_cfg.get("fail_reconstruction_error", 1e-8))

    # Forward check default: TOML key (if present) else off
    if args.forward_check is None:
        forward_check = bool(val_cfg.get("forward_check", False))
    else:
        forward_check = bool(args.forward_check)

    # phason energy calc normalization should match your energy config (if present)
    normalize_by_degree = bool(energy_cfg.get("phason_degree_normalize", True))

    # This K is only used for reporting phason_energy(tile=...) at the end.
    # It does NOT change the lift/reconstruction diagnostics.
    K = float(val_cfg.get("stiffness", energy_cfg.get("phason_stiffness", 0.3)))

    with open(tiling_path, "r", encoding="utf-8") as f:
        tiling = json.load(f)

    with open(calib_path, "r", encoding="utf-8") as f:
        cal = json.load(f)

    # High-signal warning (helps interpret reconstruction errors)
    gsd = cal.get("gauge_sum_distribution")
    if isinstance(gsd, dict) and len(gsd) > 1:
        print(f"⚠️  NOTE: multiple gauge sums exist in calibration: {gsd}")
        print("    If lifting enforces a single target_sum, other-gauge tiles will show nonzero reconstruction_error.\n")

    calc = PhasonStrainCalculator(cal, stiffness=K)

    # -------------------------
    # Single-tile diagnostics
    # -------------------------
    d = calc.diagnostics_for_tile(tile_id, tiling)

    print("=== Single-tile diagnostics ===")
    for k, v in d.items():
        print(f"{k}: {v}")

    # extra high-signal comparisons (stored vs lifted)
    t0 = tiling["tiles"][tile_id]
    stored = t0.get("lattice_coords")
    if isinstance(stored, list) and len(stored) == 5:
        print(f"stored_lattice_coords: {stored}")
        print(f"stored_lattice_sum   : {int(sum(stored))}")

    hint = _pair_key_hint_from_tile(t0)
    print(f"pair_key_hint(from strips): {hint}")

    if isinstance(stored, list) and len(stored) == 5 and "indices" in d:
        try:
            lifted = [int(x) for x in d["indices"]]
            delta = [lifted[i] - int(stored[i]) for i in range(5)]
            print(f"indices_delta(lift - stored): {delta}  delta_sum={sum(delta)}")
        except Exception:
            pass

    if forward_check:
        pred, key = _forward_center_from_stored(t0, cal)
        if pred is None:
            print("forward_check: N/A (missing lattice_coords or strips)")
        else:
            fwd_err = float(np.linalg.norm(np.asarray(t0["center"], float) - pred))
            print(f"forward_pair_key: {key}")
            print(f"forward_error   : {fwd_err:.12g}")

    # -------------------------
    # Sample diagnostics
    # -------------------------
    n_tiles = len(tiling.get("tiles", []))
    rng = np.random.default_rng(None if seed is None else int(seed))
    sample_ids = rng.choice(n_tiles, size=min(samples, n_tiles), replace=False)

    err_list = []
    gauge_ok = 0
    rows = []  # (err, tile_id, stored_sum, hint_key, best_pair, gauge_sum)

    for tid in sample_ids:
        tid = int(tid)
        dd = calc.diagnostics_for_tile(tid, tiling)
        e = float(dd.get("reconstruction_error", 0.0))
        err_list.append(e)
        gauge_ok += int(dd.get("gauge_ok", False))

        t = tiling["tiles"][tid]
        lc = t.get("lattice_coords")
        stored_sum = int(sum(lc)) if isinstance(lc, list) and len(lc) == 5 else None
        hint_key = _pair_key_hint_from_tile(t)
        rows.append((
            e,
            tid,
            stored_sum,
            hint_key,
            dd.get("best_pair_key"),
            dd.get("gauge_sum"),
        ))

    errs = np.asarray(err_list, dtype=float)
    mean = float(errs.mean()) if errs.size else 0.0
    mx = float(errs.max()) if errs.size else 0.0
    p95 = float(np.percentile(errs, 95)) if errs.size else 0.0

    status = "PASS"
    if mx > fail_thr:
        status = "FAIL"
    elif mx > warn_thr:
        status = "WARN"

    print("\n=== Sample summary ===")
    print(f"samples: {len(sample_ids)}")
    print(f"reconstruction_error: mean={mean:.6g}  p95={p95:.6g}  max={mx:.6g}")
    print(f"gauge_ok: {gauge_ok}/{len(sample_ids)}")
    print(f"status: {status}")

    if topk and topk > 0:
        rows.sort(key=lambda r: r[0], reverse=True)
        print(f"\nWorst {min(topk, len(rows))} tiles (by reconstruction_error):")
        for (e, tid, stored_sum, hint_key, best_key, gs) in rows[:min(topk, len(rows))]:
            print(
                f"  tile={tid:4d} err={e:.12g} stored_sum={stored_sum} gauge_sum={gs} hint={hint_key} best={best_key}"
            )

    # -------------------------
    # Sanity energy on the chosen tile
    # -------------------------
    e_tile = float(calc.compute_energy_for_tile(tile_id, tiling, normalize_by_degree=normalize_by_degree))
    print(f"\nphason_energy(tile={tile_id}): {e_tile:.6g}")

    # -------------------------
    # Optional compact JSON report
    # -------------------------
    if report_path:
        report = {
            "validator": "phason_validation",
            "status": status,
            "inputs": {
                "config": args.config,
                "tiling_path": tiling_path,
                "calibration_path": calib_path,
            },
            "settings": {
                "tile_id": tile_id,
                "samples": int(len(sample_ids)),
                "seed": seed,
                "topk": int(topk or 0),
                "forward_check": bool(forward_check),
                "warn_reconstruction_error": warn_thr,
                "fail_reconstruction_error": fail_thr,
                "stiffness_K": K,
                "normalize_by_degree": normalize_by_degree,
            },
            "single_tile": {
                "tile_id": tile_id,
                "diagnostics": d,
                "stored_lattice_coords": stored,
                "pair_key_hint": hint,
                "phason_energy": e_tile,
            },
            "sample_summary": {
                "reconstruction_error_mean": mean,
                "reconstruction_error_p95": p95,
                "reconstruction_error_max": mx,
                "gauge_ok_fraction": float(gauge_ok) / float(len(sample_ids)) if len(sample_ids) else 0.0,
            },
        }

        rp = Path(report_path)
        rp.parent.mkdir(parents=True, exist_ok=True)
        with open(rp, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"report_saved: {report_path}")


if __name__ == "__main__":
    main()
