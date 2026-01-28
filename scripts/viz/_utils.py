#!/usr/bin/env python3
"""Common utilities for visualization scripts."""

from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import Any, List, Optional, Set, Dict

# Add project root to Python path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.viz.config import load_publication_config, get_viz_jobs
from src.viz.io import load_tiling_state, short_path
from src.viz.progress import progress
from src.viz.style import default_output_dir


# Valid plot types for each script
VALID_STATE_PLOTS = {
    "matrix_2x2", "grid_3x3", "diffraction", "vertex_dist", 
    "radial_defects", "strain_map", "strain_hist", "strain_vs_distance"
}

VALID_COMPARE_PLOTS = {
    "pair", "triptych", "change_panel", "phason_drift_series"
}

VALID_SPATIAL_PLOTS = {
    "defect_density_by_distance"
}

VALID_STRAIN_PLOTS = {
    "strain_series", "strain_vs_defects", "storyboard"
}

VALID_MOVIE_PLOTS = {
    "movie"
}


def csv_to_list(s: Optional[str]) -> List[str]:
    """Parse comma-separated string to list of strings."""
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def csv_to_floats(s: Optional[str]) -> List[float]:
    """Parse comma-separated string to list of floats."""
    if not s:
        return []
    try:
        return [float(x.strip()) for x in s.split(",") if x.strip()]
    except ValueError:
        return []


def resolve_output_dir(
    input_path: Optional[Path] = None,
    cli_outdir: Optional[Path] = None,
    job_outdir: Optional[str] = None,
    cfg: Optional[dict[str, Any]] = None
) -> Path:
    """Determine output directory with precedence: CLI > Job > input_parent/viz > Config default."""
    if cli_outdir:
        return Path(cli_outdir)
    
    if job_outdir:
        return Path(job_outdir)
    
    if input_path:
        return input_path.parent / "viz"
    
    if cfg:
        return default_output_dir(cfg)
    
    return Path("viz_output")


def get_enabled_plots(
    viz_config: Dict[str, Any],
    plot_category: str,
    job_config: Optional[Dict[str, Any]] = None,
    cli_plots: Optional[str] = None
) -> Set[str]:
    """Get enabled plots for a specific category with precedence: CLI > Job > Global."""
    
    # Determine which valid plots to use
    if plot_category == "state":
        valid_plots = VALID_STATE_PLOTS
    elif plot_category == "compare":
        valid_plots = VALID_COMPARE_PLOTS
    elif plot_category == "spatial":
        valid_plots = VALID_SPATIAL_PLOTS
    elif plot_category == "strain":
        valid_plots = VALID_STRAIN_PLOTS
    elif plot_category == "movie":
        valid_plots = VALID_MOVIE_PLOTS
    else:
        valid_plots = set()
    
    # 1. CLI override (highest priority)
    if cli_plots:
        requested = set(csv_to_list(cli_plots))
        valid = requested & valid_plots
        invalid = requested - valid_plots
        
        if invalid:
            print(f"Note: Skipping invalid plot types for {plot_category}: {', '.join(sorted(invalid))}")
        
        return valid
    
    # 2. Job-specific plots
    if job_config and "plots" in job_config:
        job_plots = job_config["plots"]
        if isinstance(job_plots, list):
            requested = set(job_plots)
            return requested & valid_plots
        elif isinstance(job_plots, dict):
            requested = {plot for plot, enabled in job_plots.items() if enabled}
            return requested & valid_plots
    
    # 3. Global plots_enabled dictionary
    plots_enabled = viz_config.get("plots_enabled", {})
    if isinstance(plots_enabled, dict):
        enabled_plots = {plot for plot, enabled in plots_enabled.items() 
                        if enabled and plot in valid_plots}
        return enabled_plots
    
    # 4. Default fallback for category
    if plot_category == "state":
        return {"matrix_2x2"}
    elif plot_category == "compare":
        return {"pair", "change_panel"}
    elif plot_category == "spatial":
        return {"defect_density_by_distance"}
    else:
        return set()


def get_parameter(
    param_name: str,
    viz_config: Dict[str, Any],
    job_config: Optional[Dict[str, Any]] = None,
    cli_value: Any = None,
    default_value: Any = None
) -> Any:
    """Get a parameter with precedence: CLI > Job > Global config > Default."""
    
    if cli_value is not None:
        return cli_value
    
    if job_config and param_name in job_config:
        return job_config[param_name]
    
    if param_name in viz_config:
        return viz_config[param_name]
    
    return default_value


class Timer:
    """Simple context manager for timing code execution."""
    
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
    
    def __str__(self) -> str:
        return f"{self.elapsed:.1f}s"


def print_job_info(job_idx: int, total_jobs: int, job: Dict[str, Any], outdir: Path):
    """Print standardized job information."""
    print(f"\n{'='*60}")
    print(f"Job {job_idx}/{total_jobs}")
    print(f"Kind: {job.get('kind', 'unknown')}")
    
    if job.get('input'):
        print(f"Input: {short_path(Path(job['input']))}")
    if job.get('snapshot_dir'):
        print(f"Snapshot dir: {short_path(Path(job['snapshot_dir']))}")
    if job.get('baseline'):
        print(f"Baseline: {short_path(Path(job['baseline']))}")
    if job.get('damaged'):
        print(f"Damaged: {short_path(Path(job['damaged']))}")
    if job.get('healed'):
        print(f"Healed: {short_path(Path(job['healed']))}")
    
    print(f"Output: {short_path(outdir)}")
    print(f"{'='*60}")


def is_plot_enabled(plot_name: str, viz_config: Dict[str, Any], job_config: Optional[Dict[str, Any]] = None) -> bool:
    """Return True if a plot is enabled (supports both plot lists/dicts and global plots_enabled flags)."""

    # If plot belongs to a known category, defer to get_enabled_plots
    if plot_name in VALID_STATE_PLOTS:
        return plot_name in get_enabled_plots(viz_config, "state", job_config)
    if plot_name in VALID_COMPARE_PLOTS:
        return plot_name in get_enabled_plots(viz_config, "compare", job_config)
    if plot_name in VALID_SPATIAL_PLOTS:
        return plot_name in get_enabled_plots(viz_config, "spatial", job_config)
    if plot_name in VALID_STRAIN_PLOTS:
        return plot_name in get_enabled_plots(viz_config, "strain", job_config)
    if plot_name in VALID_MOVIE_PLOTS:
        return plot_name in get_enabled_plots(viz_config, "movie", job_config)

    # Otherwise: allow explicit toggles in job.plots
    plots = (job_config or {}).get("plots")
    if isinstance(plots, dict):
        if plot_name in plots:
            return bool(plots[plot_name])
    elif isinstance(plots, (list, tuple, set)):
        if plot_name in plots:
            return True

    # Finally: global plots_enabled flag
    return bool(viz_config.get("plots_enabled", {}).get(plot_name, False))
