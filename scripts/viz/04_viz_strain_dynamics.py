#!/usr/bin/env python3
"""Phason strain dynamics from snapshot directory.

Usage:
  # Single run - REQUIRES --snapshot_dir
  python 04_viz_strain_dynamics.py --snapshot_dir data/snapshots
  
  # With options
  python 04_viz_strain_dynamics.py --snapshot_dir data/snapshots --with_defect_corr --storyboard
  
  # TOML batch mode (no --snapshot_dir, requires enabled TOML jobs)
  python 04_viz_strain_dynamics.py

TOML defaults + CLI overrides all parameters.
Output defaults to: snapshot_dir/viz
"""

from __future__ import annotations

import sys
import time
import argparse
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.path.insert(0, str(Path(__file__).parent))
import _utils

from src.viz.config import load_publication_config, get_viz_jobs
from src.viz.io import list_snapshots, load_tiling_state, short_path
from src.viz.progress import progress
from src.viz.panels import get_obstacle_mask
from src.viz.strain_plots import (
    compute_strain_series_from_snapshots,
    plot_strain_series,
    plot_strain_vs_defects,
)
from src.viz.movie import make_storyboard


def defect_count(state, defect_threshold: float, treat_immobile_as_fixed: bool) -> int:
    """Count defects above threshold, excluding obstacles."""
    obs = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    count = 0
    for i, t in enumerate(state.get("tiles", [])):
        tid = int(t.get("id", i))
        if obs.get(tid) is not None:
            continue
        if float(t.get("local_energy", 0.0) or 0.0) >= defect_threshold:
            count += 1
    return count


def main() -> int:
    start_time = time.time()
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--snapshot_dir", help="Directory with snapshot JSON files")
    parser.add_argument("--pattern", default="*.json", help="Glob pattern for snapshots")
    parser.add_argument("--outdir", help="Output directory (default: snapshot_dir/viz)")
    parser.add_argument("--config", default=None, help="Path to publication_plots.toml")
    
    # CRITICAL FIX 1: Set CLI defaults to None so job/TOML can override
    parser.add_argument("--view", default=None, help="View type for storyboard")
    parser.add_argument("--n_frames", type=int, default=None, 
                       help="Number of frames for storyboard")
    parser.add_argument("--ncols", type=int, default=None, 
                       help="Columns in storyboard grid")
    
    parser.add_argument("--defect_threshold", type=float, default=None, 
                       help="Defect energy threshold")
    parser.add_argument("--treat_immobile_as_fixed", 
                       action=argparse.BooleanOptionalAction, default=None,
                       help="Treat immobile tiles as fixed obstacles")
    parser.add_argument("--with_defect_corr", action="store_true", 
                       help="Generate defect vs strain correlation")
    parser.add_argument("--storyboard", action="store_true", 
                       help="Generate storyboard contact sheet")
    
    args = parser.parse_args()
    
    # CRITICAL FIX 3: Handle config loading with error checking
    try:
        cfg = load_publication_config(args.config)
    except Exception as e:
        parser.print_help()
        print(f"\nError loading config: {e}")
        return 1
    
    viz = cfg.get("viz_jobs", {})
    
    # ===== TOML BATCH MODE (no --snapshot_dir) =====
    if not args.snapshot_dir:
        print(f"\n{'='*60}")
        print("STRAIN DYNAMICS: TOML Batch Mode")
        print(f"{'='*60}")
        
        if not viz.get("enabled", False):
            parser.print_help()
            print("\nError: --snapshot_dir required when TOML jobs disabled")
            return 1
        
        jobs = [j for j in get_viz_jobs(cfg)
                if str(j.get("kind", "")).strip().lower() in {"strain_dynamics", "storyboard"}]
        
        if not jobs:
            parser.print_help()
            print("\nError: --snapshot_dir required when no TOML jobs found")
            return 1
        
        print(f"Found {len(jobs)} jobs")
        
        for idx, job in enumerate(progress(jobs, desc="Processing jobs"), 1):
            snapdir = job.get("snapshot_dir")
            if not snapdir:
                print(f"Warning: Job {idx} missing snapshot_dir -> skipped")
                continue
            
            # CRITICAL FIX 1: Use proper precedence with None handling
            view = _utils.get_parameter("view", viz, job, args.view, "strain")
            n_frames = _utils.get_parameter("n_frames", viz, job, args.n_frames, 12)
            ncols = _utils.get_parameter("ncols", viz, job, args.ncols, 4)
            defect_threshold = _utils.get_parameter("defect_threshold", viz, job, args.defect_threshold, 1.5)
            treat_immobile = _utils.get_parameter("treat_immobile_as_fixed", viz, job, args.treat_immobile_as_fixed, False)
            
            with_corr = (args.with_defect_corr or job.get("with_defect_corr", False))
            do_storyboard = (args.storyboard or 
                           str(job.get("kind", "")).strip().lower() == "storyboard")
            
            # Output directory: CLI > Job > default (input/viz)
            if args.outdir:
                outdir = Path(args.outdir)
            elif job.get("outdir"):
                outdir = Path(job["outdir"])
            else:
                outdir = Path(snapdir) / "viz"
            
            print(f"\n--- Job {idx}/{len(jobs)} ---")
            print(f"Input: {short_path(Path(snapdir))}")
            print(f"Output: {short_path(outdir)}")
            print(f"View: {view}")
            print(f"Defect threshold: {defect_threshold}")
            
            outdir.mkdir(parents=True, exist_ok=True)
            
            snap_paths = list_snapshots(snapdir, pattern=args.pattern)
            if not snap_paths:
                print(f"  ⚠️  No snapshots found -> skipped")
                continue
            
            print(f"Snapshots: {len(snap_paths)}")
            
            # FIX: Strain series - compute if plot enabled OR needed for correlation/storyboard
            plot_series = _utils.is_plot_enabled("strain_series", viz, job)
            series_needed = plot_series or with_corr or do_storyboard
            
            if series_needed:
                with _utils.Timer() as t:
                    series = compute_strain_series_from_snapshots(snap_paths)
                    # Only plot if enabled in TOML
                    if plot_series:
                        plot_strain_series(series, outdir=outdir, cfg=cfg)
                print(f"  Strain series computed: {t}")
            
            # FIX: Defect correlation with plot gating
            if with_corr and _utils.is_plot_enabled("strain_vs_defects", viz, job):
                if not series_needed:
                    # CRITICAL FIX 2: Compute series on demand
                    with _utils.Timer() as t:
                        series = compute_strain_series_from_snapshots(snap_paths)
                    print(f"  Strain series computed for correlation: {t}")
                
                with _utils.Timer() as t:
                    defect_counts = []
                    for p in progress(snap_paths, desc="Counting defects"):
                        state = load_tiling_state(p)
                        defect_counts.append(
                            defect_count(state, defect_threshold, treat_immobile)
                        )
                    plot_strain_vs_defects(series, defect_counts, outdir=outdir, cfg=cfg)
                print(f"  Defect correlation: {t}")
            
            # FIX: Storyboard with plot gating
            if do_storyboard and _utils.is_plot_enabled("storyboard", viz, job):
                with _utils.Timer() as t:
                    make_storyboard(snapdir, view=view, n_frames=n_frames, 
                                  ncols=ncols, outdir=outdir, cfg=cfg)
                print(f"  Storyboard: {t}")
        
        total_time = time.time() - start_time
        print(f"\n{'='*60}")
        print(f"Total time: {total_time:.1f}s")
        print(f"{'='*60}")
        return 0
    
    # ===== SINGLE-RUN MODE (with --snapshot_dir) =====
    print(f"\n{'='*60}")
    print("STRAIN DYNAMICS: Single Run")
    print(f"{'='*60}")
    print(f"Input: {short_path(Path(args.snapshot_dir))}")
    
    # Get parameters with proper precedence
    view = _utils.get_parameter("view", viz, None, args.view, "strain")
    n_frames = _utils.get_parameter("n_frames", viz, None, args.n_frames, 12)
    ncols = _utils.get_parameter("ncols", viz, None, args.ncols, 4)
    defect_threshold = _utils.get_parameter("defect_threshold", viz, None, args.defect_threshold, 1.5)
    treat_immobile = _utils.get_parameter("treat_immobile_as_fixed", viz, None, args.treat_immobile_as_fixed, False)
    
    # Output directory: CLI > default (input/viz)
    if args.outdir:
        outdir = Path(args.outdir)
    else:
        outdir = Path(args.snapshot_dir) / "viz"
    
    print(f"Output: {short_path(outdir)}")
    outdir.mkdir(parents=True, exist_ok=True)
    
    snap_paths = list_snapshots(args.snapshot_dir, pattern=args.pattern)
    if not snap_paths:
        print(f"Error: No snapshots found in {args.snapshot_dir}")
        return 1
    
    print(f"Snapshots: {len(snap_paths)}")
    
    # Check TOML enabled plots
    enabled_plots = _utils.get_enabled_plots(viz, "strain")
    
    # CRITICAL FIX 2: Compute series if needed for correlation or storyboard
    compute_series = (args.with_defect_corr or args.storyboard)
    series = None
    
    # Strain series
    if "strain_series" in enabled_plots or not enabled_plots:
        print("\nGenerating strain series...")
        with _utils.Timer() as t:
            series = compute_strain_series_from_snapshots(snap_paths)
            plot_strain_series(series, outdir=outdir, cfg=cfg)
        print(f"  Completed in {t}")
    elif compute_series:
        # Need series for correlation/storyboard
        print("\nComputing strain series (required for correlation/storyboard)...")
        with _utils.Timer() as t:
            series = compute_strain_series_from_snapshots(snap_paths)
        print(f"  Computed in {t}")
    
    # Defect correlation
    if args.with_defect_corr and "strain_vs_defects" in enabled_plots:
        if series is None:
            # Compute series if not already computed
            print("\nComputing strain series for correlation...")
            with _utils.Timer() as t:
                series = compute_strain_series_from_snapshots(snap_paths)
            print(f"  Computed in {t}")
        
        print("\nGenerating defect correlation...")
        with _utils.Timer() as t:
            defect_counts = []
            for p in progress(snap_paths, desc="Counting defects"):
                state = load_tiling_state(p)
                defect_counts.append(
                    defect_count(state, defect_threshold, treat_immobile)
                )
            plot_strain_vs_defects(series, defect_counts, outdir=outdir, cfg=cfg)
        print(f"  Completed in {t}")
    
    # Storyboard
    if args.storyboard and "storyboard" in enabled_plots:
        print(f"\nGenerating storyboard ({n_frames} frames)...")
        with _utils.Timer() as t:
            make_storyboard(args.snapshot_dir, view=view,
                          n_frames=n_frames, ncols=ncols,
                          outdir=outdir, cfg=cfg)
        print(f"  Completed in {t}")
    
    total_time = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"Total time: {total_time:.1f}s")
    print(f"{'='*60}")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())