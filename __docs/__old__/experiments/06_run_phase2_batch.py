#!/usr/bin/env python3
"""
🚀 MILESTONE 2B: BATCH SIMULATION RUNNER (FIXED & ROBUST)
Systematically runs growth experiments across all generated obstacle densities.

Pipeline:
1. Scan data/obstacles/pores/*.json
2. For each obstacle file:
   a. Load simulation config
   b. Override 'input_tiling' to point to the obstacle file (TRIPLE INJECTION)
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
import gc

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
    if not full_path.exists():
        return None
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Import the growth runner logic directly
growth_script = import_numbered_script("scripts/experiments/04_run_growth.py", "run_growth")
# Import visualization logic
viz_module = import_numbered_script("scripts/validation/visualize_growth_fidelity.py", "viz_fidelity")

def main():
    print("🚀 BATCH SIMULATION RUNNER: PHASE 2")
    print("=" * 60)
    
    # 1. Setup Paths
    obstacle_dir = project_root / "data" / "obstacles" / "pores"
    output_dir = project_root / "data" / "experiments" / "growth"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Find Obstacle Files
    if not obstacle_dir.exists():
        print(f"❌ Obstacle directory not found: {clean_path(obstacle_dir)}")
        return
        
    obstacle_files = sorted(list(obstacle_dir.glob("*.json")))
    if not obstacle_files:
        print(f"⚠️  No obstacle files found in {clean_path(obstacle_dir)}")
        return
        
    print(f"📂 Found {len(obstacle_files)} obstacle configurations.")
    print(f"📂 Output directory: {clean_path(output_dir)}")
    
    # 3. Load Base Config
    config_path = "configs/phase2_experiments.toml"
    print(f"⚙️  Using base config: {config_path}")
    base_config_manager = ConfigManager(config_path)
    # Access the raw dictionary for copying
    base_config = base_config_manager._config 
    
    # Print the Critical Physics Parameters being used
    mc_cfg = base_config.get("monte_carlo", {})
    print("\n🔬 PHYSICS SETTINGS (Applied to ALL runs):")
    print(f"   • Temperature: {mc_cfg.get('temperature', '???')} (Should be 0.8)")
    print(f"   • Radius:      {mc_cfg.get('neighborhood_radius', '???')}")
    print(f"   • Steps:       {mc_cfg.get('steps_per_growth', '???')}")
    print("-" * 60)

    batch_results = []
    
    # 4. Run Loop
    pbar = tqdm(obstacle_files, desc="Batch Progress", unit="run")
    
    for obs_file in pbar:
        try:
            # Extract density from filename (e.g. "pores_density_0.05.json")
            fname = obs_file.stem 
            parts = fname.split("_")
            
            # Robust Density Parser
            density_val = 0.0
            try:
                # Try the last part (standard naming)
                density_val = float(parts[-1])
            except ValueError:
                # Fallback: Try to find any part that looks like a float
                for p in parts:
                    try:
                        if "." in p:
                            density_val = float(p)
                            break
                    except: continue
            
            density_token = f"d{density_val:.3f}"
            pbar.set_postfix(density=density_token)
            
            # Prepare Run Config
            run_config = copy.deepcopy(base_config)
            
            # --- CRITICAL FIX: TRIPLE PATH INJECTION ---
            # We inject the input path in every place the code might look
            str_obs_path = str(obs_file)
            
            # 1. Tiling section (Primary)
            if "tiling" not in run_config: run_config["tiling"] = {}
            run_config["tiling"]["input_tiling"] = str_obs_path
            
            # 2. Project section (Fallback)
            if "project" not in run_config: run_config["project"] = {}
            run_config["project"]["input_tiling"] = str_obs_path
            
            # 3. Meta section (Safety)
            if "meta" not in run_config: run_config["meta"] = {}
            run_config["meta"]["input_tiling"] = str_obs_path
            # -------------------------------------------

            experiment_name = f"growth_pores_{density_token}_{int(time.time())}"
            
            # Run Growth Experiment
            start_t = time.time()
            
            # Capture stdout to prevent spamming the progress bar
            # (Optional: redirect stdout if desired, but for now we let it print if verbosity is low)
            result_data = growth_script.run_growth_experiment(run_config, experiment_name)
            
            duration = time.time() - start_t
            
            # Forensic Visualization
            # We import the viz script dynamically to use its plotting logic
            viz_path = output_dir / f"{experiment_name}_forensic.png"
            
            if viz_module and hasattr(viz_module, "plot_growth_forensics"):
                # Load the final state file
                final_tiling_path = output_dir / f"{experiment_name}_final.json"
                if final_tiling_path.exists():
                    with open(final_tiling_path, 'r') as f:
                        final_tiling = json.load(f)
                    try:
                        viz_module.plot_growth_forensics(final_tiling, str(viz_path))
                    except Exception as e:
                        # Don't crash batch on plotting error
                        pass 
            
            # Collect Metrics
            metrics = result_data.get("metrics", {})
            metrics["density"] = density_val
            metrics["file"] = obs_file.name
            metrics["duration"] = duration
            
            # Add Key Physics Outcomes
            steps = result_data.get("series", {}).get("growth_steps", [])
            if steps:
                metrics["final_energy"] = steps[-1].get("total_energy", 0.0)
                metrics["defects_end"] = steps[-1].get("defect_count", 0)
            
            batch_results.append(metrics)
            
            # Garbage Collection to keep memory clean
            del result_data
            del steps
            gc.collect()
            
        except Exception as e:
            tqdm.write(f"❌ Failed processing {obs_file.name}: {e}")
            import traceback
            traceback.print_exc()

    # 5. Save Summary
    summary_path = output_dir / "batch_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(batch_results, f, indent=2)
        
    print("\n" + "="*60)
    print("✅ BATCH COMPLETE")
    print(f"📂 Results: {clean_path(output_dir)}")
    print(f"📊 Summary: {clean_path(summary_path)}")
    
    if batch_results:
        try:
            df = pd.DataFrame(batch_results)
            cols_to_show = ["density", "defects_end", "mean_acceptance_rate"]
            existing_cols = [c for c in cols_to_show if c in df.columns]
            print("\nSnapshot:")
            print(df[existing_cols].head(10))
        except ImportError:
            pass

if __name__ == "__main__":
    main()