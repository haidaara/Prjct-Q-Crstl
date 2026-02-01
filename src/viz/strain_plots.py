"""Phason-strain (energy) visualization.

In current snapshots we expect per-tile ``phason_energy`` to be present (this is
already computed by the phason-strain model).

This module treats ``phason_energy`` as a *strain energy density* field suitable for publication:
- maps (spatial distribution)
- time series over snapshots (mean/max/total)
- correlations with defect count (optional)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np
import matplotlib.pyplot as plt

from .config import load_publication_config
from .io import load_tiling_state, list_snapshots, parse_step, short_path
from .panels import build_patch_cache, draw_strain
from .style import mpl_style, save_figure, resolve_output_path

PathLike = Union[str, Path]


def extract_phason_energy(state: Dict[str, Any]) -> np.ndarray:
    vals = []
    for t in state.get("tiles", []):
        vals.append(float(t.get("phason_energy", 0.0) or 0.0))
    return np.asarray(vals, dtype=float)


def compute_strain_series_from_states(states: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute mean/max/total phason_energy for each state."""
    mean_v = []
    max_v = []
    sum_v = []

    for s in states:
        e = extract_phason_energy(s)
        mean_v.append(float(np.mean(e)) if e.size else float("nan"))
        max_v.append(float(np.max(e)) if e.size else float("nan"))
        sum_v.append(float(np.sum(e)) if e.size else float("nan"))

    return {
        "mean": mean_v,
        "max": max_v,
        "sum": sum_v,
    }


def compute_strain_series_from_snapshots(snapshot_paths: Sequence[PathLike]) -> Dict[str, Any]:
    """Load snapshots and compute strain series.

    Returns dict with:
      - steps
      - mean/max/sum
      - paths
    """
    paths = [Path(p) for p in snapshot_paths]

    states = []
    kept_paths = []
    for p in paths:
        try:
            states.append(load_tiling_state(p))
            kept_paths.append(p)
        except ValueError:
            # metrics/summary json -> skip
            continue

    if not states:
        raise ValueError("No state snapshots found (no 'tiles' / 'tiling.tiles').")

    paths = kept_paths

    steps = [parse_step(s, default=i) for i, s in enumerate(states)]

    series = compute_strain_series_from_states(states)
    series.update({"steps": steps, "paths": [str(p) for p in kept_paths]})
    return series


def plot_strain_energy_map(
    state: Dict[str, Any],
    *,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    percentile: Optional[Tuple[float, float]] = None,
) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})
    if percentile is None:
        p = viz.get("strain_percentile", [5, 95])
        percentile = (float(p[0]), float(p[1]))

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 8))
        cache = build_patch_cache(state)
        draw_strain(ax, state, cache=cache, percentile=percentile, title="Phason strain energy")

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="phason_strain_energy_map")
            saved = save_figure(fig, pth, cfg)
            print(f"      Saved strain map: {short_path(saved)}")

    return fig


def plot_strain_series(
    series: Dict[str, Any],
    *,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: str = "Phason strain energy vs step",
) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)

    steps = series.get("steps", [])
    mean_v = series.get("mean", [])
    max_v = series.get("max", [])

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(10, 6))
        if not steps or not mean_v:
            ax.text(0.5, 0.5, "Missing strain series", ha="center", va="center")
            ax.axis("off")
        else:
            ax.plot(steps, mean_v, marker="o", linewidth=2, label="Mean")
            if max_v:
                ax.plot(steps, max_v, linestyle="--", linewidth=1.5, label="Max")
            ax.set_xlabel("Step")
            ax.set_ylabel("Phason strain energy")
            ax.set_title(title)
            ax.grid(True, alpha=0.3)
            ax.legend(loc="best")

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="phason_strain_series")
            saved = save_figure(fig, pth, cfg)
            print(f"      Saved strain series: {short_path(saved)}")

    return fig


def plot_strain_vs_defects(
    strain_series: Dict[str, Any],
    defect_series: Sequence[float],
    *,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: str = "Defects vs phason strain energy",
) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)

    mean_v = np.asarray(strain_series.get("mean", []), dtype=float)
    defects = np.asarray(defect_series, dtype=float)

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        n = min(mean_v.size, defects.size)
        if n == 0:
            ax.text(0.5, 0.5, "Missing data", ha="center", va="center")
            ax.axis("off")
        else:
            ax.scatter(defects[:n], mean_v[:n])
            ax.set_xlabel("Defect count")
            ax.set_ylabel("Mean phason strain energy")
            ax.set_title(title)
            ax.grid(True, alpha=0.3)

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="defects_vs_strain")
            saved = save_figure(fig, pth, cfg)
            print(f"      Saved defects-vs-strain: {short_path(saved)}")

    return fig


def plot_strain_histogram(
    state: Dict[str, Any],
    *,
    bins: int = 40,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: str = "Distribution of phason strain energy",
) -> plt.Figure:
    """Histogram of per-tile phason_energy (active tiles only when obstacles exist)."""
    cfg = cfg or load_publication_config(config_path)

    # Exclude obstacles if obstacle_type exists
    try:
        from .panels import get_obstacle_mask
        from .io import iter_tiles
        obs = get_obstacle_mask(state)
        vals = []
        for tid, t in iter_tiles(state):
            if obs.get(tid) is not None:
                continue
            vals.append(float(t.get("phason_energy", 0.0) or 0.0))
        e = np.asarray(vals, dtype=float)
    except Exception:
        e = extract_phason_energy(state)

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if e.size == 0:
            ax.text(0.5, 0.5, "No phason_energy data", ha="center", va="center")
            ax.axis("off")
        else:
            ax.hist(e, bins=bins)
            ax.set_xlabel("phason_energy")
            ax.set_ylabel("Tile count")
            ax.set_title(title)
            ax.grid(True, alpha=0.25, axis="y")
            ax.text(0.02, 0.98, f"mean={np.mean(e):.4g}\nmax={np.max(e):.4g}",
                    transform=ax.transAxes, va="top",
                    bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="phason_strain_hist")
            saved = save_figure(fig, pth, cfg)
            print(f"      Saved strain histogram: {short_path(saved)}")

    return fig


def plot_strain_vs_distance(
    state: Dict[str, Any],
    *,
    bin_edges: Sequence[float] = (0, 2, 4, 6, 8, 10, 12),
    treat_immobile_as_fixed: bool = False,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: str = "Mean phason strain energy vs distance to obstacle",
) -> plt.Figure:
    """Publication-ready distance profile of phason strain energy around obstacles."""
    cfg = cfg or load_publication_config(config_path)

    from .spatial_plots import compute_distance_to_nearest_obstacle
    from .io import iter_tiles
    from .panels import get_obstacle_mask

    obs = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    d = compute_distance_to_nearest_obstacle(state, treat_immobile_as_fixed=treat_immobile_as_fixed)

    strain = []
    active = []
    for (tid, t), di in zip(iter_tiles(state), d):
        if obs.get(tid) is not None:
            continue
        if np.isnan(di):
            continue
        strain.append(float(t.get("phason_energy", 0.0) or 0.0))
        active.append(float(di))
    strain = np.asarray(strain, dtype=float)
    active = np.asarray(active, dtype=float)

    edges = np.asarray(list(bin_edges), dtype=float)
    means = []
    
    centers = []
    for i in range(len(edges)-1):
        r0, r1 = edges[i], edges[i+1]
        mask = (active >= r0) & (active < r1)
        if np.any(mask):
            means.append(float(np.mean(strain[mask])))
        else:
            means.append(float("nan"))
        centers.append(float(0.5*(r0+r1)))

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(9, 6))
        if strain.size == 0:
            ax.text(0.5, 0.5, "No obstacle distances or strain values", ha="center", va="center")
            ax.axis("off")
        else:
            ax.plot(centers, means, marker="o", linewidth=2)
            ax.set_xlabel("Distance to nearest obstacle")
            ax.set_ylabel("Mean phason strain energy")
            ax.set_title(title)
            ax.grid(True, alpha=0.3)

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="phason_strain_vs_distance")
            saved = save_figure(fig, pth, cfg)
            print(f"      Saved strain vs distance: {short_path(saved)}")

    return fig
