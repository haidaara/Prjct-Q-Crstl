#!/usr/bin/env python3
"""
Diagnostic 2: ΔE distribution for PROPOSED moves (2-ring neighborhood)
FOCUS: Is energy landscape meaningful?
FIXED: Proper energy recomputation without cache contamination
"""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import random

import sys
import os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


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

def analyze_proposed_ΔE_distribution(sample_size=200):
    """Analyze ΔE for proposed moves before acceptance"""
    print("\n🎯 DIAGNOSTIC 2: ΔE DISTRIBUTION FOR PROPOSED MOVES")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize seed region and set active region
    initialize_seed_region(tiling)
    
    # Fresh imports for each analysis
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
    from src.simulation.flip_engine import FlipEngine
    
    # Create fresh instances
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy(EnergyParameters())
    flip_engine = FlipEngine(classifier, energy_model)
    
    # FIX: Save current flippable states and set all to True for global count
    saved_flippable = {}
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        saved_flippable[tile['id']] = tile.get('flippable', True)
        tile['flippable'] = True
    
    # Get ALL possible flippable hexagons globally
    all_hexagons = flip_engine.find_flippable_hexagons(tiling)
    
    # Restore flippable states
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        tile['flippable'] = saved_flippable.get(tile['id'], True)
    
    # Define active region (seed + neighbors)
    active_tile_ids = set()
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        if tile.get('growth_status') == 'seed':
            active_tile_ids.add(tile['id'])
    
    # Add 1-ring neighbors (healing extension)
    adjacency = tiling['adjacency_graph']
    additional_active = set()
    for tile_id in active_tile_ids:
        neighbors = adjacency.get(str(tile_id), [])
        for nid in neighbors:
            nid_int = int(nid)
            if nid_int not in active_tile_ids:
                additional_active.add(nid_int)
    
    active_tile_ids.update(additional_active)
    
    # Filter hexagons that are entirely in the active region
    active_hexagons = [h for h in all_hexagons if all(tid in active_tile_ids for tid in h)]
    
    # Sample flips
    if len(active_hexagons) < sample_size:
        sample_hexagons = active_hexagons
    else:
        sample_hexagons = random.sample(active_hexagons, sample_size)
    
    ΔE_values = []
    proposals_by_sign = {'downhill': 0, 'uphill': 0, 'neutral': 0}
    ΔE_by_defect_status = {'near_defect': [], 'perfect': []}
    
    print(f"Analyzing {len(sample_hexagons)} proposed flips from active region...")
    
    for i, hexagon in enumerate(sample_hexagons):
        # FRESH copy for each test
        with open('data/processed/penrose_tiling_energy_initialized.json') as f:
            tiling_copy = json.load(f)
        
        # Initialize the same active region in the copy
        initialize_seed_region(tiling_copy)
        
        # Set flippable for the same active region
        for tile in tiling_copy['tiles']:
            if tile['id'] in active_tile_ids and not tile.get('removed', False):
                tile['flippable'] = True
            else:
                tile['flippable'] = False
        
        # FRESH instances for this test
        classifier_fresh = CombinatorialVertexClassifier()
        energy_model_fresh = WidomInspiredEnergy(EnergyParameters())
        flip_engine_fresh = FlipEngine(classifier_fresh, energy_model_fresh)
        
        # Get 2-ring neighborhood (SAME AS MC ENGINE USES!)
        neighborhood = flip_engine_fresh._get_two_ring_neighborhood(hexagon, tiling_copy)
        
        # FIX: Wipe ALL stored data in neighborhood, then compute energy and check defects
        # Wipe first
        for tile_id in neighborhood:
            tile = tiling_copy['tiles'][tile_id]
            tile.pop('vertex_class', None)
            tile.pop('local_energy', None)
        
        # Clear caches
        if hasattr(energy_model_fresh, '_vertex_class_cache'):
            energy_model_fresh._vertex_class_cache.clear()
        if hasattr(energy_model_fresh, 'clear_cache'):
            energy_model_fresh.clear_cache()
        
        # Compute energy BEFORE and check for defects in ONE PASS
        energy_before = 0
        has_defect = False
        for tile_id in neighborhood:
            tile = tiling_copy['tiles'][tile_id]
            if not tile.get('removed', False):
                energy = energy_model_fresh.compute_local_energy(tile_id, tiling_copy)
                energy_before += energy
                if tile.get('vertex_class') == 'HIGH_ENERGY':
                    has_defect = True

        # Apply flip
        undo_info = flip_engine_fresh.capture_state(hexagon, tiling_copy)
        success = flip_engine_fresh.apply_flip(hexagon, tiling_copy)
        
        if not success:
            flip_engine_fresh.restore_state(undo_info, tiling_copy)
            continue
        
        # FIX: Wipe AGAIN after flip, then compute energy AFTER
        for tile_id in neighborhood:
            tile = tiling_copy['tiles'][tile_id]
            tile.pop('vertex_class', None)
            tile.pop('local_energy', None)
        
        if hasattr(energy_model_fresh, '_vertex_class_cache'):
            energy_model_fresh._vertex_class_cache.clear()
        if hasattr(energy_model_fresh, 'clear_cache'):
            energy_model_fresh.clear_cache()
        
        # Compute energy AFTER
        energy_after = 0
        for tile_id in neighborhood:
            tile = tiling_copy['tiles'][tile_id]
            if not tile.get('removed', False):
                energy = energy_model_fresh.compute_local_energy(tile_id, tiling_copy)
                energy_after += energy
    
        ΔE = energy_after - energy_before
        ΔE_values.append(ΔE)
        
        # Classify
        if ΔE < -0.001:
            proposals_by_sign['downhill'] += 1
        elif ΔE > 0.001:
            proposals_by_sign['uphill'] += 1
        else:
            proposals_by_sign['neutral'] += 1
        
        # Store by defect status
        if has_defect:
            ΔE_by_defect_status['near_defect'].append(ΔE)
        else:
            ΔE_by_defect_status['perfect'].append(ΔE)
        
        # Restore
        flip_engine_fresh.restore_state(undo_info, tiling_copy)
    
    # Report
    if not ΔE_values:
        print("❌ No successful flips to analyze")
        return None
    
    ΔE_arr = np.array(ΔE_values)
    
    print(f"\n📊 ΔE STATISTICS (n={len(ΔE_arr)}):")
    print(f"  Mean: {np.mean(ΔE_arr):+.4f}")
    print(f"  Std:  {np.std(ΔE_arr):.4f}")
    print(f"  Min:  {np.min(ΔE_arr):+.4f}")
    print(f"  Max:  {np.max(ΔE_arr):+.4f}")
    
    print(f"\n📊 PROPOSAL DISTRIBUTION:")
    total = len(ΔE_arr)
    for key, count in proposals_by_sign.items():
        print(f"  {key}: {count}/{total} ({count/max(1, total):.1%})")
    
    print(f"\n🎯 CRITICAL METRICS:")
    print(f"  % uphill proposals: {proposals_by_sign['uphill']/max(1, total):.1%}")
    print(f"  |ΔE| mean: {np.mean(np.abs(ΔE_arr)):.4f}")
    
    # Check for flat landscape
    if np.std(ΔE_arr) < 0.05:
        print("\n⚠️ WARNING: Very narrow ΔE distribution (std < 0.05)")
        print("Energy landscape may be too flat for meaningful MC")
    
    # Compare near defects vs perfect
    if ΔE_by_defect_status['near_defect'] and ΔE_by_defect_status['perfect']:
        print(f"\n🔍 NEAR DEFECTS vs PERFECT REGIONS:")
        near_defect_arr = np.array(ΔE_by_defect_status['near_defect'])
        perfect_arr = np.array(ΔE_by_defect_status['perfect'])
        
        print(f"  Near defects (n={len(near_defect_arr)}):")
        print(f"    Mean ΔE: {np.mean(near_defect_arr):+.4f}")
        print(f"    % downhill: {np.sum(near_defect_arr < -0.001)/max(1, len(near_defect_arr)):.1%}")
        
        print(f"  Perfect regions (n={len(perfect_arr)}):")
        print(f"    Mean ΔE: {np.mean(perfect_arr):+.4f}")
        print(f"    % downhill: {np.sum(perfect_arr < -0.001)/max(1, len(perfect_arr)):.1%}")
        
        # Key healing metric
        downhill_near = np.sum(near_defect_arr < -0.001)/max(1, len(near_defect_arr))
        downhill_perfect = np.sum(perfect_arr < -0.001)/max(1, len(perfect_arr))
        
        if downhill_near > downhill_perfect:
            print(f"\n✅ HEALING OPPORTUNITY: More downhill moves near defects!")
            print(f"   Ratio: {downhill_near/downhill_perfect:.2f}x more downhill near defects")
        else:
            print(f"\n⚠️  No healing advantage near defects")
    
    # Plot histogram
    os.makedirs('data/diagnostics', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.hist(ΔE_arr, bins=30, alpha=0.7, edgecolor='black')
    plt.axvline(x=0, color='r', linestyle='--', label='ΔE = 0')
    plt.xlabel('ΔE (energy change)')
    plt.ylabel('Count')
    plt.title(f'ΔE Distribution for Proposed Moves (n={len(ΔE_arr)})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('data/diagnostics/delta_E_distribution_proposed.png', dpi=150, bbox_inches='tight')
    print(f"\n📈 Plot saved: data/diagnostics/delta_E_distribution_proposed.png")
    
    return {
        'ΔE_mean': float(np.mean(ΔE_arr)),
        'ΔE_std': float(np.std(ΔE_arr)),
        'uphill_fraction': proposals_by_sign['uphill']/max(1, total),
        'downhill_fraction': proposals_by_sign['downhill']/max(1, total),
        'sample_size': total
    }

if __name__ == "__main__":
    results = analyze_proposed_ΔE_distribution(sample_size=200)