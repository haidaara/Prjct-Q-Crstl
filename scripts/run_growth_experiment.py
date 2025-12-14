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

def load_config(config_path: str = "configs/phase2_growth_experiments.toml") -> dict:
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

def find_obstacle_file(obstacle_type: str, density: float) -> Path:
    """Find obstacle file with flexible naming"""
    base_path = Path("data/obstacles")
    
    if not base_path.exists():
        print(f"⚠️  Obstacle directory not found: {base_path}")
        return None
    
    # Try multiple naming patterns
    patterns = [
        f"{obstacle_type}_density_{density}.json",
        f"{obstacle_type}_density_{density:.3f}.json",
        f"{obstacle_type}_density_{str(density).rstrip('0').rstrip('.')}.json"
    ]
    
    for pattern in patterns:
        file_path = base_path / obstacle_type / pattern
        if file_path.exists():
            return file_path
    
    # Try glob pattern as fallback
    try:
        import glob
        pattern = f"{obstacle_type}_density_*.json"
        files = list((base_path / obstacle_type).glob(pattern))
        
        if files:
            # Find closest density
            closest = min(files, key=lambda f: abs(float(f.stem.split('_')[-1]) - density))
            print(f"⚠️  Using closest density: {closest.stem.split('_')[-1]} (requested: {density})")
            return closest
    except Exception:
        pass
    
    return None

def run_growth_experiment(config: dict, experiment_name: str = None):
    """Run a single growth experiment"""
    print("🧪 Running growth experiment...")
    print("=" * 50)
    
    # Setup imports
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import EnergyParameters, WidomInspiredEnergy
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    from src.simulation.growth_engine import GrowthSimulator
    
    # Experiment timestamp
    if experiment_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        obstacle_type = config["obstacles"]["active_type"]
        density = config["obstacles"]["test_densities"][0]
        experiment_name = f"{obstacle_type}_{density}_{timestamp}"
    
    print(f"Experiment: {experiment_name}")
    
    # Load tiling data (with or without obstacles)
    obstacle_type = config["obstacles"]["active_type"]
    density = config["obstacles"]["test_densities"][0]
    
    if density > 0:
        obstacle_file = find_obstacle_file(obstacle_type, density)
        if obstacle_file and obstacle_file.exists():
            print(f"📂 Loading obstacles: {obstacle_file}")
            with open(obstacle_file, 'r') as f:
                tiling_data = json.load(f)
        else:
            print(f"⚠️  Obstacle file not found for density {density}, using base tiling")
            # Fall back to base tiling
            base_paths = [
                Path("data/processed/penrose_tiling_energy_initialized.json"),
                Path("penrose_tiling_energy_initialized.json")
            ]
            for base_path in base_paths:
                if base_path.exists():
                    with open(base_path, 'r') as f:
                        tiling_data = json.load(f)
                    break
            else:
                raise FileNotFoundError("Base tiling file not found")
    else:
        # No obstacles requested
        base_paths = [
            Path("data/processed/penrose_tiling_energy_initialized.json"),
            Path("penrose_tiling_energy_initialized.json")
        ]
        for base_path in base_paths:
            if base_path.exists():
                with open(base_path, 'r') as f:
                    tiling_data = json.load(f)
                break
        else:
            raise FileNotFoundError("Base tiling file not found")
    
    # Initialize simulation components
    print("⚙️  Initializing simulation components...")
    classifier = CombinatorialVertexClassifier()
    
    # Wire energy parameters from config (CRITICAL FIX)
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
    
    # Create MC engine with config
    mc_config = config.get("monte_carlo", {})
    mc_engine = MonteCarloEngine(
        temperature=mc_config.get("temperature", 1.5),
        energy_model=energy_model,
        flip_engine=flip_engine,
        config=mc_config
    )
    
    # Create growth simulator with config
    growth_config = config.get("growth", {})
    growth_sim = GrowthSimulator(mc_engine, growth_config)
    
    # Initialize seed
    window_size = tiling_data.get("window_size", [60.0, 60.0])
    seed_center = [window_size[0] / 2, window_size[1] / 2]
    tiling_data = growth_sim.initialize_seed(tiling_data, seed_center)
    
    # Initialize MC energy (CRITICAL FIX)
    mc_engine.initialize_energy(tiling_data)
    print(f"📊 Initial energy: {mc_engine.current_energy:.2f}")
    
    # Run growth steps
    growth_steps = growth_config.get("growth_steps", 10)
    print(f"🌱 Running {growth_steps} growth steps...")
    
    experiment_data = {
        "experiment_name": experiment_name,
        "config": config,
        "growth_steps": [],
        "final_tiling": None
    }
    
    for step in range(growth_steps):
        print(f"\n  Step {step + 1}/{growth_steps}")
        
        # Grow one step
        tiling_data, new_tiles, mc_stats = growth_sim.grow_step(tiling_data, obstacles={})
        
        # Collect metrics
        step_metrics = {
            "step": step + 1,
            "new_tiles": len(new_tiles),
            "total_energy": mc_engine.current_energy,
            "acceptance_rate": mc_stats.get("acceptance_rate", 0.0),
            "delta_mean": mc_stats.get("delta_mean"),
            "delta_std": mc_stats.get("delta_std"),
            "positive_ratio": mc_stats.get("positive_ratio")
        }
        
        # Count defects in grown region
        grown_tiles = [t for t in tiling_data['tiles'] 
                      if t.get('growth_status') in ['seed', 'grown', 'frontier', 'recently_grown']]
        if grown_tiles:
            defects = sum(1 for t in grown_tiles if t.get('vertex_class') == 'HIGH_ENERGY')
            step_metrics["defect_count"] = defects
            step_metrics["defect_density"] = defects / len(grown_tiles)
        
        experiment_data["growth_steps"].append(step_metrics)
        
        print(f"    New tiles: {len(new_tiles)}, Defects: {step_metrics.get('defect_count', 0)}")
        print(f"    Acceptance rate: {step_metrics['acceptance_rate']:.1%}")
    
    # Save results
    output_dir = Path(config["project"]["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save experiment data
    experiment_file = output_dir / f"{experiment_name}.json"
    
    # Prepare data for JSON serialization
    import copy
    save_data = copy.deepcopy(experiment_data)
    
    # Convert numpy types and other non-serializable types
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
    
    # Save final tiling state (optional)
    if config.get("metrics", {}).get("save_full_state", False):
        tiling_file = output_dir / f"{experiment_name}_final.json"
        with open(tiling_file, 'w') as f:
            json.dump(tiling_data, f, indent=2)
    
    print(f"\n✅ Experiment complete!")
    print(f"📊 Results saved to: {experiment_file}")
    
    return experiment_data

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run growth experiment")
    parser.add_argument("--config", "-c", default="configs/phase2_growth_experiments.toml",
                       help="Configuration file path")
    parser.add_argument("--name", "-n", help="Experiment name (optional)")
    
    args = parser.parse_args()
    
    try:
        config = load_config(args.config)
        results = run_growth_experiment(config, args.name)
        
        # Quick summary
        print("\n" + "=" * 50)
        print("📈 EXPERIMENT SUMMARY:")
        print(f"  Total steps: {len(results['growth_steps'])}")
        if results['growth_steps']:
            last_step = results['growth_steps'][-1]
            print(f"  Final energy: {last_step['total_energy']:.2f}")
            if 'defect_density' in last_step:
                print(f"  Final defect density: {last_step['defect_density']:.3f}")
        
    except Exception as e:
        print(f"❌ Error running experiment: {e}")
        traceback.print_exc()
        sys.exit(1)