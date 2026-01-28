"""src.viz

Lightweight, script-friendly visualization utilities for the Quasi‑Phason project.

- Works directly from JSON tiling states / snapshots (must contain ``tiles``).
- Figure aesthetics are read from ``configs/publication_plots.toml``.
- Plot *jobs* are optional and can be defined under the ``[viz_jobs]`` section.

This package intentionally avoids heavy orchestration. The recommended workflow is:
1) write a small script in ``scripts/viz/`` that loads a state
2) call 1–3 plotting functions from this package
3) save the figure(s) to your run folder or publication output folder
"""

from .config import load_publication_config

# Panels (low-level)
from .panels import (
    draw_geometry,
    draw_energy,
    draw_defects,
    draw_class,
    draw_growth,
    draw_strain,
)

# Common single-state figures
from .static_plots import (
    plot_physics_matrix,
    plot_publication_matrix_2x2,
    plot_publication_grid_3x3,
    plot_diffraction_pattern,
    plot_vertex_distribution,
    plot_radial_defect_density,
)

# Comparisons / change tracking
from .compare_plots import (
    plot_pair,
    plot_triptych,
    plot_change_panel,
    plot_phason_drift_series,
)

# Dashboards
from .dashboards import (
    plot_healing_dashboard,
    plot_spatial_dashboard,
)

# Strain (phason) plots
from .strain_plots import (
    plot_strain_energy_map,
    plot_strain_series,
    plot_strain_vs_defects,
    plot_strain_histogram,
    plot_strain_vs_distance,
    compute_strain_series_from_snapshots,
    compute_strain_series_from_states,
)

# Dynamics / movies
from .movie import (
    make_storyboard,
    make_movie,
    render_frames,
)

__all__ = [
    "load_publication_config",
    "draw_geometry",
    "draw_energy",
    "draw_defects",
    "draw_class",
    "draw_growth",
    "draw_strain",
    "plot_physics_matrix",
    "plot_publication_matrix_2x2",
    "plot_publication_grid_3x3",
    "plot_diffraction_pattern",
    "plot_vertex_distribution",
    "plot_radial_defect_density",
    "plot_pair",
    "plot_triptych",
    "plot_change_panel",
    "plot_phason_drift_series",
    "plot_healing_dashboard",
    "plot_spatial_dashboard",
    "plot_strain_energy_map",
    "plot_strain_series",
    "plot_strain_vs_defects",
    "plot_strain_histogram",
    "plot_strain_vs_distance",
    "compute_strain_series_from_snapshots",
    "compute_strain_series_from_states",
    "make_storyboard",
    "make_movie",
    "render_frames",
]


from .progress import progress
