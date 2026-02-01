#!/usr/bin/env python3
"""Diagnostic: flippable hexagons in active region vs globally.

Use this when MC seems starved for moves (almost no proposals/accepts).
"""
import sys
from pathlib import Path
from collections import Counter

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling, setup_simulation_components, initialize_seed_region


def main(seed_radius: float = 10.0) -> int:
    print(" DIAGNOSE ACTIVE REGION FLIPS")
    print("=" * 60)

    tiling = load_tiling()
    _, _, flip_engine = setup_simulation_components()

    # mark seed + optionally set flippable (we want active region flippability)
    initialize_seed_region(tiling, seed_radius=seed_radius, set_flippable=True)

    tiles = tiling["tiles"]
    active_ids = {t["id"] for t in tiles if t.get("growth_status") == "seed" and not t.get("removed", False)}

    # Global: ignore flippable flag by temporarily enabling it
    for t in tiles:
        if not t.get("removed", False):
            t["flippable"] = True
    global_hex = flip_engine.find_flippable_hexagons(tiling)

    # Active: restore active-only flippable
    for t in tiles:
        t["flippable"] = (t["id"] in active_ids) and (not t.get("removed", False))
    active_hex = flip_engine.find_flippable_hexagons(tiling)

    print(f"Seed radius: {seed_radius}")
    print(f"Active (seed) tiles: {len(active_ids)}")
    print(f"Flippable hexagons (global): {len(global_hex)}")
    print(f"Flippable hexagons (active): {len(active_hex)}")

    if len(active_hex) == 0:
        print("\n     CRITICAL: 0 flippable hexagons in active region → MC cannot move.")
        return 1
    if len(active_hex) < 10:
        print("\n    WARNING: very few flippable hexagons in active region → MC will be slow.")
        return 1

    print("\n    Active region has sufficient moves.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
