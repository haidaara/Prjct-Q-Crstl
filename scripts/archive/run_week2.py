# scripts/run_week2.py - CORRECTED VERSION
#!/usr/bin/env python3
"""
Simple test for Week 2 implementation - WITH DEBUGGING AND CORRECT DATA LOADING
"""

import sys
import os
import json
from pathlib import Path

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_week2():
    print("🧪 Testing Week 2 Implementation")
    print("=" * 40)
    
    # Load data - CORRECT METHOD
    data_file = "data/processed/penrose_tiling_energy_initialized.json"
    
    if not os.path.exists(data_file):
        print(f"❌ Missing data file: {data_file}")
        print("   Run Week 1 validation first:")
        print("   python scripts/validate_week1_physics.py")
        return False
    
    with open(data_file, "r") as f:
        tiling_data = json.load(f)
    
    print(f"📁 Loaded tiling: {len(tiling_data['tiles'])} tiles")
    print(f"📊 Metadata: {tiling_data['metadata']['tile_count']} tiles, "
          f"{tiling_data['metadata'].get('energy_model', 'No energy model')}")
    
    # Initialize components
    from src.utils.config import ConfigManager
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    from src.simulation.growth_engine import GrowthSimulator
    
    config = ConfigManager("configs/phase1_baseline.toml")
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy.from_config(config)
    flip_engine = FlipEngine(classifier, energy_model)
    mc_engine = MonteCarloEngine(temperature=0.3, energy_model=energy_model, flip_engine=flip_engine)
    growth_engine = GrowthSimulator(mc_engine)
    
    print("✅ Components initialized")
    
    # Create output directory for diagnostics
    output_dir = Path("data/experiments")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🔍 DEBUG: Checking flippable hexagons...")
    flippable_clusters = flip_engine.find_flippable_hexagons(tiling_data)
    print(f"   Found {len(flippable_clusters)} flippable hexagons")
    
    if len(flippable_clusters) > 0:
        print(f"   First cluster: {flippable_clusters[0]}")
        # Debug first cluster
        for tile_id in flippable_clusters[0]:
            tile = tiling_data["tiles"][tile_id]
            print(f"     Tile {tile_id}: {tile['type']}, flippable={tile.get('flippable', True)}")
    
    # Test MC
    print(f"\n🔬 Testing Monte Carlo (T=0.3)...")
    
    # Initialize energy for all tiles
    print("   Initializing energy for all tiles...")
    for tile in tiling_data["tiles"]:
        if not tile.get("removed", False):
            # Ensure all tiles have energy calculated
            if "local_energy" not in tile:
                tile_id = tile["id"]
                energy_model.compute_local_energy(tile_id, tiling_data)
    
    mc_engine.initialize_energy(tiling_data)
    initial_energy = mc_engine.current_energy
    
    # Run MC steps with better reporting
    acceptance_count = 0
    energy_history = []
    
    for step in range(100):
        accepted, delta_energy = mc_engine.run_step(tiling_data)
        if accepted:
            acceptance_count += 1
        energy_history.append(mc_engine.current_energy)
        
        if step % 20 == 0:
            current_rate = acceptance_count / (step + 1)
            print(f"   Step {step}: E={mc_engine.current_energy:.2f}, "
                  f"Acceptance={current_rate:.1%}, Δ={delta_energy:.3f}")
    
    final_energy = mc_engine.current_energy
    
    # Save MC diagnostics
    mc_diagnostics = {
        "initial_energy": initial_energy,
        "final_energy": final_energy,
        "acceptance_rate": acceptance_count / 100,
        "energy_history": energy_history,
        "flip_stats": mc_engine.metrics["flip_stats"]
    }
    
    with open(output_dir / "mc_diagnostics.json", 'w') as f:
        json.dump(mc_diagnostics, f, indent=2)
    
    print(f"✅ MC test: {acceptance_count}/100 accepted ({acceptance_count/100:.1%})")
    print(f"   Energy: {initial_energy:.2f} → {final_energy:.2f}")
    
    # Test growth
    print(f"\n🌱 Testing growth simulation...")
    seed_center = [30.0, 30.0]
    tiling_data = growth_engine.initialize_seed(tiling_data, seed_center, radius=8.0)
    
    # Count initial growth status
    status_counts = {}
    for tile in tiling_data["tiles"]:
        status = tile.get("growth_status", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
    print(f"   Growth status: {status_counts}")
    
    # Save initial growth state
    with open(output_dir / "growth_initial.json", 'w') as f:
        json.dump(tiling_data, f, indent=2)
    
    obstacles = {}
    tiling_data, new_tiles, _ = growth_engine.grow_step(tiling_data, obstacles)
    
    # Save growth diagnostics
    growth_diagnostics = growth_engine.get_diagnostics()
    with open(output_dir / "growth_diagnostics.json", 'w') as f:
        json.dump(growth_diagnostics, f, indent=2)
    
    print(f"✅ Growth test: added {len(new_tiles)} tiles")
    print(f"   Total growth steps: {growth_diagnostics['current_step']}")
    
    # Final check
    energy_model.clear_cache()
    recomputed_energy = energy_model.compute_total_energy(tiling_data)
    energy_consistent = abs(mc_engine.current_energy - recomputed_energy) < 0.01
    
    print(f"\n📊 Final validation:")
    print(f"   MC energy: {mc_engine.current_energy:.2f}")
    print(f"   Recomputed energy: {recomputed_energy:.2f}")
    print(f"   Energy consistent: {energy_consistent}")



    # Test: Does flipping actually change vertex classification?
    cluster = [ 54, 55, 56]
    print("\n🔬 SINGLE FLIP TEST:")
    print("Before flip:")
    for tid in cluster:
        tile = tiling_data["tiles"][tid]
         # Recompute energy (updates vertex_class)
        energy = energy_model.compute_local_energy(tid, tiling_data)
        tile = tiling_data["tiles"][tid]
        print(f"  Tile {tid}: {tile['type']}, vertex_class={tile['vertex_class']}, energy={energy}")

    # Manually flip
    flip_engine.apply_flip(cluster, tiling_data)
    energy_model.clear_cache()

    print("\nAfter flip:")
    for tid in cluster:
        # Recompute energy (updates vertex_class)
        energy = energy_model.compute_local_energy(tid, tiling_data)
        tile = tiling_data["tiles"][tid]
        print(f"  Tile {tid}: {tile['type']}, vertex_class={tile['vertex_class']}, energy={energy}")



    # Save final state
    with open(output_dir / "final_state.json", 'w') as f:
        json.dump(tiling_data, f, indent=2)
    
    # Check for data files created
    created_files = list(output_dir.glob("*.json"))
    print(f"\n📁 Data files created in {output_dir}:")
    for f in created_files:
        print(f"   • {f.name}")
    
    success_conditions = [
        energy_consistent,
        acceptance_count > 0,
        final_energy < initial_energy
    ]
    
    if all(success_conditions):
        print("\n🎉 Week 2 implementation successful!")
        return True
    else:
        print("\n⚠️  Issues detected:")
        if acceptance_count == 0:
            print("   - No MC moves accepted (check flip constraints)")
        if final_energy >= initial_energy:
            print("   - Energy didn't decrease (check energy model)")
        if not energy_consistent:
            print("   - Energy inconsistency detected")
        print(f"   Success conditions: {success_conditions}")
        return False

if __name__ == "__main__":
    success = test_week2()
    sys.exit(0 if success else 1)