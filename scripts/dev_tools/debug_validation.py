#!/usr/bin/env python3
"""
Debug script to see exactly why vertices are classified as HIGH_ENERGY
NOW RESPECTS CONFIG SAMPLING SETTINGS
"""

import sys
import os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.energy.widom_inspired_energy import WidomInspiredEnergy
from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.tilings.penrose_p3 import PenroseTiling
from src.utils.config import ConfigManager

def debug_vertex_classification(use_sampling=True, sample_size=10):
    classifier = CombinatorialVertexClassifier()
    
    config = ConfigManager("configs/phase3_healing_dynamics.toml")
    tiling_generator = PenroseTiling(config)
    tiling = tiling_generator.generate()
    
    # ===== CONFIG-DRIVEN SAMPLING LOGIC =====
    if use_sampling:
        # Sample mode - for quick debugging
        total_tiles = len(tiling["tiles"])
        sample_tiles = list(range(0, total_tiles, total_tiles // sample_size))[:sample_size]
        print(f"🔍 SAMPLING MODE: Processing {len(sample_tiles)} tiles (config: debug.use_sampling=true)")
    else:
        # Full mode - for complete analysis  
        sample_tiles = range(len(tiling["tiles"]))
        print(f"🔍 FULL MODE: Processing ALL {len(tiling['tiles'])} tiles (config: debug.use_sampling=false)")
    # ==================================
    
    print("🔍 DEBUGGING VERTEX CLASSIFICATION")
    print("=" * 60)
    
    for tile_id in sample_tiles:
        if tile_id >= len(tiling["tiles"]):
            continue
            
        print(f"\n📐 Tile {tile_id}:")
        
        # Get the environment analysis
        environment = classifier._analyze_vertex_environment(tile_id, tiling)
        geometric_violations = classifier._check_geometric_constraints(environment)
        coordination_analysis = classifier._analyze_coordination_pattern(environment)
        
        print(f"   Center type: {environment.center_tile_type}")
        print(f"   Coordination: {environment.coordination_number}")
        print(f"   Angles: {[f'{a:.1f}°' for a in environment.angle_sequence]}")
        print(f"   Angle std: {np.std(environment.angle_sequence):.1f}°")
        
        print(f"   Geometric violations: {geometric_violations}")
        print(f"   Angular regularity: {coordination_analysis['angular_regularity']:.2f}")
        print(f"   Coordination quality: {coordination_analysis['coordination_quality']:.2f}")
        
        final_class = classifier.classify_vertex_environment(tile_id, tiling)
        print(f"   🎯 FINAL CLASS: {final_class}")
        
        if any(geometric_violations.values()):
            print("   ❌ FAILED: Geometric constraints")
        elif (coordination_analysis['angular_regularity'] < 0.3 or 
              coordination_analysis['coordination_quality'] < 0.5):
            print("   ⚠️  MEDIUM: Coordination pattern issues")
        else:
            print("   ✅ LOW_ENERGY: Good Penrose environment")

# Add to debug_validation.py to see full distribution
def analyze_full_distribution():
    config = ConfigManager("configs/phase1_baseline.toml")
    tiling_generator = PenroseTiling(config)
    tiling = tiling_generator.generate()
    
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy()
    
    # Get classification for ALL tiles
    all_classifications = []
    for tile_id in range(len(tiling["tiles"])):
        classification = classifier.classify_vertex_environment(tile_id, tiling)
        all_classifications.append(classification)
    
    low_count = all_classifications.count("LOW_ENERGY")
    medium_count = all_classifications.count("MEDIUM_ENERGY")
    high_count = all_classifications.count("HIGH_ENERGY")
    
    print(f"📊 FULL DISTRIBUTION ({len(all_classifications)} tiles):")
    print(f"   LOW_ENERGY: {low_count} ({low_count/len(all_classifications)*100:.1f}%)")
    print(f"   MEDIUM_ENERGY: {medium_count} ({medium_count/len(all_classifications)*100:.1f}%)")
    print(f"   HIGH_ENERGY: {high_count} ({high_count/len(all_classifications)*100:.1f}%)")

if __name__ == "__main__":
    # Load config to determine sampling behavior
    config = ConfigManager("configs/phase3_healing_dynamics.toml")
    
    # Get debug settings from config with safe defaults
    debug_config = config._config.get("debug", {})
    use_sampling = debug_config.get("use_sampling", True)  # Default to True for debugging
    sample_size = debug_config.get("sample_size", 10)      # Default to 10 for quick debugging
    
    print(f"🔧 Config settings: use_sampling={use_sampling}, sample_size={sample_size}")
    
    debug_vertex_classification(use_sampling, sample_size)
    analyze_full_distribution()