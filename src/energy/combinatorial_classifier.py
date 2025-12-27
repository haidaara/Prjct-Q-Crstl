# src/energy/combinatorial_classifier.py
"""
Physically accurate vertex classification for Penrose tilings
FIXED VERSION: Uses adjacency graph as primary neighbor source
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class VertexEnvironment:
    """Complete physical description of vertex local environment"""
    center_tile_type: str
    neighbor_tile_types: List[str]
    coordination_number: int
    angle_sequence: List[float]
    lattice_coords: List[int]

class CombinatorialVertexClassifier:
    """
    Classifies vertex environments using physically meaningful criteria
    FIXED: Uses adjacency graph as primary neighbor source for correct coordination
    """
    
    def __init__(self, angle_tolerance: float = 15.0):
        self.valid_coordinations = {2, 3, 4, 5, 7}
        self.penrose_angles = {36.0, 72.0, 108.0, 144.0}
        self.angle_tolerance = angle_tolerance
        self.angular_regularity_threshold = 0.3
        self.coordination_quality_threshold = 0.4
    
    def classify_vertex_environment(self, tile_id: int, tiling_data: Dict) -> str:
        """
        Main classification method - uses adjacency graph for correct coordination
        """
        environment = self._analyze_vertex_environment(tile_id, tiling_data)
        
        geometric_violations = self._check_geometric_constraints(environment)
        coordination_analysis = self._analyze_coordination_pattern(environment)
        
        return self._synthesize_energy_classification(
            environment, geometric_violations, coordination_analysis
        )
    
    def _analyze_vertex_environment(self, tile_id: int, tiling_data: Dict) -> VertexEnvironment:
        """Comprehensive physical analysis using adjacency graph"""
        center_tile = tiling_data["tiles"][tile_id]
        neighbors = self._get_immediate_neighbors(tile_id, tiling_data)
        
        # Get neighbor vectors and sort by angle for proper geometric analysis
        neighbor_vectors = self._compute_neighbor_vectors(center_tile, neighbors, tiling_data)
        sorted_vectors, sorted_neighbors = self._sort_neighbors_by_angle(neighbor_vectors, neighbors)
        angles = self._compute_relative_angles(sorted_vectors)
        
        return VertexEnvironment(
            center_tile_type=center_tile["type"],
            neighbor_tile_types=[n["type"] for n in sorted_neighbors],
            coordination_number=len(neighbors),
            angle_sequence=angles,
            lattice_coords=center_tile.get("lattice_coords", [0, 0, 0, 0, 0])
        )
    
    def _get_immediate_neighbors(self, tile_id: int, tiling_data: Dict) -> List[Dict]:
        """
        FIXED: Uses adjacency graph as primary source for correct coordination
        """
        neighbors = []
        adjacency_graph = tiling_data["adjacency_graph"]
        
        # Use adjacency graph as primary source - this is the critical fix
        tile_key = str(tile_id)
        if tile_key in adjacency_graph:
            neighbor_ids = adjacency_graph[tile_key]
        else:
            # Fallback to tile neighbor list if adjacency graph missing
            neighbor_ids = tiling_data["tiles"][tile_id].get("neighbors", [])
        
        for neighbor_id in neighbor_ids:
            neighbor_id_int = int(neighbor_id)
            if 0 <= neighbor_id_int < len(tiling_data["tiles"]):
                n = tiling_data["tiles"][neighbor_id_int]
        
                # Skip inactive / vacuum neighbors (match energy model semantics)
                if n.get("removed", False): 
                    continue
                if n.get("obstacle_type") == "pore":
                    continue
                if n.get("growth_status") == "ungrown":
                    continue
                
                neighbors.append(n)
        
        
        return neighbors
    
    def _compute_neighbor_vectors(self, center_tile: Dict, neighbors: List[Dict], 
                                tiling_data: Dict) -> List[np.ndarray]:
        """Compute vectors from center to each neighbor"""
        vectors = []
        center_x, center_y = center_tile["center"]
        
        for neighbor in neighbors:
            neighbor_x, neighbor_y = neighbor["center"]
            vector = np.array([neighbor_x - center_x, neighbor_y - center_y])
            vectors.append(vector)
        
        return vectors
    
    def _sort_neighbors_by_angle(self, vectors: List[np.ndarray], 
                               neighbors: List[Dict]) -> Tuple[List[np.ndarray], List[Dict]]:
        """Sort neighbors by polar angle for proper geometric analysis"""
        if not vectors:
            return vectors, neighbors
            
        # Compute polar angles
        angles = []
        for v in vectors:
            angle = math.atan2(v[1], v[0])
            if angle < 0:
                angle += 2 * math.pi
            angles.append(angle)
        
        # Sort by angle
        sorted_indices = np.argsort(angles)
        sorted_vectors = [vectors[i] for i in sorted_indices]
        sorted_neighbors = [neighbors[i] for i in sorted_indices]
        
        return sorted_vectors, sorted_neighbors
    
    def _compute_relative_angles(self, vectors: List[np.ndarray]) -> List[float]:
        """Compute angles between consecutive neighbor vectors in sorted order"""
        if len(vectors) < 2:
            return []

        angles = []
        for i in range(len(vectors)):
            v1 = vectors[i]
            v2 = vectors[(i + 1) % len(vectors)]

            denom = np.linalg.norm(v1) * np.linalg.norm(v2)
            if denom < 1e-12:
                continue

            cos_angle = np.dot(v1, v2) / denom
            angle = math.degrees(math.acos(np.clip(cos_angle, -1.0, 1.0)))
            angles.append(angle)

        return angles
    
    # In CombinatorialVertexClassifier class (around line 140)
    def clear_cache(self):
        """Clear any internal caches"""
        # This class doesn't have caches yet, but add for future compatibility
        pass

    def _check_geometric_constraints(self, environment: VertexEnvironment) -> Dict[str, bool]:
        violations = {
            "invalid_coordination": environment.coordination_number not in self.valid_coordinations,
            "severe_angular_strain": False,
            "impossible_configuration": self._check_impossible_configuration(environment),
        }

        if environment.angle_sequence:
            angle_std = np.std(environment.angle_sequence)
            violations["severe_angular_strain"] = angle_std > 50.0

        return violations
    
    def _check_impossible_configuration(self, environment: VertexEnvironment) -> bool:
        """Check for configurations that violate basic Penrose constraints"""
        center_type = environment.center_tile_type
        neighbor_types = environment.neighbor_tile_types
        coordination = environment.coordination_number
        
        if coordination == 7:
            if center_type == "THIN" and neighbor_types.count("THIN") > 4:
                return True
            if center_type == "THICK" and neighbor_types.count("THICK") > 5:
                return True
        
        thick_count = neighbor_types.count("THICK")
        thin_count = neighbor_types.count("THIN")
        if thick_count > 6 or thin_count > 5:
            return True
            
        return False
    
    def _analyze_coordination_pattern(self, environment: VertexEnvironment) -> Dict:
        """Analyze coordination pattern with physically meaningful metrics"""
        analysis = {
            "angular_regularity": 0.0,
            "coordination_quality": self._assess_coordination_quality(environment),
        }
        
        if environment.angle_sequence:
            penrose_match = 0
            for angle in environment.angle_sequence:
                if any(abs(angle - pa) < self.angle_tolerance for pa in self.penrose_angles):
                    penrose_match += 1
            analysis["angular_regularity"] = penrose_match / len(environment.angle_sequence)
        
        return analysis
    
    def _assess_coordination_quality(self, environment: VertexEnvironment) -> float:
        """Assess quality with realistic boundary handling"""
        coord = environment.coordination_number
        center_type = environment.center_tile_type

        if coord == 2:
            return 0.6
        elif coord == 3:
            return 0.9
        elif coord == 4:
            return 0.8
        elif coord == 5:
            if center_type == "THICK":
                return 0.7
            else:
                return 0.6
        elif coord == 7:
            return 0.5
        else:
            return 0.3
    
    def _synthesize_energy_classification(self, environment: VertexEnvironment,
                                        geometric_violations: Dict, coordination_analysis: Dict) -> str:
        """Realistic classification thresholds"""
        if any(geometric_violations.values()):
            return "HIGH_ENERGY"
        
        if (coordination_analysis["angular_regularity"] < self.angular_regularity_threshold or
            coordination_analysis["coordination_quality"] < self.coordination_quality_threshold):
            return "MEDIUM_ENERGY"
        
        return "LOW_ENERGY"