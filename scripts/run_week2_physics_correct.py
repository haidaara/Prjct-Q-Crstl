#!/usr/bin/env python3
"""
Week 2 Physics-Correct Implementation - Full Integration Test
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def main():
    print("🚀 WEEK 2: Physics-Correct Implementation")
    print("=" * 50)
    
    # 1. Load existing energy-initialized tiling
    from src.utils.io import load_tiling
    tiling_data = load_tiling("data/processed/penrose_tiling_energy_initialized.json")
    print(f"✅ Loaded tiling: {len(tiling_data['tiles'])} tiles")
    
    # 2. Initialize physics-correct components
    from src.utils.config import ConfigManager
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy
    
    config = ConfigManager("configs/phase1_baseline.toml")
    
    # Core physics components
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy.from_config(config)
    
    # Week 2 physics-correct components
    from src.simulation.flip.physics_correct_flip_engine import PhysicsCorrectFlipEngine
    from src.simulation.monte_carlo.physics_correct_mc import PhysicsCorrectMCEngine
    from src.growth.physics_correct_growth import PhysicsCorrectGrowthSimulator
    
    flip_engine = PhysicsCorrectFlipEngine(classifier, energy_model)
    mc_engine = PhysicsCorrectMCEngine(temperature=0.3, energy_model=energy_model, 
                                     flip_engine=flip_engine)
    growth_engine = PhysicsCorrectGrowthSimulator(mc_engine)
    
    print("✅ Physics-correct components initialized")
    
    # 3. Initialize energy tracking
    mc_engine.initialize_energy(tiling_data)
    
    # 4. Test MC relaxation
    print("\n🔬 Testing MC Relaxation...")
    initial_energy = mc_engine.current_energy
    mc_engine.run_mc_sweep(tiling_data, steps=50)
    final_energy = mc_engine.current_energy
    
    mc_diagnostics = mc_engine.get_diagnostics()
    print(f"✅ MC relaxation: {initial_energy:.2f} → {final_energy:.2f}")
    print(f"✅ Acceptance rate: {mc_diagnostics['acceptance_rate']:.1%}")
    
    # 5. Test growth integration
    print("\n🌱 Testing Growth Integration...")
    seed_center = [30.0, 30.0]  # Center of 60x60 window
    
    # Initialize growth
    tiling_data = growth_engine.initialize_growth_seed(tiling_data, seed_center, radius=8.0)
    
    # Run one growth step
    obstacles = {}  # Load actual obstacles here
    tiling_data, new_tiles = growth_engine.propagate_growth_front(tiling_data, obstacles)
    
    growth_diagnostics = growth_engine.get_growth_diagnostics()
    print(f"✅ Growth test: added {len(new_tiles)} tiles")
    print(f"✅ Total growth steps: {growth_diagnostics['current_step']}")
    
    # 6. Final validation
    print("\n📊 FINAL VALIDATION")
    print("=" * 50)
    
    # Check physics consistency
    energy_consistent = abs(mc_engine.current_energy - 
                           energy_model.compute_total_energy(tiling_data)) < 0.01
    
    print(f"✅ Energy consistency: {energy_consistent}")
    print(f"✅ Final energy: {mc_engine.current_energy:.2f}")
    print(f"✅ Total MC steps: {mc_diagnostics['flip_statistics']['proposed']}")
    print(f"✅ Growth steps completed: {growth_diagnostics['current_step']}")
    
    if energy_consistent:
        print("\n🎉 WEEK 2 IMPLEMENTATION SUCCESSFUL!")
        print("   Physics-correct MC and growth systems are operational")
        return True
    else:
        print("\n❨ Energy consistency check failed - investigate physics")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)