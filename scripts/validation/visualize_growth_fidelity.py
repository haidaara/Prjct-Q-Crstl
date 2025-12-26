import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import json
import sys
import os
from pathlib import Path

# --- HELPER: Geometric Hashing ---
def get_tile_fingerprints(tiles):
    """
    Creates a set of unique strings representing the center position of each tile.
    Used to detect which tiles are NEW (did not exist in input).
    """
    fingerprints = set()
    for t in tiles:
        # Calculate centroid
        verts = np.array(t["vertices"])
        center = np.mean(verts, axis=0)
        # Create a precision-safe string hash (e.g., "10.552,-3.221")
        h = f"{center[0]:.3f},{center[1]:.3f}"
        fingerprints.add(h)
    return fingerprints

def plot_growth_forensics(tiling_data, output_path, input_tiling_path=None):
    """
    Generates a 4-Panel Matrix Report.
    UPDATED: Uses GEOMETRIC DIFFERENCING to identify new tiles (Panel 4).
    """
    tiles = tiling_data.get("tiles", [])
    meta = tiling_data.get("meta", {})
    params = tiling_data.get("params", {})
    
    # --- EXTRACT CONFIG FOR SUBTITLES ---
    # Example: "T=0.8 | Steps=200 | Density=d0.03"
    temp = params.get("temperature", "N/A")
    steps = params.get("mc_steps_per_growth", "N/A")
    dens = meta.get("density_token", "N/A")
    config_subtitle = f"Config: T={temp} | Steps={steps} | {dens}"

    if not tiles:
        print("   ⚠️ ERROR: No tiles found.")
        return

    # --- 1. IDENTIFY NEW TILES (Geometric Differencing) ---
    new_tile_indices = set()
    
    if input_tiling_path and os.path.exists(input_tiling_path):
        print(f"   • Loading input baseline: {Path(input_tiling_path).name}")
        try:
            with open(input_tiling_path, 'r') as f:
                input_data = json.load(f)
            
            # Get fingerprints of the ORIGINAL tiles
            original_fingerprints = get_tile_fingerprints(input_data.get("tiles", []))
            
            # Check current tiles against original
            new_count = 0
            for idx, t in enumerate(tiles):
                verts = np.array(t["vertices"])
                center = np.mean(verts, axis=0)
                h = f"{center[0]:.3f},{center[1]:.3f}"
                
                if h not in original_fingerprints:
                    new_tile_indices.add(idx)
                    new_count += 1
            
            print(f"   • Geometric Diff: Found {new_count} truly new tiles.")
            
        except Exception as e:
            print(f"   ⚠️ Baseline comparison failed: {e}")
    else:
        print("   ⚠️ Input tiling file not found. Panel 4 will be blank.")

    # --- 2. DATA EXTRACTION ---
    polygons = []
    types = []
    neighbor_counts = []
    # We create a dummy ID list for the rainbow plot since real IDs are sorted
    # This approximates radial growth if we assume sorting by position
    ids = [] 
    
    for idx, t in enumerate(tiles):
        verts = np.array(t["vertices"])
        polygons.append(Polygon(verts, closed=True))
        types.append(t.get("type", "UNKNOWN"))
        ids.append(idx) 
        neighbor_counts.append(len(t.get("neighbors", [])))

    # --- 3. SETUP CANVAS ---
    fig, axes = plt.subplots(2, 2, figsize=(18, 18), facecolor='white')
    
    # Main Title + Config Subtitle
    fig.suptitle(f"Phason Dynamics Forensic Report\n{config_subtitle}", fontsize=20, weight='bold')

    ax_geo = axes[0, 0]
    ax_topo = axes[0, 1]
    ax_hist = axes[1, 0]
    ax_act = axes[1, 1]

    # --- PANEL 1: GEOMETRY ---
    ax_geo.set_title(f"1. Structural Phase Map\n{dens} Geometry", fontsize=12, weight='bold')
    colors_geo = ['#FFD700' if t == "THIN" else '#4169E1' for t in types]
    _render_collection(ax_geo, polygons, colors_geo)

    # --- PANEL 2: TOPOLOGY ---
    ax_topo.set_title(f"2. Coordination Map\nCrack Detection (Red=Defect)", fontsize=12, weight='bold')
    colors_topo = []
    for n in neighbor_counts:
        if n >= 4: colors_topo.append('#2E8B57')  # Sea Green
        elif n == 3: colors_topo.append('#F4A460')  # Sandy Brown
        else: colors_topo.append('#DC143C')  # Crimson
    _render_collection(ax_topo, polygons, colors_topo)

    # --- PANEL 3: SPATIAL GRADIENT ---
    # Since IDs are sorted by position, this is now a "Position Gradient"
    # It still helps see the order of the file structure.
    ax_hist.set_title(f"3. Index Gradient\n(Sorted Spatial Order)", fontsize=12, weight='bold')
    collection_hist = PatchCollection(polygons, match_original=False)
    collection_hist.set_array(np.array(ids))
    collection_hist.set_cmap('viridis') 
    collection_hist.set_edgecolor('none')
    ax_hist.add_collection(collection_hist)
    ax_hist.autoscale_view()
    ax_hist.axis('equal')
    ax_hist.axis('off')
    cbar = plt.colorbar(collection_hist, ax=ax_hist, orientation='horizontal', pad=0.05, fraction=0.046)
    cbar.set_label("Tile Storage Index")

    # --- PANEL 4: TRUE ACTIVITY MAP ---
    ax_act.set_title(f"4. Differential Growth Map\nMagenta = {len(new_tile_indices)} Healed Tiles", fontsize=12, weight='bold')
    
    colors_act = []
    edges_act = []
    
    for idx in range(len(tiles)):
        if idx in new_tile_indices:
            # TRUE NEW TILE
            colors_act.append('#FF00FF')  # Magenta
            edges_act.append('black')
        else:
            # ORIGINAL TILE
            colors_act.append('#E0E0E0')  # Light Gray
            edges_act.append('none')
    
    collection_act = PatchCollection(polygons, match_original=False)
    collection_act.set_facecolor(colors_act)
    collection_act.set_edgecolor(edges_act)
    collection_act.set_linewidth(0.5)
    ax_act.add_collection(collection_act)
    ax_act.autoscale_view()
    ax_act.axis('equal')
    ax_act.axis('off')

    # --- SAVE ---
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"   ✅ SUCCESS: Matrix saved to: {output_path}")

def _render_collection(ax, polys, colors):
    coll = PatchCollection(polys, match_original=False)
    coll.set_facecolor(colors)
    coll.set_edgecolor('white')
    coll.set_linewidth(0.5)
    ax.add_collection(coll)
    ax.autoscale_view()
    ax.axis('equal')
    ax.axis('off')
if __name__ == "__main__":
    # 1. Collect files to process
    files_to_process = []
    
    if len(sys.argv) > 1:
        # Loop through ALL arguments to handle wildcards (e.g., healing_*.json)
        for arg in sys.argv[1:]:
            path = Path(arg)
            if path.exists():
                files_to_process.append(str(path))
            else:
                print(f"⚠️ File not found: {arg}")
    else:
        # Auto-detect latest if no args
        # We check both growth and healing folders since you are working on both
        search_dirs = [Path("data/experiments/growth"), Path("data/experiments/healing")]
        found_files = []
        for d in search_dirs:
            if d.exists():
                # Look for JSON files (final or run)
                found_files.extend(d.glob("*.json"))
        
        if found_files:
            found_files.sort(key=os.path.getmtime, reverse=True)
            files_to_process.append(str(found_files[0]))
            print(f"🤖 AUTO-DETECT: Found latest run: {found_files[0].name}")

    if not files_to_process:
        print("❌ No files found to process.")
        sys.exit(1)

    print(f"🚀 Batch processing {len(files_to_process)} files...")

    # 2. Process Loop (The Fix for Wildcards & Crashes)
    for input_file in files_to_process:
        print(f"\n🔎 PROCESSING: {Path(input_file).name}")
        
        # --- A. Load Data SAFELY ---
        data = None
        try:
            with open(input_file, 'r') as f:
                content = f.read()
                if not content.strip():
                    print("   ⚠️ SKIP: File is empty (previous crash?).")
                    continue
                data = json.loads(content)
        except Exception as e:
            print(f"   ❌ ERROR: Could not load JSON: {e}")
            continue

        # --- B. Determine Output Path ---
        viz_root = Path("data/visualizations/growth_forensics")
        viz_root.mkdir(parents=True, exist_ok=True)
        output_filename = f"{Path(input_file).stem}_matrix.png"
        output_file = viz_root / output_filename
        
        # --- C. Determine Baseline (Optional) ---
        baseline_path = None
        try:
            raw_path = data.get("meta", {}).get("input_tiling")
            if raw_path:
                if os.path.exists(raw_path):
                    baseline_path = raw_path
                else:
                    # Try relative to project root
                    project_root = Path(__file__).resolve().parents[2]
                    potential = project_root / raw_path
                    if potential.exists():
                        baseline_path = str(potential)
        except:
            pass # Baseline is optional, don't crash

        # --- D. Call Original Plotting Logic ---
        try:
            # We call your existing function here
            plot_growth_forensics(data, str(output_file), input_tiling_path=baseline_path)
        except Exception as e:
            print(f"   ⚠️ Plotting failed for this file: {e}")
            import traceback
            traceback.print_exc()