# test_correct_flip.py
import json
import numpy as np

def test_correct_flip():
    print("🧪 Testing corrected flip implementation")
    
    # Load data
    with open("data/processed/penrose_tiling_energy_initialized.json", "r") as f:
        tiling_data = json.load(f)
    
    # Initialize components
    from src.simulation.flip_engine import FlipEngine
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy
    from src.utils.config import ConfigManager
    
    config = ConfigManager("configs/phase1_baseline.toml")
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy.from_config(config)
    flip_engine = FlipEngine(classifier, energy_model)
    
    # Find a test cluster
    test_cluster = [7, 8, 2596]  # From your data
    
    print(f"\n🔍 Testing cluster: {test_cluster}")
    
    # Get initial state
    initial_vertices = {}
    for tid in test_cluster:
        tile = tiling_data["tiles"][tid]
        initial_vertices[tid] = [tuple(v) for v in tile["vertices"]]
    
    # Capture complete state
    undo_info = flip_engine.capture_state(test_cluster, tiling_data)
    
    # Apply flip
    flip_engine.apply_flip(test_cluster, tiling_data)
    
    # Verify changes
    print("\n📊 After flip:")
    changes = False
    for tid in test_cluster:
        tile = tiling_data["tiles"][tid]
        new_vertices = [tuple(v) for v in tile["vertices"]]
        
        if set(new_vertices) != set(initial_vertices[tid]):
            changes = True
            print(f"  Tile {tid}: geometry changed")
            print(f"    Old vertices: {initial_vertices[tid][:2]}...")
            print(f"    New vertices: {new_vertices[:2]}...")
    
    if not changes:
        print("❌ No geometry changes - flip not working")
        return False
    
    # Check energy sensitivity
    energy_before = 0
    for tid in test_cluster:
        energy_before += energy_model.compute_local_energy(tid, tiling_data)
    
    energy_model.clear_cache()
    
    energy_after = 0
    for tid in test_cluster:
        energy_after += energy_model.compute_local_energy(tid, tiling_data)
    
    print(f"\n⚡ Energy change: {energy_after - energy_before:.6f}")
    
    if abs(energy_after - energy_before) < 0.001:
        print("⚠️  Small energy change - check energy model")
    
    # Restore and verify
    flip_engine.restore_state(undo_info, tiling_data)
    
    print("\n🔙 After restore:")
    for tid in test_cluster:
        tile = tiling_data["tiles"][tid]
        restored_vertices = [tuple(v) for v in tile["vertices"]]
        if set(restored_vertices) == set(initial_vertices[tid]):
            print(f"  Tile {tid}: correctly restored")
        else:
            print(f"  Tile {tid}: RESTORE FAILED")
            return False
    
    print("\n✅ All tests passed!")
    return True

if __name__ == "__main__":
    import sys
    success = test_correct_flip()
    sys.exit(0 if success else 1)