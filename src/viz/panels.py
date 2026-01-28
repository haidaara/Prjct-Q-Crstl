from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
from matplotlib.collections import PatchCollection
from matplotlib.colors import PowerNorm

from .io import iter_tiles, extract_vertices, bounds_from_vertices, extract_tile_positions


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


def draw_energy(
    ax,
    state: Dict[str, Any],
    *,
    cache: Optional[TilePatchCache] = None,
    treat_immobile_as_fixed: bool = False,
    percentile: Tuple[float, float] = (5, 95),
    gamma: float = 1.0,
    line_width: float = 0.5,
    title: Optional[str] = None,
    add_colorbar: bool = True,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
):
    """Local energy map (percentile scaling, excluding obstacles from scale)."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    energy_map = get_energy_map(state)

    values: List[float] = []
    for tid in cache.ids:
        if obs_map.get(tid) in ("pore", "fixed"):
            values.append(np.nan)
            continue
        v = energy_map.get(tid, np.nan)
        try:
            fv = float(v)
        except Exception:
            fv = np.nan
        values.append(fv if np.isfinite(fv) else np.nan)

    valid = np.asarray([v for v in values if np.isfinite(v)], dtype=float)

    if valid.size == 0:
        pc = PatchCollection(cache.patches, facecolor="#EEEEEE", edgecolor="white", linewidth=line_width)
        ax.add_collection(pc)
        ax.text(
            0.5, 0.5, "NO ENERGY DATA\n(missing 'energy_local')",
            ha="center", va="center", transform=ax.transAxes, color="red",
        )
        if title:
            ax.set_title(title, fontweight="bold")
        _finalize_ax(ax, cache)
        return pc

    # Percentile-based limits (robust)
    try:
        p_lo = float(percentile[0]); p_hi = float(percentile[1])
    except Exception:
        p_lo, p_hi = 5.0, 95.0
    p_lo = max(0.0, min(100.0, p_lo))
    p_hi = max(0.0, min(100.0, p_hi))
    if p_hi < p_lo:
        p_lo, p_hi = p_hi, p_lo
    if p_hi == p_lo:
        p_hi = min(100.0, p_lo + 1.0)

    pvmin, pvmax = np.percentile(valid, [p_lo, p_hi])
    if (not np.isfinite(pvmin)) or (not np.isfinite(pvmax)) or (pvmax <= pvmin):
        pvmin = float(np.nanmin(valid))
        pvmax = float(np.nanmax(valid))
        if pvmax <= pvmin:
            pvmax = pvmin + 1.0

    use_fixed = (
        vmin is not None and vmax is not None and
        np.isfinite(vmin) and np.isfinite(vmax) and float(vmax) > float(vmin)
    )
    scale_vmin, scale_vmax = (float(vmin), float(vmax)) if use_fixed else (float(pvmin), float(pvmax))

    norm = None
    if gamma is not None and float(gamma) != 1.0:
        norm = PowerNorm(gamma=float(gamma), vmin=scale_vmin, vmax=scale_vmax)

    pc = PatchCollection(
        cache.patches,
        cmap="Spectral_r",
        edgecolor="white",
        linewidth=line_width,
        norm=norm,
    )
    pc.set_array(np.asarray(values, dtype=float))
    if norm is None:
        pc.set_clim(vmin=scale_vmin, vmax=scale_vmax)

    ax.add_collection(pc)

    if add_colorbar:
        cbar = plt.colorbar(pc, ax=ax, fraction=0.046, pad=0.04)
        label = "Local energy"
        if use_fixed:
            label += f" (fixed scale: {scale_vmin:.3g}..{scale_vmax:.3g})"
        else:
            label += (
                f" (p{p_lo:.0f}={pvmin:.3g}, p{p_hi:.0f}={pvmax:.3g}; "
                f"scale={scale_vmin:.3g}..{scale_vmax:.3g})"
            )
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


def draw_strain(
    ax,
    state: Dict[str, Any],
    *,
    cache: Optional[TilePatchCache] = None,
    treat_immobile_as_fixed: bool = False,
    percentile: Tuple[float, float] = (5, 95),
    line_width: float = 0.5,
    title: Optional[str] = None,
    add_colorbar: bool = True,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
):
    """Phason strain energy map (percentile scaling, excluding obstacles from scale)."""
    if cache is None:
        cache = build_patch_cache(state)

    obs_map = get_obstacle_mask(state, treat_immobile_as_fixed=treat_immobile_as_fixed)
    strain_map = get_phason_energy_map(state)

    values: List[float] = []
    for tid in cache.ids:
        if obs_map.get(tid) in ("pore", "fixed"):
            values.append(np.nan)
            continue
        v = strain_map.get(tid, np.nan)
        try:
            fv = float(v)
        except Exception:
            fv = np.nan
        values.append(fv if np.isfinite(fv) else np.nan)

    valid = np.asarray([v for v in values if np.isfinite(v)], dtype=float)

    if valid.size == 0:
        pc = PatchCollection(cache.patches, facecolor="#EEEEEE", edgecolor="white", linewidth=line_width)
        ax.add_collection(pc)
        ax.text(
            0.5, 0.5, "NO STRAIN DATA\n(missing 'phason_energy')",
            ha="center", va="center", transform=ax.transAxes, color="red",
        )
        if title:
            ax.set_title(title, fontweight="bold")
        _finalize_ax(ax, cache)
        return pc

    # Percentile-based limits (robust)
    try:
        p_lo = float(percentile[0]); p_hi = float(percentile[1])
    except Exception:
        p_lo, p_hi = 5.0, 95.0
    p_lo = max(0.0, min(100.0, p_lo))
    p_hi = max(0.0, min(100.0, p_hi))
    if p_hi < p_lo:
        p_lo, p_hi = p_hi, p_lo
    if p_hi == p_lo:
        p_hi = min(100.0, p_lo + 1.0)

    pvmin, pvmax = np.percentile(valid, [p_lo, p_hi])
    if (not np.isfinite(pvmin)) or (not np.isfinite(pvmax)) or (pvmax <= pvmin):
        pvmin = float(np.nanmin(valid))
        pvmax = float(np.nanmax(valid))
        if pvmax <= pvmin:
            pvmax = pvmin + 1.0

    use_fixed = (
        vmin is not None and vmax is not None and
        np.isfinite(vmin) and np.isfinite(vmax) and float(vmax) > float(vmin)
    )
    scale_vmin, scale_vmax = (float(vmin), float(vmax)) if use_fixed else (float(pvmin), float(pvmax))

    pc = PatchCollection(cache.patches, cmap="magma", edgecolor="white", linewidth=line_width)
    pc.set_array(np.asarray(values, dtype=float))
    pc.set_clim(vmin=scale_vmin, vmax=scale_vmax)
    ax.add_collection(pc)

    if add_colorbar:
        cbar = plt.colorbar(pc, ax=ax, fraction=0.046, pad=0.04)
        if use_fixed:
            cbar.set_label(f"Phason strain energy (fixed scale: {scale_vmin:.3g}..{scale_vmax:.3g})")
        else:
            cbar.set_label(
                f"Phason strain energy (p{p_lo:.0f}={pvmin:.3g}, p{p_hi:.0f}={pvmax:.3g}; "
                f"scale={scale_vmin:.3g}..{scale_vmax:.3g})"
            )

    if title:
        ax.set_title(title, fontweight="bold")

    _finalize_ax(ax, cache)
    return pc




# ---------------------------------------------------------------------------
# Extra analytical panels (FFT / histograms) + a small dispatcher.
# ---------------------------------------------------------------------------

def draw_fft_panel(ax, state: dict, *, add_colorbar: bool = False) -> None:
    """Diffraction/structure-factor style FFT panel (log intensity)."""
    positions = extract_tile_positions(state)
    if not positions:
        ax.text(0.5, 0.5, "No tile positions", ha="center", va="center", transform=ax.transAxes)
        ax.axis("off")
        return

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
    I[N // 2, N // 2] = 0.0  # kill DC peak
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


def draw_vertex_dist_panel(ax, state: dict) -> None:
    """Bar chart of vertex_class distribution."""
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


def draw_energy_hist_panel(ax, state: dict) -> None:
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


def draw_strain_hist_panel(ax, state: dict) -> None:
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


def draw_energy_cdf_panel(ax, state: dict) -> None:
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


def draw_energy_quantiles_panel(ax, state: dict) -> None:
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
    ax.plot(qs, qv, marker="o")
    ax.set_title("Energy quantiles")
    ax.set_xlabel("Quantile")
    ax.set_ylabel("Energy")
    ax.set_xticks(qs)
    ax.grid(True, alpha=0.25)


_PANEL_ALIASES = {
    "geom": "geometry",
    "energy_local": "energy",
    "local_energy": "energy",
    "defect": "defects",
    "energy_class": "class",
    "phason": "strain",
    "phason_energy": "strain",
}


def draw_named_panel(
    ax,
    state: Dict[str, Any],
    kind: str,
    *,
    cache: Optional[TilePatchCache] = None,
    title: Optional[str] = None,
    **kwargs,
):
    """Draw a single panel by name.

    Layout code controls: titles, legends, colorbars.
    This router only selects the right panel implementation.
    """
    k = str(kind).lower().strip()
    k = _PANEL_ALIASES.get(k, k)

    treat_immobile_as_fixed = bool(kwargs.get("treat_immobile_as_fixed", False))
    line_width = float(kwargs.get("line_width", 0.4))
    legend = bool(kwargs.get("legend", False))
    add_colorbar = bool(kwargs.get("add_colorbar", False))

    if k == "geometry":
        return draw_geometry(
            ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, title=title, legend=legend
        )

    if k == "energy":
        percentile = kwargs.get("percentile", (5.0, 99.8))
        gamma = float(kwargs.get("gamma", 4.0))
        vmin = kwargs.get("vmin", None)
        vmax = kwargs.get("vmax", None)
        return draw_energy(
            ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, percentile=percentile, gamma=gamma,
            vmin=vmin, vmax=vmax, title=title, add_colorbar=add_colorbar
        )

    if k == "defects":
        defect_threshold = float(kwargs.get("defect_threshold", 1.5))
        return draw_defects(
            ax, state, cache=cache, defect_threshold=defect_threshold,
            treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, title=title, legend=legend
        )

    if k == "class":
        prefer = str(kwargs.get("prefer", "energy_class"))
        return draw_class(
            ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, prefer=prefer, title=title, legend=legend
        )

    if k == "vertex_class":
        return draw_class(
            ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, prefer="vertex_class", title=title, legend=legend
        )

    if k == "growth":
        return draw_growth(
            ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, title=title, legend=legend
        )

    if k == "strain":
        percentile = kwargs.get("percentile", (5.0, 95.0))
        vmin = kwargs.get("vmin", None)
        vmax = kwargs.get("vmax", None)
        return draw_strain(
            ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
            line_width=line_width, percentile=percentile,
            vmin=vmin, vmax=vmax, title=title, add_colorbar=add_colorbar
        )

    if k == "fft":
        return draw_fft_panel(ax, state, add_colorbar=add_colorbar)

    if k in {"vertex_dist", "vertex_distribution"}:
        return draw_vertex_dist_panel(ax, state)

    if k == "energy_hist":
        return draw_energy_hist_panel(ax, state)

    if k == "strain_hist":
        return draw_strain_hist_panel(ax, state)

    if k == "energy_cdf":
        return draw_energy_cdf_panel(ax, state)

    if k == "energy_quantiles":
        return draw_energy_quantiles_panel(ax, state)

    raise ValueError(f"Unknown panel kind: {kind}")
