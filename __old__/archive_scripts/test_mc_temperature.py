
# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------
# scripts/test_mc_temperature.py
import json
import sys
import os

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy
from src.simulation.flip_engine import FlipEngine

def test_temperatures():
    print("🌡️ Testing temperature scaling...")
    
    # Load data
    with open("data/processed/penrose_tiling_energy_initialized.json", "r") as f:
        tiling_data = json.load(f)
    
    # Test different temperatures
    temperatures = [0.3, 0.1, 0.05, 0.01, 0.001]
    
    for T in temperatures:
        print(f"\n🧪 T = {T}:")
        
        # Initialize
        classifier = CombinatorialVertexClassifier()
        energy_model = WidomInspiredEnergy()
        flip_engine = FlipEngine(classifier, energy_model)
        
        # Find clusters
        clusters = flip_engine.find_flippable_hexagons(tiling_data)[:50]  # First 50
        
        # Sample energy differences
        delta_energies = []
        for cluster in clusters[:10]:  # Test 10 clusters
            # Compute ΔE without applying
            affected = flip_engine._get_two_ring_neighborhood(cluster, tiling_data)
            
            # Energy before
            energy_before = 0
            for tid in affected:
                tile = tiling_data["tiles"][tid]
                if not tile.get("removed", False):
                    energy_before += tile.get("local_energy", 0)
            
            # Apply and undo
            undo = flip_engine.capture_state(cluster, tiling_data)
            success = flip_engine.apply_flip(cluster, tiling_data)
            if success:
                # Energy after
                energy_after = 0
                for tid in affected:
                    tile = tiling_data["tiles"][tid]
                    if not tile.get("removed", False):
                        energy_after += tile.get("local_energy", 0)
                
                delta = energy_after - energy_before
                delta_energies.append(delta)
                
                # Restore
                flip_engine.restore_state(undo, tiling_data)
                energy_model.clear_cache()
        
        if delta_energies:
            avg_delta = sum(delta_energies) / len(delta_energies)
            max_delta = max(delta_energies)
            min_delta = min(delta_energies)
            
            # Expected acceptance at this T
            acceptance_est = sum(1 for d in delta_energies if d <= 0 or 
                                __import__('math').exp(-d/T) > 0.5) / len(delta_energies)
            
            print(f"  ΔE range: {min_delta:.4f} to {max_delta:.4f}")
            print(f"  Avg |ΔE|: {abs(avg_delta):.4f}")
            print(f"  Est. acceptance: {acceptance_est:.1%}")
            print(f"  kT = {T:.4f}, kT/|ΔE|_avg = {T/max(0.001, abs(avg_delta)):.2f}")

if __name__ == "__main__":
    test_temperatures()