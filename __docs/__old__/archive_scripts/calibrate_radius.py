
# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------
# scripts/test_neighborhood_radius.py
#!/usr/bin/env python3
"""
Test to find minimum neighborhood radius for accurate ΔE calculation
"""

import json
import sys

import numpy as np
from src.utils.energy_utils import (
    wipe_all_energy_fields, clear_all_caches,
    get_k_ring_neighborhood, compute_total_energy_fresh
)
from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine

def test_neighborhood_radius(num_tests=20):
    """Find required neighborhood radius for accurate ΔE"""
    print("🔬 TESTING NEIGHBORHOOD RADIUS FOR ENERGY CONSISTENCY")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Setup fresh instances
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy(EnergyParameters())
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find flippable hexagons
    flips = flip_engine.find_flippable_hexagons(tiling)[:num_tests]
    
    print(f"Testing {len(flips)} random flips...")
    
    radius_stats = {1: [], 2: [], 3: [], 4: [], 5: []}
    
    for i, flip in enumerate(flips):
        print(f"\nTest {i+1}/{len(flips)}: Flip {flip}")
        
        # 1. Compute GLOBAL ΔE (true reference)
        # Create fresh copies
        tiling_before = json.loads(json.dumps(tiling))
        tiling_after = json.loads(json.dumps(tiling))
        
        # Compute energy BEFORE
        E_before_global = compute_total_energy_fresh(energy_model, tiling_before)
        
        # Apply flip
        flip_engine.apply_flip(flip, tiling_after)
        
        # Compute energy AFTER
        E_after_global = compute_total_energy_fresh(energy_model, tiling_after)
        
        ΔE_global = E_after_global - E_before_global
        print(f"  Global ΔE: {ΔE_global:.6f}")
        
        # 2. Test different radii
        for radius in sorted(radius_stats.keys()):
            # Fresh tiling copy for this test
            tiling_test = json.loads(json.dumps(tiling))
            
            # Get neighborhood
            neighborhood = get_k_ring_neighborhood(flip, tiling_test, k=radius)
            
            # Wipe everything in neighborhood + 1 extra ring
            wipe_region = get_k_ring_neighborhood(list(neighborhood), tiling_test, k=1)
            for tid in wipe_region:
                tile = tiling_test["tiles"][tid]
                tile.pop("local_energy", None)
                tile.pop("vertex_class", None)
            clear_all_caches(energy_model)
            
            # Compute energy BEFORE in neighborhood
            E_before_local = 0
            for tile_id in neighborhood:
                tile = tiling_test["tiles"][tile_id]
                if not tile.get("removed", False):
                    E_before_local += energy_model.compute_local_energy(tile_id, tiling_test)
            
            # Apply flip
            flip_engine.apply_flip(flip, tiling_test)
            
            # Wipe again
            for tid in wipe_region:
                tile = tiling_test["tiles"][tid]
                tile.pop("local_energy", None)
                tile.pop("vertex_class", None)
            clear_all_caches(energy_model)
            
            # Compute energy AFTER in same neighborhood
            E_after_local = 0
            for tile_id in neighborhood:
                tile = tiling_test["tiles"][tile_id]
                if not tile.get("removed", False):
                    E_after_local += energy_model.compute_local_energy(tile_id, tiling_test)
            
            ΔE_local = E_after_local - E_before_local
            error = abs(ΔE_local - ΔE_global)
            
            radius_stats[radius].append(error)
            
            print(f"  Radius {radius}: ΔE_local = {ΔE_local:.6f}, error = {error:.6f}")
            
            if error < 1e-6:
                print(f"    ✅ Radius {radius} sufficient!")
                break
    
    # Print statistics
    print("\n" + "=" * 60)
    print("📊 NEIGHBORHOOD RADIUS STATISTICS:")
    print("=" * 60)
    print("Radius | Avg Error | Max Error | % Perfect (error < 1e-6)")
    print("-" * 60)
    
    for radius in sorted(radius_stats.keys()):
        errors = radius_stats[radius]
        if errors:
            avg_error = np.mean(errors)
            max_error = np.max(errors)
            perfect = sum(1 for e in errors if e < 1e-6) / len(errors) * 100
            print(f"   {radius}    | {avg_error:.6f}  | {max_error:.6f}  | {perfect:.1f}%")
    
    # Determine optimal radius
    print("\n🎯 RECOMMENDATION:")
    optimal_radius = None
    for radius in sorted(radius_stats.keys()):
        errors = radius_stats[radius]
        if errors:
            # Check if 95% of tests have error < 1e-5 and max < 1e-4
            reliable = (sum(1 for e in errors if e < 1e-5) / len(errors) >= 0.95 and 
                       max(errors) < 1e-4)
            if reliable:
                optimal_radius = radius
                print(f"  Use radius = {radius} (95% < 1e-5, max = {max(errors):.6f})")
                break
    
    if optimal_radius is None:
        print("  ⚠️  No radius reliably gives < 1e-5 error")
        print("  Using radius = 4 for safety")
        optimal_radius = 4
    
    return optimal_radius

if __name__ == "__main__":
    optimal_radius = test_neighborhood_radius(15)
    print(f"\n✅ Optimal neighborhood radius: {optimal_radius}")
    
    # Save result to config
    import toml
    config_path = "configs/phase1_baseline.toml"
    try:
        with open(config_path, 'r') as f:
            config = toml.load(f)
        
        if 'mc' not in config:
            config['mc'] = {}
        config['mc']['neighborhood_radius'] = optimal_radius
        
        with open(config_path, 'w') as f:
            toml.dump(config, f)
        
        print(f"📝 Updated {config_path} with neighborhood_radius = {optimal_radius}")
    except Exception as e:
        print(f"⚠️  Could not update config: {e}")