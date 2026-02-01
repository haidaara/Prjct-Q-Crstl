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

    log(f"  Creating {num_defects} defects (Strict Mode)...", 1)

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

    log(f"  Created {created} defects.", 1)
    return active_ids


def run_experiment():
    print(" EXPERIMENT 03: PHASON HEALING (Refactored)")
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
    
    # FIX: Create Run Directory IMMEDIATELY
    output_dir_base = Path(healing.get("output_dir", "data/experiments/healing"))
    output_dir_base.mkdir(parents=True, exist_ok=True)

    # Calculate Run ID and Create Folder
    run_id = _next_run_id(output_dir_base, f"healing_{scenario}")
    run_dir = output_dir_base / f"healing_{scenario}_run_{run_id:03d}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # Point output_dir to the specific run folder
    output_dir = str(run_dir)

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
    log(f" Input tiling: {tiling_path}", 1)
    log(f" Output dir : {output_dir}", 1)
    log(f"  scenario={scenario} seed_radius={seed_radius} num_defects={num_defects} defect_threshold={defect_threshold}", 1)
    log(f"  MC: T={temperature} steps={total_steps} R={neighborhood_radius} verify_energy={verify_energy} base_steps={base_steps}", 1)
    log("-" * 60, 1)

    tiling = load_tiling(tiling_path)
    classifier, energy_model, flip_engine = setup_simulation_components(str(cfg.config_path))

    initialize_seed_region(tiling, seed_radius=seed_radius, set_flippable=True)
    
    # Healing uses growth_status only as an "active region" marker.
    # IMPORTANT: reserve "ungrown" for true vacuum in growth runs.
    for tile in tiling["tiles"]:
        if tile.get("removed", False):
            continue
        if tile.get("growth_status") == "ungrown":
            tile["growth_status"] = "frozen"   # or "grown" (any non-"ungrown" label is fine)


    # ======================================================================
    # PHASE 1: DAMAGE INJECTION (Two-Engine Protocol)
    # Goal: Use High-T Engine to scramble, then switch to Low-T Engie.
    # ======================================================================
    
    # 1. Setup DAMAGE Engine (High Temperature)
    # We use a specific High-T engine just for scrambling.
    T_damage = 5.0
    mc_damage = MonteCarloEngine(
        temperature=T_damage, 
        energy_model=energy_model,
        flip_engine=flip_engine,
        config={
            "temperature": T_damage,
            "base_steps": base_steps,
            "neighborhood_radius": neighborhood_radius,
            "verify_energy": verify_energy,
            "verbosity": 0, # Quiet during damage
        },
    )
    mc_damage.initialize_energy(tiling)

    start_defects = 0
    damage_steps = 0
    check_interval = 50 # Check every 50 steps to save time
    baseline_defects = start_defects
    target_defects = baseline_defects + num_defects

    log(f" DAMAGE PHASE: Heating (T={T_damage}) to create {target_defects} energetic defects...", 1)
    

    
    
    
    # 2. Run Damage Loop
    while start_defects < target_defects and damage_steps < 3000:
        # Run a burst of steps
        mc_damage.run_sweep(tiling, steps=check_interval) 
        damage_steps += check_interval
        

        
        # Check progress (Metric: High Energy Tiles)
        start_defects = sum(
            1 for t in tiling["tiles"]
            if t.get("flippable", False)
            and t.get("local_energy", 0.0) > defect_threshold
            and not t.get("is_boundary", False)   # bulk-only for “healable” defects
        )
                        
        # Wipe energy fields 
        wipe_all_energy_fields(tiling)
        clear_all_caches(energy_model)
        # --------------------------------------------------

        log(f"   Heating Step {damage_steps}: High-Energy Tiles={start_defects} (Target: {target_defects})", 1)
    if start_defects == 0:
        log(" CRITICAL ERROR: High-T Damage Phase failed. System is still perfect.", 1)
        sys.exit(1)
        
    log(f"  DAMAGE COMPLETE: Scrambled. Starting Count: {start_defects} Defects.", 1)

# 3. Snapshot ("The Before Picture")
    timestamp = int(time.time())
    snapshot_filename = f"healing_damaged_state_{timestamp}.json"
    damaged_snapshot_path = run_dir / snapshot_filename
    # Folder already created at start
    
    try:
        # Compute energy so we can visualize the damage
        energy_model.update_tiling_energy(tiling) 
        
        tiling["adjacency_graph"] = {
            str(t["id"]): list(t.get("neighbors", [])) for t in tiling.get("tiles", [])
        }


        with open(damaged_snapshot_path, 'w') as f:
            json.dump(tiling, f, indent=2)

        log(f" SNAPSHOT SAVED: {damaged_snapshot_path}", 1)
    except Exception as e:
        log(f" Could not save snapshot: {e}", 1)

    # ======================================================================
    #  PHASE 2: HEALING (ROBUST ANNEALING)
    # Goal: Continuous cooling from 5.0 -> 0.05 with smart step allocation.
    # ======================================================================
    
    # 1. Load & Validate Schedule
    default_schedule = [5.0, 2.5, 1.2, 0.6, 0.3, 0.15, 0.05]
    raw_schedule = healing.get("annealing_schedule", default_schedule)
    
    # Ensure list of floats
    annealing_schedule = [float(t) for t in raw_schedule]

    # Validation: Prevent configuration errors
    if not annealing_schedule:
        raise ValueError(" Config Error: annealing_schedule cannot be empty.")
    if any(t <= 0.0 for t in annealing_schedule):
        raise ValueError(f" Config Error: All temperatures must be > 0. Got: {annealing_schedule}")
    
    nT = len(annealing_schedule)

    # 2. Robust Step Allocation (Handle remainders & small budgets)
    # If we have fewer steps than stages, compress the schedule
    if total_steps < nT:
        log(f" Total steps ({total_steps}) < Stages ({nT}). Compressing schedule.", 1)
        # Pick indices evenly spaced
        idxs = [int(round(i * (nT - 1) / max(1, total_steps - 1))) for i in range(total_steps)]
        annealing_schedule = [annealing_schedule[i] for i in idxs]
        nT = len(annealing_schedule)

    # Distribute steps: base amount + remainder distributed to first few stages
    base_steps_per_stage = total_steps // nT
    remainder = total_steps % nT
    stage_steps_list = [base_steps_per_stage + (1 if i < remainder else 0) for i in range(nT)]

    log(f" SWITCHING TO ANNEALING: {nT} Stages", 1)
    log(f"   Schedule: {annealing_schedule}", 1)
    log(f"   Allocation: {stage_steps_list} steps/stage", 1)

    t0 = time.time()
    accepted_total = 0
    max_drift = 0.0
    global_step = 0
    
    snapshot_interval = 50
    next_snapshot = snapshot_interval

    # 3. The Annealing Loop
    for stage_idx, current_temp in enumerate(annealing_schedule):
        steps_this_stage = stage_steps_list[stage_idx]
        if steps_this_stage <= 0: continue

        log(f"\n STAGE {stage_idx+1}/{nT}: Cooling to T={current_temp} ({steps_this_stage} steps)...", 1)
        
        # Create fresh engine for this temperature
        mc_heal = MonteCarloEngine(
            temperature=current_temp,
            energy_model=energy_model,
            flip_engine=flip_engine,
            config={
                "temperature": current_temp,
                "base_steps": 100,
                "neighborhood_radius": neighborhood_radius,
                "verify_energy": verify_energy,
                "verbosity": verbosity,
            },
        )
        mc_heal.initialize_energy(tiling)

        stage_done = 0
        stage_accepted = 0
        
        while stage_done < steps_this_stage:
            # Calculate chunk size (don't over-run stage or global limits)
            chunk_size = min(progress_every, snapshot_interval, steps_this_stage - stage_done)
            if chunk_size <= 0: break 
            
            stats = mc_heal.run_sweep(tiling, steps=chunk_size)
            
            n_acc = int(stats.get("accepted", 0))
            accepted_total += n_acc
            stage_accepted += n_acc
            max_drift = max(max_drift, float(stats.get("max_drift", 0.0)))
            
            stage_done += chunk_size
            global_step += chunk_size

            # --- Early Exit Optimization ---
            # If in the deep freeze (lowest T) and nothing is moving, stop wasting CPU.
            if current_temp == annealing_schedule[-1] and stage_done > 100 and stage_accepted == 0:
                log("  Deep Freeze detected (0 moves). Exiting stage early.", 1)
                # Fast-forward global counter to keep logs consistent
                global_step += (steps_this_stage - stage_done)
                break

            # --- Robust Snapshotting ---
            if global_step >= next_snapshot:
                snap_name = f"healing_step_{global_step:04d}.json"
                snap_path = run_dir / snap_name
                try:
                    #  energy fields so snapshot is physically truthful
                    # (Snapshot should reflect the state of the system, not just geometry)
                    energy_model.update_tiling_energy(tiling)

                    tiling["adjacency_graph"] = {
                        str(t["id"]): list(t.get("neighbors", [])) for t in tiling.get("tiles", [])
                    }

                    with open(snap_path, 'w') as f:
                        json.dump(tiling, f)
                    log(f"   Snapshot: {snap_name} (T={current_temp})", 1)
                except Exception as e:
                    log(f"   Snapshot failed: {e}", 1)
                next_snapshot += snapshot_interval

            # Log Progress
            log(
                f"   Global {global_step}/{total_steps} | Stage {stage_done}/{steps_this_stage} | "
                f"T={current_temp} | Acc={n_acc}", 
                1
            )
    # ======================================================================
    #  PHASE 3: RESULTS ANALYSIS
    # ======================================================================
    
    # 1. Final Defect Count (FIXED: Scan all tiles, no 'active_ids')
    wipe_all_energy_fields(tiling)
    clear_all_caches(energy_model)
    
    # (active-only, consistent with start_defects)
    defects_end = sum(
        1 for t in tiling["tiles"]
        if t.get("flippable", False) and energy_model.compute_local_energy(t["id"], tiling) > defect_threshold
    )

    # 2. Link Start Variable
    # We use 'start_defects' which we calculated in Phase 1
    defects_start = start_defects 

    log("-" * 60, 1)
    eff = (defects_start - defects_end) / max(1, defects_start)
    log(f"RESULTS: {defects_start} -> {defects_end} (Efficiency: {eff:.1%})", 1)
    log(f"Drift: {max_drift:.6f}\n", 1)


    # Save results
    # run_dir and run_id were created at start
    run_path = run_dir / f"healing_{scenario}_run_{run_id:03d}.json"
    latest_path = output_dir_base / "latest.json"

    dt = time.time() - t0
    acceptance_rate = (accepted_total / total_steps) if total_steps > 0 else 0.0

    # FIX: Regenerate Adjacency Graph from Tile Neighbors to prevent staleness
    tiling["adjacency_graph"] = {
        str(t["id"]): list(t.get("neighbors", [])) for t in tiling.get("tiles", [])
    }

    

    payload = {
        "meta": {
            "phase": "phase1_healing",
            "scenario": scenario,
            "input_tiling": tiling_path,
            "output_dir": output_dir,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "obstacle_density": 0.0, # Placeholder for Viz Title
            "temperature": temperature,
            "steps": total_steps
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
        },
        "results": {
            "defects_start": defects_start,
            "defects_end": defects_end,
            "efficiency": eff,
            "accepted": accepted_total,
            "acceptance_rate": acceptance_rate, # Fixed variable name
            "max_drift": max_drift,
            "runtime_s": dt,                    # Fixed variable name
        },
        # CRITICAL: Save Geometry for Visualization
        "tiles": tiling["tiles"],
        "adjacency_graph": tiling["adjacency_graph"],
        "obstacle_metadata": tiling.get("obstacle_metadata", {})
    }

    
    # 1. Save Full State (Geometry + Metrics) -> For Visualization
    # 'run_path' is the heavy file
    with open(run_path, "w") as f:
        json.dump(payload, f, indent=2)

    # 2. Save Summary (Metrics Only) -> For Quick Analysis
    # Create a lightweight copy by removing heavy geometry arrays
    summary_payload = copy.deepcopy(payload)
    summary_payload.pop("tiles", None)
    summary_payload.pop("adjacency_graph", None)
    summary_payload.pop("obstacle_metadata", None)
    
    summary_path = run_dir / f"healing_{scenario}_run_{run_id:03d}_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary_payload, f, indent=2)

    # 3. Update Latest (Point to Full State)
    with open(latest_path, "w") as f:
        json.dump(payload, f, indent=2)

    log(f"💾 Saved Full State: {run_path.name} (for viz)", 1)
    log(f"📄 Saved Summary   : {summary_path.name} (for stats)", 1)
    log(f"📌 Latest: {latest_path.as_posix()}", 1)


if __name__ == "__main__":
    run_experiment()
