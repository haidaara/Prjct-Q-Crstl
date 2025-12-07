"""
🚀 MILESTONE 2A: HIGH-PERFORMANCE OBSTACLE CREATION PIPELINE
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.utils.config import ConfigManager
from src.obstacle.obstacle_creator import ObstacleCreator, ObstacleSpec, adjacency_intkeys_to_str
from src.obstacle.obstacle_config import ObstacleConfig
from src.obstacle.obstacle_visualizer import ObstacleVisualizer
import json
from pathlib import Path
import time

def main():
    start_time = time.time()
    
    # Load configuration - FIXED PATH
    config = ConfigManager("configs/phase2_obstacles.toml")
    
    print("🚀 STARTING MILESTONE 2A: HIGH-PERFORMANCE OBSTACLE CREATION")
    print(f"📁 Config: {config.config_path}")
    
    obstacle_dir = Path("data/obstacles")
    if obstacle_dir.exists() and any(obstacle_dir.iterdir()):
        print("⚠️  WARNING: data/obstacles already has data!")
        print("   Run: python scripts/archive_obstacles.py to archive existing data")
        response = input("   Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("❌ Aborted - archive existing data first")
            return


    # Load validated Milestone1 data
    base_tiling = load_base_tiling()
    if not base_tiling:
        return
    
    # Initialize high-performance obstacle system
    obstacle_creator = ObstacleCreator(config)
    obstacle_config = ObstacleConfig(config)
    visualizer = ObstacleVisualizer(config)
    
    # Generate scalable obstacle configurations
    obstacle_specs = obstacle_config.generate_scalable_obstacles(base_tiling)
    
    # Create and save all obstacle configurations
    output_dir = setup_output_directory()
    results = create_obstacle_configurations(obstacle_creator, visualizer, 
                                           base_tiling, obstacle_specs, output_dir)
    
    # Save comprehensive experiment summary
    save_experiment_summary(results, output_dir, start_time)
    
    print(f"\n✅ MILESTONE 2A COMPLETED IN {time.time() - start_time:.2f}s")
    print(f"   • Generated {len(results)} obstacle configurations")
    print(f"   • Output: {output_dir}")
    print(f"   • Run verification: python scripts/verify_obstacles.py")

def load_base_tiling():
    """Load and validate Milestone1 tiling data - FIXED PATH"""
    milestone1_file = Path("data/raw/penrose_tiling.json")
    
    if not milestone1_file.exists():
        print("❌ Error: Run Milestone1 first - missing penrose_tiling.json")
        return None
        
    with open(milestone1_file, 'r') as f:
        tiling_data = json.load(f)
    
    print(f"📐 Loaded base tiling: {tiling_data['metadata']['tile_count']} tiles")
    return tiling_data

def setup_output_directory():
    """Create organized output directory structure - FIXED PATH"""
    output_dir = Path("data/obstacles")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create subdirectories for organization
    (output_dir / "pores").mkdir(exist_ok=True)
    (output_dir / "fixed_defects").mkdir(exist_ok=True)
    (output_dir / "visualizations").mkdir(exist_ok=True)
    
    return output_dir

def create_obstacle_configurations(obstacle_creator, visualizer, base_tiling, 
                                 obstacle_specs, output_dir):
    """Create all obstacle configurations with visualization"""
    results = []
    
    for spec_name, obstacle_spec in obstacle_specs.items():
        print(f"\n🔧 Creating {spec_name}...")
        
        # Create obstacles with high-performance method
        obstacle_tiling = obstacle_creator.create_obstacles(base_tiling, obstacle_spec)
        
        # Convert adjacency keys to strings for JSON export
        obstacle_tiling["adjacency_graph"] = adjacency_intkeys_to_str(obstacle_tiling["adjacency_graph"])
        
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
        
        print(f"💾 Saved: {file_path}")
    
    return results

def save_obstacle_config(obstacle_tiling, spec_name, output_dir):
    """Save obstacle configuration to appropriate subdirectory"""
    if "pores" in spec_name:
        subdir = "pores"
    else:
        subdir = "fixed_defects"
        
    file_path = output_dir / subdir / f"{spec_name}.json"
    with open(file_path, 'w') as f:
        json.dump(obstacle_tiling, f, indent=2)
        
    return file_path

def save_experiment_summary(results, output_dir, start_time):
    """Save comprehensive experiment summary"""
    now = time.time()
    summary = {
        "timestamp": now,
        "duration_seconds": now - start_time,
        "total_configurations": len(results),
        "configurations": results
    }
    
    summary_file = output_dir / "experiment_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"📊 Experiment summary: {summary_file}")

if __name__ == "__main__":
    main()