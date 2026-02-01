"""
MILESTONE 2A: HIGH-PERFORMANCE OBSTACLE CREATION PIPELINE
"""

import sys
import os
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]   # .../quasi-phason
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.utils.config import ConfigManager
from src.obstacle.obstacle_creator import ObstacleCreator, ObstacleSpec, adjacency_intkeys_to_str
from src.obstacle.obstacle_config import ObstacleConfig
from src.obstacle.obstacle_visualizer import ObstacleVisualizer
import json

import time


def main():
    start_time = time.time()
    
    print("MILESTONE 2A: OBSTACLE CREATION PIPELINE")
    print("=" * 60)
    
    # Load configuration
    config = ConfigManager("configs/phase2_experiments.toml")
    print(f"Using config: {config.config_path}")
    
    # Setup output directory structure
    output_dir = setup_output_directory()
    
    # Check if output directory already has data
    existing_files = list(output_dir.glob("**/*.json"))
    if existing_files:
        print(f"\nWARNING: {output_dir} already contains {len(existing_files)} JSON files")
        print("   This will overwrite existing obstacle configurations")
        print("   Run: python src/utils/archive_obstacles.py to archive existing data")
        
        response = input("\nContinue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted")
            return
    
    # Load base tiling
    base_tiling = load_base_tiling()
    if base_tiling is None:
        return
    
    # Tag true window boundary once (before any removals)
    for t in base_tiling["tiles"]:
        t.setdefault("is_outer_edge", t.get("boundary_kind") == "outer_edge")


    # Initialize components
    obstacle_creator = ObstacleCreator(config)
    obstacle_config = ObstacleConfig(config)
    visualizer = ObstacleVisualizer(config)
    
    print("\nGenerating obstacle specifications...")
    obstacle_specs = obstacle_config.generate_scalable_obstacles(base_tiling)
    print(f"Generated {len(obstacle_specs)} obstacle specs")
    
    # Create obstacles
    results = create_obstacle_configurations(
        obstacle_creator, visualizer,
        base_tiling, obstacle_specs, output_dir
    )
    
    # Save comprehensive experiment summary
    save_experiment_summary(results, output_dir, start_time)
    
    print(f"\ngenerate obstacles completed in {time.time() - start_time:.2f}s")
    print(f"   • Generated {len(results)} obstacle configurations")
    print(f"   • Output: {output_dir}")
    print(f"   • Run verification: python validation/validate_obstacles.py")


def load_base_tiling():
    """
    Load canonical tiling for obstacle generation.

    Priority:
      1) data/processed/penrose_tiling_energy_initialized.json (if it exists)
      2) data/raw/penrose_tiling.json
    """
    candidates = [
        Path("data/processed/penrose_tiling_energy_initialized.json"),
        Path("data/raw/penrose_tiling.json"),
    ]

    for path in candidates:
        if path.exists():
            with open(path, 'r') as f:
                tiling_data = json.load(f)

            print(f"Loaded base tiling: {tiling_data['metadata']['tile_count']} tiles")
            print(f"   Source: {path}")
            return tiling_data

    print("Error: Missing base tiling.")
    raise FileNotFoundError("Processed tiling missing. Run 01_prepare_processed_tiling.py first.")
    return None


def setup_output_directory():
    """organize output directory structure"""
    output_dir = Path("data/obstacles")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create subdirectories for organization
    (output_dir / "pores").mkdir(exist_ok=True)
    (output_dir / "fixed_defects").mkdir(exist_ok=True)
    (output_dir / "visualizations").mkdir(exist_ok=True)
    
    return output_dir


def create_obstacle_configurations(obstacle_creator, visualizer, base_tiling, obstacle_specs, output_dir):
    """Create all obstacle configurations efficiently"""
    results = []
    
    for spec_name, obstacle_spec in obstacle_specs.items():
        print(f"\nCreating obstacles: {spec_name}")
        
        # Create obstacles
        obstacle_tiling = obstacle_creator.create_obstacles(base_tiling, obstacle_spec)

        # recompute topology-dependent energy fields after removal
        from src.energy.widom_inspired_energy import WidomInspiredEnergy
        energy_model = WidomInspiredEnergy.from_config(obstacle_creator.config)
        energy_model.update_tiling_energy(obstacle_tiling)

        # refresh coordination distribution AFTER topology edits ---
        # (Otherwise pores configs keep the "perfect tiling" coordination stats, which becomes stale.)
        coord = {}
        for t in obstacle_tiling["tiles"]:
            deg = str(len(t.get("neighbors", [])))
            coord[deg] = coord.get(deg, 0) + 1

        md = obstacle_tiling.get("metadata", {})
        if "coordination_distribution" in md and "coordination_distribution_original" not in md:
            md["coordination_distribution_original"] = md["coordination_distribution"]
        md["coordination_distribution"] = dict(sorted(coord.items(), key=lambda kv: int(kv[0])))

        # # --- Keep decomposition fields consistent with updated local_energy ---
        # w = energy_model.params.matching_rule_weight
        # for t in obstacle_tiling["tiles"]:
        #      if t.get("removed", False):
        #         t["surface_contribution"] = 0.0
        #         t["bulk_energy"] = 0.0
        #         continue
        #     sc = w * float(t.get("surface_energy", 0.0))
        #     t["surface_contribution"] = sc
        #     t["bulk_energy"] = float(t["local_energy"]) - sc

        
        # Ensure adjacency keys are strings (JSON safe)
        if "adjacency_graph" in obstacle_tiling:
            obstacle_tiling["adjacency_graph"] = adjacency_intkeys_to_str(
                obstacle_tiling["adjacency_graph"]
            )

        
        # Save obstacle configuration
        file_path = save_obstacle_config(obstacle_tiling, spec_name, output_dir)
        
        # Create visualization
        viz_path = output_dir / "visualizations" / f"{spec_name}.png"
        visualizer.plot_obstacles(obstacle_tiling, save_path=viz_path)
        
        results.append({
            "name": spec_name,
            "file": str(file_path),
            "visualization": str(viz_path),
            "metadata": obstacle_tiling["obstacle_metadata"]
        })
        
        print(f" Saved: {file_path.name}")
    
    return results


def save_obstacle_config(obstacle_tiling, spec_name, output_dir):
    """Save obstacle configuration to appropriate subdirectory"""
    if "pores" in spec_name:
        save_dir = output_dir / "pores"
    else:
        save_dir = output_dir / "fixed_defects"
    
    file_path = save_dir / f"{spec_name}.json"
    with open(file_path, 'w') as f:
        json.dump(obstacle_tiling, f, indent=2)
    
    return file_path


def save_experiment_summary(results, output_dir, start_time):
    """Save comprehensive experiment summary"""
    summary = {
        "duration_seconds": time.time() - start_time,
        "total_configurations": len(results),
        "configurations": results
    }
    
    summary_file = output_dir / "experiment_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nSummary saved: {summary_file.name}")


if __name__ == "__main__":
    main()
