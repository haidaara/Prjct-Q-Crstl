"""Healing-run metric plots.

These plots operate on a *run metrics dictionary* saved by experiment scripts.
They do not depend on the tiling geometry.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Union

import numpy as np
import matplotlib.pyplot as plt

from .config import load_publication_config
from .style import mpl_style, save_figure, resolve_output_path
from .io import short_path

PathLike = Union[str, Path]


def _add_stage_backgrounds(ax, stage_transitions: Sequence[Dict[str, Any]], steps: Sequence[float]):
    if not stage_transitions or not steps:
        return
    steps_arr = np.asarray(steps, dtype=float)
    xmin = float(np.min(steps_arr))
    xmax = float(np.max(steps_arr))

    colors = {
        "baseline": "#8ecae6",
        "damage": "#ffb703",
        "healing": "#90be6d",
        "anneal": "#90be6d",
    }

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
        ax.axvspan(max(s0, xmin), min(s1, xmax), alpha=0.12, color=colors.get(name, "#dddddd"))


def plot_energy_evolution(data: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                          config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                          outdir: Optional[PathLike] = None) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)

    steps = data.get("steps", [])
    energy = data.get("energy_total", [])

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if not steps or not energy:
            ax.text(0.5, 0.5, "No energy data", ha="center", va="center", transform=ax.transAxes)
            ax.axis("off")
        else:
            ax.plot(steps, energy, linewidth=2)
            _add_stage_backgrounds(ax, data.get("stage_transitions", []), steps)
            ax.set_xlabel("Simulation step")
            ax.set_ylabel("Total energy")
            ax.set_title("Energy evolution")
            ax.grid(True, alpha=0.3)
            if len(energy) > 1:
                dE = float(energy[-1]) - float(energy[0])
                pct = (dE / abs(float(energy[0]))) * 100 if float(energy[0]) != 0 else 0.0
                ax.text(0.02, 0.98, f"ΔE={dE:+.3f} ({pct:+.1f}%)", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="energy_evolution")
            saved = save_figure(fig, p, cfg)
            print(f"      Saved energy evolution: {short_path(saved)}")

    return fig


def plot_defect_timeline(data: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                         config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                         outdir: Optional[PathLike] = None) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)

    steps = data.get("steps", [])
    defects = data.get("defect_count", [])

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if not steps or not defects:
            ax.text(0.5, 0.5, "No defect data", ha="center", va="center", transform=ax.transAxes)
            ax.axis("off")
        else:
            ax.plot(steps, defects, linewidth=2)
            _add_stage_backgrounds(ax, data.get("stage_transitions", []), steps)
            ax.set_xlabel("Simulation step")
            ax.set_ylabel("Defects")
            ax.set_title("Defect timeline")
            ax.grid(True, alpha=0.3)
            if len(defects) > 1 and float(defects[0]) > 0:
                healing = (float(defects[0]) - float(defects[-1])) / float(defects[0]) * 100.0
                ax.text(0.02, 0.98, f"Healing={healing:.1f}%", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="defect_timeline")
            saved = save_figure(fig, p, cfg)
            print(f"      Saved defect timeline: {short_path(saved)}")

    return fig


def plot_acceptance_rate(data: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                         config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                         outdir: Optional[PathLike] = None) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)

    steps = data.get("steps", [])
    acc = data.get("acceptance_rate")
    temp = data.get("temperature")

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if not steps or acc is None:
            ax.text(0.5, 0.5, "No acceptance data", ha="center", va="center", transform=ax.transAxes)
            ax.axis("off")
        else:
            acc_arr = np.asarray(acc, dtype=float)
            ax.plot(steps, acc_arr, linewidth=2, label="Acceptance")
            ax.set_xlabel("Simulation step")
            ax.set_ylabel("Acceptance")
            ax.set_title("Metropolis acceptance rate")
            ax.grid(True, alpha=0.3)
            if temp is not None:
                t_arr = np.asarray(temp, dtype=float)
                if t_arr.size and not np.all(np.isnan(t_arr)):
                    ax2 = ax.twinx()
                    ax2.plot(steps, t_arr, linestyle="--", linewidth=1.5, label="T")
                    ax2.set_ylabel("Temperature")
                    lines1, labels1 = ax.get_legend_handles_labels()
                    lines2, labels2 = ax2.get_legend_handles_labels()
                    ax.legend(lines1 + lines2, labels1 + labels2, loc="best")
                else:
                    ax.legend(loc="best")
            else:
                ax.legend(loc="best")

            _add_stage_backgrounds(ax, data.get("stage_transitions", []), steps)
            if acc_arr.size and not np.all(np.isnan(acc_arr)):
                ax.text(0.02, 0.98, f"Avg={np.nanmean(acc_arr)*100:.1f}%", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="acceptance_rate")
            saved = save_figure(fig, p, cfg)
            print(f"      Saved acceptance rate: {short_path(saved)}")

    return fig


def plot_healing_efficiency(data: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                            config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                            outdir: Optional[PathLike] = None) -> plt.Figure:
    cfg = cfg or load_publication_config(config_path)

    steps = data.get("steps", [])
    defects = data.get("defect_count", [])

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if not steps or not defects:
            ax.text(0.5, 0.5, "No defect data", ha="center", va="center", transform=ax.transAxes)
            ax.axis("off")
        else:
            d0 = float(defects[0])
            if d0 <= 0:
                ax.text(0.5, 0.5, "No initial defects", ha="center", va="center", transform=ax.transAxes)
                ax.axis("off")
            else:
                eff = [(d0 - float(d)) / d0 for d in defects]
                ax.plot(steps, eff, linewidth=2)
                _add_stage_backgrounds(ax, data.get("stage_transitions", []), steps)
                ax.set_xlabel("Simulation step")
                ax.set_ylabel("Healing efficiency")
                ax.set_ylim(0, 1.0)
                ax.set_title("Healing efficiency")
                ax.grid(True, alpha=0.3)
                ax.text(0.02, 0.98, f"Final={eff[-1]*100:.1f}%", transform=ax.transAxes, va="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="healing_efficiency")
            saved = save_figure(fig, p, cfg)
            print(f"      Saved healing efficiency: {short_path(saved)}")

    return fig


def plot_annealing_hysteresis(data: Dict[str, Any], *, save_path: Optional[PathLike] = None,
                             config_path: Optional[PathLike] = None, cfg: Optional[Dict[str, Any]] = None,
                             outdir: Optional[PathLike] = None) -> plt.Figure:
    """Plot mean energy per temperature stage."""
    cfg = cfg or load_publication_config(config_path)

    temp = data.get("temperature")
    energy = data.get("energy_total")

    with mpl_style(cfg):
        fig, ax = plt.subplots(figsize=(8, 6))
        if temp is None or energy is None:
            ax.text(0.5, 0.5, "No temperature/energy data", ha="center", va="center", transform=ax.transAxes)
            ax.axis("off")
        else:
            t = np.asarray(temp, dtype=float)
            e = np.asarray(energy, dtype=float)
            mask = ~np.isnan(t) & ~np.isnan(e)
            if not np.any(mask):
                ax.text(0.5, 0.5, "All temperature/energy values are NaN", ha="center", va="center", transform=ax.transAxes)
                ax.axis("off")
            else:
                t = t[mask]
                e = e[mask]

                # group by (approximately) constant temperature blocks
                uniq_t = []
                mean_e = []
                current_t = None
                block = []
                for ti, ei in zip(t, e):
                    if current_t is None or abs(ti - current_t) > 1e-6:
                        if current_t is not None:
                            uniq_t.append(current_t)
                            mean_e.append(float(np.mean(block)))
                        current_t = float(ti)
                        block = [float(ei)]
                    else:
                        block.append(float(ei))
                if current_t is not None:
                    uniq_t.append(current_t)
                    mean_e.append(float(np.mean(block)))

                ax.plot(uniq_t, mean_e, marker="o", linewidth=2)
                ax.set_xlabel("Temperature")
                ax.set_ylabel("Mean energy")
                ax.set_title("Annealing hysteresis (E vs T)")
                ax.grid(True, alpha=0.3)

        if save_path is not None or outdir is not None:
            p = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename="annealing_hysteresis")
            saved = save_figure(fig, p, cfg)
            print(f"      Saved annealing hysteresis: {short_path(saved)}")

    return fig
