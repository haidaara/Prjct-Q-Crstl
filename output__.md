randa@Randa:quasi-phason$ python scripts/quick_verify_fixes.py
🔍 QUICK VERIFICATION OF CRITICAL FIXES
============================================================

1. Testing energy reproducibility...
   First computation: 307.855000
   Second computation: 307.855000
   Energy drift: 0.000000
   ✅ PASS: Energy reproducible

2. Checking diagnose_energy_landscape_fixed.py...
   ✅ PASS: No nested loop bug

3. Checking FlipEngine verbose parameter...
   ✅ PASS: FlipEngine accepts verbose=False

============================================================
✅ ALL CRITICAL FIXES VERIFIED!
You can now run diagnostics with confidence.
randa@Randa:quasi-phason$ python scripts/diagnose_energy_landscape_fixed.py

============================================================
Testing with neighborhood radius = 2
============================================================

🎯 DIAGNOSTIC 2 (FIXED): ΔE DISTRIBUTION WITH ENERGY CONSISTENCY
============================================================
📏 Penrose edge length: 1.000000 (from 524 valid edges)
Analyzing 100 flips with radius=2...
  Progress: 0/100
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
  Progress: 50/100
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

📊 ΔE STATISTICS (n=100, radius=2):
  Mean: +5.554487
  Std:  3.038934
  Min:  -0.300000
  Max:  +9.196667

📊 PROPOSAL DISTRIBUTION:
  downhill: 13/100 (13.0%)
  uphill: 87/100 (87.0%)
  neutral: 0/100 (0.0%)

📈 Plot saved: data/diagnostics/delta_E_distribution_fixed.png

============================================================
Testing with neighborhood radius = 3
============================================================

🎯 DIAGNOSTIC 2 (FIXED): ΔE DISTRIBUTION WITH ENERGY CONSISTENCY
============================================================
📏 Penrose edge length: 1.000000 (from 524 valid edges)
Analyzing 100 flips with radius=3...
  Progress: 0/100
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
  Progress: 50/100
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 ΔE STATISTICS (n=100, radius=3):
  Mean: +5.866827
  Std:  3.000261
  Min:  -0.300000
  Max:  +9.246667

📊 PROPOSAL DISTRIBUTION:
  downhill: 9/100 (9.0%)
  uphill: 91/100 (91.0%)
  neutral: 0/100 (0.0%)

📈 Plot saved: data/diagnostics/delta_E_distribution_fixed.png

============================================================
Testing with neighborhood radius = 4
============================================================

🎯 DIAGNOSTIC 2 (FIXED): ΔE DISTRIBUTION WITH ENERGY CONSISTENCY
============================================================
📏 Penrose edge length: 1.000000 (from 524 valid edges)
Analyzing 100 flips with radius=4...
  Progress: 0/100
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
  Progress: 50/100
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 ΔE STATISTICS (n=100, radius=4):
  Mean: +5.868153
  Std:  2.815803
  Min:  -0.300000
  Max:  +9.246667

📊 PROPOSAL DISTRIBUTION:
  downhill: 7/100 (7.0%)
  uphill: 93/100 (93.0%)
  neutral: 0/100 (0.0%)

📈 Plot saved: data/diagnostics/delta_E_distribution_fixed.png
randa@Randa:quasi-phason$ python scripts/test_manual_defects.py
Traceback (most recent call last):
  File "/mnt/c/Users/randa chames/Downloads/aberration-master/interns_&_project_&_conf/Prjct_Q-Crstl/quasi-phason/scripts/test_manual_defects.py", line 15, in <module>
    from src.utils.energy_utils import compute_total_energy_fresh, wipe_all_energy_fields, clear_all_caches
ModuleNotFoundError: No module named 'src'
randa@Randa:quasi-phason$ python scripts/test_manual_defects.py
🧪 TESTING MC HEALING WITH REAL GEOMETRIC DEFECTS
============================================================

🎯 DIAGNOSTIC 3: MC HEALING (T=0.1, steps=100)
============================================================
  Creating 15 REAL geometric defects...
📏 Penrose edge length: 1.000000 (from 524 valid edges)
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #1: ΔE = +5.87 (hexagon [972, 973, 2517])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #2: ΔE = +5.87 (hexagon [3424, 3425, 4162])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #3: ΔE = +4.95 (hexagon [909, 910, 2299])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #4: ΔE = +8.20 (hexagon [2188, 2189, 3373])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #5: ΔE = +3.91 (hexagon [606, 607, 2343])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #6: ΔE = +3.91 (hexagon [914, 915, 2246])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #7: ΔE = +3.60 (hexagon [1123, 1124, 4053])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #8: ΔE = +2.60 (hexagon [1043, 1044, 2573])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #9: ΔE = +2.01 (hexagon [1051, 1052, 3381])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #10: ΔE = +2.15 (hexagon [2134, 2135, 3372])
❌ Invalid hexagon: 8 boundary, 2 internal
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #11: ΔE = +9.15 (hexagon [3567, 3568, 4111])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #12: ΔE = +9.21 (hexagon [1125, 1126, 2467])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #13: ΔE = +5.03 (hexagon [906, 907, 4134])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #14: ΔE = +0.99 (hexagon [2522, 2523, 3337])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #15: ΔE = +5.87 (hexagon [1058, 1059, 4105])
  Created 15 real geometric defects
Active region: 454 tiles
Initial defects (energy > 1.5): 20
Average defect energy: 2.00
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 RESULTS:
  Defects: 20 → 19 (Δ=+1)
  Healing efficiency: +5.0%
  Avg defect energy: 2.00 → 2.00
  Energy change: -16.44
  Acceptance rate: 16.0%
  Avg flippable hexagons: 188.1
  Energy consistency drift: 2.016368

🔍 INVARIANT CHECKS:
  ❌ Energy inconsistent! Drift = 2.0164

🎯 INTERPRETATION:
  ✅ REAL HEALING DETECTED: 1 defects removed
     Efficiency: 5.0%
  ✅ MC is active (acceptance: 16.0%)

🎯 DIAGNOSTIC 3: MC HEALING (T=0.3, steps=100)
============================================================
  Creating 15 REAL geometric defects...
📏 Penrose edge length: 1.000000 (from 524 valid edges)
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #1: ΔE = +1.66 (hexagon [2515, 2516, 3475])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #2: ΔE = +3.61 (hexagon [3608, 3609, 4138])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #3: ΔE = +10.10 (hexagon [676, 677, 3607])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #4: ΔE = +3.66 (hexagon [1043, 1044, 2573])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #5: ΔE = +3.61 (hexagon [1123, 1124, 4053])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #6: ΔE = +5.92 (hexagon [3334, 3335, 4079])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #7: ΔE = +9.10 (hexagon [910, 911, 2300])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #8: ΔE = +5.96 (hexagon [2459, 2460, 3521])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #9: ΔE = +2.85 (hexagon [1199, 1200, 2469])
❌ Invalid hexagon: 8 boundary, 2 internal
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #10: ΔE = +6.91 (hexagon [2194, 2195, 4158])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #11: ΔE = +8.25 (hexagon [894, 895, 2570])
❌ Invalid hexagon: 8 boundary, 2 internal
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #12: ΔE = +1.70 (hexagon [833, 834, 4162])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #13: ΔE = +4.22 (hexagon [1121, 1122, 2520])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #14: ΔE = +2.21 (hexagon [1053, 1054, 2411])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #15: ΔE = +5.86 (hexagon [1058, 1059, 4105])
  Created 15 real geometric defects
Active region: 454 tiles
Initial defects (energy > 1.5): 21
Average defect energy: 2.01
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 RESULTS:
  Defects: 21 → 15 (Δ=+6)
  Healing efficiency: +28.6%
  Avg defect energy: 2.01 → 2.00
  Energy change: -22.80
  Acceptance rate: 23.0%
  Avg flippable hexagons: 195.5
  Energy consistency drift: 0.042000

🔍 INVARIANT CHECKS:
  ❌ Energy inconsistent! Drift = 0.0420

🎯 INTERPRETATION:
  ✅ REAL HEALING DETECTED: 6 defects removed
     Efficiency: 28.6%
  ✅ MC is active (acceptance: 23.0%)

🎯 DIAGNOSTIC 3: MC HEALING (T=1.0, steps=100)
============================================================
  Creating 15 REAL geometric defects...
📏 Penrose edge length: 1.000000 (from 524 valid edges)
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #1: ΔE = +5.87 (hexagon [844, 845, 2135])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #2: ΔE = +5.87 (hexagon [2304, 2305, 3285])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #3: ΔE = +5.86 (hexagon [1054, 1055, 2412])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #4: ΔE = +3.61 (hexagon [3377, 3378, 4133])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #5: ΔE = +6.91 (hexagon [2457, 2458, 4137])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #6: ΔE = +5.87 (hexagon [992, 993, 2194])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #7: ΔE = +6.11 (hexagon [1061, 1062, 3284])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #8: ΔE = +4.23 (hexagon [2192, 2193, 3281])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #9: ΔE = +4.03 (hexagon [989, 990, 4159])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #10: ΔE = +4.86 (hexagon [915, 916, 3328])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #11: ΔE = +7.22 (hexagon [754, 755, 4164])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #12: ΔE = +4.81 (hexagon [607, 608, 2344])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #13: ΔE = +9.20 (hexagon [2522, 2523, 3337])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
❌ Invalid hexagon: 10 boundary, 1 internal
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #14: ΔE = +1.80 (hexagon [3332, 3333, 4106])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #15: ΔE = +4.06 (hexagon [610, 611, 2290])
  Created 15 real geometric defects
Active region: 454 tiles
Initial defects (energy > 1.5): 25
Average defect energy: 2.00
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 RESULTS:
  Defects: 25 → 15 (Δ=+10)
  Healing efficiency: +40.0%
  Avg defect energy: 2.00 → 2.01
  Energy change: -22.76
  Acceptance rate: 31.0%
  Avg flippable hexagons: 190.7
  Energy consistency drift: 0.073816

🔍 INVARIANT CHECKS:
  ❌ Energy inconsistent! Drift = 0.0738

🎯 INTERPRETATION:
  ✅ REAL HEALING DETECTED: 10 defects removed
     Efficiency: 40.0%
  ✅ MC is active (acceptance: 31.0%)

🎯 DIAGNOSTIC 3: MC HEALING (T=2.0, steps=100)
============================================================
  Creating 15 REAL geometric defects...
📏 Penrose edge length: 1.000000 (from 524 valid edges)
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #1: ΔE = +8.20 (hexagon [2290, 2291, 3561])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #2: ΔE = +6.91 (hexagon [751, 752, 3565])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #3: ΔE = +9.13 (hexagon [3567, 3568, 4111])
❌ Invalid hexagon: 8 boundary, 2 internal
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #4: ΔE = +9.10 (hexagon [3430, 3431, 4054])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #5: ΔE = +1.95 (hexagon [608, 609, 4218])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #6: ΔE = +3.91 (hexagon [2408, 2409, 3427])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #7: ΔE = +6.91 (hexagon [2298, 2299, 4161])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #8: ΔE = +7.06 (hexagon [3476, 3477, 4055])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #9: ΔE = +7.14 (hexagon [831, 832, 2350])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #10: ΔE = +5.81 (hexagon [901, 902, 3473])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #11: ΔE = +3.72 (hexagon [2410, 2411, 3380])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #12: ΔE = +5.87 (hexagon [1199, 1200, 2469])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #13: ΔE = +0.56 (hexagon [1051, 1052, 3381])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #14: ΔE = +6.14 (hexagon [1120, 1121, 3384])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #15: ΔE = +9.22 (hexagon [897, 898, 2514])
  Created 15 real geometric defects
Active region: 454 tiles
Initial defects (energy > 1.5): 28
Average defect energy: 2.02
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 RESULTS:
  Defects: 28 → 31 (Δ=-3)
  Healing efficiency: -10.7%
  Avg defect energy: 2.02 → 2.02
  Energy change: +12.37
  Acceptance rate: 46.0%
  Avg flippable hexagons: 179.8
  Energy consistency drift: 2.375632

🔍 INVARIANT CHECKS:
  ❌ Energy inconsistent! Drift = 2.3756

🎯 INTERPRETATION:
  ❌ NEGATIVE HEALING: Defects increased by 3

🎯 DIAGNOSTIC 3: MC HEALING (T=5.0, steps=100)
============================================================
  Creating 15 REAL geometric defects...
📏 Penrose edge length: 1.000000 (from 524 valid edges)
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #1: ΔE = +9.10 (hexagon [3476, 3477, 4055])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #2: ΔE = +5.87 (hexagon [3424, 3425, 4162])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #3: ΔE = +3.61 (hexagon [3608, 3609, 4138])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #4: ΔE = +9.20 (hexagon [2522, 2523, 3337])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #5: ΔE = +4.06 (hexagon [2349, 2350, 3470])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #6: ΔE = +6.23 (hexagon [894, 895, 2570])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #7: ΔE = +4.22 (hexagon [747, 748, 2510])
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #8: ΔE = +4.83 (hexagon [759, 760, 2294])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #9: ΔE = +3.98 (hexagon [686, 687, 3515])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #10: ΔE = +3.91 (hexagon [2136, 2137, 3326])
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #11: ΔE = +3.91 (hexagon [1052, 1053, 4079])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #12: ΔE = +6.95 (hexagon [2344, 2345, 3562])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #13: ΔE = +5.12 (hexagon [2463, 2464, 3429])
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
    Defect #14: ΔE = +5.60 (hexagon [2291, 2292, 4217])
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
    Defect #15: ΔE = +1.95 (hexagon [973, 974, 4081])
  Created 15 real geometric defects
Active region: 454 tiles
Initial defects (energy > 1.5): 21
Average defect energy: 2.02
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

📊 RESULTS:
  Defects: 21 → 37 (Δ=-16)
  Healing efficiency: -76.2%
  Avg defect energy: 2.02 → 2.01
  Energy change: +43.19
  Acceptance rate: 71.0%
  Avg flippable hexagons: 179.9
  Energy consistency drift: 3.270203

🔍 INVARIANT CHECKS:
  ❌ Energy inconsistent! Drift = 3.2702

🎯 INTERPRETATION:
  ❌ NEGATIVE HEALING: Defects increased by 16

================================================================================
📈 TEMPERATURE DEPENDENCE SUMMARY:
================================================================================
Temp | Defects Before→After | Healing | Efficiency | Accept% | Avg Flippable
--------------------------------------------------------------------------------
T= 0.1 |  20→19  | ✅  +1 |      5.0% |   16.0% |  188.1
T= 0.3 |  21→15  | ✅  +6 |     28.6% |   23.0% |  195.5
T= 1.0 |  25→15  | ✅ +10 |     40.0% |   31.0% |  190.7
T= 2.0 |  28→31  | ❌  -3 |    -10.7% |   46.0% |  179.8
T= 5.0 |  21→37  | ❌ -16 |    -76.2% |   71.0% |  179.9

🎯 OPTIMAL: T=1.0 (efficiency=40.0%)
randa@Randa:quasi-phason$


