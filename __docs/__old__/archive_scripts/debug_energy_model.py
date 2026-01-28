#!/usr/bin/env python3
"""
Debug energy model computation - verify it's working correctly
"""

# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------

import json
import sys

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters

import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def debug_energy_model():
    """Debug the energy model calculation"""
    print("🔍 ENERGY MODEL DEBUG")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    
    # Test 1: Verify energy computation for a few tiles
    test_tiles = [0, 100, 500, 1000, 2000]
    
    print("Testing energy computation for individual tiles:")
    print("-" * 60)
    
    for tile_id in test_tiles:
        tile = tiling["tiles"][tile_id]
        
        # Get existing energy
        existing_energy = tile.get("local_energy", 0)
        
        # Recompute
        energy_model.clear_cache()
        recomputed = energy_model.compute_local_energy(tile_id, tiling)
        
        # Get vertex class
        vertex_class = tile.get("vertex_class", "UNKNOWN")
        
        print(f"Tile {tile_id:4d}: {tile['type']:6s} | "
              f"Class: {vertex_class:12s} | "
              f"Existing: {existing_energy:7.4f} | "
              f"Recomputed: {recomputed:7.4f} | "
              f"Match: {abs(existing_energy - recomputed) < 0.001}")
    
    # Test 2: Verify total energy
    print("\n" + "=" * 60)
    print("Testing total energy calculation:")
    
    # Clear cache
    energy_model.clear_cache()
    
    # Method 1: Sum of existing local_energy
    sum_local = sum(t.get("local_energy", 0) for t in tiling["tiles"] 
                   if not t.get("removed", False))
    
    # Method 2: compute_total_energy
    total_energy = energy_model.compute_total_energy(tiling)
    
    print(f"Sum of local_energy: {sum_local:.6f}")
    print(f"compute_total_energy: {total_energy:.6f}")
    print(f"Difference: {abs(sum_local - total_energy):.6f}")
    
    if abs(sum_local - total_energy) < 0.001:
        print("✅ Energy calculation consistent")
    else:
        print("❌ Energy calculation inconsistent!")
        print("   Check if energy model updates tile['local_energy'] properly")
    
    # Test 3: Check energy model parameters
    print("\n" + "=" * 60)
    print("Current energy model parameters:")
    print(f"  high_energy_penalty: {energy_model.params.high_energy_penalty}")
    print(f"  medium_energy_penalty: {energy_model.params.medium_energy_penalty}")
    print(f"  low_energy_reference: {energy_model.params.low_energy_reference}")
    print(f"  neighbor_interaction_strength: {energy_model.params.neighbor_interaction_strength}")
    print(f"  geometric_strain_penalty: {energy_model.params.geometric_strain_penalty}")
    
    # Test 4: Check vertex classification distribution
    print("\n" + "=" * 60)
    print("Vertex classification distribution:")
    
    classes = {}
    for tile in tiling["tiles"]:
        if tile.get("removed", False):
            continue
        cls = tile.get("vertex_class", "UNKNOWN")
        classes[cls] = classes.get(cls, 0) + 1
    
    total = sum(classes.values())
    for cls, count in classes.items():
        print(f"  {cls:12s}: {count:4d} tiles ({count/total:.1%})")
    
    # Expected ratios
    print(f"\nExpected for ideal Penrose tiling:")
    print(f"  LOW_ENERGY: >95% (ideal local environments)")
    print(f"  MEDIUM_ENERGY: <5% (boundaries, strains)")
    print(f"  HIGH_ENERGY: <1% (defects)")
    
    # Conclusion
    print("\n" + "=" * 60)
    print("🎯 DIAGNOSIS:")
    
    low_pct = classes.get("LOW_ENERGY", 0) / total if total > 0 else 0
    if low_pct > 0.95:
        print("✅ Tiling is mostly low-energy (good starting point)")
    else:
        print(f"⚠️  Only {low_pct:.1%} low-energy tiles")
        print("   Many strained/defective tiles initially")
    
    return {
        "energy_consistent": abs(sum_local - total_energy) < 0.001,
        "class_distribution": classes,
        "parameters": vars(energy_model.params)
    }

if __name__ == "__main__":
    debug_energy_model()