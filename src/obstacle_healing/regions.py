# src/obstacle_healing/regions.py
from __future__ import annotations

import math
from typing import Dict, List, Set, Tuple


def _distance(p: Tuple[float, float], q: Tuple[float, float]) -> float:
    return math.hypot(p[0] - q[0], p[1] - q[1])


def _get_obstacle_centers_and_radii(tiling: Dict) -> Tuple[List[Tuple[float, float]], List[float]]:
    meta = tiling.get("obstacle_metadata") or {}
    positions = meta.get("positions") or []
    radii = meta.get("radii") or []
    centers = [(float(x), float(y)) for x, y in positions]
    radii_f = [float(r) for r in radii] if radii is not None else []
    return centers, radii_f


def select_measurement_tiles(
    tiling: Dict,
    *,
    mode: str,
    inner: float,
    outer: float,
    relative_to_radius: bool = True,
    fixed_k: int = 2,
) -> List[int]:
    """
    mode:
      - 'pores': annulus around pore centers
      - 'fixed_defects': k-hop neighborhood around immobile tiles
    """
    mode = str(mode).lower()
    tiles = tiling["tiles"]

    if mode == "pores":
        centers, radii = _get_obstacle_centers_and_radii(tiling)
        if not centers:
            return []
        selected: Set[int] = set()
        for idx, t in enumerate(tiles):
            if t.get("removed", False):
                continue
            cx, cy = map(float, t.get("center", (0.0, 0.0)))
            p = (cx, cy)
            for c, r in zip(centers, radii or [0.0] * len(centers)):
                r_in = (r + inner) if relative_to_radius else inner
                r_out = (r + outer) if relative_to_radius else outer
                d = _distance(p, c)
                if (d >= r_in) and (d <= r_out):
                    selected.add(idx)
                    break
        return sorted(selected)

    if mode == "fixed_defects":
        immobile = {i for i, t in enumerate(tiles) if (t.get("immobile", False) and not t.get("removed", False))}
        if not immobile:
            return []
        g = tiling.get("adjacency_graph") or {}

        def neigh(node: int) -> List[int]:
            return [int(x) for x in g.get(str(node), g.get(node, [])) or []]

        frontier = set(immobile)
        visited = set(immobile)
        for _ in range(int(max(fixed_k, 0))):
            nxt = set()
            for u in frontier:
                for v in neigh(u):
                    if v not in visited:
                        visited.add(v)
                        nxt.add(v)
            frontier = nxt
            if not frontier:
                break

        visited = {i for i in visited if (i not in immobile and not tiles[i].get("removed", False))}
        return sorted(visited)

    raise ValueError(f"Unknown obstacle mode: {mode}")


def select_active_tiles(
    tiling: Dict,
    *,
    mode: str,
    measurement_ids: List[int],
    active_buffer: float = 6.0,
    fixed_active_k: int = 3,
) -> List[int]:
    """Tile IDs allowed to flip during damage/healing."""
    mode = str(mode).lower()
    tiles = tiling["tiles"]

    if mode == "pores":
        centers, radii = _get_obstacle_centers_and_radii(tiling)
        if not centers:
            return []
        selected: Set[int] = set()
        for idx, t in enumerate(tiles):
            if t.get("removed", False) or t.get("immobile", False):
                continue
            cx, cy = map(float, t.get("center", (0.0, 0.0)))
            p = (cx, cy)
            for c, r in zip(centers, radii or [0.0] * len(centers)):
                d = _distance(p, c)
                if d <= (r + active_buffer):
                    selected.add(idx)
                    break
        selected.update(measurement_ids)
        return sorted(selected)

    if mode == "fixed_defects":
        g = tiling.get("adjacency_graph") or {}
        immobile = {i for i, t in enumerate(tiles) if (t.get("immobile", False) and not t.get("removed", False))}
        if not immobile:
            return []

        def neigh(node: int) -> List[int]:
            return [int(x) for x in g.get(str(node), g.get(node, [])) or []]

        frontier = set(immobile)
        visited = set(immobile)
        for _ in range(int(max(fixed_active_k, 0))):
            nxt = set()
            for u in frontier:
                for v in neigh(u):
                    if v not in visited:
                        visited.add(v)
                        nxt.add(v)
            frontier = nxt
            if not frontier:
                break

        active = {i for i in visited if (not tiles[i].get("removed", False) and not tiles[i].get("immobile", False))}
        active.update(measurement_ids)
        return sorted(active)

    raise ValueError(f"Unknown obstacle mode: {mode}")
