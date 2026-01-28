#!/usr/bin/env python3
"""Run visualization jobs from configs/publication_plots.toml with group toggles.

Usage:
    python scripts/viz/00_viz_from_toml.py

Configuration:
    See configs/publication_plots.toml for job definitions and plot toggles.
    Groups can be enabled/disabled via groups_enabled dictionary.

Examples:
    # Run all jobs from TOML
    python scripts/viz/00_viz_from_toml.py
    
    # Use specific config file
    python scripts/viz/00_viz_from_toml.py --config my_config.toml
"""

from __future__ import annotations

import sys
import argparse
from pathlib import Path

# Add current directory to path for _utils import
sys.path.insert(0, str(Path(__file__).parent))

import _utils
from src.viz.io import load_tiling_state
from src.viz.static_plots import (
    plot_physics_matrix,
    plot_publication_grid_3x3,
    plot_diffraction_pattern,
    plot_vertex_distribution,
    plot_radial_defect_density,
)
from src.viz.compare_plots import plot_pair, plot_triptych, plot_change_panel, plot_phason_drift_series
from src.viz.strain_plots import (
    plot_strain_energy_map,
    plot_strain_histogram,
    plot_strain_vs_distance,
    plot_strain_series,
    plot_strain_vs_defects,
)
from src.viz.dashboards import plot_healing_dashboard, plot_spatial_dashboard
from src.viz.healing_plots import (
    plot_energy_evolution,
    plot_defect_timeline,
    plot_acceptance_rate,
    plot_healing_efficiency,
    plot_annealing_hysteresis,
)
from src.viz.movie import make_storyboard, make_movie
from src.viz.spatial_plots import compute_spatial_bin_stats, plot_defect_density_by_distance
from src.viz.panels import (
    draw_geometry,
    draw_energy,
    draw_defects,
    draw_class,
    draw_growth,
    draw_strain,
)


def process_state_job(job: dict[str, Any], viz_config: dict[str, Any], cfg: dict[str, Any]):
    """Process a single state visualization job."""
    inp = job.get("input")
    if not inp:
        print("Warning: Missing job.input -> skipped")
        return
    
    state = load_tiling_state(inp)
    outdir = _utils.resolve_output_dir(Path(inp), None, job.get("outdir"), cfg)
    
    # Get plots to generate
    plot_list = job.get("plots", ["matrix_2x2", "grid_3x3", "diffraction", "vertex_dist", 
                                 "radial_defects", "strain_map", "strain_hist", "strain_vs_distance"])

    enabled_plots = _utils.get_enabled_plots(viz_config, "state", {"plots": plot_list})
    enabled_plots = [p for p in plot_list if p in enabled_plots]
    
    if not enabled_plots:
        print("No plots enabled for this job -> skipped")
        return
    
    print(f"Generating {len(enabled_plots)} plots: {', '.join(sorted(enabled_plots))}")
    
    # Generate each enabled plot
    for plot_type in _utils.progress(sorted(enabled_plots), desc="Generating plots"):
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
            edges = job.get("bin_edges", [0, 2, 4, 6, 8, 10, 12])
            plot_strain_vs_distance(state, bin_edges=edges, outdir=outdir, cfg=cfg)


def process_compare_job(job: dict[str, Any], viz_config: dict[str, Any], cfg: dict[str, Any]):
    """Process a comparison job."""
    baseline = job.get("baseline")
    damaged = job.get("damaged")
    healed = job.get("healed") or job.get("current")
    if not baseline or not healed:
        print("Warning: Need job.baseline and job.healed (or job.current) -> skipped")
        return
    
    b = load_tiling_state(baseline)
    h = load_tiling_state(healed)
    d = load_tiling_state(damaged) if damaged else None
    view = job.get("view", "energy")

    outdir = _utils.resolve_output_dir(Path(baseline), None, job.get("outdir"), cfg)
    
    # Check which comparison plots are enabled
    plot_list = ["pair", "triptych", "change_panel", "phason_drift_series"]
    enabled_plots = _utils.get_enabled_plots(viz_config, "compare", {"plots": plot_list})
    enabled_plots = [p for p in plot_list if p in enabled_plots]
    
    if d is not None and "triptych" in enabled_plots:
        plot_triptych(b, d, h, view=view, outdir=outdir, cfg=cfg)

    elif "pair" in enabled_plots:
        plot_pair(b, h, view=view, outdir=outdir, cfg=cfg)
    
    if "change_panel" in enabled_plots:
        plot_change_panel(b, h, outdir=outdir, cfg=cfg)
    
    if "phason_drift_series" in enabled_plots:
        series = [("healed", h)] if d is None else [("damaged", d), ("healed", h)]
        plot_phason_drift_series(b, series, outdir=outdir, cfg=cfg)



def process_strain_dynamics_job(job: dict[str, Any], viz_config: dict[str, Any], cfg: dict[str, Any]):
    """Process a strain dynamics job."""
    snapdir = job.get("snapshot_dir")
    if not snapdir:
        print("Warning: Need job.snapshot_dir -> skipped")
        return
    
    outdir = _utils.resolve_output_dir(None, None, job.get("outdir"), cfg)
    outdir.mkdir(parents=True, exist_ok=True)

    # Check if strain plots are enabled
    plot_list = ["strain_series", "strain_vs_defects"]
    enabled_plots = _utils.get_enabled_plots(viz_config, "strain", {"plots": plot_list})
    enabled_plots = [p for p in plot_list if p in enabled_plots]
    
    if not enabled_plots:
        print("No strain plots enabled -> skipped")
        return
    
    # This would need actual implementation - for now just print
    print(f"Would generate strain dynamics plots: {', '.join(enabled_plots)}")
    print(f"Snapshot dir: {snapdir}")
    print(f"Output dir: {outdir}")


def process_healing_dashboard_job(job: dict[str, Any], viz_config: dict[str, Any], cfg: dict[str, Any]):
    """Process a healing dashboard job."""
    # Check if dashboards group is enabled
    if not _utils.is_plot_enabled("healing_dashboard", viz_config, job):
        print("Dashboards group disabled -> skipped")
        return
    
    data_file = job.get("input") or job.get("data")
    if not data_file:
        print("Warning: Need job.input or job.data -> skipped")
        return
    
    outdir = _utils.resolve_output_dir(Path(data_file), None, job.get("outdir"), cfg)
    
    # Load data and generate dashboard
    # This is a placeholder - actual implementation would load the data
    print(f"Would generate healing dashboard from: {data_file}")
    print(f"Output dir: {outdir}")


def process_panel_job(job: dict[str, Any], viz_config: dict[str, Any], cfg: dict[str, Any]):
    """Process an individual panel job."""
    # Check if individual_panels group is enabled
    if not _utils.is_plot_enabled("geometry", viz_config, job):  # Check any panel type
        print("Individual panels group disabled -> skipped")
        return
    
    inp = job.get("input")
    if not inp:
        print("Warning: Missing job.input -> skipped")
        return
    
    view = job.get("view", "geometry")
    outdir = _utils.resolve_output_dir(Path(inp), None, job.get("outdir"), cfg)
    
    print(f"Would generate {view} panel from: {inp}")
    print(f"Output dir: {outdir}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--config", default=None, help="Path to publication_plots.toml (optional)")
    args = parser.parse_args()
    
    config_path = Path(args.config) if args.config else None
    # _utils.print_progress_header("TOML Visualization Runner", config_path)
    
    with _utils.Timer() as timer:
        cfg = _utils.load_publication_config(args.config)
        viz = cfg.get("viz_jobs", {})
        
        if not viz.get("enabled", False):
            print("viz_jobs.enabled is false -> nothing to run")
            return 0
        
        jobs = _utils.get_viz_jobs(cfg)
        if not jobs:
            print("No viz jobs found under [viz_jobs.jobs]")
            return 0
        
        print(f"Found {len(jobs)} visualization jobs")
        
        for job_idx, job in enumerate(_utils.progress(jobs, desc="Processing jobs"), 1):
            kind = str(job.get("kind", "")).strip().lower()
            
            # Determine output directory for info display
            inp_path = None
            if job.get("input"):
                inp_path = Path(job["input"])
            elif job.get("baseline"):
                inp_path = Path(job["baseline"])
            
            outdir = _utils.resolve_output_dir(inp_path, None, job.get("outdir"), cfg)
            _utils.print_job_info(job_idx, len(jobs), job, outdir)
            
            # Process based on kind
            if kind == "state":
                process_state_job(job, viz, cfg)
            elif kind == "compare":
                process_compare_job(job, viz, cfg)
            elif kind == "storyboard":
                # Check if storyboard is enabled
                if _utils.is_plot_enabled("storyboard", viz, job):
                    view = job.get("movie_view")
                    if view is None:
                        view = job.get("view", viz.get("movie_view", "strain"))

                    n_frames = int(_utils.get_parameter("n_frames", viz, job, None, 12))
                    ncols = int(_utils.get_parameter("ncols", viz, job, None, 4))

                    job_cfg = _utils.cfg_with_job_overrides(cfg, job)
                    make_storyboard(
                        job["snapshot_dir"],
                        view=view,
                        n_frames=n_frames,
                        ncols=ncols,
                        outdir=outdir,
                        cfg=job_cfg,
                    )

            elif kind == "movie":
                # Check if movie is enabled
                if _utils.is_plot_enabled("movie", viz, job):
                    view = job.get("movie_view")
                    if view is None:
                        view = job.get("view", viz.get("movie_view", "strain"))

                    fps = int(_utils.get_parameter("fps", viz, job, None, 12))
                    format_type = _utils.get_parameter("format", viz, job, None, "gif")

                    job_cfg = _utils.cfg_with_job_overrides(cfg, job)
                    save_path = Path(outdir) / f"movie_{Path(str(job['snapshot_dir'])).name}_{view}.{str(format_type).lower()}"

                    make_movie(
                        job["snapshot_dir"],
                        view=view,
                        fps=fps,
                        save_path=save_path,
                        outdir=outdir,
                        cfg=job_cfg,
                    )

            elif kind == "spatial":
                # Check if spatial plot is enabled
                if _utils.is_plot_enabled("defect_density_by_distance", viz, job):
                    state = load_tiling_state(job["input"])
                    bin_edges = job.get("bin_edges", [0, 2, 4, 6, 8, 10])
                    defect_threshold = float(job.get("defect_threshold", viz.get("defect_threshold", 1.5)))
                    treat_immobile_as_fixed = bool(job.get("treat_immobile_as_fixed", 
                                                         viz.get("treat_immobile_as_fixed", False)))
                    snap = compute_spatial_bin_stats(
                        state,
                        bin_edges=bin_edges,
                        defect_threshold=defect_threshold,
                        treat_immobile_as_fixed=treat_immobile_as_fixed,
                    )
                    plot_defect_density_by_distance(snap, outdir=outdir, cfg=cfg)
            elif kind == "strain_dynamics":
                process_strain_dynamics_job(job, viz, cfg)
            elif kind == "healing_dashboard":
                process_healing_dashboard_job(job, viz, cfg)
            elif kind == "panel":
                process_panel_job(job, viz, cfg)
            else:
                print(f"Warning: Unknown job kind: {kind}")
    
    print(f"\nCompleted in {timer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())