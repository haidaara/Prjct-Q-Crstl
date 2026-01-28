# src/obstacle/obstacle_creator.py
"""
High-performance obstacle creation with spatial indexing for research scalability.
"""

import numpy as np
import copy
from typing import List, Dict, Tuple, Any
from dataclasses import dataclass
from src.utils.config import ConfigManager

# Optional KDTree for performance
try:
    from scipy.spatial import cKDTree as KDTree
except ImportError:
    KDTree = None
    print("⚠️  SciPy not available - using fallback spatial indexing (recommend install for large tilings)")

@dataclass
class ObstacleSpec:
    """Efficient obstacle specification for scalable studies"""
    type: str
    positions: List[Tuple[float, float]]  # Optional for fixed_defects
    radii: List[float]  # Optional for fixed_defects  
    density: float

class ObstacleCreator:
    """High-performance obstacle creation with spatial indexing"""
    
    def __init__(self, config: ConfigManager):
        self.config = config
        self.obstacle_config = config.obstacles
        self._tile_tree = None
        self._tile_centers = None
        self._id_to_index = None
        
    def create_obstacles(self, tiling_data: Dict, obstacle_spec: ObstacleSpec) -> Dict:
        """Main entry point - create obstacles with optimal performance"""
        print(f"🚀 Creating {obstacle_spec.type} obstacles (density: {obstacle_spec.density})")
        
        # Build spatial index for lightning-fast lookups
        self._build_spatial_index(tiling_data)
        
        # Deep copy with efficient serialization
        modified_tiling = self._fast_deep_copy(tiling_data)

        # Preserve original topology BEFORE pores remove links
        for tile in modified_tiling["tiles"]:
            tile.setdefault("neighbors_full", list(tile.get("neighbors", [])))

        
        # CRITICAL: Initialize ALL physics fields consistently
        for tile in modified_tiling["tiles"]:
            tile.setdefault("removed", False)
            tile.setdefault("immobile", False)
            tile.setdefault("obstacle_type", "none")

            # Preserve provenance once (MUST happen before pores set growth_status="removed")
            tile.setdefault("growth_status_original", "grown")

            # WEEK 1 PHYSICS FIELDS:
            tile.setdefault("vertex_class", "LOW_ENERGY")
            tile.setdefault("local_energy", 0.0)

            # Obstacle stage baseline is a fully-grown tiling (safer with treat_ungrown_as_vacuum)
            tile.setdefault("growth_status", "grown")

            tile.setdefault("flippable", True)

        
        if obstacle_spec.type == "pores":
            result = self._create_pores_optimized(modified_tiling, obstacle_spec)
        else:
            result = self._create_fixed_defects_optimized(modified_tiling, obstacle_spec)
            
        return self._finalize_obstacle_data(result, obstacle_spec)
    
    def _build_spatial_index(self, tiling_data: Dict):
        """Build KDTree for O(log n) tile lookups with normalized integer IDs"""
        tiles = tiling_data["tiles"]
        self._tile_centers = np.array([tile["center"] for tile in tiles])
        
        if KDTree is not None and len(tiles) > 1000:
            self._tile_tree = KDTree(self._tile_centers)
            print("📊 Built spatial index with KDTree")
        else:
            self._tile_tree = None
            if len(tiles) > 1000:
                print("📊 Using fallback spatial indexing (SciPy recommended for large tilings)")
        
        # Build ID to index mapping with normalized integer keys
        self._id_to_index = {int(tile["id"]): i for i, tile in enumerate(tiles)}  # NORMALIZED TO INT
    
    def _create_pores_optimized(self, tiling_data: Dict, spec: ObstacleSpec) -> Dict:
        """Optimized pore creation using spatial queries"""
        # Validate input
        if len(spec.positions) != len(spec.radii):
            raise ValueError("Mismatch: positions and radii must have equal length for pores")
        
        tiles = tiling_data["tiles"]
        removed_mask = np.zeros(len(tiles), dtype=bool)
        
        for center, radius in zip(spec.positions, spec.radii):
            center_array = np.array(center)
            
            # Find tiles within radius using optimal method
            if self._tile_tree is not None:
                indices = self._tile_tree.query_ball_point(center_array, radius)
            else:
                # Fallback: manual distance calculation
                distances = np.linalg.norm(self._tile_centers - center_array, axis=1)
                indices = np.where(distances <= radius)[0].tolist()
            
            removed_mask[indices] = True
        
        # Apply removals in batch
        removed_count = 0
        for i, tile in enumerate(tiles):
            if removed_mask[i]:
                    tile["removed"] = True
                    tile["obstacle_type"] = "pore"

                    # Truthful semantics for downstream viz/metrics
                    tile["growth_status"] = "removed"
                    tile["vertex_class"] = "VACUUM"
                    tile["energy_class"] = "VACUUM"
                    tile["boundary_kind"] = "vacuum"
                    tile["is_boundary"] = False

                    # Ensure pores do not contribute energy terms
                    tile["local_energy"] = 0.0
                    tile["surface_energy"] = 0.0
                    tile["missing_bonds"] = 0
                    tile["phason_energy"] = 0.0
                    tile["surface_contribution"] = 0.0
                    tile["bulk_energy"] = 0.0

                    tile["flippable"] = False
                    removed_count += 1

                
        print(f"   → Removed {removed_count} tiles within {len(spec.positions)} pore regions")
        self._update_adjacency_batch(tiling_data, removed_mask)
        return tiling_data
    
    def _create_fixed_defects_optimized(self, tiling_data: Dict, spec: ObstacleSpec) -> Dict:
        """Deterministic fixed defect placement"""
        tiles = tiling_data["tiles"]
    
        # Sample every nth tile for deterministic placement
        active_indices = [
            i for i, t in enumerate(tiles)
            if (not t.get("removed", False))
            and t.get("flippable", True)
            and (not t.get("immobile", False))
            and len(t.get("neighbors_full", t.get("neighbors", []))) == 4  # exclude outer boundary
        ]

        n_target = max(1, int(round(spec.density * len(active_indices))))
    
        if n_target > len(active_indices):
            n_target = len(active_indices)
    
        # Simple deterministic selection - every k-th tile
        step = max(1, len(active_indices) // n_target)
        chosen_indices = [active_indices[i] for i in range(0, len(active_indices), step)][:n_target]
    
        for idx in chosen_indices:
            tiles[idx]["immobile"] = True
            tiles[idx]["obstacle_type"] = "fixed_defect"
            # CRITICAL: Fixed defects can have energy but cannot flip
            tiles[idx]["flippable"] = False
            tiles[idx]["growth_status"] = "grown"  # ensures it never becomes “vacuum” if treat_ungrown_as_vacuum flips

    
        defects_created = len(chosen_indices)
        print(f"   → Created {defects_created} fixed defects (target: {n_target})")
        return tiling_data
    
    def _update_adjacency_batch(self, tiling_data: Dict, removed_mask: np.ndarray):
        """Batch update adjacency graph for optimal performance with proper blanking"""
        adjacency_graph = tiling_data["adjacency_graph"]
        tiles = tiling_data["tiles"]
        
        # First: blank removed tiles completely
        for tile_id, neighbors in list(adjacency_graph.items()):
            # Convert to integer if needed
            tile_id_int = int(tile_id) if isinstance(tile_id, str) else tile_id
            
            # Blank removed tiles entirely
            if removed_mask[self._id_to_index[tile_id_int]]:
                adjacency_graph[tile_id] = []  # Critical: removed tiles have no neighbors
                continue
                
            # For active tiles: keep only non-removed neighbors
            adjacency_graph[tile_id] = sorted([
                int(n) for n in neighbors 
                if not removed_mask[self._id_to_index[int(n)]]
            ])
        # Update tile neighbor lists
        for i, tile in enumerate(tiles):
            # NEW: preserve original neighbor ids before pruning (for truthful diagnostics/classification)
            tile.setdefault("neighbors_full", [int(n) for n in tile.get("neighbors", [])])

            if removed_mask[i]:
                tile["neighbors"] = []  # Critical: removed tiles have no neighbors
                tile["flippable"] = False

                # --- Option 1: VACUUM semantics override (truthful-by-default) ---
                tile.setdefault("growth_status_original", "grown")

                tile["growth_status"] = "removed"
                tile["boundary_kind"] = "vacuum"
                tile["vertex_class"] = "VACUUM"
                tile["energy_class"] = "VACUUM"
                tile["is_boundary"] = False

                # Ensure vacuum energetics stay strictly zero
                tile["local_energy"] = 0.0
                tile["surface_energy"] = 0.0
                tile["missing_bonds"] = 0
                tile["phason_energy"] = 0.0
                tile["strain"] = 0.0
                tile["surface_contribution"] = 0.0
                tile["bulk_energy"] = 0.0


            
            else:
                tile["neighbors"] = sorted([
                    int(n) for n in tile["neighbors_full"]
                    if not removed_mask[self._id_to_index[int(n)]]
                ])

                
    def _fast_deep_copy(self, data: Dict) -> Dict:
        """Optimized deep copy preserving integer keys"""
        return copy.deepcopy(data)
    
    def _finalize_obstacle_data(self, tiling_data: Dict, spec: ObstacleSpec) -> Dict:
        """Add research metadata efficiently"""
        tiles = tiling_data["tiles"]

        # Canonicalize topology ordering across obstacle types (deterministic + compare-safe)
        if "adjacency_graph" in tiling_data:
            tiling_data["adjacency_graph"] = {
                str(k): sorted(int(n) for n in v)
                for k, v in tiling_data["adjacency_graph"].items()
            }

        for tile in tiles:
            if "neighbors" in tile and tile["neighbors"] is not None:
                tile["neighbors"] = sorted(int(n) for n in tile["neighbors"])
            if "neighbors_full" in tile and tile["neighbors_full"] is not None:
                # Keep original order (do NOT sort), but ensure ints
                tile["neighbors_full"] = [int(n) for n in tile["neighbors_full"]]

        # Defensive: keep outputs truthful for viz/metrics
        for tile in tiles:

            if tile.get("removed", False):
                tile["growth_status"] = "removed"
                tile["boundary_kind"] = "vacuum"
                tile["vertex_class"] = "VACUUM"
                tile["energy_class"] = "VACUUM"
                tile["flippable"] = False
                tile["is_boundary"] = False
                tile["neighbors"] = []

                # Defensive vacuum energetics (export-safe even if earlier steps change later)
                tile["local_energy"] = 0.0
                tile["surface_energy"] = 0.0
                tile["missing_bonds"] = 0
                tile["phason_energy"] = 0.0
                tile["strain"] = 0.0
                tile["surface_contribution"] = 0.0
                tile["bulk_energy"] = 0.0


        removed_count = sum(1 for tile in tiles if tile.get("removed", False))
        immobile_count = sum(1 for tile in tiles if tile.get("immobile", False))

        
        tiling_data["obstacle_metadata"] = {
            "type": spec.type,
            "density": spec.density,
            "positions": spec.positions,
            "radii": spec.radii if spec.type == "pores" else None,
            "positions_semantics": "centers for pores; unused for fixed_defects",
            "removed_count": removed_count,
            "immobile_count": immobile_count,
            "active_tiles": len(tiles) - removed_count
        }
        
        return tiling_data

def adjacency_intkeys_to_str(adjacency_dict: Dict) -> Dict[str, List[int]]:
    """Convert adjacency graph integer keys to strings for JSON export"""
    return {str(k): [int(x) for x in v] for k, v in adjacency_dict.items()}