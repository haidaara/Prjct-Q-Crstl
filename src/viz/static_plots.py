# src/viz/static_plots.py
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
from matplotlib.collections import PatchCollection
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional, List

try:
    import tomllib as toml 
except ImportError:
    try:
        import toml 
    except ImportError:
        toml = None

from src.viz.utils import (
    extract_topology, 
    extract_physics_fields, 
    get_growth_mask, 
    get_obstacle_mask
)

# --- CONFIG LOADING ---
def _load_publication_config() -> Dict[str, Any]:
    """Loads aesthetics from configs/publication_plots.toml."""
    defaults = {
        "publication": {"format": "png", "dpi": 300, "transparent_background": False, "tight_layout": True},
        "fonts": {"family": "sans-serif", "title_size": 14, "base_size": 10},
        "lines": {"line_width": 0.5},
        "figure": {"matrix_figsize": [18, 18]} 
    }
    
    if toml is None: return defaults

    project_root = Path(__file__).resolve().parents[2]
    config_path = project_root / "configs" / "publication_plots.toml"
    
    if not config_path.exists(): return defaults

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if toml.__name__ == "tomllib":
            cfg = toml.loads(content)
        else:
            cfg = toml.loads(content)
            
        # Merge defaults
        for section in defaults:
            if section not in cfg:
                cfg[section] = defaults[section]
        return cfg

    except Exception as e:
        print(f"⚠️ Config load failed ({e}), using defaults.")
        return defaults
# --- HELPERS ---
def _generate_subtitle(data: Dict[str, Any]) -> str:
    meta = data.get("meta", {})
    params = data.get("params", {})
    
    T = params.get("temperature") or meta.get("temperature") or "N/A"
    
    d_val = meta.get("obstacle_density")
    if d_val is None:
        d_val = params.get("density")
    if d_val is None:
        d_val = meta.get("density")
    if d_val is None:
        d_val = meta.get("density_token", "N/A")

    dens = str(d_val).replace("d", "") if d_val != "N/A" else d_val


    steps = params.get("steps") or params.get("total_steps") or params.get("mc_steps_per_growth") or params.get("growth_steps") or "N/A"

    return f"T={T} | Density={dens} | Steps={steps}"

def _add_legend(ax, items: List[tuple], loc='upper right', title="Legend", font_size=10):
    legend_handles = [
        Patch(facecolor=color, edgecolor='white', linewidth=0.5, label=label)
        for color, label in items
    ]
    ax.legend(
        handles=legend_handles, loc=loc, fontsize=font_size, 
        title=title, title_fontsize=font_size+1, framealpha=0.9, edgecolor='gray'
    )

def plot_physics_matrix(tiling_data: Dict[str, Any], save_path: Optional[str] = None):
    """
    Generates the 2x2 Diagnostic Matrix.
    Strictly follows P0 (Correctness) and P1 (Config) requirements.
    """
    # 1. Load Aesthetics (P1 Compliance)
    cfg = _load_publication_config()
    pub = cfg.get("publication", {})
    fonts = cfg.get("fonts", {})
    lines = cfg.get("lines", {})
    
    dpi = pub.get("dpi", 300)
    fmt = pub.get("format", "png")
    transparent = pub.get("transparent_background", False)
    lw = lines.get("line_width", 0.5)
    figsize = cfg.get("figure", {}).get("matrix_figsize", [18, 18])
    
    # 2. Extract Data
    tiles = tiling_data["tiles"]
    adj_graph = extract_topology(tiling_data)
    energy_map, class_map = extract_physics_fields(tiling_data)
    growth_map = get_growth_mask(tiling_data)
    obs_map = get_obstacle_mask(tiling_data)
    
    # 3. Apply Style Context
    with plt.rc_context({'font.family': fonts.get("family", "sans-serif"), 
                         'font.size': fonts.get("base_size", 10)}):
        
        fig, axes = plt.subplots(2, 2, figsize=figsize, facecolor='white' if not transparent else 'none')
        axes = axes.flatten()
        
        # Header
        main_title = "Phason Dynamics & Growth State"
        subtitle = _generate_subtitle(tiling_data)
        fig.suptitle(f"{main_title}\n{subtitle}", fontsize=fonts.get("title_size", 14)+6, fontweight='bold', y=0.96)
        
        # Pre-calculate vertices
        patches_base = []
        ids = []
        all_verts = []
        
        for i, t in enumerate(tiles):
            verts = np.array(t["vertices"])
            patches_base.append(Polygon(verts, closed=True))
            ids.append(int(t.get("id", i)))
            all_verts.append(verts)
            
        all_verts_stacked = np.vstack(all_verts)
        xlims = (all_verts_stacked[:,0].min(), all_verts_stacked[:,0].max())
        ylims = (all_verts_stacked[:,1].min(), all_verts_stacked[:,1].max())

        # =========================================================================
        # PANEL 1: Structural Phase Map
        # =========================================================================
        ax = axes[0]
        ax.set_title("1. Structural Phase Map\n(Geometry & Obstacles)", fontsize=fonts.get("title_size", 12), fontweight='bold')
        
        colors_p1 = []
        for i, tid in enumerate(ids):
            obs = obs_map.get(tid)
            t_type = tiles[i]["type"]
            
            if obs == "pore": colors_p1.append("#2c3e50")
            elif obs == "fixed": colors_p1.append("#d35400") # P0 Fixed
            else:
                if t_type == "THIN": colors_p1.append("#FFD700")
                else: colors_p1.append("#4169E1")
                
        p1 = PatchCollection(patches_base, match_original=False)
        p1.set_facecolor(colors_p1)
        p1.set_edgecolor('white')
        p1.set_linewidth(lw)
        ax.add_collection(p1)

        _add_legend(ax, [("#FFD700", "Thin Rhombus"), ("#4169E1", "Thick Rhombus"), ("#2c3e50", "Pore"), ("#d35400", "Fixed Defect")], title="Lattice Components", font_size=fonts.get("base_size", 10))
        
        # =========================================================================
        # PANEL 2: Local Energy (Dynamic Scaling)
        # =========================================================================
        ax = axes[1]
        ax.set_title("2. Local Potential Energy\n(Widom Hamiltonian)", fontsize=fonts.get("title_size", 12), fontweight='bold')
        
        energies = []
        
        for tid in ids:
                    # Exclude Pores AND Fixed Defects from the heat scale
                    obs = obs_map.get(tid)
                    if obs == "pore" or obs == "fixed":
                        energies.append(np.nan)
                    else:
                        energies.append(energy_map.get(tid, np.nan))

        valid_energies = [e for e in energies if not np.isnan(e)]
        
        if not valid_energies:
            ax.text(0.5, 0.5, "NO ENERGY DATA", ha='center', transform=ax.transAxes, color='red')
            p2 = PatchCollection(patches_base, facecolor='#EEEEEE', edgecolor='white', linewidth=lw)
        else:
            # P0: Percentile Scaling (Avoid hard clipping)
            vmin, vmax = np.percentile(valid_energies, [5, 95])
            
            p2 = PatchCollection(patches_base, cmap='Spectral_r', edgecolor='white', linewidth=lw)
            p2.set_array(np.array(energies))
            p2.set_clim(vmin=vmin, vmax=vmax)
            
            cbar = plt.colorbar(p2, ax=ax, fraction=0.046, pad=0.04)
            cbar.set_label(f"Local Energy (p5={vmin:.2f}, p95={vmax:.2f})", fontsize=fonts.get("base_size", 10))
        
        ax.add_collection(p2)

        # =========================================================================
        # PANEL 3: Order Parameter (Vertex Class) - P2 Healing Proof
        # =========================================================================
        # FIX: Explicitly switch to the correct panel (axes[2])
        ax = axes[2]
        has_classes = any(c != "UNKNOWN" for c in class_map.values())
        
        colors_p3 = []
        legend_items = []

        if has_classes:
            ax.set_title("3. Vertex Classification\n(Healing Order Parameter)", fontsize=fonts.get("title_size", 12), fontweight='bold')
            
            # FIX: Loop is now correctly indented INSIDE the 'if' block
            for tid in ids:
                cls = class_map.get(tid, "UNKNOWN")
                obs = obs_map.get(tid)
                
                if obs == "pore": colors_p3.append("#2c3e50")
                elif obs == "fixed": colors_p3.append("#d35400") # Distinct Fixed Color
                elif cls == "LOW_ENERGY": colors_p3.append("#2E8B57") # Green
                elif cls == "MEDIUM_ENERGY": colors_p3.append("#F4A460") # Orange
                elif cls == "HIGH_ENERGY": colors_p3.append("#DC143C") # Red
                else: colors_p3.append("lightgray")
            
            # FIX: Define legend once
            legend_items = [("#2E8B57", "Low Energy"), ("#F4A460", "Medium Energy"), ("#DC143C", "High Energy")]

        else:
            ax = axes[2]
            ax.set_title("3. Coordination Topology", fontsize=fonts.get("title_size", 12), fontweight='bold')
            
            colors_p3 = []
            for tid in ids:
                obs = obs_map.get(tid)
                if obs == "pore":
                    colors_p3.append("#2c3e50")
                    continue

                raw_neighbors = adj_graph.get(tid, []) if adj_graph else []

                active_neighbors = set()
                for n in raw_neighbors:
                    try:
                        n = int(n)
                    except Exception:
                        continue
                    if n == tid:
                        continue
                    if obs_map.get(n) == "pore":
                        continue
                    active_neighbors.add(n)

                c = len(active_neighbors)

                if c >= 4: colors_p3.append("#2E8B57")     # Bulk
                elif c == 3: colors_p3.append("#F4A460")   # Surface
                else: colors_p3.append("#DC143C")          # Anomaly

            
            legend_items = [
                ("#2E8B57", "Bulk (Z=4)"), 
                ("#F4A460", "Surface (Z=3)"), 
                ("#DC143C", "Anomaly (Z!=3,4)")
            ]

        p3 = PatchCollection(patches_base, facecolor=colors_p3, edgecolor='white', linewidth=lw)
        ax.add_collection(p3)
        _add_legend(ax, legend_items, title="Order Parameter", font_size=fonts.get("base_size", 10))
        # =========================================================================
        # PANEL 4: Kinetic Growth Front
        # =========================================================================
        ax = axes[3]
        ax.set_title("4. Kinetic Growth Front\n(Propagation State)", fontsize=fonts.get("title_size", 12), fontweight='bold')
        
        colors_p4 = []
        for tid in ids:
            status = growth_map.get(tid)
            obs = obs_map.get(tid)
            if obs == "pore": colors_p4.append("#2c3e50")
            elif obs == "fixed": colors_p4.append("#d35400") # FIX: Distinct color
            elif status == "seed": colors_p4.append("#2ecc71")
            elif status == "grown": colors_p4.append("#3498db")
            elif status == "frontier": colors_p4.append("#f1c40f")
            else: colors_p4.append("#ecf0f1")
                
        p4 = PatchCollection(patches_base, facecolor=colors_p4, edgecolor='white', linewidth=lw)
        ax.add_collection(p4)
        _add_legend(ax, [("#2ecc71", "Seed"), ("#3498db", "Relaxed"), ("#f1c40f", "Frontier"), ("#ecf0f1", "Melt")], title="Kinetic State", font_size=fonts.get("base_size", 10))

        # --- Final Layout ---
        for ax in axes:
            ax.set_aspect('equal')
            ax.set_xlim(xlims)
            ax.set_ylim(ylims)
            ax.axis('off')

        if pub.get("tight_layout", True):
            plt.tight_layout()
            plt.subplots_adjust(top=0.90)
        
        if save_path:
            # FIX: Respect driver's suffix if provided (e.g. if driver requests .pdf)
            sp = Path(save_path)
            if not sp.suffix:
                sp = sp.with_suffix(f".{fmt}")
            
            # Ensure directory exists
            sp.parent.mkdir(parents=True, exist_ok=True)
            
            # FIX: Save ONLY ONCE (Speed up)
            plt.savefig(sp, dpi=dpi, bbox_inches='tight', transparent=transparent)
            
            # Clean print path relative to project
            try:
                project_root = Path(__file__).resolve().parents[2]
                display_path = sp.resolve().relative_to(project_root.resolve())
            except Exception:
                display_path = sp.name
                
            print(f"   📊 Saved Matrix: {display_path}")
            plt.close(fig)
        else:
            plt.show()