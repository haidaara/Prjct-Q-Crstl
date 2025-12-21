#!/usr/bin/env python3
"""
Diagnostic 1: Count flippable hexagons in active region vs globally
FOCUS: Is MC even active?
FIXED: Global count now correctly counts all flips regardless of flippable flag
"""

# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------

import json
import sys

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

def count_flippable_in_active_region():
    """Count how many flips are actually available in active region"""
    print("🎯 DIAGNOSTIC 1: FLIPPABLE HEXAGONS IN ACTIVE REGION")
    print("=" * 60)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize seed region (so we have an active region)
    initialize_seed_region(tiling)
    
    # Fresh imports
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
        tile['flippable'] = True  # Temporarily set all to True for global count
    
    # Get TRUE global flippable hexagons (all possible flips)
    all_hexagons = flip_engine.find_flippable_hexagons(tiling)
    
    # Restore flippable states
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        tile['flippable'] = saved_flippable.get(tile['id'], True)
    
    # Define active region (same as growth constraints use)
    active_tile_ids = set()
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        
        # Active region = seed
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
    
    # Set flippable for the extended active region (for MC)
    for tile in tiling['tiles']:
        if tile['id'] in active_tile_ids and not tile.get('removed', False):
            tile['flippable'] = True
        elif not tile.get('removed', False):
            tile['flippable'] = False
    
    # Count hexagons in active region (with current flippable settings)
    active_hexagons = []
    for hexagon in all_hexagons:  # Use the global list we computed
        if all(tid in active_tile_ids for tid in hexagon):
            active_hexagons.append(hexagon)
    
    # Report
    print(f"Total flippable hexagons globally: {len(all_hexagons)}")
    print(f"Flippable hexagons in active region: {len(active_hexagons)}")
    print(f"Active region size (tiles): {len(active_tile_ids)}")
    print(f"Ratio: {len(active_hexagons)/max(1, len(all_hexagons)):.1%}")
    
    if len(active_hexagons) == 0:
        print("\n🚨 CRITICAL: NO FLIPPABLE HEXAGONS IN ACTIVE REGION!")
        print("MC cannot propose any moves - healing impossible")
        print("Need to adjust growth constraints or active region definition")
        return False
    elif len(active_hexagons) < 10:
        print("\n⚠️ WARNING: Very few flips in active region")
        print("MC will be starved for moves")
        return False
    else:
        print("\n✅ Active region has sufficient flippable hexagons")
        return True

if __name__ == "__main__":
    success = count_flippable_in_active_region()
    sys.exit(0 if success else 1)