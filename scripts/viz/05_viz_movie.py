#!/usr/bin/env python3
"""Create movies from snapshot directories.

Usage:
  # Single run - REQUIRES --snapshot_dir
  python 05_viz_movie.py --snapshot_dir data/snapshots
  
  # With custom view and FPS
  python 05_viz_movie.py --snapshot_dir data/snapshots --view energy --fps 24
  
  # Create storyboard only
  python 05_viz_movie.py --snapshot_dir data/snapshots --storyboard
  
  # TOML batch mode (no --snapshot_dir, requires enabled TOML jobs)
  python 05_viz_movie.py

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
from src.viz.io import short_path, list_snapshots
from src.viz.progress import progress
from src.viz.movie import make_movie, make_storyboard


def main() -> int:
    start_time = time.time()
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--snapshot_dir", help="Directory with snapshot JSON files")
    parser.add_argument("--outdir", help="Output directory (default: snapshot_dir/viz)")

    parser.add_argument("--config", default=None, help="Path to publication_plots.toml")
    
    # CRITICAL FIX: Set CLI defaults to None so job/TOML can override
    parser.add_argument("--view", default=None, help="View type (strain, energy, geometry, etc.)")
    parser.add_argument("--fps", type=int, default=None, help="Frames per second")
    parser.add_argument("--format", default=None, choices=["gif", "mp4"], help="Output format")
    
    # Movie/storyboard options
    parser.add_argument("--movie", action=argparse.BooleanOptionalAction, default=None, 
                       help="Generate animated movie")
    parser.add_argument("--storyboard", action=argparse.BooleanOptionalAction, default=None,
                       help="Generate storyboard contact sheet")
    parser.add_argument("--n_frames", type=int, default=None, help="Number of frames for storyboard")
    parser.add_argument("--ncols", type=int, default=None, help="Columns in storyboard grid")
    
    args = parser.parse_args()
    
    # CRITICAL FIX: Handle config loading with error checking
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
        print("MOVIE GENERATION: TOML Batch Mode")
        print(f"{'='*60}")
        
        if not viz.get("enabled", False):
            parser.print_help()
            print("\nError: --snapshot_dir required when TOML jobs disabled")
            return 1
        
        jobs = [j for j in get_viz_jobs(cfg)
                if str(j.get("kind", "")).strip().lower() in {"movie", "storyboard"}]
        
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
            
            # CRITICAL FIX: Use proper precedence with None handling
            # View: special two-step fallback for movie_view then view
            view = args.view
            if view is None:
                if "movie_view" in job:
                    view = job["movie_view"]
                elif "view" in job:
                    view = job["view"]
                elif "movie_view" in viz:
                    view = viz["movie_view"]
                elif "view" in viz:
                    view = viz["view"]
                else:
                    view = "strain"
            
            fps = _utils.get_parameter("fps", viz, job, args.fps, 12)
            format_type = _utils.get_parameter("format", viz, job, args.format, "gif")
            n_frames = _utils.get_parameter("n_frames", viz, job, args.n_frames, 12)
            ncols = _utils.get_parameter("ncols", viz, job, args.ncols, 4)
            
            # Determine if we should create movie or storyboard based on job kind
            job_kind = str(job.get("kind", "")).strip().lower()
            
            # Use proper boolean precedence
            create_movie = _utils.get_parameter("movie", viz, job, args.movie, job_kind == "movie")
            create_storyboard = _utils.get_parameter("storyboard", viz, job, args.storyboard, job_kind == "storyboard")
            
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
            print(f"FPS: {fps}")
            print(f"Format: {format_type}")
            
            outdir.mkdir(parents=True, exist_ok=True)

            # Apply per-job overrides (scales, dpi, figsize, gamma, etc.)
            job_cfg = _utils.cfg_with_job_overrides(cfg, job)
            
            # Check if enabled in TOML
            if create_movie and not _utils.is_plot_enabled("movie", viz, job):

                print("  Movie disabled in TOML -> skipped")
                create_movie = False
            
            if create_storyboard and not _utils.is_plot_enabled("storyboard", viz, job):
                print("  Storyboard disabled in TOML -> skipped")
                create_storyboard = False
            
            # Generate movie
            if create_movie:
                print(f"  Generating movie ({format_type}, {fps} fps)...")
                with _utils.Timer() as t:
                    save_path = Path(outdir) / f"movie_{Path(str(snapdir)).name}_{view}.{str(format_type).lower()}"
                    result = make_movie(
                        snapdir,
                        view=view,
                        fps=fps,
                        save_path=save_path,
                        outdir=outdir,
                        cfg=job_cfg
                    )

                    if result:
                        print(f"    Movie saved: {short_path(result)}")
                    else:
                        print(f"    Movie generation failed")
            # Wall-clock runtime (not video duration)
            wall_s = float(t.elapsed)  # use t.elapsed for float conversion
            
            # Expected video duration from frames/fps
            try:
                frames_dir = Path(outdir) / "frames" / f"{Path(str(snapdir)).name}_{view}"
                n = len(list(frames_dir.glob("frame_*.png")))
            except Exception:
                n = None
            
            if n is not None and fps > 0:
                dur = n / float(fps)
                print(f"  Wall time: {wall_s:.1f}s")
                print(f"  Video duration: {dur:.2f}s  ({n} frames @ {fps} fps)")
            else:
                print(f"  Wall time: {wall_s:.1f}s")
                        
            # Generate storyboard
            if create_storyboard:
                print(f"  Generating storyboard ({n_frames} frames)...")
                with _utils.Timer() as t:
                    make_storyboard(
                        snapdir,
                        view=view,
                        n_frames=n_frames,
                        ncols=ncols,
                        outdir=outdir,
                        cfg=job_cfg
                    )
                print(f"  Storyboard time: {t}")
        
        total_time = time.time() - start_time
        print(f"\n{'='*60}")
        print(f"Total time: {total_time:.1f}s")
        print(f"{'='*60}")
        return 0
    
    # ===== SINGLE-RUN MODE (with --snapshot_dir) =====
    print(f"\n{'='*60}")
    print("MOVIE GENERATION: Single Run")
    print(f"{'='*60}")
    print(f"Input: {short_path(Path(args.snapshot_dir))}")
    
    # Add input validation
    snap_paths = list_snapshots(args.snapshot_dir)
    if not snap_paths:
        print(f"Error: No snapshots found in {args.snapshot_dir}")
        return 1
    
    # Get parameters with proper precedence
    # View: special two-step fallback for movie_view then view
    view = args.view
    if view is None:
        if "movie_view" in viz:
            view = viz["movie_view"]
        elif "view" in viz:
            view = viz["view"]
        else:
            view = "strain"
    
    fps = _utils.get_parameter("fps", viz, None, args.fps, 12)
    format_type = _utils.get_parameter("format", viz, None, args.format, "gif")
    n_frames = _utils.get_parameter("n_frames", viz, None, args.n_frames, 12)
    ncols = _utils.get_parameter("ncols", viz, None, args.ncols, 4)
    
    # Determine what to create
    create_movie = args.movie
    create_storyboard = args.storyboard
    
    # If no explicit flags, check TOML defaults
    if create_movie is None and create_storyboard is None:
        enabled_plots = _utils.get_enabled_plots(viz, "movie")
        create_movie = "movie" in enabled_plots
        create_storyboard = "storyboard" in enabled_plots
    else:
        # Interpret None as False when the other is explicitly set
        if create_movie is None:
            create_movie = False
        if create_storyboard is None:
            create_storyboard = False

    
    # Output directory: CLI > default (input/viz)
    if args.outdir:
        outdir = Path(args.outdir)
    else:
        outdir = Path(args.snapshot_dir) / "viz"
    
    print(f"Output: {short_path(outdir)}")
    outdir.mkdir(parents=True, exist_ok=True)
    
    # Generate movie
    if create_movie:
        print(f"\nGenerating movie ({format_type}, {fps} fps)...")
        with _utils.Timer() as t:
            save_path = outdir / f"movie_{Path(str(args.snapshot_dir)).name}_{view}.{str(format_type).lower()}"
            result = make_movie(
                args.snapshot_dir,
                view=view,
                fps=fps,
                save_path=save_path,
                outdir=outdir,
                cfg=cfg
            )


            if result:
                print(f"  Movie saved: {short_path(result)}")
            else:
                print(f"  Movie generation failed")
        print(f"  Completed in {t}")
    
    # Generate storyboard
    if create_storyboard:
        print(f"\nGenerating storyboard ({n_frames} frames)...")
        with _utils.Timer() as t:
            make_storyboard(
                args.snapshot_dir,
                view=view,
                n_frames=n_frames,
                ncols=ncols,
                outdir=outdir,
                cfg=cfg
            )
        print(f"  Completed in {t}")
    
    # If nothing was created
    if not create_movie and not create_storyboard:
        print("\nNote: No action specified and nothing enabled in TOML.")
        print("      Use --movie, --storyboard, or enable in TOML.")
    
    total_time = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"Total time: {total_time:.1f}s")
    print(f"{'='*60}")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())