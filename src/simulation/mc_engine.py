# src/simulation/mc_engine.py
"""
Monte Carlo engine with proper energy consistency verification
FIXED VERSION: Implements Option A (Radius 4 for Delta E, Radius 3 for Geometry)
"""

import math
import random
import time
from typing import Dict, List, Tuple, Any, Optional
import numpy as np

from src.utils.energy_utils import (
    wipe_all_energy_fields, clear_all_caches,
    get_k_ring_neighborhood, compute_total_energy_fresh,
    verify_energy_convention
)

class MonteCarloEngine:
    """
    Monte Carlo engine that preserves detailed balance with verified energy consistency
    """
    
    def __init__(self, temperature: float = 0.3, energy_model=None, 
                 flip_engine=None, config: Optional[Dict] = None):
        self.temperature = temperature
        self.energy_model = energy_model
        self.flip_engine = flip_engine
        self.config = config or {}
        
        # CRITICAL PHYSICS PARAMETER:
        # Radius 3 is required for geometry/class propagation consistency.
        # However, delta_E calculation requires Radius 4 due to asymmetric neighbor terms.
        req_radius = self.config.get("neighborhood_radius", 3)
        self.neighborhood_radius = max(req_radius, 3)
        
        # Global energy tracking
        self.current_energy = 0.0
        
        # Configurable parameters
        self.base_steps = self.config.get("base_steps", 500)
        self.burn_in_steps = self.config.get("burn_in_steps", 100)
        
        # Verification settings
        self.verify_frequency = self.config.get("verify_frequency", 0.1)
        self.verify_energy = self.config.get("verify_energy", False)
        
        # Diagnostics
        self.metrics = {
            "energy_history": [],
            "acceptance_rates": [],
            "computation_times": [],
            "flip_stats": {"proposed": 0, "accepted": 0, "rejected": 0},
            "energy_drift_history": [],
            "delta_energy_history": []
        }
    
    def initialize_energy(self, tiling_data: Dict) -> None:
        """Compute initial total energy with fresh computation"""
        self.current_energy = compute_total_energy_fresh(self.energy_model, tiling_data)
        self.metrics["energy_history"].append(self.current_energy)
    
    def _compute_region_energy_fresh(self, tile_ids: List[int], tiling_data: Dict, 
                                   extra_ring: int = 1) -> float:
        """
        Compute total energy of region with fresh computation.
        Wipes region + extra_ring to prevent neighbor contamination.
        """
        # Get region to wipe (region + extra ring)
        wipe_region = get_k_ring_neighborhood(tile_ids, tiling_data, k=extra_ring)
        
        # Wipe energy fields in wipe_region
        for tile_id in wipe_region:
            tile = tiling_data["tiles"][tile_id]
            tile.pop("local_energy", None)
            tile.pop("vertex_class", None)
        
        # Clear caches
        clear_all_caches(self.energy_model)
        
        # Compute fresh energy ONLY for the requested tile_ids
        energy = 0.0
        for tile_id in tile_ids:
            tile = tiling_data["tiles"][tile_id]
            if not tile.get("removed", False):
                energy += self.energy_model.compute_local_energy(tile_id, tiling_data)
        
        return energy
    
    def _verify_energy_consistency(self, tiling_data: Dict, message: str = "") -> float:
        """Verify current_energy matches recomputed total energy"""
        actual_energy = compute_total_energy_fresh(self.energy_model, tiling_data)
        drift = abs(actual_energy - self.current_energy)
        
        if drift > 0.001:
            print(f"⚠️  ENERGY DRIFT {message}: {drift:.6f} "
                  f"(MC={self.current_energy:.6f}, actual={actual_energy:.6f})")
        
        self.metrics["energy_drift_history"].append(drift)
        return drift
    
    def run_step(self, tiling_data: Dict, debug_mode: bool = False) -> Tuple[bool, float]:
        """Single MC step with verified energy consistency"""
        step_start = time.time()
        self.metrics["flip_stats"]["proposed"] += 1
        
        # Find flippable clusters
        flippable_clusters = self.flip_engine.find_flippable_hexagons(tiling_data)
        if not flippable_clusters:
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0
        
        cluster_ids = random.choice(flippable_clusters)
        
        # ---------------------------------------------------------
        # OPTION A FIX: Split Physics Radius vs Energy Radius
        # ---------------------------------------------------------
        
        # 1. Core Region (Radius 3): The region physically affected by the flip
        #    This is used for geometry updates and adjacency consistency.
        core_region = get_k_ring_neighborhood(
            cluster_ids, tiling_data, k=self.neighborhood_radius
        )
        
        # 2. Delta Region (Radius 4): The region needed for Energy Summation
        #    Because neighbor interactions are asymmetric, an update in the Core Region
        #    changes the computed energy of tiles one step further out.
        delta_region = get_k_ring_neighborhood(
            list(core_region), tiling_data, k=1
        )
        
        # 3. Capture State (Use Delta Region)
        #    We must capture the full delta_region so that if we reject,
        #    we restore the energy values of the 4th ring too.
        undo_info = self.flip_engine.capture_state(list(delta_region), tiling_data)
        
        # 4. Compute Energy BEFORE (Sum over Delta Region)
        energy_before = self._compute_region_energy_fresh(
            list(delta_region), tiling_data, extra_ring=1
        )
        
        # 5. Apply Flip (Uses Core Region Logic internally)
        success = self.flip_engine.apply_flip(cluster_ids, tiling_data)
        if not success:
            self.flip_engine.restore_state(undo_info, tiling_data)
            self.metrics["flip_stats"]["rejected"] += 1
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0
        
        # 6. Compute Energy AFTER (Sum over Delta Region)
        energy_after = self._compute_region_energy_fresh(
            list(delta_region), tiling_data, extra_ring=1
        )
        
        delta_energy = energy_after - energy_before
        
        # 7. Metropolis Acceptance
        accepted = self._metropolis_accept(delta_energy)
        
        if accepted:
            # Update global energy
            self.current_energy += delta_energy
            self.metrics["flip_stats"]["accepted"] += 1
            
            if debug_mode:
                self._verify_energy_consistency(tiling_data, f"step {len(self.metrics['energy_history'])}")
            elif self.verify_energy and random.random() < self.verify_frequency:
                self._verify_energy_consistency(tiling_data)
        else:
            # REJECT: Restore state (Restores Delta Region)
            self.flip_engine.restore_state(undo_info, tiling_data)
            
            # Safety: Wipe and recompute to ensure no stale cache remains after restore
            self._compute_region_energy_fresh(list(delta_region), tiling_data, extra_ring=1)
            
            self.metrics["flip_stats"]["rejected"] += 1
        
        # Record metrics
        self.metrics["energy_history"].append(self.current_energy)
        self.metrics["delta_energy_history"].append(delta_energy)
        self.metrics["computation_times"].append(time.time() - step_start)
        
        return accepted, delta_energy

    def run_debug_validation(self, tiling_data: Dict, steps: int = 200) -> Dict:
        """Run MC with full verification for debugging"""
        print(f"🔍 Running debug validation for {steps} steps...")
        self.metrics["energy_drift_history"] = []
        stats = self.run_sweep(tiling_data, steps=steps, debug_mode=True)
        return stats
        
    def run_sweep(self, tiling_data: Dict, steps: Optional[int] = None, 
                  debug_mode: bool = False) -> Dict:
        """Run multiple MC steps with verification"""
        if steps is None:
            steps = self.base_steps
        
        acceptance_count = 0
        delta_energies = []
        
        for step in range(steps):
            accepted, delta = self.run_step(tiling_data, debug_mode=debug_mode)
            if accepted:
                acceptance_count += 1
                delta_energies.append(delta)
        
        final_rate = acceptance_count / steps if steps > 0 else 0.0
        
        stats = {
            "steps": steps,
            "accepted": acceptance_count,
            "acceptance_rate": final_rate,
            "final_energy": self.current_energy,
            "delta_mean": np.mean(delta_energies) if delta_energies else 0.0,
            "delta_std": np.std(delta_energies) if len(delta_energies) > 1 else 0.0,
            "positive_ratio": np.sum(np.array(delta_energies) > 0) / len(delta_energies) if delta_energies else 0.0,
            "max_drift": max(self.metrics["energy_drift_history"]) if self.metrics["energy_drift_history"] else 0.0
        }
        
        print(f"✅ MC sweep: {acceptance_count}/{steps} accepted ({final_rate:.1%}), max drift: {stats['max_drift']:.6f}")
        return stats
    
    def _metropolis_accept(self, delta_energy: float) -> bool:
        if delta_energy <= 0:
            return True
        return random.random() < math.exp(-delta_energy / self.temperature)
    
    def get_diagnostics(self) -> Dict[str, Any]:
        return {
            "temperature": self.temperature,
            "final_energy": self.current_energy,
            "config": {"neighborhood_radius": self.neighborhood_radius}
        }