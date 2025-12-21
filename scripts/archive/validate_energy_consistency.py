# scripts/validate_energy_consistency.py
#!/usr/bin/env python3
"""
Validate energy bookkeeping consistency
"""

import json
from pathlib import Path
import sys

def validate_energy_bookkeeping() -> dict:
    """Validate energy computation consistency"""
    print("🔍 Validating Energy Bookkeeping")
    print("=" * 40)

    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    
    # Load data
    data_path = Path("data/processed/penrose_tiling_energy_initialized.json")
    with open(data_path, 'r') as f:
        tiling_data = json.load(f)
    
    # Import
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    
    results = {
        "initial_consistency": None,
        "post_flip_consistency": None,
        "mc_tracking_consistency": None,
        "errors": []
    }
    
    # Test 1: Initial energy consistency
    print("1. Checking initial energy consistency...")
    energy_model = WidomInspiredEnergy()
    
    # Tracked method
    energy_model.clear_cache()
    tracked = energy_model.compute_total_energy(tiling_data)
    
    # Manual sum
    manual_sum = sum(
        tile.get("local_energy", 0) 
        for tile in tiling_data["tiles"] 
        if not tile.get("removed", False)
    )
    
    diff1 = abs(tracked - manual_sum)
    results["initial_consistency"] = {
        "tracked": tracked,
        "manual_sum": manual_sum,
        "difference": diff1,
        "ok": diff1 < 0.001
    }
    
    print(f"   Tracked: {tracked:.6f}")
    print(f"   Manual sum: {manual_sum:.6f}")
    print(f"   Difference: {diff1:.6f} ({'✅ OK' if diff1 < 0.001 else '❌ FAIL'})")
    
    # Test 2: Single flip consistency
    print("\n2. Testing single flip energy tracking...")
    classifier = CombinatorialVertexClassifier()
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find clusters
    clusters = flip_engine.find_flippable_hexagons(tiling_data)[:3]
    
    flip_results = []
    for i, cluster in enumerate(clusters):
        print(f"   Cluster {i+1}: {cluster}")
        
        # Copy for testing
        import copy
        test_data = copy.deepcopy(tiling_data)
        
        # Get affected region
        affected = flip_engine._get_two_ring_neighborhood(cluster, test_data)
        
        # Energy before (stored)
        energy_before_stored = sum(
            test_data["tiles"][tid].get("local_energy", 0) 
            for tid in affected
        )
        
        # Energy before (recomputed)
        energy_model.clear_cache()
        energy_before_recomputed = 0
        for tid in affected:
            tile = test_data["tiles"][tid]
            if not tile.get("removed", False):
                energy_before_recomputed += energy_model.compute_local_energy(tid, test_data)
        
        # Apply flip
        success = flip_engine.apply_flip(cluster, test_data)
        if not success:
            print(f"     ❌ Flip failed")
            continue
        
        # Energy after (stored)
        energy_after_stored = sum(
            test_data["tiles"][tid].get("local_energy", 0) 
            for tid in affected
        )
        
        # Energy after (recomputed)
        energy_model.clear_cache()
        energy_after_recomputed = 0
        for tid in affected:
            tile = test_data["tiles"][tid]
            if not tile.get("removed", False):
                energy_after_recomputed += energy_model.compute_local_energy(tid, test_data)
        
        # Check consistency
        before_diff = abs(energy_before_stored - energy_before_recomputed)
        after_diff = abs(energy_after_stored - energy_after_recomputed)
        delta_stored = energy_after_stored - energy_before_stored
        delta_recomputed = energy_after_recomputed - energy_before_recomputed
        
        flip_results.append({
            "cluster": cluster,
            "energy_before_stored": energy_before_stored,
            "energy_before_recomputed": energy_before_recomputed,
            "energy_after_stored": energy_after_stored,
            "energy_after_recomputed": energy_after_recomputed,
            "before_diff": before_diff,
            "after_diff": after_diff,
            "delta_stored": delta_stored,
            "delta_recomputed": delta_recomputed,
            "delta_diff": abs(delta_stored - delta_recomputed)
        })
        
        print(f"     Before: {energy_before_stored:.3f} vs {energy_before_recomputed:.3f} (diff: {before_diff:.6f})")
        print(f"     After:  {energy_after_stored:.3f} vs {energy_after_recomputed:.3f} (diff: {after_diff:.6f})")
        print(f"     ΔE:     {delta_stored:.3f} vs {delta_recomputed:.3f}")
    
    results["post_flip_consistency"] = flip_results
    
    # Test 3: MC tracking
    print("\n3. Testing MC energy tracking...")
    mc = MonteCarloEngine(temperature=1.0, energy_model=energy_model, flip_engine=flip_engine)
    
    # Copy again
    import copy
    mc_data = copy.deepcopy(tiling_data)
    
    # Initialize MC
    mc.initialize_energy(mc_data)
    mc_energy = mc.current_energy
    
    # Recompute
    energy_model.clear_cache()
    recomputed = energy_model.compute_total_energy(mc_data)
    
    diff3 = abs(mc_energy - recomputed)
    results["mc_tracking_consistency"] = {
        "mc_tracked": mc_energy,
        "recomputed": recomputed,
        "difference": diff3,
        "ok": diff3 < 0.001
    }
    
    print(f"   MC tracked: {mc_energy:.6f}")
    print(f"   Recomputed: {recomputed:.6f}")
    print(f"   Difference: {diff3:.6f} ({'✅ OK' if diff3 < 0.001 else '❌ FAIL'})")
    
    # Summary
    print("\n" + "=" * 40)
    print("📋 VALIDATION SUMMARY:")
    
    all_ok = True
    for flip in flip_results:
        if flip["before_diff"] > 0.001 or flip["after_diff"] > 0.001:
            all_ok = False
            results["errors"].append(f"Inconsistent flip on cluster {flip['cluster']}")
    
    if diff1 > 0.001:
        all_ok = False
        results["errors"].append("Initial energy inconsistency")
    
    if diff3 > 0.001:
        all_ok = False
        results["errors"].append("MC tracking inconsistency")
    
    if all_ok:
        print("✅ All energy bookkeeping checks PASSED")
        results["overall_status"] = "PASS"
    else:
        print("❌ Energy bookkeeping issues detected")
        for error in results["errors"]:
            print(f"   - {error}")
        results["overall_status"] = "FAIL"
    
    # Save results
    output_path = Path("data/experiments/energy_validation_report.json")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\n✅ Full report saved to: {output_path}")
    
    return results

if __name__ == "__main__":
    results = validate_energy_bookkeeping()
    sys.exit(0 if results["overall_status"] == "PASS" else 1)