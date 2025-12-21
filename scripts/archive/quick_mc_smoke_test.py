#!/usr/bin/env python3
"""Quick MC smoke test.

Runs a short MC sweep and prints acceptance/drift.
Use when you want to confirm the MC loop works end-to-end.
"""
import sys
import copy
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling, setup_simulation_components
from src.utils.energy_utils import compute_total_energy_fresh, wipe_all_energy_fields, clear_all_caches
from src.simulation.mc_engine import MonteCarloEngine


def main(steps: int = 50, temperature: float = 0.3) -> int:
    print("🏃 QUICK MC SMOKE TEST")
    print("=" * 60)

    tiling = load_tiling()
    t = copy.deepcopy(tiling)

    _, energy_model, flip_engine = setup_simulation_components()

    # Ensure MC has moves (make everything flippable)
    for tile in t["tiles"]:
        if not tile.get("removed", False):
            tile["flippable"] = True

    mc = MonteCarloEngine(
        config={
            "temperature": temperature,
            "base_steps": steps,
            "neighborhood_radius": 3,
            "verify_energy": True,
            "verify_frequency": 0.2,
        },
        energy_model=energy_model,
        flip_engine=flip_engine,
    )

    mc.initialize_energy(t)
    stats = mc.run_sweep(t, steps=steps, debug_mode=True)

    # Ground truth recompute
    wipe_all_energy_fields(t)
    clear_all_caches(energy_model)
    gt = compute_total_energy_fresh(energy_model, t)
    drift = abs(gt - mc.current_energy)

    internal_max = stats.get("max_drift", stats.get("energy_drift", {}).get("max", 0.0))
    accepted = stats.get("acceptance_rate", 0.0)

    print("-" * 60)
    print(f"T={temperature} | steps={steps}")
    print(f"Acceptance rate: {accepted:.3f}")
    print(f"Internal max drift: {internal_max:.6f}")
    print(f"GT final drift:     {drift:.6f}")

    return 0 if drift < 1e-3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
