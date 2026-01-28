#!/usr/bin/env python3
"""Spatial (distance-to-obstacle) profiles from a single state JSON.

Usage:
  python scripts/viz/03_viz_spatial.py --input file.json [--bin_edges 0,2,4,6,8,10] [--defect_threshold 1.5]
  python scripts/viz/03_viz_spatial.py  # runs from TOML jobs if configured

Parameters (with precedence: CLI > TOML job > TOML global > default):
  --bin_edges: Comma-separated bin edges for distance analysis
              Default from TOML: none → use [0, 2, 4, 6, 8, 10]
  --defect_threshold: Threshold for defect classification
                     Default from TOML: viz_jobs.defect_threshold = 1.5
  --treat_immobile_as_fixed: Treat immobile tiles as fixed obstacles
                            Default from TOML: viz_jobs.treat_immobile_as_fixed = false

Examples:
  python scripts/viz/03_viz_spatial.py \
    --input data/experiments/healing/run_001/final_state.json \
    --bin_edges 0,1,2,3,4,5,6,8,10 \
    --defect_threshold 1.5

Outputs:
  - defect_density_by_distance (mean defect fraction per radial bin)
"""

from __future__ import annotations

import sys
import time
import argparse
from pathlib import Path

# Ensure project root is on PYTHONPATH
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.path.insert(0, str(Path(__file__).parent))
import _utils

from src.viz.config import load_publication_config, get_viz_jobs
from src.viz.io import load_tiling_state, short_path
from src.viz.progress import progress
from src.viz.spatial_plots import compute_spatial_bin_stats, plot_defect_density_by_distance


def main() -> int:
    start_time = time.time()
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="See configs/publication_plots.toml for job configurations and defaults."
    )
    parser.add_argument("--input", default=None, help="Path to a state JSON containing tiles")
    parser.add_argument("--outdir", default=None, help="Output directory (optional)")
    parser.add_argument("--config", default=None, help="Path to publication_plots.toml (optional)")
    parser.add_argument("--bin_edges", default=None, help="Bin edges for distance analysis (comma-separated)")
    parser.add_argument("--defect_threshold", type=float, default=None, 
                       help="Override defect threshold (default: from TOML)")
    parser.add_argument("--treat_immobile_as_fixed", action="store_true", default=None,
                       help="Treat immobile tiles as fixed obstacles (default: from TOML)")
    parser.add_argument("--plots", default=None, help="Override enabled plots (comma-separated)")

    
    args = parser.parse_args()
    
    cfg = load_publication_config(args.config)
    viz = cfg.get("viz_jobs", {})
    
    # If no --input was provided, run all TOML jobs of kind=spatial
    if not args.input:
        if not viz.get("enabled", False):
            print("viz_jobs.enabled is false -> nothing to run")
            return 0

        jobs = [j for j in get_viz_jobs(cfg) if str(j.get("kind", "")).strip().lower() == "spatial"]
        if not jobs:
            print("No spatial jobs found under [viz_jobs.jobs] (kind='spatial')")
            return 0

        print(f"\nFound {len(jobs)} spatial analysis jobs")
        
        for job_idx, job in enumerate(progress(jobs, desc="Processing jobs"), 1):
            inp = job.get("input")
            if not inp:
                print(f"Warning: Job {job_idx}/{len(jobs)} missing 'input' -> skipped")
                continue

            # Get parameters with proper precedence
            bin_edges = _utils.get_parameter(
                "bin_edges", viz, job, args.bin_edges, [0, 2, 4, 6, 8, 10]
            )
            defect_threshold = _utils.get_parameter(
                "defect_threshold", viz, job, args.defect_threshold, 1.5
            )
            treat_immobile_as_fixed = _utils.get_parameter(
                "treat_immobile_as_fixed", viz, job, 
                args.treat_immobile_as_fixed, False
            )
            
            # Convert bin_edges to list of floats if it's a string
            if isinstance(bin_edges, str):
                bin_edges = _utils.csv_to_floats(bin_edges)
            elif not isinstance(bin_edges, list):
                bin_edges = [0, 2, 4, 6, 8, 10]
            
            # Determine output directory
            outdir = _utils.resolve_output_dir(
                Path(inp), 
                args.outdir,
                job.get("outdir"),
                cfg
            )
            
            _utils.print_job_info(job_idx, len(jobs), job, outdir)
            print(f"Bin edges: {bin_edges}")
            print(f"Defect threshold: {defect_threshold}")
            print(f"Treat immobile as fixed: {treat_immobile_as_fixed}")
            
            outdir.mkdir(parents=True, exist_ok=True)
            state = load_tiling_state(inp)
            
            # Check if spatial plot is enabled
            enabled_plots = _utils.get_enabled_plots(viz, "spatial", job, args.plots)
            if "defect_density_by_distance" not in enabled_plots:
                print("Note: defect_density_by_distance not enabled in TOML -> skipped")
                continue
            
            # Compute and plot
            snap = compute_spatial_bin_stats(
                state,
                bin_edges=bin_edges,
                defect_threshold=defect_threshold,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
            )
            plot_defect_density_by_distance(snap, outdir=outdir, cfg=cfg)
        
        elapsed = time.time() - start_time
        print(f"\nCompleted {len(jobs)} jobs in {elapsed:.1f}s")
        return 0

    # ===== SINGLE-RUN MODE (with --input) =====
    print(f"\nProcessing: {short_path(Path(args.input))}")
    
    # Get parameters with proper precedence (no job config in single-run mode)
    bin_edges = _utils.get_parameter(
        "bin_edges", viz, None, args.bin_edges, [0, 2, 4, 6, 8, 10]
    )
    defect_threshold = _utils.get_parameter(
        "defect_threshold", viz, None, args.defect_threshold, 1.5
    )
    treat_immobile_as_fixed = _utils.get_parameter(
        "treat_immobile_as_fixed", viz, None, 
        args.treat_immobile_as_fixed, False
    )
    
    # Convert bin_edges to list of floats if it's a string
    if isinstance(bin_edges, str):
        bin_edges = _utils.csv_to_floats(bin_edges)
    elif not isinstance(bin_edges, list):
        bin_edges = [0, 2, 4, 6, 8, 10]
    
    # Determine output directory
    outdir = _utils.resolve_output_dir(
        Path(args.input), 
        args.outdir,
        None,
        cfg
    )
    
    print(f"Output directory: {outdir}")
    print(f"Bin edges: {bin_edges}")
    print(f"Defect threshold: {defect_threshold}")
    print(f"Treat immobile as fixed: {treat_immobile_as_fixed}")
    
    outdir.mkdir(parents=True, exist_ok=True)
    state = load_tiling_state(args.input)
    
    # Check if spatial plot is enabled
    enabled_plots = _utils.get_enabled_plots(viz, "spatial", None, args.plots)
    if _utils.is_plot_enabled("defect_density_by_distance", viz, None):
        print("Note: defect_density_by_distance not enabled in TOML -> skipped")
        print("      Enable it in TOML [viz_jobs.plots_enabled] or use --plots to override")
        return 0
    
    # Compute and plot
    snap = compute_spatial_bin_stats(
        state,
        bin_edges=bin_edges,
        defect_threshold=defect_threshold,
        treat_immobile_as_fixed=treat_immobile_as_fixed,
    )
    plot_defect_density_by_distance(snap, outdir=outdir, cfg=cfg)
    
    elapsed = time.time() - start_time
    print(f"\nCompleted in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())