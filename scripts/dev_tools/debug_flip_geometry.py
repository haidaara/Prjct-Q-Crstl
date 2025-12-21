#!/usr/bin/env python3
"""Flip geometry + energy delta smoke test.

Use when flips behave strangely (geometry jumps, parity mismatch, weird ΔE).
"""
import sys
import random
import copy
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling, setup_simulation_components
from src.utils.energy_utils import wipe_all_energy_fields, clear_all_caches


def region_energy(energy_model, tiling_data, region):
    return sum(
        energy_model.compute_local_energy(tid, tiling_data)
        for tid in region
        if not tiling_data["tiles"][tid].get("removed", False)
    )


def main(trials: int = 20) -> int:
    print("🧱 DEBUG FLIP GEOMETRY")
    print("=" * 60)

    base = load_tiling()
    tiling = copy.deepcopy(base)

    _, energy_model, flip_engine = setup_simulation_components(verbose=False)

    # Ensure moves exist
    for t in tiling["tiles"]:
        if not t.get("removed", False):
            t["flippable"] = True

    hexes = flip_engine.find_flippable_hexagons(tiling)
    if not hexes:
        print("❌ No flippable hexagons found.")
        return 1

    random.shuffle(hexes)
    tested = 0

    for hx in hexes:
        if tested >= trials:
            break

        region = flip_engine._get_k_ring_neighborhood(hx, tiling, k=4)

        wipe_all_energy_fields(tiling)
        clear_all_caches(energy_model)
        e_before = region_energy(energy_model, tiling, region)

        undo = flip_engine.capture_state(list(region), tiling)
        ok = flip_engine.apply_flip(hx, tiling)
        if not ok:
            flip_engine.restore_state(undo, tiling)
            continue

        wipe_all_energy_fields(tiling)
        clear_all_caches(energy_model)
        e_after = region_energy(energy_model, tiling, region)

        # restore and recompute again to ensure exact undo
        flip_engine.restore_state(undo, tiling)

        wipe_all_energy_fields(tiling)
        clear_all_caches(energy_model)
        e_restore = region_energy(energy_model, tiling, region)

        tested += 1
        print(f"Trial {tested:02d}: ΔE={(e_after - e_before): .6f} | restore_diff={abs(e_restore - e_before):.3e} | region={len(region)}")

        if abs(e_restore - e_before) > 1e-8:
            print("❌ FAIL: restore did not return to identical energy (state capture/restore bug or hidden mutation).")
            return 1

    print("✅ PASS: flip apply/restore seems consistent for tested samples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
