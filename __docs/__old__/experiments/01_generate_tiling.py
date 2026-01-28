# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------
import sys
import os

# Adjust sys.path to ensure src.* imports work ONLY if this file is in scripts/

from src.utils.config import ConfigManager
from src.tilings.penrose_p3 import PenroseTiling
from src.viz.plotters import TilingVisualizer
import json
from pathlib import Path


def main():
    # Load configuration
    config = ConfigManager("configs/phase2_experiments.toml")
    
    print("🚀 Starting Milestone 1: Penrose Tiling Generation")
    print(f"📁 Using config: {config.config_path}")
    
    # Generate tiling
    print("🔷 Generating Penrose P3 tiling...")
    penrose = PenroseTiling(config)
    tiling_data = penrose.generate()
    
    # Visualize + Export (I/O FIX: use exports.tiling_json as canonical path)
    print("📊 Creating visualization...")
    viz = TilingVisualizer(config)

    # Use the explicit file path if provided (canonical & safest)
    output_file = Path(config.exports.get("tiling_json", "data/raw/penrose_tiling.json"))
    output_dir = output_file.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    viz.plot_tiling(tiling_data, save_path=str(output_dir / "penrose_tiling.png"))
    
    # Export data for future phases
    if config.exports.get("format") == "json":
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
