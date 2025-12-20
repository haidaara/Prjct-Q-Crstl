# scripts/test_mc_quick.py
#!/usr/bin/env python3
"""
Quick MC test with minimal output
"""

import json
from pathlib import Path
import sys

def mc_quick_test(temperature: float = 1.0, steps: int = 200):
    """Run quick MC test"""
    print(f"⚡ Quick MC Test (T={temperature}, {steps} steps)")
    print("=" * 40)
    
    import os, sys
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)

    # Load data
    data_path = Path("data/processed/penrose_tiling_energy_initialized.json")
    with open(data_path, 'r') as f:
        tiling_data = json.load(f)
    
    # Import
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    from src.energy.widom_inspired_energy import WidomInspiredEnergy
    from src.simulation.flip_engine import FlipEngine
    from src.simulation.mc_engine import MonteCarloEngine
    
    # Setup
    classifier = CombinatorialVertexClassifier()
    energy_model = WidomInspiredEnergy()
    flip_engine = FlipEngine(classifier, energy_model)
    mc = MonteCarloEngine(temperature=temperature, energy_model=energy_model, flip_engine=flip_engine)
    
    # Initialize
    mc.initialize_energy(tiling_data)
    initial_energy = mc.current_energy
    print(f"Initial energy: {initial_energy:.3f}")
    
    # Run steps
    accepted = 0
    energies = []
    deltas = []
    
    print("Running steps... ", end="")
    sys.stdout.flush()
    
    for step in range(steps):
        a, delta = mc.run_step(tiling_data)
        if a:
            accepted += 1
            deltas.append(delta)
        energies.append(mc.current_energy)
        
        # Progress every 40 steps
        if steps > 100 and (step + 1) % (steps // 5) == 0:
            print(f"{step + 1}... ", end="")
            sys.stdout.flush()
    
    print("done!")
    
    # Analysis
    acceptance_rate = accepted / steps
    final_energy = mc.current_energy
    energy_change = final_energy - initial_energy
    
    # Energy drift rate (per step)
    drift_rate = energy_change / steps
    
    print(f"\n📊 Results:")
    print(f"  Acceptance rate: {acceptance_rate:.1%}")
    print(f"  Final energy: {final_energy:.3f}")
    print(f"  Energy change: {energy_change:+.3f}")
    print(f"  Drift per step: {drift_rate:+.6f}")
    
    if deltas:
        import statistics
        avg_delta = statistics.mean(deltas)
        std_delta = statistics.stdev(deltas) if len(deltas) > 1 else 0
        positive_ratio = sum(1 for d in deltas if d > 0) / len(deltas)
        
        print(f"  Avg ΔE: {avg_delta:.3f} ± {std_delta:.3f}")
        print(f"  Positive ΔE moves: {positive_ratio:.1%}")
    
    # Determine regime
    if acceptance_rate < 0.1:
        regime = "❄️ Too cold (mostly downhill)"
        recommendation = "Increase temperature to ~1.0-2.0"
    elif acceptance_rate < 0.3:
        regime = "🧊 Good for healing"
        recommendation = "Perfect for error-and-repair experiments"
    elif acceptance_rate < 0.6:
        regime = "🌡️ Good for mixing"
        recommendation = "Good for equilibrium sampling"
    else:
        regime = "🔥 Too hot"
        recommendation = "Decrease temperature to ~0.3-1.0"
    
    print(f"\n💡 Assessment: {regime}")
    print(f"   {recommendation}")
    
    # Save quick results
    results = {
        "temperature": temperature,
        "steps": steps,
        "acceptance_rate": acceptance_rate,
        "initial_energy": initial_energy,
        "final_energy": final_energy,
        "energy_change": energy_change,
        "regime": regime,
        "recommendation": recommendation
    }
    
    output_path = Path(f"data/experiments/mc_test_T{temperature}.json")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Results saved to: {output_path}")
    
    return results

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Quick MC test")
    parser.add_argument("--temperature", "-T", type=float, default=1.0,
                       help="Temperature for MC test")
    parser.add_argument("--steps", "-s", type=int, default=200,
                       help="Number of MC steps")
    
    args = parser.parse_args()
    
    try:
        results = mc_quick_test(args.temperature, args.steps)
        exit(0 if results["acceptance_rate"] > 0.05 else 1)  # At least 5% acceptance
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)