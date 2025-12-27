#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from tqdm import tqdm  # Recommended for progress tracking

# Setup Path
project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.viz.utils import load_tiling_state
from src.viz.static_plots import plot_physics_matrix

def main():
    parser = argparse.ArgumentParser(description="Batch generate physics matrices for a directory")
    parser.add_argument("--dir", "-d", type=str, required=True, help="Directory containing JSON files")
    parser.add_argument("--output", "-o", type=str, help="Custom output directory (default: same as input/viz)")
    args = parser.parse_args()

    input_dir = Path(args.dir)
    if not input_dir.exists():
        print(f"❌ Error: Directory not found: {input_dir}")
        sys.exit(1)

    # 1. Gather all candidates (Matching your visualize_state.py logic)
    candidates = list(input_dir.glob("**/*.json"))
    
    # 2. Filter out summaries and pointer files
    files_to_plot = [
        p for p in candidates 
        if "summary" not in p.name and "latest" not in p.name and "pointer" not in p.name
    ]

    print(f"🔍 Found {len(files_to_plot)} state files. Starting batch visualization...")

    for json_path in tqdm(files_to_plot, desc="Generating Plots"):
        try:
            # Load Data
            tiling_data = load_tiling_state(json_path)
            
            # Determine Output Path
            if args.output:
                out_dir = Path(args.output)
            else:
                # Standard Contract: Save in a 'viz' folder next to the data
                out_dir = json_path.parent / "viz"
            
            out_dir.mkdir(parents=True, exist_ok=True)
            save_path = out_dir / f"{json_path.stem}_matrix.png"

            # Generate Matrix
            plot_physics_matrix(tiling_data, save_path=str(save_path))
            
        except Exception as e:
            print(f"\n⚠️ Skipping {json_path.name}: {e}")

    print(f"\n✅ Batch complete. Plots saved to designated 'viz' folders.")

if __name__ == "__main__":
    main()