#!/usr/bin/env python3
"""
Debug script to check if flips are working correctly
"""

# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------

import json
import sys

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine

def test_single_flip():
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize components
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find a flippable hexagon
    hexagons = flip_engine.find_flippable_hexagons(tiling)
    
    if not hexagons:
        print("❌ No flippable hexagons found")
        return False
    
    print(f"Found {len(hexagons)} flippable hexagons")
    
    # Pick first hexagon
    hexagon = hexagons[0]
    print(f"Testing hexagon: {hexagon}")
    
    # Get initial state
    initial_vertices = []
    for tile_id in hexagon:
        tile = tiling['tiles'][tile_id]
        initial_vertices.append((tile_id, tile['vertices'][:], tile['vertex_class'], tile['local_energy']))
    
    # Apply flip
    success = flip_engine.apply_flip(hexagon, tiling)
    
    if not success:
        print("❌ Flip failed")
        return False
    
    print("✅ Flip succeeded")
    
    # Check changes
    for tile_id, old_verts, old_class, old_energy in initial_vertices:
        tile = tiling['tiles'][tile_id]
        new_verts = tile['vertices']
        new_class = tile['vertex_class']
        new_energy = tile['local_energy']
        
        print(f"\nTile {tile_id}:")
        print(f"  Geometry changed: {old_verts != new_verts}")
        print(f"  Vertex class: {old_class} → {new_class}")
        print(f"  Energy: {old_energy:.3f} → {new_energy:.3f}")
        print(f"  ΔE: {new_energy - old_energy:.3f}")
    
    return True

if __name__ == "__main__":
    test_single_flip()