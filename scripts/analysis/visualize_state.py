#!/usr/bin/env python3
"""
VISUALIZATION DRIVER: 2x2 Physics Matrix
Contract: Output to .../run_XXX/viz/ and respect 'plot_format' in config.
"""

import sys
import argparse
import toml
from pathlib import Path

# --- Setup Path ---
project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.viz.utils import load_tiling_state
from src.viz.static_plots import plot_physics_matrix

def clean_path(p: Path) -> str:
    try: return str(p.relative_to(project_root))
    except ValueError: return str(p)

def find_latest_experiment(search_dir: Path) -> Path:
    # 1. Gather all candidates
    candidates = list(search_dir.glob("**/*_final.json")) + \
                 list(search_dir.glob("**/*_run_*.json")) + \
                 list(search_dir.glob("**/snapshots/*.json"))
    
    # 2. FIX: Filter out "Summary" files (metrics only, no tiles)
    candidates = [p for p in candidates if "summary" not in p.name]

    if not candidates:
        raise FileNotFoundError(f"No state files found in {clean_path(search_dir)}")
    
    # 3. Return the most recently modified valid file
    return max(candidates, key=lambda p: p.stat().st_mtime)

def get_config_format() -> str:
    """Reads plot_format from phase2_experiments.toml (The Contract)."""
    cfg_path = project_root / "configs" / "phase2_experiments.toml"
    if cfg_path.exists():
        try:
            with open(cfg_path, "r") as f:
                cfg = toml.load(f)
            return cfg.get("metrics", {}).get("plot_format", "png")
        except: pass
    return "png" # Default to contract if missing

def main():
    parser = argparse.ArgumentParser(description="Generate 2x2 Physics Matrix")
    parser.add_argument("--file", "-f", type=str, help="Path to state file")
    parser.add_argument("--output", "-o", type=str, help="Custom output path")
    args = parser.parse_args()
    
    try:
        # 1. Resolve Input
        if args.file:
            input_path = Path(args.file)
            if not input_path.is_absolute():
                input_path = project_root / input_path
        else:
            search_path = project_root / "data/experiments"
            print(f"🔍 Searching in: {clean_path(search_path)}")
            input_path = find_latest_experiment(search_path)
            
        print(f"📂 Loading State: {input_path.name}")
        
        # 2. Load Data (Robust)
        tiling_data = load_tiling_state(input_path)
        
        # 3. Determine Output
        if args.output:
            output_path = Path(args.output)
        else:
            # CONTRACT: Save to .../run_XXX/viz/filename.fmt
            # Find the run directory (parent of the json)
            run_dir = input_path.parent
            if run_dir.name in ["snapshots", "frames"]:
                run_dir = run_dir.parent
            
            viz_dir = run_dir / "viz"
            viz_dir.mkdir(parents=True, exist_ok=True)
            
            # Determine format from Config Contract
            fmt = get_config_format().replace(".", "")
            output_path = viz_dir / f"{input_path.stem}_matrix.{fmt}"
            
        # 4. Generate
        plot_physics_matrix(tiling_data, save_path=str(output_path))

    except Exception as e:
        print(f"\n❌ Error: {e}")
        if not isinstance(e, (FileNotFoundError, ValueError)):
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()