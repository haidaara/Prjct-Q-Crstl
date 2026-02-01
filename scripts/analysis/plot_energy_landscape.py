#!/usr/bin/env python3
"""
Plot / diagnose the energy landscape by sampling phason flips and measuring delta_E.

This consolidates older:
- plot_energy_landscape.py
- debug_energy_distribution.py

Key properties:
- Uses strict cache/field hygiene (wipes local_energy + vertex_class + clears model caches).
- Uses a k-ring neighborhood (default k=4) for robust manual delta_E estimation.
- Does NOT modify your input tiling on disk (all work is in-memory).

Examples:
  python scripts/analysis/plot_energy_landscape.py
  python scripts/analysis/plot_energy_landscape.py --sample 800 --k 4 --seed-radius 10 --seed-only
  python scripts/analysis/plot_energy_landscape.py --config configs/phase1_baseline.toml --outdir results/analysis
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import random
import statistics
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

# --- ensure project root in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# --- imports from project
from src.utils.script_utils import load_tiling, setup_simulation_components, initialize_seed_region  # type: ignore

# Optional imports (fallbacks included)
try:
    from src.utils.energy_utils import clear_all_caches, wipe_all_energy_fields  # type: ignore
except Exception:  # pragma: no cover
    def clear_all_caches(model) -> None:
        """Best-effort cache clearing if energy_utils.clear_all_caches is unavailable."""
        if hasattr(model, "clear_caches") and callable(getattr(model, "clear_caches")):
            model.clear_caches()
            return
        for attr in ("_cache", "_local_cache", "_vertex_cache", "_local_energy_cache", "_vertex_class_cache"):
            if hasattr(model, attr):
                try:
                    setattr(model, attr, {})
                except Exception:
                    pass

    def wipe_all_energy_fields(tiling: dict) -> None:
        """Best-effort field wipe if energy_utils.wipe_all_energy_fields is unavailable."""
        for t in tiling.get("tiles", []):
            t.pop("local_energy", None)
            t.pop("vertex_class", None)


def _wipe_tile_fields(tiling: dict, tile_ids: Iterable[int]) -> None:
    tiles = tiling["tiles"]
    for tid in tile_ids:
        tiles[tid].pop("local_energy", None)
        tiles[tid].pop("vertex_class", None)


def _region_energy(tiling: dict, region_ids: Sequence[int], energy_model) -> float:
    # Hygiene before any manual energy sum
    _wipe_tile_fields(tiling, region_ids)
    clear_all_caches(energy_model)
    e = 0.0
    for tid in region_ids:
        if tiling["tiles"][tid].get("removed", False):
            continue
        e += float(energy_model.compute_local_energy(tid, tiling))
    return e


def _set_all_flippable(tiling: dict) -> None:
    for t in tiling["tiles"]:
        if t.get("removed", False):
            t["flippable"] = False
        else:
            t["flippable"] = True


def _seed_only_filter(hexagons: List[List[int]], tiling: dict) -> List[List[int]]:
    tiles = tiling["tiles"]
    out = []
    for h in hexagons:
        if all(tiles[tid].get("growth_status") == "seed" for tid in h):
            out.append(h)
    return out


def measure_delta_e_for_hexagon(
    tiling: dict,
    hexagon: Sequence[int],
    flip_engine,
    energy_model,
    k: int = 4,
) -> Optional[float]:
    """
    Returns delta_E (after - before) for this hexagon, or None if the flip could not be applied.
    """
    # Neighborhood for robust manual delta calculation
    region_ids = list(flip_engine._get_k_ring_neighborhood(list(hexagon), tiling, k=k))

    e_before = _region_energy(tiling, region_ids, energy_model)

    undo_state = flip_engine.capture_state(region_ids, tiling)
    applied = flip_engine.apply_flip(list(hexagon), tiling)
    if not applied:
        flip_engine.restore_state(undo_state, tiling)
        _wipe_tile_fields(tiling, region_ids)
        return None

    e_after = _region_energy(tiling, region_ids, energy_model)

    # Restore + hygiene
    flip_engine.restore_state(undo_state, tiling)
    _wipe_tile_fields(tiling, region_ids)
    clear_all_caches(energy_model)

    return float(e_after - e_before)


def plot_histogram(deltas: List[float], out_png: Path, title: str) -> None:
    import matplotlib
    matplotlib.use("Agg")  # safe for headless runs
    import matplotlib.pyplot as plt
    import numpy as np

    arr = np.array(deltas, dtype=float)
    fig = plt.figure(figsize=(10, 6))
    plt.hist(arr, bins=50, edgecolor="black")
    plt.axvline(0.0)
    plt.title(title)
    plt.xlabel("delta_E (after - before)")
    plt.ylabel("Count")
    fig.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tiling", default="data/processed/penrose_tiling_energy_initialized.json",
                    help="Path to tiling JSON (default: energy-initialized tiling).")
    ap.add_argument("--config", default="configs/phase1_baseline.toml",
                    help="Energy/config TOML used to build the energy model.")
    ap.add_argument("--sample", type=int, default=500,
                    help="How many hexagons to sample (default 500). Use 0 to use all.")
    ap.add_argument("--k", type=int, default=4,
                    help="k-ring neighborhood for manual delta_E (default 4).")
    ap.add_argument("--seed-radius", type=float, default=10.0,
                    help="Seed radius if using --seed-only (default 10).")
    ap.add_argument("--seed-only", action="store_true",
                    help="Restrict sampled flips to seed-region-only hexagons.")
    ap.add_argument("--outdir", default="results/analysis",
                    help="Output directory for plots/data.")
    ap.add_argument("--save-deltas", action="store_true",
                    help="Also save delta_E list as JSON.")
    ap.add_argument("--rng-seed", type=int, default=0,
                    help="RNG seed for sampling (default 0).")
    args = ap.parse_args()

    random.seed(args.rng_seed)

    # Work on a copy so we never mutate your data file
    tiling = load_tiling(args.tiling)
    tiling = copy.deepcopy(tiling)

    # Setup engines (config-aware)
    _, energy_model, flip_engine = setup_simulation_components(args.config, verbose=False)

    # Choose region
    if args.seed_only:
        initialize_seed_region(tiling, seed_radius=float(args.seed_radius), set_flippable=True)
    else:
        _set_all_flippable(tiling)

    # Find hexagons
    hexagons = flip_engine.find_flippable_hexagons(tiling)
    if args.seed_only:
        hexagons = _seed_only_filter(hexagons, tiling)

    if not hexagons:
        print("   No flippable hexagons found for the selected region.")
        return 1

    # Sampling
    if args.sample and args.sample > 0 and len(hexagons) > args.sample:
        hexagons = random.sample(hexagons, args.sample)

    print(f"   Sampling {len(hexagons)} hexagons (k={args.k}, seed_only={args.seed_only}) ...")

    deltas: List[float] = []
    failed = 0
    for h in hexagons:
        de = measure_delta_e_for_hexagon(tiling, h, flip_engine, energy_model, k=int(args.k))
        if de is None or not math.isfinite(de):
            failed += 1
            continue
        deltas.append(de)

    if not deltas:
        print("     No valid delta_E samples computed.")
        return 1

    mean = statistics.fmean(deltas)
    stdev = statistics.pstdev(deltas) if len(deltas) > 1 else 0.0
    uphill = sum(1 for x in deltas if x > 0)
    downhill = sum(1 for x in deltas if x < 0)

    print("\n=== delta_E Summary ===")
    print(f"Samples: {len(deltas)} (failed: {failed})")
    print(f"Mean delta_E: {mean:.6f}")
    print(f"Std  delta_E: {stdev:.6f}")
    print(f"Uphill:  {uphill/len(deltas):.1%}  (count={uphill})")
    print(f"Downhill:{downhill/len(deltas):.1%}  (count={downhill})")
    print(f"Min/Max: {min(deltas):.6f} / {max(deltas):.6f}")

    outdir = Path(args.outdir)
    tag = "seed" if args.seed_only else "all"
    out_png = outdir / f"deltaE_hist_{tag}_k{args.k}_n{len(deltas)}.png"
    plot_histogram(deltas, out_png, f"delta_E distribution ({tag}, k={args.k}, n={len(deltas)})")
    print(f"\n   Saved histogram to: {out_png}")

    if args.save_deltas:
        out_json = outdir / f"deltaE_samples_{tag}_k{args.k}_n{len(deltas)}.json"
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps({"tag": tag, "k": args.k, "deltas": deltas}, indent=2), encoding="utf-8")
        print(f" Saved deltas to: {out_json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
