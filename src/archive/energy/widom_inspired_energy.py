"""
Widom-inspired energy model for Penrose tilings
Physics-accurate with disabled phason strain term (placeholder)
Paper-ready with proper physical grounding
"""

import numpy as np
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
    geometric_strain_penalty: float = 0.3

class WidomInspiredEnergy:
    """
    Energy model inspired by Widom's quasicrystal Hamiltonian concept
    
    PAPER NOTE: 
    - Uses relative energy hierarchy, not absolute values from specific alloys
    - Disabled phason strain term (placeholder) until perpendicular space implementation
    - Realistic energy ranges for meaningful Monte Carlo dynamics
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
        
        # Widom-inspired energy hierarchy
        self.energy_map = {
            "HIGH_ENERGY": self.params.high_energy_penalty,
            "MEDIUM_ENERGY": self.params.medium_energy_penalty,
            "LOW_ENERGY": self.params.low_energy_reference
        }
    
    def compute_local_energy(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute local energy with physical accuracy
        
        PAPER CRITICAL: 
        - Disabled phason strain term (placeholder) 
        - Pores contribute zero energy
        - Realistic energy ranges for MC acceptance
        """
        tile = tiling_data["tiles"][tile_id]
        
        # Skip pores (removed tiles) - they don't contribute to energy
        if tile.get("removed", False) or tile.get("obstacle_type") == "pore":
            return 0.0
        
        # Core Widom-inspired term (vertex classification)
        vertex_class = self.classifier.classify_vertex_environment(tile_id, tiling_data)
        base_energy = self.energy_map[vertex_class]
        
        # Additional physical terms
        neighbor_energy = self._compute_neighbor_interaction(tile_id, tiling_data)
        strain_energy = self._compute_geometric_strain_energy(tile_id, tiling_data)
        
        total_energy = base_energy + neighbor_energy + strain_energy
        
        # Update tile's energy field for tracking
        tile["local_energy"] = total_energy
        tile["vertex_class"] = vertex_class
        
        return total_energy
    
    def _compute_neighbor_interaction(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute energy from interactions with neighboring tiles
        Models weak elastic coupling between local environments
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
                
            # Energy depends on compatibility of local environments
            neighbor_class = self.classifier.classify_vertex_environment(neighbor["id"], tiling_data)
            
            # High-energy neighbors increase local energy (defect propagation)
            if neighbor_class == "HIGH_ENERGY":
                interaction_energy += 0.1 * self.params.neighbor_interaction_strength
            elif neighbor_class == "MEDIUM_ENERGY":
                interaction_energy += 0.05 * self.params.neighbor_interaction_strength
        
        return interaction_energy
    
    def _compute_geometric_strain_energy(self, tile_id: int, tiling_data: Dict) -> float:
        """
        Compute energy from local geometric strain
        Based on angular deviations from characteristic Penrose patterns
        """
        environment = self.classifier._analyze_vertex_environment(tile_id, tiling_data)
        
        if not environment.angle_sequence:
            return 0.0
            
        # Characteristic Penrose angles
        penrose_angles = {36.0, 72.0, 108.0, 144.0}
        
        # Compute deviation from ideal Penrose angles
        total_deviation = 0.0
        for angle in environment.angle_sequence:
            # Find closest Penrose angle
            min_dev = min(abs(angle - pa) for pa in penrose_angles)
            total_deviation += min_dev
        
        avg_deviation = total_deviation / len(environment.angle_sequence)
        
        # Normalize by characteristic angle and apply penalty
        return self.params.geometric_strain_penalty * avg_deviation / 36.0
    
    def _compute_phason_strain_energy(self, tile_id: int, tiling_data: Dict) -> float:
        """
        PHASON STRAIN ENERGY - CURRENTLY DISABLED
        
        PAPER CRITICAL NOTE:
        This requires proper perpendicular space coordinates which are not yet available.
        Using integer lattice_coords makes this term always zero - physically incorrect.
        This will be implemented in Phase 2 with proper perpendicular space analysis.
        """
        return 0.0  # Placeholder until proper perpendicular space implementation
    
    def compute_total_energy(self, tiling_data: Dict) -> float:
        """Compute total energy of the tiling for paper metrics"""
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
        Useful for visualization and analysis
        """
        for tile_id, tile in enumerate(tiling_data["tiles"]):
            if not tile.get("removed", False):
                self.compute_local_energy(tile_id, tiling_data)
        return tiling_data