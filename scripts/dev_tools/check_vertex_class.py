#!/usr/bin/env python3
"""
Check if vertex_class and local_energy are present for all active tiles
"""

import json

def main():
    # Load latest experiment
    with open('data/growth_experiments/pores_0.0_20251214_194224.json') as f:
        exp = json.load(f)
    
    # Load the tiling with energy
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Check first 100 tiles
    missing_vertex = 0
    missing_energy = 0
    
    for i, tile in enumerate(tiling['tiles'][:100]):
        if 'vertex_class' not in tile:
            missing_vertex += 1
        if 'local_energy' not in tile:
            missing_energy += 1
    
    print(f"Checked 100 tiles:")
    print(f"  Missing vertex_class: {missing_vertex}")
    print(f"  Missing local_energy: {missing_energy}")
    
    # Check defect counts
    print(f"\nDefect tracking from experiment:")
    for step in exp['growth_steps'][:3]:
        print(f"  Step {step['step']}: defects={step['defect_count']}")
    
    return missing_vertex == 0 and missing_energy == 0

if __name__ == "__main__":
    main()