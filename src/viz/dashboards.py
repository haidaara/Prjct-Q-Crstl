"""Dashboards: multi-panel summary figures.

These functions expect *already-aggregated* data dictionaries (typically saved by
experiment scripts). They avoid heavy coupling to the simulation code.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union

import numpy as np
import matplotlib.pyplot as plt

from .config import load_publication_config
from .style import mpl_style, save_figure, resolve_output_path
from .io import short_path

PathLike = Union[str, Path]


def _stage_backgrounds(stage_transitions: Sequence[Dict[str, Any]], steps: Sequence[float]):
    """Convert stage transitions into axvspan specs."""
    if not stage_transitions or not steps:
        return []

    colors = {
        "baseline": "#8ecae6",
        "damage": "#ffb703",
        "healing": "#90be6d",
        "anneal": "#90be6d",
    }

    steps_arr = np.asarray(steps)
    xmin = float(np.min(steps_arr))
    xmax = float(np.max(steps_arr))

    bgs = []
    for tr in stage_transitions:
        s0 = tr.get("start_step")
        s1 = tr.get("end_step")
        if s0 is None or s1 is None:
            continue
        try:
            s0 = float(s0)
            s1 = float(s1)
        except Exception:
            continue
        name = str(tr.get("stage", "stage")).lower()
        c = colors.get(name, "#dddddd")
        bgs.append({"xmin": max(s0, xmin), "xmax": min(s1, xmax), "color": c, "alpha": 0.12})
    return bgs


def plot_healing_dashboard(
    data: Dict[str, Any],
    aggregates: Optional[Dict[str, Any]] = None,
    *,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """4-panel dashboard for healing runs.

    Expected keys in `data` (best-effort):
    - steps
    - energy_total
    - defect_count
    - acceptance_rate
    - stage_transitions (optional)
    """
    cfg = cfg or load_publication_config(config_path)

    steps = data.get("steps", [])
    energy = data.get("energy_total")
    defects = data.get("defect_count")
    acc = data.get("acceptance_rate")

    with mpl_style(cfg):
        fig, axes = plt.subplots(2, 2, figsize=(18, 12))
        axes = axes.ravel()

        # Panel 1: energy
        ax = axes[0]
        if steps and energy:
            ax.plot(steps, energy, linewidth=2)
            ax.set_title("Energy Evolution")
            ax.set_xlabel("Step")
            ax.set_ylabel("Energy")
            ax.grid(True, alpha=0.3)
            if len(energy) > 1:
                dE = float(energy[-1]) - float(energy[0])
                ax.text(0.02, 0.98, f"ΔE={dE:+.3f}", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))
        else:
            ax.text(0.5, 0.5, "Missing energy series", ha="center", va="center")
            ax.axis("off")

        # Panel 2: defects
        ax = axes[1]
        if steps and defects:
            ax.plot(steps, defects, linewidth=2)
            ax.set_title("Defect Timeline")
            ax.set_xlabel("Step")
            ax.set_ylabel("Defects")
            ax.grid(True, alpha=0.3)
            if len(defects) > 1 and float(defects[0]) > 0:
                healing = (float(defects[0]) - float(defects[-1])) / float(defects[0]) * 100.0
                ax.text(0.02, 0.98, f"Healing={healing:.1f}%", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))
        else:
            ax.text(0.5, 0.5, "Missing defect series", ha="center", va="center")
            ax.axis("off")

        # Panel 3: acceptance
        ax = axes[2]
        if steps and acc is not None:
            acc_arr = np.asarray(acc, dtype=float)
            if acc_arr.size and not np.all(np.isnan(acc_arr)):
                ax.plot(steps, acc_arr, linewidth=2)
                ax.set_title("Acceptance Rate")
                ax.set_xlabel("Step")
                ax.set_ylabel("Acceptance")
                ax.grid(True, alpha=0.3)
                ax.text(0.02, 0.98, f"Avg={np.nanmean(acc_arr)*100:.1f}%", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))
            else:
                ax.text(0.5, 0.5, "Acceptance series is NaN", ha="center", va="center")
                ax.axis("off")
        else:
            ax.text(0.5, 0.5, "Missing acceptance series", ha="center", va="center")
            ax.axis("off")

        # Panel 4: efficiency
        ax = axes[3]
        if steps and defects and len(defects) > 1 and float(defects[0]) > 0:
            d0 = float(defects[0])
            eff = [(d0 - float(d)) / d0 for d in defects]
            ax.plot(steps, eff, linewidth=2)
            ax.set_title("Healing Efficiency")
            ax.set_xlabel("Step")
            ax.set_ylabel("Efficiency")
            ax.set_ylim(0, 1.0)
            ax.grid(True, alpha=0.3)
            ax.text(0.02, 0.98, f"Final={eff[-1]*100:.1f}%", transform=ax.transAxes, va="top",
                    bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))
        else:
            ax.text(0.5, 0.5, "Need defects series with nonzero start", ha="center", va="center")
            ax.axis("off")

        # Stage backgrounds
        stage_transitions = data.get("stage_transitions", [])
        bgs = _stage_backgrounds(stage_transitions, steps)
        if bgs:
            for ax in axes:
                if not ax.has_data():
                    continue
                for bg in bgs:
                    ax.axvspan(bg["xmin"], bg["xmax"], alpha=bg["alpha"], color=bg["color"])

        fig.suptitle("Healing Experiment Dashboard", fontweight="bold")

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="healing_dashboard")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved healing dashboard: {short_path(saved)}")

    return fig


def plot_spatial_dashboard(
    spatial_data: List[Dict[str, Any]],
    *,
    save_path: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
    outdir: Optional[PathLike] = None,
) -> plt.Figure:
    """2x3 dashboard for obstacle/bin studies.

    Expected format (best-effort): a list of snapshots, each containing:
      - bin_stats: {bin_name: {tile_count, defect_density, mean_energy, ...}}
      - summary: {total_tiles, total_defects, overall_defect_density, ...}
    """
    cfg = cfg or load_publication_config(config_path)

    with mpl_style(cfg):
        if not spatial_data:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.text(0.5, 0.5, "No spatial data", ha="center", va="center")
            ax.axis("off")
            return fig

        latest = spatial_data[-1]
        bin_stats = latest.get("bin_stats")
        if not isinstance(bin_stats, dict) or not bin_stats:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.text(0.5, 0.5, "No bin_stats in spatial data", ha="center", va="center")
            ax.axis("off")
            return fig

        bins = list(bin_stats.keys())
        x = np.arange(len(bins))

        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.ravel()

        # 1) defect density
        dens = [float(bin_stats[b].get("defect_density", 0.0)) for b in bins]
        axes[0].bar(x, dens)
        axes[0].set_title("Defect density by distance")
        axes[0].set_ylabel("Defect density")
        axes[0].set_xticks(x)
        axes[0].set_xticklabels(bins, rotation=45, ha="right")
        axes[0].grid(True, alpha=0.3, axis="y")

        # 2) tile count
        counts = [float(bin_stats[b].get("tile_count", 0.0)) for b in bins]
        axes[1].bar(x, counts)
        axes[1].set_title("Tile count by distance")
        axes[1].set_ylabel("Tiles")
        axes[1].set_xticks(x)
        axes[1].set_xticklabels(bins, rotation=45, ha="right")
        axes[1].grid(True, alpha=0.3, axis="y")

        # 3) mean energy
        mean_e = [float(bin_stats[b].get("mean_energy", 0.0)) for b in bins]
        axes[2].bar(x, mean_e)
        axes[2].set_title("Mean energy by distance")
        axes[2].set_ylabel("Energy")
        axes[2].set_xticks(x)
        axes[2].set_xticklabels(bins, rotation=45, ha="right")
        axes[2].grid(True, alpha=0.3, axis="y")

        # 4) healing efficiency per bin (if >=2)
        if len(spatial_data) >= 2 and isinstance(spatial_data[0].get("bin_stats"), dict):
            first = spatial_data[0]["bin_stats"]
            heff = []
            for b in bins:
                i0 = float(first.get(b, {}).get("defect_density", 0.0))
                i1 = float(bin_stats.get(b, {}).get("defect_density", 0.0))
                heff.append(((i0 - i1) / i0 * 100.0) if i0 > 0 else 0.0)
            axes[3].bar(x, heff)
            axes[3].set_title("Healing efficiency by distance")
            axes[3].set_ylabel("Healing (%)")
            axes[3].set_ylim(0, 100)
            axes[3].set_xticks(x)
            axes[3].set_xticklabels(bins, rotation=45, ha="right")
            axes[3].grid(True, alpha=0.3, axis="y")
        else:
            axes[3].text(0.5, 0.5, "Need ≥2 snapshots", ha="center", va="center")
            axes[3].axis("off")

        # 5) selected bin evolutions
        if len(spatial_data) >= 2:
            selected = bins[: min(3, len(bins))]
            for b in selected:
                series = []
                for snap in spatial_data:
                    bs = snap.get("bin_stats", {})
                    series.append(float(bs.get(b, {}).get("defect_density", 0.0)))
                axes[4].plot(series, marker="o", label=b)
            axes[4].set_title("Defect density evolution (selected bins)")
            axes[4].set_xlabel("Snapshot index")
            axes[4].set_ylabel("Defect density")
            axes[4].grid(True, alpha=0.3)
            axes[4].legend()
        else:
            axes[4].text(0.5, 0.5, "Need ≥2 snapshots", ha="center", va="center")
            axes[4].axis("off")

        # 6) summary text
        axes[5].axis("off")
        summary = latest.get("summary", {}) if isinstance(latest.get("summary"), dict) else {}
        lines = ["=== Spatial summary ==="]
        for k in ("total_tiles", "total_defects", "overall_defect_density", "mean_energy"):
            if k in summary:
                lines.append(f"{k}: {summary[k]}")
        axes[5].text(0.02, 0.98, "\n".join(lines), transform=axes[5].transAxes, va="top",
                     bbox=dict(boxstyle="round", facecolor="white", alpha=0.9), family="monospace")

        fig.suptitle("Spatial Analysis Dashboard", fontweight="bold")

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="spatial_dashboard")
            saved = save_figure(fig, p, cfg)
            print(f"   📊 Saved spatial dashboard: {short_path(saved)}")

    return fig
