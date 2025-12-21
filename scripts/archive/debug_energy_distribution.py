#!/usr/bin/env python3
"""
Check energy differences for proposed flips
"""

# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------

import json
import random
import numpy as np
import sys

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine

def check_energy_distribution():
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize components
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find flippable hexagons
    hexagons = flip_engine.find_flippable_hexagons(tiling)
    
    if not hexagons:
        print("No flippable hexagons")
        return
    
    print(f"Found {len(hexagons)} flippable hexagons")
    
    # Sample some hexagons and compute ΔE
    delta_energies = []
    
    for i, hexagon in enumerate(random.sample(hexagons, min(20, len(hexagons)))):
        # Compute energy before flip
        energy_before = 0
        for tile_id in hexagon:
            tile = tiling['tiles'][tile_id]
            energy_before += tile['local_energy']
        
        # Store original state
        original_states = {}
        for tile_id in hexagon:
            tile = tiling['tiles'][tile_id]
            original_states[tile_id] = {
                'vertices': [v[:] for v in tile['vertices']],
                'vertex_class': tile['vertex_class'],
                'energy': tile['local_energy']
            }
        
        # Apply flip
        success = flip_engine.apply_flip(hexagon, tiling)
        
        if not success:
            continue
        
        # Compute energy after flip
        energy_after = 0
        for tile_id in hexagon:
            tile = tiling['tiles'][tile_id]
            energy_after += tile['local_energy']
        
        delta = energy_after - energy_before
        delta_energies.append(delta)
        
        print(f"Hexagon {hexagon}: ΔE = {delta:.4f}")
        
        # Restore original state
        for tile_id, state in original_states.items():
            tile = tiling['tiles'][tile_id]
            tile['vertices'] = [v[:] for v in state['vertices']]
            tile['vertex_class'] = state['vertex_class']
            tile['local_energy'] = state['energy']
    
    if delta_energies:
        print(f"\n📊 ΔE Statistics (n={len(delta_energies)}):")
        print(f"  Mean: {np.mean(delta_energies):.4f}")
        print(f"  Std: {np.std(delta_energies):.4f}")
        print(f"  Min: {np.min(delta_energies):.4f}")
        print(f"  Max: {np.max(delta_energies):.4f}")
        print(f"  % uphill (ΔE>0): {100 * sum(1 for d in delta_energies if d > 0) / len(delta_energies):.1f}%")

if __name__ == "__main__":
    check_energy_distribution()