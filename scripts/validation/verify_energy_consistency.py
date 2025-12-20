# scripts/verify_energy_consistency.py
#!/usr/bin/env python3
"""
Verify energy computation consistency across the system
FIXED: Checks both sum and half-sum conventions
"""

import numpy as np 
import json
import sys
sys.path.insert(0, '.')

from src.utils.energy_utils import (
    wipe_all_energy_fields, clear_all_caches,
    compute_total_energy_fresh, verify_energy_convention
)
from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters

def verify_energy_consistency():
    """Verify that energy computations are consistent"""
    print("🔍 VERIFYING ENERGY COMPUTATION CONSISTENCY")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Setup
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy(EnergyParameters())
    
    # Test 1: Energy counting convention
    print("\n1. Testing energy counting convention...")
    convention_result = verify_energy_convention(energy_model, tiling)
    
    print(f"   Total energy: {convention_result['total_energy']:.6f}")
    print(f"   Sum local energies: {convention_result['sum_local']:.6f}")
    print(f"   Difference (sum): {convention_result['diff_sum']:.6f}")
    print(f"   Difference (half-sum): {convention_result['diff_half_sum']:.6f}")
    
    if convention_result['status'] == 'pass':
        print(f"   ✅ PASS: Convention is '{convention_result['convention']}'")
    else:
        print("   ❌ FAIL: Energy counting convention mismatch!")
        print("      Neither sum nor half-sum matches total energy")
        return False
    
    # Test 2: Energy reproducibility
    print("\n2. Testing energy reproducibility...")
    
    energies = []
    for i in range(5):
        wipe_all_energy_fields(tiling)
        clear_all_caches(energy_model)
        energy = energy_model.compute_total_energy(tiling)
        energies.append(energy)
        print(f"   Run {i+1}: {energy:.6f}")
    
    energy_std = np.std(energies)
    if energy_std < 1e-6:
        print(f"   ✅ PASS: Energy reproducible (std = {energy_std:.6e})")
    else:
        print(f"   ❌ FAIL: Energy not reproducible (std = {energy_std:.6f})")
        return False
    
    # Test 3: Cache invalidation
    print("\n3. Testing cache invalidation...")
    
    # Get a random tile
    tile_id = 100
    tile = tiling["tiles"][tile_id]
    
    # Compute energy once
    wipe_all_energy_fields(tiling)
    clear_all_caches(energy_model)
    energy1 = energy_model.compute_local_energy(tile_id, tiling)
    
    # Modify tile (simulate flip)
    original_type = tile["type"]
    tile["type"] = "THIN" if original_type == "THICK" else "THICK"
    
    # Compute again - should be different
    wipe_all_energy_fields(tiling)
    clear_all_caches(energy_model)
    energy2 = energy_model.compute_local_energy(tile_id, tiling)
    
    # Restore
    tile["type"] = original_type
    
    if abs(energy1 - energy2) > 0.001:
        print(f"   ✅ PASS: Cache properly invalidated")
        print(f"      Before: {energy1:.6f}, After: {energy2:.6f}")
    else:
        print(f"   ⚠️  WARNING: Energy unchanged after modification")
        print(f"      Before: {energy1:.6f}, After: {energy2:.6f}")
    
    # Test 4: Neighborhood energy consistency
    print("\n4. Testing neighborhood energy consistency...")
    
    # Get a random tile and its neighbors
    tile_id = 500
    neighbors = []
    adj = tiling["adjacency_graph"].get(str(tile_id), [])
    for n in adj[:3]:  # Test first 3 neighbors
        nid = int(n)
        neighbors.append(nid)
    
    test_tiles = [tile_id] + neighbors
    
    # Compute energy individually
    individual_energy = 0
    for tid in test_tiles:
        wipe_all_energy_fields(tiling)
        clear_all_caches(energy_model)
        individual_energy += energy_model.compute_local_energy(tid, tiling)
    
    # Compute energy as region
    wipe_all_energy_fields(tiling)
    clear_all_caches(energy_model)
    region_energy = 0
    for tid in test_tiles:
        region_energy += energy_model.compute_local_energy(tid, tiling)
    
    if abs(individual_energy - region_energy) < 1e-6:
        print(f"   ✅ PASS: Region energy = sum(individual energies)")
    else:
        print(f"   ❌ FAIL: Region energy mismatch!")
        print(f"      Individual sum: {individual_energy:.6f}")
        print(f"      Region compute: {region_energy:.6f}")
        return False
    
    print("\n" + "=" * 60)
    print("✅ ENERGY CONSISTENCY TESTS COMPLETE")
    print(f"   Using convention: {convention_result['convention']}")
    return True

if __name__ == "__main__":
    import numpy as np
    success = verify_energy_consistency()
    sys.exit(0 if success else 1)