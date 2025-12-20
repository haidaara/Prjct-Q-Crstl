#!/usr/bin/env python3
"""
Verify if energy recomputation overwrites manual vertex_class
"""

import json
import random

def verify_label_persistence():
    print("🔍 VERIFYING LABEL PERSISTENCE")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Randomly select 10 tiles
    non_removed = [t for t in tiling['tiles'] if not t.get('removed', False)]
    test_tiles = random.sample(non_removed, 10)
    
    print("Setting manual HIGH_ENERGY labels...")
    for tile in test_tiles:
        original_class = tile.get('vertex_class', 'UNKNOWN')
        tile['vertex_class'] = 'HIGH_ENERGY'
        tile['local_energy'] = 2.0
        print(f"  Tile {tile['id']}: {original_class} → HIGH_ENERGY")
    
    # Now run energy recomputation
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
    
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    
    print("\nRecomputing total energy...")
    total_energy = energy_model.compute_total_energy(tiling)
    
    print("\nChecking labels after recomputation:")
    changed = 0
    for tile in test_tiles:
        tile_id = tile['id']
        current_class = tiling['tiles'][tile_id]['vertex_class']
        if current_class != 'HIGH_ENERGY':
            changed += 1
            print(f"  Tile {tile_id}: changed from HIGH_ENERGY to {current_class}")
        else:
            print(f"  Tile {tile_id}: still HIGH_ENERGY")
    
    print(f"\n📊 Result: {changed}/{len(test_tiles)} labels changed during recomputation")
    
    if changed == len(test_tiles):
        print("🚨 ALL labels overwritten! Manual defects not persistent.")
        print("   This explains why manual defects appeared to heal instantly.")
        return False
    elif changed > 0:
        print("⚠️  Some labels changed. Manual defects partially persistent.")
        return False
    else:
        print("✅ All labels persisted. Manual defects are stable.")
        return True

if __name__ == "__main__":
    success = verify_label_persistence()