from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Optional, Union

import matplotlib.pyplot as plt


PathLike = Union[str, Path]


@contextmanager
def mpl_style(cfg: Dict[str, Any]):
    """Apply matplotlib styling from config for the duration of the context."""
    fonts = cfg.get("fonts", {})
    base_size = fonts.get("base_size", 10)
    family = fonts.get("family", "DejaVu Sans")

    rc = {
        "font.family": family,
        "font.size": base_size,
        "axes.titlesize": fonts.get("title_size", base_size + 2),
        "axes.labelsize": fonts.get("label_size", base_size),
        "xtick.labelsize": base_size - 1,
        "ytick.labelsize": base_size - 1,
        "legend.fontsize": base_size - 1,
        "figure.titlesize": fonts.get("title_size", base_size + 2) + 2,
        "axes.grid": False,
    }

    with plt.rc_context(rc):
        yield


def ensure_suffix(path: Path, fmt: str) -> Path:
    if path.suffix:
        return path
    return path.with_suffix(f".{fmt}")


def save_figure(fig, outpath: PathLike, cfg: Dict[str, Any]) -> Path:
    pub = cfg.get("publication", {})
    fmt = pub.get("format", "pdf")
    dpi = int(pub.get("dpi", 300))
    transparent = bool(pub.get("transparent_background", False))

    p = Path(outpath)
    p = ensure_suffix(p, fmt)
    p.parent.mkdir(parents=True, exist_ok=True)

    if pub.get("tight_layout", True):
        try:
            fig.tight_layout()
        except Exception:
            pass

    fig.savefig(p, dpi=dpi, bbox_inches="tight", transparent=transparent)
    plt.close(fig)
    return p


def default_output_dir(cfg: Dict[str, Any]) -> Path:
    paths = cfg.get("paths", {})
    return Path(paths.get("output_dir", "data/publication/plots"))


def resolve_output_path(
    cfg: Dict[str, Any],
    *,
    outdir: Optional[PathLike] = None,
    filename: str,
) -> Path:
    base = Path(outdir) if outdir is not None else default_output_dir(cfg)
    return base / filename
