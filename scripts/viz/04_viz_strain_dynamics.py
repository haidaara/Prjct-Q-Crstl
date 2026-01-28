#!/usr/bin/env python3
"""Phason strain *dynamics* from a directory of snapshots.

Assumes each snapshot JSON contains per-tile ``phason_energy`` and optionally ``local_energy``.

Example:
  python scripts/viz/04_viz_strain_dynamics.py \
    --snapshot_dir data/experiments/healing/run_021/snapshots \
    --outdir data/viz/run_021

This script generates:
  - phason strain series (mean/max vs step)
  - optional correlation: defects vs mean strain
  - optional storyboard / movie frames (use --storyboard)
"""

from __future__ import annotations

from pathlib import Path
import sys

# Ensure project root is on PYTHONPATH so `import src...` works
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import argparse
import time
from src.viz.config import load_publication_config, get_viz_jobs
from src.viz.io import list_snapshots, load_tiling_state, short_path
from src.viz.panels import get_obstacle_mask
from src.viz.strain_plots import compute_strain_series_from_snapshots, plot_strain_series, plot_strain_vs_defects
from src.viz.movie import make_storyboard
from src.viz.style import default_output_dir


def _defect_count(state, *, defect_threshold: float, treat_immobile_as_fixed: bool = False) -> int:
    obs = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    n = 0
    for i, t in enumerate(state.get("tiles", [])):
        tid = int(t.get("id", i))
        if obs.get(tid) is not None:
            continue

        if float(t.get("local_energy", 0.0) or 0.0) >= defect_threshold:
            n += 1
    return n


def main() -> int:
    start_time = time.time()
    
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot_dir", default=None)
    ap.add_argument("--pattern", default="*.json")
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--config", default=None)
    ap.add_argument("--defect_threshold", default=None)
    ap.add_argument("--treat_immobile_as_fixed", action="store_true")
    ap.add_argument("--with_defect_corr", action="store_true")
    ap.add_argument("--storyboard", action="store_true")
    ap.add_argument("--n_frames", default=None, type=int)
    ap.add_argument("--ncols", default=None, type=int)
    ap.add_argument("--view", default=None, help="view for storyboard")
    args = ap.parse_args()

    cfg = load_publication_config(args.config)
    viz = cfg.get("viz_jobs", {})

    # TOML mode: reuse snapshot_dir/outdir from jobs (movie/storyboard) so you don't have to pass args
    if not args.snapshot_dir:
        if not viz.get("enabled", False):
            print("viz_jobs.enabled is false -> nothing to run")
            return 0

        jobs = [j for j in get_viz_jobs(cfg)
                if str(j.get("kind", "")).strip().lower() in {"movie", "storyboard"}]
        if not jobs:
            print("No movie/storyboard jobs found under [viz_jobs.jobs] (need snapshot_dir)")
            return 0

        print("\n============================================================")
        print("VIZ STRAIN DYNAMICS: running from TOML")
        print(f"Config : {short_path(Path(args.config) if args.config else (Path('configs')/'publication_plots.toml'))}")
        print("============================================================")

        for idx, j in enumerate(jobs, 1):
            snapdir = j.get("snapshot_dir")
            if not snapdir:
                print(f"Warning: Job {idx}/{len(jobs)} missing snapshot_dir -> skipped")
                continue

            outdir = args.outdir or j.get("outdir") or str(Path(snapdir) / "viz")
            out_show = short_path(Path(outdir))
            
            pattern = j.get("pattern", args.pattern)

            print(f"\n--- Job {idx}/{len(jobs)} ---")
            print(f"Snapshots: {short_path(Path(snapdir))}")
            print(f"Output   : {out_show}")
            print(f"Pattern  : {pattern}")

            snap_paths = list_snapshots(snapdir, pattern=pattern)
            if not snap_paths:
                print(f"  ⚠️  No snapshots found -> skipped")
                continue

            Path(outdir).mkdir(parents=True, exist_ok=True)
            
            print(f"Found    : {len(snap_paths)} files")
            
            series = compute_strain_series_from_snapshots(snap_paths)
            plot_strain_series(series, outdir=outdir, cfg=cfg)

            with_corr = bool(args.with_defect_corr or j.get("with_defect_corr", False))
            if with_corr:
                defect_threshold = float(args.defect_threshold) if args.defect_threshold is not None else float(j.get("defect_threshold", viz.get("defect_threshold", 1.5)))
                treat = bool(args.treat_immobile_as_fixed or j.get("treat_immobile_as_fixed", viz.get("treat_immobile_as_fixed", False)))
                defect_counts = []
                for p in snap_paths:
                    st = load_tiling_state(p)
                    defect_counts.append(_defect_count(st, defect_threshold=defect_threshold, treat_immobile_as_fixed=treat))
                plot_strain_vs_defects(series, defect_counts, outdir=outdir, cfg=cfg)

            # If this job is a storyboard job, also create storyboard frames
            do_story = bool(args.storyboard or str(j.get("kind", "")).strip().lower() == "storyboard")
            if do_story:
                view = args.view if args.view is not None else j.get("view", "strain")
                n_frames = int(args.n_frames) if args.n_frames is not None else int(j.get("n_frames", 12))
                ncols = int(args.ncols) if args.ncols is not None else int(j.get("ncols", 4))
                make_storyboard(snapdir, view=view, n_frames=n_frames, ncols=ncols, outdir=outdir, cfg=cfg)

        elapsed = time.time() - start_time
        print(f"\nCompleted in {elapsed:.1f}s")
        return 0

    # Single-run mode
    snapdir = args.snapshot_dir
    pattern = args.pattern

    snap_paths = list_snapshots(snapdir, pattern=pattern)
    if not snap_paths:
        print(f"No snapshots found in {args.snapshot_dir}")
        return 1

    # Determine output directory
    if args.outdir:
        outdir = Path(args.outdir)
    else:
        outdir = Path(args.snapshot_dir) / "viz"
    
    print(f"\nProcessing snapshots from: {short_path(Path(args.snapshot_dir))}")
    print(f"Output directory: {outdir}")
    print(f"Pattern: {pattern}")
    print(f"Found {len(snap_paths)} snapshots")
    
    outdir.mkdir(parents=True, exist_ok=True)

    series = compute_strain_series_from_snapshots(snap_paths)
    plot_strain_series(series, outdir=outdir, cfg=cfg)

    if args.with_defect_corr:
        defect_threshold = float(args.defect_threshold) if args.defect_threshold is not None else float(viz.get("defect_threshold", 1.5))
        treat = bool(args.treat_immobile_as_fixed)
        defect_counts = []
        for p in snap_paths:
            st = load_tiling_state(p)
            defect_counts.append(_defect_count(st, defect_threshold=defect_threshold, treat_immobile_as_fixed=treat))
        plot_strain_vs_defects(series, defect_counts, outdir=outdir, cfg=cfg)

    if args.storyboard:
        view = args.view or "strain"
        n_frames = int(args.n_frames) if args.n_frames is not None else 12
        ncols = int(args.ncols) if args.ncols is not None else 4
        make_storyboard(args.snapshot_dir, view=view, n_frames=n_frames, ncols=ncols, outdir=outdir, cfg=cfg)

    elapsed = time.time() - start_time
    print(f"\nCompleted in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())