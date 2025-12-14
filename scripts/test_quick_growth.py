#!/usr/bin/env python3
"""
Quick test to verify growth system works
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing imports...")
    
    # Add project root to path
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    
    try:
        from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
        print("✅ CombinatorialVertexClassifier imported")
        
        from src.energy.widom_inspired_energy import EnergyParameters, WidomInspiredEnergy
        print("✅ WidomInspiredEnergy imported")
        
        from src.simulation.flip_engine import FlipEngine
        print("✅ FlipEngine imported")
        
        from src.simulation.mc_engine import MonteCarloEngine
        print("✅ MonteCarloEngine imported")
        
        from src.simulation.growth_engine import GrowthSimulator
        print("✅ GrowthSimulator imported")
        
        print("\n✅ All imports successful!")
        return True
        
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)