#!/usr/bin/env python3
"""
Diagnostic 2: Fixed version with proper energy consistency
"""

# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import random
import sys
import copy  # <-- ADD THIS


from src.utils.energy_utils import (
    wipe_all_energy_fields, clear_all_caches,
    get_k_ring_neighborhood
)
from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine

def initialize_seed_region(tiling_data, seed_center=None, seed_radius=10.0):
    """Initialize a seed region"""
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

def analyze_proposed_ΔE_distribution_fixed(sample_size=200, neighborhood_radius=3):
    """Analyze ΔE with proper energy consistency"""
    print("\n🎯 DIAGNOSTIC 2 (FIXED): ΔE DISTRIBUTION WITH ENERGY CONSISTENCY")
    print("=" * 60)
    
    # Load tiling ONCE
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        base_tiling = json.load(f)
    
    # Initialize seed region in base tiling
    initialize_seed_region(base_tiling)
    
    # Setup
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy(EnergyParameters())
    flip_engine = FlipEngine(classifier, energy_model, verbose=False)  # <-- ADD verbose=False
    
    # Define active region in base tiling
    active_tile_ids = set()
    for tile in base_tiling['tiles']:
        if tile.get('removed', False):
            continue
        if tile.get('growth_status') == 'seed':
            active_tile_ids.add(tile['id'])
    
    # Add 1-ring neighbors
    adjacency = base_tiling['adjacency_graph']
    for tile_id in list(active_tile_ids):
        neighbors = adjacency.get(str(tile_id), [])
        for nid in neighbors:
            nid_int = int(nid)
            active_tile_ids.add(nid_int)
    
    # Get all flips, filter to active region
    all_hexagons = flip_engine.find_flippable_hexagons(base_tiling)
    active_hexagons = [h for h in all_hexagons if all(tid in active_tile_ids for tid in h)]
    
    # Sample
    if len(active_hexagons) < sample_size:
        sample_hexagons = active_hexagons
    else:
        sample_hexagons = random.sample(active_hexagons, sample_size)
    
    ΔE_values = []
    proposals_by_sign = {'downhill': 0, 'uphill': 0, 'neutral': 0}
    defect_info = {'near_defect': [], 'perfect': []}
    
    print(f"Analyzing {len(sample_hexagons)} flips with radius={neighborhood_radius}...")
    
    for i, hexagon in enumerate(sample_hexagons):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(sample_hexagons)}")
        
        # COPY from memory (FAST!)
        tiling_copy = copy.deepcopy(base_tiling)
        
        # Get neighborhood
        neighborhood = get_k_ring_neighborhood(hexagon, tiling_copy, k=neighborhood_radius)
        
        # OPTIMIZED: Compute all energies once for defect check
        wipe_all_energy_fields(tiling_copy)
        clear_all_caches(energy_model)
        
        energies_before = {}
        for tile_id in neighborhood:
            tile = tiling_copy["tiles"][tile_id]
            if not tile.get("removed", False):
                energies_before[tile_id] = energy_model.compute_local_energy(tile_id, tiling_copy)
        
        # Check for defects using energy threshold
        has_defect = any(energy > 1.5 for energy in energies_before.values())
        energy_before = sum(energies_before.values())
        
        # Apply flip
        undo_info = flip_engine.capture_state(hexagon, tiling_copy)
        success = flip_engine.apply_flip(hexagon, tiling_copy)
        
        if not success:
            flip_engine.restore_state(undo_info, tiling_copy)
            continue
        
        # Compute energy AFTER - wipe again
        wipe_all_energy_fields(tiling_copy)
        clear_all_caches(energy_model)
        
        energy_after = 0
        for tile_id in neighborhood:
            tile = tiling_copy["tiles"][tile_id]
            if not tile.get("removed", False):
                energy_after += energy_model.compute_local_energy(tile_id, tiling_copy)
        
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
            defect_info['near_defect'].append(ΔE)
        else:
            defect_info['perfect'].append(ΔE)
        
        # Restore
        flip_engine.restore_state(undo_info, tiling_copy)
    
    # Report
    if not ΔE_values:
        print("❌ No successful flips to analyze")
        return None
    
    ΔE_arr = np.array(ΔE_values)
    
    print(f"\n📊 ΔE STATISTICS (n={len(ΔE_arr)}, radius={neighborhood_radius}):")
    print(f"  Mean: {np.mean(ΔE_arr):+.6f}")
    print(f"  Std:  {np.std(ΔE_arr):.6f}")
    print(f"  Min:  {np.min(ΔE_arr):+.6f}")
    print(f"  Max:  {np.max(ΔE_arr):+.6f}")
    
    print(f"\n📊 PROPOSAL DISTRIBUTION:")
    total = len(ΔE_arr)
    for key, count in proposals_by_sign.items():
        print(f"  {key}: {count}/{total} ({count/max(1, total):.1%})")
    
    # Defect analysis
    if defect_info['near_defect'] and defect_info['perfect']:
        print(f"\n🔍 NEAR DEFECTS vs PERFECT REGIONS:")
        near_defect_arr = np.array(defect_info['near_defect'])
        perfect_arr = np.array(defect_info['perfect'])
        
        print(f"  Near defects (n={len(near_defect_arr)}):")
        print(f"    Mean ΔE: {np.mean(near_defect_arr):+.6f}")
        print(f"    % downhill: {np.sum(near_defect_arr < -0.001)/max(1, len(near_defect_arr)):.1%}")
        
        print(f"  Perfect regions (n={len(perfect_arr)}):")
        print(f"    Mean ΔE: {np.mean(perfect_arr):+.6f}")
        print(f"    % downhill: {np.sum(perfect_arr < -0.001)/max(1, len(perfect_arr)):.1%}")
    
    # Plot
    os.makedirs('data/diagnostics', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.hist(ΔE_arr, bins=30, alpha=0.7, edgecolor='black')
    plt.axvline(x=0, color='r', linestyle='--', label='ΔE = 0')
    plt.xlabel('ΔE (energy change)')
    plt.ylabel('Count')
    plt.title(f'ΔE Distribution (radius={neighborhood_radius}, n={len(ΔE_arr)})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('data/diagnostics/delta_E_distribution_fixed.png', dpi=150, bbox_inches='tight')
    print(f"\n📈 Plot saved: data/diagnostics/delta_E_distribution_fixed.png")
    
    return {
        'ΔE_mean': float(np.mean(ΔE_arr)),
        'ΔE_std': float(np.std(ΔE_arr)),
        'uphill_fraction': proposals_by_sign['uphill']/max(1, total),
        'downhill_fraction': proposals_by_sign['downhill']/max(1, total),
        'sample_size': total,
        'neighborhood_radius': neighborhood_radius
    }

if __name__ == "__main__":
    # Test with different radii
    for radius in [2, 3, 4]:
        print(f"\n{'='*60}")
        print(f"Testing with neighborhood radius = {radius}")
        print('='*60)
        results = analyze_proposed_ΔE_distribution_fixed(sample_size=100, neighborhood_radius=radius)