#!/usr/bin/env python3
"""
🚀 MILESTONE 2B: BATCH SIMULATION RUNNER
Systematically runs growth experiments across all generated obstacle densities.

Pipeline:
1. Scan data/obstacles/pores/*.json
2. For each obstacle file:
   a. Load simulation config
   b. Override 'input_tiling' to point to the obstacle file
   c. Run Growth Experiment
   d. Run Forensic Visualization
3. Aggregate results into data/experiments/growth/batch_summary.json
"""

import sys
import json
import time
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import importlib.util
import copy

# Add project root
project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.utils.config import ConfigManager

# --- HELPER: Clean Paths for Display ---
def clean_path(p: Path) -> str:
    try:
        return str(p.relative_to(project_root))
    except ValueError:
        return str(p.name)

# --- DYNAMIC IMPORT HELPER ---
def import_numbered_script(path_from_root, module_name):
    full_path = project_root / path_from_root
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Import logic dynamically
try:
    mod_04 = import_numbered_script("scripts/experiments/04_run_growth.py", "mod_04_growth")
    run_growth_experiment = mod_04.run_growth_experiment
    from scripts.validation.visualize_growth_fidelity import plot_growth_forensics
except ImportError as e:
    print(f"❌ Setup Error: Could not import scripts. {e}")
    sys.exit(1)

def main():
    print("🏭 STARTING PHASE 2 BATCH PRODUCTION")
    print("=" * 60)

    # 1. Setup Directories
    obstacles_dir = project_root / "data" / "obstacles" / "pores"
    output_dir = project_root / "data" / "experiments" / "growth_batch"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Find Targets
    obstacle_files = sorted(list(obstacles_dir.glob("*.json")))
    if not obstacle_files:
        print("❌ No obstacle files found! Run experiments/02_generate_obstacles.py first.")
        sys.exit(1)
        
    print(f"📋 Found {len(obstacle_files)} obstacle configurations.")
    
    # 3. Load Base Config
    config_path = "configs/phase2_experiments.toml"
    base_config = ConfigManager(config_path)
    
    if "metrics" not in base_config._config:
        base_config._config["metrics"] = {}
    base_config._config["metrics"]["save_full_state"] = True

    batch_results = []

    # 4. Batch Loop
    for obs_file in tqdm(obstacle_files, desc="Simulating"):
        density_token = obs_file.stem.split("_")[-1]
        run_name = f"growth_{obs_file.stem}"
        
        tqdm.write(f"🧪 Processing: {clean_path(obs_file)}")
        
        # --- CONFIG OVERRIDE ---
        run_config = copy.deepcopy(base_config._config)
        if "tiling" not in run_config: run_config["tiling"] = {}
        run_config["tiling"]["input_file"] = str(obs_file)
        
        # --- RUN SIMULATION ---
        try:
            start_t = time.time()
            if "monte_carlo" not in run_config: run_config["monte_carlo"] = {}
            run_config["monte_carlo"]["verbosity"] = 0 
            
            result_data = run_growth_experiment(run_config, experiment_name=run_name)
            duration = time.time() - start_t
            
            # --- RUN VISUALIZATION ---
            final_json_path = output_dir / f"{run_name}_final.json"
            if final_json_path.exists():
                viz_path = output_dir / f"{run_name}_forensics.png"
                with open(final_json_path, 'r') as f:
                    final_tiling = json.load(f)
                try:
                    plot_growth_forensics(final_tiling, viz_path)
                except Exception:
                    pass # Squelch viz errors in batch
            
            # --- COLLECT METRICS ---
            metrics = result_data.get("metrics", {})
            try: d_val = float(density_token)
            except ValueError: d_val = 0.0
                
            metrics["density"] = d_val
            metrics["file"] = obs_file.name
            metrics["duration"] = duration
            batch_results.append(metrics)
            
        except Exception as e:
            tqdm.write(f"❌ Failed: {e}")

    # 5. Save Summary
    summary_path = output_dir / "batch_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(batch_results, f, indent=2)
        
    print("\n" + "="*60)
    print("✅ BATCH COMPLETE")
    print(f"📂 Results: {clean_path(output_dir)}")
    print(f"📊 Summary: {clean_path(summary_path)}")
    
    if batch_results:
        df = pd.DataFrame(batch_results)
        cols_to_show = ["density", "defect_density_end", "mean_acceptance_rate"]
        existing_cols = [c for c in cols_to_show if c in df.columns]
        if "density" in existing_cols:
            df = df.sort_values("density")
            print("\n📈 Healing Efficiency vs Density:")
            print(df[existing_cols].to_string(index=False))

if __name__ == "__main__":
    main()