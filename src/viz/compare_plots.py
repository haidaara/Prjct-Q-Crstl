from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Set, Tuple, Union

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

from .config import load_publication_config
from .io import iter_tiles, short_path
from .panels import (
    build_patch_cache,
    get_obstacle_mask,
    get_class_map,
)
from .style import mpl_style, save_figure, resolve_output_path


PathLike = Union[str, Path]


def changed_tile_ids(
    baseline_state: Dict[str, Any],
    current_state: Dict[str, Any],
    *,
    position_threshold: float = 0.01,
) -> Set[int]:
    """Detect changed tiles by id.

    A tile is marked changed if any of these differ:
    - center position (L2 > position_threshold)
    - vertex_class
    - type

    This is intentionally conservative: it flags likely phason flips and related updates.
    """
    base = {}
    for tid, t in iter_tiles(baseline_state):
        base[tid] = {
            "center": tuple((t.get("center") or [0.0, 0.0])[:2]),
            "vertex_class": t.get("vertex_class"),
            "type": t.get("type"),
        }

    cur = {}
    for tid, t in iter_tiles(current_state):
        cur[tid] = {
            "center": tuple((t.get("center") or [0.0, 0.0])[:2]),
            "vertex_class": t.get("vertex_class"),
            "type": t.get("type"),
        }

    changed: Set[int] = set()

    for tid, b in base.items():
        if tid not in cur:
            changed.add(tid)
            continue
        c = cur[tid]
        try:
            dx = float(b["center"][0]) - float(c["center"][0])
            dy = float(b["center"][1]) - float(c["center"][1])
            if (dx * dx + dy * dy) ** 0.5 > position_threshold:
                changed.add(tid)
                continue
        except Exception:
            pass

        if b.get("vertex_class") != c.get("vertex_class") or b.get("type") != c.get("type"):
            changed.add(tid)

    # new tiles
    for tid in cur.keys() - base.keys():
        changed.add(tid)

    return changed


def plot_triptych(
    state_a: Dict[str, Any],
    state_b: Dict[str, Any],
    state_c: Dict[str, Any],
    *,
    view: str = "energy",
    titles: Sequence[str] = ("Baseline", "Damaged", "Healed"),
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """1x3 comparison panel.

    view in {'geometry','energy','defects','class','growth','strain','change'}
    """
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})

    view = view.lower().strip()
    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    defect_threshold = float(viz.get("defect_threshold", 1.5))
    ep = viz.get("energy_percentile", [5, 95])
    sp = viz.get("strain_percentile", [5, 95])

    from .panels import draw_geometry, draw_energy, draw_defects, draw_class, draw_growth, draw_strain

    with mpl_style(cfg):
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        states = [state_a, state_b, state_c]

        for ax, st, ttl in zip(axes, states, titles):
            cache = build_patch_cache(st)
            if view == "geometry":
                draw_geometry(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                              line_width=0.4, title=ttl, legend=False)
            elif view == "energy":
                draw_energy(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                            percentile=(ep[0], ep[1]), line_width=0.4, title=ttl, add_colorbar=False)
            elif view == "defects":
                draw_defects(ax, st, cache=cache, defect_threshold=defect_threshold,
                             treat_immobile_as_fixed=treat_immobile_as_fixed,
                             line_width=0.4, title=ttl, legend=False)
            elif view == "class":
                draw_class(ax, st, cache=cache, prefer="energy_class",
                           treat_immobile_as_fixed=treat_immobile_as_fixed,
                           line_width=0.4, title=ttl, legend=False)
            elif view == "growth":
                draw_growth(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                            line_width=0.4, title=ttl, legend=False)
            elif view == "strain":
                draw_strain(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                            percentile=(sp[0], sp[1]), line_width=0.4, title=ttl, add_colorbar=False)
            elif view == "change":
                # baseline vs current for each panel: A is baseline, B and C compared to baseline
                if st is state_a:
                    _draw_change_map(ax, state_a, state_a, title=f"{ttl} (ref)", cfg=cfg)
                else:
                    _draw_change_map(ax, state_a, st, title=ttl, cfg=cfg)
            else:
                ax.text(0.5, 0.5, f"Unknown view: {view}", ha="center", va="center")
                ax.axis("off")

        fig.suptitle(f"Triptych: {view}", fontweight="bold")

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename=f"triptych_{view}")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved triptych: {short_path(saved)}")

    return fig


def plot_pair(
    baseline_state: Dict[str, Any],
    current_state: Dict[str, Any],
    *,
    view: str = "energy",
    titles: Sequence[str] = ("Baseline", "Current"),
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """1x2 comparison panel (baseline vs current).

    view in {'geometry','energy','defects','class','growth','strain','change'}
    """
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})

    view = view.lower().strip()
    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    defect_threshold = float(viz.get("defect_threshold", 1.5))
    ep = viz.get("energy_percentile", [5, 95])
    sp = viz.get("strain_percentile", [5, 95])

    from .panels import draw_geometry, draw_energy, draw_defects, draw_class, draw_growth, draw_strain

    with mpl_style(cfg):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        states = [baseline_state, current_state]

        for ax, st, ttl in zip(axes, states, titles):
            cache = build_patch_cache(st)
            if view == "geometry":
                draw_geometry(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                              line_width=0.4, title=ttl, legend=False)
            elif view == "energy":
                draw_energy(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                            percentile=(ep[0], ep[1]), line_width=0.4, title=ttl, add_colorbar=False)
            elif view == "defects":
                draw_defects(ax, st, cache=cache, defect_threshold=defect_threshold,
                             treat_immobile_as_fixed=treat_immobile_as_fixed,
                             line_width=0.4, title=ttl, legend=False)
            elif view == "class":
                draw_class(ax, st, cache=cache, prefer="energy_class",
                           treat_immobile_as_fixed=treat_immobile_as_fixed,
                           line_width=0.4, title=ttl, legend=False)
            elif view == "growth":
                draw_growth(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                            line_width=0.4, title=ttl, legend=False)
            elif view == "strain":
                draw_strain(ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                            percentile=(sp[0], sp[1]), line_width=0.4, title=ttl, add_colorbar=False)
            elif view == "change":
                if st is baseline_state:
                    _draw_change_map(ax, baseline_state, baseline_state, title=f"{ttl} (ref)", cfg=cfg)
                else:
                    _draw_change_map(ax, baseline_state, st, title=ttl, cfg=cfg)
            else:
                ax.text(0.5, 0.5, f"Unknown view: {view}", ha="center", va="center")
                ax.axis("off")

        fig.suptitle(f"Pair: {view}", fontweight="bold")

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename=f"pair_{view}")
            saved = save_figure(fig, pth, cfg)
            print(f"   📊 Saved pair: {short_path(saved)}")

    return fig


def plot_change_panel(
    baseline_state: Dict[str, Any],
    current_state: Dict[str, Any],
    *,
    position_threshold: float = 0.01,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """Single change map: unchanged vs changed tiles."""
    cfg = cfg or load_publication_config(config_path)

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(10, 8))
        _draw_change_map(ax, baseline_state, current_state, title="Changed tiles", cfg=cfg,
                         position_threshold=position_threshold)

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="change_map")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved change map: {short_path(saved)}")

    return fig


def _draw_change_map(
    ax,
    baseline_state: Dict[str, Any],
    current_state: Dict[str, Any],
    *,
    title: Optional[str] = None,
    cfg: Optional[Dict[str, Any]] = None,
    position_threshold: float = 0.01,
):
    cache = build_patch_cache(current_state)

    changed = changed_tile_ids(baseline_state, current_state, position_threshold=position_threshold)
    obs_map = get_obstacle_mask(current_state)

    colors = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        if obs == "pore":
            colors.append("#2c3e50")
        elif obs == "fixed":
            colors.append("#d35400")
        else:
            colors.append("#ff0000" if tid in changed else "#808080")

    pc = PatchCollection(cache.patches, facecolor=colors, edgecolor="white", linewidth=0.4)
    ax.add_collection(pc)

    if title:
        ax.set_title(title, fontweight="bold")

    # summary box
    total = len([tid for tid in cache.ids if obs_map.get(tid) is None])
    n_changed = len([tid for tid in cache.ids if (obs_map.get(tid) is None and tid in changed)])
    frac = (100.0 * n_changed / total) if total else 0.0

    ax.text(0.02, 0.98, f"Changed: {n_changed}/{total} ({frac:.1f}%)", transform=ax.transAxes,
            va="top", bbox=dict(boxstyle="round", facecolor="white", alpha=0.9))

    ax.set_aspect("equal")
    ax.set_xlim(cache.xlims)
    ax.set_ylim(cache.ylims)
    ax.axis("off")

    return pc


def compute_phason_drift_percent(
    baseline_state: Dict[str, Any],
    current_state: Dict[str, Any],
    *,
    position_threshold: float = 0.01,
) -> float:
    """Percent of *active* tiles that changed (position/type/class) relative to baseline."""
    changed = changed_tile_ids(baseline_state, current_state, position_threshold=position_threshold)
    obs_map = get_obstacle_mask(current_state)
    active = [tid for tid, _ in iter_tiles(current_state) if obs_map.get(tid) is None]
    if not active:
        return 0.0
    n_changed = sum(1 for tid in active if tid in changed)
    return 100.0 * n_changed / len(active)


def plot_phason_drift_series(
    baseline_state: Dict[str, Any],
    labeled_states: Sequence[Tuple[str, Dict[str, Any]]],
    *,
    position_threshold: float = 0.01,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
    title: str = "Structural drift (changed tiles vs baseline)",
) -> plt.Figure:
    """Bar plot of drift percentage across labeled states."""
    cfg = cfg or load_publication_config(config_path)

    labels = []
    vals = []
    for name, st in labeled_states:
        labels.append(str(name))
        vals.append(compute_phason_drift_percent(baseline_state, st, position_threshold=position_threshold))

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(10, 6))
        if not labels:
            ax.text(0.5, 0.5, "No states provided", ha="center", va="center")
            ax.axis("off")
        else:
            x = np.arange(len(labels))
            ax.bar(x, vals)
            ax.set_xticks(x)
            ax.set_xticklabels(labels, rotation=45, ha="right")
            ax.set_ylabel("Changed tiles (%)")
            ax.set_title(title)
            ax.grid(True, alpha=0.3, axis="y")
            for xi, v in zip(x, vals):
                ax.text(xi, v, f"{v:.1f}%", ha="center", va="bottom")

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="phason_drift_series")
            saved = save_figure(fig, pth, cfg)
            print(f"   📊 Saved drift series: {short_path(saved)}")

    return fig
