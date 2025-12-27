randa@Randa:quasi-phason$ time python scripts/experiments/03_run_healing_test.py
🧪 EXPERIMENT 03: PHASON HEALING (Refactored)
============================================================
📥 Input tiling: data/processed/penrose_tiling_energy_initialized.json
📤 Output dir : data/experiments/healing/healing_base_run_001
⚙️  scenario=base seed_radius=10.0 num_defects=15 defect_threshold=1.0
⚙️  MC: T=0.1 steps=3000 R=3 verify_energy=True base_steps=100
------------------------------------------------------------
⚡ DAMAGE PHASE: Heating (T=5.0) to create 15 energetic defects...
✅ MC sweep: 50/50 accepted (100.0%), max drift: 0.000000
   🔥 Heating Step 50: High-Energy Tiles=94 (Target: 15)
✅ DAMAGE COMPLETE: Scrambled. Starting Count: 94 Defects.
📸 SNAPSHOT SAVED: data/experiments/healing/healing_base_run_001/healing_damaged_state_1766773651.json
🩺 SWITCHING TO ANNEALING: 7 Stages
   📅 Schedule: [5.0, 2.5, 1.2, 0.6, 0.3, 0.15, 0.05]
   ℹ️  Allocation: [429, 429, 429, 429, 428, 428, 428] steps/stage

🌡️ STAGE 1/7: Cooling to T=5.0 (429 steps)...
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 10/3000 | Stage 10/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 20/3000 | Stage 20/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 30/3000 | Stage 30/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 40/3000 | Stage 40/429 | T=5.0 | Acc=10
🔁 Step 50: cluster=[906, 907, 4134] ΔE=+0.050000 accept=True
    core_region=3 delta_region=58 | E_before=1.600001 E_after=1.650001
    Tile-level changes (top 6 by |ΔE|):
      id=  980 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4134 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  906 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3426 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0050.json (T=5.0)
   ⏳ Global 50/3000 | Stage 50/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 60/3000 | Stage 60/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 70/3000 | Stage 70/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 80/3000 | Stage 80/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 90/3000 | Stage 90/429 | T=5.0 | Acc=8
🔁 Step 100: cluster=[751, 752, 3565] ΔE=-0.050000 accept=True
    core_region=3 delta_region=60 | E_before=2.502000 E_after=2.452001
    Tile-level changes (top 6 by |ΔE|):
      id=  751 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  753 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  750 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2457 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  752 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4165 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0100.json (T=5.0)
   ⏳ Global 100/3000 | Stage 100/429 | T=5.0 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 110/3000 | Stage 110/429 | T=5.0 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 120/3000 | Stage 120/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 130/3000 | Stage 130/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 140/3000 | Stage 140/429 | T=5.0 | Acc=8
🔁 Step 150: cluster=[1127, 2467, 2468] ΔE=+1.458000 accept=True
    core_region=3 delta_region=59 | E_before=2.000001 E_after=3.458000
    Tile-level changes (top 6 by |ΔE|):
      id= 1128 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1127 THIN->THICK move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2469 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4052 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2467 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1126 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0150.json (T=5.0)
   ⏳ Global 150/3000 | Stage 150/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 160/3000 | Stage 160/429 | T=5.0 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 170/3000 | Stage 170/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 180/3000 | Stage 180/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 190/3000 | Stage 190/429 | T=5.0 | Acc=10
🔁 Step 200: cluster=[2403, 2404, 3519] ΔE=+0.050000 accept=True
    core_region=3 delta_region=60 | E_before=2.750000 E_after=2.800000
    Tile-level changes (top 6 by |ΔE|):
      id= 2403 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  829 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3520 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  753 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2404 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THIN->THIN move= 0.8090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0200.json (T=5.0)
   ⏳ Global 200/3000 | Stage 200/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 210/3000 | Stage 210/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 220/3000 | Stage 220/429 | T=5.0 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 230/3000 | Stage 230/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 240/3000 | Stage 240/429 | T=5.0 | Acc=10
🔁 Step 250: cluster=[607, 608, 3562] ΔE=+0.000000 accept=True
    core_region=3 delta_region=54 | E_before=2.105000 E_after=2.105000
    Tile-level changes (top 6 by |ΔE|):
      id= 3562 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  608 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2344 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  607 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4218 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  609 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0250.json (T=5.0)
   ⏳ Global 250/3000 | Stage 250/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 260/3000 | Stage 260/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 270/3000 | Stage 270/429 | T=5.0 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 280/3000 | Stage 280/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 290/3000 | Stage 290/429 | T=5.0 | Acc=10
🔁 Step 300: cluster=[977, 978, 2409] ΔE=+0.050000 accept=True
    core_region=3 delta_region=58 | E_before=4.510000 E_after=4.560000
    Tile-level changes (top 6 by |ΔE|):
      id=  903 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2409 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  978 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  979 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3428 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2408 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0300.json (T=5.0)
   ⏳ Global 300/3000 | Stage 300/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 310/3000 | Stage 310/429 | T=5.0 | Acc=10
^[[B✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 320/3000 | Stage 320/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 330/3000 | Stage 330/429 | T=5.0 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 340/3000 | Stage 340/429 | T=5.0 | Acc=9
🔁 Step 350: cluster=[894, 895, 2570] ΔE=+0.000000 accept=True
    core_region=3 delta_region=59 | E_before=2.600000 E_after=2.600000
    Tile-level changes (top 6 by |ΔE|):
      id=  894 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2570 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3523 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  969 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  895 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2569 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0350.json (T=5.0)
   ⏳ Global 350/3000 | Stage 350/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 360/3000 | Stage 360/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 370/3000 | Stage 370/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 380/3000 | Stage 380/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 390/3000 | Stage 390/429 | T=5.0 | Acc=10
🔁 Step 400: cluster=[760, 3516, 4190] ΔE=+1.058000 accept=True
    core_region=3 delta_region=55 | E_before=4.270000 E_after=5.328000
    Tile-level changes (top 6 by |ΔE|):
      id=  760 THICK->THICK move= 0.3090 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4190 THIN->THICK move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2294 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  761 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3516 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  759 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0400.json (T=5.0)
   ⏳ Global 400/3000 | Stage 400/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 410/3000 | Stage 410/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 420/3000 | Stage 420/429 | T=5.0 | Acc=10
✅ MC sweep: 8/9 accepted (88.9%), max drift: 0.000000
   ⏳ Global 429/3000 | Stage 429/429 | T=5.0 | Acc=8

🌡️ STAGE 2/7: Cooling to T=2.5 (429 steps)...
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 439/3000 | Stage 10/429 | T=2.5 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 449/3000 | Stage 20/429 | T=2.5 | Acc=10
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0459.json (T=2.5)
   ⏳ Global 459/3000 | Stage 30/429 | T=2.5 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 469/3000 | Stage 40/429 | T=2.5 | Acc=8
🔁 Step 50: cluster=[3419, 3420, 4241] ΔE=-0.000000 accept=True
    core_region=3 delta_region=57 | E_before=3.608000 E_after=3.608000
    Tile-level changes (top 6 by |ΔE|):
      id= 3420 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  693 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4241 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3419 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  768 THICK->THICK move= 0.0000 E:  0.0520-> 0.0520 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  694 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 479/3000 | Stage 50/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 489/3000 | Stage 60/429 | T=2.5 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 499/3000 | Stage 70/429 | T=2.5 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0509.json (T=2.5)
   ⏳ Global 509/3000 | Stage 80/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 519/3000 | Stage 90/429 | T=2.5 | Acc=9
🔁 Step 100: cluster=[3564, 3565, 4165] ΔE=+0.300000 accept=False
    core_region=3 delta_region=56 | E_before=1.750001 E_after=2.050001
    Tile-level changes (top 6 by |ΔE|):
      id= 3564 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2401 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2400 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3565 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4165 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2402 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 529/3000 | Stage 100/429 | T=2.5 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 539/3000 | Stage 110/429 | T=2.5 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 549/3000 | Stage 120/429 | T=2.5 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0559.json (T=2.5)
   ⏳ Global 559/3000 | Stage 130/429 | T=2.5 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 569/3000 | Stage 140/429 | T=2.5 | Acc=10
🔁 Step 150: cluster=[760, 3516, 4190] ΔE=-1.008000 accept=True
    core_region=3 delta_region=55 | E_before=3.558000 E_after=2.550000
    Tile-level changes (top 6 by |ΔE|):
      id=  760 THICK->THICK move= 0.3090 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3517 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2294 THIN->THIN move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3516 THIN->THICK move= 0.5878 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  761 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4190 THICK->THIN move= 0.5878 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 579/3000 | Stage 150/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 589/3000 | Stage 160/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 599/3000 | Stage 170/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0609.json (T=2.5)
   ⏳ Global 609/3000 | Stage 180/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 619/3000 | Stage 190/429 | T=2.5 | Acc=9
🔁 Step 200: cluster=[831, 833, 834] ΔE=+0.000000 accept=True
    core_region=3 delta_region=57 | E_before=4.566000 E_after=4.566000
    Tile-level changes (top 6 by |ΔE|):
      id= 3470 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  833 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3425 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4161 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 629/3000 | Stage 200/429 | T=2.5 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 639/3000 | Stage 210/429 | T=2.5 | Acc=7
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 649/3000 | Stage 220/429 | T=2.5 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0659.json (T=2.5)
   ⏳ Global 659/3000 | Stage 230/429 | T=2.5 | Acc=7
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 669/3000 | Stage 240/429 | T=2.5 | Acc=10
🔁 Step 250: cluster=[3522, 4110, 4137] ΔE=+0.050000 accept=True
    core_region=3 delta_region=59 | E_before=5.976000 E_after=6.026000
    Tile-level changes (top 6 by |ΔE|):
      id= 2457 THIN->THIN move= 0.0000 E:  0.0020-> 0.0520 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  824 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  823 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4110 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3521 THICK->THICK move= 0.0000 E:  0.0520-> 0.0520 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4137 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 679/3000 | Stage 250/429 | T=2.5 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 689/3000 | Stage 260/429 | T=2.5 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 699/3000 | Stage 270/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0709.json (T=2.5)
   ⏳ Global 709/3000 | Stage 280/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 719/3000 | Stage 290/429 | T=2.5 | Acc=9
🔁 Step 300: cluster=[2357, 3332, 4106] ΔE=-0.050000 accept=True
    core_region=3 delta_region=55 | E_before=3.308001 E_after=3.258001
    Tile-level changes (top 6 by |ΔE|):
      id=  984 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1058 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4106 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2357 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3332 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 729/3000 | Stage 300/429 | T=2.5 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 739/3000 | Stage 310/429 | T=2.5 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 749/3000 | Stage 320/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0759.json (T=2.5)
   ⏳ Global 759/3000 | Stage 330/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 769/3000 | Stage 340/429 | T=2.5 | Acc=9
🔁 Step 350: cluster=[835, 3422, 4189] ΔE=-0.299999 accept=True
    core_region=3 delta_region=51 | E_before=2.355000 E_after=2.055001
    Tile-level changes (top 6 by |ΔE|):
      id= 3468 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3469 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  836 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  835 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  762 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4189 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 779/3000 | Stage 350/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 789/3000 | Stage 360/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 799/3000 | Stage 370/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0809.json (T=2.5)
   ⏳ Global 809/3000 | Stage 380/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 819/3000 | Stage 390/429 | T=2.5 | Acc=9
🔁 Step 400: cluster=[760, 3516, 4190] ΔE=+1.058000 accept=True
    core_region=3 delta_region=55 | E_before=3.554000 E_after=4.612000
    Tile-level changes (top 6 by |ΔE|):
      id=  760 THICK->THICK move= 0.3090 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4190 THIN->THICK move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3516 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2294 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  761 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  684 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 829/3000 | Stage 400/429 | T=2.5 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 839/3000 | Stage 410/429 | T=2.5 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 849/3000 | Stage 420/429 | T=2.5 | Acc=7
✅ MC sweep: 4/9 accepted (44.4%), max drift: 0.000000
   📸 Snapshot: healing_step_0858.json (T=2.5)
   ⏳ Global 858/3000 | Stage 429/429 | T=2.5 | Acc=4

🌡️ STAGE 3/7: Cooling to T=1.2 (429 steps)...
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 868/3000 | Stage 10/429 | T=1.2 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 878/3000 | Stage 20/429 | T=1.2 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 888/3000 | Stage 30/429 | T=1.2 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 898/3000 | Stage 40/429 | T=1.2 | Acc=8
🔁 Step 50: cluster=[915, 3282, 4159] ΔE=+1.158000 accept=False
    core_region=3 delta_region=59 | E_before=4.714000 E_after=5.872000
    Tile-level changes (top 6 by |ΔE|):
      id= 4160 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3282 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  915 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  988 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2247 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2248 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0908.json (T=1.2)
   ⏳ Global 908/3000 | Stage 50/429 | T=1.2 | Acc=5
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 918/3000 | Stage 60/429 | T=1.2 | Acc=7
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 928/3000 | Stage 70/429 | T=1.2 | Acc=10
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 938/3000 | Stage 80/429 | T=1.2 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 948/3000 | Stage 90/429 | T=1.2 | Acc=6
🔁 Step 100: cluster=[909, 2299, 3424] ΔE=-0.050000 accept=True
    core_region=3 delta_region=59 | E_before=5.978000 E_after=5.928000
    Tile-level changes (top 6 by |ΔE|):
      id= 3424 THICK->THIN move= 0.5878 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  910 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3425 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  909 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2299 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  912 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0958.json (T=1.2)
   ⏳ Global 958/3000 | Stage 100/429 | T=1.2 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 968/3000 | Stage 110/429 | T=1.2 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 978/3000 | Stage 120/429 | T=1.2 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 988/3000 | Stage 130/429 | T=1.2 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 998/3000 | Stage 140/429 | T=1.2 | Acc=7
🔁 Step 150: cluster=[981, 984, 3333] ΔE=-0.050000 accept=True
    core_region=3 delta_region=55 | E_before=2.102001 E_after=2.052001
    Tile-level changes (top 6 by |ΔE|):
      id= 1058 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2355 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1057 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2357 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2354 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  984 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1008.json (T=1.2)
   ⏳ Global 1008/3000 | Stage 150/429 | T=1.2 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1018/3000 | Stage 160/429 | T=1.2 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1028/3000 | Stage 170/429 | T=1.2 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1038/3000 | Stage 180/429 | T=1.2 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1048/3000 | Stage 190/429 | T=1.2 | Acc=8
🔁 Step 200: cluster=[904, 2407, 3427] ΔE=-0.000000 accept=True
    core_region=3 delta_region=55 | E_before=3.360000 E_after=3.360000
    Tile-level changes (top 6 by |ΔE|):
      id= 3473 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3426 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2408 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2407 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3427 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3472 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1058.json (T=1.2)
   ⏳ Global 1058/3000 | Stage 200/429 | T=1.2 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1068/3000 | Stage 210/429 | T=1.2 | Acc=7
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1078/3000 | Stage 220/429 | T=1.2 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1088/3000 | Stage 230/429 | T=1.2 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1098/3000 | Stage 240/429 | T=1.2 | Acc=7
🔁 Step 250: cluster=[1055, 1056, 4079] ΔE=-0.050000 accept=True
    core_region=3 delta_region=55 | E_before=2.956002 E_after=2.906002
    Tile-level changes (top 6 by |ΔE|):
      id= 1054 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3287 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1056 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1057 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4079 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2412 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1108.json (T=1.2)
   ⏳ Global 1108/3000 | Stage 250/429 | T=1.2 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1118/3000 | Stage 260/429 | T=1.2 | Acc=6
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1128/3000 | Stage 270/429 | T=1.2 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1138/3000 | Stage 280/429 | T=1.2 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1148/3000 | Stage 290/429 | T=1.2 | Acc=7
🔁 Step 300: cluster=[1049, 2465, 3382] ΔE=-0.000000 accept=True
    core_region=3 delta_region=58 | E_before=1.900001 E_after=1.900001
    Tile-level changes (top 6 by |ΔE|):
      id= 1048 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3381 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2464 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2465 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2466 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1049 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1158.json (T=1.2)
   ⏳ Global 1158/3000 | Stage 300/429 | T=1.2 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1168/3000 | Stage 310/429 | T=1.2 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1178/3000 | Stage 320/429 | T=1.2 | Acc=6
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1188/3000 | Stage 330/429 | T=1.2 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1198/3000 | Stage 340/429 | T=1.2 | Acc=10
🔁 Step 350: cluster=[1129, 2360, 2414] ΔE=+3.078000 accept=False
    core_region=3 delta_region=56 | E_before=3.456000 E_after=6.534000
    Tile-level changes (top 6 by |ΔE|):
      id= 3287 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 1056 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1055 THIN->THIN move= 0.0000 E:  0.0500-> 0.0570 ΔE=+  0.0070 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1129 THICK->THIN move= 0.5878 E:  0.0500-> 0.0550 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2413 THIN->THIN move= 0.0000 E:  0.0500-> 0.0550 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2415 THIN->THIN move= 0.0000 E:  0.0000-> 0.0050 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1208.json (T=1.2)
   ⏳ Global 1208/3000 | Stage 350/429 | T=1.2 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1218/3000 | Stage 360/429 | T=1.2 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1228/3000 | Stage 370/429 | T=1.2 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1238/3000 | Stage 380/429 | T=1.2 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1248/3000 | Stage 390/429 | T=1.2 | Acc=6
🔁 Step 400: cluster=[3419, 3420, 4241] ΔE=+1.058000 accept=True
    core_region=3 delta_region=54 | E_before=4.516000 E_after=5.574000
    Tile-level changes (top 6 by |ΔE|):
      id= 4241 THICK->THICK move= 0.3090 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3420 THIN->THICK move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3419 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2187 THICK->THICK move= 0.0000 E:  0.0520-> 0.0540 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  693 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  768 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1258.json (T=1.2)
   ⏳ Global 1258/3000 | Stage 400/429 | T=1.2 | Acc=9
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1268/3000 | Stage 410/429 | T=1.2 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1278/3000 | Stage 420/429 | T=1.2 | Acc=7
✅ MC sweep: 7/9 accepted (77.8%), max drift: 0.000000
   ⏳ Global 1287/3000 | Stage 429/429 | T=1.2 | Acc=7

🌡️ STAGE 4/7: Cooling to T=0.6 (429 steps)...
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1297/3000 | Stage 10/429 | T=0.6 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1307.json (T=0.6)
   ⏳ Global 1307/3000 | Stage 20/429 | T=0.6 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1317/3000 | Stage 30/429 | T=0.6 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1327/3000 | Stage 40/429 | T=0.6 | Acc=7
🔁 Step 50: cluster=[2353, 2354, 3379] ΔE=+0.050000 accept=True
    core_region=3 delta_region=57 | E_before=2.150001 E_after=2.200001
    Tile-level changes (top 6 by |ΔE|):
      id= 2409 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4134 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1337/3000 | Stage 50/429 | T=0.6 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1347/3000 | Stage 60/429 | T=0.6 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1357.json (T=0.6)
   ⏳ Global 1357/3000 | Stage 70/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1367/3000 | Stage 80/429 | T=0.6 | Acc=8
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 1377/3000 | Stage 90/429 | T=0.6 | Acc=2
🔁 Step 100: cluster=[761, 3516, 4190] ΔE=+1.058000 accept=False
    core_region=3 delta_region=58 | E_before=1.800001 E_after=2.858001
    Tile-level changes (top 6 by |ΔE|):
      id=  761 THICK->THICK move= 0.3090 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4190 THIN->THICK move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2294 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3516 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  760 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3515 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1387/3000 | Stage 100/429 | T=0.6 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1397/3000 | Stage 110/429 | T=0.6 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1407.json (T=0.6)
   ⏳ Global 1407/3000 | Stage 120/429 | T=0.6 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1417/3000 | Stage 130/429 | T=0.6 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1427/3000 | Stage 140/429 | T=0.6 | Acc=7
🔁 Step 150: cluster=[2239, 2240, 3467] ΔE=+1.108000 accept=False
    core_region=3 delta_region=55 | E_before=4.466000 E_after=5.574000
    Tile-level changes (top 6 by |ΔE|):
      id= 2239 THIN->THICK move= 0.5878 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2294 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3467 THICK->THICK move= 0.3090 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  763 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2240 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4189 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1437/3000 | Stage 150/429 | T=0.6 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1447/3000 | Stage 160/429 | T=0.6 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1457.json (T=0.6)
   ⏳ Global 1457/3000 | Stage 170/429 | T=0.6 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1467/3000 | Stage 180/429 | T=0.6 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1477/3000 | Stage 190/429 | T=0.6 | Acc=5
🔁 Step 200: cluster=[914, 2191, 3327] ΔE=+2.316000 accept=False
    core_region=3 delta_region=57 | E_before=2.350000 E_after=4.666000
    Tile-level changes (top 6 by |ΔE|):
      id= 2246 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3326 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3327 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  918 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2191 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  916 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 1487/3000 | Stage 200/429 | T=0.6 | Acc=3
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1497/3000 | Stage 210/429 | T=0.6 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1507.json (T=0.6)
   ⏳ Global 1507/3000 | Stage 220/429 | T=0.6 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1517/3000 | Stage 230/429 | T=0.6 | Acc=5
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1527/3000 | Stage 240/429 | T=0.6 | Acc=10
🔁 Step 250: cluster=[833, 2296, 4162] ΔE=-0.149999 accept=True
    core_region=3 delta_region=55 | E_before=2.450000 E_after=2.300001
    Tile-level changes (top 6 by |ΔE|):
      id= 2296 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2298 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2297 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  762 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1537/3000 | Stage 250/429 | T=0.6 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1547/3000 | Stage 260/429 | T=0.6 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1557.json (T=0.6)
   ⏳ Global 1557/3000 | Stage 270/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1567/3000 | Stage 280/429 | T=0.6 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1577/3000 | Stage 290/429 | T=0.6 | Acc=8
🔁 Step 300: cluster=[914, 2191, 3327] ΔE=+1.258000 accept=False
    core_region=3 delta_region=56 | E_before=3.158001 E_after=4.416001
    Tile-level changes (top 6 by |ΔE|):
      id= 3326 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3327 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  918 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  916 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2191 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  919 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 1587/3000 | Stage 300/429 | T=0.6 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1597/3000 | Stage 310/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1607.json (T=0.6)
   ⏳ Global 1607/3000 | Stage 320/429 | T=0.6 | Acc=8
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1617/3000 | Stage 330/429 | T=0.6 | Acc=6
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1627/3000 | Stage 340/429 | T=0.6 | Acc=10
🔁 Step 350: cluster=[824, 3521, 4110] ΔE=+0.858000 accept=True
    core_region=3 delta_region=60 | E_before=2.652000 E_after=3.510000
    Tile-level changes (top 6 by |ΔE|):
      id=  898 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3521 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4137 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2403 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  824 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  899 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1637/3000 | Stage 350/429 | T=0.6 | Acc=9
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1647/3000 | Stage 360/429 | T=0.6 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1657.json (T=0.6)
   ⏳ Global 1657/3000 | Stage 370/429 | T=0.6 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1667/3000 | Stage 380/429 | T=0.6 | Acc=5
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1677/3000 | Stage 390/429 | T=0.6 | Acc=7
🔁 Step 400: cluster=[838, 2244, 3423] ΔE=+3.224000 accept=False
    core_region=3 delta_region=59 | E_before=2.100001 E_after=5.324001
    Tile-level changes (top 6 by |ΔE|):
      id= 4214 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  911 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  839 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2244 THIN->THICK move= 0.3090 E:  0.0000-> 0.0540 ΔE=+  0.0540 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2243 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  838 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1687/3000 | Stage 400/429 | T=0.6 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1697/3000 | Stage 410/429 | T=0.6 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1707.json (T=0.6)
   ⏳ Global 1707/3000 | Stage 420/429 | T=0.6 | Acc=7
✅ MC sweep: 4/9 accepted (44.4%), max drift: 0.000000
   ⏳ Global 1716/3000 | Stage 429/429 | T=0.6 | Acc=4

🌡️ STAGE 5/7: Cooling to T=0.3 (428 steps)...
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1726/3000 | Stage 10/428 | T=0.3 | Acc=5
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 1736/3000 | Stage 20/428 | T=0.3 | Acc=3
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1746/3000 | Stage 30/428 | T=0.3 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1756.json (T=0.3)
   ⏳ Global 1756/3000 | Stage 40/428 | T=0.3 | Acc=6
🔁 Step 50: cluster=[1046, 1122, 1123] ΔE=-0.150000 accept=True
    core_region=3 delta_region=55 | E_before=2.400000 E_after=2.250001
    Tile-level changes (top 6 by |ΔE|):
      id= 1121 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1122 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1046 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1125 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1050 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1047 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1766/3000 | Stage 50/428 | T=0.3 | Acc=7
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1776/3000 | Stage 60/428 | T=0.3 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1786/3000 | Stage 70/428 | T=0.3 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1796/3000 | Stage 80/428 | T=0.3 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1806.json (T=0.3)
   ⏳ Global 1806/3000 | Stage 90/428 | T=0.3 | Acc=6
🔁 Step 100: cluster=[983, 3377, 4133] ΔE=+0.000000 accept=True
    core_region=3 delta_region=57 | E_before=2.450001 E_after=2.450001
    Tile-level changes (top 6 by |ΔE|):
      id= 4133 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3377 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  909 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  983 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3331 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1816/3000 | Stage 100/428 | T=0.3 | Acc=8
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1826/3000 | Stage 110/428 | T=0.3 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1836/3000 | Stage 120/428 | T=0.3 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1846/3000 | Stage 130/428 | T=0.3 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1856.json (T=0.3)
   ⏳ Global 1856/3000 | Stage 140/428 | T=0.3 | Acc=7
🔁 Step 150: cluster=[750, 2456, 4165] ΔE=-0.000000 accept=True
    core_region=3 delta_region=55 | E_before=2.250001 E_after=2.250001
    Tile-level changes (top 6 by |ΔE|):
      id= 2456 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4138 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  750 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  749 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4165 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2455 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1866/3000 | Stage 150/428 | T=0.3 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1876/3000 | Stage 160/428 | T=0.3 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1886/3000 | Stage 170/428 | T=0.3 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1896/3000 | Stage 180/428 | T=0.3 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1906.json (T=0.3)
   ⏳ Global 1906/3000 | Stage 190/428 | T=0.3 | Acc=5
🔁 Step 200: cluster=[1062, 3284, 4132] ΔE=+0.050000 accept=True
    core_region=3 delta_region=59 | E_before=2.050002 E_after=2.100002
    Tile-level changes (top 6 by |ΔE|):
      id=  989 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1063 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3284 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1062 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4132 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1060 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1916/3000 | Stage 200/428 | T=0.3 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1926/3000 | Stage 210/428 | T=0.3 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1936/3000 | Stage 220/428 | T=0.3 | Acc=8
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1946/3000 | Stage 230/428 | T=0.3 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1956.json (T=0.3)
   ⏳ Global 1956/3000 | Stage 240/428 | T=0.3 | Acc=7
🔁 Step 250: cluster=[1049, 2465, 3381] ΔE=+0.000000 accept=True
    core_region=3 delta_region=59 | E_before=2.450001 E_after=2.450001
    Tile-level changes (top 6 by |ΔE|):
      id= 1048 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1050 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1049 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2464 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2466 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2411 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1966/3000 | Stage 250/428 | T=0.3 | Acc=4
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1976/3000 | Stage 260/428 | T=0.3 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1986/3000 | Stage 270/428 | T=0.3 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1996/3000 | Stage 280/428 | T=0.3 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2006.json (T=0.3)
   ⏳ Global 2006/3000 | Stage 290/428 | T=0.3 | Acc=4
🔁 Step 300: cluster=[972, 975, 2517] ΔE=+0.449998 accept=False
    core_region=3 delta_region=57 | E_before=1.600003 E_after=2.050002
    Tile-level changes (top 6 by |ΔE|):
      id= 4081 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  972 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  971 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2518 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2517 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2016/3000 | Stage 300/428 | T=0.3 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 2026/3000 | Stage 310/428 | T=0.3 | Acc=7
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2036/3000 | Stage 320/428 | T=0.3 | Acc=4
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 2046/3000 | Stage 330/428 | T=0.3 | Acc=8
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2056.json (T=0.3)
   ⏳ Global 2056/3000 | Stage 340/428 | T=0.3 | Acc=6
🔁 Step 350: cluster=[3471, 3472, 4135] ΔE=+0.000000 accept=True
    core_region=3 delta_region=56 | E_before=2.400000 E_after=2.400001
    Tile-level changes (top 6 by |ΔE|):
      id=  906 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3472 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4135 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  830 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2405 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 2066/3000 | Stage 350/428 | T=0.3 | Acc=8
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2076/3000 | Stage 360/428 | T=0.3 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2086/3000 | Stage 370/428 | T=0.3 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2096/3000 | Stage 380/428 | T=0.3 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2106.json (T=0.3)
   ⏳ Global 2106/3000 | Stage 390/428 | T=0.3 | Acc=5
🔁 Step 400: cluster=[904, 977, 2408] ΔE=+0.200000 accept=True
    core_region=3 delta_region=56 | E_before=2.000001 E_after=2.200001
    Tile-level changes (top 6 by |ΔE|):
      id= 2409 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3426 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2408 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  977 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4108 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  904 THIN->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 2116/3000 | Stage 400/428 | T=0.3 | Acc=7
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2126/3000 | Stage 410/428 | T=0.3 | Acc=4
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2136/3000 | Stage 420/428 | T=0.3 | Acc=6
✅ MC sweep: 7/8 accepted (87.5%), max drift: 0.000000
   ⏳ Global 2144/3000 | Stage 428/428 | T=0.3 | Acc=7

🌡️ STAGE 6/7: Cooling to T=0.15 (428 steps)...
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2154.json (T=0.15)
   ⏳ Global 2154/3000 | Stage 10/428 | T=0.15 | Acc=7
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2164/3000 | Stage 20/428 | T=0.15 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2174/3000 | Stage 30/428 | T=0.15 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2184/3000 | Stage 40/428 | T=0.15 | Acc=5
🔁 Step 50: cluster=[682, 683, 2347] ΔE=+2.466000 accept=False
    core_region=3 delta_region=56 | E_before=2.000001 E_after=4.466000
    Tile-level changes (top 6 by |ΔE|):
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2348 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  680 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2346 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2347 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  682 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2194/3000 | Stage 50/428 | T=0.15 | Acc=6
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2204.json (T=0.15)
   ⏳ Global 2204/3000 | Stage 60/428 | T=0.15 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2214/3000 | Stage 70/428 | T=0.15 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2224/3000 | Stage 80/428 | T=0.15 | Acc=6
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2234/3000 | Stage 90/428 | T=0.15 | Acc=4
🔁 Step 100: cluster=[2353, 2355, 3380] ΔE=+2.366000 accept=False
    core_region=3 delta_region=57 | E_before=2.300001 E_after=4.666000
    Tile-level changes (top 6 by |ΔE|):
      id= 3428 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4080 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3380 THIN->THICK move= 0.3090 E:  0.0000-> 0.0540 ΔE=+  0.0540 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2409 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2355 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2244/3000 | Stage 100/428 | T=0.15 | Acc=1
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2254.json (T=0.15)
   ⏳ Global 2254/3000 | Stage 110/428 | T=0.15 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2264/3000 | Stage 120/428 | T=0.15 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2274/3000 | Stage 130/428 | T=0.15 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2284/3000 | Stage 140/428 | T=0.15 | Acc=4
🔁 Step 150: cluster=[749, 752, 4165] ΔE=+1.058000 accept=False
    core_region=3 delta_region=55 | E_before=2.300000 E_after=3.358000
    Tile-level changes (top 6 by |ΔE|):
      id=  749 THIN->THICK move= 0.5878 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4165 THICK->THICK move= 0.3090 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3567 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3566 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  752 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2457 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2294/3000 | Stage 150/428 | T=0.15 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2304.json (T=0.15)
   ⏳ Global 2304/3000 | Stage 160/428 | T=0.15 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2314/3000 | Stage 170/428 | T=0.15 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2324/3000 | Stage 180/428 | T=0.15 | Acc=5
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2334/3000 | Stage 190/428 | T=0.15 | Acc=3
🔁 Step 200: cluster=[3471, 3472, 4135] ΔE=-0.050000 accept=True
    core_region=3 delta_region=56 | E_before=2.400000 E_after=2.350000
    Tile-level changes (top 6 by |ΔE|):
      id=  906 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4135 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2406 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2407 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3472 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2344/3000 | Stage 200/428 | T=0.15 | Acc=6
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2354.json (T=0.15)
   ⏳ Global 2354/3000 | Stage 210/428 | T=0.15 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2364/3000 | Stage 220/428 | T=0.15 | Acc=3
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2374/3000 | Stage 230/428 | T=0.15 | Acc=6
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2384/3000 | Stage 240/428 | T=0.15 | Acc=3
🔁 Step 250: cluster=[686, 687, 688] ΔE=-0.050000 accept=True
    core_region=3 delta_region=55 | E_before=1.700001 E_after=1.650001
    Tile-level changes (top 6 by |ΔE|):
      id=  612 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  687 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  691 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  685 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3515 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  688 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 2394/3000 | Stage 250/428 | T=0.15 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2404.json (T=0.15)
   ⏳ Global 2404/3000 | Stage 260/428 | T=0.15 | Acc=6
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2414/3000 | Stage 270/428 | T=0.15 | Acc=3
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2424/3000 | Stage 280/428 | T=0.15 | Acc=4
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2434/3000 | Stage 290/428 | T=0.15 | Acc=6
🔁 Step 300: cluster=[1055, 1057, 3285] ΔE=+1.008000 accept=False
    core_region=3 delta_region=57 | E_before=2.350001 E_after=3.358001
    Tile-level changes (top 6 by |ΔE|):
      id= 1058 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1055 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2358 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3332 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2357 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1057 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2444/3000 | Stage 300/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2454.json (T=0.15)
   ⏳ Global 2454/3000 | Stage 310/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2464/3000 | Stage 320/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2474/3000 | Stage 330/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2484/3000 | Stage 340/428 | T=0.15 | Acc=5
🔁 Step 350: cluster=[3328, 3423, 4188] ΔE=+0.050000 accept=True
    core_region=3 delta_region=59 | E_before=1.450002 E_after=1.500002
    Tile-level changes (top 6 by |ΔE|):
      id=  841 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3328 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  911 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3423 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  912 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 2494/3000 | Stage 350/428 | T=0.15 | Acc=7
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2504.json (T=0.15)
   ⏳ Global 2504/3000 | Stage 360/428 | T=0.15 | Acc=3
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 2514/3000 | Stage 370/428 | T=0.15 | Acc=7
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2524/3000 | Stage 380/428 | T=0.15 | Acc=3
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2534/3000 | Stage 390/428 | T=0.15 | Acc=6
🔁 Step 400: cluster=[2412, 3335, 4078] ΔE=+0.250000 accept=False
    core_region=3 delta_region=55 | E_before=1.650002 E_after=1.900001
    Tile-level changes (top 6 by |ΔE|):
      id= 1053 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2413 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1128 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4078 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2412 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2467 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2544/3000 | Stage 400/428 | T=0.15 | Acc=5
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2554.json (T=0.15)
   ⏳ Global 2554/3000 | Stage 410/428 | T=0.15 | Acc=3
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2564/3000 | Stage 420/428 | T=0.15 | Acc=6
✅ MC sweep: 7/8 accepted (87.5%), max drift: 0.000000
   ⏳ Global 2572/3000 | Stage 428/428 | T=0.15 | Acc=7

🌡️ STAGE 7/7: Cooling to T=0.05 (428 steps)...
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2582/3000 | Stage 10/428 | T=0.05 | Acc=3
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2592/3000 | Stage 20/428 | T=0.05 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2602.json (T=0.05)
   ⏳ Global 2602/3000 | Stage 30/428 | T=0.05 | Acc=3
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2612/3000 | Stage 40/428 | T=0.05 | Acc=3
🔁 Step 50: cluster=[908, 980, 2352] ΔE=+0.000000 accept=True
    core_region=3 delta_region=56 | E_before=1.900001 E_after=1.900001
    Tile-level changes (top 6 by |ΔE|):
      id=  980 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2299 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  908 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3425 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2352 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2622/3000 | Stage 50/428 | T=0.05 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2632/3000 | Stage 60/428 | T=0.05 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2642/3000 | Stage 70/428 | T=0.05 | Acc=5
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2652.json (T=0.05)
   ⏳ Global 2652/3000 | Stage 80/428 | T=0.05 | Acc=3
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2662/3000 | Stage 90/428 | T=0.05 | Acc=3
🔁 Step 100: cluster=[841, 2243, 3375] ΔE=+0.199999 accept=False
    core_region=3 delta_region=58 | E_before=1.450002 E_after=1.650002
    Tile-level changes (top 6 by |ΔE|):
      id= 2243 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3374 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  911 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3375 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  841 THICK->THIN move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4188 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2672/3000 | Stage 100/428 | T=0.05 | Acc=2
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2682/3000 | Stage 110/428 | T=0.05 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2692/3000 | Stage 120/428 | T=0.05 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2702.json (T=0.05)
   ⏳ Global 2702/3000 | Stage 130/428 | T=0.05 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2712/3000 | Stage 140/428 | T=0.05 | Acc=4
🔁 Step 150: cluster=[1056, 1129, 1131] ΔE=+0.449999 accept=False
    core_region=3 delta_region=55 | E_before=1.200003 E_after=1.650002
    Tile-level changes (top 6 by |ΔE|):
      id= 1131 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1135 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1133 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1056 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4105 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2722/3000 | Stage 150/428 | T=0.05 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2732/3000 | Stage 160/428 | T=0.05 | Acc=4
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2742/3000 | Stage 170/428 | T=0.05 | Acc=1
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2752.json (T=0.05)
   ⏳ Global 2752/3000 | Stage 180/428 | T=0.05 | Acc=1
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2762/3000 | Stage 190/428 | T=0.05 | Acc=2
🔁 Step 200: cluster=[2240, 3467, 4189] ΔE=+0.349999 accept=False
    core_region=3 delta_region=56 | E_before=1.150002 E_after=1.500002
    Tile-level changes (top 6 by |ΔE|):
      id= 2241 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  764 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4189 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2294 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2240 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3469 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2772/3000 | Stage 200/428 | T=0.05 | Acc=1
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2782/3000 | Stage 210/428 | T=0.05 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2792/3000 | Stage 220/428 | T=0.05 | Acc=5
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2802.json (T=0.05)
   ⏳ Global 2802/3000 | Stage 230/428 | T=0.05 | Acc=2
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2812/3000 | Stage 240/428 | T=0.05 | Acc=3
🔁 Step 250: cluster=[1053, 1128, 2412] ΔE=+0.399999 accept=False
    core_region=3 delta_region=55 | E_before=1.150004 E_after=1.550003
    Tile-level changes (top 6 by |ΔE|):
      id= 4078 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4079 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1053 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1054 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1128 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3287 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2822/3000 | Stage 250/428 | T=0.05 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2832/3000 | Stage 260/428 | T=0.05 | Acc=5
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2842/3000 | Stage 270/428 | T=0.05 | Acc=2
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2852.json (T=0.05)
   ⏳ Global 2852/3000 | Stage 280/428 | T=0.05 | Acc=3
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2862/3000 | Stage 290/428 | T=0.05 | Acc=4
🔁 Step 300: cluster=[841, 2243, 3375] ΔE=+0.349999 accept=False
    core_region=3 delta_region=58 | E_before=1.000003 E_after=1.350002
    Tile-level changes (top 6 by |ΔE|):
      id= 2243 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  841 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  911 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3374 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3373 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2245 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2872/3000 | Stage 300/428 | T=0.05 | Acc=2
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2882/3000 | Stage 310/428 | T=0.05 | Acc=3
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2892/3000 | Stage 320/428 | T=0.05 | Acc=4
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2902.json (T=0.05)
   ⏳ Global 2902/3000 | Stage 330/428 | T=0.05 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2912/3000 | Stage 340/428 | T=0.05 | Acc=4
🔁 Step 350: cluster=[689, 3514, 4217] ΔE=+0.250000 accept=False
    core_region=3 delta_region=57 | E_before=1.750001 E_after=2.000001
    Tile-level changes (top 6 by |ΔE|):
      id= 3513 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  688 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  691 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  613 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  689 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3514 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2922/3000 | Stage 350/428 | T=0.05 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2932/3000 | Stage 360/428 | T=0.05 | Acc=3
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2942/3000 | Stage 370/428 | T=0.05 | Acc=1
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2952.json (T=0.05)
   ⏳ Global 2952/3000 | Stage 380/428 | T=0.05 | Acc=3
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2962/3000 | Stage 390/428 | T=0.05 | Acc=1
🔁 Step 400: cluster=[974, 2461, 2514] ΔE=+1.008000 accept=False
    core_region=3 delta_region=56 | E_before=1.900002 E_after=2.908002
    Tile-level changes (top 6 by |ΔE|):
      id= 2461 THICK->THICK move= 0.3090 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  971 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2514 THIN->THICK move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2513 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  899 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2972/3000 | Stage 400/428 | T=0.05 | Acc=1
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2982/3000 | Stage 410/428 | T=0.05 | Acc=1
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2992/3000 | Stage 420/428 | T=0.05 | Acc=1
✅ MC sweep: 1/8 accepted (12.5%), max drift: 0.000000
   📸 Snapshot: healing_step_3000.json (T=0.05)
   ⏳ Global 3000/3000 | Stage 428/428 | T=0.05 | Acc=1
------------------------------------------------------------
RESULTS: 94 -> 0 (Efficiency: 100.0%)
Drift: 0.000000

💾 Saved Full State: healing_base_run_001.json (for viz)
📄 Saved Summary   : healing_base_run_001_summary.json (for stats)
📌 Latest: data/experiments/healing/latest.json

real    11m59.563s
user    11m47.511s
sys     0m1.755s
randa@Randa:quasi-phason$ time python scripts/analysis/visualize_state.py
🔍 Searching in: data/experiments
📂 Loading State: healing_base_run_001.json
   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_base_run_001_matrix.png

real    0m14.949s
user    0m10.105s
sys     0m3.538s
randa@Randa:quasi-phason$ time python scripts/analysis/batch_visualize.py --dir data/experiments/healing/
healing_base_run_001/                  healing_damaged_state_1766734207.json
healing_base_run_002/                  latest.json
randa@Randa:quasi-phason$ time python scripts/analysis/batch_visualize.py --dir data/experiments/healing/healing_base_run_001/
🔍 Found 66 state files. Starting batch visualization...
Generating Plots:   0%|                                                                                                 | 0/66 [00:00<?, ?it/s]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_base_run_001_matrix.png
Generating Plots:   2%|█▎                                                                                     | 1/66 [00:56<1:01:17, 56.58s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_damaged_state_1766734394_matrix.png
Generating Plots:   3%|██▋                                                                                      | 2/66 [01:06<31:14, 29.29s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_damaged_state_1766741636_matrix.png
Generating Plots:   5%|████                                                                                     | 3/66 [01:24<25:20, 24.13s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_damaged_state_1766751221_matrix.png
Generating Plots:   6%|█████▍                                                                                   | 4/66 [01:47<24:31, 23.74s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_damaged_state_1766766995_matrix.png
Generating Plots:   8%|██████▋                                                                                  | 5/66 [02:13<24:41, 24.28s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_damaged_state_1766773651_matrix.png
Generating Plots:   9%|████████                                                                                 | 6/66 [03:05<33:56, 33.94s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0050_matrix.png
Generating Plots:  11%|█████████▍                                                                               | 7/66 [03:21<27:28, 27.94s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0100_matrix.png
Generating Plots:  12%|██████████▊                                                                              | 8/66 [03:35<22:36, 23.39s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0150_matrix.png
Generating Plots:  14%|████████████▏                                                                            | 9/66 [03:50<19:56, 20.98s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0200_matrix.png
Generating Plots:  15%|█████████████▎                                                                          | 10/66 [04:07<18:20, 19.65s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0250_matrix.png
Generating Plots:  17%|██████████████▋                                                                         | 11/66 [04:17<15:13, 16.61s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0300_matrix.png
Generating Plots:  18%|████████████████                                                                        | 12/66 [04:33<14:50, 16.49s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0350_matrix.png
Generating Plots:  20%|█████████████████▎                                                                      | 13/66 [04:44<13:12, 14.94s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0400_matrix.png
Generating Plots:  21%|██████████████████▋                                                                     | 14/66 [04:54<11:37, 13.41s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0459_matrix.png
Generating Plots:  23%|████████████████████                                                                    | 15/66 [05:01<09:50, 11.59s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0509_matrix.png
Generating Plots:  24%|█████████████████████▎                                                                  | 16/66 [05:09<08:31, 10.22s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0559_matrix.png
Generating Plots:  26%|██████████████████████▋                                                                 | 17/66 [05:15<07:33,  9.25s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0609_matrix.png
Generating Plots:  27%|████████████████████████                                                                | 18/66 [05:23<06:58,  8.72s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0659_matrix.png
Generating Plots:  29%|█████████████████████████▎                                                              | 19/66 [05:30<06:32,  8.34s/it   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0709_matrix.png
Generating Plots:  30%|██████████████████████████▋                                                             | 20/66 [05:38<06:13,  8.12s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0759_matrix.png
Generating Plots:  32%|████████████████████████████                                                            | 21/66 [05:46<06:00,  8.01s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0809_matrix.png
Generating Plots:  33%|█████████████████████████████▎                                                          | 22/66 [05:53<05:43,  7.82s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0858_matrix.png
Generating Plots:  35%|██████████████████████████████▋                                                         | 23/66 [06:01<05:30,  7.69s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0908_matrix.png
Generating Plots:  36%|████████████████████████████████                                                        | 24/66 [06:08<05:18,  7.57s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_0958_matrix.png
Generating Plots:  38%|█████████████████████████████████▎                                                      | 25/66 [06:15<05:04,  7.43s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1008_matrix.png
Generating Plots:  39%|██████████████████████████████████▋                                                     | 26/66 [06:22<04:49,  7.25s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1058_matrix.png
Generating Plots:  41%|████████████████████████████████████                                                    | 27/66 [06:29<04:36,  7.10s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1108_matrix.png
Generating Plots:  42%|█████████████████████████████████████▎                                                  | 28/66 [06:35<04:26,  7.01s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1158_matrix.png
Generating Plots:  44%|██████████████████████████████████████▋                                                 | 29/66 [06:42<04:19,  7.01s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1208_matrix.png
Generating Plots:  45%|████████████████████████████████████████                                                | 30/66 [06:50<04:14,  7.06s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1258_matrix.png
Generating Plots:  47%|█████████████████████████████████████████▎                                              | 31/66 [06:57<04:08,  7.09s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1307_matrix.png
Generating Plots:  48%|██████████████████████████████████████████▋                                             | 32/66 [07:04<04:01,  7.11s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1357_matrix.png
Generating Plots:  50%|████████████████████████████████████████████                                            | 33/66 [07:11<03:55,  7.14s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1407_matrix.png
Generating Plots:  52%|█████████████████████████████████████████████▎                                          | 34/66 [07:18<03:47,  7.10s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1457_matrix.png
Generating Plots:  53%|██████████████████████████████████████████████▋                                         | 35/66 [07:25<03:38,  7.05s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1507_matrix.png
Generating Plots:  55%|████████████████████████████████████████████████                                        | 36/66 [07:32<03:28,  6.96s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1557_matrix.png
Generating Plots:  56%|█████████████████████████████████████████████████▎                                      | 37/66 [07:38<03:19,  6.90s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1607_matrix.png
Generating Plots:  58%|██████████████████████████████████████████████████▋                                     | 38/66 [07:46<03:19,  7.11s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1657_matrix.png
Generating Plots:  59%|████████████████████████████████████████████████████                                    | 39/66 [07:53<03:11,  7.08s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1707_matrix.png
Generating Plots:  61%|█████████████████████████████████████████████████████▎                                  | 40/66 [08:01<03:09,  7.27s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1756_matrix.png
Generating Plots:  62%|██████████████████████████████████████████████████████▋                                 | 41/66 [08:08<03:03,  7.32s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1806_matrix.png
Generating Plots:  64%|████████████████████████████████████████████████████████                                | 42/66 [08:15<02:50,  7.10s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1856_matrix.png
Generating Plots:  65%|█████████████████████████████████████████████████████████▎                              | 43/66 [08:22<02:40,  6.97s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1906_matrix.png
Generating Plots:  67%|██████████████████████████████████████████████████████████▋                             | 44/66 [08:28<02:31,  6.88s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_1956_matrix.png
Generating Plots:  68%|███████████████████████████████████████████████████████████▉                            | 45/66 [08:35<02:24,  6.88s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2006_matrix.png
Generating Plots:  70%|█████████████████████████████████████████████████████████████▎                          | 46/66 [08:43<02:22,  7.11s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2056_matrix.png
Generating Plots:  71%|██████████████████████████████████████████████████████████████▋                         | 47/66 [08:50<02:15,  7.11s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2106_matrix.png
Generating Plots:  73%|████████████████████████████████████████████████████████████████                        | 48/66 [08:57<02:10,  7.25s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2154_matrix.png
Generating Plots:  74%|█████████████████████████████████████████████████████████████████▎                      | 49/66 [09:05<02:03,  7.29s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2204_matrix.png
Generating Plots:  76%|██████████████████████████████████████████████████████████████████▋                     | 50/66 [09:12<01:55,  7.25s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2254_matrix.png
Generating Plots:  77%|████████████████████████████████████████████████████████████████████                    | 51/66 [09:19<01:47,  7.17s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2304_matrix.png
Generating Plots:  79%|█████████████████████████████████████████████████████████████████████▎                  | 52/66 [09:26<01:38,  7.05s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2354_matrix.png
Generating Plots:  80%|██████████████████████████████████████████████████████████████████████▋                 | 53/66 [09:33<01:33,  7.17s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2404_matrix.png
Generating Plots:  82%|████████████████████████████████████████████████████████████████████████                | 54/66 [09:40<01:25,  7.16s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2454_matrix.png
Generating Plots:  83%|█████████████████████████████████████████████████████████████████████████▎              | 55/66 [09:47<01:18,  7.14s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2504_matrix.png
Generating Plots:  85%|██████████████████████████████████████████████████████████████████████████▋             | 56/66 [09:55<01:11,  7.14s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2554_matrix.png
Generating Plots:  86%|████████████████████████████████████████████████████████████████████████████            | 57/66 [10:01<01:03,  7.05s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2602_matrix.png
Generating Plots:  88%|█████████████████████████████████████████████████████████████████████████████▎          | 58/66 [10:08<00:55,  6.94s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2652_matrix.png
Generating Plots:  89%|██████████████████████████████████████████████████████████████████████████████▋         | 59/66 [10:15<00:49,  7.01s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2702_matrix.png
Generating Plots:  91%|████████████████████████████████████████████████████████████████████████████████        | 60/66 [10:22<00:41,  6.94s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2752_matrix.png
Generating Plots:  92%|█████████████████████████████████████████████████████████████████████████████████▎      | 61/66 [10:29<00:34,  6.89s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2802_matrix.png
Generating Plots:  94%|██████████████████████████████████████████████████████████████████████████████████▋     | 62/66 [10:36<00:27,  6.87s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2852_matrix.png
Generating Plots:  95%|████████████████████████████████████████████████████████████████████████████████████    | 63/66 [10:42<00:20,  6.82s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2902_matrix.png
Generating Plots:  97%|█████████████████████████████████████████████████████████████████████████████████████▎  | 64/66 [10:50<00:13,  6.99s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_2952_matrix.png
Generating Plots:  98%|██████████████████████████████████████████████████████████████████████████████████████▋ | 65/66 [10:57<00:06,  6.96s/it]   📊 Saved Matrix: data/experiments/healing/healing_base_run_001/viz/healing_step_3000_matrix.png
Generating Plots: 100%|████████████████████████████████████████████████████████████████████████████████████████| 66/66 [11:04<00:00, 10.06s/it]

✅ Batch complete. Plots saved to designated 'viz' folders.

real    11m6.295s
user    8m51.785s
sys     1m1.160s
randa@Randa:quasi-phason$