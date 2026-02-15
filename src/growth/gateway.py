"""SSOT Gateway (C0–C2c): loading, validation, field initialization.

Design goals
------------
- Minimal, flat (no extra folders).
- Pure-ish functions: mutate only tiling_data in a controlled, additive way.
- Fail-fast on invalid input (Contract 1.2).

This module does NOT implement any growth engine loop.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Literal, Optional, Tuple

from src.utils.config import ConfigManager

AdjacencySource = Literal["neighbors", "adjacency_graph"]


def load_config(config_path: str) -> ConfigManager:
    """Load TOML via the existing ConfigManager (reuse mandate).

    SSOT v1.0 determinism and defaults are handled in GrowthContext creation.
    """

    return ConfigManager(config_path)


def validate_tiling_schema(tiling_data: Dict[str, Any]) -> None:
    """Fail-fast validation for minimum tiling schema (Contract 1.1 + C2).

    Required:
      - tiling_data['tiles'] list
      - each tile has: id, center, vertices
      - removed/immobile/flippable may be missing but must be addable
      - adjacency exists via tile['neighbors'] OR tiling_data['adjacency_graph']
    """

    if not isinstance(tiling_data, dict):
        raise TypeError("tiling_data must be a dict")

    tiles = tiling_data.get("tiles")
    if not isinstance(tiles, list) or not tiles:
        raise ValueError("tiling_data['tiles'] must be a non-empty list")

    # Minimal per-tile fields
    for i, t in enumerate(tiles[: min(len(tiles), 50)]):  # sample early for speed
        if not isinstance(t, dict):
            raise ValueError(f"tile[{i}] must be a dict")
        for k in ("id", "center", "vertices"):
            if k not in t:
                raise ValueError(f"tile[{i}] missing required key: {k}")

    # Adjacency presence
    has_neighbors = any(isinstance(t.get("neighbors"), list) for t in tiles[: min(len(tiles), 50)])
    has_adj_graph = isinstance(tiling_data.get("adjacency_graph"), dict)
    if not (has_neighbors or has_adj_graph):
        raise ValueError(
            "Adjacency missing: expected per-tile 'neighbors' OR tiling_data['adjacency_graph']"
        )


def detect_adjacency_source(tiling_data: Dict[str, Any]) -> AdjacencySource:
    """Detect adjacency source (Contract C2): neighbors vs adjacency_graph."""

    tiles = tiling_data["tiles"]
    if tiles and all(isinstance(t.get("neighbors"), list) for t in tiles):
        return "neighbors"
    if isinstance(tiling_data.get("adjacency_graph"), dict):
        return "adjacency_graph"
    raise ValueError("No adjacency source detected")


def _ensure_bool_field(tiles: List[Dict[str, Any]], key: str, default: bool) -> None:
    for t in tiles:
        if key not in t:
            t[key] = default
        else:
            # Normalize to bool (JSON might have 0/1)
            t[key] = bool(t[key])


def ensure_constraint_fields(tiling_data: Dict[str, Any]) -> None:
    """C2c: ensure removed/immobile exist on all tiles (additive)."""

    tiles = tiling_data["tiles"]
    _ensure_bool_field(tiles, "removed", False)
    _ensure_bool_field(tiles, "immobile", False)


def ensure_mc_fields(tiling_data: Dict[str, Any]) -> None:
    """C2a: ensure flippable exists on all tiles (additive)."""

    tiles = tiling_data["tiles"]
    _ensure_bool_field(tiles, "flippable", False)


def ensure_growth_fields(tiling_data: Dict[str, Any], *, birth_event_enabled: bool = True) -> None:
    """C1: ensure growth fields exist on all tiles (additive).

    Contract 2.1 requires:
      - growth_status in {ungrown, seed, grown}
      - birth_cycle, birth_event (optional), birth_mode, birth_family
    """

    tiles = tiling_data["tiles"]
    for t in tiles:
        # SSOT compatibility: many inputs are "fully grown" snapshots;
        # reset_growth_state_for_run() will enforce the run semantics.
        if "growth_status" not in t:
            t["growth_status"] = "grown"

        gs = t.get("growth_status")
        removed = bool(t.get("removed", False))

        # Legacy/obstacle data may carry gs="removed" for pore-vacuum tiles.
        # growth_status is irrelevant for removed tiles (present(tile)=False).
        if removed and gs not in ("ungrown", "seed", "grown"):
            t["growth_status"] = "ungrown"
        elif (not removed) and gs not in ("ungrown", "seed", "grown"):
            raise ValueError(f"Invalid growth_status: {gs}")


        t.setdefault("birth_cycle", None)
        if birth_event_enabled:
            t.setdefault("birth_event", None)
        else:
            # Keep additive compatibility: don't delete; just leave as-is if present
            pass

        t.setdefault("birth_mode", None)
        t.setdefault("birth_family", None)


def reset_growth_state_for_run(tiling_data: Dict[str, Any]) -> None:
    """C2b: reset growth state for a run (MANDATORY).

    Rules (per SSOT v1.0 + your matrix notes):
      - removed stays removed (do not change)
      - immobile tiles are treated as grown (present but not active)
      - all other non-removed tiles become ungrown
      - clear birth fields

    This does NOT seed anything; seeding is Phase 2.
    """

    tiles = tiling_data["tiles"]
    for t in tiles:
        if bool(t.get("removed", False)):
            # Keep removed tiles as ungrown (or leave) but they should not be present.
            t["growth_status"] = "ungrown"
        elif bool(t.get("immobile", False)):
            t["growth_status"] = "grown"
        else:
            t["growth_status"] = "ungrown"

        # Clear birth fields
        t["birth_cycle"] = None
        if "birth_event" in t:
            t["birth_event"] = None
        t["birth_mode"] = None
        t["birth_family"] = None


def normalize_adjacency_graph_keys(tiling_data: Dict[str, Any]) -> None:
    """Normalize adjacency_graph keys to strings (legacy reality).

    - If adjacency_graph exists with int keys, rewrite to str keys.
    - Values are expected to be list[int].

    This is additive/safe and matches FlipEngine behavior.
    """

    g = tiling_data.get("adjacency_graph")
    if not isinstance(g, dict):
        return

    # If already all strings, nothing to do.
    if all(isinstance(k, str) for k in g.keys()):
        return

    new_g: Dict[str, Any] = {}
    for k, v in g.items():
        new_g[str(k)] = v
    tiling_data["adjacency_graph"] = new_g


def adjacency_sanity_check(tiling_data: Dict[str, Any], *, sample_edges: int = 2000) -> None:
    """C2: adjacency detect + sanity (lightweight).

    Checks:
      - neighbor lists are list[int]
      - IDs within range
      - approximate symmetry on a sample (optional)

    Raises ValueError on invalid adjacency.
    """

    tiles = tiling_data["tiles"]
    n = len(tiles)
    src = detect_adjacency_source(tiling_data)

    def neighbors_of(i: int) -> List[int]:
        if src == "neighbors":
            return list(tiles[i].get("neighbors") or [])
        g = tiling_data["adjacency_graph"]
        return list(g.get(str(i), []) or [])

    # Type + bounds
    for i in range(min(n, 200)):
        nbrs = neighbors_of(i)
        if not isinstance(nbrs, list):
            raise ValueError(f"neighbors for tile {i} not a list")
        for j in nbrs[:100]:
            if not isinstance(j, int):
                raise ValueError(f"neighbor id not int: tile {i} -> {j}")
            if j < 0 or j >= n:
                raise ValueError(f"neighbor out of range: tile {i} -> {j} (n={n})")

    # Approx symmetry check on a sample
    checked = 0
    for i in range(min(n, 500)):
        for j in neighbors_of(i)[:20]:
            if checked >= sample_edges:
                return
            if i not in neighbors_of(j):
                # Don't error hard: legacy adjacency may be slightly asymmetric.
                # But for SSOT v1.0 we at least warn loudly.
                # Raise ValueError only if asymmetry is extreme? Here: soft via exception type.
                raise ValueError(f"adjacency asymmetry detected at edge {i}<->{j}")
            checked += 1
