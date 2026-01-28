"""Spatial analysis helpers for obstacle studies.

This module provides:
- extracting obstacle positions
- computing radial/bin statistics (defect density vs distance)
- basic plots for those statistics

It is designed to support the next project phase: statistical analysis of growth/healing around obstacles.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np
import matplotlib.pyplot as plt

from .config import load_publication_config
from .io import iter_tiles, short_path
from .panels import get_obstacle_mask
from .style import mpl_style, save_figure, resolve_output_path

PathLike = Union[str, Path]


def _as_float_or_nan(x: Any) -> float:
    """Convert to float; return NaN if missing/invalid.

    Why: spatial plots must not silently treat missing fields as 0.0
    (that produces misleading 'uniform color / clean' plots).
    """
    if x is None:
        return float("nan")
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("nan")


def _nanmean_or_nan(x: np.ndarray) -> float:
    """np.nanmean with a safe all-NaN guard."""
    x = np.asarray(x, dtype=float)
    if x.size == 0 or np.all(np.isnan(x)):
        return float("nan")
    return float(np.nanmean(x))


def extract_obstacle_centers(
    state: Dict[str, Any],
    *,
    treat_immobile_as_fixed: bool = False,
) -> np.ndarray:
    """Return Nx2 array of obstacle centers (fixed defects + pores)."""
    obs = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    pts = []
    for tid, t in iter_tiles(state):
        if obs.get(tid) is None:
            continue
        c = t.get("center")
        if c is None:
            continue
        pts.append([float(c[0]), float(c[1])])
    return np.asarray(pts, dtype=float)


def compute_distance_to_nearest_obstacle(
    state: Dict[str, Any],
    *,
    treat_immobile_as_fixed: bool = False,
) -> np.ndarray:
    """For each tile (iteration order of iter_tiles), compute distance to the nearest obstacle.

    Distance definition:
      - If obstacle_metadata provides centers + radii (positions + radii),
        distance is computed to the *obstacle boundary*: min(||x-c_i|| - R_i).
      - Otherwise (e.g. fixed defects encoded by immobile tiles), we fall back to
        distance to the nearest *obstacle-tile center*.

    Returns an array aligned with iter_tiles(state).
    """
    meta = state.get("obstacle_metadata") or {}
    positions = meta.get("positions")
    radii = meta.get("radii")

    use_boundary = (
        isinstance(positions, list)
        and len(positions) > 0
        and isinstance(radii, list)
        and len(radii) == len(positions)
    )

    if use_boundary:
        centers = np.asarray(positions, dtype=float)
        r = np.asarray(radii, dtype=float)
        dists: List[float] = []
        for _tid, t in iter_tiles(state):
            c = t.get("center")
            if c is None:
                dists.append(np.nan)
                continue
            p = np.array([float(c[0]), float(c[1])], dtype=float)
            diff = centers - p
            d = np.sqrt(np.sum(diff * diff, axis=1)) - r
            dists.append(float(np.min(d)))
        return np.asarray(dists, dtype=float)

    # Fallback: obstacle tiles (removed/fixed/immobile tiles)
    obstacles = extract_obstacle_centers(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    dists: List[float] = []

    if obstacles.size == 0:
        for _tid, _t in iter_tiles(state):
            dists.append(np.nan)
        return np.asarray(dists, dtype=float)

    for _tid, t in iter_tiles(state):
        c = t.get("center")
        if c is None:
            dists.append(np.nan)
            continue
        p = np.array([float(c[0]), float(c[1])], dtype=float)
        diff = obstacles - p
        d = np.sqrt(np.sum(diff * diff, axis=1))
        dists.append(float(np.min(d)))

    return np.asarray(dists, dtype=float)



def compute_spatial_bin_stats(
    state: Dict[str, Any],
    *,
    bin_edges: Sequence[float],
    defect_threshold: float = 1.5,
    treat_immobile_as_fixed: bool = False,
) -> Dict[str, Any]:
    """Compute per-distance-bin statistics around obstacles.

    bin_edges: e.g. [0, 2, 4, 6, 8, 10]

    Returned dict keys:
      - bin_stats: {"[r0,r1)": {...}}
      - summary: {...}
    """
    obs = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    d_to_obs = compute_distance_to_nearest_obstacle(state, treat_immobile_as_fixed=treat_immobile_as_fixed)

    # Extract energies / strain
    energies = []
    strains = []
    active_mask = []

    for tid, t in iter_tiles(state):
        energies.append(_as_float_or_nan(t.get("local_energy")))
        strains.append(_as_float_or_nan(t.get("phason_energy")))
        active_mask.append(obs.get(tid) is None)


    energies = np.asarray(energies, dtype=float)
    strains = np.asarray(strains, dtype=float)
    active_mask = np.asarray(active_mask, dtype=bool)

    # Defects: use local_energy threshold on active tiles
    defects = (energies > float(defect_threshold)) & active_mask

    # Bin stats
    edges = np.asarray(bin_edges, dtype=float)
    if edges.ndim != 1 or edges.size < 2:
        raise ValueError("bin_edges must be a 1D sequence with at least 2 values")

    bin_stats: Dict[str, Any] = {}
    total_tiles = int(np.sum(active_mask))
    total_defects = int(np.sum(defects))

    for i in range(len(edges) - 1):
        r0 = float(edges[i])
        r1 = float(edges[i + 1])
        name = f"[{r0:g},{r1:g})"

        in_bin = (d_to_obs >= r0) & (d_to_obs < r1) & active_mask
        n = int(np.sum(in_bin))
        if n == 0:
            bin_stats[name] = {
                "r0": r0,
                "r1": r1,
                "tile_count": 0,
                "defect_count": 0,
                "defect_density": 0.0,
                "mean_energy": float("nan"),
                "mean_strain_energy": float("nan"),
            }
            continue

        dcount = int(np.sum(defects & in_bin))
        bin_stats[name] = {
            "r0": r0,
            "r1": r1,
            "tile_count": n,
            "defect_count": dcount,
            "defect_density": dcount / n,
            "mean_energy": _nanmean_or_nan(energies[in_bin]),
            "mean_strain_energy": _nanmean_or_nan(strains[in_bin]),

        }

    meta = state.get("obstacle_metadata") or {}
    positions = meta.get("positions")
    radii = meta.get("radii")
    use_boundary = (
        isinstance(positions, list)
        and len(positions) > 0
        and isinstance(radii, list)
        and len(radii) == len(positions)
    )

    missing_local_energy = int(np.sum(np.isnan(energies) & active_mask))
    missing_phason_energy = int(np.sum(np.isnan(strains) & active_mask))

    summary = {
        "total_tiles": total_tiles,
        "total_defects": total_defects,
        "overall_defect_density": (total_defects / total_tiles) if total_tiles else 0.0,
        "mean_energy": _nanmean_or_nan(energies[active_mask]) if total_tiles else float("nan"),
        "mean_strain_energy": _nanmean_or_nan(strains[active_mask]) if total_tiles else float("nan"),

        # Truthful obstacle accounting:
        "num_obstacle_tiles": int(np.sum([v is not None for v in obs.values()])),
        "num_obstacles_metadata": int(len(positions)) if isinstance(positions, list) else 0,

        # Make interpretation explicit:
        "defect_threshold": float(defect_threshold),
        "defect_definition": "local_energy > defect_threshold (active tiles only)",
        "distance_definition": "boundary" if use_boundary else "nearest_obstacle_tile_center",

        # Diagnostics (catch silent bad data):
        "missing_local_energy_active": missing_local_energy,
        "missing_phason_energy_active": missing_phason_energy,
    }


    return {"bin_stats": bin_stats, "summary": summary}


def plot_defect_density_by_distance(
    spatial_snapshot: Dict[str, Any],
    *,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """Bar plot from a single spatial snapshot produced by compute_spatial_bin_stats."""
    cfg = cfg or load_publication_config(config_path)

    bin_stats = spatial_snapshot.get("bin_stats", {})
    if not isinstance(bin_stats, dict) or not bin_stats:
        with mpl_style(cfg):
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.text(0.5, 0.5, "No bin_stats", ha="center", va="center")
            ax.axis("off")
            return fig

    bins = list(bin_stats.keys())
    dens = [float(bin_stats[b].get("defect_density", 0.0)) for b in bins]

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.arange(len(bins))
        ax.bar(x, dens)
        ax.set_xticks(x)
        ax.set_xticklabels(bins, rotation=45, ha="right")
        ax.set_xlabel("Distance bin")
        ax.set_ylabel("Defect density")
        thr = spatial_snapshot.get("summary", {}).get("defect_threshold", None)
        dist_def = spatial_snapshot.get("summary", {}).get("distance_definition", "")
        if thr is None:
            ax.set_title("Defect density vs distance to obstacle")
        else:
            ax.set_title(
                f"Defect density vs distance to obstacle "
                f"(defect: local_energy > {float(thr):g}; distance: {dist_def})"
            )
        ax.grid(True, alpha=0.3, axis="y")

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="defect_density_by_distance")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved defect density by distance: {short_path(saved)}")

    return fig
