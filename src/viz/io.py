from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union


PathLike = Union[str, Path]


def load_json(path: PathLike) -> Dict[str, Any]:
    p = Path(path)
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def load_tiling_state(path: PathLike) -> Dict[str, Any]:
    """Load a *state* JSON. Accepts either:
      - flat: {"tiles": [...]}
      - wrapped: {"tiling": {"tiles": [...]}, "meta": {...}, ...}
    """
    data = load_json(path)

    # Flat schema
    if "tiles" in data:
        return data

    # Wrapped schema (healing snapshots)
    tiling = data.get("tiling")
    if isinstance(tiling, dict) and "tiles" in tiling:
        state = dict(tiling)  # shallow copy
        # carry metadata through for step parsing / provenance
        if "meta" in data and "meta" not in state:
            state["meta"] = data["meta"]
        if "metrics" in data and "metrics" not in state:
            state["metrics"] = data["metrics"]
        if "obstacle_metadata" in data and "obstacle_metadata" not in state:
            state["obstacle_metadata"] = data["obstacle_metadata"]
        return state

    raise ValueError(
        f"Input file '{Path(path).name}' is not a state snapshot. "
        "Expected 'tiles' or 'tiling.tiles'."
    )



def iter_tiles(state: Dict[str, Any]) -> Iterable[Tuple[int, Dict[str, Any]]]:
    for i, t in enumerate(state.get("tiles", [])):
        tid = t.get("id", i)
        try:
            tid_i = int(tid)
        except Exception:
            tid_i = i
        yield tid_i, t


def extract_tile_positions(state: Dict[str, Any]) -> List[List[float]]:
    """Return list of [x,y] centers for non-removed tiles."""
    pts: List[List[float]] = []
    for _, t in iter_tiles(state):
        if t.get("removed", False):
            continue
        c = t.get("center")
        if isinstance(c, (list, tuple)) and len(c) >= 2:
            pts.append([float(c[0]), float(c[1])])
    return pts


def extract_vertices(state: Dict[str, Any]) -> Tuple[List[List[List[float]]], List[int]]:
    """Return (polygons, ids) where polygons are lists of vertices [[x,y],...]."""
    polys: List[List[List[float]]] = []
    ids: List[int] = []
    for tid, t in iter_tiles(state):
        verts = t.get("vertices")
        if not isinstance(verts, list) or len(verts) < 3:
            continue
        poly = [[float(v[0]), float(v[1])] for v in verts]
        polys.append(poly)
        ids.append(tid)
    return polys, ids


def bounds_from_vertices(polys: List[List[List[float]]]) -> Optional[Tuple[Tuple[float, float], Tuple[float, float]]]:
    if not polys:
        return None
    xs = [v[0] for poly in polys for v in poly]
    ys = [v[1] for poly in polys for v in poly]
    return (min(xs), max(xs)), (min(ys), max(ys))


def short_path(path: PathLike, project_root: Optional[Path] = None) -> str:
    p = Path(path)
    if project_root is None:
        try:
            from .config import project_root_from_here
            project_root = project_root_from_here()
        except Exception:
            project_root = None

    if project_root is not None:
        try:
            return str(p.resolve().relative_to(project_root.resolve()))
        except Exception:
            pass

    parts = p.parts
    return str(Path(*parts[-4:])) if len(parts) > 4 else str(p)


_STEP_PAT = re.compile(r"(\d+)")


def step_from_snapshot_path(p: Path) -> Optional[int]:
    """Try to extract a step index from a snapshot filename."""
    m = _STEP_PAT.findall(p.stem)
    if not m:
        return None
    # heuristics: last number is often a counter or timestamp
    try:
        return int(m[-1])
    except Exception:
        return None


def step_from_snapshot_data(data: Dict[str, Any]) -> Optional[int]:
    meta = data.get("meta", {})
    for k in ("step", "mc_step", "timestep", "iteration", "sweep"):
        if k in meta:
            try:
                return int(meta[k])
            except Exception:
                continue
    # sometimes stored at top-level
    for k in ("step", "mc_step", "timestep"):
        if k in data:
            try:
                return int(data[k])
            except Exception:
                continue
    return None



def parse_step(data: Dict[str, Any], default: Optional[int] = None) -> int:
    """Best-effort step extraction used across viz modules.

    Priority:
      1) meta fields (meta.step / meta.mc_step / ...)
      2) top-level step-like fields
      3) fall back to `default` (or 0)
    """
    s = step_from_snapshot_data(data)
    if s is not None:
        return int(s)
    return int(default if default is not None else 0)

def list_snapshots(snapshot_dir: PathLike, pattern: str = "*.json") -> List[Path]:
    d = Path(snapshot_dir)
    if not d.exists() or not d.is_dir():
        return []
    return sort_snapshot_paths(list(d.glob(pattern)))


def sort_snapshot_paths(paths: List[Path]) -> List[Path]:
    def key(p: Path):
        s = step_from_snapshot_path(p)
        return (s is None, s if s is not None else 10**18, p.name)
    return sorted(paths, key=key)


def load_snapshots(paths: List[PathLike]) -> List[Tuple[Path, Dict[str, Any]]]:
    out: List[Tuple[Path, Dict[str, Any]]] = []
    for p in paths:
        pp = Path(p)
        data = load_tiling_state(pp)
        out.append((pp, data))
    return out
