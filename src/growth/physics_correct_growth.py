"""
Physics-correct growth simulator with clear constraint semantics
"""

from typing import Dict, List, Set, Any
import numpy as np

class PhysicsCorrectGrowthSimulator:
    """
    Growth simulator that maintains clear physics semantics
    Uses temporary constraints without affecting permanent physics
    """
    
    def __init__(self, mc_engine):
        self.mc_engine = mc_engine
        self.growth_step = 0
        self.growth_history = []
    
    def initialize_growth_seed(self, tiling_data: Dict, seed_center: List[float], 
                             radius: float = 5.0) -> Dict:
        """
        Initialize growth using physics-clear field semantics
        """
        print("🌱 Initializing growth seed...")
        
        # Reset all tiles to ungrown state
        for tile in tiling_data["tiles"]:
            if not tile.get("removed", False):  # Don't modify pores
                tile["growth_status"] = "ungrown"
                tile["flippable"] = True  # Default physical state
        
        # Set seed region (physics: these tiles exist from beginning)
        seed_tiles = self._find_tiles_in_radius(seed_center, radius, tiling_data)
        for tile in seed_tiles:
            tile["growth_status"] = "seed"
        
        # Initialize growth frontier
        self._update_growth_frontier(tiling_data)
        
        seed_count = len(seed_tiles)
        print(f"✅ Growth seed: {seed_count} tiles initialized")
        
        return tiling_data
    
    def propagate_growth_front(self, tiling_data: Dict, obstacles: Dict) -> Tuple[Dict, List[int]]:
        """
        Single growth step with physics-correct constraint handling
        Returns: (updated_tiling, new_tile_ids)
        """
        print(f"🌿 Growth step {self.growth_step}...")
        
        # NO NEED to save/restore permanent physics fields
        # Use temporary operational constraints only
        
        try:
            # 1. Apply TEMPORARY growth region constraints
            self._apply_temporary_growth_constraints(tiling_data)
            
            # 2. Run MC healing on ACTUAL system with temporary constraints
            self.mc_engine.run_mc_sweep(tiling_data, steps=100)
            
            # 3. Add new growth layer (modifies PERMANENT physics fields)
            new_tiles = self._add_growth_layer(tiling_data, obstacles)
            
            # 4. Update growth frontier
            self._update_growth_frontier(tiling_data)
            
        finally:
            # 5. CLEANUP: Remove TEMPORARY constraints only
            self._remove_temporary_constraints(tiling_data)
        
        self.growth_step += 1
        self.growth_history.append({
            "step": self.growth_step,
            "new_tiles": len(new_tiles),
            "total_energy": self.mc_engine.current_energy
        })
        
        print(f"✅ Growth step {self.growth_step}: added {len(new_tiles)} tiles, "
              f"E={self.mc_engine.current_energy:.2f}")
        
        return tiling_data, new_tiles
    
    def _apply_temporary_growth_constraints(self, tiling_data: Dict):
        """
        Apply TEMPORARY operational constraints without affecting physics
        """
        for tile in tiling_data["tiles"]:
            if tile.get("removed", False):
                continue
                
            # Temporary constraint: only allow flips in growth region
            tile["_temporary_growth_flippable"] = (
                tile["growth_status"] in ["frontier", "recently_grown"]
            )
    
    def _remove_temporary_constraints(self, tiling_data: Dict):
        """
        Remove TEMPORARY constraints without affecting permanent physics
        """
        for tile in tiling_data["tiles"]:
            if "_temporary_growth_flippable" in tile:
                del tile["_temporary_growth_flippable"]
    
    def _add_growth_layer(self, tiling_data: Dict, obstacles: Dict) -> List[int]:
        """
        Add new growth layer around current frontier
        Modifies PERMANENT physics fields (growth_status, flippable)
        """
        new_tile_ids = []
        frontier_tiles = self._get_frontier_tiles(tiling_data)
        
        for tile in frontier_tiles:
            # Find ungrown neighbors that can be added
            neighbors = self.mc_engine.flip_engine._get_immediate_neighbors(tile["id"], tiling_data)
            
            for neighbor in neighbors:
                if (neighbor["growth_status"] == "ungrown" and 
                    not neighbor.get("removed", False) and
                    self._can_grow_into_tile(neighbor, obstacles)):
                    
                    # PERMANENT physics change: this tile now exists
                    neighbor["growth_status"] = "recently_grown"
                    neighbor["flippable"] = True  # New tiles start flippable
                    new_tile_ids.append(neighbor["id"])
        
        return new_tile_ids
    
    def _update_growth_frontier(self, tiling_data: Dict):
        """
        Update growth frontier based on current growth status
        """
        # Reset frontier status
        for tile in tiling_data["tiles"]:
            if tile["growth_status"] == "frontier":
                tile["growth_status"] = "grown"
        
        # Find new frontier: grown tiles adjacent to ungrown tiles
        for tile in tiling_data["tiles"]:
            if tile["growth_status"] in ["grown", "seed", "recently_grown"]:
                neighbors = self.mc_engine.flip_engine._get_immediate_neighbors(tile["id"], tiling_data)
                
                for neighbor in neighbors:
                    if neighbor["growth_status"] == "ungrown":
                        tile["growth_status"] = "frontier"
                        break
    
    def _get_frontier_tiles(self, tiling_data: Dict) -> List[Dict]:
        """
        Get current frontier tiles
        """
        return [tile for tile in tiling_data["tiles"] 
                if tile["growth_status"] == "frontier"]
    
    def _find_tiles_in_radius(self, center: List[float], radius: float, 
                            tiling_data: Dict) -> List[Dict]:
        """
        Find tiles within radius of center point
        """
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
    
    def _can_grow_into_tile(self, tile: Dict, obstacles: Dict) -> bool:
        """
        Check if growth can proceed into this tile
        Respects obstacle constraints
        """
        # Check if tile is blocked by obstacles
        if tile.get("immobile", False):  # Fixed defect
            return False
        
        # Additional obstacle checking could go here
        # (e.g., geometric constraints from pore boundaries)
        
        return True
    
    def get_growth_diagnostics(self) -> Dict[str, Any]:
        """
        Return growth diagnostics for scientific analysis
        """
        return {
            "current_step": self.growth_step,
            "growth_history": self.growth_history,
            "total_growth_steps": len(self.growth_history)
        }