from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
import matplotlib.pyplot as plt

from .config import load_publication_config
from .io import extract_tile_positions, iter_tiles, short_path
from .panels import (
    build_patch_cache,
    draw_geometry,
    draw_energy,
    draw_defects,
    draw_class,
    draw_growth,
    draw_strain,
    get_obstacle_mask,
    get_energy_map,
    get_phason_energy_map,
    draw_named_panel,
)
from .style import mpl_style, save_figure, resolve_output_path
from .progress import progress




def _state_stats(state: Dict[str, Any], *, defect_threshold: float, treat_immobile_as_fixed: bool) -> Dict[str, Any]:
    cache = build_patch_cache(state)
    obs = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    emap = get_energy_map(state)
    smap = get_phason_energy_map(state)

    n_total = len(cache.ids)
    n_pore = sum(1 for tid in cache.ids if obs.get(tid) == 'pore')
    n_fixed = sum(1 for tid in cache.ids if obs.get(tid) == 'fixed')

    energies = [emap.get(tid, np.nan) for tid in cache.ids if obs.get(tid) is None]
    energies = np.asarray([e for e in energies if not np.isnan(e)], dtype=float)
    e_mean = float(np.mean(energies)) if energies.size else float('nan')

    defects = [tid for tid in cache.ids if obs.get(tid) is None and not np.isnan(emap.get(tid, np.nan)) and emap.get(tid, 0.0) >= defect_threshold]
    n_def = len(defects)

    strains = [smap.get(tid, np.nan) for tid in cache.ids if obs.get(tid) is None]
    strains = np.asarray([s for s in strains if not np.isnan(s)], dtype=float)
    s_mean = float(np.mean(strains)) if strains.size else float('nan')

    class_counts: Dict[str, int] = {}
    for _, t in iter_tiles(state):
        if t.get('removed', False):
            continue
        cls = str(t.get('energy_class', 'UNKNOWN'))
        class_counts[cls] = class_counts.get(cls, 0) + 1

    growth_counts: Dict[str, int] = {}
    for _, t in iter_tiles(state):
        if t.get('removed', False):
            continue
        g = str(t.get('growth_status', 'UNKNOWN'))
        growth_counts[g] = growth_counts.get(g, 0) + 1

    return {
        'n_total': n_total,
        'n_pore': n_pore,
        'n_fixed': n_fixed,
        'e_mean': e_mean,
        'n_defects': n_def,
        's_mean': s_mean,
        'class_counts': class_counts,
        'growth_counts': growth_counts,
    }

PathLike = Union[str, Path]


def draw_matrix_2x2(
    axes,
    state: Dict[str, Any],
    *,
    panels: Sequence[str],
    cfg: Dict[str, Any],
    cache=None,
    defect_threshold: float = 1.5,
    treat_immobile_as_fixed: bool = False,
    line_width: float = 0.5,
) -> None:
    """Draw a configurable 2x2 panel matrix into the provided 4 axes.

    Supported panel kinds (same philosophy as grid_3x3):
      geometry, energy, defects, class, strain, growth,
      fft, vertex_dist, energy_hist, energy_cdf, energy_quantiles, strain_hist

    Titles are numbered by position (1..4) to remain publication-friendly.
    """
    if len(panels) != 4:
        raise ValueError("matrix_2x2 panels must be a list of exactly 4 panel names")

    if cache is None:
        cache = build_patch_cache(state)

    viz = cfg.get("viz_jobs", {})

    ep = viz.get("energy_percentile", [5, 99.8])
    sp = viz.get("strain_percentile", [5, 95])
    energy_percentile = (float(ep[0]), float(ep[1]))
    strain_percentile = (float(sp[0]), float(sp[1]))

    energy_gamma = float(viz.get("energy_gamma", 4.0))

    energy_vmin = viz.get("energy_vmin", None)
    energy_vmax = viz.get("energy_vmax", None)
    energy_vmin = float(energy_vmin) if energy_vmin is not None else None
    energy_vmax = float(energy_vmax) if energy_vmax is not None else None

    strain_vmin = viz.get("strain_vmin", None)
    strain_vmax = viz.get("strain_vmax", None)
    strain_vmin = float(strain_vmin) if strain_vmin is not None else None
    strain_vmax = float(strain_vmax) if strain_vmax is not None else None

    stats = _state_stats(
        state,
        defect_threshold=defect_threshold,
        treat_immobile_as_fixed=treat_immobile_as_fixed,
    )

    def _class_title(prefix: str) -> str:
        cc = stats.get("class_counts", {}) or {}
        low = cc.get("LOW_ENERGY", cc.get("low", 0))
        med = cc.get("MEDIUM_ENERGY", cc.get("medium", 0))
        high = cc.get("HIGH_ENERGY", cc.get("high", 0))
        return f"{prefix}Energy Class (L={low}, M={med}, H={high})"

    def _growth_title(prefix: str) -> str:
        gc = stats.get("growth_counts", {}) or {}
        return (
            f"{prefix}Growth "
            f"(seed={gc.get('seed',0)}, frontier={gc.get('frontier',0)}, "
            f"grown={gc.get('grown',0)}, ungrown={gc.get('ungrown',0)})"
        )

    for i, kind in enumerate(panels):
        ax = axes[i]
        k = str(kind).lower().strip()
        prefix = f"{i+1}. "

        if k == "geometry":
            draw_geometry(
                ax,
                state,
                cache=cache,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=line_width,
                title=f"{prefix}Geometry & Obstacles (pores={stats['n_pore']}, fixed={stats['n_fixed']})",
                legend=True,
            )

        elif k == "energy":
            draw_energy(
                ax,
                state,
                cache=cache,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=line_width,
                percentile=energy_percentile,
                gamma=energy_gamma,
                title=f"{prefix}Local Energy",
                add_colorbar=True,
                vmin=energy_vmin,
                vmax=energy_vmax,
            )

        elif k == "class":
            draw_class(
                ax,
                state,
                cache=cache,
                prefer="energy_class",
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=line_width,
                title=_class_title(prefix),
                legend=True,
            )

        elif k == "growth":
            draw_growth(
                ax,
                state,
                cache=cache,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=line_width,
                title=_growth_title(prefix),
                legend=True,
            )

        elif k == "strain":
            draw_strain(
                ax,
                state,
                cache=cache,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=line_width,
                percentile=strain_percentile,
                title=f"{prefix}Phason Strain Energy",
                add_colorbar=True,
                vmin=strain_vmin,
                vmax=strain_vmax,
            )

        elif k == "defects":
            draw_defects(
                ax,
                state,
                cache=cache,
                defect_threshold=defect_threshold,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=line_width,
                title=f"{prefix}Defects (E≥{defect_threshold})",
                legend=False,
            )

        elif k == "fft":
            _draw_fft_panel(ax, state, add_colorbar=False)
            ax.set_title(f"{prefix}Diffraction (FFT)")

        elif k == "vertex_dist":
            _draw_vertex_dist_panel(ax, state)
            ax.set_title(f"{prefix}Vertex Distribution")

        elif k == "energy_hist":
            _draw_energy_hist_panel(ax, state)
            ax.set_title(f"{prefix}Energy Histogram")

        elif k == "energy_cdf":
            _draw_energy_cdf_panel(ax, state)
            ax.set_title(f"{prefix}Energy CDF")

        elif k == "energy_quantiles":
            _draw_energy_quantiles_panel(ax, state)
            ax.set_title(f"{prefix}Energy Quantiles")

        elif k == "strain_hist":
            _draw_strain_hist_panel(ax, state)
            ax.set_title(f"{prefix}Strain Histogram")

        else:
            ax.text(0.5, 0.5, f"Unknown panel\n'{kind}'", ha="center", va="center", transform=ax.transAxes)
            ax.axis("off")


def plot_physics_matrix(
    state: Dict[str, Any],
    *,
    panels: Optional[Sequence[str]] = None,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: Optional[str] = None,
    defect_threshold: Optional[float] = None,
    log: bool = True,
) -> plt.Figure:


    """2x2 publication matrix.

    Panels:
    1) Geometry + obstacles
    2) Local energy map
    3) Energy class map
    4) Growth status map
    """
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})

    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    defect_threshold = float(defect_threshold if defect_threshold is not None else viz.get("defect_threshold", 1.5))

    ep = viz.get("energy_percentile", [5, 99.8])
    sp = viz.get("strain_percentile", [5, 95])
    energy_percentile = (float(ep[0]), float(ep[1]))
    strain_percentile = (float(sp[0]), float(sp[1]))

    energy_gamma = float(viz.get("energy_gamma", 4.0))

    energy_vmin = viz.get("energy_vmin", None)
    energy_vmax = viz.get("energy_vmax", None)
    energy_vmin = float(energy_vmin) if energy_vmin is not None else None
    energy_vmax = float(energy_vmax) if energy_vmax is not None else None

    strain_vmin = viz.get("strain_vmin", None)
    strain_vmax = viz.get("strain_vmax", None)
    strain_vmin = float(strain_vmin) if strain_vmin is not None else None
    strain_vmax = float(strain_vmax) if strain_vmax is not None else None

    fs = viz.get("matrix_figsize", None)
    figsize = tuple(fs if fs is not None else cfg.get("figure", {}).get("matrix_figsize", [18, 18]))
    lw = float(cfg.get("lines", {}).get("line_width", 0.5))

    cache = build_patch_cache(state)
    stats = _state_stats(state, defect_threshold=defect_threshold, treat_immobile_as_fixed=treat_immobile_as_fixed)

    default_panels = ["geometry", "energy", "class", "growth"]
    if panels is None:
        panels = viz.get("matrix_2x2_panels", default_panels)
    panels = [str(p).strip() for p in panels]
    if len(panels) != 4:
        raise ValueError(f"matrix_2x2_panels must have exactly 4 entries, got {len(panels)}")

    with mpl_style(cfg):
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        axes = axes.ravel()

        for ax, kind in zip(axes, panels):
            k = str(kind).lower().strip()

            panel_kwargs: Dict[str, Any] = dict(
                cache=cache,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=lw,
                title=None,
            )

            if k in {"geometry", "geom"}:
                panel_kwargs.update(
                    legend=True,
                    title=f"1. Geometry & Obstacles (N={stats['n_total']}, pores={stats['n_pore']}, fixed={stats['n_fixed']})",
                )

            elif k in {"energy", "energy_local", "local_energy"}:
                panel_kwargs.update(
                    add_colorbar=True,
                    percentile=energy_percentile,
                    gamma=energy_gamma,
                    vmin=energy_vmin,
                    vmax=energy_vmax,
                    title="Local Energy",
                )

            elif k in {"class", "energy_class"}:
                panel_kwargs.update(
                    prefer="energy_class",
                    legend=True,
                    title=_format_class_title(stats),
                )

            elif k in {"growth"}:
                panel_kwargs.update(
                    legend=True,
                    title=(
                        f"4. Growth (seed={stats['growth_counts'].get('seed',0)}, frontier={stats['growth_counts'].get('frontier',0)}, "
                        f"grown={stats['growth_counts'].get('grown',0)}, ungrown={stats['growth_counts'].get('ungrown',0)})"
                    ),
                )

            elif k in {"strain", "phason", "phason_energy"}:
                panel_kwargs.update(
                    add_colorbar=True,
                    percentile=strain_percentile,
                    vmin=strain_vmin,
                    vmax=strain_vmax,
                    title="Phason strain energy",
                )

            elif k in {"defects", "defect"}:
                panel_kwargs.update(
                    defect_threshold=defect_threshold,
                    title="Defects",
                )

            try:
                draw_named_panel(ax, state, k, **panel_kwargs)
            except Exception as e:
                ax.text(0.5, 0.5, f"Panel '{k}' failed:\n{e}", ha="center", va="center", transform=ax.transAxes)
                ax.axis("off")

        if title:
            fig.suptitle(title, fontweight="bold")

        if save_path is not None:
            p = Path(save_path)
        else:
            p = resolve_output_path(cfg, outdir=outdir, filename="matrix_2x2")

        if save_path is not None or outdir is not None:
            saved = save_figure(fig, p, cfg)
            if log:
                print(f"Saved 2x2 matrix: {short_path(saved)}")

    return fig



# Backward-compatible alias used in some scripts
plot_publication_matrix_2x2 = plot_physics_matrix




def _format_class_title(stats: Dict[str, Any]) -> str:
    cc = stats.get('class_counts', {}) or {}
    low = cc.get('LOW_ENERGY', cc.get('low', 0))
    med = cc.get('MEDIUM_ENERGY', cc.get('medium', 0))
    high = cc.get('HIGH_ENERGY', cc.get('high', 0))
    return f"3. Energy Class (L={low}, M={med}, H={high})"

def plot_publication_grid_3x3(
    state: Dict[str, Any],
    *,
    panels: Optional[Sequence[str]] = None,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: Optional[str] = None,
    defect_threshold: Optional[float] = None,
) -> plt.Figure:
    """3x3 grid for publication.

    Default panel list (9):
      geometry, energy, defects,
      class, strain, growth,
      fft, vertex_dist, energy_hist

    You can override by providing a list of 9 panel names.
    """
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})

    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    defect_threshold = float(defect_threshold if defect_threshold is not None else viz.get("defect_threshold", 1.5))

    ep = viz.get("energy_percentile", [5, 99.8])
    sp = viz.get("strain_percentile", [5, 95])
    energy_percentile = (float(ep[0]), float(ep[1]))
    strain_percentile = (float(sp[0]), float(sp[1]))

    energy_gamma = float(viz.get("energy_gamma", 4.0))
    energy_vmin = viz.get("energy_vmin", None)
    energy_vmax = viz.get("energy_vmax", None)
    energy_vmin = float(energy_vmin) if energy_vmin is not None else None
    energy_vmax = float(energy_vmax) if energy_vmax is not None else None

    if panels is None:
        panels = viz.get(
            "grid_3x3_panels",
            [
                "geometry", "energy", "defects",
                "class", "strain", "growth",
                "fft", "energy_cdf", "energy_quantiles",
            ],
        )


    if len(panels) != 9:
        raise ValueError("panels must be a list of exactly 9 panel names")

    lw = float(cfg.get("lines", {}).get("line_width", 0.4))
    cache = build_patch_cache(state)

    figsize = tuple(cfg.get("figure", {}).get("grid_figsize", [22, 14]))

    with mpl_style(cfg):
        fig, axes = plt.subplots(3, 3, figsize=figsize)
        axes = axes.ravel()

        for i, kind in enumerate(progress(panels, desc="grid_3x3")):
            ax = axes[i]
            k = str(kind).lower().strip()

            strain_vmin = viz.get("strain_vmin", None)
            strain_vmax = viz.get("strain_vmax", None)
            strain_vmin = float(strain_vmin) if strain_vmin is not None else None
            strain_vmax = float(strain_vmax) if strain_vmax is not None else None

            panel_kwargs: Dict[str, Any] = dict(
                cache=cache,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
                line_width=lw,
                legend=False,
                add_colorbar=False,
                title=None,
            )

            if k in {"energy", "energy_local", "local_energy"}:
                panel_kwargs.update(
                    percentile=energy_percentile,
                    gamma=energy_gamma,
                    vmin=energy_vmin,
                    vmax=energy_vmax,
                    title="Local Energy",
                )

            elif k in {"strain", "phason", "phason_energy"}:
                panel_kwargs.update(
                    percentile=strain_percentile,
                    vmin=strain_vmin,
                    vmax=strain_vmax,
                    title="Phason Strain Energy",
                )

            elif k in {"defects", "defect"}:
                panel_kwargs.update(
                    defect_threshold=defect_threshold,
                    title=f"Defects (E≥{defect_threshold})",
                )

            elif k in {"class", "energy_class"}:
                panel_kwargs.update(
                    prefer="energy_class",
                    title="Energy Class",
                )

            elif k in {"growth"}:
                panel_kwargs.update(title="Growth")

            elif k in {"geometry", "geom"}:
                panel_kwargs.update(title="Geometry")

            try:
                draw_named_panel(ax, state, k, **panel_kwargs)
            except Exception as e:
                ax.text(0.5, 0.5, f"Unknown panel\n'{k}'\n\n{e}", ha="center", va="center")
                ax.axis("off")

        if title:
            fig.suptitle(title, fontweight="bold")

        if save_path is not None:
            p = Path(save_path)
        else:
            p = resolve_output_path(cfg, outdir=outdir, filename="grid_3x3")

        if save_path is not None or outdir is not None:
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved 3x3 grid: {short_path(saved)}")

    return fig


def plot_diffraction_pattern(state: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                             config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                             outdir: Optional[PathLike] = None) -> plt.Figure:
    """Diffraction/structure-factor style FFT panel as a single figure."""
    cfg = cfg or load_publication_config(config_path)

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        draw_named_panel(ax, state, "fft", add_colorbar=True)

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="fft")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved FFT: {short_path(saved)}")

    return fig


def plot_vertex_distribution(state: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                             config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                             outdir: Optional[PathLike] = None) -> plt.Figure:
    """Bar chart of vertex_class distribution."""
    cfg = cfg or load_publication_config(config_path)

    counts: Dict[str, int] = {}
    for _, t in iter_tiles(state):
        if t.get("removed", False):
            continue
        cls = str(t.get("vertex_class", "UNKNOWN"))
        counts[cls] = counts.get(cls, 0) + 1

    items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if not items:
            ax.text(0.5, 0.5, "No vertex_class data", ha="center", va="center")
            ax.axis("off")
        else:
            labels = [k for k, _ in items]
            values = [v for _, v in items]
            x = np.arange(len(labels))
            ax.bar(x, values)
            ax.set_xticks(x)
            ax.set_xticklabels(labels, rotation=45, ha="right")
            ax.set_ylabel("Count")
            ax.set_title("Vertex Class Distribution")
            ax.grid(True, alpha=0.25, axis="y")
            ax.text(0.02, 0.98, f"Total: {sum(values)}", transform=ax.transAxes, va="top",
                    bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="vertex_distribution")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved vertex distribution: {short_path(saved)}")

    return fig


def plot_radial_defect_density(
    state: Dict[str, Any],
    *,
    center: Optional[Tuple[float, float]] = None,
    defect_threshold: float = 1.5,
    nbins: int = 25,
    max_radius: Optional[float] = None,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """Defect density vs radius (useful for obstacle influence studies)."""
    cfg = cfg or load_publication_config(config_path)

    pts = []
    defects = []
    obs_map = get_obstacle_mask(state)
    energy = get_energy_map(state)

    for tid, t in iter_tiles(state):
        if t.get("removed", False) or obs_map.get(tid) in ("pore", "fixed"):
            continue
        c = t.get("center")
        if not isinstance(c, (list, tuple)) or len(c) < 2:
            continue
        pts.append((float(c[0]), float(c[1])))
        e = energy.get(tid, np.nan)
        defects.append((not np.isnan(e)) and (e >= defect_threshold))

    if not pts:
        pts_arr = np.zeros((0, 2))
    else:
        pts_arr = np.asarray(pts)

    if center is None:
        center = (0.0, 0.0)

    r = np.sqrt((pts_arr[:, 0] - center[0]) ** 2 + (pts_arr[:, 1] - center[1]) ** 2) if len(pts_arr) else np.asarray([])
    if max_radius is None and r.size:
        max_radius = float(np.max(r))

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if r.size == 0 or max_radius is None:
            ax.text(0.5, 0.5, "No positions", ha="center", va="center")
            ax.axis("off")
        else:
            bins = np.linspace(0, max_radius, nbins + 1)
            idx = np.minimum(np.digitize(r, bins) - 1, nbins - 1)

            # counts per annulus
            total_counts = np.bincount(idx, minlength=nbins)
            defect_counts = np.bincount(idx, weights=np.asarray(defects, dtype=float), minlength=nbins)

            # area per annulus
            r0 = bins[:-1]
            r1 = bins[1:]
            area = np.pi * (r1**2 - r0**2)

            density = np.where(total_counts > 0, defect_counts / area, 0.0)
            rc = 0.5 * (r0 + r1)

            ax.plot(rc, density, marker="o")
            ax.set_xlabel("Radius")
            ax.set_ylabel("Defect density (count / area)")
            ax.set_title(f"Radial Defect Density (E≥{defect_threshold})")
            ax.grid(True, alpha=0.3)

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="radial_defect_density")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved radial defect density: {short_path(saved)}")

    return fig


# ----- internal helper panels for grids -----

def _draw_fft_panel(ax, state: Dict[str, Any], *, add_colorbar: bool = False):
    positions = extract_tile_positions(state)
    if not positions:
        ax.text(0.5, 0.5, "No tile positions", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return

    # Diffraction: huge DC peak at k=0 hides everything.
    # Fix: grid density -> subtract mean -> FFT -> log scale -> percentile clip.
    pts = np.asarray(positions, dtype=float)
    pts = pts - np.mean(pts, axis=0, keepdims=True)

    N = 512
    xmin, ymin = np.min(pts, axis=0)
    xmax, ymax = np.max(pts, axis=0)
    Lx = max(1e-12, float(xmax - xmin))
    Ly = max(1e-12, float(ymax - ymin))

    ix = np.clip(((pts[:, 0] - xmin) / Lx * (N - 1)).astype(int), 0, N - 1)
    iy = np.clip(((pts[:, 1] - ymin) / Ly * (N - 1)).astype(int), 0, N - 1)

    grid = np.zeros((N, N), dtype=float)
    np.add.at(grid, (iy, ix), 1.0)
    grid = grid - grid.mean()

    wx = np.hanning(N)
    wy = np.hanning(N)
    grid *= wy[:, None] * wx[None, :]

    F = np.fft.fftshift(np.fft.fft2(grid))
    I = np.abs(F) ** 2
    I[N // 2, N // 2] = 0.0
    logI = np.log1p(I)

    dx = Lx / (N - 1)
    dy = Ly / (N - 1)
    kx = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(N, d=dx))
    ky = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(N, d=dy))

    show_k = 8.0
    mx = np.where(np.abs(kx) <= show_k)[0]
    my = np.where(np.abs(ky) <= show_k)[0]

    crop = logI[my.min(): my.max() + 1, mx.min(): mx.max() + 1]
    crop_kx = kx[mx]
    crop_ky = ky[my]
    extent = [crop_kx.min(), crop_kx.max(), crop_ky.min(), crop_ky.max()]

    pos = crop[crop > 0]
    vmax = float(np.percentile(pos, 99.7)) if pos.size else float(np.max(crop))

    im = ax.imshow(crop, extent=extent, origin="lower", aspect="equal", vmin=0.0, vmax=vmax)
    ax.set_title("Diffraction (FFT, log scale)")
    ax.set_xlabel(r"$k_x$")
    ax.set_ylabel(r"$k_y$")

    if add_colorbar:
        plt.colorbar(im, ax=ax, label=r"$\log(1+I)$")




def _draw_energy_cdf_panel(ax, state: Dict[str, Any]):
    obs_map = get_obstacle_mask(state)
    emap = get_energy_map(state)
    vals = [v for tid, v in emap.items() if not np.isnan(v) and obs_map.get(tid) is None]
    if not vals:
        ax.text(0.5, 0.5, "No energy", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return
    x = np.sort(np.asarray(vals, dtype=float))
    y = np.linspace(0.0, 1.0, x.size)
    ax.plot(x, y)
    ax.set_title("Energy CDF")
    ax.set_xlabel("Local energy")
    ax.set_ylabel("CDF")
    ax.grid(True, alpha=0.25)


def _draw_energy_quantiles_panel(ax, state: Dict[str, Any]):
    obs_map = get_obstacle_mask(state)
    emap = get_energy_map(state)
    vals = [v for tid, v in emap.items() if not np.isnan(v) and obs_map.get(tid) is None]
    if not vals:
        ax.text(0.5, 0.5, "No energy", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return
    vals = np.asarray(vals, dtype=float)
    qs = np.array([0.5, 0.75, 0.9, 0.95, 0.99])
    qv = np.quantile(vals, qs)
    ax.plot(qs, qv, marker='o')
    ax.set_title("Energy quantiles")
    ax.set_xlabel("Quantile")
    ax.set_ylabel("Energy")
    ax.set_xticks(qs)
    ax.grid(True, alpha=0.25)

def _draw_vertex_dist_panel(ax, state: Dict[str, Any]):
    counts: Dict[str, int] = {}
    for _, t in iter_tiles(state):
        if t.get("removed", False):
            continue
        cls = str(t.get("vertex_class", "UNKNOWN"))
        counts[cls] = counts.get(cls, 0) + 1
    if not counts:
        ax.text(0.5, 0.5, "No vertex_class", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return

    items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    labels = [k for k, _ in items]
    values = [v for _, v in items]
    x = np.arange(len(labels))
    ax.bar(x, values)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_title("Vertex classes")
    ax.grid(True, alpha=0.25, axis="y")


def _draw_energy_hist_panel(ax, state: Dict[str, Any]):
    obs_map = get_obstacle_mask(state)
    emap = get_energy_map(state)
    vals = [v for tid, v in emap.items() if not np.isnan(v) and obs_map.get(tid) is None]
    if not vals:
        ax.text(0.5, 0.5, "No energy", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return
    ax.hist(vals, bins=50, density=True)
    ax.set_title("Energy histogram")
    ax.set_xlabel("Local energy")
    ax.set_ylabel("Density")
    ax.grid(True, alpha=0.25)


def _draw_strain_hist_panel(ax, state: Dict[str, Any]):
    obs_map = get_obstacle_mask(state)
    smap = get_phason_energy_map(state)
    vals = [v for tid, v in smap.items() if not np.isnan(v) and obs_map.get(tid) is None]
    if not vals:
        ax.text(0.5, 0.5, "No phason_energy", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return
    ax.hist(vals, bins=50, density=True)
    ax.set_title("Phason strain energy hist")
    ax.set_xlabel("Phason strain energy")
    ax.set_ylabel("Density")
    ax.grid(True, alpha=0.25)
