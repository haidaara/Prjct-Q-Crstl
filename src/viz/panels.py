from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
from matplotlib.collections import PatchCollection
from matplotlib.colors import PowerNorm

from .io import iter_tiles, extract_vertices, bounds_from_vertices


@dataclass
class TilePatchCache:
    patches: List[Polygon]
    ids: List[int]
    xlims: Tuple[float, float]
    ylims: Tuple[float, float]


def build_patch_cache(state: Dict[str, Any]) -> TilePatchCache:
    polys, ids = extract_vertices(state)
    patches: List[Polygon] = [Polygon(np.asarray(poly), closed=True) for poly in polys]
    b = bounds_from_vertices(polys)
    if b is None:
        xlims = (-1, 1)
        ylims = (-1, 1)
    else:
        xlims, ylims = b
    return TilePatchCache(patches=patches, ids=ids, xlims=xlims, ylims=ylims)


def get_obstacle_mask(state: Dict[str, Any], *, treat_immobile_as_fixed: bool = False) -> Dict[int, Optional[str]]:
    """Return obs_map[tid] in {"pore","fixed",None}.

    Default is strict:
    - pore := removed == True OR obstacle_type == 'pore'
    - fixed := obstacle_type in {'fixed_defect','fixed'}

    Some old datasets used immobile=True for fixed defects; enable treat_immobile_as_fixed only if needed.
    """
    obs: Dict[int, Optional[str]] = {}
    for tid, t in iter_tiles(state):
        if t.get("removed", False) or t.get("obstacle_type") == "pore":
            obs[tid] = "pore"
            continue
        ot = t.get("obstacle_type")
        if ot in ("fixed_defect", "fixed"):
            obs[tid] = "fixed"
            continue
        if treat_immobile_as_fixed and bool(t.get("immobile", False)):
            obs[tid] = "fixed"
            continue
        obs[tid] = None
    return obs


def get_energy_map(state: Dict[str, Any]) -> Dict[int, float]:
    out: Dict[int, float] = {}
    for tid, t in iter_tiles(state):
        try:
            out[tid] = float(t.get("local_energy", np.nan))
        except Exception:
            out[tid] = np.nan
    return out


def get_class_map(state: Dict[str, Any], *, prefer: str = "energy_class") -> Dict[int, str]:
    out: Dict[int, str] = {}
    for tid, t in iter_tiles(state):
        if prefer == "energy_class" and "energy_class" in t:
            out[tid] = str(t.get("energy_class", "UNKNOWN"))
        elif prefer == "vertex_class" and "vertex_class" in t:
            out[tid] = str(t.get("vertex_class", "UNKNOWN"))
        else:
            out[tid] = str(t.get("vertex_class", t.get("energy_class", "UNKNOWN")))
    return out


def get_growth_map(state: Dict[str, Any]) -> Dict[int, str]:
    out: Dict[int, str] = {}
    for tid, t in iter_tiles(state):
        out[tid] = str(t.get("growth_status", "ungrown"))
    return out


def get_phason_energy_map(state: Dict[str, Any]) -> Dict[int, float]:
    out: Dict[int, float] = {}
    for tid, t in iter_tiles(state):
        try:
            out[tid] = float(t.get("phason_energy", np.nan))
        except Exception:
            out[tid] = np.nan
    return out


def _add_legend(ax, items: List[tuple], loc: str = "upper right", title: str = "Legend", font_size: int = 10):
    handles = [Patch(facecolor=color, edgecolor="white", linewidth=0.5, label=label) for color, label in items]
    ax.legend(handles=handles, loc=loc, fontsize=font_size, title=title, title_fontsize=font_size + 1,
              framealpha=0.9, edgecolor="gray")


def _finalize_ax(ax, cache: TilePatchCache):
    ax.set_aspect("equal")
    ax.set_xlim(cache.xlims)
    ax.set_ylim(cache.ylims)
    ax.axis("off")


def draw_geometry(ax, state: Dict[str, Any], *, cache: Optional[TilePatchCache] = None,
                  treat_immobile_as_fixed: bool = False,
                  line_width: float = 0.5,
                  title: Optional[str] = None,
                  legend: bool = True):
    """Geometry & obstacles (thin/thick, pores, fixed)."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)

    # We need tile types aligned with cache.ids. We'll build a dict once.
    type_map: Dict[int, str] = {}
    for tid, t in iter_tiles(state):
        type_map[tid] = str(t.get("type", "UNKNOWN"))

    colors: List[str] = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        ttype = type_map.get(tid, "UNKNOWN")
        if obs == "pore":
            colors.append("#2c3e50")
        elif obs == "fixed":
            colors.append("#d35400")
        else:
            if ttype == "THIN":
                colors.append("#FFD700")
            else:
                colors.append("#4169E1")

    pc = PatchCollection(cache.patches, match_original=False)
    pc.set_facecolor(colors)
    pc.set_edgecolor("white")
    pc.set_linewidth(line_width)
    ax.add_collection(pc)

    if title:
        ax.set_title(title, fontweight="bold")

    if legend:
        _add_legend(
            ax,
            [("#FFD700", "Thin"), ("#4169E1", "Thick"), ("#2c3e50", "Pore"), ("#d35400", "Fixed")],
            title="Components",
        )

    _finalize_ax(ax, cache)
    return pc


def draw_energy(ax, state: Dict[str, Any], *, cache: Optional[TilePatchCache] = None,
                treat_immobile_as_fixed: bool = False,
                percentile: Tuple[float, float] = (5, 95),
                gamma: float = 1.0,
                line_width: float = 0.5,
                title: Optional[str] = None,
                add_colorbar: bool = True):
    """Local energy map (percentile scaling, excluding obstacles from scale)."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    energy_map = get_energy_map(state)

    values: List[float] = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        if obs in ("pore", "fixed"):
            values.append(np.nan)
        else:
            values.append(energy_map.get(tid, np.nan))

    valid = np.asarray([v for v in values if not np.isnan(v)])

    if valid.size == 0:
        pc = PatchCollection(cache.patches, facecolor="#EEEEEE", edgecolor="white", linewidth=line_width)
        ax.add_collection(pc)
        ax.text(0.5, 0.5, "NO ENERGY DATA", ha="center", va="center", transform=ax.transAxes, color="red")
        _finalize_ax(ax, cache)
        if title:
            ax.set_title(title, fontweight="bold")
        return pc

    vmin, vmax = np.percentile(valid, [percentile[0], percentile[1]])

    norm = None
    if gamma is not None and float(gamma) != 1.0:
        norm = PowerNorm(gamma=float(gamma), vmin=float(vmin), vmax=float(vmax))

    pc = PatchCollection(
        cache.patches,
        cmap="Spectral_r",
        edgecolor="white",
        linewidth=line_width,
        norm=norm,
    )
    pc.set_array(np.asarray(values, dtype=float))
    if norm is None:
        pc.set_clim(vmin=vmin, vmax=vmax)
    ax.add_collection(pc)

    if add_colorbar:
        cbar = plt.colorbar(pc, ax=ax, fraction=0.046, pad=0.04)
        label = f"Local Energy (p{percentile[0]:.0f}={vmin:.2f}, p{percentile[1]:.0f}={vmax:.2f})"
        if gamma is not None and float(gamma) != 1.0:
            label += f"  γ={float(gamma):.2f}"
        cbar.set_label(label)

    if title:
        ax.set_title(title, fontweight="bold")

    _finalize_ax(ax, cache)
    return pc


def draw_defects(ax, state: Dict[str, Any], *, cache: Optional[TilePatchCache] = None,
                 defect_threshold: float = 1.5,
                 treat_immobile_as_fixed: bool = False,
                 line_width: float = 0.5,
                 title: Optional[str] = None,
                 legend: bool = True):
    """Defect map: classify tiles as defect if local_energy >= defect_threshold."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    energy_map = get_energy_map(state)

    colors: List[str] = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        if obs == "pore":
            colors.append("#2c3e50")
            continue
        if obs == "fixed":
            colors.append("#d35400")
            continue

        e = energy_map.get(tid, np.nan)
        if np.isnan(e):
            colors.append("lightgray")
        elif e >= defect_threshold:
            colors.append("#DC143C")
        else:
            colors.append("#2E8B57")

    pc = PatchCollection(cache.patches, facecolor=colors, edgecolor="white", linewidth=line_width)
    ax.add_collection(pc)

    if title:
        ax.set_title(title, fontweight="bold")

    if legend:
        _add_legend(
            ax,
            [("#2E8B57", "Healthy"), ("#DC143C", f"Defect (E≥{defect_threshold})"), ("#2c3e50", "Pore"), ("#d35400", "Fixed")],
            title="Defects",
        )

    _finalize_ax(ax, cache)
    return pc


def draw_class(ax, state: Dict[str, Any], *, cache: Optional[TilePatchCache] = None,
               prefer: str = "energy_class",
               treat_immobile_as_fixed: bool = False,
               line_width: float = 0.5,
               title: Optional[str] = None,
               legend: bool = True):
    """Vertex/energy classification map."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    class_map = get_class_map(state, prefer=prefer)

    colors: List[str] = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        if obs == "pore":
            colors.append("#2c3e50")
        elif obs == "fixed":
            colors.append("#d35400")
        else:
            cls = class_map.get(tid, "UNKNOWN")
            if cls == "LOW_ENERGY":
                colors.append("#2E8B57")
            elif cls == "MEDIUM_ENERGY":
                colors.append("#F4A460")
            elif cls == "HIGH_ENERGY":
                colors.append("#DC143C")
            else:
                colors.append("lightgray")

    pc = PatchCollection(cache.patches, facecolor=colors, edgecolor="white", linewidth=line_width)
    ax.add_collection(pc)

    if title:
        ax.set_title(title, fontweight="bold")

    if legend:
        _add_legend(
            ax,
            [("#2E8B57", "Low"), ("#F4A460", "Medium"), ("#DC143C", "High"), ("#2c3e50", "Pore"), ("#d35400", "Fixed")],
            title="Class",
        )

    _finalize_ax(ax, cache)
    return pc


def draw_growth(ax, state: Dict[str, Any], *, cache: Optional[TilePatchCache] = None,
                treat_immobile_as_fixed: bool = False,
                line_width: float = 0.5,
                title: Optional[str] = None,
                legend: bool = True):
    """Growth front map from growth_status."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    growth_map = get_growth_map(state)

    colors: List[str] = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        if obs == "pore":
            colors.append("#2c3e50")
        elif obs == "fixed":
            colors.append("#d35400")
        else:
            st = growth_map.get(tid, "ungrown")
            if st == "seed":
                colors.append("#2ecc71")
            elif st == "grown":
                colors.append("#3498db")
            elif st == "frontier":
                colors.append("#f1c40f")
            else:
                colors.append("#ecf0f1")

    pc = PatchCollection(cache.patches, facecolor=colors, edgecolor="white", linewidth=line_width)
    ax.add_collection(pc)

    if title:
        ax.set_title(title, fontweight="bold")

    if legend:
        _add_legend(ax, [("#2ecc71", "Seed"), ("#3498db", "Grown"), ("#f1c40f", "Frontier"), ("#ecf0f1", "Ungrown")],
                    title="Growth")

    _finalize_ax(ax, cache)
    return pc


def draw_strain(ax, state: Dict[str, Any], *, cache: Optional[TilePatchCache] = None,
                treat_immobile_as_fixed: bool = False,
                percentile: Tuple[float, float] = (5, 95),
                line_width: float = 0.5,
                title: Optional[str] = None,
                add_colorbar: bool = True):
    """Phason strain energy density map (uses per-tile 'phason_energy')."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    strain_map = get_phason_energy_map(state)

    values: List[float] = []
    for tid in cache.ids:
        obs = obs_map.get(tid)
        if obs in ("pore", "fixed"):
            values.append(np.nan)
        else:
            values.append(strain_map.get(tid, np.nan))

    valid = np.asarray([v for v in values if not np.isnan(v)])

    if valid.size == 0:
        pc = PatchCollection(cache.patches, facecolor="#EEEEEE", edgecolor="white", linewidth=line_width)
        ax.add_collection(pc)
        ax.text(0.5, 0.5, "NO STRAIN DATA\n(missing 'phason_energy')", ha="center", va="center",
                transform=ax.transAxes, color="red")
        if title:
            ax.set_title(title, fontweight="bold")
        _finalize_ax(ax, cache)
        return pc

    vmin, vmax = np.percentile(valid, [percentile[0], percentile[1]])

    pc = PatchCollection(cache.patches, cmap="magma", edgecolor="white", linewidth=line_width)
    pc.set_array(np.asarray(values, dtype=float))
    pc.set_clim(vmin=vmin, vmax=vmax)
    ax.add_collection(pc)

    if add_colorbar:
        cbar = plt.colorbar(pc, ax=ax, fraction=0.046, pad=0.04)
        cbar.set_label(f"Phason strain energy (p{percentile[0]:.0f}={vmin:.2e}, p{percentile[1]:.0f}={vmax:.2e})")

    if title:
        ax.set_title(title, fontweight="bold")

    _finalize_ax(ax, cache)
    return pc
