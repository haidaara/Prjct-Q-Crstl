"""Dynamic visualization (frames, storyboard, movie).

This module is snapshot-driven: it renders a chosen view for each snapshot file.

Output strategy (simple, robust):
- always write PNG frames
- optionally compile to GIF (always available) or MP4 (if ffmpeg works)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Union

import numpy as np
import matplotlib.pyplot as plt

from .config import load_publication_config
from .io import load_tiling_state, list_snapshots, parse_step, short_path
from .panels import build_patch_cache, draw_geometry, draw_energy, draw_defects, draw_class, draw_growth, draw_strain
from .style import mpl_style, save_figure, resolve_output_path

PathLike = Union[str, Path]


def _draw_view(ax, state: Dict[str, Any], view: str, cache=None, *, cfg: Dict[str, Any]):
    view = view.lower().strip()
    viz = cfg.get("viz_jobs", {})
    defect_threshold = float(viz.get("defect_threshold", 1.5))
    eperc = viz.get("energy_percentile", [5, 95])
    sperc = viz.get("strain_percentile", [5, 95])

    if view in {"geometry", "geom"}:
        draw_geometry(ax, state, cache=cache, title=None)
    elif view in {"energy"}:
        draw_energy(ax, state, cache=cache, percentile=(float(eperc[0]), float(eperc[1])), title=None)
    elif view in {"defects", "defect"}:
        draw_defects(ax, state, cache=cache, defect_threshold=defect_threshold, title=None)
    elif view in {"class", "energy_class", "vertex_class"}:
        draw_class(ax, state, cache=cache, title=None)
    elif view in {"growth"}:
        draw_growth(ax, state, cache=cache, title=None)
    elif view in {"strain", "phason"}:
        draw_strain(ax, state, cache=cache, percentile=(float(sperc[0]), float(sperc[1])), title=None)
    else:
        raise ValueError(f"Unknown view: {view}")


def render_frames(
    snapshot_paths: Sequence[PathLike],
    *,
    view: str = "strain",
    outdir: PathLike = "data/viz/frames",
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
) -> Path:
    """Render one PNG per snapshot and return the frames directory."""
    cfg = cfg or load_publication_config(config_path)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    with mpl_style(cfg):
        for i, p in enumerate(snapshot_paths):
            state = load_tiling_state(p)
            step = parse_step(state, default=i)

            fig, ax = plt.subplots(figsize=(8, 8))
            cache = build_patch_cache(state)
            _draw_view(ax, state, view, cache=cache, cfg=cfg)
            ax.set_title(f"{view} | step={step}")

            frame_path = outdir / f"frame_{i:05d}.png"
            fig.savefig(frame_path, dpi=200, bbox_inches="tight")
            plt.close(fig)

    return outdir


def make_storyboard(
    snapshot_dir: PathLike,
    *,
    view: str = "strain",
    n_frames: int = 12,
    ncols: int = 4,
    save_path: Optional[PathLike] = None,
    outdir: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
) -> plt.Figure:
    """Create a contact-sheet figure sampling snapshots across time."""
    cfg = cfg or load_publication_config(config_path)
    paths = list_snapshots(snapshot_dir)

    if not paths:
        with mpl_style(cfg):
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.text(0.5, 0.5, f"No snapshots found in {snapshot_dir}", ha="center", va="center")
            ax.axis("off")
            return fig

    n = min(int(n_frames), len(paths))
    idx = np.linspace(0, len(paths) - 1, n, dtype=int)
    chosen = [paths[i] for i in idx]

    ncols = max(1, int(ncols))
    nrows = int(np.ceil(n / ncols))

    with mpl_style(cfg):
        fig, axes = plt.subplots(nrows, ncols, figsize=(4.0 * ncols, 4.0 * nrows))
        axes = np.atleast_1d(axes).ravel()

        for ax in axes[n:]:
            ax.axis("off")

        for k, (ax, p) in enumerate(zip(axes[:n], chosen)):
            state = load_tiling_state(p)
            step = parse_step(state, default=k)
            cache = build_patch_cache(state)
            _draw_view(ax, state, view, cache=cache, cfg=cfg)
            ax.set_title(f"step={step}")

        fig.suptitle(f"Storyboard: {view}", fontweight="bold")

        if save_path is not None or outdir is not None:
            pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename=f"storyboard_{view}")
            saved = save_figure(fig, pth, cfg)
            print(f"   🎞️  Saved storyboard: {short_path(saved)}")

    return fig


def make_movie(
    snapshot_dir: PathLike,
    *,
    view: str = "strain",
    fps: int = 12,
    save_path: Optional[PathLike] = None,
    outdir: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
) -> Optional[Path]:
    """Render frames and compile to GIF (default) or MP4 (if chosen by suffix)."""
    cfg = cfg or load_publication_config(config_path)
    paths = list_snapshots(snapshot_dir)
    if not paths:
        print(f"⚠️  No snapshots found in {snapshot_dir}")
        return None

    viz_out = outdir or (cfg.get("paths", {}).get("output_dir", "data/publication/plots"))
    frames_dir = Path(viz_out) / "frames" / f"{Path(str(snapshot_dir)).name}_{view}"
    frames_dir = render_frames(paths, view=view, outdir=frames_dir, cfg=cfg)

    out = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=viz_out, filename=f"movie_{Path(str(snapshot_dir)).name}_{view}")
    if out.suffix.lower() not in {".gif", ".mp4"}:
        out = out.with_suffix(".gif")

    try:
        import imageio.v2 as imageio

        frame_paths = sorted(frames_dir.glob("frame_*.png"))
        if not frame_paths:
            print(f"⚠️  No frames written in {frames_dir}")
            return None

        if out.suffix.lower() == ".gif":
            imgs = [imageio.imread(p) for p in frame_paths]
            imageio.mimsave(out, imgs, duration=1 / max(1, fps))
        else:
            # mp4 via ffmpeg plugin
            writer = imageio.get_writer(out, fps=fps)
            for p in frame_paths:
                writer.append_data(imageio.imread(p))
            writer.close()

        print(f"   🎞️  Saved movie: {short_path(out)}")
        return out

    except Exception as e:
        print(f"⚠️  Movie compilation failed: {e}. Frames are in {frames_dir}")
        return None
