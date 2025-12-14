#!/usr/bin/env python3
"""
Simple test script to verify growth system works
"""

import sys
from pathlib import Path

def test_baseline():
    """Run minimal test to verify system works"""
    print("🧪 Testing growth system baseline...")
    
    import os
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    
    try:
        # Import to verify no syntax errors
        from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
        from src.energy.widom_inspired_energy import EnergyParameters, WidomInspiredEnergy
        from src.simulation.flip_engine import FlipEngine
        from src.simulation.mc_engine import MonteCarloEngine
        from src.simulation.growth_engine import GrowthSimulator
        
        print("✅ All imports successful")
        
        # Create minimal config
        config = {
            "growth": {
                "seed_radius": 5.0,
                "growth_steps": 3,
                "mc_steps_per_growth": 10
            },
            "monte_carlo": {
                "temperature": 1.5,
                "base_steps": 50,
                "burn_in_steps": 10
            }
        }
        
        # Create instances
        classifier = CombinatorialVertexClassifier()
        energy_params = EnergyParameters()
        energy_model = WidomInspiredEnergy(energy_params)
        flip_engine = FlipEngine(classifier, energy_model)
        mc_engine = MonteCarloEngine(
            temperature=1.5,
            energy_model=energy_model,
            flip_engine=flip_engine,
            config=config["monte_carlo"]
        )
        growth_sim = GrowthSimulator(mc_engine, config["growth"])
        
        print("✅ All components instantiated")
        print("\nSystem is ready for testing!")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_baseline()
    sys.exit(0 if success else 1)