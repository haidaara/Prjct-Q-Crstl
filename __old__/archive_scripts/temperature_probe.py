#!/usr/bin/env python3
"""Temperature probe (small sweep from same initial state).

Use when you want to confirm temperature affects acceptance/energy trend
without running the full experiment suite.
"""
import sys
import copy
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling, setup_simulation_components
from src.simulation.mc_engine import MonteCarloEngine


def run_at_temperature(base_tiling, T: float, steps: int):
    t = copy.deepcopy(base_tiling)
    _, energy_model, flip_engine = setup_simulation_components()

    # Make all tiles flippable (probe should not be constrained by growth rules)
    for tile in t["tiles"]:
        if not tile.get("removed", False):
            tile["flippable"] = True

    mc = MonteCarloEngine(
        config={"temperature": T, "base_steps": steps, "neighborhood_radius": 3, "verify_energy": False},
        energy_model=energy_model,
        flip_engine=flip_engine,
    )
    mc.initialize_energy(t)
    stats = mc.run_sweep(t, steps=steps)
    return {
        "T": T,
        "acceptance_rate": stats.get("acceptance_rate", 0.0),
        "energy_final": stats.get("energy_final", mc.current_energy),
        "max_drift": stats.get("max_drift", 0.0),
    }


def main() -> int:
    print("🌡️  TEMPERATURE PROBE")
    print("=" * 60)

    base = load_tiling()

    temps = [0.05, 0.1, 0.2, 0.5, 1.0]
    steps = 80

    rows = []
    for T in temps:
        r = run_at_temperature(base, T, steps)
        rows.append(r)
        print(f"T={T:>5.2f} | acc={r['acceptance_rate']:.3f} | E_final={r['energy_final']:.3f} | drift={r['max_drift']:.6f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
