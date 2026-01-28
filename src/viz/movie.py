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
from .static_plots import plot_physics_matrix
from .style import mpl_style, save_figure, resolve_output_path
from .static_plots import draw_matrix_2x2


PathLike = Union[str, Path]


def _iter_tiles(state: Dict[str, Any]) -> Sequence[Dict[str, Any]]:
    """Best-effort tiles extractor compatible with snapshots structure."""
    if isinstance(state, dict):
        tiling = state.get("tiling")
        if isinstance(tiling, dict):
            tiles = tiling.get("tiles")
            if isinstance(tiles, list):
                return tiles
        tiles = state.get("tiles")
        if isinstance(tiles, list):
            return tiles
    return []


def _safe_float(x: Any) -> Optional[float]:
    try:
        if x is None or isinstance(x, bool):
            return None
        return float(x)
    except Exception:
        return None


def _frame_metrics_title(state: Dict[str, Any], cfg: Optional[Dict[str, Any]]) -> str:
    """Compact metrics string for each frame title."""
    tiles = _iter_tiles(state)
    n_total = len(tiles)

    n_removed = 0
    n_pore = 0

    e_local: list[float] = []
    e_phason: list[float] = []

    for t in tiles:
        if bool(t.get("removed", False)):
            n_removed += 1
            continue
        if str(t.get("obstacle_type", "none")).lower() == "pore":
            n_pore += 1
            continue

        el = _safe_float(t.get("local_energy"))
        if el is not None:
            e_local.append(el)

        ep = _safe_float(t.get("phason_energy"))
        if ep is not None:
            e_phason.append(ep)

    mean_local = (sum(e_local) / len(e_local)) if e_local else None
    mean_phason = (sum(e_phason) / len(e_phason)) if e_phason else None

    thr = None
    if isinstance(cfg, dict):
        viz = cfg.get("viz_jobs", {})
        if isinstance(viz, dict):
            thr = _safe_float(viz.get("defect_threshold"))
    n_def = None
    if thr is not None and e_local:
        n_def = sum(1 for e in e_local if e >= thr)

    parts = [f"N={n_total}", f"pore={n_pore}"]
    if n_removed:
        parts.append(f"removed={n_removed}")
    if mean_local is not None:
        parts.append(f"<E>={mean_local:.3g}")
    if mean_phason is not None:
        parts.append(f"<Ephi>={mean_phason:.3g}")
    if n_def is not None:
        parts.append(f"E>={thr:g}:{n_def}")

    return "  ".join(parts)


def _frame_title(state: Dict[str, Any], view: str, step: int) -> str:
    """Consistent, informative title for frames (works for flat and wrapped snapshots)."""
    meta = state.get("meta", {})
    if not isinstance(meta, dict):
        meta = {}

    metrics = state.get("metrics", {})
    if not isinstance(metrics, dict):
        metrics = {}

    parts = [f"{view}", f"step={step}"]

    label = meta.get("label", None)
    run_id = meta.get("run_id", None)
    temp = meta.get("temperature", None)

    if label:
        parts.append(f"label={label}")
    if run_id:
        parts.append(f"run={run_id}")
    if temp is not None:
        parts.append(f"T={temp}")

    E = metrics.get("energy", None)
    D = metrics.get("defects", None)

    if isinstance(E, (int, float)):
        parts.append(f"E={E:.3f}")
    elif E is not None:
        parts.append(f"E={E}")

    if D is not None:
        parts.append(f"defects={D}")

    return " | ".join(parts)


def _draw_view(ax, state: Dict[str, Any], view: str, cache=None, *, cfg: Dict[str, Any]):
    view = view.lower().strip()
    viz = cfg.get("viz_jobs", {})
    defect_threshold = float(viz.get("defect_threshold", 1.5))

    treat_immobile_as_fixed = bool(viz.get("treat_immobile_as_fixed", False))
    energy_gamma = float(viz.get("energy_gamma", 4.0))

    eperc = viz.get("energy_percentile", [5, 95])
    sperc = viz.get("strain_percentile", [5, 95])

    energy_vmin = viz.get("energy_vmin", None)
    energy_vmax = viz.get("energy_vmax", None)
    strain_vmin = viz.get("strain_vmin", None)
    strain_vmax = viz.get("strain_vmax", None)


    if view in {"geometry", "geom"}:
        draw_geometry(ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed, title=None)
    elif view in {"energy", "energy_local", "local_energy"}:
        draw_energy(ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    percentile=(float(eperc[0]), float(eperc[1])), gamma=energy_gamma,
                    vmin=energy_vmin, vmax=energy_vmax, title=None)

    elif view in {"defects", "defect"}:
        draw_defects(ax, state, cache=cache, defect_threshold=defect_threshold, title=None)
    elif view in {"class", "energy_class"}:
        draw_class(ax, state, cache=cache, prefer="energy_class",
                   treat_immobile_as_fixed=treat_immobile_as_fixed, title=None)
    elif view in {"vertex_class"}:
        draw_class(ax, state, cache=cache, prefer="vertex_class",
                   treat_immobile_as_fixed=treat_immobile_as_fixed, title=None)

    elif view in {"growth"}:
        draw_growth(ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed, title=None)
    elif view in {"strain", "phason", "phason_energy", "phason_strain"}:
        draw_strain(ax, state, cache=cache, treat_immobile_as_fixed=treat_immobile_as_fixed,
                    percentile=(float(sperc[0]), float(sperc[1])),
                    vmin=strain_vmin, vmax=strain_vmax, title=None)

    else:
        raise ValueError(f"Unknown view: {view}")


def _log_forced_scale(*, view: str, cfg: Dict[str, Any], n_snapshots: int) -> None:
    """Log the forced (vmin,vmax) scale used for comparability across frames.

    Option A: scales are chosen by the user in TOML; we do NOT infer them from frames.
    """
    viz = cfg.get("viz_jobs", {})
    v = str(view).lower().strip()

    if v in {"energy", "energy_local", "local_energy"}:
        vmin = viz.get("energy_vmin", None)
        vmax = viz.get("energy_vmax", None)
        gamma = float(viz.get("energy_gamma", 4.0))
        if vmin is not None and vmax is not None:
            print(f"   Fixed scale (Local Energy) over {n_snapshots} snapshots: {vmin} .. {vmax}  (gamma={gamma})")
        else:
            print("   Local Energy scale: not fixed (no energy_vmin/energy_vmax in TOML). Colors may not be comparable across time.")
        return

    if v in {"strain", "phason", "phason_energy"}:
        vmin = viz.get("strain_vmin", None)
        vmax = viz.get("strain_vmax", None)
        if vmin is not None and vmax is not None:
            print(f"   Fixed scale (Phason strain energy) over {n_snapshots} snapshots: {vmin} .. {vmax}")
        else:
            print("   Phason strain energy scale: not fixed (no strain_vmin/strain_vmax in TOML). Colors may not be comparable across time.")
        return



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

    snapshot_paths = list(snapshot_paths)
    if not snapshot_paths:
        print("No snapshots to render.")
        return outdir


    # Prevent stale frames from corrupting movies on reruns
    for old in outdir.glob("frame_*.png"):
        try:
            old.unlink()
        except Exception:
            pass


    viz = cfg.get("viz_jobs", {})
    fs = viz.get("movie_figsize", [8, 8])
    try:
        movie_figsize = (float(fs[0]), float(fs[1]))
    except Exception:
        movie_figsize = (8.0, 8.0)

    movie_dpi = int(viz.get("movie_dpi", 200))
    show_title = bool(viz.get("movie_title", True))

    with mpl_style(cfg):
        for i, p in enumerate(snapshot_paths):
            state = load_tiling_state(p)
            step = parse_step(state, default=i)

            v = str(view).lower().strip()

            if v in {"matrix_2x2", "matrix"}:
                # Render using the same publication plotter as 01_viz_state to preserve style
                from .static_plots import plot_physics_matrix

                fig = plot_physics_matrix(
                    state,
                    panels=None,      # uses cfg["viz_jobs"]["matrix_2x2_panels"]
                    cfg=cfg,
                    outdir=None,      # IMPORTANT: avoid auto-saving from inside plot_physics_matrix
                    save_path=None,   # IMPORTANT: avoid auto-saving from inside plot_physics_matrix
                    title=None,
                    log=False,
                )

                if show_title:
                    fig.suptitle(_frame_title(state, "matrix_2x2", step), fontweight="bold")

            else:
                metrics = _frame_metrics_title(state, cfg)
                title = f"{view} | step={step}  {metrics}"

                if str(view).lower().strip() in {"matrix_2x2", "matrix"}:
                    fig = plot_physics_matrix(state, cfg=cfg, title=title)
                else:
                    fig, ax = plt.subplots(figsize=movie_figsize)
                    cache = build_patch_cache(state)
                    _draw_view(ax, state, view, cache=cache, cfg=cfg)
                    if show_title:
                        ax.set_title(title, fontsize=10)



            frame_path = outdir / f"frame_{i:05d}.png"
            # IMPORTANT: do NOT use bbox_inches="tight" for movie frames
            fig.savefig(frame_path, dpi=movie_dpi)
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

    _log_forced_scale(view=view, cfg=cfg, n_snapshots=len(paths))


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


def make_storyboard_from_frames(
    frames_dir: PathLike,
    *,
    view: str = "strain",
    n_frames: int = 12,
    ncols: int = 4,
    save_path: Optional[PathLike] = None,
    outdir: Optional[PathLike] = None,
    config_path: Optional[PathLike] = None,
    cfg: Optional[Dict[str, Any]] = None,
) -> plt.Figure:
    """Create a storyboard (contact sheet) from already-rendered frame PNGs."""
    import math
    import matplotlib.image as mpimg

    cfg = cfg or load_publication_config(config_path)
    frames_dir = Path(frames_dir)

    frame_paths = sorted(frames_dir.glob("frame_*.png"))
    if not frame_paths:
        raise ValueError(f"No frames found in {frames_dir}")

    ncols = max(int(ncols), 1)
    n_take = min(int(n_frames), len(frame_paths)) if n_frames else len(frame_paths)

    idxs = np.linspace(0, len(frame_paths) - 1, n_take).astype(int)
    chosen = [frame_paths[i] for i in idxs]

    nrows = int(math.ceil(len(chosen) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.2 * ncols, 3.2 * nrows))
    if not isinstance(axes, np.ndarray):
        axes = np.array([axes])
    axes_flat = axes.ravel()

    for ax, pth in zip(axes_flat, chosen):
        img = mpimg.imread(pth)
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(pth.stem.replace("frame_", ""), fontsize=8)

    for ax in axes_flat[len(chosen):]:
        ax.axis("off")

    fig.suptitle(f"Storyboard: {view}", y=0.99)
    fig.tight_layout()

    pth = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=outdir, filename=f"storyboard_{view}")
    saved = save_figure(fig, pth, cfg=cfg)
    print(f"   Saved storyboard: {short_path(saved)}")
    return fig



def make_movie(
    snapshot_dir: PathLike,
    *,
    view: str = "strain",
    fps: int = 12,
    save_path: Optional[PathLike] = None,
    frames_dir: Optional[PathLike] = None,
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

    _log_forced_scale(view=view, cfg=cfg, n_snapshots=len(paths))


    viz_out = outdir or (cfg.get("paths", {}).get("output_dir", "data/publication/plots"))
    frames_dir_path = Path(frames_dir) if frames_dir is not None else (Path(viz_out) / "frames" / f"{Path(str(snapshot_dir)).name}_{view}")
    frames_dir_path = render_frames(paths, view=view, outdir=frames_dir_path, cfg=cfg)


    out = Path(save_path) if save_path is not None else resolve_output_path(cfg, outdir=viz_out, filename=f"movie_{Path(str(snapshot_dir)).name}_{view}")
    if out.suffix.lower() not in {".gif", ".mp4"}:
        out = out.with_suffix(".mp4")

    try:
        import imageio.v2 as imageio

        frame_paths = sorted(frames_dir_path.glob("frame_*.png"))
        if not frame_paths:
            print(f"[Attention]  No frames written in {frames_dir}")
            return None
        else:
            print(f"Frames produced: {len(frame_paths)}")
            print(f"Frames location: {frames_dir}")

        if out.suffix.lower() == ".gif":
            imgs = [imageio.imread(p) for p in frame_paths]
            imageio.mimsave(out, imgs, duration=1 / max(1, fps))
        else:
            # mp4 via ffmpeg plugin
            writer = imageio.get_writer(out, fps=fps)
            for p in frame_paths:
                writer.append_data(imageio.imread(p))
            writer.close()

        print(f"      Saved movie: {short_path(out)}")
        return out

    except Exception as e:
        msg = str(e)
        if "No module named" in msg and "imageio" in msg:
            print("[Attention]  Movie compilation requires 'imageio'. Install with: pip install imageio imageio-ffmpeg")
            print(f"    Frames are in {frames_dir}")
        else:
            print(f"[Attention]  Movie compilation failed: {e}. Frames are in {frames_dir}")
        return None

