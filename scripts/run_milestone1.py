import sys
import os

# Adjust sys.path to ensure src.* imports work ONLY if this file is in scripts/
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.utils.config import ConfigManager
from src.tilings.penrose_p3 import PenroseTiling
from src.viz.plotters import TilingVisualizer
import json
from pathlib import Path

def main():
    # Load configuration
    config = ConfigManager("configs/phase1_baseline.toml")
    
    print("🚀 Starting Milestone 1: Penrose Tiling Generation")
    print(f"📁 Using config: {config.config_path}")
    
    # Generate tiling
    print("🔷 Generating Penrose P3 tiling...")
    penrose = PenroseTiling(config)
    tiling_data = penrose.generate()
    
    # Visualize
    print("📊 Creating visualization...")
    viz = TilingVisualizer(config)
    output_dir = Path(config.exports.get("output_dir", "data/raw"))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    viz.plot_tiling(tiling_data, save_path=output_dir / "penrose_tiling.png")
    
    # Export data for future phases
    if config.exports.get("format") == "json":
        output_file = output_dir / "penrose_tiling.json"
        with open(output_file, 'w') as f:
            json.dump(tiling_data, f, indent=2)
        print(f"💾 Data exported to: {output_file}")
    
    # Print summary
    metadata = tiling_data["metadata"]
    print("\n✅ Milestone 1 Complete!")
    print(f"   • Generated {metadata['tile_count']} tiles")
    print(f"   • Thick/Thin ratio: {metadata['thick_count']}/{metadata['thin_count']}")
    print(f"   • Adjacency computed: {metadata['adjacency_computed']}")
    # --- BLOCKING FIX #4 --- Make sure "window_origin" is present in metadata
    window_origin = metadata.get("window_origin", None)
    if window_origin is not None:
        print(f"   • Window: {window_origin} to {metadata['window_size']}")
    else:
        print(f"   • Window size: {metadata['window_size']}")

if __name__ == "__main__":
    main()