#!/usr/bin/env python3
"""
Run config-driven growth experiments with obstacle healing
FIXED VERSION: All critical issues addressed
"""

import json
import toml
from pathlib import Path
import sys
from datetime import datetime
import numpy as np
import traceback

# Add project root
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def short_path(p) -> str:
    p = Path(p)
    try:
        return str(p.resolve().relative_to(PROJECT_ROOT.resolve()))
    except Exception:
        parts = p.parts
        return str(Path(*parts[-4:])) if len(parts) > 4 else str(p)


def load_config(config_path: str = "configs/phase2_experiments.toml") -> dict:
    """Load experiment configuration from TOML"""
    config_path = Path(config_path)
    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, 'r') as f:
        config = toml.load(f)

    # Ensure output directory exists
    output_dir = Path(config.get("project", {}).get("output_dir", "data/growth_experiments"))
    output_dir.mkdir(parents=True, exist_ok=True)

    return config

import re
import shutil

def density_token(d: float) -> str:
    return "d" + f"{d:.3f}".replace(".", "p")

def next_run_id(folder: Path) -> int:
    nums = []
    for p in folder.glob("*_run_*.json"):
        m = re.search(r"_run_(\d+)$", p.stem)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1

def overwrite_latest(run_file: Path, latest_path: Path) -> None:
    shutil.copyfile(run_file, latest_path)

def find_obstacle_file(obstacle_type: str, density: float) -> Path:
    """Find obstacle file with flexible naming"""
    base_path = Path("data/obstacles")

    if not base_path.exists():
        print(f"⚠️  Obstacle directory not found: {base_path}")
        return None

    patterns = [
        f"{obstacle_type}_density_{density}.json",
        f"{obstacle_type}_density_{density:.3f}.json",
        f"{obstacle_type}_density_{str(density).rstrip('0').rstrip('.')}.json"
    ]

    for pattern in patterns:
        file_path = base_path / obstacle_type / pattern
        if file_path.exists():
            return file_path

    try:
        import glob
        pattern = f"{obstacle_type}_density_*.json"
        files = list((base_path / obstacle_type).glob(pattern))

        if files:
            closest = min(files, key=lambda f: abs(float(f.stem.split('_')[-1]) - density))
            print(f"⚠️  Using closest density: {closest.stem.split('_')[-1]} (requested: {density})")
            return closest
    except Exception:
        pass

    return None

def run_growth_experiment(config: dict, experiment_name: str = None):
    """Run a single growth experiment"""

    debug = config.get("debug", {})
    verbosity = int(debug.get("verbosity", 1) or 1)
    verbosity = 2 if verbosity >= 2 else 1

    progress_every = int(debug.get("progress_every", 1) or 1)
    progress_every = max(1, progress_every)

    trace_every = int(debug.get("trace_every", 50) or 50)
    trace_every = max(1, trace_every)

    if verbosity >= 1:
        print("🧪 Running growth experiment...")
        print("=" * 50)
        print(f"🔧 debug: verbosity={verbosity}, progress_every={progress_every}, trace_every={trace_every}")

    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import EnergyParameters, WidomInspiredEnergy
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    from src.simulation.growth_engine import GrowthSimulator

    output_dir = Path(config.get("project", {}).get("output_dir", "data/experiments/growth"))
    output_dir.mkdir(parents=True, exist_ok=True)

    obstacle_type = config["obstacles"]["active_type"]
    density = config["obstacles"]["test_densities"][0]
    dtoken = density_token(density)

    run_id = next_run_id(output_dir)

    if experiment_name is None:
        experiment_name = f"growth_{obstacle_type}_{dtoken}_run_{run_id:03d}"

    print(f"Experiment: {experiment_name}")

    obstacle_type = config["obstacles"]["active_type"]
    density = float(config["obstacles"]["test_densities"][0])

    preferred_base = Path(
        config.get("growth", {}).get(
            "tiling_path",
            "data/processed/penrose_tiling_energy_initialized.json"
        )
    )

    input_tiling_path = None

    def load_json(p: Path) -> dict:
        with open(p, "r") as f:
            return json.load(f)

    base_paths = [
        preferred_base,
        Path("data/processed/penrose_tiling_energy_initialized.json"),
        Path("penrose_tiling_energy_initialized.json"),
    ]

    if density > 0:
        obstacle_file = find_obstacle_file(obstacle_type, density)
        if obstacle_file and obstacle_file.exists():
            print(f"📂 Loading obstacles: {obstacle_file}")
            tiling_data = load_json(obstacle_file)
            input_tiling_path = str(obstacle_file)
        else:
            print(f"⚠️  Obstacle file not found for density {density}, using base tiling")
            for base_path in base_paths:
                if base_path.exists():
                    tiling_data = load_json(base_path)
                    input_tiling_path = str(base_path)
                    break
            else:
                raise FileNotFoundError("Base tiling file not found")
    else:
        for base_path in base_paths:
            if base_path.exists():
                tiling_data = load_json(base_path)
                input_tiling_path = str(base_path)
                break
        else:
            raise FileNotFoundError("Base tiling file not found")

    if verbosity >= 1:
        print("⚙️  Initializing simulation components...")
    classifier = CombinatorialVertexClassifier()

    energy_config = config.get("energy", {})
    energy_params = EnergyParameters(
        high_energy_penalty=energy_config.get("high_energy_penalty", 2.0),
        medium_energy_penalty=energy_config.get("medium_energy_penalty", 1.0),
        low_energy_reference=energy_config.get("low_energy_reference", 0.0),
        neighbor_interaction_strength=energy_config.get("neighbor_interaction_strength", 0.1),
        geometric_strain_penalty=energy_config.get("geometric_strain_penalty", 0.2)
    )
    energy_model = WidomInspiredEnergy(energy_params)

    flip_engine = FlipEngine(classifier, energy_model)

    mc_config = dict(config.get("monte_carlo", {}))
    mc_config["verbosity"] = verbosity
    mc_config["trace_every"] = trace_every

    mc_engine = MonteCarloEngine(
        temperature=mc_config.get("temperature", 1.5),
        energy_model=energy_model,
        flip_engine=flip_engine,
        config=mc_config
    )

    growth_config = config.get("growth", {})
    growth_sim = GrowthSimulator(mc_engine, growth_config)

    window_size = tiling_data.get("window_size", [60.0, 60.0])
    seed_center = [window_size[0] / 2, window_size[1] / 2]
    tiling_data = growth_sim.initialize_seed(tiling_data, seed_center)

    mc_engine.initialize_energy(tiling_data)
    if verbosity >= 1:
        print(f"📊 Initial energy: {mc_engine.current_energy:.2f}")

    growth_steps = growth_config.get("growth_steps", 10)
    if verbosity >= 1:
        print(f"🌱 Running {growth_steps} growth steps...")

    config_path_used = config.get("_meta_config_path", "configs/phase2_experiments.toml")
    growth_cfg = config.get("growth", {})

    experiment_data = {
        "meta": {
            "experiment": "growth",
            "obstacle_type": obstacle_type,
            "density": density,
            "density_token": dtoken,
            "run_id": run_id,
            "input_tiling": input_tiling_path,
            "config": str(config_path_used)
        },
        "params": {
            "growth_steps": growth_steps,
            "mc_steps_per_growth": growth_cfg.get("mc_steps_per_growth"),
            "temperature": config.get("monte_carlo", {}).get("temperature"),
        },
        "metrics": {},
        "series": {
            "growth_steps": []
        }
    }

    for step in range(growth_steps):
        step_num = step + 1
        do_progress_print = (verbosity >= 1) and (
            step_num == 1 or
            step_num == growth_steps or
            (step_num % progress_every == 0)
        )

        if do_progress_print:
            print(f"\n  Step {step_num}/{growth_steps}")

        tiling_data, new_tiles, mc_stats = growth_sim.grow_step(tiling_data, obstacles={})

        step_metrics = {
            "step": step + 1,
            "new_tiles": len(new_tiles),
            "total_energy": mc_engine.current_energy,
            "acceptance_rate": mc_stats.get("acceptance_rate", 0.0),
            "delta_mean": mc_stats.get("delta_mean"),
            "delta_std": mc_stats.get("delta_std"),
            "positive_ratio": mc_stats.get("positive_ratio")
        }

        grown_tiles = [t for t in tiling_data['tiles']
                      if t.get('growth_status') in ['seed', 'grown', 'frontier', 'recently_grown']]
        if grown_tiles:
            defects = sum(1 for t in grown_tiles if t.get('vertex_class') == 'HIGH_ENERGY')
            step_metrics["defect_count"] = defects
            step_metrics["defect_density"] = defects / len(grown_tiles)

        experiment_data["series"]["growth_steps"].append(step_metrics)

        if do_progress_print:
            print(f"    New tiles: {len(new_tiles)}, Defects: {step_metrics.get('defect_count', 0)}")
            print(f"    Acceptance rate: {step_metrics['acceptance_rate']:.1%}")

    series = experiment_data["series"]["growth_steps"]
    last = series[-1] if series else {}

    experiment_data["metrics"] = {
        "final_energy": last.get("total_energy"),
        "defects_end": last.get("defect_count"),
        "defect_density_end": last.get("defect_density"),
        "mean_acceptance_rate": (
            sum(s.get("acceptance_rate", 0.0) for s in series) / len(series)
            if series else None
        ),
        "total_new_tiles": int(sum(s.get("new_tiles", 0) for s in series)) if series else 0
    }

    output_dir.mkdir(parents=True, exist_ok=True)

    experiment_file = output_dir / f"{experiment_name}.json"
    latest_file = output_dir / "latest.json"

    import copy
    save_data = copy.deepcopy(experiment_data)

    def convert_for_json(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {k: convert_for_json(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_for_json(item) for item in obj]
        else:
            return obj

    save_data = convert_for_json(save_data)

    with open(experiment_file, 'w') as f:
        json.dump(save_data, f, indent=2)

    overwrite_latest(experiment_file, latest_file)

    if config.get("metrics", {}).get("save_full_state", False):
        tiling_file = output_dir / f"{experiment_name}_final.json"
        with open(tiling_file, 'w') as f:
            json.dump(tiling_data, f, indent=2)

    if verbosity >= 1:
        print(f"\n✅ Experiment complete!")
    print(f"📊 Results saved to: {short_path(experiment_file)}")

    return experiment_data

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run growth experiment")
    parser.add_argument("--config", "-c", default="configs/phase2_experiments.toml",
                       help="Configuration file path")
    parser.add_argument("--name", "-n", help="Experiment name (optional)")

    args = parser.parse_args()

    try:
        config = load_config(args.config)
        config["_meta_config_path"] = args.config

        results = run_growth_experiment(config, args.name)

        series = results.get("series", {}).get("growth_steps", [])
        print("\n" + "=" * 50)
        print("📈 EXPERIMENT SUMMARY:")
        print(f"  Total steps: {len(series)}")

        if series:
            last_step = series[-1]
            print(f"  Final energy: {last_step.get('total_energy', float('nan')):.2f}")
            if 'defect_density' in last_step:
                print(f"  Final defect density: {last_step['defect_density']:.3f}")

    except Exception as e:
        print(f"❌ Error running experiment: {e}")
        traceback.print_exc()
        sys.exit(1)
