"""
Efficient obstacle configuration generation for systematic studies.
"""

import numpy as np
from typing import List, Dict, Tuple
from src.utils.config import ConfigManager
from src.obstacle.obstacle_creator import ObstacleSpec


class ObstacleConfig:
    """High-performance obstacle configuration generator"""
    
    def __init__(self, config: ConfigManager):
        self.config = config
        self.obstacle_config = config.obstacles
        self.rng = np.random.default_rng(config.tiling.get("seed", 42))

    def generate_scalable_obstacles(self, tiling_data: Dict) -> Dict[str, ObstacleSpec]:
        """Generate obstacle specs for systematic density studies"""
        # Use actual tile count from array if available
        tile_count = len(tiling_data["tiles"]) if "tiles" in tiling_data else tiling_data["metadata"]["tile_count"]
        window_size = tiling_data["metadata"]["window_size"]
        window_origin = tiling_data["metadata"].get("window_origin", [0.0, 0.0])
        window_area = window_size[0] * window_size[1]
    
        density_sweep = self.obstacle_config.get("density_sweep", [0.01, 0.05, 0.1, 0.2])
        min_separation = self.obstacle_config.get("min_separation", 2.0)
        obstacle_specs = {}
    
        for density in density_sweep:
            # AREA-BASED CALCULATION FOR PORES
            min_radius = self.obstacle_config.get("min_radius", 2.0)
            max_radius = self.obstacle_config.get("max_radius", 8.0)
            r_mean = 0.5 * (min_radius + max_radius)
    
            for obstacle_type in ["pores", "fixed_defects"]:
                key = f"{obstacle_type}_density_{density}"
    
                if obstacle_type == "pores":
                    # Calculate pore count based on area coverage
                    n_obstacles = max(1, int(round(density * window_area / (np.pi * r_mean**2))))
                    
                    # SIMPLE DETERMINISTIC PLACEMENT - no RNG
                    positions = self._generate_grid_positions(n_obstacles, window_size, window_origin)
                    radii = [r_mean] * n_obstacles  # All same size for consistency
                    
                else:
                    # Fixed defects: tile-based
                    n_obstacles = max(1, int(density * tile_count))
                    positions = []
                    radii = []
    
                obstacle_specs[key] = ObstacleSpec(
                    type=obstacle_type,
                    positions=positions,
                    radii=radii,
                    density=density
                )
    
        print(f"📊 Generated {len(obstacle_specs)} obstacle configurations")
        return obstacle_specs
    
    def _generate_grid_positions(self, n_obstacles: int, window_size: List[float], 
                               origin: List[float]) -> List[Tuple[float, float]]:
        """Simple deterministic grid-based placement"""
        positions = []
        
        # Create a grid that fits in the window
        grid_size = int(np.ceil(np.sqrt(n_obstacles)))
        spacing_x = window_size[0] / (grid_size + 1)
        spacing_y = window_size[1] / (grid_size + 1)
        
        for i in range(n_obstacles):
            row = i // grid_size
            col = i % grid_size
            x = origin[0] + (col + 1) * spacing_x
            y = origin[1] + (row + 1) * spacing_y
            positions.append((x, y))
        
        return positions    

    def _generate_random_radii(self, n_obstacles: int, rng) -> List[float]:  # ADD RNG PARAMETER
        """Generate random radii with research-appropriate range"""
        min_radius = self.obstacle_config.get("min_radius", 2.0)
        max_radius = self.obstacle_config.get("max_radius", 8.0)
        return rng.uniform(min_radius, max_radius, size=n_obstacles).tolist()

    def _generate_positions_radius_aware(self, n_obstacles: int, window_size: List[float], 
                                       origin: List[float], radii: List[float], 
                                       min_separation: float, rng) -> List[Tuple[float, float]]:
        """Generate positions with edge-to-edge separation"""
        positions = []
        max_attempts = n_obstacles * 100
        
        for k in range(n_obstacles):
            r_k = radii[k]
            placed = False
            
            for attempt in range(max_attempts):
                candidate = tuple(rng.uniform([0.0, 0.0], [window_size[0], window_size[1]], size=2) + np.array(origin))
                
                # Check edge-to-edge separation from existing positions
                valid = True
                for j, existing_pos in enumerate(positions):
                    r_j = radii[j]
                    center_distance = np.linalg.norm(np.array(candidate) - np.array(existing_pos))
                    edge_distance = center_distance - (r_k + r_j)
                    
                    if edge_distance < min_separation:
                        valid = False
                        break
                        
                if valid:
                    positions.append(candidate)
                    placed = True
                    break
                    
            if not placed:
                # Fallback: place with minimum overlap
                positions.append(candidate)
                
        return positions
    