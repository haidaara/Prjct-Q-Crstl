#!/usr/bin/env python3
"""
Test temperature effect on fixed tiling state
"""

import json
import sys
sys.path.insert(0, '.')

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine
from src.simulation.mc_engine import MonteCarloEngine

def test_temperature_effect():
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize seed region (same as in growth experiments)
    for tile in tiling['tiles']:
        if not tile.get('removed', False):
            tile['growth_status'] = 'ungrown'
            tile['flippable'] = True
    
    # Create seed region
    window_size = tiling.get('window_size', [60.0, 60.0])
    seed_center = [window_size[0] / 2, window_size[1] / 2]
    
    # Simple seed: all tiles within radius 5.0
    seed_tiles = []
    for tile in tiling['tiles']:
        if tile.get('removed', False):
            continue
        dx = tile['center'][0] - seed_center[0]
        dy = tile['center'][1] - seed_center[1]
        if (dx*dx + dy*dy) <= 25.0:  # radius^2
            tile['growth_status'] = 'seed'
            tile['flippable'] = True
            seed_tiles.append(tile['id'])
    
    print(f"Created seed with {len(seed_tiles)} tiles")
    
    # Test different temperatures on same state
    temperatures = [0.1, 0.5, 1.0, 2.0, 5.0]
    
    for T in temperatures:
        print(f"\n🌡️ Testing T={T}")
        
        # Make a fresh copy of tiling
        with open('data/processed/penrose_tiling_energy_initialized.json') as f:
            tiling_copy = json.load(f)
        
        # Apply same seed
        for tile in tiling_copy['tiles']:
            if tile['id'] in seed_tiles:
                tile['growth_status'] = 'seed'
                tile['flippable'] = True
        
        # Initialize components
        classifier = CombinatorialVertexClassifier()
        energy_params = EnergyParameters()
        energy_model = WidomInspiredEnergy(energy_params)
        flip_engine = FlipEngine(classifier, energy_model)
        
        # Create MC engine
        mc_engine = MonteCarloEngine(
            temperature=T,
            energy_model=energy_model,
            flip_engine=flip_engine,
            config={'base_steps': 200, 'burn_in_steps': 0}
        )
        
        # Initialize energy
        mc_engine.initialize_energy(tiling_copy)
        
        # Run MC
        stats = mc_engine.run_sweep(tiling_copy, steps=200)
        
        print(f"  Acceptance: {stats['acceptance_rate']:.1%}")
        print(f"  Uphill fraction: {stats['positive_ratio']:.1%}")
        print(f"  ΔE mean: {stats['delta_mean']:.3f}")
        print(f"  ΔE std: {stats['delta_std']:.3f}")

if __name__ == "__main__":
    test_temperature_effect()