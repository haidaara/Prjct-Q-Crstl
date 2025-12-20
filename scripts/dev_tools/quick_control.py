#!/usr/bin/env python3
"""
RELIABLE control experiment with verification
"""

import json
import sys
import os
sys.path.insert(0, '.')

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine
from src.simulation.mc_engine import MonteCarloEngine
from src.simulation.growth_engine import GrowthSimulator

def run_control_experiment():
    """Run control experiment - GROWTH ONLY (no MC)"""
    print("🧪 RELIABLE CONTROL EXPERIMENT")
    print("=" * 60)
    print("Testing: Growth WITHOUT MC healing")
    print("Purpose: Establish baseline defect creation rate")
    print()
    
    # Ensure output directory exists
    os.makedirs("data/control_tests", exist_ok=True)
    
    # Load tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Initialize components
    classifier = CombinatorialVertexClassifier()
    energy_params = EnergyParameters()
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Create MC engine (will NOT be used - steps=0)
    mc_engine = MonteCarloEngine(
        temperature=1.5,  # Irrelevant since steps=0
        energy_model=energy_model,
        flip_engine=flip_engine,
        config={'base_steps': 100, 'burn_in_steps': 0}
    )
    
    # Create growth simulator
    growth_config = {
        "seed_radius": 5.0,
        "growth_steps": 5,  # Fewer steps for quick test
        "mc_steps_per_growth": 0,  # CRITICAL: NO MC
    }
    
    growth_sim = GrowthSimulator(mc_engine, growth_config)
    
    # Initialize seed
    tiling = growth_sim.initialize_seed(tiling)
    
    # Track defects
    defect_history = []
    tile_count_history = []
    
    print("Step 0 (seed):")
    active_tiles = [t for t in tiling["tiles"] 
                   if t.get("growth_status") == "seed" 
                   and not t.get("removed", False)]
    seed_defects = sum(1 for t in active_tiles if t.get("vertex_class") == "HIGH_ENERGY")
    print(f"  Active tiles: {len(active_tiles)}")
    print(f"  Defects: {seed_defects}")
    print(f"  Defect density: {seed_defects/len(active_tiles):.3%}")
    defect_history.append(seed_defects)
    tile_count_history.append(len(active_tiles))
    
    # Growth steps
    for step in range(1, growth_config["growth_steps"] + 1):
        print(f"\nStep {step}:")
        
        # Store state before growth
        before_defects = sum(1 for t in tiling["tiles"] 
                           if t.get("growth_status") in ["seed", "grown", "frontier", "recently_grown"]
                           and not t.get("removed", False)
                           and t.get("vertex_class") == "HIGH_ENERGY")
        
        # Grow (NO MC - growth only)
        tiling, new_tiles, mc_stats = growth_sim.grow_step(tiling, obstacles={})
        
        # Get active region after growth
        active_tiles = [t for t in tiling["tiles"] 
                       if t.get("growth_status") in ["seed", "grown", "frontier", "recently_grown"]
                       and not t.get("removed", False)]
        
        after_defects = sum(1 for t in active_tiles if t.get("vertex_class") == "HIGH_ENERGY")
        new_defects = after_defects - before_defects
        
        print(f"  New tiles added: {len(new_tiles)}")
        print(f"  Total active tiles: {len(active_tiles)}")
        print(f"  Defects before growth: {before_defects}")
        print(f"  Defects after growth: {after_defects}")
        print(f"  New defects from growth: {new_defects}")
        print(f"  Defect density: {after_defects/len(active_tiles):.3%}")
        
        defect_history.append(after_defects)
        tile_count_history.append(len(active_tiles))
    
    # Analysis
    print("\n" + "=" * 60)
    print("📊 CONTROL EXPERIMENT ANALYSIS:")
    
    # Calculate defect creation rate
    if len(defect_history) > 1:
        total_new_defects = defect_history[-1] - defect_history[0]
        total_new_tiles = tile_count_history[-1] - tile_count_history[0]
        
        if total_new_tiles > 0:
            defect_rate = total_new_defects / total_new_tiles
            print(f"Total new tiles grown: {total_new_tiles}")
            print(f"Total new defects created: {total_new_defects}")
            print(f"Defect creation rate: {defect_rate:.3%} (defects/new tile)")
            
            # Interpretation
            if defect_rate < 0.01:
                print("✅ LOW defect creation (<1%)")
                print("   MC healing might keep up easily")
            elif defect_rate < 0.05:
                print("⚠️  MODERATE defect creation (1-5%)")
                print("   MC needs reasonable acceptance to heal")
            else:
                print("❌ HIGH defect creation (>5%)")
                print("   Growth overwhelms healing - need more MC steps")
        else:
            print("⚠️  No new tiles grown - check growth constraints")
    
    # Save results
    results = {
        "experiment_type": "control_growth_only",
        "growth_steps": growth_config["growth_steps"],
        "mc_steps_per_growth": 0,
        "defect_history": defect_history,
        "tile_count_history": tile_count_history,
        "defect_densities": [d/t if t>0 else 0 
                            for d, t in zip(defect_history, tile_count_history)]
    }
    
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"data/control_tests/control_growth_only_{timestamp}.json"
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Results saved to: {output_file}")
    
    # Critical question for healing experiments
    print("\n" + "=" * 60)
    print("🔑 KEY QUESTION FOR HEALING EXPERIMENTS:")
    print("How many MC steps are needed to heal the defects created each step?")
    print(f"If growth creates ~{defect_history[-1]-defect_history[0]} defects in {growth_config['growth_steps']} steps,")
    print(f"then MC needs to heal ~{(defect_history[-1]-defect_history[0])/growth_config['growth_steps']:.1f} defects per step.")
    
    return results

if __name__ == "__main__":
    results = run_control_experiment()