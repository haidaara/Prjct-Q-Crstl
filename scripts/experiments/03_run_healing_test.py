# scripts/test_manual_defects.py
#!/usr/bin/env python3
"""
Test MC healing with manual defects (REAL geometric defects)
FIXED: Creates real defects by applying uphill flips, tracks energy properly
"""

import json
import random
import copy
import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from src.utils.energy_utils import compute_total_energy_fresh, wipe_all_energy_fields, clear_all_caches


def initialize_seed_region(tiling_data, seed_center=None, seed_radius=10.0):
    """Initialize a seed region (same as in growth_engine)"""
    if seed_center is None:
        window_size = tiling_data.get('window_size', [60.0, 60.0])
        seed_center = [window_size[0]/2, window_size[1]/2]
    
    for tile in tiling_data['tiles']:
        if tile.get('removed', False):
            continue
        dx = tile['center'][0] - seed_center[0]
        dy = tile['center'][1] - seed_center[1]
        if (dx*dx + dy*dy) <= seed_radius*seed_radius:
            tile['growth_status'] = 'seed'
            tile['flippable'] = True
        else:
            tile['growth_status'] = 'ungrown'
            tile['flippable'] = False

def create_real_geometric_defects(tiling_data, energy_model, flip_engine, num_defects=10):
    """
    Create REAL defects by applying flips that increase energy
    Returns: (active_tile_ids, defect_hexagons_applied)
    """
    print(f"  Creating {num_defects} REAL geometric defects...")
    
    # Define active region
    active_tile_ids = set()
    for tile in tiling_data['tiles']:
        if tile.get('removed', False):
            continue
        if tile.get('growth_status') == 'seed':
            active_tile_ids.add(tile['id'])
    
    # Add 1-ring neighbors
    adjacency = tiling_data['adjacency_graph']
    additional_active = set()
    for tile_id in active_tile_ids:
        neighbors = adjacency.get(str(tile_id), [])
        for nid in neighbors:
            nid_int = int(nid)
            if nid_int not in active_tile_ids:
                additional_active.add(nid_int)
    
    active_tile_ids.update(additional_active)

    # SET flippable for active region BEFORE finding hexagons
    for tile in tiling_data['tiles']:
        if tile.get('removed', False):
            continue
        tile['flippable'] = (tile['id'] in active_tile_ids)

    # Now find flippable hexagons
    hexagons = flip_engine.find_flippable_hexagons(tiling_data)
    active_hexagons = [h for h in hexagons if all(tid in active_tile_ids for tid in h)]
    
    # Create defects by applying uphill flips
    defects_created = 0
    defect_hexagons = []
    
    # Shuffle hexagons for random selection
    random.shuffle(active_hexagons)
    
    for hexagon in active_hexagons:
        if defects_created >= num_defects:
            break
        
        # 1. VERIFY VALIDITY: Hexagon might be broken by previous flips
        # We need to construct the edge map temporarily just to check structure
        # A lightweight check: do these 3 tiles still share edges?
        # Better: use the engine's check
        edge_to_tiles_dummy = {} # We can't easily rebuild this every time efficiently
        # Instead, try-catch the flip or just proceed. The Engine's apply_flip checks structure.
        # But we need neighborhood for energy calculation first.
        
        # Use updated k=3 neighborhood
        neighborhood = flip_engine._get_k_ring_neighborhood(hexagon, tiling_data, k=3)
        
        # FIX: Wipe stored data and clear cache BEFORE computing energy
        for tile_id in neighborhood:
            tile = tiling_data['tiles'][tile_id]
            tile.pop('vertex_class', None)
            tile.pop('local_energy', None)
        
        if hasattr(energy_model, '_vertex_class_cache'):
            energy_model._vertex_class_cache.clear()
        if hasattr(energy_model, 'clear_cache'):
            energy_model.clear_cache()
        
        # Compute energy BEFORE
        energy_before = 0
        for tile_id in neighborhood:
            tile = tiling_data['tiles'][tile_id]
            if not tile.get('removed', False):
                energy_before += energy_model.compute_local_energy(tile_id, tiling_data)

        # Apply flip (without Metropolis - we force it)
        undo_info = flip_engine.capture_state(list(neighborhood), tiling_data)
        success = flip_engine.apply_flip(hexagon, tiling_data)
        
        if not success:
            flip_engine.restore_state(undo_info, tiling_data)
            # CRITICAL: Also wipe energy fields in affected region to prevent corruption
            for tid in neighborhood:
                tile = tiling_data["tiles"][tid]
                tile.pop("local_energy", None)
                tile.pop("vertex_class", None)
            continue
        
        # FIX: Wipe again after flip, then compute energy AFTER
        for tile_id in neighborhood:
            tile = tiling_data['tiles'][tile_id]
            tile.pop('vertex_class', None)
            tile.pop('local_energy', None)
        
        if hasattr(energy_model, '_vertex_class_cache'):
            energy_model._vertex_class_cache.clear()
        if hasattr(energy_model, 'clear_cache'):
            energy_model.clear_cache()
        
        # Compute energy AFTER
        energy_after = 0
        for tile_id in neighborhood:
            tile = tiling_data['tiles'][tile_id]
            if not tile.get('removed', False):
                energy_after += energy_model.compute_local_energy(tile_id, tiling_data)

        ΔE = energy_after - energy_before
        
        # Keep if it increases energy (creates a defect)
        if ΔE > 0.1:  # Significant energy increase
            defects_created += 1
            defect_hexagons.append(hexagon)
            print(f"    Defect #{defects_created}: ΔE = +{ΔE:.2f} (hexagon {hexagon})")
        else:
            # Reject - doesn't create enough of a defect
            flip_engine.restore_state(undo_info, tiling_data)
            # Safety wipe
            for tid in neighborhood:
                tile = tiling_data["tiles"][tid]
                tile.pop("local_energy", None)
                tile.pop("vertex_class", None)

    print(f"  Created {defects_created} real geometric defects")
    return list(active_tile_ids), defect_hexagons

def count_defects_by_energy(tiling_data, active_tile_ids, energy_model, threshold=1.5):
    """Count defects with GUARANTEED fresh computation"""
    # FORCE fresh computation
    wipe_all_energy_fields(tiling_data)
    clear_all_caches(energy_model)
    
    defects = 0
    total_energy = 0
    defect_energies = []
    
    for tile_id in active_tile_ids:
        tile = tiling_data["tiles"][tile_id]
        if tile.get("removed", False):
            continue
        
        # FRESH computation (no caching)
        energy = energy_model.compute_local_energy(tile_id, tiling_data)
        total_energy += energy
        
        if energy > threshold:
            defects += 1
            defect_energies.append(energy)
    
    avg_defect_energy = np.mean(defect_energies) if defect_energies else 0.0
    return defects, avg_defect_energy


def test_mc_healing_isolated(T=0.5, mc_steps=100, num_defects=15):
    """Test MC healing on REAL geometric defects"""
    print(f"\n🎯 DIAGNOSTIC 3: MC HEALING (T={T}, steps={mc_steps})")
    print("=" * 60)
    
    # Load fresh tiling ONCE
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        base_tiling = json.load(f)
    
    # QUICK CHECK: Make sure tile IDs match list indices
    for i, tile in enumerate(base_tiling['tiles']):
        if tile['id'] != i:
            print(f"🚨 ERROR: Tile {i} has id {tile['id']} - IDs don't match indices!")
            print("This will break everything. Fix your tiling generation.")
            return None
    
    # Create test tiling
    test_tiling = copy.deepcopy(base_tiling)  # Use deepcopy instead of json.loads(json.dumps())
    initialize_seed_region(test_tiling)
    
    # Create fresh instances
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    
    # Setup energy model and flip engine
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model, verbose=False)  # Add verbose=False
    
    # Create REAL geometric defects
    active_tile_ids, defect_hexagons = create_real_geometric_defects(
        test_tiling, energy_model, flip_engine, num_defects=num_defects
    )
    
    if len(defect_hexagons) == 0:
        print("❌ Failed to create real defects - test invalid")
        return None
    
    # Set flippable for active region only
    for tile in test_tiling['tiles']:
        if tile['id'] in active_tile_ids and not tile.get('removed', False):
            tile['flippable'] = True
        else:
            tile['flippable'] = False
    
    # Count initial defects (by energy, not labels)
    defects_before, avg_defect_energy_before = count_defects_by_energy(
        test_tiling, active_tile_ids, energy_model
    )
    
    print(f"Active region: {len(active_tile_ids)} tiles")
    print(f"Initial defects (energy > 1.5): {defects_before}")
    print(f"Average defect energy: {avg_defect_energy_before:.2f}")
    
    if defects_before == 0:
        print("❌ No real defects created - test invalid")
        return None
    
    
    # GLOBAL WIPE: Clear all cached energy fields before MC starts
    wipe_all_energy_fields(test_tiling)
    clear_all_caches(energy_model)
    
    # Setup MC engine - USE RADIUS=3 (validated as optimal)
    mc_config = {
        'temperature': T,
        'base_steps': mc_steps,
        'burn_in_steps': 20,
        'neighborhood_radius': 3,  # <-- CRITICAL: Use validated radius
        'verify_energy': False,    # We'll verify manually
        'verify_frequency': 0.1,
    }
    
    # Setup MC engine with validated radius
    mc_engine = MonteCarloEngine(
        temperature=T,
        energy_model=energy_model,
        flip_engine=flip_engine,
        config=mc_config  # Use the config we defined above
    )
    
    # Initialize energy (should be fresh after wipe)
    mc_engine.initialize_energy(test_tiling)
    energy_before = mc_engine.current_energy
    
    # Track metrics during MC
    metrics = {
        'defects': [],
        'energy': [],
        'acceptance': [],
        'flippable': []
    }
    
    # Run MC steps while tracking
    for step in range(mc_steps):
        accepted, ΔE = mc_engine.run_step(test_tiling)
        
        # Count defects in active region (by energy)
        defects, _ = count_defects_by_energy(test_tiling, active_tile_ids, energy_model)
        
        # Count flippable hexagons in active region
        hexagons = flip_engine.find_flippable_hexagons(test_tiling)
        active_hexagons = [h for h in hexagons if all(tid in active_tile_ids for tid in h)]
        
        metrics['defects'].append(defects)
        metrics['energy'].append(mc_engine.current_energy)
        metrics['acceptance'].append(accepted)
        metrics['flippable'].append(len(active_hexagons))
    
    # Final counts
    defects_after, avg_defect_energy_after = count_defects_by_energy(
        test_tiling, active_tile_ids, energy_model
    )
    
    # Analyze
    healing = defects_before - defects_after
    healing_efficiency = healing / defects_before if defects_before > 0 else 0
    
    # MC statistics
    accepted_steps = sum(metrics['acceptance'])
    acceptance_rate = accepted_steps / mc_steps
    
    # Check energy consistency (FRESH computation)
    energy_recomputed = compute_total_energy_fresh(energy_model, test_tiling)
    energy_drift = abs(energy_recomputed - mc_engine.current_energy)

    print(f"\n📊 RESULTS:")
    print(f"  Defects: {defects_before} → {defects_after} (Δ={healing:+d})")
    print(f"  Healing efficiency: {healing_efficiency:+.1%}")
    print(f"  Avg defect energy: {avg_defect_energy_before:.2f} → {avg_defect_energy_after:.2f}")
    print(f"  Energy change: {mc_engine.current_energy - energy_before:+.2f}")
    print(f"  Acceptance rate: {acceptance_rate:.1%}")
    print(f"  Avg flippable hexagons: {np.mean(metrics['flippable']):.1f}")
    print(f"  Energy consistency drift: {energy_drift:.6f}")
    
    # Check invariants
    print(f"\n🔍 INVARIANT CHECKS:")
    
    if energy_drift > 0.01:
        print(f"  ❌ Energy inconsistent! Drift = {energy_drift:.4f}")
    else:
        print(f"  ✅ Energy consistent (drift < 0.01)")
    
    # Interpretation
    print(f"\n🎯 INTERPRETATION:")
    
    if healing > 0:
        print(f"  ✅ REAL HEALING DETECTED: {healing} defects removed")
        print(f"     Efficiency: {healing_efficiency:.1%}")
        
        if acceptance_rate > 0.1:
            print(f"  ✅ MC is active (acceptance: {acceptance_rate:.1%})")
        else:
            print(f"  ⚠️  MC acceptance very low ({acceptance_rate:.1%})")
    elif healing == 0:
        print(f"  ⚖️  NO NET HEALING: Defect count unchanged")
        print(f"     MC maintains equilibrium")
    else:
        print(f"  ❌ NEGATIVE HEALING: Defects increased by {-healing}")
    
    # Check if MC had moves
    if np.mean(metrics['flippable']) < 1:
        print(f"  ❌ MC STARVED: Avg flippable hexagons = {np.mean(metrics['flippable']):.1f}")
    
    return {
        'temperature': T,
        'defects_before': defects_before,
        'defects_after': defects_after,
        'healing': healing,
        'healing_efficiency': healing_efficiency,
        'energy_change': mc_engine.current_energy - energy_before,
        'acceptance_rate': acceptance_rate,
        'avg_flippable': np.mean(metrics['flippable']),
        'energy_drift': energy_drift,
        'avg_defect_energy_before': avg_defect_energy_before,
        'avg_defect_energy_after': avg_defect_energy_after
    }

if __name__ == "__main__":
    print("🧪 TESTING MC HEALING WITH REAL GEOMETRIC DEFECTS")
    print("=" * 60)
    
    # Test multiple temperatures
    temperatures = [0.1, 0.3, 1.0, 2.0, 5.0]
    all_results = []
    
    for T in temperatures:
        result = test_mc_healing_isolated(T=T, mc_steps=100, num_defects=15)
        if result:
            all_results.append(result)
    
    # Summary
    if all_results:
        print("\n" + "=" * 80)
        print("📈 TEMPERATURE DEPENDENCE SUMMARY:")
        print("=" * 80)
        print("Temp | Defects Before→After | Healing | Efficiency | Accept% | Avg Flippable")
        print("-" * 80)
        
        for r in all_results:
            heal = "✅" if r['healing'] > 0 else "❌" if r['healing'] < 0 else "⚖️"
            print(f"T={r['temperature']:4.1f} | "
                  f"{r['defects_before']:3d}→{r['defects_after']:<3d} | "
                  f"{heal} {r['healing']:+3d} | "
                  f"{r['healing_efficiency']:9.1%} | "
                  f"{r['acceptance_rate']:7.1%} | "
                  f"{r['avg_flippable']:6.1f}")
        
        # Find best temperature
        if any(r['healing'] > 0 for r in all_results):
            best = max(all_results, key=lambda x: x['healing_efficiency'])
            print(f"\n🎯 OPTIMAL: T={best['temperature']} "
                  f"(efficiency={best['healing_efficiency']:.1%})")
        else:
            print("\n❌ NO HEALING at any temperature")