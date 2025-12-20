# src/energy/widom_inspired_energy.py
"""
Widom-inspired energy model for Penrose tilings with LIMITED continuous corrections
OPTIMIZED VERSION: Vertex class caching for performance
"""

import numpy as np
import math
from typing import Dict, Optional
from dataclasses import dataclass

from src.utils.config import ConfigManager


@dataclass 
class EnergyParameters:
    """Physical parameters for Widom-inspired energy model"""
    high_energy_penalty: float = 2.0    # Defect patterns
    medium_energy_penalty: float = 1.0  # Strained configurations
    low_energy_reference: float = 0.0   # Ideal Penrose patterns
    neighbor_interaction_strength: float = 0.1
    geometric_strain_penalty: float = 0.2  # Reduced for limited continuity

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

    def compute_local_energy(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute local energy with LIMITED continuous corrections
        OPTIMIZED: Uses vertex class caching
        """
        tile = tiling_data["tiles"][tile_id]
        
        # Skip pores (removed tiles) - they don't contribute to energy
        if tile.get("removed", False) or tile.get("obstacle_type") == "pore":
            return 0.0
        
        # 1. WIDOM'S CORE CLASSIFICATION (with caching)
        vertex_class = self._get_cached_vertex_class(tile_id, tiling_data)
        base_energy = self.energy_map[vertex_class]
        
        # 2. LIMITED CONTINUOUS CORRECTIONS
        neighbor_energy = self._compute_continuous_neighbor_interaction(tile_id, tiling_data)
        strain_energy = self._compute_continuous_geometric_strain(tile_id, tiling_data)
        
        # 3. COMBINE: Widom base + limited corrections
        total_energy = base_energy + neighbor_energy + strain_energy
        
        # Update tile's energy field for tracking
        tile["local_energy"] = total_energy
        tile["vertex_class"] = vertex_class
        
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
            if not tile.get("removed", False):
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
