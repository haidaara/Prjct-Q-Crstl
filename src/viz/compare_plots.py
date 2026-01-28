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
    Shared-scale (publishable): energy/strain use one common vmin/vmax across panels.
    """
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})

    view = view.lower().strip()
    # aliases (keep CLI/TOML flexible)
    if view in ("energy_local", "local_energy"):
        view = "energy"
    if view in ("phason", "phason_energy", "phason_strain"):
        view = "strain"

    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    pos_thresh = float(viz.get("compare_position_threshold", 0.01))

    defect_threshold = float(viz.get("defect_threshold", 1.5))
    ep = viz.get("energy_percentile", [5, 95])
    sp = viz.get("strain_percentile", [5, 95])

    from .panels import (
        draw_geometry, draw_energy, draw_defects, draw_class, draw_growth, draw_strain,
        get_obstacle_mask, get_energy_map, get_phason_energy_map,
    )

    def _safe_percentiles(p, default=(5.0, 95.0)):
        try:
            lo = float(p[0]); hi = float(p[1])
        except Exception:
            lo, hi = default
        lo = max(0.0, min(100.0, lo))
        hi = max(0.0, min(100.0, hi))
        if hi < lo:
            lo, hi = hi, lo
        if hi == lo:
            hi = min(100.0, lo + 1.0)
        return lo, hi

    with mpl_style(cfg):
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        states = [state_a, state_b, state_c]
        caches = [build_patch_cache(st) for st in states]

        shared_vmin = None
        shared_vmax = None

        if view == "energy":
            p_lo, p_hi = _safe_percentiles(ep, default=(5.0, 95.0))
            vals = []
            for st in states:
                obs = get_obstacle_mask(st, treat_immobile_as_fixed=treat_immobile_as_fixed)
                emap = get_energy_map(st)
                for tid, v in emap.items():
                    if obs.get(tid) in ("pore", "fixed"):
                        continue
                    try:
                        fv = float(v)
                    except Exception:
                        continue
                    if np.isfinite(fv):
                        vals.append(fv)
            if vals:
                arr = np.asarray(vals, dtype=float)
                lo, hi = np.percentile(arr, [p_lo, p_hi])
                if np.isfinite(lo) and np.isfinite(hi) and hi > lo:
                    shared_vmin, shared_vmax = float(lo), float(hi)

        elif view == "strain":
            p_lo, p_hi = _safe_percentiles(sp, default=(5.0, 95.0))
            vals = []
            for st in states:
                obs = get_obstacle_mask(st, treat_immobile_as_fixed=treat_immobile_as_fixed)
                smap = get_phason_energy_map(st)
                for tid, v in smap.items():
                    if obs.get(tid) in ("pore", "fixed"):
                        continue
                    try:
                        fv = float(v)
                    except Exception:
                        continue
                    if np.isfinite(fv):
                        vals.append(fv)
            if vals:
                arr = np.asarray(vals, dtype=float)
                lo, hi = np.percentile(arr, [p_lo, p_hi])
                if np.isfinite(lo) and np.isfinite(hi) and hi > lo:
                    shared_vmin, shared_vmax = float(lo), float(hi)

        pc_last = None

        for ax, st, ttl, cache in zip(axes, states, titles, caches):
            if view == "geometry":
                draw_geometry(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "energy":
                pc_last = draw_energy(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    percentile=(ep[0], ep[1]),
                    gamma=float(viz.get("energy_gamma", 1.0)),
                    vmin=shared_vmin, vmax=shared_vmax,
                    line_width=0.4, title=ttl, add_colorbar=False,
                )
            elif view == "defects":
                draw_defects(
                    ax, st, cache=cache, defect_threshold=defect_threshold,
                    treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "class":
                draw_class(
                    ax, st, cache=cache, prefer="energy_class",
                    treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "growth":
                draw_growth(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "strain":
                pc_last = draw_strain(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    percentile=(sp[0], sp[1]),
                    vmin=shared_vmin, vmax=shared_vmax,
                    line_width=0.4, title=ttl, add_colorbar=False,
                )
            elif view == "change":
                if st is state_a:
                    _draw_change_map(
                        ax, state_a, state_a, title=f"{ttl} (ref)", cfg=cfg,
                        position_threshold=pos_thresh, treat_immobile_as_fixed=treat_immobile_as_fixed
                    )
                else:
                    _draw_change_map(
                        ax, state_a, st, title=ttl, cfg=cfg,
                        position_threshold=pos_thresh, treat_immobile_as_fixed=treat_immobile_as_fixed
                    )
            else:
                ax.text(0.5, 0.5, f"Unknown view: {view}", ha="center", va="center")
                ax.axis("off")

        # Shared axis bounds across panels
        x0 = min(c.xlims[0] for c in caches)
        x1 = max(c.xlims[1] for c in caches)
        y0 = min(c.ylims[0] for c in caches)
        y1 = max(c.ylims[1] for c in caches)
        for ax in axes:
            ax.set_xlim((x0, x1))
            ax.set_ylim((y0, y1))
            ax.set_aspect("equal")

        # One shared colorbar (energy/strain)
        if view in ("energy", "strain") and pc_last is not None:
            cbar = fig.colorbar(pc_last, ax=axes, fraction=0.046, pad=0.04)
            lo, hi = pc_last.get_clim()
            if view == "energy":
                cbar.set_label(f"Local Energy (shared scale: {lo:.3g}..{hi:.3g})")
            else:
                cbar.set_label(f"Phason strain energy (shared scale: {lo:.3g}..{hi:.3g})")

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
    Shared-scale (publishable): energy/strain use one common vmin/vmax across panels.
    """
    cfg = cfg or load_publication_config(config_path)
    viz = cfg.get("viz_jobs", {})

    view = view.lower().strip()
    # aliases (keep CLI/TOML flexible)
    if view in ("energy_local", "local_energy"):
        view = "energy"
    if view in ("phason", "phason_energy", "phason_strain"):
        view = "strain"

    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    pos_thresh = float(viz.get("compare_position_threshold", 0.01))

    defect_threshold = float(viz.get("defect_threshold", 1.5))
    ep = viz.get("energy_percentile", [5, 95])
    sp = viz.get("strain_percentile", [5, 95])

    from .panels import (
        draw_geometry, draw_energy, draw_defects, draw_class, draw_growth, draw_strain,
        get_obstacle_mask, get_energy_map, get_phason_energy_map,
    )

    def _safe_percentiles(p, default=(5.0, 95.0)):
        try:
            lo = float(p[0]); hi = float(p[1])
        except Exception:
            lo, hi = default
        lo = max(0.0, min(100.0, lo))
        hi = max(0.0, min(100.0, hi))
        if hi < lo:
            lo, hi = hi, lo
        if hi == lo:
            hi = min(100.0, lo + 1.0)
        return lo, hi

    with mpl_style(cfg):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        states = [baseline_state, current_state]
        caches = [build_patch_cache(st) for st in states]

        # Shared vmin/vmax for publishable comparisons (energy/strain)
        shared_vmin = None
        shared_vmax = None

        if view == "energy":
            p_lo, p_hi = _safe_percentiles(ep, default=(5.0, 95.0))
            vals = []
            for st in states:
                obs = get_obstacle_mask(st, treat_immobile_as_fixed=treat_immobile_as_fixed)
                emap = get_energy_map(st)
                for tid, v in emap.items():
                    if obs.get(tid) in ("pore", "fixed"):
                        continue
                    try:
                        fv = float(v)
                    except Exception:
                        continue
                    if np.isfinite(fv):
                        vals.append(fv)
            if vals:
                arr = np.asarray(vals, dtype=float)
                lo, hi = np.percentile(arr, [p_lo, p_hi])
                if np.isfinite(lo) and np.isfinite(hi) and hi > lo:
                    shared_vmin, shared_vmax = float(lo), float(hi)

        elif view == "strain":
            p_lo, p_hi = _safe_percentiles(sp, default=(5.0, 95.0))
            vals = []
            for st in states:
                obs = get_obstacle_mask(st, treat_immobile_as_fixed=treat_immobile_as_fixed)
                smap = get_phason_energy_map(st)
                for tid, v in smap.items():
                    if obs.get(tid) in ("pore", "fixed"):
                        continue
                    try:
                        fv = float(v)
                    except Exception:
                        continue
                    if np.isfinite(fv):
                        vals.append(fv)
            if vals:
                arr = np.asarray(vals, dtype=float)
                lo, hi = np.percentile(arr, [p_lo, p_hi])
                if np.isfinite(lo) and np.isfinite(hi) and hi > lo:
                    shared_vmin, shared_vmax = float(lo), float(hi)

        pc_last = None

        for ax, st, ttl, cache in zip(axes, states, titles, caches):
            if view == "geometry":
                draw_geometry(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "energy":
                pc_last = draw_energy(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    percentile=(ep[0], ep[1]),
                    gamma=float(viz.get("energy_gamma", 1.0)),
                    vmin=shared_vmin, vmax=shared_vmax,
                    line_width=0.4, title=ttl, add_colorbar=False,
                )
            elif view == "defects":
                draw_defects(
                    ax, st, cache=cache, defect_threshold=defect_threshold,
                    treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "class":
                draw_class(
                    ax, st, cache=cache, prefer="energy_class",
                    treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "growth":
                draw_growth(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    line_width=0.4, title=ttl, legend=False
                )
            elif view == "strain":
                pc_last = draw_strain(
                    ax, st, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    percentile=(sp[0], sp[1]),
                    vmin=shared_vmin, vmax=shared_vmax,
                    line_width=0.4, title=ttl, add_colorbar=False,
                )
            elif view == "change":
                if st is baseline_state:
                    _draw_change_map(
                        ax, baseline_state, baseline_state, title=f"{ttl} (ref)", cfg=cfg,
                        position_threshold=pos_thresh, treat_immobile_as_fixed=treat_immobile_as_fixed
                    )
                else:
                    _draw_change_map(
                        ax, baseline_state, st, title=ttl, cfg=cfg,
                        position_threshold=pos_thresh, treat_immobile_as_fixed=treat_immobile_as_fixed
                    )
            else:
                ax.text(0.5, 0.5, f"Unknown view: {view}", ha="center", va="center")
                ax.axis("off")

        # Shared axis bounds across panels
        x0 = min(c.xlims[0] for c in caches)
        x1 = max(c.xlims[1] for c in caches)
        y0 = min(c.ylims[0] for c in caches)
        y1 = max(c.ylims[1] for c in caches)
        for ax in axes:
            ax.set_xlim((x0, x1))
            ax.set_ylim((y0, y1))
            ax.set_aspect("equal")

        # One shared colorbar (energy/strain)
        if view in ("energy", "strain") and pc_last is not None:
            cbar = fig.colorbar(pc_last, ax=axes, fraction=0.046, pad=0.04)
            lo, hi = pc_last.get_clim()
            if view == "energy":
                cbar.set_label(f"Local Energy (shared scale: {lo:.3g}..{hi:.3g})")
            else:
                cbar.set_label(f"Phason strain energy (shared scale: {lo:.3g}..{hi:.3g})")

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
    viz = cfg.get("viz_jobs", {})
    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(10, 8))
        _draw_change_map(
            ax, baseline_state, current_state,
            title="Changed tiles", cfg=cfg,
            position_threshold=position_threshold,
            treat_immobile_as_fixed=treat_immobile_as_fixed,
        )

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
    treat_immobile_as_fixed: bool = False,
):
    cache = build_patch_cache(current_state)

    changed = changed_tile_ids(baseline_state, current_state, position_threshold=position_threshold)
    obs_map = get_obstacle_mask(current_state, treat_immobile_as_fixed=treat_immobile_as_fixed)

    colors = []
    for tid in cache.ids:
        if obs_map.get(tid) in ("pore", "fixed"):
            colors.append((0.85, 0.85, 0.85, 1.0))  # obstacles: light gray
        elif tid in changed:
            colors.append((0.85, 0.10, 0.10, 1.0))  # changed: red
        else:
            colors.append((0.20, 0.70, 0.25, 1.0))  # unchanged: green

    pc = PatchCollection(cache.patches, facecolor=colors, edgecolor="white", linewidth=0.3)
    ax.add_collection(pc)

    total = len([tid for tid in cache.ids if obs_map.get(tid) is None])
    n_changed = len([tid for tid in cache.ids if (obs_map.get(tid) is None and tid in changed)])
    frac = (100.0 * n_changed / total) if total else 0.0

    ax.text(
        0.02, 0.98, f"Changed: {n_changed}/{total} ({frac:.1f}%)",
        transform=ax.transAxes, va="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.9),
    )

    if title:
        ax.set_title(title, fontweight="bold")

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
    treat_immobile_as_fixed: bool = False,
) -> float:
    """Percent of *active* tiles that changed (position/type/class) relative to baseline."""
    changed = changed_tile_ids(baseline_state, current_state, position_threshold=position_threshold)
    obs_map = get_obstacle_mask(current_state, treat_immobile_as_fixed=treat_immobile_as_fixed)
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
    viz = cfg.get("viz_jobs", {})
    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))

    labels = []
    vals = []
    for label, st in labeled_states:
        labels.append(label)
        vals.append(
            compute_phason_drift_percent(
                baseline_state, st,
                position_threshold=position_threshold,
                treat_immobile_as_fixed=treat_immobile_as_fixed,
            )
        )

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 5))
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
