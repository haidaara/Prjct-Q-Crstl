#!/usr/bin/env python3
"""
Diagnostic 3: Before/After MC defect tracking in SAME active region
FOCUS: Does MC actually heal?
"""

import json
import numpy as np

import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


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

def create_defective_seed(tiling_data, num_defects=10, seed_radius=10.0):
    """Create seed with controlled defects"""
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
    from src.simulation.flip_engine import FlipEngine
    import random
    
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Reset
    for tile in tiling_data['tiles']:
        if not tile.get('removed', False):
            tile['growth_status'] = 'ungrown'
            tile['flippable'] = False
    
    # Create seed (center region)
    window_size = tiling_data.get('window_size', [60.0, 60.0])
    seed_center = [window_size[0]/2, window_size[1]/2]
    
    seed_tiles = []
    for tile in tiling_data['tiles']:
        if tile.get('removed', False):
            continue
        dx = tile['center'][0] - seed_center[0]
        dy = tile['center'][1] - seed_center[1]
        if (dx*dx + dy*dy) <= seed_radius*seed_radius:
            tile['growth_status'] = 'seed'
            tile['flippable'] = True
            seed_tiles.append(tile['id'])
    
    # Find flips in seed
    hexagons = flip_engine.find_flippable_hexagons(tiling_data)
    seed_hexagons = [h for h in hexagons if all(tid in seed_tiles for tid in h)]
    
    # Create defects by random flips
    defects_created = 0
    attempts = 0
    
    while defects_created < num_defects and attempts < num_defects * 3 and seed_hexagons:
        attempts += 1
        hexagon = random.choice(seed_hexagons)
        
        defects_before = sum(
            1 for tid in hexagon 
            if tiling_data['tiles'][tid].get('vertex_class') == 'HIGH_ENERGY'
        )
        
        undo_info = flip_engine.capture_state(hexagon, tiling_data)
        success = flip_engine.apply_flip(hexagon, tiling_data)
        
        if not success:
            flip_engine.restore_state(undo_info, tiling_data)
            continue
        
        defects_after = sum(
            1 for tid in hexagon 
            if tiling_data['tiles'][tid].get('vertex_class') == 'HIGH_ENERGY'
        )
        
        if defects_after > defects_before:
            defects_created += 1
        else:
            flip_engine.restore_state(undo_info, tiling_data)
    
    print(f"  Created {defects_created} defects in seed")
    return seed_tiles

def test_mc_healing_isolated(T=0.5, mc_steps=100):
    """Test MC healing on a fixed active region (no growth)"""
    print(f"\n🎯 DIAGNOSTIC 3: MC HEALING (T={T}, steps={mc_steps})")
    print("=" * 60)
    
    # Load fresh tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        base_tiling = json.load(f)
    
    # Create fresh instances
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    
    # Create test tiling with defects
    test_tiling = json.loads(json.dumps(base_tiling))  # Deep copy
    seed_tiles = create_defective_seed(test_tiling, num_defects=15)
    
    # Define active region as seed + 1-ring neighbors (healing extension)
    active_tile_ids = set(seed_tiles)
    adjacency = test_tiling['adjacency_graph']
    additional_active = set()
    for tile_id in active_tile_ids:
        neighbors = adjacency.get(str(tile_id), [])
        for nid in neighbors:
            nid_int = int(nid)
            if nid_int not in active_tile_ids:
                additional_active.add(nid_int)
    
    active_tile_ids.update(additional_active)
    
    # Set flippable for the extended active region
    for tile in test_tiling['tiles']:
        if tile['id'] in active_tile_ids and not tile.get('removed', False):
            tile['flippable'] = True
        else:
            tile['flippable'] = False
    
    # Count initial defects in active region
    defects_before = sum(
        1 for tid in active_tile_ids
        if test_tiling['tiles'][tid].get('vertex_class') == 'HIGH_ENERGY'
    )
    
    if defects_before == 0:
        print("❌ No defects created - test invalid")
        return None
    
    print(f"Active region: {len(active_tile_ids)} tiles")
    print(f"Initial defects: {defects_before} ({defects_before/len(active_tile_ids):.1%} density)")
    
    # Setup MC engine (FRESH instances)
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy(EnergyParameters())
    flip_engine = FlipEngine(classifier, energy_model)
    
    mc_engine = MonteCarloEngine(
        temperature=T,
        energy_model=energy_model,
        flip_engine=flip_engine,
        config={'base_steps': mc_steps, 'burn_in_steps': 20}
    )
    
    # Initialize energy
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
        
        # Count defects in active region
        defects = sum(
            1 for tid in active_tile_ids
            if test_tiling['tiles'][tid].get('vertex_class') == 'HIGH_ENERGY'
        )
        
        # Count flippable hexagons in active region
        hexagons = flip_engine.find_flippable_hexagons(test_tiling)
        active_hexagons = [h for h in hexagons if all(tid in active_tile_ids for tid in h)]
        
        metrics['defects'].append(defects)
        metrics['energy'].append(mc_engine.current_energy)
        metrics['acceptance'].append(accepted)
        metrics['flippable'].append(len(active_hexagons))
    
    # Final counts
    defects_after = sum(
        1 for tid in active_tile_ids
        if test_tiling['tiles'][tid].get('vertex_class') == 'HIGH_ENERGY'
    )
    
    # Analyze
    healing = defects_before - defects_after
    healing_efficiency = healing / defects_before if defects_before > 0 else 0
    
    # MC statistics
    accepted_steps = sum(metrics['acceptance'])
    acceptance_rate = accepted_steps / mc_steps
    
    # Check energy consistency: clear cache and recompute total energy
    energy_model.clear_cache()  # Ensure we recompute everything
    energy_recomputed = energy_model.compute_total_energy(test_tiling)
    energy_drift = abs(energy_recomputed - mc_engine.current_energy)
    
    print(f"\n📊 RESULTS:")
    print(f"  Defects: {defects_before} → {defects_after} (Δ={healing:+d})")
    print(f"  Healing efficiency: {healing_efficiency:+.1%}")
    print(f"  Energy change: {mc_engine.current_energy - energy_before:+.2f}")
    print(f"  Acceptance rate: {acceptance_rate:.1%}")
    print(f"  Avg flippable hexagons: {np.mean(metrics['flippable']):.1f}")
    print(f"  Energy consistency drift: {energy_drift:.6f} (should be ~0)")
    
    # Check invariants
    print(f"\n🔍 INVARIANT CHECKS:")
    
    if energy_drift > 0.01:
        print(f"  ❌ Energy inconsistent! Drift = {energy_drift:.4f}")
        print(f"     MC energy: {mc_engine.current_energy:.4f}")
        print(f"     Recomputed: {energy_recomputed:.4f}")
    else:
        print(f"  ✅ Energy consistent (drift < 0.01)")
    
    # Check if vertex_class is updated for all active tiles
    missing_class = sum(
        1 for tid in active_tile_ids
        if 'vertex_class' not in test_tiling['tiles'][tid]
    )
    if missing_class > 0:
        print(f"  ❌ {missing_class} tiles missing vertex_class")
    else:
        print(f"  ✅ All active tiles have vertex_class")
    
    # Interpretation
    print(f"\n🎯 INTERPRETATION:")
    
    if healing > 0:
        print(f"  ✅ HEALING DETECTED: {healing} defects removed")
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
        print(f"     MC is making things worse!")
    
    # Check if MC had moves
    if np.mean(metrics['flippable']) < 1:
        print(f"  ❌ MC STARVED: Avg flippable hexagons = {np.mean(metrics['flippable']):.1f}")
        print(f"     MC couldn't propose moves!")
    
    return {
        'temperature': T,
        'defects_before': defects_before,
        'defects_after': defects_after,
        'healing': healing,
        'healing_efficiency': healing_efficiency,
        'energy_change': mc_engine.current_energy - energy_before,
        'acceptance_rate': acceptance_rate,
        'avg_flippable': np.mean(metrics['flippable']),
        'energy_drift': energy_drift
    }

if __name__ == "__main__":
    # Test multiple temperatures
    temperatures = [0.1, 0.3, 1.0, 2.0, 5.0]
    all_results = []
    
    for T in temperatures:
        result = test_mc_healing_isolated(T=T, mc_steps=100)
        if result:
            all_results.append(result)
    
    # Summary
    if all_results:
        print("\n" + "=" * 80)
        print("📈 TEMPERATURE DEPENDENCE SUMMARY:")
        print("=" * 80)
        
        for r in all_results:
            heal = "✅" if r['healing'] > 0 else "❌" if r['healing'] < 0 else "⚖️"
            print(f"T={r['temperature']:4.1f}: {heal} Healing={r['healing']:+3d} "
                  f"Eff={r['healing_efficiency']:6.1%} "
                  f"Accept={r['acceptance_rate']:5.1%} "
                  f"Flippable={r['avg_flippable']:5.1f}")
        
        # Find best temperature
        best = max(all_results, key=lambda x: x['healing_efficiency'])
        print(f"\n🎯 OPTIMAL: T={best['temperature']} "
              f"(efficiency={best['healing_efficiency']:.1%})")