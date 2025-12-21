#!/usr/bin/env python3
"""
Experiment 03: Run Healing Test
Refactored and enhanced healing experiment script.

"""

import sys
import json
import time
import copy
from pathlib import Path

import numpy as np

# Add project root
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from src.utils.config import ConfigManager
from src.utils.script_utils import load_tiling, setup_simulation_components, initialize_seed_region
from src.utils.energy_utils import wipe_all_energy_fields, clear_all_caches
from src.simulation.mc_engine import MonteCarloEngine


def _make_logger(verbosity: int):
    def log(msg: str, level: int = 1):
        if verbosity >= level:
            print(msg, flush=True)
    return log


def _next_run_id(out_dir: Path, prefix: str) -> int:
    existing = sorted(out_dir.glob(f"{prefix}_run_*.json"))
    if not existing:
        return 1
    nums = []
    for p in existing:
        try:
            nums.append(int(p.stem.split("_run_")[-1]))
        except Exception:
            pass
    return (max(nums) + 1) if nums else 1


def create_defects_strictly(tiling_data, energy_model, flip_engine, num_defects=10, log=None):
    log = log or (lambda *a, **k: None)

    log(f"  🔨 Creating {num_defects} defects (Strict Mode)...", 1)

    active_ids = {t["id"] for t in tiling_data["tiles"] if t.get("growth_status") == "seed"}

    for tile in tiling_data["tiles"]:
        tile["flippable"] = (tile["id"] in active_ids) and not tile.get("removed", False)

    hexagons = flip_engine.find_flippable_hexagons(tiling_data)
    active_hexagons = [h for h in hexagons if all(tid in active_ids for tid in h)]

    import random
    random.shuffle(active_hexagons)

    created = 0
    for hexagon in active_hexagons:
        if created >= num_defects:
            break

        region = flip_engine._get_k_ring_neighborhood(hexagon, tiling_data, k=4)

        # Pre-wipe
        for tid in region:
            tiling_data["tiles"][tid].pop("local_energy", None)
            tiling_data["tiles"][tid].pop("vertex_class", None)
        clear_all_caches(energy_model)

        # Calc Before
        e_before = sum(
            energy_model.compute_local_energy(tid, tiling_data)
            for tid in region
            if not tiling_data["tiles"][tid].get("removed")
        )

        undo = flip_engine.capture_state(list(region), tiling_data)
        if flip_engine.apply_flip(hexagon, tiling_data):
            # Post-wipe
            for tid in region:
                tiling_data["tiles"][tid].pop("local_energy", None)
                tiling_data["tiles"][tid].pop("vertex_class", None)
            clear_all_caches(energy_model)

            # Calc After
            e_after = sum(
                energy_model.compute_local_energy(tid, tiling_data)
                for tid in region
                if not tiling_data["tiles"][tid].get("removed")
            )

            if e_after > e_before + 0.1:
                created += 1
            else:
                flip_engine.restore_state(undo, tiling_data)
                for tid in region:
                    tiling_data["tiles"][tid].pop("local_energy", None)
                    tiling_data["tiles"][tid].pop("vertex_class", None)
        else:
            flip_engine.restore_state(undo, tiling_data)

    log(f"  ✅ Created {created} defects.", 1)
    return active_ids


def run_experiment():
    print("🧪 EXPERIMENT 03: PHASON HEALING (Refactored)")
    print("=" * 60)

    cfg = ConfigManager("configs/phase2_experiments.toml")

    # ConfigManager stores the merged TOML in cfg._config

    cfg_dict = getattr(cfg, "_config", {})  # raw dict of all sections
    # Use the official properties for sections that exist as properties
    energy_cfg = cfg.energy
    mc_cfg = cfg.monte_carlo
    # Sections that don't have dedicated properties (like healing/debug) read from cfg_dict
    healing = cfg_dict.get("healing", {})
    debug = cfg_dict.get("debug", {})


    # Verbosity: only 1 or 2 (no 0)
    verbosity = int(debug.get("verbosity", 1))
    # Allow CLI override: --verbosity 1|2
    if "--verbosity" in sys.argv:
        try:
            i = sys.argv.index("--verbosity")
            verbosity = int(sys.argv[i + 1])
        except Exception:
            pass
    verbosity = 2 if verbosity >= 2 else 1

    progress_every = int(debug.get("progress_every", 500))
    trace_every = int(debug.get("trace_every", 50))
    trace_every = max(1, trace_every)  # safety

    log = _make_logger(verbosity)

    scenario = str(healing.get("scenario", "base"))
    tiling_path = str(healing.get("tiling_path", "data/processed/penrose_tiling_energy_initialized.json"))
    output_dir = str(healing.get("output_dir", "data/experiments/healing"))

    seed_radius = float(healing.get("seed_radius", 10.0))
    num_defects = int(healing.get("num_defects", 15))
    defect_threshold = float(healing.get("defect_threshold", 1.5))

    temperature = float(mc_cfg.get("temperature", 0.1))
    base_steps = int(mc_cfg.get("base_steps", 100))
    neighborhood_radius = int(mc_cfg.get("neighborhood_radius", 3))
    verify_energy = bool(mc_cfg.get("verify_energy", False))

    # Total steps: prefer healing.sweep_steps if present, otherwise monte_carlo.steps, otherwise base_steps
    total_steps = int(healing.get("sweep_steps", mc_cfg.get("steps", base_steps)))

    # Output header (verbosity 1+)
    log(f"📥 Input tiling: {tiling_path}", 1)
    log(f"📤 Output dir : {output_dir}", 1)
    log(f"⚙️  scenario={scenario} seed_radius={seed_radius} num_defects={num_defects} defect_threshold={defect_threshold}", 1)
    log(f"⚙️  MC: T={temperature} steps={total_steps} R={neighborhood_radius} verify_energy={verify_energy} base_steps={base_steps}", 1)
    log("-" * 60, 1)

    tiling = load_tiling(tiling_path)
    classifier, energy_model, flip_engine = setup_simulation_components(str(cfg.config_path))


    initialize_seed_region(tiling, seed_radius=seed_radius, set_flippable=True)

    active_ids = create_defects_strictly(
        tiling, energy_model, flip_engine,
        num_defects=num_defects,
        log=log
    )

    # Initial defect count
    wipe_all_energy_fields(tiling)
    clear_all_caches(energy_model)
    defects_start = sum(
        1 for tid in active_ids
        if energy_model.compute_local_energy(tid, tiling) > defect_threshold
    )
    log(f"  Initial Defects: {defects_start}", 1)

    # MC engine
    mc = MonteCarloEngine(
        temperature=temperature,
        energy_model=energy_model,
        flip_engine=flip_engine,
        config={
            "temperature": temperature,
            "base_steps": base_steps,
            "neighborhood_radius": neighborhood_radius,
            "verify_energy": verify_energy,
            "verbosity": verbosity,
            "trace_every": trace_every,

        },
    )
    mc.initialize_energy(tiling)

    log("🎲 Starting Monte Carlo...", 1)
    t0 = time.time()

    accepted_total = 0
    max_drift = 0.0
    done = 0

    while done < total_steps:
        chunk = min(progress_every, total_steps - done)
        stats = mc.run_sweep(tiling, steps=chunk)
        accepted_total += int(stats.get("accepted", 0))
        max_drift = max(max_drift, float(stats.get("max_drift", 0.0)))
        done += chunk

        log(
            f"  ⏳ MC progress: {done}/{total_steps} ({100.0*done/max(1,total_steps):.1f}%) "
            f"| accepted={accepted_total} | max_drift={max_drift:.6f}",
            1
        )

    dt = time.time() - t0
    acceptance = accepted_total / max(1, total_steps)
    log(f"✅ MC finished in {dt:.2f}s | acceptance={acceptance:.1%} | max_drift={max_drift:.6f}", 1)

    # Final defect count
    wipe_all_energy_fields(tiling)
    clear_all_caches(energy_model)
    defects_end = sum(
        1 for tid in active_ids
        if energy_model.compute_local_energy(tid, tiling) > defect_threshold
    )

    log("-" * 60, 1)
    eff = (defects_start - defects_end) / max(1, defects_start)
    log(f"RESULTS: {defects_start} -> {defects_end} (Efficiency: {eff:.1%})", 1)
    log(f"Drift: {max_drift:.6f}\n", 1)

    # Save results
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    run_id = _next_run_id(out_dir, f"healing_{scenario}")
    run_path = out_dir / f"healing_{scenario}_run_{run_id:03d}.json"
    latest_path = out_dir / "latest.json"

    payload = {
        "meta": {
            "phase": "phase1_healing",
            "scenario": scenario,
            "input_tiling": tiling_path,
            "output_dir": output_dir,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "config": {
            "seed_radius": seed_radius,
            "num_defects": num_defects,
            "defect_threshold": defect_threshold,
            "monte_carlo": {
                "temperature": temperature,
                "steps": total_steps,
                "base_steps": base_steps,
                "neighborhood_radius": neighborhood_radius,
                "verify_energy": verify_energy,
            },
            "verbosity": verbosity,
            "progress_every": progress_every,
            "trace_every": trace_every,

        },
        "results": {
            "defects_start": defects_start,
            "defects_end": defects_end,
            "efficiency": eff,
            "accepted": accepted_total,
            "acceptance_rate": acceptance,
            "max_drift": max_drift,
            "runtime_s": dt,
        },
    }

    with open(run_path, "w") as f:
        json.dump(payload, f, indent=2)

    with open(latest_path, "w") as f:
        json.dump(payload, f, indent=2)

    log(f"💾 Saved: {run_path.as_posix()}", 1)
    log(f"📌 Latest: {latest_path.as_posix()}", 1)


if __name__ == "__main__":
    run_experiment()
