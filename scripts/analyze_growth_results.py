#!/usr/bin/env python3
"""
Analyze growth experiment results and create simple visualizations
FIXED VERSION for actual data structure
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import glob

def load_experiment_results(experiment_file: str):
    """Load experiment results from JSON file"""
    with open(experiment_file, 'r') as f:
        return json.load(f)

def create_simple_plots(experiment_data: dict, output_dir: Path):
    """Create basic plots of growth metrics"""
    if not experiment_data.get("growth_steps"):
        print("⚠️  No growth steps data to plot")
        return None
    
    steps = [s["step"] for s in experiment_data["growth_steps"]]
    
    # Check what data we have
    new_tiles = [s["new_tiles"] for s in experiment_data["growth_steps"]]
    energies = [s["total_energy"] for s in experiment_data["growth_steps"]]
    
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Total growth
    axes[0, 0].plot(steps, np.cumsum(new_tiles), 'b-o', linewidth=2, markersize=6)
    axes[0, 0].set_title("Total Tiles Grown")
    axes[0, 0].set_xlabel("Growth Step")
    axes[0, 0].set_ylabel("Cumulative Tiles")
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Growth rate per step
    axes[0, 1].bar(steps, new_tiles, alpha=0.7, color='green', width=0.6)
    axes[0, 1].set_title("Growth Rate per Step")
    axes[0, 1].set_xlabel("Growth Step")
    axes[0, 1].set_ylabel("New Tiles")
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # Plot 3: Energy evolution
    axes[1, 0].plot(steps, energies, 'r-o', linewidth=2, markersize=6)
    axes[1, 0].set_title("Total Energy")
    axes[1, 0].set_xlabel("Growth Step")
    axes[1, 0].set_ylabel("Energy")
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Energy change per step
    energy_changes = np.diff(energies)
    axes[1, 1].bar(steps[1:], energy_changes, alpha=0.7, color='orange', width=0.6)
    axes[1, 1].set_title("Energy Change per Step")
    axes[1, 1].set_xlabel("Growth Step")
    axes[1, 1].set_ylabel("Δ Energy")
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    
    # Add experiment info
    exp_name = experiment_data.get("experiment_name", "Unknown")
    config = experiment_data.get("config", {})
    temp = config.get("monte_carlo", {}).get("temperature", "?")
    mc_steps = config.get("growth", {}).get("mc_steps_per_growth", "?")
    
    fig.suptitle(f"Growth Experiment: {exp_name}\nTemperature: {temp}, MC steps/growth: {mc_steps}", 
                fontsize=14, y=1.02)
    
    plt.tight_layout()
    
    # Save figure
    plot_file = output_dir / f"{exp_name}_analysis.png"
    plt.savefig(plot_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"📊 Plots saved to: {plot_file}")
    return plot_file

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Analyze growth experiment results")
    parser.add_argument("experiment_file", nargs='?', default=None, 
                       help="Path to experiment results JSON (or pattern)")
    
    args = parser.parse_args()
    
    # Create output directory for plots
    output_dir = Path("data/growth_experiments/plots")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Handle different input patterns
    experiment_files = []
    
    if args.experiment_file:
        if '*' in args.experiment_file:
            # It's a glob pattern
            experiment_files = glob.glob(args.experiment_file)
        else:
            # Single file
            experiment_files = [args.experiment_file]
    else:
        # No file specified, look for all JSON files in growth_experiments
        experiment_files = glob.glob("data/growth_experiments/*.json")
    
    if not experiment_files:
        print("❌ No experiment files found")
        print("Try running an experiment first:")
        print("  python scripts/run_growth_experiment.py")
        return
    
    print(f"Found {len(experiment_files)} experiment file(s)")
    
    all_results = []
    for exp_file in sorted(experiment_files):
        print(f"\n📊 Analyzing: {Path(exp_file).name}")
        try:
            results = load_experiment_results(exp_file)
            plot_file = create_simple_plots(results, output_dir)
            
            # Print summary statistics
            steps = results["growth_steps"]
            if steps:
                print(f"  Steps: {len(steps)}")
                
                # Growth statistics
                new_tiles = [s['new_tiles'] for s in steps]
                total_grown = sum(new_tiles)
                avg_growth = np.mean(new_tiles)
                print(f"  Total tiles grown: {total_grown}")
                print(f"  Average growth rate: {avg_growth:.1f} tiles/step")
                
                # Energy statistics
                energies = [s['total_energy'] for s in steps]
                energy_change = energies[-1] - energies[0]
                print(f"  Energy change: {energy_change:+.2f}")
                print(f"  Final energy: {energies[-1]:.2f}")
                
                # Acceptance statistics
                if 'acceptance_rate' in steps[0]:
                    acceptances = [s.get('acceptance_rate', 0) for s in steps]
                    avg_acceptance = np.mean(acceptances)
                    print(f"  Average acceptance rate: {avg_acceptance:.1%}")
                
                # Note about missing defect data
                if 'defect_count' not in steps[0]:
                    print("  ⚠️  No defect data available (check if vertex_class exists in tiling)")
                
                all_results.append(results)
                    
        except Exception as e:
            print(f"❌ Error analyzing {exp_file}: {e}")
            import traceback
            traceback.print_exc()
    
    # Overall comparison
    if len(all_results) > 1:
        print("\n" + "=" * 60)
        print("📈 COMPARISON OF ALL EXPERIMENTS")
        print("=" * 60)
        
        for results in all_results:
            exp_name = results.get("experiment_name", "Unknown")
            steps = results.get("growth_steps", [])
            if steps:
                last = steps[-1]
                print(f"\n{exp_name}:")
                print(f"  Final energy: {last['total_energy']:.2f}")
                print(f"  Growth rate: {last['new_tiles']} tiles")
                print(f"  Cumulative growth: {sum(s['new_tiles'] for s in steps)} tiles")

if __name__ == "__main__":
    main()
