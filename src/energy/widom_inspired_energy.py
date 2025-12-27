# src/energy/widom_inspired_energy.py
"""
Widom-inspired energy model for Penrose tilings with LIMITED continuous corrections
OPTIMIZED VERSION: Vertex class caching for performance
"""

import numpy as np
import math
from typing import Dict, Optional, Tuple
from dataclasses import dataclass

from src.utils.config import ConfigManager


@dataclass 
class EnergyParameters:
    """Physical parameters for Widom-inspired energy model"""
    # Base Geometric Penalties (Widom)
    high_energy_penalty: float = 2.0    
    medium_energy_penalty: float = 1.0  
    low_energy_reference: float = 0.0   
    
    # Continuous Terms
    neighbor_interaction_strength: float = 0.1
    geometric_strain_penalty: float = 0.2
    
    # [NEW] Surface Tension / Topology (Option A)
    surface_tension_per_bond: float = 1.0       # Energy cost per missing bond
    matching_rule_weight: float = 1.0           # Weight of surface term
    continuous_correction_weight: float = 0.5   # Weight of strain terms
    
    # Thresholds for visualization (Low->Med, Med->High)
    energy_class_thresholds: Tuple[float, float] = (0.5, 1.5)

    treat_ungrown_as_vacuum: bool = False   # Safer default; set to True only for growth

class WidomInspiredEnergy:
    """
    Energy model inspired by Widom's quasicrystal Hamiltonian concept
    OPTIMIZED: Vertex class caching for performance
    LIMITED CONTINUITY: Small corrections create energy variations within Widom classes
    """
    
    @classmethod
    def from_config(cls, config_manager: ConfigManager) -> 'WidomInspiredEnergy':
        """Create energy model from ConfigManager instance"""
        energy_config = config_manager.energy
        parameters = EnergyParameters(**energy_config)
        
        return cls(parameters)

    def __init__(self, parameters: Optional[EnergyParameters] = None):
        self.params = parameters or EnergyParameters()
        from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
        self.classifier = CombinatorialVertexClassifier()
        
        # WIDOM'S ORIGINAL HIERARCHY
        self.energy_map = {
            "HIGH_ENERGY": self.params.high_energy_penalty,
            "MEDIUM_ENERGY": self.params.medium_energy_penalty,
            "LOW_ENERGY": self.params.low_energy_reference
        }
        
        # PERFORMANCE OPTIMIZATION: Vertex class cache
        self._vertex_class_cache = {}
    
    def _compute_surface_energy(self, tile_id: int, tiling_data: Dict) -> Tuple[float, int, bool]:
        """
        Calculate surface tension energy (broken bonds).
        Treats 'Ungrown', 'Removed', and 'Pore' as vacuum.
        Returns: (Energy, Missing_Bonds_Count, Is_Boundary_Bool)
        """
        tile = tiling_data["tiles"][tile_id]
        adj = tiling_data.get("adjacency_graph", {})
        tiles = tiling_data["tiles"]
        
        # Handle string/int key mismatch safely, with fallback to tile's own neighbor list
        neighbors = adj.get(str(tile_id)) or adj.get(tile_id, []) or tile.get("neighbors", [])
        
        active_count = 0
        inactive_removed_or_pore = 0
        inactive_ungrown = 0
        
        
        for nid in neighbors:
            try:
                # Robust index conversion
                n_idx = int(nid)
                if n_idx < 0 or n_idx >= len(tiles): continue
                n_tile = tiles[n_idx]
            except (ValueError, IndexError, TypeError):
                continue
            
            # 1. Vacuum Check: Removed or Pore
            if n_tile.get("removed", False) or n_tile.get("obstacle_type") == "pore":
                inactive_removed_or_pore += 1  # FIX: COUNT INACTIVE
                continue
                        
            # 2. Growth Front Check
            # If treat_ungrown_as_vacuum=True, ungrown tiles behave as vacuum (surface bonds are broken).
            # If False, ungrown tiles are treated as solid neighbors for surface counting.
            if n_tile.get("growth_status") == "ungrown":
                if self.params.treat_ungrown_as_vacuum:
                    inactive_ungrown += 1
                    continue
                # else: count as active neighbor (no broken bond)
            
            
            active_count += 1
        
        # Penrose Rhombus always has 4 edges -> Ideal coordination is 4
        expected = 4
        missing_bonds = max(0, expected - active_count)
        
        energy = missing_bonds * self.params.surface_tension_per_bond
        is_boundary = missing_bonds > 0
        
        # Classify Boundary Type
        if is_boundary:
            if inactive_ungrown > 0:
                boundary_kind = "growth_front"  # Interface with vacuum
            elif inactive_removed_or_pore > 0:
                boundary_kind = "pore_edge"     # Interface with obstacle
            else:
                boundary_kind = "outer_edge"    # Interface with window boundary
        else:
            boundary_kind = "bulk"  # FIX: Explicitly set for non-boundary tiles
        
        # Store directly on tile for Viz/Metrics
        tile["boundary_kind"] = boundary_kind
        tile["surface_energy"] = energy  # Store for debugging/metrics


        return energy, missing_bonds, is_boundary

    def compute_local_energy(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute total energy = Geometry + Surface + Strain.
        Populates 'energy_class' without overwriting 'vertex_class'.
        """
        tile = tiling_data["tiles"][tile_id]
        
        
        # 0. Pores / Removed: Zero energy state
        if tile.get("removed", False) or tile.get("obstacle_type") == "pore":
            tile["local_energy"] = 0.0
            tile["vertex_class"] = "LOW_ENERGY"
            tile["energy_class"] = "LOW_ENERGY"
            tile["is_boundary"] = False
            tile["boundary_kind"] = "bulk"
            tile["missing_bonds"] = 0
            tile["surface_energy"] = 0.0
            return 0.0
        
        # CRITICAL FIX: Ungrown tiles as vacuum (prevents ghost energy)
        if self.params.treat_ungrown_as_vacuum and tile.get("growth_status") == "ungrown":
            tile["local_energy"] = 0.0
            tile["energy_class"] = "LOW_ENERGY"
            tile["is_boundary"] = False
            tile["boundary_kind"] = "vacuum"
            tile["missing_bonds"] = 0
            tile["surface_energy"] = 0.0
            tile["vertex_class"] = "LOW_ENERGY"  # Also set geometric class
            return 0.0

        
        # 1. GEOMETRY (Pure Widom)
        # We keep this strictly geometric so we can track "Healing" vs "Boundary"
        vertex_class = self._get_cached_vertex_class(tile_id, tiling_data)
        E_widom = self.energy_map[vertex_class]
        
        # 2. TOPOLOGY (Surface Tension)
        E_surface, missing_bonds, is_boundary = self._compute_surface_energy(tile_id, tiling_data)
        
        # 3. STRAIN (Continuous)
        E_neighbor = self._compute_continuous_neighbor_interaction(tile_id, tiling_data)
        E_strain = self._compute_continuous_geometric_strain(tile_id, tiling_data)
        E_continuous = E_neighbor + E_strain
        
        # 4. TOTAL WEIGHTED ENERGY
        total_energy = (
            E_widom + 
            (self.params.matching_rule_weight * E_surface) +
            (self.params.continuous_correction_weight * E_continuous)
        )
        
        # 5. STATE UPDATE (Clean Semantics)
        tile["local_energy"] = total_energy
        tile["vertex_class"] = vertex_class  # Preserves geometric classification
        tile["surface_energy"] = E_surface   # Explicit for debugging
        tile["missing_bonds"] = missing_bonds
        tile["is_boundary"] = is_boundary
        
        # 6. ENERGY CLASS (For Visualization)
        # Classifies the *Resulting* Physics (Red Boundary comes from here)
        low_thresh, high_thresh = self.params.energy_class_thresholds 
        if total_energy >= high_thresh:
            tile["energy_class"] = "HIGH_ENERGY"
        elif total_energy >= low_thresh:
            tile["energy_class"] = "MEDIUM_ENERGY"
        else:
            tile["energy_class"] = "LOW_ENERGY"
            
        return total_energy

    def _get_cached_vertex_class(self, tile_id: int, tiling_data: Dict) -> str:
        """
        OPTIMIZED: Get vertex class with caching
        Reduces classifier calls from O(n×neighbors) to O(n)
        """
        if tile_id not in self._vertex_class_cache:
            self._vertex_class_cache[tile_id] = self.classifier.classify_vertex_environment(
                tile_id, tiling_data
            )
        return self._vertex_class_cache[tile_id]
    
    def _compute_continuous_neighbor_interaction(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute LIMITED energy from interactions with neighboring tiles
        OPTIMIZED: Uses cached vertex classes
        """
        neighbors = self.classifier._get_immediate_neighbors(tile_id, tiling_data)
        
        if not neighbors:
            return 0.0
            
        interaction_energy = 0.0
        
        for neighbor in neighbors:
            # Skip pores and fixed defects for interaction calculation
            if (neighbor.get("removed", False) or 
                neighbor.get("obstacle_type") == "pore"):
                continue
                
            # OPTIMIZED: Use cached vertex class (not recursive energy)
            neighbor_class = self._get_cached_vertex_class(neighbor["id"], tiling_data)
            
            # LIMITED continuity: Small corrections based on neighbor class
            if neighbor_class == "HIGH_ENERGY":
                interaction_energy += 0.05 * self.params.neighbor_interaction_strength
            elif neighbor_class == "MEDIUM_ENERGY":
                interaction_energy += 0.02 * self.params.neighbor_interaction_strength
        
        return interaction_energy
    
    def _compute_continuous_geometric_strain(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute LIMITED energy from local geometric strain
        Creates SOME continuity but not full continuum
        """
        environment = self.classifier._analyze_vertex_environment(tile_id, tiling_data)
        
        if not environment.angle_sequence:
            return 0.0
            
        # Characteristic Penrose angles
        penrose_angles = {36.0, 72.0, 108.0, 144.0}
        
        # Compute RMS deviation for LIMITED continuity
        total_deviation = 0.0
        for angle in environment.angle_sequence:
            # Find closest Penrose angle
            min_dev = min(abs(angle - pa) for pa in penrose_angles)
            total_deviation += min_dev
        
        avg_deviation = total_deviation / len(environment.angle_sequence)
        
        # LIMITED continuous scaling
        return self.params.geometric_strain_penalty * avg_deviation / 36.0
    
    def _compute_phason_strain_energy(self, tile_id: int, tiling_data: Dict) -> float:
        """
        PHASON STRAIN ENERGY - CURRENTLY DISABLED
        Placeholder until proper perpendicular space implementation
        """
        return 0.0
    
    def compute_total_energy(self, tiling_data: Dict) -> float:
        """Compute total energy of the tiling with caching optimization"""
        # Clear cache for fresh computation
        self._vertex_class_cache.clear()
        
        total_energy = 0.0
        
        for tile_id, tile in enumerate(tiling_data["tiles"]):
            # Skip pores in total energy calculation
            if tile.get("removed", False) or tile.get("obstacle_type") == "pore":
                continue
            total_energy += self.compute_local_energy(tile_id, tiling_data)
            
        return total_energy
    
    def update_tiling_energy(self, tiling_data: Dict) -> Dict:
        """
        Update energy fields for all tiles in tiling data
        Uses caching for optimal performance
        """
        # Clear cache for fresh computation
        self._vertex_class_cache.clear()
        
        for tile_id, tile in enumerate(tiling_data["tiles"]):
                self.compute_local_energy(tile_id, tiling_data)
        return tiling_data

    def clear_cache(self):
        # clear whatever you actually have
        if hasattr(self, "_vertex_class_cache"):
            self._vertex_class_cache.clear()
        if hasattr(self, "_local_energy_cache"):
            self._local_energy_cache.clear()

         # Force garbage collection for good measure
        import gc
        gc.collect()
