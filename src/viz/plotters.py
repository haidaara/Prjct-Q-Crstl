import matplotlib.pyplot as plt
from src.utils.config import ConfigManager  # Fixed import path

class TilingVisualizer:
    """Research-grade visualization for Penrose tilings"""

    def __init__(self, config: ConfigManager):
        self.config = config
        self.viz_config = config.visualization

    def plot_tiling(self, tiling_data: dict, save_path: str = None):
        """Create publication-quality tiling visualization"""
        # Get figsize and ensure it's a tuple
        figsize = self.viz_config.get("figsize", [12, 12])
        if isinstance(figsize, list):
            figsize = tuple(figsize)

        fig, ax = plt.subplots(figsize=figsize)

        tiles = tiling_data["tiles"]
        colors = self.viz_config.get("tile_colors", {"THICK": "red", "THIN": "blue"})

        # Compute counts directly from tiles for reliability
        tile_count = len(tiles)
        thick_count = sum(1 for t in tiles if t["type"] == "THICK")
        thin_count = tile_count - thick_count

        for tile in tiles:
            verts = tile["vertices"]

            # Ensure vertices are in list format for safe concatenation
            if not isinstance(verts, list):
                verts = list(verts)
            poly_verts = verts + [verts[0]]  # Close polygon

            x, y = zip(*poly_verts)

            # Safe color lookup with fallback
            color = colors.get(tile["type"], "gray")

            # Plot edges
            ax.plot(x, y, 'k-', linewidth=0.8, alpha=0.8)
            # Fill tiles with explicit facecolor
            ax.fill(x, y, facecolor=color, alpha=0.4, edgecolor='none')

            # Show tile IDs using lattice_coords if available, otherwise use id
            if self.viz_config.get("show_tile_ids", False):
                # Use lattice_coords for stable, meaningful IDs
                tile_id = tile.get("lattice_coords", tile["id"])
                ax.annotate(str(tile_id), tile["center"],
                            fontsize=6, ha='center', va='center',
                            bbox=dict(boxstyle="round,pad=0.1", fc="white", alpha=0.7))

        self._format_plot(ax, tile_count, thick_count, thin_count)

        if save_path and self.viz_config.get("save_plots", True):
            plt.savefig(save_path, dpi=self.viz_config.get("plot_dpi", 300),
                        bbox_inches='tight')

        plt.show()

    def _format_plot(self, ax, tile_count: int, thick_count: int, thin_count: int):
        """Format the plot with research standards"""
        ax.set_aspect('equal')

        # Use pynrose-specific method description
        title = (f"Penrose P3 Tiling (de Bruijn pentagrid via pynrose)\n"
                 f"Tiles: {tile_count} "
                 f"(Thick: {thick_count}, Thin: {thin_count})")

        ax.set_title(title, fontsize=14)
        ax.set_xlabel("X coordinate", fontsize=12)
        ax.set_ylabel("Y coordinate", fontsize=12)
        ax.grid(True, alpha=0.2)
        plt.tight_layout()