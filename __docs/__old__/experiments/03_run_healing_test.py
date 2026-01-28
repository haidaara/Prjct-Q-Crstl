#!/usr/bin/env python3
"""
Refactored Healing Experiment Script
Uses the new healing architecture.
"""

import sys
import os
import json
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from healing import healing_engine
from src.simulation.flip_engine import FlipEngine
from src.simulation.mc_engine import MonteCarloEngine
from src.energy.widom_inspired_energy import WidomInspiredEnergy
from src.healing.healing_engine import HealingEngine

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run healing experiment")
    
    parser.add_argument(
        "--input", 
        default="data/processed/penrose_tiling_energy_initialized.json",
        help="Input tiling file"
    )
    
    parser.add_argument(
        "--output-dir", 
        default="data/experiments/healing",
        help="Output directory"
    )
    
    parser.add_argument(
        "--center-x", 
        type=float, 
        default=0.0,
        help="X coordinate of region center"
    )
    
    parser.add_argument(
        "--center-y", 
        type=float, 
        default=0.0,
        help="Y coordinate of region center"
    )
    
    parser.add_argument(
        "--R-core", 
        type=float, 
        default=15.0,
        help="Core region radius"
    )
    
    parser.add_argument(
        "--R-buffer", 
        type=float, 
        default=25.0,
        help="Buffer region radius"
    )
    
    parser.add_argument(
        "--create-defects", 
        action="store_true",
        help="Create controlled defects before healing"
    )
    
    parser.add_argument(
        "--target-defects", 
        type=int, 
        default=15,
        help="Number of defects to create"
    )
    
    parser.add_argument(
        "--defect-criterion",
        choices=["geometry", "physics"],
        default="physics",
        help="Defect criterion to use"
    )
    
    parser.add_argument(
        "--temperature-schedule",
        nargs="+",
        type=float,
        default=[5.0, 3.0, 2.0, 1.0, 0.5, 0.2, 0.1],
        help="Temperature schedule (list of temperatures)"
    )
    
    parser.add_argument(
        "--steps-per-t",
        type=int,
        default=100,
        help="Steps per temperature"
    )
    
    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility"
    )
    
    return parser.parse_args()

def main():
    """Main healing experiment."""
    args = parse_arguments()
    
    # Set random seed if provided
    if args.seed is not None:
        import random
        import numpy as np
        random.seed(args.seed)
        np.random.seed(args.seed)
    
    print("=" * 60)
    print("HEALING EXPERIMENT")
    print("=" * 60)
    print(f"Input: {args.input}")
    print(f"Output: {args.output_dir}")
    print(f"Region: center=({args.center_x}, {args.center_y}), "
          f"R_core={args.R_core}, R_buffer={args.R_buffer}")
    print(f"Create defects: {args.create_defects} (target: {args.target_defects})")
    print(f"Defect criterion: {args.defect_criterion}")
    print(f"Temperature schedule: {args.temperature_schedule}")
    print(f"Steps per T: {args.steps_per_t}")
    print(f"Seed: {args.seed}")
    print()
    
    # 1. Load tiling
    print("Loading tiling...")
    with open(args.input, 'r') as f:
        tiling = json.load(f)
    
    print(f"Loaded {len(tiling['tiles'])} tiles")
    
    print("Initializing engines...")
    energy_model = WidomInspiredEnergy()
    flip_engine = FlipEngine(energy_model.classifier, energy_model)
    mc_engine = MonteCarloEngine(energy_model=energy_model, flip_engine=flip_engine)

    
    # 3. Create healing engine
    print("Creating healing engine...")
    healing_engine = HealingEngine(flip_engine, mc_engine, energy_model)
    
    # 4. Configure healing engine
    from src.healing.defect_policy import DefectCriterion
    
    healing_engine.configure(
        center=(args.center_x, args.center_y),
        R_core=args.R_core,
        R_buffer=args.R_buffer,
        defect_criterion=DefectCriterion(args.defect_criterion),
        temperature_schedule=[
            (T, args.steps_per_t) for T in args.temperature_schedule
        ]
    )
    
    # 5. Run experiment
    print("\nRunning healing experiment...")
    results, tiling = healing_engine.run_full_experiment(
        tiling_data=tiling,
        create_defects=args.create_defects,
        target_defects=args.target_defects
    )

    
    # 6. Save results
    print("\nSaving results...")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate unique experiment ID
    import time
    experiment_id = f"healing_{int(time.time())}_{args.seed if args.seed else 'random'}"
    
    # Save final tiling
    tiling_path = output_dir / f"{experiment_id}_tiling.json"
    with open(tiling_path, 'w') as f:
        json.dump(tiling, f, indent=2)
    
    # Save metrics
    metrics_path = output_dir / f"{experiment_id}_metrics.json"
    if healing_engine.metrics_tracker is not None:
        healing_engine.metrics_tracker.export_metrics(str(metrics_path))
    
    # Save results summary
    summary_path = output_dir / f"{experiment_id}_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    # Save configuration
    config = {
        'experiment_id': experiment_id,
        'timestamp': time.time(),
        'arguments': vars(args),
        'configuration': healing_engine.config,
        'success': results['success'],
        'healing_efficiency': results['healing_efficiency'],
        'total_time': results['total_time']
    }
    
    config_path = output_dir / f"{experiment_id}_config.json"
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2, default=str)
    
    # 7. Generate quick visualization if available
    try:
        from src.viz.static_plots import plot_energy_map
        import matplotlib.pyplot as plt
        
        fig = plot_energy_map(tiling, title=f"Healing Results: {experiment_id}")
        plot_path = output_dir / f"{experiment_id}_energy_map.png"
        plt.savefig(plot_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Saved visualization: {plot_path}")
    except ImportError:
        print("Visualization module not available, skipping plots")
    
    print("\n" + "=" * 60)
    print("EXPERIMENT COMPLETE")
    print("=" * 60)
    print(f"Experiment ID: {experiment_id}")
    print(f"Success: {results['success']}")
    print(f"Healing Efficiency: {results['healing_efficiency']:.1%}")
    print(f"Time: {results['total_time']:.1f}s")
    print(f"Results saved to: {output_dir}")
    
    return 0 if results['success'] else 1

if __name__ == "__main__":
    sys.exit(main())