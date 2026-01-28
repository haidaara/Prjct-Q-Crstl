"""
Healing Engine - Main orchestration of healing process.
"""

import copy
import time
from typing import Dict, List, Tuple, Optional, Any

class HealingEngine:
    """
    Main healing orchestration engine.
    """
    
    def __init__(self, flip_engine, mc_engine, energy_model):
        """
        Initialize healing engine.
        
        Args:
            flip_engine: FlipEngine instance
            mc_engine: MonteCarloEngine instance
            energy_model: Energy model instance
        """
        # Import adapters and policies
        from .adapters import HealingAdapters
        from .region_policy import RegionPolicy
        from .defect_policy import DefectPolicy, DefectCriterion
        from .signature import SignatureComputer
        from .tracker import MetricsTracker
        
        # Initialize adapters
        self.adapters = HealingAdapters(flip_engine, mc_engine, energy_model)
        
        # Default configuration
        self.config = {
            'center': (0.0, 0.0),
            'R_core': 15.0,
            'R_buffer': 25.0,
            'defect_criterion': DefectCriterion.PHYSICS,
            'temperature_schedule': [
                (5.0, 100),   # High T, exploration
                (3.0, 200),   # Medium-high
                (2.0, 300),   # Medium
                (1.0, 400),   # Medium-low
                (0.5, 500),   # Low
                (0.2, 600),   # Very low
                (0.1, 700)    # Freezing
            ],
            'checkpoint_interval': 10,
            'max_defect_creation_attempts': 5000
        }
        
        # State
        self.region_policy = None
        self.defect_policy = None
        self.signature_computer = None
        self.metrics_tracker = None
        self.baseline_signature = None
        
        # Statistics
        self.stats = {
            'total_flips': 0,
            'accepted_flips': 0,
            'defects_created': 0,
            'defects_healed': 0,
            'start_time': None,
            'end_time': None
        }
    
    def configure(self, **kwargs):
        """
        Configure healing engine parameters.
        
        Args:
            **kwargs: Configuration parameters to update
        """
        self.config.update(kwargs)
    
    def prepare_baseline(self, tiling_data: Dict) -> Tuple[Dict, Dict]:
        """
        Prepare baseline tiling and compute baseline signature.
        
        Args:
            tiling_data: Raw tiling data
            
        Returns:
            (baseline_tiling, baseline_signature)
        """
        print("Preparing baseline...")
        
        # Deep copy to avoid modifying original
        baseline_tiling = copy.deepcopy(tiling_data)
        
        # Initialize policies
        from .region_policy import RegionPolicy
        from .defect_policy import DefectPolicy, DefectCriterion
        from .signature import SignatureComputer
        
        self.region_policy = RegionPolicy(
            self.config['center'],
            self.config['R_core'],
            self.config['R_buffer']
        )
        
        self.defect_policy = DefectPolicy(
            criterion=self.config['defect_criterion']
        )
        
        # Apply region policy
        baseline_tiling = self.region_policy.apply(baseline_tiling)
        
        # Refresh energy
        self.adapters.refresh_energy_full(baseline_tiling)
        
        # Initialize signature computer
        self.signature_computer = SignatureComputer(
            self.region_policy,
            self.defect_policy,
            self.adapters.energy_model
        )
        
        # Compute baseline signature
        self.baseline_signature = self.signature_computer.compute_signature(
            baseline_tiling,
            include_phason_strain=True
        )
        
        # Initialize metrics tracker
        from .tracker import MetricsTracker
        self.metrics_tracker = MetricsTracker(self.baseline_signature)
        
        print(f"Baseline prepared: {self.region_policy.validate_regions()}")
        
        return baseline_tiling, self.baseline_signature
    
    def create_controlled_defects(self, tiling_data: Dict, 
                                 target_defects: int) -> Dict:
        """
        Create controlled defects in core region.
        
        Args:
            tiling_data: Tiling with region policy applied
            target_defects: Target number of defects
            
        Returns:
            Modified tiling
        """
        assert self.defect_policy is not None, "Defect policy not initialized. Run prepare_baseline first."

        print(f"Creating {target_defects} controlled defects...")
        
        current_defects = self.defect_policy.count_defects(tiling_data, 'core')
        attempts = 0
        
        while current_defects != target_defects and attempts < self.config['max_defect_creation_attempts']:
            # Get random hexagon in buffer region
            hexagon = self.adapters.get_random_flippable_hexagon(tiling_data)
            if not hexagon:
                attempts += 1
                continue
            
            # Check eligibility (must be in buffer, not immobile, etc.)
            eligible, reason = self.adapters.is_hexagon_eligible(hexagon, tiling_data, require_in_buffer=True)
            if not eligible:
                attempts += 1
                continue
            
            # Capture state for potential revert
            state = self.adapters.capture_state(hexagon, tiling_data)
            
            # Apply flip
            if not self.adapters.apply_force_flip(hexagon, tiling_data):
                attempts += 1
                continue
            
            # Refresh energy for affected region
            affected_tiles = list(set(hexagon))
            for tile_id in hexagon:
                neighbors = tiling_data.get('adjacency_graph', {}).get(str(tile_id), [])
                affected_tiles.extend(int(n) for n in neighbors)
            
            # For correctness during defect targeting:
            self.adapters.refresh_energy_full(tiling_data)

            new_defects = self.defect_policy.count_defects(tiling_data, 'core')


            # Decision: keep or revert
            old_distance = abs(current_defects - target_defects)
            new_distance = abs(new_defects - target_defects)
            
# --- OLD LOGIC (COMMENT ALL THIS OUT) ---
            # if new_distance < old_distance:
            #     # Better: accept
            #     old_defects = current_defects
            #     current_defects = new_defects
            #     delta = max(0, current_defects - old_defects)
            #     self.stats['defects_created'] += delta
            #
            # elif new_distance == old_distance and random.random() < 0.5:
            #     # Same: randomly accept (prevents loops)
            #     current_defects = new_defects
            # else:
            #     # Worse or rejected: revert
            #     self.adapters.restore_state(state, tiling_data)
            #     self.adapters.refresh_energy_region(tiling_data, list(set(affected_tiles)))
            
            # --- NEW LOGIC (INSERT THIS) ---
            # Just accept the flip! We want to scramble the tiling (create strain).
            # We treat every flip as 1 "unit of disorder" created.
            current_defects += 1  
            self.stats['defects_created'] += 1
            
            attempts += 1
            
            if attempts % 100 == 0:
                print(f"  Attempt {attempts}: {current_defects}/{target_defects} defects")
        
        print(f"Defect creation complete: {current_defects}/{target_defects} defects after {attempts} attempts")
        return tiling_data
    
    def run_healing(self, tiling_data: Dict, 
                   temperature_schedule: Optional[List[Tuple[float, int]]] = None) -> Dict:
        """Run healing annealing schedule."""
        # FIX: Ensure components exist
        assert self.metrics_tracker is not None
        assert self.adapters is not None
        assert self.signature_computer is not None

        print("Starting healing annealing...")
        
        if temperature_schedule is None:
            temperature_schedule = self.config['temperature_schedule']
            
        # FIX: Ensure schedule is valid list
        assert temperature_schedule is not None
            
        total_steps = 0
        self.stats['start_time'] = time.time()
        
        for stage_idx, (temperature, steps) in enumerate(temperature_schedule):
            print(f"  Stage {stage_idx + 1}/{len(temperature_schedule)}: T={temperature}, steps={steps}")
            
            # Run MC stage
            stage_stats = self.adapters.run_mc_stage(
                tiling_data=tiling_data,
                temperature=temperature,
                steps=steps,
                progress_callback=lambda p: print(f"    Progress: {p:.1%}")
            )
            
            # Update statistics
            self.stats['total_flips'] += stage_stats.get('proposed', 0)
            self.stats['accepted_flips'] += stage_stats.get('accepted', 0)
            
            # Record checkpoint
            total_steps += steps
            if total_steps % self.config['checkpoint_interval'] == 0:
                # Refresh energy and compute signature
                self.adapters.refresh_energy_full(tiling_data)
                current_signature = self.signature_computer.compute_signature(tiling_data)
                
                # Record checkpoint
                checkpoint = self.metrics_tracker.record_checkpoint(
                    step=total_steps,
                    temperature=temperature,
                    signature=current_signature,
                    acceptance_rate=self.adapters.get_acceptance_rate()
                )
                
                # Check for early convergence
                if checkpoint['convergence']['fully_converged']:
                    print(f"    Early convergence at step {total_steps}")
                    break
            
            # Check for stagnation
            if self.metrics_tracker.detect_stagnation():
                print(f"    Stagnation detected at step {total_steps}")
                break
        
        self.stats['end_time'] = time.time()
        print(f"Healing complete: {total_steps} total steps")
        
        return tiling_data
    
    def validate_healing(self, tiling_data: Dict) -> Tuple[bool, str, Dict]:
        """Validate healing results."""
        # FIX: Ensure components exist
        assert self.signature_computer is not None
        assert self.metrics_tracker is not None

        print("Validating healing...")
        
        # Final energy refresh
        self.adapters.refresh_energy_full(tiling_data)
        
        # Compute final signature
        final_signature = self.signature_computer.compute_signature(tiling_data)
        
        # Get final checkpoint
        if self.metrics_tracker.history:
            final_checkpoint = self.metrics_tracker.history[-1]
            convergence = final_checkpoint['convergence']
        else:
            convergence = {'fully_converged': False}
        
        # Compute healing metrics
        healing_metrics = self.metrics_tracker.compute_healing_metrics()
        
        # Determine success
        if convergence['fully_converged']:
            success = True
            message = "Healing successful: converged to baseline signature"
        elif healing_metrics['healing_efficiency'] > 0.7:  # 70% efficiency threshold
            success = True
            message = f"Healing partially successful: {healing_metrics['healing_efficiency']:.1%} efficiency"
        else:
            success = False
            message = f"Healing failed: {healing_metrics['healing_efficiency']:.1%} efficiency"
        
        # Update statistics
        initial_defects = healing_metrics.get('defects_initial', 0)
        final_defects = healing_metrics.get('defects_final', 0)
        self.stats['defects_healed'] = max(0, initial_defects - final_defects)
        
        return success, message, healing_metrics
    
    def run_full_experiment(self, tiling_data: Dict, 
                           create_defects: bool = True,
                           target_defects: int = 15) -> Tuple[Dict[str, Any], Dict]:
        """
        Run full healing experiment.
        
        Args:
            tiling_data: Raw tiling data
            create_defects: Whether to create controlled defects
            target_defects: Number of defects to create
            
        Returns:
            Experiment results
        """
        print("=" * 60)
        print("HEALING EXPERIMENT START")
        print("=" * 60)
        
        # 1. Prepare baseline
        baseline_tiling, baseline_signature = self.prepare_baseline(tiling_data)
        
        # 2. Prepare experiment tiling
        experiment_tiling = copy.deepcopy(tiling_data)
        experiment_tiling = self.region_policy.apply(experiment_tiling)
        
        # 3. Create defects if requested
        if create_defects:
            # FIX: Ensure policy exists (it was created in step 1, but Pylance needs reassurance)
            assert self.defect_policy is not None
            initial_defects = self.defect_policy.count_defects(experiment_tiling, 'core')
            if initial_defects < target_defects:
                experiment_tiling = self.create_controlled_defects(experiment_tiling, target_defects)
        
        # 4. Record initial checkpoint
        self.adapters.refresh_energy_full(experiment_tiling)
        initial_signature = self.signature_computer.compute_signature(experiment_tiling)
        
        initial_checkpoint = self.metrics_tracker.record_checkpoint(
            step=0,
            temperature=0.0,
            signature=initial_signature,
            acceptance_rate=0.0
        )
        
        # 5. Run healing
        healed_tiling = self.run_healing(experiment_tiling)
        
        # 6. Validate
        success, message, metrics = self.validate_healing(healed_tiling)
        
        # 7. Compile results
        results = {
            'success': success,
            'message': message,
            'metrics': metrics,
            'statistics': self.stats,
            'configuration': self.config,
            'region_info': self.region_policy.validate_regions(),
            'defect_info': self.defect_policy.compute_defect_statistics(healed_tiling),
            'baseline_defects': self.baseline_signature['core']['defect_count'],
            'final_defects': metrics.get('defects_final', 0),
            'healing_efficiency': metrics.get('healing_efficiency', 0.0),
            'convergence_step': metrics.get('convergence_step'),
            'total_time': self.stats['end_time'] - self.stats['start_time'] if self.stats['end_time'] else 0
        }
        
        # Print summary
        print("\n" + "=" * 60)
        print("HEALING EXPERIMENT SUMMARY")
        print("=" * 60)
        print(f"Success: {success}")
        print(f"Message: {message}")
        print(f"Healing Efficiency: {results['healing_efficiency']:.1%}")
        print(f"Time: {results['total_time']:.1f}s")
        print(f"Final Defects: {results['final_defects']} (Baseline: {results['baseline_defects']})")
        print(f"Acceptance Rate: {metrics.get('acceptance_rate_mean', 0.0):.3f}")
        
        return results, healed_tiling