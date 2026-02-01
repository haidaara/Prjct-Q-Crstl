#!/usr/bin/env python3
"""
ENERGY & PHYSICS ENGINE (Phase 2) VALIDATION SCRIPT
Checks:
1) Determinism (fresh model + deep copies)
2) Energy convention (total vs sum of locals)
3) MC drift (internal + ground-truth recompute with fresh model)

"""
import sys
import copy
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling, setup_simulation_components
from src.utils.energy_utils import compute_total_energy_fresh, verify_energy_convention, wipe_all_energy_fields
from src.simulation.mc_engine import MonteCarloEngine


def check_determinism(tiling_data) -> bool:
    print("\n1) Determinism")
    t1 = copy.deepcopy(tiling_data)
    _, m1, _ = setup_simulation_components()
    e1 = compute_total_energy_fresh(m1, t1)

    t2 = copy.deepcopy(tiling_data)
    _, m2, _ = setup_simulation_components()
    e2 = compute_total_energy_fresh(m2, t2)

    drift = abs(e1 - e2)
    if drift < 1e-9:
        print(f"   PASS: deterministic (E={e1:.6f})")
        return True
    print(f"   FAIL: non-deterministic (|Δ|={drift:.9f})")
    return False


def check_convention(tiling_data) -> bool:
    print("\n2) Convention (Total vs Sum(Local))")
    t = copy.deepcopy(tiling_data)
    _, m, _ = setup_simulation_components()
    res = verify_energy_convention(m, t)

    diff = res.get("diff_sum", float("inf"))
    if diff < 1e-6:
        print("   PASS: convention consistent")
        return True
    print(f"   FAIL: convention mismatch (diff_sum={diff:.6f})")
    return False


def check_mc_drift(tiling_data, steps: int = 100) -> bool:
    print("\n3) MC drift (internal + ground truth)")
    t = copy.deepcopy(tiling_data)
    _, energy_model, flip_engine = setup_simulation_components()

    mc = MonteCarloEngine(
        config={
            "temperature": 0.5,
            "base_steps": steps,
            "neighborhood_radius": 3,
            "verify_energy": True,
            "verify_frequency": 0.1,
        },
        energy_model=energy_model,
        flip_engine=flip_engine,
    )
    mc.initialize_energy(t)
    stats = mc.run_sweep(t, steps=steps, debug_mode=True)

    # Ground truth recompute with fresh model (and explicit wipe)
    wipe_all_energy_fields(t)
    _, fresh_model, _ = setup_simulation_components()
    final_actual = compute_total_energy_fresh(fresh_model, t)
    final_drift = abs(final_actual - mc.current_energy)

    internal_max = stats.get("max_drift", stats.get("energy_drift", {}).get("max", 0.0))
    print(f"   MC internal max drift: {internal_max:.6f}")
    print(f"   True final drift:      {final_drift:.6f}")

    if final_drift < 1e-3:
        print("   PASS: drift contained")
        return True
    print("   FAIL: drift detected")
    return False


if __name__ == "__main__":
    print("ENERGY ENGINE VALIDATOR")
    print("=" * 60)

    tiling = load_tiling()
    checks = [check_determinism(tiling), check_convention(tiling), check_mc_drift(tiling, steps=100)]
    if all(checks):
        print("\nALL PHYSICS CHECKS PASSED.")
        sys.exit(0)
    print("\nPHYSICS CHECKS FAILED.")
    sys.exit(1)
