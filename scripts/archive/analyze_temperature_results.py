#!/usr/bin/env python3
"""
Analyze temperature sweep results and suggest optimal T
"""

# --- Auto-fixed import path ---
import sys, os
# Adjust path to find 'src' from 'scripts/subfolder/'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path: sys.path.insert(0, project_root)
# ------------------------------

import json
from pathlib import Path
import glob

def load_experiment(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_experiment(exp_data):
    """Extract key physics metrics"""
    steps = exp_data.get('growth_steps', [])
    if not steps:
        return None
    
    # Collect metrics
    metrics = {
        'temperature': exp_data['config']['monte_carlo']['temperature'],
        'acceptance_rates': [],
        'defect_counts': [],
        'defect_changes': [],
        'positive_ratios': [],
        'energy_changes': []
    }
    
    for i, step in enumerate(steps):
        if 'acceptance_rate' in step:
            metrics['acceptance_rates'].append(step['acceptance_rate'])
        if 'defect_count' in step:
            metrics['defect_counts'].append(step['defect_count'])
        if 'positive_ratio' in step:
            metrics['positive_ratios'].append(step['positive_ratio'])
    
    # Calculate trends
    if len(metrics['defect_counts']) >= 2:
        metrics['defect_trend'] = metrics['defect_counts'][-1] - metrics['defect_counts'][0]
    
    # Averages
    if metrics['acceptance_rates']:
        metrics['avg_acceptance'] = sum(metrics['acceptance_rates']) / len(metrics['acceptance_rates'])
    
    if metrics['defect_counts']:
        metrics['avg_defects'] = sum(metrics['defect_counts']) / len(metrics['defect_counts'])
    
    if metrics['positive_ratios']:
        metrics['avg_uphill'] = sum(metrics['positive_ratios']) / len(metrics['positive_ratios'])
    
    return metrics

def main():
    print("🔬 TEMPERATURE SWEEP ANALYSIS")
    print("="*60)
    
    # Find all temperature sweep files
    files = glob.glob("data/growth_experiments/temp_sweep_T*.json")
    
    if not files:
        print("No temperature sweep files found.")
        print("Run: python scripts/temperature_sweep_physics.py")
        return
    
    results = []
    for file in sorted(files):
        exp_data = load_experiment(file)
        metrics = analyze_experiment(exp_data)
        if metrics:
            results.append(metrics)
    
    # Print comparison table
    print("\n📊 COMPARISON TABLE:")
    print("-" * 80)
    print(f"{'T':>5} {'Acceptance':>12} {'Defects':>10} {'Trend':>8} {'Uphill%':>10}")
    print("-" * 80)
    
    for r in sorted(results, key=lambda x: x['temperature']):
        trend_symbol = "↑" if r.get('defect_trend', 0) > 1 else "↓" if r.get('defect_trend', 0) < -1 else "→"
        
        print(f"{r['temperature']:5.1f} "
              f"{r.get('avg_acceptance', 0):11.1%} "
              f"{r.get('avg_defects', 0):10.1f} "
              f"{trend_symbol:>8} "
              f"{r.get('avg_uphill', 0)*100:9.1f}%")
    
    # Suggest optimal temperature
    print("\n🎯 OPTIMAL TEMPERATURE SUGGESTION:")
    
    # Criteria: 15-25% acceptance, defects decreasing, some uphill
    candidates = []
    for r in results:
        acceptance = r.get('avg_acceptance', 0)
        trend = r.get('defect_trend', 0)
        uphill = r.get('avg_uphill', 0)
        
        if 0.15 <= acceptance <= 0.25 and trend < 0 and uphill > 0.1:
            candidates.append((r['temperature'], acceptance, trend, uphill))
    
    if candidates:
        print("Found optimal temperatures:")
        for T, acc, trend, uphill in candidates:
            print(f"  T={T}: acceptance={acc:.1%}, "
                  f"defect Δ={trend:.1f}, uphill={uphill:.1%}")
        
        # Choose the one with best combination
        best = min(candidates, key=lambda x: abs(x[1] - 0.20))  # Closest to 20%
        print(f"\n💡 Recommended: T={best[0]}")
    else:
        print("No temperature meets all criteria.")
        print("Consider:")
        print("  - T with acceptance closest to 20%")
        print("  - T with most negative defect trend")
        print("  - T with uphill accepts ~10-30%")

if __name__ == "__main__":
    main()