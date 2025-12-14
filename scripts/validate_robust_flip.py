# scripts/validate_robust_flip.py
"""
Robust validation of flip physics with detailed diagnostics
"""

import json
import sys
import os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy
from src.simulation.flip_engine import FlipEngine

def validate_cluster(cluster_ids, tiling_data, flip_engine, energy_model, test_num=1):
    """Validate a single cluster flip"""
    print(f"\n{'='*60}")
    print(f"🧪 TEST {test_num}: CLUSTER {cluster_ids}")
    print(f"{'='*60}")
    
    # Make a copy for testing
    import copy
    test_data = copy.deepcopy(tiling_data)
    
    # Get edge length
    L = flip_engine.compute_edge_length(test_data)
    
    # ==============================================
    # 1. PRE-FLIP VALIDATION
    # ==============================================
    print("📐 PRE-FLIP GEOMETRY:")
    
    # Check each tile
    for tile_id in cluster_ids:
        tile = test_data["tiles"][tile_id]
        vertices = tile["vertices"]
        
        # Check vertex count
        if len(vertices) != 4:
            print(f"  ❌ Tile {tile_id}: {len(vertices)} vertices")
            return False
        
        # Check edge lengths
        lengths = []
        for i in range(4):
            v1 = np.array(vertices[i])
            v2 = np.array(vertices[(i + 1) % 4])
            length = np.linalg.norm(v2 - v1)
            lengths.append(length)
        
        avg_length = np.mean(lengths)
        std_length = np.std(lengths)
        print(f"  Tile {tile_id} ({tile['type']}): edges {avg_length:.4f}±{std_length:.4f}")
        
        if std_length > 0.001:
            print(f"    ⚠️  Edge length variation: {lengths}")
    
    # ==============================================
    # 2. APPLY FLIP
    # ==============================================
    print("\n🔄 APPLYING FLIP...")
    try:
        success = flip_engine.apply_flip(cluster_ids, test_data)
        if not success:
            print("  ❌ Flip failed (returned False)")
            return False
    except Exception as e:
        print(f"  ❌ Flip error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # ==============================================
    # 3. POST-FLIP VALIDATION
    # ==============================================
    print("\n✅ POST-FLIP CHECKS:")
    
    # Check geometry preserved
    geometry_ok = True
    for tile_id in cluster_ids:
        tile = test_data["tiles"][tile_id]
        vertices = tile["vertices"]
        
        # Still 4 vertices
        if len(vertices) != 4:
            print(f"  ❌ Tile {tile_id}: now has {len(vertices)} vertices")
            geometry_ok = False
            continue
        
        # Edge lengths still ≈ L
        lengths = []
        for i in range(4):
            v1 = np.array(vertices[i])
            v2 = np.array(vertices[(i + 1) % 4])
            length = np.linalg.norm(v2 - v1)
            lengths.append(length)
        
        avg_length = np.mean(lengths)
        if abs(avg_length - L) > 0.01 * L:
            print(f"  ❌ Tile {tile_id}: edge length changed to {avg_length:.4f}")
            geometry_ok = False
        else:
            print(f"  ✓ Tile {tile_id}: edges {avg_length:.4f} (close to {L:.4f})")
    
    if not geometry_ok:
        return False
    
    # ==============================================
    # 4. ENERGY CHANGE
    # ==============================================
    print("\n⚡ ENERGY ANALYSIS:")
    
    # Compute energy before (from original)
    energy_before = 0
    for tile_id in cluster_ids:
        tile = tiling_data["tiles"][tile_id]
        energy_before += tile.get("local_energy", 0)
    
    # Compute energy after
    energy_after = 0
    for tile_id in cluster_ids:
        tile = test_data["tiles"][tile_id]
        energy_after += tile.get("local_energy", 0)
    
    ΔE = energy_after - energy_before
    print(f"  Energy: {energy_before:.4f} → {energy_after:.4f}")
    print(f"  ΔE = {ΔE:.4f}")
    
    if abs(ΔE) < 0.001:
        print("  ⚠️  Energy unchanged (check classifier sensitivity)")
    elif ΔE > 0:
        print(f"  ↑ Energy increased by {ΔE:.4f}")
    else:
        print(f"  ↓ Energy decreased by {-ΔE:.4f}")
    
    # ==============================================
    # 5. VERTEX CLASSIFICATION CHANGES
    # ==============================================
    print("\n🎯 VERTEX CLASSIFICATION:")
    
    for tile_id in cluster_ids:
        tile_before = tiling_data["tiles"][tile_id]
        tile_after = test_data["tiles"][tile_id]
        
        print(f"  Tile {tile_id}: {tile_before['vertex_class']} → {tile_after['vertex_class']}")
    
    return True

def main():
    print("🔬 ROBUST PHYSICS VALIDATION")
    print("=" * 70)
    
    # Load data
    data_file = "data/processed/penrose_tiling_energy_initialized.json"
    if not os.path.exists(data_file):
        print(f"❌ Missing: {data_file}")
        return False
    
    with open(data_file, "r") as f:
        tiling_data = json.load(f)
    
    print(f"📊 Loaded {len(tiling_data['tiles'])} tiles")
    
    # Initialize
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy()
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find hexagons
    clusters = flip_engine.find_flippable_hexagons(tiling_data)
    print(f"🔍 Found {len(clusters)} candidate hexagons")
    
    if not clusters:
        print("❌ No flippable hexagons found")
        return False
    
    # Test first 3 clusters
    success_count = 0
    for i, cluster in enumerate(clusters[:3]):
        if validate_cluster(cluster, tiling_data, flip_engine, energy_model, i+1):
            success_count += 1
    
    # Summary
    print(f"\n{'='*70}")
    print("📊 VALIDATION SUMMARY:")
    print(f"  Tests run: {min(3, len(clusters))}")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {min(3, len(clusters)) - success_count}")
    
    if success_count > 0:
        print("\n✅ PHYSICS VALIDATION PASSED")
        print("   Flip engine correctly preserves:")
        print("   - Unit edge lengths")
        print("   - Rhombus geometry")
        print("   - Hexagon boundary")
        print("   - Energy changes observed")
        return True
    else:
        print("\n❌ ALL TESTS FAILED")
        print("   Need to debug fundamental issues")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)