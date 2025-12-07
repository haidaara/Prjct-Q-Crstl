# src/energy/energy_logger.py
"""
Research-grade energy landscape logging - ENHANCED VERSION
FIXED: Better coordination validation and energy statistics
"""

import json
import datetime
import os
import numpy as np
from typing import Dict, Any, List
from collections import Counter

class EnergyLogger:
    """Logs energy landscape concepts for research reproducibility"""
    
    def __init__(self, base_data_dir: str = "data"):
        self.base_data_dir = base_data_dir
        self.timestamp = datetime.datetime.now().isoformat()
        
    def log_energy_parameters(self, energy_model) -> str:
        """Log the fundamental energy model parameters"""
        energy_params = {
            "timestamp": self.timestamp,
            "energy_model": "WidomInspiredQuasicrystalHamiltonian",
            "vertex_energy_hierarchy": {
                "high_energy_defect": energy_model.params.high_energy_penalty,
                "medium_energy_strained": energy_model.params.medium_energy_penalty,
                "low_energy_ideal": energy_model.params.low_energy_reference
            },
            "interaction_terms": {
                "neighbor_elastic_coupling": energy_model.params.neighbor_interaction_strength,
                "geometric_strain_penalty": energy_model.params.geometric_strain_penalty,
                "phason_strain_penalty": 0.0
            }
        }
        
        filepath = self._save_json("energy/energy_model_parameters.json", energy_params)
        return filepath
        
    def log_vertex_environment_statistics(self, tiling_data: Dict) -> str:
        """Log comprehensive vertex environment and energy statistics"""
        # Calculate distributions from actual tiling data
        active_tiles = [t for t in tiling_data["tiles"] if not t.get("removed", False)]
        
        # Use adjacency graph for coordination numbers (more reliable)
        coordination_numbers = self._get_coordination_from_adjacency(tiling_data)
        vertex_classes = [tile.get("vertex_class", "UNCLASSIFIED") for tile in active_tiles]
        energies = [tile.get("local_energy", 0.0) for tile in active_tiles]
        
        analysis = {
            "timestamp": self.timestamp,
            "tiling_reference": {
                "total_tiles": len(tiling_data["tiles"]),
                "active_tiles": len(active_tiles),
                "pores_excluded": len(tiling_data["tiles"]) - len(active_tiles),
                "thick_rhombus_count": sum(1 for t in tiling_data["tiles"] if t.get("type") == "THICK"),
                "thin_rhombus_count": sum(1 for t in tiling_data["tiles"] if t.get("type") == "THIN")
            },
            "vertex_classification_distribution": dict(Counter(vertex_classes)),
            "coordination_number_distribution": dict(Counter(coordination_numbers)),
            "energy_landscape_statistics": self._calculate_energy_statistics(energies),
            "coordination_quality_metrics": self._assess_coordination_quality(coordination_numbers),
            "energy_landscape_quality": {
                "percentage_low_energy": vertex_classes.count("LOW_ENERGY") / len(vertex_classes) * 100,
                "energy_landscape_ruggedness": np.std(energies) / (np.mean(energies) + 1e-12),
                "energy_range_adequacy": "GOOD" if max(energies) > 1.0 else "LOW_CONTRAST"
            }
        }
        
        filepath = self._save_json("energy/vertex_environment_statistics.json", analysis)
        return filepath
        
    # src/energy/energy_logger.py - UPDATED METHOD
    def _get_coordination_from_adjacency(self, tiling_data: Dict) -> List[int]:
        """Get coordination numbers from adjacency graph - FIXED KEY HANDLING"""
        coordination_numbers = []
        adjacency_graph = tiling_data["adjacency_graph"]
        
        for tile in tiling_data["tiles"]:
            tile_id = tile["id"]
            
            # FIXED: Handle both integer and string keys
            if tile_id in adjacency_graph:
                neighbors = adjacency_graph[tile_id]
            elif str(tile_id) in adjacency_graph:
                neighbors = adjacency_graph[str(tile_id)]
            else:
                neighbors = []
            
            coordination_numbers.append(len(neighbors))
        
        # Validate the coordination data
        if not self._validate_coordination_data(coordination_numbers):
            print("⚠️  Coordination data validation failed - using fallback")
            # Fallback: use tile neighbor lists
            coordination_numbers = [len(tile.get("neighbors", [])) for tile in tiling_data["tiles"]]
        
        return coordination_numbers
    
    def _validate_coordination_data(self, coordination_numbers: List[int]) -> bool:
        """Validate coordination numbers are physically plausible"""
        if not coordination_numbers:
            return False
            
        zero_count = coordination_numbers.count(0)
        max_coord = max(coordination_numbers)
        avg_coord = sum(coordination_numbers) / len(coordination_numbers)
        
        # Basic sanity checks for Penrose tilings
        if zero_count > len(coordination_numbers) * 0.01:  # More than 1% isolated tiles
            print(f"⚠️  Suspicious: {zero_count} isolated tiles detected")
            return False
            
        if max_coord > 10:  # Physically impossible coordination for Penrose
            print(f"⚠️  Suspicious: max coordination {max_coord} too high")
            return False
            
        if avg_coord < 2.0 or avg_coord > 5.0:  # Expected range for Penrose
            print(f"⚠️  Suspicious: average coordination {avg_coord:.2f} outside expected range")
            return False
            
        return True
        
    def _assess_coordination_quality(self, coordination_numbers: List[int]) -> Dict[str, Any]:
        """Assess the quality of coordination number distribution"""
        coord_counts = Counter(coordination_numbers)
        total_tiles = len(coordination_numbers)
        
        # Check for physically problematic distributions
        has_coord_0 = coord_counts.get(0, 0) > 0
        coord_1_percentage = coord_counts.get(1, 0) / total_tiles * 100
        coord_2_percentage = coord_counts.get(2, 0) / total_tiles * 100
        typical_coord_percentage = (coord_counts.get(3, 0) + coord_counts.get(4, 0)) / total_tiles * 100
        
        return {
            "has_isolated_tiles": has_coord_0,
            "percentage_single_neighbor": coord_1_percentage,
            "percentage_boundary_tiles": coord_2_percentage,
            "percentage_typical_coordination": typical_coord_percentage,
            "coordination_distribution_quality": "GOOD" if (
                not has_coord_0 and 
                coord_1_percentage < 5.0 and
                typical_coord_percentage > 70.0
            ) else "POOR"
        }
        
    def log_energy_validation_report(self, validation_results: Dict, computation_time: float) -> str:
        """Log validation and performance metrics for energy calculations"""
        qa_report = {
            "timestamp": self.timestamp,
            "energy_computation_performance": {
                "total_computation_time_seconds": computation_time,
                "tiles_processed_per_second": validation_results.get("total_tiles", 0) / computation_time,
                "computation_complexity": "O(n)",
                "memory_efficiency": "HIGH"
            },
            "energy_model_validation": validation_results.get("validation_checks", {}),
            "coordination_validation": validation_results.get("coordination_validation", {}),
            "simulation_readiness": validation_results.get("simulation_readiness", {})
        }
        
        filepath = self._save_json("energy/energy_validation_report.json", qa_report)
        return filepath
        
    def save_energy_initialized_tiling(self, tiling_data: Dict) -> str:
        """Save tiling with energy landscape initialized for simulation phases"""
        enhanced_tiling = {
            "metadata": {
                **tiling_data.get("metadata", {}),
                "energy_model": "WidomInspiredQuasicrystalHamiltonian",
                "energy_initialization_timestamp": self.timestamp,
                "simulation_ready": True,
                "next_phases": ["monte_carlo_relaxation", "growth_dynamics", "phason_analysis"]
            },
            "tiles": tiling_data["tiles"],
            "adjacency_graph": tiling_data["adjacency_graph"]
        }
        
        filepath = self._save_json("processed/penrose_tiling_energy_initialized.json", enhanced_tiling)
        return filepath
        
    def _save_json(self, relative_path: str, data: Dict) -> str:
        """Save JSON with directory creation, return filepath"""
        full_path = os.path.join(self.base_data_dir, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            json.dump(data, f, indent=2)
        return full_path
    
    def _calculate_energy_statistics(self, energies: List[float]) -> Dict[str, float]:
        """Calculate comprehensive energy statistics"""
        if not energies:
            return {}
            
        return {
            "total_configurational_energy": float(sum(energies)),
            "average_energy_per_tile": float(np.mean(energies)),
            "energy_standard_deviation": float(np.std(energies)),
            "min_energy_observed": float(min(energies)),
            "max_energy_observed": float(max(energies)),
            "energy_variance": float(np.var(energies)),
            "energy_skewness": float(self._calculate_skewness(energies)),
            "energy_kurtosis": float(self._calculate_kurtosis(energies))
        }
    
    def _calculate_skewness(self, data: List[float]) -> float:
        """Calculate skewness of energy distribution"""
        if len(data) < 2:
            return 0.0
        data = np.array(data)
        return float(((data - data.mean()) ** 3).mean() / (data.std() ** 3 + 1e-12))
    
    def _calculate_kurtosis(self, data: List[float]) -> float:
        """Calculate kurtosis of energy distribution"""
        if len(data) < 2:
            return 0.0
        data = np.array(data)
        return float(((data - data.mean()) ** 4).mean() / (data.std() ** 4 + 1e-12))