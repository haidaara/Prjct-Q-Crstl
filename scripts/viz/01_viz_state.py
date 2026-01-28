#!/usr/bin/env python3
"""Quick visualization for a single tiling state JSON.

Usage:
  python scripts/viz/01_viz_state.py --input file.json [--outdir dir] [--plots plot1,plot2]
  python scripts/viz/01_viz_state.py  # runs from TOML jobs if configured

Plot types (state-specific only):
  - matrix_2x2: 2x2 publication matrix (geometry, energy, class, growth)
  - grid_3x3: 3x3 grid with various analyses
  - diffraction: FFT diffraction pattern
  - vertex_dist: Vertex class distribution bar chart
  - radial_defects: Radial defect density profile
  - strain_map: Phason strain energy map
  - strain_hist: Phason strain histogram
  - strain_vs_distance: Strain vs distance to obstacles

Examples:
  python scripts/viz/01_viz_state.py \
    --input data/processed/penrose_tiling_energy_initialized.json \
    --outdir data/viz/demo \
    --plots matrix_2x2,grid_3x3,diffraction
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

from src.viz.config import load_publication_config, get_viz_jobs
from src.viz.io import load_tiling_state, short_path
from src.viz.progress import progress
from src.viz.static_plots import (
    plot_physics_matrix,
    plot_publication_grid_3x3,
    plot_diffraction_pattern,
    plot_vertex_distribution,
    plot_radial_defect_density,
)
from src.viz.strain_plots import (
    plot_strain_energy_map,
    plot_strain_histogram,
    plot_strain_vs_distance,
)

# Valid plot types for THIS script (state visualization only)
VALID_STATE_PLOTS = {
    "matrix_2x2",
    "grid_3x3",
    "diffraction",
    "vertex_dist",
    "radial_defects",
    "strain_map",
    "strain_hist",
    "strain_vs_distance",
}


def _csv_list(s: str) -> list[str]:
    """Parse comma-separated string to list of strings."""
    return [x.strip() for x in (s or "").split(",") if x.strip()]


def _csv_floats(s: str) -> list[float]:
    """Parse comma-separated string to list of floats."""
    return [float(x.strip()) for x in (s or "").split(",") if x.strip()]


def _get_plots_from_toml(viz_config: dict) -> set[str]:
    """Get all enabled state plots from TOML configuration."""
    plots_enabled = viz_config.get("plots_enabled", {})
    
    if isinstance(plots_enabled, dict):
        # Dictionary format: {matrix_2x2 = true, grid_3x3 = false, ...}
        enabled_plots = {plot for plot, enabled in plots_enabled.items() 
                        if enabled and plot in VALID_STATE_PLOTS}
    else:
        # List format or other - fallback to all state plots
        enabled_plots = VALID_STATE_PLOTS.copy()
    
    return enabled_plots


def _get_plots_to_generate(viz_config: dict, job: dict = None, cli_plots: str = None) -> set[str]:
    """Get plots to generate with precedence: CLI > Job > TOML global."""
    # 1. CLI override (highest priority)
    if cli_plots:
        requested = set(_csv_list(cli_plots))
        valid_plots = requested & VALID_STATE_PLOTS
        invalid_plots = requested - VALID_STATE_PLOTS
        
        if invalid_plots:
            print(f"Note: Skipping non-state plot types: {', '.join(sorted(invalid_plots))}")
            print(f"      Use 02_viz_compare.py for comparison plots")
        
        return valid_plots
    
    # 2. Job-specific plots (if we have a job)
    if job:
        job_plots = job.get("plots")
        if isinstance(job_plots, list):
            requested = set(job_plots)
            return requested & VALID_STATE_PLOTS
        elif isinstance(job_plots, dict):
            requested = {plot for plot, enabled in job_plots.items() if enabled}
            return requested & VALID_STATE_PLOTS
    
    # 3. Global TOML configuration
    return _get_plots_from_toml(viz_config)


def _resolve_output_dir(input_path: Path, cli_outdir: Path = None, job_outdir: str = None) -> Path:
    """Simple output directory resolution for single script."""
    if cli_outdir:
        return Path(cli_outdir)
    if job_outdir:
        return Path(job_outdir)
    if input_path:
        return input_path.parent / "viz"
    return Path("viz_output")


def main() -> int:
    start_time = time.time()
    
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Note: For comparison plots (pair, triptych, change_panel), use 02_viz_compare.py"
    )
    parser.add_argument("--input", default=None, help="Path to a state JSON containing tiles")
    parser.add_argument("--outdir", default=None, help="Output directory (optional)")
    parser.add_argument("--config", default=None, help="Path to publication_plots.toml (optional)")
    parser.add_argument("--plots", default=None, 
                       help="Comma-separated plot names (overrides TOML, leave empty to use all TOML-enabled plots)")
    parser.add_argument("--bin_edges", default=None, help="Bin edges for strain_vs_distance (comma-separated)")
    
    args = parser.parse_args()
    
    cfg = load_publication_config(args.config)
    viz = cfg.get("viz_jobs", {})
    
    # If no --input was provided, run all TOML jobs of kind=state
    if not args.input:
        if not viz.get("enabled", False):
            print("viz_jobs.enabled is false -> nothing to run")
            return 0

        jobs = [j for j in get_viz_jobs(cfg) if str(j.get("kind", "")).strip().lower() == "state"]
        if not jobs:
            print("No state jobs found under [viz_jobs.jobs] (kind='state')")
            return 0

        print(f"\nFound {len(jobs)} state visualization jobs")
        
        for job_idx, job in enumerate(progress(jobs, desc="Processing jobs"), 1):
            inp = job.get("input")
            if not inp:
                print(f"Warning: Job {job_idx}/{len(jobs)} missing 'input' -> skipped")
                continue

            # Determine output directory
            outdir = _resolve_output_dir(
                Path(inp), 
                args.outdir,
                job.get("outdir")
            )
            
            # Determine plots to generate (filtered to state plots only)
            plots_to_generate = _get_plots_to_generate(viz, job, args.plots)
            
            if not plots_to_generate:
                print(f"Warning: Job {job_idx} has no valid state plots to generate -> skipped")
                continue
            
            print(f"\nJob {job_idx}/{len(jobs)}")
            print(f"Input: {short_path(Path(inp))}")
            print(f"Output: {outdir}")
            print(f"Plots: {', '.join(sorted(plots_to_generate))}")
            
            outdir.mkdir(parents=True, exist_ok=True)
            state = load_tiling_state(inp)
            
            for plot_type in progress(sorted(plots_to_generate), desc="Generating plots"):
                if plot_type == "matrix_2x2":
                    plot_physics_matrix(state, outdir=outdir, cfg=cfg)
                elif plot_type == "grid_3x3":
                    plot_publication_grid_3x3(state, outdir=outdir, cfg=cfg)
                elif plot_type == "diffraction":
                    plot_diffraction_pattern(state, outdir=outdir, cfg=cfg)
                elif plot_type == "vertex_dist":
                    plot_vertex_distribution(state, outdir=outdir, cfg=cfg)
                elif plot_type == "radial_defects":
                    plot_radial_defect_density(state, outdir=outdir, cfg=cfg)
                elif plot_type == "strain_map":
                    plot_strain_energy_map(state, outdir=outdir, cfg=cfg)
                elif plot_type == "strain_hist":
                    plot_strain_histogram(state, outdir=outdir, cfg=cfg)
                elif plot_type == "strain_vs_distance":
                    edges_raw = args.bin_edges or job.get("bin_edges") or "0,2,4,6,8,10,12"
                    edges = _csv_floats(str(edges_raw))
                    plot_strain_vs_distance(state, bin_edges=edges, outdir=outdir, cfg=cfg)
                else:
                    print(f"Error: Unknown plot type for state visualization: {plot_type}")
        
        elapsed = time.time() - start_time
        print(f"\nCompleted {len(jobs)} jobs in {elapsed:.1f}s")
        return 0

    # ===== SINGLE-RUN MODE (with --input) =====
    print(f"\nProcessing: {short_path(Path(args.input))}")
    
    # Determine output directory
    outdir = _resolve_output_dir(Path(args.input), args.outdir, None)
    
    print(f"Output directory: {outdir}")
    outdir.mkdir(parents=True, exist_ok=True)
    
    state = load_tiling_state(args.input)
    
    # Get plots to generate with proper precedence
    # If --plots is explicitly empty string or not provided, use TOML configuration
    if args.plots is not None and args.plots.strip() == "":
        # User explicitly passed empty --plots, so generate nothing
        print("Note: Empty --plots argument provided, generating no plots")
        plots_to_generate = set()
    elif args.plots is not None:
        # User provided specific plots via CLI
        requested_plots = set(_csv_list(args.plots))
        plots_to_generate = requested_plots & VALID_STATE_PLOTS
        invalid_plots = requested_plots - VALID_STATE_PLOTS
        
        if invalid_plots:
            print(f"Note: Skipping non-state plot types: {', '.join(sorted(invalid_plots))}")
            print(f"      Use 02_viz_compare.py for comparison plots")
    else:
        # No --plots argument: use ALL enabled plots from TOML
        plots_to_generate = _get_plots_from_toml(viz)
    
    if not plots_to_generate:
        if args.plots is not None and args.plots.strip() != "":
            print("Error: No valid state plots to generate from the provided list")
        else:
            print("Note: No state plots enabled in TOML configuration")
        return 0
    
    print(f"Generating {len(plots_to_generate)} plots: {', '.join(sorted(plots_to_generate))}")
    
    for plot_type in progress(sorted(plots_to_generate), desc="Generating plots"):
        if plot_type == "matrix_2x2":
            plot_physics_matrix(state, outdir=outdir, cfg=cfg)
        elif plot_type == "grid_3x3":
            plot_publication_grid_3x3(state, outdir=outdir, cfg=cfg)
        elif plot_type == "diffraction":
            plot_diffraction_pattern(state, outdir=outdir, cfg=cfg)
        elif plot_type == "vertex_dist":
            plot_vertex_distribution(state, outdir=outdir, cfg=cfg)
        elif plot_type == "radial_defects":
            plot_radial_defect_density(state, outdir=outdir, cfg=cfg)
        elif plot_type == "strain_map":
            plot_strain_energy_map(state, outdir=outdir, cfg=cfg)
        elif plot_type == "strain_hist":
            plot_strain_histogram(state, outdir=outdir, cfg=cfg)
        elif plot_type == "strain_vs_distance":
            edges_raw = args.bin_edges or "0,2,4,6,8,10,12"
            edges = _csv_floats(str(edges_raw))
            plot_strain_vs_distance(state, bin_edges=edges, outdir=outdir, cfg=cfg)
        else:
            print(f"Error: Unknown plot type for state visualization: {plot_type}")
    
    elapsed = time.time() - start_time
    print(f"\nCompleted in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())