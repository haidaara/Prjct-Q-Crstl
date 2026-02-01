# src/simulation/growth_engine.py
"""
Growth simulator with working constraints and config-driven parameters
"""

from typing import Dict, List, Set, Any, Tuple, Optional
import numpy as np

class GrowthSimulator:
    """
    Simulator for growth front propagation with healing
    """
    
    def __init__(self, mc_engine, config: Optional[Dict] = None):
        self.mc_engine = mc_engine
        self.config = config or {}
        self.growth_step = 0
        self.growth_history = []
        
        # Configurable parameters
        self.seed_radius = self.config.get("seed_radius", 5.0)
        self.mc_steps_per_growth = self.config.get("mc_steps_per_growth", 100)
        self.healing_radius = self.config.get("healing_radius", 2.0)
    
    def initialize_seed(self, tiling_data: Dict, seed_center: Optional[List[float]] = None) -> Dict:
        """Initialize growth from seed region with configurable center"""
        print("   Initializing growth seed...")
        
        # Reset all tiles to ungrown state
        for tile in tiling_data["tiles"]:
            if not tile.get("removed", False):
                tile["growth_status"] = "ungrown"
                tile["flippable"] = True  # Default flippable
        
        # Use provided center or window center
        if seed_center is None:
            window_size = tiling_data.get("window_size", [60.0, 60.0])
            seed_center = [window_size[0] / 2, window_size[1] / 2]
        
        # Set seed region
        seed_tiles = self._find_tiles_in_radius(seed_center, self.seed_radius, tiling_data)
        for tile in seed_tiles:
            tile["growth_status"] = "seed"
        
        self._update_frontier(tiling_data)
        
        seed_count = len(seed_tiles)
        print(f"   Growth seed: {seed_count} tiles initialized at {seed_center}")
        
        return tiling_data
    
    def grow_step(self, tiling_data: Dict, obstacles: Dict) -> Tuple[Dict, List[int], Dict]:
        """Single growth step with healing - returns MC stats"""
        print(f"   Growth step {self.growth_step}...")
        
        try:
            # Apply temporary growth constraints (CRITICAL FIX)
            self._apply_growth_constraints(tiling_data)
            
            # Run MC healing with configurable steps (CRITICAL FIX)
            print(f"   Running {self.mc_steps_per_growth} MC steps for healing...")
            mc_stats = self.mc_engine.run_sweep(tiling_data, steps=self.mc_steps_per_growth)
            
            # Add new growth layer
            new_tiles = self._add_growth_layer(tiling_data, obstacles)
            
            # Update growth frontier
            self._update_frontier(tiling_data)
            
        finally:
            # Remove temporary constraints
            self._remove_constraints(tiling_data)
        
        self.growth_step += 1
        step_data = {
            "step": self.growth_step,
            "new_tiles": len(new_tiles),
            "total_energy": self.mc_engine.current_energy,
            "mc_stats": mc_stats
        }
        self.growth_history.append(step_data)
        
        print(f"   Growth step {self.growth_step}: added {len(new_tiles)} tiles")
        
        return tiling_data, new_tiles, mc_stats
    
    def _apply_growth_constraints(self, tiling_data: Dict):
        """
        CRITICAL FIX: Actually constrain flips by modifying tile["flippable"]
        The flip engine uses tile["flippable"] to determine allowed flips
        """
        for tile in tiling_data["tiles"]:
            if tile.get("removed", False):
                continue
            
            # IMMOBILE AND PORE TILES ARE NEVER FLIPPABLE
            if tile.get("immobile", False) or tile.get("obstacle_type") == "pore":
                tile["flippable"] = False
                continue
            
            # Backup original flippable state once
            if "_flippable_backup" not in tile:
                tile["_flippable_backup"] = tile.get("flippable", True)
            
            # Determine if tile should be flippable during this growth step
            # Active region: seed, grown, frontier, recently_grown
            in_active = tile["growth_status"] in ["seed", "grown", "frontier", "recently_grown"]
            
            # Healing extension: allow immediate neighbors of active region
            if not in_active and tile["growth_status"] == "ungrown":
                neighbors = self._get_neighbors(tile["id"], tiling_data)
                if any(n["growth_status"] in ["seed", "grown", "frontier", "recently_grown"] 
                       for n in neighbors):
                    in_active = True
            
            # Apply constraint: flip engine reads tile["flippable"]
            tile["flippable"] = in_active
    
    def _remove_constraints(self, tiling_data: Dict):
        """Restore original flippable state, except for immobile/pore tiles"""
        for tile in tiling_data["tiles"]:
            if tile.get("removed", False):
                continue
            
            # Skip immobile/pore tiles - they stay False
            if tile.get("immobile", False) or tile.get("obstacle_type") == "pore":
                continue
            
            if "_flippable_backup" in tile:
                tile["flippable"] = tile["_flippable_backup"]
                del tile["_flippable_backup"]
    
    def _add_growth_layer(self, tiling_data: Dict, obstacles: Dict) -> List[int]:
        """Add new growth layer around current frontier"""
        new_tile_ids = []
        frontier_tiles = self._get_frontier_tiles(tiling_data)
        
        for tile in frontier_tiles:
            neighbors = self._get_neighbors(tile["id"], tiling_data)
            
            for neighbor in neighbors:
                if (neighbor["growth_status"] == "ungrown" and 
                    not neighbor.get("removed", False) and
                    self._can_grow_into(neighbor, obstacles)):
                    
                    neighbor["growth_status"] = "recently_grown"
                    neighbor["flippable"] = True  # Newly grown tiles start flippable
                    new_tile_ids.append(neighbor["id"])
        
        return new_tile_ids
    
    def _get_neighbors(self, tile_id: int, tiling_data: Dict) -> List[Dict]:
        """
        Get neighbors using adjacency graph directly
        No longer relies on nonexistent flip_engine method
        """
        neighbors = []
        adjacency_graph = tiling_data["adjacency_graph"]
        
        tile_key = str(tile_id)
        if tile_key in adjacency_graph:
            neighbor_ids = adjacency_graph[tile_key]
            for nid in neighbor_ids:
                nid_int = int(nid) if isinstance(nid, str) else nid
                if 0 <= nid_int < len(tiling_data["tiles"]):
                    neighbors.append(tiling_data["tiles"][nid_int])
        
        return neighbors
    
    def _get_frontier_tiles(self, tiling_data: Dict) -> List[Dict]:
        """Get current frontier tiles"""
        return [tile for tile in tiling_data["tiles"] 
                if tile["growth_status"] == "frontier"]
    
    def _update_frontier(self, tiling_data: Dict):
        """Update growth frontier"""
        # Reset frontier status
        for tile in tiling_data["tiles"]:
            if tile.get("removed", False):
                continue
            if tile["growth_status"] == "frontier":
                tile["growth_status"] = "grown"
        
        # Find new frontier
        for tile in tiling_data["tiles"]:
            if tile.get("removed", False):
                continue
            if tile["growth_status"] in ["grown", "seed", "recently_grown"]:
                neighbors = self._get_neighbors(tile["id"], tiling_data)
                for neighbor in neighbors:
                    if neighbor["growth_status"] == "ungrown":
                        tile["growth_status"] = "frontier"
                        break
    
    def _find_tiles_in_radius(self, center: List[float], radius: float, 
                            tiling_data: Dict) -> List[Dict]:
        """Find tiles within radius of center point"""
        center_array = np.array(center)
        tiles_in_radius = []
        
        for tile in tiling_data["tiles"]:
            if tile.get("removed", False):
                continue
            tile_center = np.array(tile["center"])
            distance = np.linalg.norm(tile_center - center_array)
            if distance <= radius:
                tiles_in_radius.append(tile)
        
        return tiles_in_radius
    
    def _can_grow_into(self, tile: Dict, obstacles: Dict) -> bool:
        """Check if growth can proceed into this tile"""
        if tile.get("immobile", False):
            return False
        if tile.get("obstacle_type") == "pore":
            return False
        return True
    
    def get_diagnostics(self) -> Dict[str, Any]:
        """Return growth diagnostics"""
        return {
            "current_step": self.growth_step,
            "growth_history": self.growth_history,
            "config": {
                "seed_radius": self.seed_radius,
                "mc_steps_per_growth": self.mc_steps_per_growth,
                "healing_radius": self.healing_radius
            }
        }