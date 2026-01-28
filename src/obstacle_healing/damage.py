# src/obstacle_healing/damage.py
from __future__ import annotations

from typing import Any, Dict, List, Tuple


def count_defects_fast(tiling: Dict, measurement_ids: List[int], *, defect_threshold: float) -> int:
    """Fast defect count using tile['local_energy'] initialized at baseline."""
    tiles = tiling["tiles"]
    c = 0
    for tid in measurement_ids:
        t = tiles[tid]
        if t.get("removed", False):
            continue
        e = t.get("local_energy")
        if e is None:
            continue
        if float(e) > defect_threshold:
            c += 1
    return c


def damage_by_heating(
    tiling: Dict,
    *,
    mc_engine: Any,
    measurement_ids: List[int],
    defect_threshold: float,
    baseline_defects: int,
    target_additional_defects: int,
    max_steps: int,
    temperature: float,
    check_every: int,
    log_cb=None,
) -> Tuple[int, int, int]:
    """
    Run MC at high T until defects reaches baseline + target_additional_defects or max_steps.
    Returns (target_total_defects, achieved_defects, steps_used).
    """


    mc_engine.temperature = float(temperature)
    if getattr(mc_engine, "_step_counter", 0) == 0:
        mc_engine.initialize_energy(tiling)

    target_total = int(baseline_defects) + int(max(target_additional_defects, 0))

    # Ensure defect counts reflect the current state:
    # local_energy may be stale for measurement tiles not touched recently by the MC delta region.
    mc_engine._compute_region_energy_fresh(list(measurement_ids), tiling, extra_ring=1)

    current = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)


    steps = 0
    while current < target_total and steps < max_steps:
        mc_engine.run_step(tiling, debug_mode=False)
        steps += 1
        if steps % max(1, int(check_every)) == 0 or steps == max_steps:
            # Refresh measurement energies before counting defects
            mc_engine._compute_region_energy_fresh(list(measurement_ids), tiling, extra_ring=1)
        
            current = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)
            if log_cb is not None:
                log_cb(steps=steps, defects=current, target=target_total)
        

    return target_total, current, steps
