# src/simulation/mc_engine.py
"""
Monte Carlo engine with configurable parameters
"""

import math
import random
import time
from typing import Dict, List, Tuple, Any, Optional
import numpy as np

class MonteCarloEngine:
    """
    Monte Carlo engine that preserves detailed balance and physical consistency
    """
    
    def __init__(self, temperature: float = 0.3, energy_model=None, 
                 flip_engine=None, config: Optional[Dict] = None):
        self.temperature = temperature
        self.energy_model = energy_model
        self.flip_engine = flip_engine
        self.config = config or {}
        
        # Global energy tracking
        self.current_energy = 0.0
        
        # Configurable parameters
        self.base_steps = self.config.get("base_steps", 500)
        self.burn_in_steps = self.config.get("burn_in_steps", 100)
        
        # Diagnostics
        self.metrics = {
            "energy_history": [],
            "acceptance_rates": [],
            "computation_times": [],
            "flip_stats": {"proposed": 0, "accepted": 0, "rejected": 0}
        }
    
    def initialize_energy(self, tiling_data: Dict) -> None:
        """Compute initial total energy once for consistency"""
        self.current_energy = self.energy_model.compute_total_energy(tiling_data)
        self.metrics["energy_history"].append(self.current_energy)
    
    def run_step(self, tiling_data: Dict) -> Tuple[bool, float]:
        """Single MC step with 2-ring neighborhood energy calculation"""
        step_start = time.time()
        self.metrics["flip_stats"]["proposed"] += 1
        
        # Find flippable clusters (respects tile["flippable"])
        flippable_clusters = self.flip_engine.find_flippable_hexagons(tiling_data)
        if not flippable_clusters:
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0
        
        cluster_ids = random.choice(flippable_clusters)
        
        # Get COMPLETE neighborhood (2-ring for ΔE correctness)
        affected_tiles = self.flip_engine._get_two_ring_neighborhood(cluster_ids, tiling_data)
        
        # Capture state (including geometry)
        undo_info = self.flip_engine.capture_state(cluster_ids, tiling_data)
        
        # Compute pre-flip energy for ALL affected tiles
        current_energy = 0.0
        for tile_id in affected_tiles:
            tile = tiling_data["tiles"][tile_id]
            if not tile.get("removed", False):
                current_energy += tile["local_energy"]
        
        # Apply flip
        success = self.flip_engine.apply_flip(cluster_ids, tiling_data)
        if not success:
            self.flip_engine.restore_state(undo_info, tiling_data)
            self.metrics["flip_stats"]["rejected"] += 1
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0
        
        self.energy_model.clear_cache()
        
        # Recompute energy for all affected tiles
        new_energy = 0.0
        for tile_id in affected_tiles:
            tile = tiling_data["tiles"][tile_id]
            if not tile.get("removed", False):
                energy = self.energy_model.compute_local_energy(tile_id, tiling_data)
                new_energy += energy
        
        delta_energy = new_energy - current_energy
        
        # Metropolis acceptance
        accepted = self._metropolis_accept(delta_energy)
        
        if accepted:
            self.current_energy += delta_energy
            self.metrics["flip_stats"]["accepted"] += 1
        else:
            self.flip_engine.restore_state(undo_info, tiling_data)
            self.energy_model.clear_cache()
            self.metrics["flip_stats"]["rejected"] += 1
        
        # Record
        self.metrics["energy_history"].append(self.current_energy)
        self.metrics["computation_times"].append(time.time() - step_start)
        
        return accepted, delta_energy
    
    def run_sweep(self, tiling_data: Dict, steps: Optional[int] = None) -> Dict:
        """Run multiple MC steps with configurable length"""
        if steps is None:
            steps = self.base_steps
        
        acceptance_count = 0
        delta_energies = []
        
        # Run burn-in steps if configured
        if hasattr(self, 'burn_in_steps') and self.burn_in_steps > 0 and len(self.metrics["energy_history"]) == 1:
            print(f"   Running {self.burn_in_steps} burn-in steps...")
            for _ in range(self.burn_in_steps):
                accepted, delta = self.run_step(tiling_data)
                if accepted:
                    acceptance_count += 1
                    delta_energies.append(delta)
        
        # Reset counters for main sweep
        sweep_acceptance = 0
        sweep_deltas = []
        
        for step in range(steps):
            accepted, delta_energy = self.run_step(tiling_data)
            if accepted:
                sweep_acceptance += 1
                sweep_deltas.append(delta_energy)
            
            # Optional progress reporting for long sweeps
            if steps > 100 and (step + 1) % (steps // 5) == 0:
                current_rate = sweep_acceptance / (step + 1)
                print(f"   MC step {step + 1}: E={self.current_energy:.2f}, "
                      f"Acceptance={current_rate:.1%}")
        
        final_rate = sweep_acceptance / steps
        
        # Calculate statistics
        stats = {
            "steps": steps,
            "accepted": sweep_acceptance,
            "acceptance_rate": final_rate,
            "final_energy": self.current_energy,
            "delta_mean": 0.0,
            "delta_std": 0.0,
            "positive_ratio": 0.0
        }
        
        if sweep_deltas:
            stats["delta_mean"] = float(np.mean(sweep_deltas))
            stats["delta_std"] = float(np.std(sweep_deltas)) if len(sweep_deltas) > 1 else 0.0
            stats["positive_ratio"] = float(sum(1 for d in sweep_deltas if d > 0) / len(sweep_deltas))
        
        print(f"✅ MC sweep: {sweep_acceptance}/{steps} accepted ({final_rate:.1%})")
        return stats
    
    def _metropolis_accept(self, delta_energy: float) -> bool:
        """Standard Metropolis criterion"""
        if delta_energy <= 0:
            return True
        return random.random() < math.exp(-delta_energy / self.temperature)
    
    def get_diagnostics(self) -> Dict[str, Any]:
        """Return comprehensive diagnostics"""
        if not self.metrics["energy_history"]:
            return {}
        
        proposed = max(1, self.metrics["flip_stats"]["proposed"])
        
        return {
            "temperature": self.temperature,
            "final_energy": self.current_energy,
            "energy_trajectory": self.metrics["energy_history"],
            "acceptance_rate": self.metrics["flip_stats"]["accepted"] / proposed,
            "flip_statistics": self.metrics["flip_stats"],
            "config": {
                "base_steps": self.base_steps,
                "burn_in_steps": self.burn_in_steps
            }
        }