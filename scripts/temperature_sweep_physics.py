#!/usr/bin/env python3
"""
Physics-focused temperature sweep for healing regime.
Creates separate config files for each temperature.
"""

import json
import subprocess
import sys
from pathlib import Path
import shutil

def create_temp_config(base_config, temperature, output_path):
    """Create temporary config with specified temperature"""
    with open(base_config, 'r') as f:
        config = f.read()
    
    # Replace temperature line
    lines = config.split('\n')
    new_lines = []
    for line in lines:
        if line.strip().startswith('temperature ='):
            new_lines.append(f'temperature = {temperature}')
        else:
            new_lines.append(line)
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(new_lines))
    
    print(f"  Created: {output_path.name} (T={temperature})")

def run_temperature_experiment(temperature, base_config_path):
    """Run experiment at specific temperature"""
    print(f"\n🌡️  Testing T={temperature}")
    
    # Create temp config
    temp_config = Path(f"configs/temp_T{temperature}.toml")
    create_temp_config(base_config_path, temperature, temp_config)
    
    # Run experiment
    cmd = [
        sys.executable, "scripts/run_growth_experiment.py",
        "--config", str(temp_config),
        "--name", f"temp_sweep_T{temperature}"
    ]
    
    print(f"  Running: {' '.join(cmd[-3:])}")  # Show only relevant part
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print(f"  ✅ Success")
            # Extract key metrics from output if possible
            for line in result.stdout.split('\n'):
                if 'Acceptance rate:' in line:
                    print(f"  {line.strip()}")
        else:
            print(f"  ❌ Failed (code: {result.returncode})")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
    
    except subprocess.TimeoutExpired:
        print(f"  ⏰ Timeout after 10 minutes")
    
    return temp_config

def analyze_temperature_sweep():
    """Analyze results from temperature sweep"""
    print("\n" + "="*60)
    print("📊 TEMPERATURE SWEEP ANALYSIS")
    print("="*60)
    
    # Find all temp sweep files
    results_dir = Path("data/growth_experiments")
    temp_files = list(results_dir.glob("temp_sweep_T*.json"))
    
    if not temp_files:
        print("No temperature sweep results found")
        return
    
    print(f"Found {len(temp_files)} temperature experiments")
    
    for file in sorted(temp_files):
        with open(file, 'r') as f:
            data = json.load(f)
        
        temp = data['config']['monte_carlo']['temperature']
        steps = data['growth_steps']
        
        if steps:
            # Calculate average metrics
            acceptances = [s['acceptance_rate'] for s in steps if 'acceptance_rate' in s]
            defects = [s['defect_count'] for s in steps if 'defect_count' in s]
            
            if acceptances and defects:
                avg_acceptance = sum(acceptances) / len(acceptances)
                avg_defects = sum(defects) / len(defects)
                
                print(f"\nT={temp}:")
                print(f"  Avg acceptance: {avg_acceptance:.1%}")
                print(f"  Avg defects: {avg_defects:.1f}")
                
                # Check defect trend
                if len(defects) >= 3:
                    trend = "↑" if defects[-1] > defects[0] else "↓" if defects[-1] < defects[0] else "→"
                    print(f"  Defect trend: {trend} ({defects[0]} → {defects[-1]})")

def main():
    """Main temperature sweep"""
    print("🌡️  TEMPERATURE SWEEP FOR HEALING REGIME")
    print("="*60)
    
    # Base config
    base_config = Path("configs/phase2_growth_experiments.toml")
    if not base_config.exists():
        print(f"❌ Base config not found: {base_config}")
        return
    
    # Test temperatures
    temperatures = [0.8, 1.0, 1.2, 1.5]
    print(f"Testing temperatures: {temperatures}")
    print(f"Base config: {base_config}")
    
    # Run experiments
    temp_configs = []
    for T in temperatures:
        config_file = run_temperature_experiment(T, base_config)
        temp_configs.append(config_file)
    
    # Analyze results
    analyze_temperature_sweep()
    
    # Cleanup temp configs
    print("\n🧹 Cleaning up temporary configs...")
    for config in temp_configs:
        if config.exists():
            config.unlink()
            print(f"  Removed: {config.name}")
    
    print("\n🎯 NEXT STEPS:")
    print("1. Choose temperature with:")
    print("   - Acceptance ~15-25%")
    print("   - Defects stable or decreasing")
    print("   - Some uphill accepts (positive_ratio > 0.1)")
    print("2. Run control (no MC) at chosen T")
    print("3. Test obstacles at chosen T")

if __name__ == "__main__":
    main()