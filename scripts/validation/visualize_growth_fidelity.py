#!/usr/bin/env python3
"""
Forensic Visualization of Growth Experiments
Validates:
1. Structural Integrity (Did it melt?)
2. Defect Localization (Did it heal?)
3. Growth Dynamics (Did it grow in layers?)

Usage:
  python scripts/validation/visualize_growth_fidelity.py [optional_path_to_json]
  
  If no path is provided, it automatically finds the latest *_final.json
  in data/experiments/growth/
"""

import sys
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
from pathlib import Path
import glob

# Add project root to path
project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.utils.config import ConfigManager

def find_latest_final_json(base_dir):
    """Auto-discovery of the most recent geometry dump"""
    search_pattern = str(base_dir / "growth" / "*_final.json")
    files = glob.glob(search_pattern)
    
    if not files:
        return None
        
    # Sort by modification time (newest first)
    files.sort(key=lambda x: Path(x).stat().st_mtime, reverse=True)
    return Path(files[0])

def load_run_data(run_path=None):
    """Smart loader: explicit path or auto-discovery"""
    data_dir = project_root / "data" / "experiments"
    
    if run_path is None:
        print("🔍 No file specified. Searching for latest run...")
        run_path = find_latest_final_json(data_dir)
        if run_path is None:
            print("❌ No '*_final.json' files found in data/experiments/growth/")
            print("   Make sure [metrics] save_full_state = true in your config.")
            sys.exit(1)
    
    path = Path(run_path)
    if not path.exists():
        # Try resolving relative to project root
        path = project_root / run_path
        if not path.exists():
            print(f"❌ File not found: {path}")
            sys.exit(1)
        
    # LOGGING: Print path relative to project root for clarity
    try:
        rel_path = path.relative_to(project_root)
        print(f"📂 Loading: {rel_path}")
    except ValueError:
        print(f"📂 Loading: {path}")
    
    # If user points to the metrics file (e.g. run_005.json), try to find run_005_final.json
    if "final" not in path.name:
        final_candidate = path.parent / f"{path.stem}_final.json"
        if final_candidate.exists():
             try:
                 rel_final = final_candidate.relative_to(project_root)
                 print(f"🔄 Redirecting to full geometry file: {rel_final}")
             except ValueError:
                 print(f"🔄 Redirecting to full geometry file: {final_candidate.name}")
             path = final_candidate
    
    with open(path, 'r') as f:
        data = json.load(f)
        
    # Quick Validation check
    if "tiles" not in data:
        print("❌ Error: JSON does not contain 'tiles' list.")
        print("   This looks like a summary file, not a geometry dump.")
        sys.exit(1)
        
    return data, path

def get_defect_coords(tiling_data):
    """Extract coordinates of high-energy vertices"""
    defects = []
    
    for tile in tiling_data['tiles']:
        if tile.get('removed', False):
            continue
        
        # Check explicit class if available
        v_class = tile.get('vertex_class', 'UNKNOWN')
        # Also check raw energy as fallback
        energy = tile.get('local_energy', 0.0)
        
        # Mark as defect if High/Medium energy (Red/Orange warning)
        if v_class in ['HIGH_ENERGY', 'MEDIUM_ENERGY'] or energy > 1.0:
            defects.append(tile['center'])
            
    return np.array(defects)

def plot_growth_forensics(tiling_data, output_path):
    """Generate the 3-panel forensic report"""
    
    tiles = tiling_data['tiles']
    
    # Setup Figure
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))
    titles = ["Structural Integrity\n(Melting Check)", 
              "Defect Distribution\n(Healing Check)", 
              "Growth History\n(Nucleation Check)"]
    
    # --- PREPARE DATA ARRAYS ---
    polygons = []
    colors_structure = [] # Thick/Thin
    colors_growth = []    # Time gradient
    
    # Find max growth step for normalization
    # Handle missing 'growth_step' (ungrown tiles get 0)
    steps = [t.get('growth_step', 0) for t in tiles if not t.get('removed', False)]
    max_step = max(steps) if steps else 1
    
    print(f"ℹ️  Max growth step found: {max_step}")

    for tile in tiles:
        if tile.get('removed', False):
            continue
            
        verts = np.array(tile['vertices'])
        poly = Polygon(verts, closed=True)
        polygons.append(poly)
        
        # 1. Structure Color (Thick/Thin)
        if tile['type'] == 'THICK':
            colors_structure.append('#4a90e2') # Blue
        else:
            colors_structure.append('#f5a623') # Orange
            
        # 2. Growth Color (Time Gradient)
        status = tile.get('growth_status', 'ungrown')
        step = tile.get('growth_step', 0)
        
        if status == 'ungrown':
            colors_growth.append('#e0e0e0') # Gray for future potential growth
        elif status == 'frontier':
            colors_growth.append('#ff00ff') # Magenta for active edge
        else:
            # Gradient: Dark Blue (seed) -> Cyan (recent)
            intensity = step / max_step if max_step > 0 else 0
            colors_growth.append(plt.cm.viridis(intensity))

    # --- PANEL 1: STRUCTURE (Did it melt?) ---
    ax = axes[0]
    collection = PatchCollection(polygons, match_original=False)
    collection.set_facecolor(colors_structure)
    collection.set_edgecolor('white')
    collection.set_linewidth(0.5)
    ax.add_collection(collection)
    ax.set_title(titles[0], fontsize=12, fontweight='bold')
    
    # --- PANEL 2: DEFECTS (Did it heal?) ---
    ax = axes[1]
    # Background: faint gray structure
    collection_bg = PatchCollection(polygons, match_original=False)
    collection_bg.set_facecolor('#f0f0f0')
    collection_bg.set_edgecolor('#d0d0d0')
    collection_bg.set_linewidth(0.5)
    ax.add_collection(collection_bg)
    
    # Overlay: Defects
    defects = get_defect_coords(tiling_data)
    if len(defects) > 0:
        ax.scatter(defects[:,0], defects[:,1], c='red', s=15, alpha=0.7, label='Defect', zorder=10)
        ax.legend(loc='upper right')
    
    ax.set_title(titles[1], fontsize=12, fontweight='bold')

    # --- PANEL 3: GROWTH HISTORY ---
    ax = axes[2]
    collection_growth = PatchCollection(polygons, match_original=False)
    collection_growth.set_facecolor(colors_growth)
    collection_growth.set_edgecolor('black')
    collection_growth.set_linewidth(0.2)
    ax.add_collection(collection_growth)
    ax.set_title(titles[2], fontsize=12, fontweight='bold')
    
    # --- COMMON FORMATTING ---
    # Use window origin/size from metadata if available to keep zoom consistent
    meta = tiling_data.get('metadata', {})
    origin = meta.get('window_origin', [0,0])
    size = meta.get('window_size', [60,60])
    
    for ax in axes:
        ax.set_aspect('equal')
        ax.set_xlim(origin[0], origin[0] + size[0])
        ax.set_ylim(origin[1], origin[1] + size[1])
        ax.axis('off')

    # Save
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    
    try:
        rel_output = output_path.relative_to(project_root)
        print(f"📸 Forensic visualization saved to: {rel_output}")
    except ValueError:
        print(f"📸 Forensic visualization saved to: {output_path}")

    # Auto-open
    try:
        plt.show()
    except Exception as e:
        print(f"⚠️  Could not open display: {e}")
        
    plt.close()

if __name__ == "__main__":
    path_arg = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        data, filepath = load_run_data(path_arg)
        
        # Determine output filename
        output_image = filepath.parent / f"{filepath.stem}_forensics.png"
        
        plot_growth_forensics(data, output_image)
        
    except Exception as e:
        print(f"\n❌ Visualization Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)