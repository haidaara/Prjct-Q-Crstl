#!/usr/bin/env python3
"""Compare baseline/damaged/healed (or baseline/healed) states.

Usage:
  python scripts/viz/02_viz_compare.py --baseline file.json --healed file.json [--damaged file.json] [--view TYPE] [--drift]
  python scripts/viz/02_viz_compare.py  # runs from TOML jobs if configured

Parameters (with precedence: CLI > TOML job > TOML global > default):
  --view: View type (geometry|energy|defects|class|growth|strain|change)
          Default from TOML: compare_view = "energy"
  --drift: Generate phason drift series
          Default from TOML: compare_drift = false

Examples:
  # Baseline vs Healed
  python scripts/viz/02_viz_compare.py \
    --baseline data/baseline.json \
    --healed data/healed.json \
    --view energy
  
  # Baseline vs Damaged vs Healed
  python scripts/viz/02_viz_compare.py \
    --baseline data/baseline.json \
    --damaged data/damaged.json \
    --healed data/healed.json \
    --view strain --drift
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
from src.viz.compare_plots import plot_pair, plot_triptych, plot_change_panel, plot_phason_drift_series


def main() -> int:
    start_time = time.time()
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="See configs/publication_plots.toml for job configurations and defaults."
    )
    parser.add_argument("--baseline", default=None, help="Baseline state JSON")
    parser.add_argument("--healed", default=None, help="Current/healed state JSON")
    parser.add_argument("--damaged", default=None, help="Optional damaged state JSON")
    parser.add_argument("--view", default=None, help="View type (geometry|energy|defects|class|growth|strain|change)")
    parser.add_argument("--drift", action="store_true", default=None, help="Generate phason drift series")
    parser.add_argument("--outdir", default=None, help="Output directory (optional)")
    parser.add_argument("--config", default=None, help="Path to publication_plots.toml (optional)")
    
    args = parser.parse_args()
    
    cfg = load_publication_config(args.config)
    viz = cfg.get("viz_jobs", {})
    
    # If required inputs are not provided, run all TOML jobs of kind=compare
    if not args.baseline or not args.healed:
        if not viz.get("enabled", False):
            print("viz_jobs.enabled is false -> nothing to run")
            return 0

        jobs = [j for j in get_viz_jobs(cfg) if str(j.get("kind", "")).strip().lower() == "compare"]
        if not jobs:
            print("No compare jobs found under [viz_jobs.jobs] (kind='compare')")
            return 0

        print(f"\nFound {len(jobs)} comparison visualization jobs")
        
        for job_idx, job in enumerate(progress(jobs, desc="Processing jobs"), 1):
            baseline = job.get("baseline")
            damaged = job.get("damaged")
            healed = job.get("healed") or job.get("current")
            
            if not baseline or not healed:
                print(f"Warning: Job {job_idx}/{len(jobs)} missing baseline/healed -> skipped")
                continue

            # Get parameters with proper precedence
            view = _utils.get_parameter("view", viz, job, args.view, viz.get("compare_view", "energy"))
            drift = _utils.get_parameter("compare_drift", viz, job, args.drift, False)
            
            # Determine output directory
            outdir = _utils.resolve_output_dir(
                Path(baseline), 
                args.outdir,
                job.get("outdir"),
                cfg
            )
            
            _utils.print_job_info(job_idx, len(jobs), job, outdir)
            print(f"View: {view}")
            print(f"Drift: {drift}")
            
            outdir.mkdir(parents=True, exist_ok=True)
            b = load_tiling_state(baseline)
            h = load_tiling_state(healed)
            
            # Get enabled comparison plots
            enabled_plots = _utils.get_enabled_plots(viz, "compare", job)
            
            if damaged:
                d = load_tiling_state(damaged)
                if "triptych" in enabled_plots:
                    plot_triptych(b, d, h, view=view, outdir=outdir, cfg=cfg)
            elif "pair" in enabled_plots:
                plot_pair(b, h, view=view, outdir=outdir, cfg=cfg)
            
            if "change_panel" in enabled_plots:
                plot_change_panel(b, h, outdir=outdir, cfg=cfg)
            
            if "phason_drift_series" in enabled_plots and drift:
                if damaged:
                    plot_phason_drift_series(b, [("damaged", d), ("healed", h)], outdir=outdir, cfg=cfg)
                else:
                    plot_phason_drift_series(b, [("healed", h)], outdir=outdir, cfg=cfg)
        
        elapsed = time.time() - start_time
        print(f"\nCompleted {len(jobs)} jobs in {elapsed:.1f}s")
        return 0

    # ===== SINGLE-RUN MODE (with --baseline and --healed) =====
    print(f"\nComparing states:")
    print(f"  Baseline: {short_path(Path(args.baseline))}")
    print(f"  Healed: {short_path(Path(args.healed))}")
    if args.damaged:
        print(f"  Damaged: {short_path(Path(args.damaged))}")
    
    # Get parameters with proper precedence
    view = _utils.get_parameter("compare_view", viz, None, args.view, "energy")
    drift = _utils.get_parameter("compare_drift", viz, None, args.drift, False)
    
    # Determine output directory
    outdir = _utils.resolve_output_dir(
        Path(args.baseline), 
        args.outdir,
        None,
        cfg
    )
    
    print(f"Output directory: {outdir}")
    print(f"View: {view}")
    print(f"Drift: {drift}")
    
    outdir.mkdir(parents=True, exist_ok=True)
    b = load_tiling_state(args.baseline)
    h = load_tiling_state(args.healed)
    
    # Get enabled comparison plots from TOML (CLI doesn't override plot types)
    enabled_plots = _utils.get_enabled_plots(viz, "compare", None)
    
    if args.damaged:
        d = load_tiling_state(args.damaged)
        if "triptych" in enabled_plots:
            plot_triptych(b, d, h, view=view, outdir=outdir, cfg=cfg)
    elif "pair" in enabled_plots:
        plot_pair(b, h, view=view, outdir=outdir, cfg=cfg)
    
    if "change_panel" in enabled_plots:
        plot_change_panel(b, h, outdir=outdir, cfg=cfg)
    
    if "phason_drift_series" in enabled_plots and drift:
        if args.damaged:
            plot_phason_drift_series(b, [("damaged", d), ("healed", h)], outdir=outdir, cfg=cfg)
        else:
            plot_phason_drift_series(b, [("healed", h)], outdir=outdir, cfg=cfg)
    
    elapsed = time.time() - start_time
    print(f"\nCompleted in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())