
# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------
# scripts/system_diagnostic.py
#!/usr/bin/env python3
"""
Quick system diagnostic - minimal output
"""

import json
from pathlib import Path

def quick_diagnostic():
    """Run quick diagnostic of the system"""
    print("🔧 QUICK SYSTEM DIAGNOSTIC")
    print("=" * 40)
    
    # Check essential files
    essential_files = [
        "data/processed/penrose_tiling_energy_initialized.json",
        "configs/phase1_baseline.toml",
        "src/simulation/flip_engine.py",
        "src/simulation/mc_engine.py",
        "src/growth/growth_engine.py"
    ]
    
    print("📁 Essential files:")
    all_exist = True
    for file in essential_files:
        exists = Path(file).exists()
        status = "✅" if exists else "❌"
        print(f"  {status} {file}")
        if not exists:
            all_exist = False
    
    if not all_exist:
        print("\n❌ Missing essential files!")
        return False
    
    # Load tiling data
    data_path = Path("data/processed/penrose_tiling_energy_initialized.json")
    with open(data_path, 'r') as f:
        tiling_data = json.load(f)
    
    print(f"\n📊 Tiling data:")
    print(f"  Tiles: {len(tiling_data['tiles'])} total")
    
    # Count active tiles
    active = [t for t in tiling_data['tiles'] if not t.get('removed', False)]
    print(f"  Active: {len(active)}")
    
    # Check energy fields
    tiles_with_energy = sum(1 for t in active if 'local_energy' in t)
    print(f"  Tiles with energy field: {tiles_with_energy}/{len(active)}")
    
    # Check vertex classes
    classes = {}
    for tile in active:
        cls = tile.get('vertex_class', 'UNKNOWN')
        classes[cls] = classes.get(cls, 0) + 1
    print(f"  Vertex classes: {classes}")
    
    # Quick flip engine test
    print("\n⚙️ Flip engine quick test:")
    try:
        from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
        from src.energy.widom_inspired_energy import WidomInspiredEnergy
        from src.simulation.flip_engine import FlipEngine
        
        classifier = CombinatorialVertexClassifier()
        energy_model = WidomInspiredEnergy()
        flip_engine = FlipEngine(classifier, energy_model)
        
        clusters = flip_engine.find_flippable_hexagons(tiling_data)
        print(f"  Flippable hexagons: {len(clusters)}")
        
        if clusters:
            # Test geometry on first cluster
            cluster = clusters[0]
            L = flip_engine.compute_edge_length(tiling_data)
            
            # Quick edge length check
            edges_before = []
            for tid in cluster:
                tile = tiling_data["tiles"][tid]
                vertices = tile["vertices"]
                for i in range(4):
                    import numpy as np
                    v1 = np.array(vertices[i])
                    v2 = np.array(vertices[(i+1)%4])
                    length = np.linalg.norm(v2 - v1)
                    edges_before.append(abs(length - L))
            
            avg_error = sum(edges_before) / len(edges_before) if edges_before else 0
            print(f"  Edge length error: {avg_error:.6f} (target L={L:.3f})")
            
            if avg_error < 0.001:
                print("  ✅ Edge lengths correct")
            else:
                print(f"  ⚠️ Edge length variance: {avg_error:.6f}")
    except Exception as e:
        print(f"  ❌ Flip engine test failed: {e}")
        return False
    
    print("\n" + "=" * 40)
    print("✅ System diagnostic complete")
    return True

if __name__ == "__main__":
    success = quick_diagnostic()
    exit(0 if success else 1)