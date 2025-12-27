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
            "version": "OptionA_WithSurfaceTension",

            # Widom Geometric Parameters
            "vertex_energy_hierarchy": {
                "high_energy_defect": energy_model.params.high_energy_penalty,
                "medium_energy_strained": energy_model.params.medium_energy_penalty,
                "low_energy_ideal": energy_model.params.low_energy_reference
            },

            # Continuous Strain Parameters
            "interaction_terms": {
                "neighbor_elastic_coupling": energy_model.params.neighbor_interaction_strength,
                "geometric_strain_penalty": energy_model.params.geometric_strain_penalty,
                "phason_strain_penalty": 0.0
            },

            # NEW: Surface Tension Parameters (Option A)
            "surface_tension_parameters": {
                "surface_tension_per_bond": energy_model.params.surface_tension_per_bond,
                "matching_rule_weight": energy_model.params.matching_rule_weight,
                "continuous_correction_weight": energy_model.params.continuous_correction_weight
            },

            # NEW: Classification Thresholds
            "classification_thresholds": {
                "energy_class_thresholds": list(energy_model.params.energy_class_thresholds),
                "treat_ungrown_as_vacuum": energy_model.params.treat_ungrown_as_vacuum
            },

            # NEW: Physics Semantics Documentation
            "semantic_clarification": {
                "vertex_class": "Geometric classification (pure Widom)",
                "energy_class": "Physics outcome (geometry + surface + strain)",
                "boundary_kind": "Type of boundary interface",
                "is_boundary": "Missing bonds > 0",
                "surface_energy": "Energy from missing bonds only"
            }
        }
        
        filepath = self._save_json("energy/energy_model_parameters.json", energy_params)
        return filepath
        
    def log_vertex_environment_statistics(self, tiling_data: Dict) -> str:
        """Log comprehensive vertex environment and energy statistics"""
        # Calculate distributions from actual tiling data
        active_tiles = [
            t for t in tiling_data["tiles"]
            if (not t.get("removed", False))
            and (t.get("obstacle_type") != "pore")
            and (t.get("growth_status") != "ungrown")   # treat vacuum as non-matter in stats
        ]
        
        # Use adjacency graph for coordination numbers (more reliable)
        coordination_numbers = self._get_coordination_from_adjacency(tiling_data)
        vertex_classes = [tile.get("vertex_class", "UNCLASSIFIED") for tile in active_tiles]
        energies = [tile.get("local_energy", 0.0) for tile in active_tiles]
        
        # NEW: Collect Option A specific distributions
        energy_classes = [tile.get("energy_class", "UNCLASSIFIED") for tile in active_tiles]
        boundary_kinds = [tile.get("boundary_kind", "unknown") for tile in active_tiles]
        is_boundary_flags = [tile.get("is_boundary", False) for tile in active_tiles]
        missing_bonds_list = [tile.get("missing_bonds", 0) for tile in active_tiles]
        surface_energies = [tile.get("surface_energy", 0.0) for tile in active_tiles]
        
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
            
            # NEW: Option A Specific Metrics
            "option_a_statistics": {
                "energy_class_distribution": dict(Counter(energy_classes)),
                "boundary_kind_distribution": dict(Counter(boundary_kinds)),
                "boundary_tile_count": sum(is_boundary_flags),
                "boundary_percentage": sum(is_boundary_flags) / len(active_tiles) * 100 if active_tiles else 0,
                "missing_bonds_distribution": dict(Counter(missing_bonds_list)),
                "surface_energy_statistics": self._calculate_energy_statistics(surface_energies),
                "surface_energy_total": sum(surface_energies),
                "surface_energy_per_boundary_tile": sum(surface_energies) / sum(is_boundary_flags) if sum(is_boundary_flags) > 0 else 0
            },
            
            # Enhanced quality metrics
            "energy_landscape_quality": {
                "percentage_low_energy": vertex_classes.count("LOW_ENERGY") / len(vertex_classes) * 100,
                "percentage_low_energy_class": energy_classes.count("LOW_ENERGY") / len(energy_classes) * 100,
                "energy_landscape_ruggedness": np.std(energies) / (np.mean(energies) + 1e-12),
                "energy_range_adequacy": "GOOD" if max(energies) > 1.0 else "LOW_CONTRAST",
                "surface_tension_active": any(e > 0 for e in surface_energies)
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
        sr = validation_results.get("simulation_readiness", {})
        ready_for_healing = sr.get("ready_for_healing", sr.get("monte_carlo_ready", False))
        ready_for_growth  = sr.get("ready_for_growth",  sr.get("growth_dynamics_ready", False))

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
            "simulation_readiness": validation_results.get("simulation_readiness", {}),

            # NEW: Option A Specific Validation
            "option_a_validation": {
                "surface_tension_active": validation_results.get("surface_tension_active", False),
                "boundary_tiles_detected": validation_results.get("boundary_tiles_detected", 0),
                "energy_class_computed": validation_results.get("energy_class_computed", False),
                "fields_present": {
                    "energy_class": validation_results.get("has_energy_class", False),
                    "boundary_kind": validation_results.get("has_boundary_kind", False),
                    "missing_bonds": validation_results.get("has_missing_bonds", False),
                    "surface_energy": validation_results.get("has_surface_energy", False)
                }
            },

            "overall_assessment": {
                "physics_correctness": "OptionA_Implemented" if validation_results.get("surface_tension_active", False) else "WidomOnly",
                "ready_for_healing": bool(ready_for_healing),
                "ready_for_growth": bool(ready_for_growth),
            }
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
        arr = np.array(data)
        return float(((arr - arr.mean()) ** 3).mean() / (arr.std() ** 3 + 1e-12))
    
    def _calculate_kurtosis(self, data: List[float]) -> float:
        """Calculate kurtosis of energy distribution"""
        if len(data) < 2:
            return 0.0
        arr = np.array(data)
        return float(((arr - arr.mean()) ** 4).mean() / (arr.std() ** 4 + 1e-12))
    
    def log_boundary_analysis(self, tiling_data: Dict) -> str:
        """
        Detailed boundary analysis for Option A implementation
        """
        active_tiles = [t for t in tiling_data["tiles"] if not t.get("removed", False)]

        # Group tiles by boundary kind
        by_boundary_kind = {}
        for tile in active_tiles:
            kind = tile.get("boundary_kind", "unknown")
            if kind not in by_boundary_kind:
                by_boundary_kind[kind] = []
            by_boundary_kind[kind].append(tile)

        # Analyze each boundary type
        boundary_analysis = {}
        for kind, tiles in by_boundary_kind.items():
            energies = [t.get("local_energy", 0.0) for t in tiles]
            missing_bonds = [t.get("missing_bonds", 0) for t in tiles]
            surface_energies = [t.get("surface_energy", 0.0) for t in tiles]

            boundary_analysis[kind] = {
                "count": len(tiles),
                "percentage": len(tiles) / len(active_tiles) * 100,
                "avg_total_energy": np.mean(energies) if energies else 0,
                "avg_missing_bonds": np.mean(missing_bonds) if missing_bonds else 0,
                "avg_surface_energy": np.mean(surface_energies) if surface_energies else 0,
                "energy_std": np.std(energies) if len(energies) > 1 else 0
            }

        # Calculate boundary transitions
        analysis = {
            "timestamp": self.timestamp,
            "total_active_tiles": len(active_tiles),
            "boundary_type_analysis": boundary_analysis,

            # Boundary statistics
            "boundary_statistics": {
                "total_boundary_tiles": sum(1 for t in active_tiles if t.get("is_boundary", False)),
                "boundary_tiles_percentage": sum(1 for t in active_tiles if t.get("is_boundary", False)) / len(active_tiles) * 100,
                "max_missing_bonds": max(t.get("missing_bonds", 0) for t in active_tiles),
                "avg_missing_bonds": np.mean([t.get("missing_bonds", 0) for t in active_tiles]),
                "total_surface_energy": sum(t.get("surface_energy", 0.0) for t in active_tiles)
            },

            # Comparison with vertex_class (geometric defects)
            "defect_comparison": {
                "geometric_defects_high": sum(1 for t in active_tiles if t.get("vertex_class") == "HIGH_ENERGY"),
                "energy_defects_high": sum(1 for t in active_tiles if t.get("energy_class") == "HIGH_ENERGY"),
                "geometric_defects_medium": sum(1 for t in active_tiles if t.get("vertex_class") == "MEDIUM_ENERGY"),
                "energy_defects_medium": sum(1 for t in active_tiles if t.get("energy_class") == "MEDIUM_ENERGY")
            }
        }

        filepath = self._save_json("energy/boundary_analysis.json", analysis)
        return filepath