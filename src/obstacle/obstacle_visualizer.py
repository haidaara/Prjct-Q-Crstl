"""
High-performance obstacle visualization for research analysis.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict
from src.utils.config import ConfigManager

class ObstacleVisualizer:
    """Research-grade obstacle visualization"""
    
    def __init__(self, config: ConfigManager):
        self.config = config
        self.viz_config = config.visualization
        
    def plot_obstacles(self, tiling_data: Dict, save_path: str = None):
        """Create publication-quality obstacle visualization"""
        fig, ax = plt.subplots(figsize=self._get_figsize())

        tiles = tiling_data["tiles"]
        obstacle_meta = tiling_data.get("obstacle_metadata", {})

        # SET CONSISTENT AXES BASED ON WINDOW SIZE
        meta = tiling_data.get("metadata", {})
        origin = meta.get("window_origin", [0.0, 0.0])
        size = meta.get("window_size", [60.0, 60.0])
        ax.set_xlim(origin[0], origin[0] + size[0])
        ax.set_ylim(origin[1], origin[1] + size[1])

        # Plot active tiles
        active_tiles = [t for t in tiles if not t.get("removed", False)]
        self._plot_tile_collection(ax, active_tiles, "active")

        # Plot obstacles
        self._plot_obstacles(ax, tiling_data)

        self._format_obstacle_plot(ax, tiling_data, obstacle_meta)

        if save_path and self.viz_config.get("save_plots", True):
            dpi = self.viz_config.get("plot_dpi", 300)  # RESPECT CONFIG DPI
            plt.savefig(save_path, dpi=dpi, bbox_inches='tight', facecolor='white')

        # Non-blocking plot display
        if self.viz_config.get("show_plots", False):
            plt.show()
        else:
            plt.close(fig)
    
    def _plot_tile_collection(self, ax, tiles, tile_type):
        """Optimized tile plotting"""
        colors = self.viz_config.get("tile_colors", {"THICK": "red", "THIN": "blue"})
        obstacle_colors = self.viz_config.get("obstacle_colors", {})
        
        for tile in tiles:
            verts = tile["vertices"]
            poly_verts = verts + [verts[0]]
            x, y = zip(*poly_verts)
            
            if tile.get("immobile", False):
                color = obstacle_colors.get("fixed_defect", "orange")
                alpha = 0.8
            else:
                color = colors.get(tile["type"], "gray") 
                alpha = 0.4
                
            ax.fill(x, y, facecolor=color, alpha=alpha, edgecolor='black', linewidth=0.5)
    
    def _plot_obstacles(self, ax, tiling_data: Dict):
        """Plot obstacle regions with proper styling and clipping"""
        obstacle_meta = tiling_data.get("obstacle_metadata", {})
        obstacle_colors = self.viz_config.get("obstacle_colors", {})
        
        if obstacle_meta.get("type") == "pores":
            pore_color = obstacle_colors.get("pore", "black")  # RESPECT CONFIG COLOR
            for center, radius in zip(obstacle_meta["positions"], obstacle_meta["radii"]):
                circle = plt.Circle(center, radius, color=pore_color, linewidth=2, 
                                  fill=False, linestyle='--')  # EDGE-ONLY
                circle.set_clip_path(ax.patch)  # CLIP TO BOUNDARIES
                ax.add_patch(circle)
    
    def _format_obstacle_plot(self, ax, tiling_data: Dict, obstacle_meta: Dict):
        """Research-grade plot formatting"""
        ax.set_aspect('equal')
        
        tile_count = len(tiling_data["tiles"])
        removed_count = obstacle_meta.get("removed_count", 0)
        immobile_count = obstacle_meta.get("immobile_count", 0)
        
        title = (f"Penrose Tiling with {obstacle_meta.get('type', 'obstacles').replace('_', ' ').title()}\n"
                f"Density: {obstacle_meta.get('density', 0):.3f} | "
                f"Active: {tile_count - removed_count} | "
                f"Removed: {removed_count} | Fixed: {immobile_count}")
                
        ax.set_title(title, fontsize=12, pad=20)
        ax.set_xlabel("X coordinate")
        ax.set_ylabel("Y coordinate")
        ax.grid(True, alpha=0.2)
        plt.tight_layout()
    
    def _get_figsize(self):
        """Get optimized figure size"""
        figsize = self.viz_config.get("figsize", [12, 12])
        return tuple(figsize) if isinstance(figsize, list) else figsize