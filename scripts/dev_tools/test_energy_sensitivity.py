#!/usr/bin/env python3
"""
RELIABLE energy model sensitivity test with proper state restoration
"""

import json
import sys
import random
import numpy as np
sys.path.insert(0, '.')

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine

def test_energy_sensitivity():
    """Test if flips actually change energy - RELIABLE VERSION"""
    print("🔬 RELIABLE ENERGY SENSITIVITY TEST")
    print("=" * 60)
    
    # Load fresh tiling for each test
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        original_tiling = json.load(f)
    
    # Initialize components
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find flippable hexagons
    hexagons = flip_engine.find_flippable_hexagons(original_tiling)
    print(f"Found {len(hexagons)} flippable hexagons")
    
    # Test 10 random flips
    sample = random.sample(hexagons, min(10, len(hexagons)))
    
    delta_energies = []
    success_count = 0
    
    for i, hexagon in enumerate(sample):
        # IMPORTANT: Create fresh copy for each test
        with open('data/processed/penrose_tiling_energy_initialized.json') as f:
            tiling = json.load(f)
        
        # Get two-ring neighborhood (what MC actually uses)
        neighborhood = flip_engine._get_two_ring_neighborhood(hexagon, tiling)
        
        # Capture state BEFORE flip
        undo_info = flip_engine.capture_state(hexagon, tiling)
        
        # Compute energy before flip (sum of local_energy in neighborhood)
        energy_before = 0
        for tile_id in neighborhood:
            tile = tiling['tiles'][tile_id]
            if not tile.get('removed', False):
                energy_before += tile.get('local_energy', 0)
        
        # Apply flip
        success = flip_engine.apply_flip(hexagon, tiling)
        
        if not success:
            print(f"❌ Flip {i+1} failed geometrically")
            flip_engine.restore_state(undo_info, tiling)
            continue
        
        success_count += 1
        
        # Recompute energy for all affected tiles (same as MC engine does)
        energy_after = 0
        for tile_id in neighborhood:
            tile = tiling['tiles'][tile_id]
            if not tile.get('removed', False):
                # Force energy recomputation (clear cache)
                if hasattr(energy_model, '_vertex_class_cache'):
                    energy_model._vertex_class_cache.pop(tile_id, None)
                energy_after += energy_model.compute_local_energy(tile_id, tiling)
        
        delta = energy_after - energy_before
        delta_energies.append(delta)
        
        # Restore original state for next test
        flip_engine.restore_state(undo_info, tiling)
        
        # Minimal output
        print(f"Flip {i+1}: ΔE = {delta:+.6f}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 RELIABLE SUMMARY:")
    print(f"Successful flips: {success_count}/{len(sample)}")
    
    if delta_energies:
        delta_arr = np.array(delta_energies)
        print(f"ΔE mean: {np.mean(delta_arr):+.6f}")
        print(f"ΔE std:  {np.std(delta_arr):.6f}")
        print(f"ΔE range: [{np.min(delta_arr):+.6f}, {np.max(delta_arr):+.6f}]")
        
        # Physics analysis
        print("\n🚨 PHYSICS ANALYSIS:")
        
        # Check energy scale
        max_abs_delta = np.max(np.abs(delta_arr))
        if max_abs_delta < 0.001:
            print("❌ ENERGY MODEL IS FLAT (ΔE < 0.001)")
            print("   Flips don't change energy - no driving force for healing")
            print("   Expected: ΔE should be ~0.1-2.0 for meaningful MC")
        elif max_abs_delta < 0.1:
            print("⚠️  ENERGY MODEL IS VERY SOFT (ΔE < 0.1)")
            print("   Flips change energy slightly - weak driving force")
            print("   Temperature effects will be minimal")
        else:
            print("✅ ENERGY MODEL HAS MEANINGFUL SCALE")
            print(f"   ΔE range indicates proper energy barriers")
        
        # Check sign distribution
        uphill_ratio = np.sum(delta_arr > 0) / len(delta_arr)
        print(f"\n📈 UPHILL/DOWNHILL RATIO:")
        print(f"   Downhill moves (ΔE < 0): {100*(1-uphill_ratio):.1f}%")
        print(f"   Uphill moves (ΔE > 0): {100*uphill_ratio:.1f}%")
        
        # Temperature guidance
        if len(delta_energies) > 3:
            avg_abs_delta = np.mean(np.abs(delta_arr))
            print(f"\n🌡️  TEMPERATURE GUIDANCE:")
            print(f"   For T ≈ avg(|ΔE|) = {avg_abs_delta:.3f}:")
            print(f"   exp(-ΔE/T) ≈ {np.exp(-1):.3f} for ΔE = avg")
            if avg_abs_delta > 0:
                print(f"   Suggested T range: {0.5*avg_abs_delta:.3f} to {2*avg_abs_delta:.3f}")
    else:
        print("❌ NO SUCCESSFUL FLIPS - CHECK FLIP ENGINE")
    
    return delta_energies

if __name__ == "__main__":
    deltas = test_energy_sensitivity()