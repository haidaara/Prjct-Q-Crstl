# scripts/debug_energy_consistency.py
#!/usr/bin/env python3
"""
Debug script to run MC with full energy consistency validation
"""

import json
import sys
sys.path.insert(0, '.')

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine
from src.simulation.mc_engine import MonteCarloEngine

def debug_energy_consistency():
    """Run MC with full verification to validate energy consistency"""
    print("🔍 DEBUG: FULL ENERGY CONSISTENCY VALIDATION")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Setup
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy(EnergyParameters())
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Create MC engine with aggressive verification
    mc_config = {
        'temperature': 0.3,
        'base_steps': 200,
        'neighborhood_radius': 3,  # Will be updated after radius test
        'verify_energy': True,
        'verify_frequency': 1.0,  # Check EVERY step
    }
    
    mc_engine = MonteCarloEngine(
        temperature=mc_config['temperature'],
        energy_model=energy_model,
        flip_engine=flip_engine,
        config=mc_config
    )
    
    # Initialize seed region
    window_size = tiling.get('window_size', [60.0, 60.0])
    seed_center = [window_size[0]/2, window_size[1]/2]
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        dx = tile['center'][0] - seed_center[0]
        dy = tile['center'][1] - seed_center[1]
        if (dx*dx + dy*dy) <= 100.0:  # radius 10
            tile['growth_status'] = 'seed'
            tile['flippable'] = True
        else:
            tile['growth_status'] = 'ungrown'
            tile['flippable'] = False
    
    # Set active region
    active_tile_ids = set()
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        if tile.get('growth_status') == 'seed':
            active_tile_ids.add(tile['id'])
    
    # Add 1-ring neighbors
    adjacency = tiling['adjacency_graph']
    for tile_id in list(active_tile_ids):
        neighbors = adjacency.get(str(tile_id), [])
        for nid in neighbors:
            nid_int = int(nid)
            active_tile_ids.add(nid_int)
    
    # Set flippable for active region
    for tile in tiling['tiles']:
        if tile['id'] in active_tile_ids and not tile.get('removed', False):
            tile['flippable'] = True
        else:
            tile['flippable'] = False
    
    # Initialize MC energy
    mc_engine.initialize_energy(tiling)
    initial_energy = mc_engine.current_energy
    
    print(f"Initial energy: {initial_energy:.6f}")
    print(f"Active region: {len(active_tile_ids)} tiles")
    
    # Run debug validation
    stats = mc_engine.run_debug_validation(tiling, steps=200)
    
    print(f"\n📊 Final stats:")
    print(f"  Energy change: {mc_engine.current_energy - initial_energy:.6f}")
    print(f"  Acceptance rate: {stats['acceptance_rate']:.1%}")
    print(f"  ΔE mean: {stats['delta_mean']:.6f}")
    print(f"  ΔE std: {stats['delta_std']:.6f}")
    print(f"  % uphill moves: {stats['positive_ratio']:.1%}")
    
    # Check if drift is acceptable
    if stats['max_drift'] > 0.001:
        print("\n❌ FAIL: Energy drift too high!")
        return False
    else:
        print("\n✅ SUCCESS: Energy consistency validated!")
        return True

if __name__ == "__main__":
    import numpy as np
    success = debug_energy_consistency()
    sys.exit(0 if success else 1)