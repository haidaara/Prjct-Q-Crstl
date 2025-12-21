#!/usr/bin/env python3
"""
RELIABLE temperature effect test with proper initialization
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
from src.simulation.mc_engine import MonteCarloEngine

def initialize_tiling_with_seed(tiling_data, seed_radius=5.0):
    """Initialize tiling with seed region - REPRODUCIBLE"""
    # Reset all tiles to ungrown state
    for tile in tiling_data["tiles"]:
        if not tile.get("removed", False):
            tile["growth_status"] = "ungrown"
            tile["flippable"] = True
    
    # Create seed region
    window_size = tiling_data.get("window_size", [60.0, 60.0])
    seed_center = [window_size[0] / 2, window_size[1] / 2]
    
    seed_tiles = []
    for tile in tiling_data["tiles"]:
        if tile.get("removed", False):
            continue
        dx = tile["center"][0] - seed_center[0]
        dy = tile["center"][1] - seed_center[1]
        if (dx*dx + dy*dy) <= seed_radius * seed_radius:
            tile["growth_status"] = "seed"
            tile["flippable"] = True
            seed_tiles.append(tile["id"])
    
    return seed_tiles

def test_temperature_summary():
    """Test temperature effect with PROPER state management"""
    print("🌡️ RELIABLE TEMPERATURE EFFECT TEST")
    print("=" * 60)
    
    # Load base tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        base_tiling = json.load(f)
    
    # Get seed tile IDs (once)
    seed_tiles = initialize_tiling_with_seed(base_tiling.copy(), seed_radius=5.0)
    print(f"Seed region: {len(seed_tiles)} tiles")
    
    # Test temperatures
    temperatures = [0.1, 0.5, 1.0, 2.0, 5.0]
    
    results = []
    for T in temperatures:
        print(f"\nTesting T={T}...")
        
        # FRESH copy for each temperature
        with open('data/processed/penrose_tiling_energy_initialized.json') as f:
            tiling = json.load(f)
        
        # Apply seed (same for all)
        for tile in tiling["tiles"]:
            if tile["id"] in seed_tiles:
                tile["growth_status"] = "seed"
                tile["flippable"] = True
            else:
                tile["growth_status"] = "ungrown"
                tile["flippable"] = False  # Only seed is flippable for pure MC test
        
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
            config={'base_steps': 200, 'burn_in_steps': 50}
        )
        
        # Initialize energy
        mc_engine.initialize_energy(tiling)
        initial_energy = mc_engine.current_energy
        
        # Run MC
        stats = mc_engine.run_sweep(tiling, steps=200)
        
        results.append({
            'temperature': T,
            'acceptance': stats['acceptance_rate'],
            'uphill_fraction': stats['positive_ratio'],
            'delta_mean': stats['delta_mean'],
            'delta_std': stats['delta_std'],
            'energy_change': stats['final_energy'] - initial_energy,
            'flippable_in_seed': len(flip_engine.find_flippable_hexagons(tiling))
        })
        
        print(f"  Acceptance: {stats['acceptance_rate']:.1%}")
        print(f"  Energy change: {stats['final_energy'] - initial_energy:+.2f}")
        print(f"  Flippable hexagons in seed: {results[-1]['flippable_in_seed']}")
    
    # Print clean table
    print("\n" + "=" * 60)
    print("📊 RELIABLE RESULTS:")
    print("-" * 60)
    print(f"{'T':>5} {'Accept':>8} {'Uphill%':>8} {'ΔE mean':>9} {'ΔE std':>9} {'ΔE total':>9}")
    print("-" * 60)
    
    for r in results:
        print(f"{r['temperature']:5.1f} "
              f"{r['acceptance']:7.1%} "
              f"{r['uphill_fraction']*100:7.1f}% "
              f"{r['delta_mean']:8.3f} "
              f"{r['delta_std']:8.3f} "
              f"{r['energy_change']:8.3f}")
    
    # CRITICAL ANALYSIS
    print("\n" + "=" * 60)
    print("🚨 PHYSICS INTERPRETATION:")
    
    # Check 1: Is MC active?
    flippable_counts = [r['flippable_in_seed'] for r in results]
    if max(flippable_counts) == 0:
        print("❌ CRITICAL: NO FLIPPABLE HEXAGONS IN SEED REGION")
        print("   MC cannot propose any moves!")
        print("   Check: Are tiles in seed region marked as flippable?")
    else:
        print(f"✅ MC is active: {min(flippable_counts)}-{max(flippable_counts)} flippable hexagons")
    
    # Check 2: Temperature dependence
    acceptances = [r['acceptance'] for r in results]
    if max(acceptances) - min(acceptances) < 0.05:
        print("⚠️  WEAK temperature dependence")
        print("   Acceptance similar at all T - energy scale may be wrong")
    else:
        print("✅ Strong temperature dependence")
        print(f"   Acceptance varies from {min(acceptances):.1%} to {max(acceptances):.1%}")
    
    # Check 3: Energy minimization
    energy_changes = [r['energy_change'] for r in results]
    avg_energy_change = np.mean(energy_changes)
    
    if avg_energy_change > 0.1:
        print(f"⚠️  Energy INCREASING on average (+{avg_energy_change:.2f})")
        print("   MC is exploring, not minimizing - check for uphill bias")
    elif avg_energy_change < -0.1:
        print(f"✅ Energy DECREASING on average ({avg_energy_change:.2f})")
        print("   MC is minimizing energy as expected")
    else:
        print("⚖️  Energy roughly constant")
        print("   Landscape may be flat or at equilibrium")
    
    # Check 4: Uphill acceptance pattern
    print(f"\n📈 UPHILL ACCEPTANCE PATTERN:")
    for r in results:
        T = r['temperature']
        uphill = r['uphill_fraction']
        expected = np.exp(-1/T) if T > 0 else 0  # Rough expectation for ΔE=1
        
        if T > 0:
            print(f"   T={T}: {uphill:.1%} uphill (expected ~{expected:.1%} for ΔE=1)")
    
    return results

if __name__ == "__main__":
    import numpy as np
    results = test_temperature_summary()