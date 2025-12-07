"""
Physics-correct Monte Carlo engine ensuring detailed balance and proper energy management
"""

import math
import random
import time
from typing import Dict, List, Tuple, Any
import numpy as np

class PhysicsCorrectMCEngine:
    """
    Monte Carlo engine that preserves detailed balance and physical consistency
    No optimizations that compromise physics correctness
    """
    
    def __init__(self, temperature: float = 0.3, energy_model=None, flip_engine=None):
        self.temperature = temperature
        self.energy_model = energy_model
        self.flip_engine = flip_engine
        
        # Global energy tracking (must be consistent with sum of local energies)
        self.current_energy = 0.0
        
        # Scientific diagnostics (for validation, not physics)
        self.metrics = {
            "energy_trajectory": [],           # Every step for autocorrelation
            "acceptance_sequence": [],         # For detailed balance verification  
            "computation_times": [],
            "flip_statistics": {
                "proposed": 0,
                "accepted": 0, 
                "rejected": 0
            }
        }
    
    def initialize_energy(self, tiling_data: Dict) -> None:
        """
        Compute initial total energy once for consistency
        """
        self.current_energy = self.energy_model.compute_total_energy(tiling_data)
        self.metrics["energy_trajectory"].append(self.current_energy)
        print(f"🔬 Initialized energy: {self.current_energy:.2f}")
    
    def run_mc_step(self, tiling_data: Dict) -> Tuple[bool, float]:
        """
        Single MC step preserving detailed balance and physical consistency
        Returns: (accepted, delta_energy)
        """
        step_start = time.time()
        
        # 1. PROPER STATISTICS: Track for scientific accuracy
        self.metrics["flip_statistics"]["proposed"] += 1
        
        # 2. Find legal flips in ACTUAL system state
        flippable_clusters = self.flip_engine.find_flippable_hexagons(tiling_data)
        if not flippable_clusters:
            self.metrics["acceptance_sequence"].append(False)
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0
        
        cluster_ids = random.choice(flippable_clusters)
        affected_tiles = self.flip_engine._get_affected_tile_neighborhood(cluster_ids, tiling_data)
        
        # 3. CAPTURE CURRENT PHYSICAL STATE (not a copy!)
        undo_info = self.flip_engine._capture_physical_state(cluster_ids, tiling_data)
        
        # 4. PRE-FLIP: Use stored energies (already computed and valid)
        current_local_energy = sum(
            tiling_data["tiles"][tile_id]["local_energy"] 
            for tile_id in affected_tiles
        )
        
        # 5. APPLY TRANSFORMATION TO ACTUAL SYSTEM
        self.flip_engine._apply_hexagon_transformation(cluster_ids, tiling_data)
        
        # 6. POST-FLIP: Clear cache and recompute with new geometry
        self.energy_model.clear_cache()  # CRITICAL: Force recomputation
        
        new_local_energy = 0.0
        for tile_id in affected_tiles:
            energy = self.energy_model.compute_local_energy(tile_id, tiling_data)
            new_local_energy += energy
        
        delta_energy = new_local_energy - current_local_energy
        
        # 7. METROPOLIS WITH PHYSICAL CONSISTENCY
        accepted = self._metropolis_accept(delta_energy)
        
        if accepted:
            # System already in new physical state - update global energy
            self.current_energy += delta_energy
            self.metrics["flip_statistics"]["accepted"] += 1
        else:
            # RESTORE EXACT PREVIOUS PHYSICAL STATE
            self.flip_engine._restore_physical_state(undo_info, tiling_data)
            # Clear cache again because we computed with wrong geometry
            self.energy_model.clear_cache()
            self.metrics["flip_statistics"]["rejected"] += 1
        
        # 8. COMPLETE DIAGNOSTICS FOR SCIENTIFIC RIGOR
        self.metrics["energy_trajectory"].append(self.current_energy)
        self.metrics["acceptance_sequence"].append(accepted)
        self.metrics["computation_times"].append(time.time() - step_start)
        
        return accepted, delta_energy
    
    def run_mc_sweep(self, tiling_data: Dict, steps: int = 500) -> None:
        """
        Run multiple MC steps with proper energy tracking
        """
        print(f"🔄 Running {steps} MC steps (T={self.temperature})...")
        
        acceptance_count = 0
        for step in range(steps):
            accepted, delta_energy = self.run_mc_step(tiling_data)
            if accepted:
                acceptance_count += 1
            
            # Progress monitoring for scientific observation
            if step % 100 == 0 and step > 0:
                current_rate = acceptance_count / step
                print(f"   Step {step}: E={self.current_energy:.2f}, "
                      f"Acceptance={current_rate:.1%}")
        
        final_rate = acceptance_count / steps
        print(f"✅ MC sweep complete: {acceptance_count}/{steps} accepted "
              f"({final_rate:.1%}), Final E={self.current_energy:.2f}")
    
    def _metropolis_accept(self, delta_energy: float) -> bool:
        """
        Standard Metropolis criterion - preserves detailed balance
        """
        if delta_energy <= 0:
            return True
        
        # Thermal fluctuation acceptance
        return random.random() < math.exp(-delta_energy / self.temperature)
    
    def get_diagnostics(self) -> Dict[str, Any]:
        """
        Return comprehensive diagnostics for scientific analysis
        """
        if not self.metrics["energy_trajectory"]:
            return {}
        
        energy_traj = self.metrics["energy_trajectory"]
        acceptance_seq = self.metrics["acceptance_sequence"]
        
        return {
            "final_energy": self.current_energy,
            "energy_trajectory": energy_traj,
            "acceptance_rate": self.metrics["flip_statistics"]["accepted"] / 
                              max(1, self.metrics["flip_statistics"]["proposed"]),
            "energy_autocorrelation": self._compute_energy_autocorrelation(energy_traj),
            "acceptance_sequence": acceptance_seq,
            "average_computation_time": np.mean(self.metrics["computation_times"]),
            "flip_statistics": self.metrics["flip_statistics"]
        }
    
    def _compute_energy_autocorrelation(self, energy_traj: List[float]) -> float:
        """
        Compute energy autocorrelation for equilibration checking
        """
        if len(energy_traj) < 10:
            return 0.0
        
        # Simple autocorrelation at lag 1
        traj = np.array(energy_traj)
        if np.std(traj) < 1e-12:
            return 0.0
        
        correlation = np.corrcoef(traj[:-1], traj[1:])[0, 1]
        return float(correlation) if not np.isnan(correlation) else 0.0