#!/usr/bin/env python3
"""Quick verification of critical fixes before running diagnostics"""

import json
import time
import sys
sys.path.insert(0, '.')

print("🔍 QUICK VERIFICATION OF CRITICAL FIXES")
print("=" * 60)

# Test 1: Energy reproducibility
print("\n1. Testing energy reproducibility...")
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.utils.energy_utils import compute_total_energy_fresh

with open('data/processed/penrose_tiling_energy_initialized.json') as f:
    tiling = json.load(f)

energy_model = WidomInspiredEnergy(EnergyParameters())

# Compute energy twice
E1 = compute_total_energy_fresh(energy_model, tiling)
E2 = compute_total_energy_fresh(energy_model, tiling)
drift = abs(E1 - E2)

print(f"   First computation: {E1:.6f}")
print(f"   Second computation: {E2:.6f}")
print(f"   Energy drift: {drift:.6f}")

if drift > 0.001:
    print("   ❌ FAIL: Energy drift too high (> 0.001)")
    sys.exit(1)
else:
    print("   ✅ PASS: Energy reproducible")

# Test 2: Check for nested loop bug
print("\n2. Checking diagnose_energy_landscape_fixed.py...")
with open('scripts/diagnose_energy_landscape_fixed.py') as f:
    content = f.read()
    
# Count number of 'for i, hexagon in enumerate(sample_hexagons):' lines
loop_count = content.count('for i, hexagon in enumerate(sample_hexagons):')
if loop_count > 1:
    print(f"   ❌ FAIL: Found {loop_count} nested loops (should be 1)")
    sys.exit(1)
else:
    print("   ✅ PASS: No nested loop bug")

# Test 3: Check FlipEngine verbose parameter
print("\n3. Checking FlipEngine verbose parameter...")
try:
    from src.simulation.flip_engine import FlipEngine
    from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
    
    classifier = CombinatorialVertexClassifier()
    energy_model2 = WidomInspiredEnergy(EnergyParameters())
    flip_engine = FlipEngine(classifier, energy_model2, verbose=False)
    print("   ✅ PASS: FlipEngine accepts verbose=False")
except TypeError as e:
    print(f"   ❌ FAIL: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ ALL CRITICAL FIXES VERIFIED!")
print("You can now run diagnostics with confidence.")