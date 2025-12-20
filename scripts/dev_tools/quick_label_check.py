#!/usr/bin/env python3
"""
Quick check: Does energy recomputation overwrite manual labels?
"""

import json
import sys
sys.path.insert(0, '.')

def check_label_persistence():
    """Quick test to see if manual labels are overwritten"""
    print("🔍 QUICK LABEL PERSISTENCE CHECK")
    print("=" * 40)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Pick a random tile
    import random
    non_removed = [t for t in tiling['tiles'] if not t.get('removed', False)]
    tile = random.choice(non_removed)
    tile_id = tile['id']
    
    print(f"Testing tile {tile_id}:")
    print(f"  Initial vertex_class: {tile.get('vertex_class', 'NOT SET')}")
    
    # Set manually
    tile['vertex_class'] = 'HIGH_ENERGY'
    tile['local_energy'] = 2.0
    print(f"  After manual set: vertex_class = {tile['vertex_class']}")
    
    # Recompute energy
    from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
    energy_model = WidomInspiredEnergy(EnergyParameters())
    
    # Method 1: compute_local_energy
    energy = energy_model.compute_local_energy(tile_id, tiling)
    print(f"  After compute_local_energy:")
    print(f"    vertex_class = {tile.get('vertex_class', 'NOT SET')}")
    print(f"    local_energy = {tile.get('local_energy', 'NOT SET'):.2f}")
    
    # Method 2: clear and recompute
    tile['vertex_class'] = 'HIGH_ENERGY'  # Reset
    energy_model.clear_cache() if hasattr(energy_model, 'clear_cache') else None
    energy = energy_model.compute_local_energy(tile_id, tiling)
    print(f"  After clear_cache + compute_local_energy:")
    print(f"    vertex_class = {tile.get('vertex_class', 'NOT SET')}")
    
    # Check if persists
    if tile.get('vertex_class') == 'HIGH_ENERGY':
        print("\n✅ Label persists after recomputation")
        return True
    else:
        print(f"\n🚨 Label CHANGED to: {tile.get('vertex_class')}")
        print("   Manual defects will be overwritten!")
        return False

if __name__ == "__main__":
    success = check_label_persistence()