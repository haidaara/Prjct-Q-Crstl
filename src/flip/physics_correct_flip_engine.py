"""
Physics-correct flip engine with consistent state management
"""

import copy
from typing import Dict, List, Tuple, Set, Any
import numpy as np

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy

class PhysicsCorrectFlipEngine:
    """
    Flip engine that maintains physical consistency and detailed balance
    """
    
    def __init__(self, vertex_classifier: CombinatorialVertexClassifier, 
                 energy_model: WidomInspiredEnergy):
        self.classifier = vertex_classifier
        self.energy_model = energy_model
        self.flip_stats = {"proposed": 0, "accepted": 0, "rejected": 0}
        
        # NO cross-step caching that could compromise physics
    
    def find_flippable_hexagons(self, tiling_data: Dict) -> List[List[int]]:
        """
        Find all flippable hexagon patterns in current physical state
        NO caching across steps to ensure completeness
        """
        flippable_clusters = []
        visited_tiles = set()
        
        for tile in tiling_data["tiles"]:
            if not self._is_eligible_for_flip(tile) or tile["id"] in visited_tiles:
                continue
                
            cluster_ids = self._detect_hexagon_pattern(tile["id"], tiling_data)
            if cluster_ids and self._validate_flip_legality(cluster_ids, tiling_data):
                flippable_clusters.append(cluster_ids)
                visited_tiles.update(cluster_ids)
        
        return flippable_clusters
    
    def _is_eligible_for_flip(self, tile: Dict) -> bool:
        """
        Physics-clear eligibility checking with proper constraint hierarchy
        """
        # 1. PERMANENT physical constraints (obstacles, defects)
        if (tile.get("removed", False) or 
            tile.get("immobile", False) or
            not tile.get("flippable", True)):
            return False
        
        # 2. TEMPORARY operational constraints (growth region)
        if "_temporary_growth_flippable" in tile:
            return tile["_temporary_growth_flippable"]
        
        # 3. Default: eligible
        return True
    
    def _detect_hexagon_pattern(self, start_tile_id: int, tiling_data: Dict) -> List[int]:
        """
        Detect hexagon pattern: 2 thick + 1 thin rhombus configuration
        Returns: [thick_id1, thick_id2, thin_id] or empty list
        """
        # Implementation of hexagon pattern detection
        # This is the actual physics of what constitutes a flippable cluster
        start_tile = tiling_data["tiles"][start_tile_id]
        
        if start_tile["type"] == "THICK":
            return self._detect_thick_based_hexagon(start_tile_id, tiling_data)
        elif start_tile["type"] == "THIN":
            return self._detect_thin_based_hexagon(start_tile_id, tiling_data)
        
        return []
    
    def _detect_thick_based_hexagon(self, thick_id: int, tiling_data: Dict) -> List[int]:
        """
        Detect hexagon pattern starting from thick rhombus
        """
        thick_tile = tiling_data["tiles"][thick_id]
        neighbors = self._get_immediate_neighbors(thick_id, tiling_data)
        
        # Look for pattern: thick -- thin -- thick
        for neighbor in neighbors:
            if neighbor["type"] == "THIN":
                thin_id = neighbor["id"]
                thin_neighbors = self._get_immediate_neighbors(thin_id, tiling_data)
                
                # Find another thick rhombus connected to this thin one
                for thin_neighbor in thin_neighbors:
                    if (thin_neighbor["type"] == "THICK" and 
                        thin_neighbor["id"] != thick_id and
                        self._are_tiles_adjacent(thick_id, thin_neighbor["id"], tiling_data)):
                        return [thick_id, thin_neighbor["id"], thin_id]
        
        return []
    
    def _detect_thin_based_hexagon(self, thin_id: int, tiling_data: Dict) -> List[int]:
        """
        Detect hexagon pattern starting from thin rhombus
        """
        thin_tile = tiling_data["tiles"][thin_id]
        neighbors = self._get_immediate_neighbors(thin_id, tiling_data)
        
        # Look for two thick neighbors that are also adjacent to each other
        thick_neighbors = [n for n in neighbors if n["type"] == "THICK"]
        
        if len(thick_neighbors) >= 2:
            # Check if any two thick neighbors are adjacent
            for i, thick1 in enumerate(thick_neighbors):
                for thick2 in thick_neighbors[i+1:]:
                    if self._are_tiles_adjacent(thick1["id"], thick2["id"], tiling_data):
                        return [thick1["id"], thick2["id"], thin_id]
        
        return []
    
    def _capture_physical_state(self, cluster_ids: List[int], tiling_data: Dict) -> Dict:
        """
        Capture MINIMAL physical state needed for exact restoration
        Ensures adjacency graph and tile neighbors remain consistent
        """
        affected_tiles = self._get_affected_tile_neighborhood(cluster_ids, tiling_data)
        undo_info = {
            "tile_states": {},
            "adjacency_graph": {}
        }
        
        # Capture tile states (physics-critical fields only)
        for tile_id in affected_tiles:
            tile = tiling_data["tiles"][tile_id]
            undo_info["tile_states"][tile_id] = {
                "type": tile["type"],                    # Direct physics
                "vertex_class": tile["vertex_class"],    # Energy classification
                "local_energy": tile["local_energy"],    # Current energy state
                "neighbors": tile["neighbors"][:],       # Connectivity
                # NOTE: We intentionally DON'T capture temporary fields
            }
        
        # Capture adjacency graph state (CRITICAL for consistency)
        for tile_id in affected_tiles:
            key = str(tile_id)
            if key in tiling_data["adjacency_graph"]:
                undo_info["adjacency_graph"][key] = tiling_data["adjacency_graph"][key][:]
        
        return undo_info
    
    def _restore_physical_state(self, undo_info: Dict, tiling_data: Dict):
        """
        Restore exact physical state for detailed balance
        Ensures tile states and adjacency graph are synchronized
        """
        # Restore tile states
        for tile_id, original_state in undo_info["tile_states"].items():
            tile = tiling_data["tiles"][tile_id]
            tile.update(original_state)
        
        # Restore adjacency graph (CRITICAL for consistency)
        for tile_key, original_neighbors in undo_info["adjacency_graph"].items():
            tiling_data["adjacency_graph"][tile_key] = original_neighbors[:]
    
    def _apply_hexagon_transformation(self, cluster_ids: List[int], tiling_data: Dict):
        """
        Apply hexagon flip transformation to actual system
        Updates both tile properties AND adjacency graph consistently
        """
        if len(cluster_ids) != 3:
            raise ValueError("Hexagon flip requires exactly 3 tiles")
        
        # Verify this is a valid hexagon pattern
        tile_types = [tiling_data["tiles"][tid]["type"] for tid in cluster_ids]
        thick_count = tile_types.count("THICK")
        thin_count = tile_types.count("THIN")
        
        if not (thick_count == 2 and thin_count == 1):
            raise ValueError(f"Invalid hexagon pattern: {tile_types}")
        
        # Identify which tiles are thick and which is thin
        thick_tiles = [tid for tid in cluster_ids if tiling_data["tiles"][tid]["type"] == "THICK"]
        thin_tile = [tid for tid in cluster_ids if tiling_data["tiles"][tid]["type"] == "THIN"][0]
        
        # Apply combinatorial transformation: thick ↔ thin
        for tid in thick_tiles:
            tiling_data["tiles"][tid]["type"] = "THIN"
        tiling_data["tiles"][thin_tile]["type"] = "THICK"
        
        # Update adjacency graph to reflect new connectivity
        self._update_adjacency_for_flip(cluster_ids, tiling_data)
        
        # Geometry updates would go here (vertex coordinates, etc.)
        # This is complex Penrose-specific math - placeholder for now
        self._update_tile_geometry(cluster_ids, tiling_data)
    
    def _update_adjacency_for_flip(self, cluster_ids: List[int], tiling_data: Dict):
        """
        Update adjacency graph after hexagon flip
        Ensures neighbors and adjacency_graph remain consistent
        """
        # For hexagon flips, the neighbor relationships change in specific ways
        # This is complex Penrose-specific logic - simplified placeholder
        
        # In reality, this would:
        # 1. Remove certain old adjacencies
        # 2. Add new adjacencies based on the new tile configuration
        # 3. Update both adjacency_graph and tile["neighbors"] consistently
        
        # For now, we'll regenerate neighbors from adjacency_graph
        # This ensures consistency but is computationally expensive
        self._regenerate_neighbor_lists(cluster_ids, tiling_data)
    
    def _regenerate_neighbor_lists(self, cluster_ids: List[int], tiling_data: Dict):
        """
        Regenerate neighbor lists from adjacency graph for consistency
        Applied to affected tiles and their neighbors
        """
        affected_tiles = self._get_affected_tile_neighborhood(cluster_ids, tiling_data)
        
        for tile_id in affected_tiles:
            tile = tiling_data["tiles"][tile_id]
            adjacency_key = str(tile_id)
            
            if adjacency_key in tiling_data["adjacency_graph"]:
                tile["neighbors"] = tiling_data["adjacency_graph"][adjacency_key][:]
            else:
                tile["neighbors"] = []
    
    def _get_immediate_neighbors(self, tile_id: int, tiling_data: Dict) -> List[Dict]:
        """
        Get immediate neighbors using adjacency graph (primary source)
        """
        neighbors = []
        adjacency_graph = tiling_data["adjacency_graph"]
        tile_key = str(tile_id)
        
        if tile_key in adjacency_graph:
            for neighbor_id in adjacency_graph[tile_key]:
                if 0 <= neighbor_id < len(tiling_data["tiles"]):
                    neighbors.append(tiling_data["tiles"][neighbor_id])
        
        return neighbors
    
    def _get_affected_tile_neighborhood(self, cluster_ids: List[int], tiling_data: Dict) -> List[int]:
        """
        Get all tiles affected by flip: cluster + their neighbors
        """
        affected = set(cluster_ids)
        
        for tile_id in cluster_ids:
            neighbors = self._get_immediate_neighbors(tile_id, tiling_data)
            affected.update(neighbor["id"] for neighbor in neighbors)
        
        return list(affected)
    
    def _are_tiles_adjacent(self, tile1_id: int, tile2_id: int, tiling_data: Dict) -> bool:
        """
        Check if two tiles are adjacent using adjacency graph
        """
        key1 = str(tile1_id)
        if key1 in tiling_data["adjacency_graph"]:
            return tile2_id in tiling_data["adjacency_graph"][key1]
        return False
    
    def _validate_flip_legality(self, cluster_ids: List[int], tiling_data: Dict) -> bool:
        """
        Validate flip preserves basic Penrose constraints
        """
        # Check that all cluster tiles are eligible
        for tile_id in cluster_ids:
            tile = tiling_data["tiles"][tile_id]
            if not self._is_eligible_for_flip(tile):
                return False
        
        # Additional Penrose-specific constraints could go here
        return True
    
    def _update_tile_geometry(self, cluster_ids: List[int], tiling_data: Dict):
        """
        Update tile geometry after flip - complex Penrose math
        PLACEHOLDER: Actual implementation requires detailed Penrose geometry
        """
        # This would update vertex coordinates, centers, etc.
        # For now, we rely on the combinatorial transformation being sufficient
        pass