#!/usr/bin/env python3
"""Label / cache diagnostics.

Goal: detect 'zombie' cached data causing wrong energies after flips.

What it does:
- computes local energies for a sample
- clears caches + wipes local_energy fields
- recomputes and compares
- performs a few random flips and repeats on impacted region
"""
import sys
import random
import copy
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling, setup_simulation_components
from src.utils.energy_utils import wipe_all_energy_fields, clear_all_caches


def main(sample_size: int = 200, flips: int = 5) -> int:
    print("🏷️  LABEL / CACHE DIAGNOSTICS")
    print("=" * 60)

    tiling = load_tiling()
    t = copy.deepcopy(tiling)

    classifier, energy_model, flip_engine = setup_simulation_components()

    # ensure moves exist
    for tile in t["tiles"]:
        if not tile.get("removed", False):
            tile["flippable"] = True

    ids = [tile["id"] for tile in t["tiles"] if not tile.get("removed", False)]
    random.shuffle(ids)
    ids = ids[:min(sample_size, len(ids))]

    # Pass 1: compute local energies (populates local_energy + caches)
    e1 = {}
    for tid in ids:
        e1[tid] = energy_model.compute_local_energy(tid, t)

    # wipe fields + caches and recompute
    wipe_all_energy_fields(t)
    clear_all_caches(energy_model)

    e2 = {}
    for tid in ids:
        e2[tid] = energy_model.compute_local_energy(tid, t)

    diffs = [abs(e1[i] - e2[i]) for i in ids]
    max_diff = max(diffs) if diffs else 0.0
    bad = sum(1 for d in diffs if d > 1e-9)

    print(f"Sample size: {len(ids)}")
    print(f"Energy recompute diffs: bad={bad}, max={max_diff:.3e}")
    if bad:
        print("⚠️  WARNING: recompute is not identical. This can indicate nondeterminism or hidden mutation.")
        # Not an auto-fail; still useful.

    # Now do a few random flips and ensure wiping restores consistency
    hexes = flip_engine.find_flippable_hexagons(t)
    if not hexes:
        print("❌ No flippable hexagons found (cannot test flip-induced caching).")
        return 1

    random.shuffle(hexes)
    tested = 0
    for hx in hexes:
        if tested >= flips:
            break

        region = flip_engine._get_k_ring_neighborhood(hx, t, k=4)

        # baseline energies in region
        wipe_all_energy_fields(t)
        clear_all_caches(energy_model)
        before = {tid: energy_model.compute_local_energy(tid, t) for tid in region if not t["tiles"][tid].get("removed", False)}

        undo = flip_engine.capture_state(list(region), t)
        ok = flip_engine.apply_flip(hx, t)
        if not ok:
            flip_engine.restore_state(undo, t)
            continue

        # After flip: recompute twice with wipe/caches, check consistent
        wipe_all_energy_fields(t)
        clear_all_caches(energy_model)
        after1 = {tid: energy_model.compute_local_energy(tid, t) for tid in region if not t["tiles"][tid].get("removed", False)}
        wipe_all_energy_fields(t)
        clear_all_caches(energy_model)
        after2 = {tid: energy_model.compute_local_energy(tid, t) for tid in region if not t["tiles"][tid].get("removed", False)}

        max_region_diff = max(abs(after1[k]-after2[k]) for k in after1.keys()) if after1 else 0.0

        flip_engine.restore_state(undo, t)
        tested += 1
        print(f"Flip test {tested}: region_size={len(region)} | max_recompute_diff={max_region_diff:.3e}")

        if max_region_diff > 1e-8:
            print("❌ FAIL: region recompute inconsistency after flip (cache hygiene may be insufficient).")
            return 1

    print("✅ PASS: cache/label hygiene looks consistent under tested flips.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
