from __future__ import annotations

"""Configuration loading for visualization.

Reads a single config file: ``configs/publication_plots.toml``.

Style (aesthetics) sections:
- [publication], [fonts], [lines], [figure], [paths]

Plot generation jobs:
- [viz_jobs]
  - [[viz_jobs.jobs]] entries

The job schema is intentionally permissive; runner scripts validate fields.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union


DEFAULT_CONFIG: Dict[str, Any] = {
    "publication": {
        "format": "pdf",
        "dpi": 600,
        "transparent_background": False,
        "tight_layout": True,
    },
    "fonts": {
        "family": "DejaVu Sans",
        "base_size": 10,
        "title_size": 12,
        "label_size": 10,
    },
    "lines": {
        "line_width": 1.2,
        "marker_size": 4,
    },
    "figure": {
        "default_figsize": [6.5, 4.0],
        "matrix_figsize": [18, 18],
    },
    "paths": {
        "output_dir": "data/publication/plots",
    },
    "viz_jobs": {
        "enabled": False,
        "defect_threshold": 1.5,
        "energy_percentile": [5, 95],
        "strain_percentile": [5, 95],
        "treat_immobile_as_fixed": False,
        "jobs": [],
    },
}


def _toml_loads(text: str) -> Dict[str, Any]:
    """Parse TOML using tomllib when available, else toml."""
    try:
        import tomllib  # py>=3.11
        return tomllib.loads(text)
    except Exception:
        try:
            import toml  # type: ignore
            return toml.loads(text)
        except Exception as e:
            raise RuntimeError(
                "TOML parsing failed. Install 'toml' (py<3.11) or fix the TOML file."
            ) from e


def _deep_merge(dst: Dict[str, Any], src: Dict[str, Any]) -> Dict[str, Any]:
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            _deep_merge(dst[k], v)  # type: ignore[index]
        else:
            dst[k] = v
    return dst


def project_root_from_here() -> Path:
    # .../src/viz/config.py -> parents[2] is project root
    return Path(__file__).resolve().parents[2]


def default_config_path() -> Path:
    root = project_root_from_here()
    p1 = root / "configs" / "publication_plots.toml"
    if p1.exists():
        return p1
    # Convenience: allow a repo-root config file.
    p2 = root / "publication_plots.toml"
    if p2.exists():
        return p2
    return p1


def load_publication_config(config_path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
    """Load config and merge with defaults."""
    # start from defaults
    cfg: Dict[str, Any] = {k: (v.copy() if isinstance(v, dict) else v) for k, v in DEFAULT_CONFIG.items()}

    path = Path(config_path) if config_path is not None else default_config_path()
    if not path.exists():
        return cfg

    try:
        text = path.read_text(encoding="utf-8")
        loaded = _toml_loads(text)
        _deep_merge(cfg, loaded)
    except Exception as e:
        print(f"⚠️  Failed to load config '{path}': {e}. Using defaults.")
        return cfg

    # ensure missing sections exist
    for section, defaults in DEFAULT_CONFIG.items():
        if section not in cfg:
            cfg[section] = defaults.copy() if isinstance(defaults, dict) else defaults

    return cfg


def get_viz_jobs(cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return list of job dicts from cfg['viz_jobs']['jobs'] (if present)."""
    viz_jobs = cfg.get("viz_jobs", {})
    jobs = viz_jobs.get("jobs", [])
    if not isinstance(jobs, list):
        return []
    return [j for j in jobs if isinstance(j, dict)]
