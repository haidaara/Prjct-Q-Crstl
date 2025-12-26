randa@Randa:quasi-phason$ python scripts/experiments/03_run_healing_test.py
🧪 EXPERIMENT 03: PHASON HEALING (Refactored)
============================================================
📥 Input tiling: data/processed/penrose_tiling_energy_initialized.json
📤 Output dir : data/experiments/healing/healing_base_run_001
⚙️  scenario=base seed_radius=10.0 num_defects=15 defect_threshold=1.5
⚙️  MC: T=0.1 steps=3000 R=3 verify_energy=True base_steps=100
------------------------------------------------------------
⚡ DAMAGE PHASE: Heating (T=5.0) to create 15 energetic defects...
✅ MC sweep: 50/50 accepted (100.0%), max drift: 0.000000
   🔥 Heating Step 50: High-Energy Tiles=23 (Target: 15)
✅ DAMAGE COMPLETE: Scrambled. Starting Count: 23 Defects.
📸 SNAPSHOT SAVED: data/experiments/healing/healing_base_run_001/healing_damaged_state_1766751221.json
🩺 SWITCHING TO ANNEALING: 7 Stages
   📅 Schedule: [5.0, 2.5, 1.2, 0.6, 0.3, 0.15, 0.05]
   ℹ️  Allocation: [429, 429, 429, 429, 428, 428, 428] steps/stage

🌡️ STAGE 1/7: Cooling to T=5.0 (429 steps)...
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 10/3000 | Stage 10/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 20/3000 | Stage 20/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 30/3000 | Stage 30/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 40/3000 | Stage 40/429 | T=5.0 | Acc=10
🔁 Step 50: cluster=[3379, 3380, 4107] ΔE=+0.000000 accept=True
    core_region=3 delta_region=57 | E_before=2.550000 E_after=2.550000
    Tile-level changes (top 6 by |ΔE|):
      id= 2411 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2410 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3380 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  979 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0050.json (T=5.0)
   ⏳ Global 50/3000 | Stage 50/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 60/3000 | Stage 60/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 70/3000 | Stage 70/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 80/3000 | Stage 80/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 90/3000 | Stage 90/429 | T=5.0 | Acc=8
🔁 Step 100: cluster=[767, 768, 3420] ΔE=-0.150000 accept=True
    core_region=3 delta_region=57 | E_before=2.400000 E_after=2.250001
    Tile-level changes (top 6 by |ΔE|):
      id=  769 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3420 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  767 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  766 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2187 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  768 THICK->THIN move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0100.json (T=5.0)
   ⏳ Global 100/3000 | Stage 100/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 110/3000 | Stage 110/429 | T=5.0 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 120/3000 | Stage 120/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 130/3000 | Stage 130/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 140/3000 | Stage 140/429 | T=5.0 | Acc=10
🔁 Step 150: cluster=[682, 683, 2345] ΔE=-1.058000 accept=True
    core_region=3 delta_region=58 | E_before=7.740000 E_after=6.682000
    Tile-level changes (top 6 by |ΔE|):
      id=  684 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  683 THICK->THIN move= 0.5878 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  685 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2291 THIN->THIN move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  758 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0150.json (T=5.0)
   ⏳ Global 150/3000 | Stage 150/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 160/3000 | Stage 160/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 170/3000 | Stage 170/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 180/3000 | Stage 180/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 190/3000 | Stage 190/429 | T=5.0 | Acc=9
🔁 Step 200: cluster=[748, 749, 4138] ΔE=-0.000000 accept=True
    core_region=3 delta_region=56 | E_before=2.254001 E_after=2.254001
    Tile-level changes (top 6 by |ΔE|):
      id= 3566 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4138 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  749 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2510 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3608 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  748 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0200.json (T=5.0)
   ⏳ Global 200/3000 | Stage 200/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 210/3000 | Stage 210/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 220/3000 | Stage 220/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 230/3000 | Stage 230/429 | T=5.0 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 240/3000 | Stage 240/429 | T=5.0 | Acc=9
🔁 Step 250: cluster=[1130, 2414, 2415] ΔE=-0.050000 accept=True
    core_region=3 delta_region=59 | E_before=2.100001 E_after=2.050001
    Tile-level changes (top 6 by |ΔE|):
      id= 1204 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2414 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1131 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2359 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1129 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2415 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0250.json (T=5.0)
   ⏳ Global 250/3000 | Stage 250/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 260/3000 | Stage 260/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 270/3000 | Stage 270/429 | T=5.0 | Acc=9
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 280/3000 | Stage 280/429 | T=5.0 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 290/3000 | Stage 290/429 | T=5.0 | Acc=9
🔁 Step 300: cluster=[984, 2301, 2302] ΔE=-1.108000 accept=True
    core_region=3 delta_region=60 | E_before=5.626001 E_after=4.518001
    Tile-level changes (top 6 by |ΔE|):
      id=  986 THIN->THIN move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3331 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2301 THICK->THICK move= 0.3090 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3330 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  987 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0300.json (T=5.0)
   ⏳ Global 300/3000 | Stage 300/429 | T=5.0 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 310/3000 | Stage 310/429 | T=5.0 | Acc=7
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 320/3000 | Stage 320/429 | T=5.0 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 330/3000 | Stage 330/429 | T=5.0 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 340/3000 | Stage 340/429 | T=5.0 | Acc=10
🔁 Step 350: cluster=[1132, 1133, 3287] ΔE=-0.050000 accept=True
    core_region=3 delta_region=57 | E_before=2.450000 E_after=2.400000
    Tile-level changes (top 6 by |ΔE|):
      id= 1134 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2358 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1132 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2360 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3287 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1133 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0350.json (T=5.0)
   ⏳ Global 350/3000 | Stage 350/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 360/3000 | Stage 360/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 370/3000 | Stage 370/429 | T=5.0 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 380/3000 | Stage 380/429 | T=5.0 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 390/3000 | Stage 390/429 | T=5.0 | Acc=9
🔁 Step 400: cluster=[1056, 2357, 3332] ΔE=+0.350000 accept=False
    core_region=3 delta_region=56 | E_before=5.266000 E_after=5.616000
    Tile-level changes (top 6 by |ΔE|):
      id= 3332 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1058 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3333 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4106 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1056 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0400.json (T=5.0)
   ⏳ Global 400/3000 | Stage 400/429 | T=5.0 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 410/3000 | Stage 410/429 | T=5.0 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 420/3000 | Stage 420/429 | T=5.0 | Acc=10
✅ MC sweep: 9/9 accepted (100.0%), max drift: 0.000000
   ⏳ Global 429/3000 | Stage 429/429 | T=5.0 | Acc=9

🌡️ STAGE 2/7: Cooling to T=2.5 (429 steps)...
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 439/3000 | Stage 10/429 | T=2.5 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 449/3000 | Stage 20/429 | T=2.5 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0459.json (T=2.5)
   ⏳ Global 459/3000 | Stage 30/429 | T=2.5 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 469/3000 | Stage 40/429 | T=2.5 | Acc=10
🔁 Step 50: cluster=[900, 2462, 3474] ΔE=+2.366000 accept=False
    core_region=3 delta_region=56 | E_before=6.536000 E_after=8.902000
    Tile-level changes (top 6 by |ΔE|):
      id= 2461 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  975 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  973 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THIN->THIN move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  900 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2462 THIN->THICK move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 479/3000 | Stage 50/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 489/3000 | Stage 60/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 499/3000 | Stage 70/429 | T=2.5 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0509.json (T=2.5)
   ⏳ Global 509/3000 | Stage 80/429 | T=2.5 | Acc=7
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 519/3000 | Stage 90/429 | T=2.5 | Acc=10
🔁 Step 100: cluster=[1126, 2466, 4053] ΔE=+1.058000 accept=True
    core_region=3 delta_region=62 | E_before=10.246000 E_after=11.304000
    Tile-level changes (top 6 by |ΔE|):
      id= 2466 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1051 THIN->THIN move= 0.0000 E:  0.0520-> 0.0040 ΔE= -0.0480 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1125 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1126 THICK->THICK move= 0.3090 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4053 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3382 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 529/3000 | Stage 100/429 | T=2.5 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 539/3000 | Stage 110/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 549/3000 | Stage 120/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0559.json (T=2.5)
   ⏳ Global 559/3000 | Stage 130/429 | T=2.5 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 569/3000 | Stage 140/429 | T=2.5 | Acc=9
🔁 Step 150: cluster=[756, 2347, 3517] ΔE=-0.050000 accept=True
    core_region=3 delta_region=54 | E_before=2.052001 E_after=2.002001
    Tile-level changes (top 6 by |ΔE|):
      id=  758 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  756 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  754 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2347 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3517 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2348 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 579/3000 | Stage 150/429 | T=2.5 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 589/3000 | Stage 160/429 | T=2.5 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 599/3000 | Stage 170/429 | T=2.5 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0609.json (T=2.5)
   ⏳ Global 609/3000 | Stage 180/429 | T=2.5 | Acc=10
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 619/3000 | Stage 190/429 | T=2.5 | Acc=9
🔁 Step 200: cluster=[2344, 3562, 4191] ΔE=+0.000000 accept=True
    core_region=3 delta_region=55 | E_before=2.400000 E_after=2.400000
    Tile-level changes (top 6 by |ΔE|):
      id= 4192 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4191 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  682 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3562 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  680 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  681 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 629/3000 | Stage 200/429 | T=2.5 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 639/3000 | Stage 210/429 | T=2.5 | Acc=9
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 649/3000 | Stage 220/429 | T=2.5 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0659.json (T=2.5)
   ⏳ Global 659/3000 | Stage 230/429 | T=2.5 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 669/3000 | Stage 240/429 | T=2.5 | Acc=8
🔁 Step 250: cluster=[841, 842, 2191] ΔE=+1.357999 accept=False
    core_region=3 delta_region=57 | E_before=5.422000 E_after=6.780000
    Tile-level changes (top 6 by |ΔE|):
      id=  843 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  840 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  841 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  842 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4187 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4186 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 679/3000 | Stage 250/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 689/3000 | Stage 260/429 | T=2.5 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 699/3000 | Stage 270/429 | T=2.5 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0709.json (T=2.5)
   ⏳ Global 709/3000 | Stage 280/429 | T=2.5 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 719/3000 | Stage 290/429 | T=2.5 | Acc=7
🔁 Step 300: cluster=[901, 902, 3473] ΔE=-0.000000 accept=True
    core_region=3 delta_region=56 | E_before=3.454000 E_after=3.454000
    Tile-level changes (top 6 by |ΔE|):
      id= 3473 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4109 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THICK->THIN move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2406 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  902 THIN->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3428 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 729/3000 | Stage 300/429 | T=2.5 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 739/3000 | Stage 310/429 | T=2.5 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 749/3000 | Stage 320/429 | T=2.5 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0759.json (T=2.5)
   ⏳ Global 759/3000 | Stage 330/429 | T=2.5 | Acc=10
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 769/3000 | Stage 340/429 | T=2.5 | Acc=10
🔁 Step 350: cluster=[759, 2349, 3516] ΔE=+0.149999 accept=True
    core_region=3 delta_region=55 | E_before=1.850002 E_after=2.000001
    Tile-level changes (top 6 by |ΔE|):
      id= 3516 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  759 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2349 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  761 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4190 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2347 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 779/3000 | Stage 350/429 | T=2.5 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 789/3000 | Stage 360/429 | T=2.5 | Acc=9
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 799/3000 | Stage 370/429 | T=2.5 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0809.json (T=2.5)
   ⏳ Global 809/3000 | Stage 380/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 819/3000 | Stage 390/429 | T=2.5 | Acc=9
🔁 Step 400: cluster=[981, 3380, 4107] ΔE=-0.050000 accept=True
    core_region=3 delta_region=55 | E_before=4.812000 E_after=4.762000
    Tile-level changes (top 6 by |ΔE|):
      id= 4106 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  982 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  978 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 829/3000 | Stage 400/429 | T=2.5 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 839/3000 | Stage 410/429 | T=2.5 | Acc=9
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 849/3000 | Stage 420/429 | T=2.5 | Acc=7
✅ MC sweep: 8/9 accepted (88.9%), max drift: 0.000000
   📸 Snapshot: healing_step_0858.json (T=2.5)
   ⏳ Global 858/3000 | Stage 429/429 | T=2.5 | Acc=8

🌡️ STAGE 3/7: Cooling to T=1.2 (429 steps)...
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 868/3000 | Stage 10/429 | T=1.2 | Acc=10
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 878/3000 | Stage 20/429 | T=1.2 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 888/3000 | Stage 30/429 | T=1.2 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 898/3000 | Stage 40/429 | T=1.2 | Acc=8
🔁 Step 50: cluster=[1049, 2464, 3429] ΔE=-0.349999 accept=True
    core_region=3 delta_region=55 | E_before=2.302001 E_after=1.952001
    Tile-level changes (top 6 by |ΔE|):
      id= 3429 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4080 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3430 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2410 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1050 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2464 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0908.json (T=1.2)
   ⏳ Global 908/3000 | Stage 50/429 | T=1.2 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 918/3000 | Stage 60/429 | T=1.2 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 928/3000 | Stage 70/429 | T=1.2 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 938/3000 | Stage 80/429 | T=1.2 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 948/3000 | Stage 90/429 | T=1.2 | Acc=7
🔁 Step 100: cluster=[907, 908, 2352] ΔE=+0.000000 accept=True
    core_region=3 delta_region=57 | E_before=2.150001 E_after=2.150001
    Tile-level changes (top 6 by |ΔE|):
      id= 2352 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  908 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3426 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2354 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  835 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_0958.json (T=1.2)
   ⏳ Global 958/3000 | Stage 100/429 | T=1.2 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 968/3000 | Stage 110/429 | T=1.2 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 978/3000 | Stage 120/429 | T=1.2 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 988/3000 | Stage 130/429 | T=1.2 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 998/3000 | Stage 140/429 | T=1.2 | Acc=8
🔁 Step 150: cluster=[917, 918, 2190] ΔE=+0.050000 accept=True
    core_region=3 delta_region=57 | E_before=2.050002 E_after=2.100001
    Tile-level changes (top 6 by |ΔE|):
      id= 2190 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2192 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  917 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  918 THIN->THIN move= 0.8090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  916 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  844 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1008.json (T=1.2)
   ⏳ Global 1008/3000 | Stage 150/429 | T=1.2 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1018/3000 | Stage 160/429 | T=1.2 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1028/3000 | Stage 170/429 | T=1.2 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1038/3000 | Stage 180/429 | T=1.2 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1048/3000 | Stage 190/429 | T=1.2 | Acc=7
🔁 Step 200: cluster=[978, 979, 2409] ΔE=+0.350000 accept=True
    core_region=3 delta_region=59 | E_before=3.208001 E_after=3.558000
    Tile-level changes (top 6 by |ΔE|):
      id=  977 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2409 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  904 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1053 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  979 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1058.json (T=1.2)
   ⏳ Global 1058/3000 | Stage 200/429 | T=1.2 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1068/3000 | Stage 210/429 | T=1.2 | Acc=8
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1078/3000 | Stage 220/429 | T=1.2 | Acc=10
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1088/3000 | Stage 230/429 | T=1.2 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1098/3000 | Stage 240/429 | T=1.2 | Acc=8
🔁 Step 250: cluster=[972, 3475, 3476] ΔE=+0.000000 accept=True
    core_region=3 delta_region=59 | E_before=4.610000 E_after=4.610000
    Tile-level changes (top 6 by |ΔE|):
      id= 2516 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3475 THICK->THIN move= 0.5878 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  972 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3477 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  971 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1108.json (T=1.2)
   ⏳ Global 1108/3000 | Stage 250/429 | T=1.2 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1118/3000 | Stage 260/429 | T=1.2 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1128/3000 | Stage 270/429 | T=1.2 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1138/3000 | Stage 280/429 | T=1.2 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1148/3000 | Stage 290/429 | T=1.2 | Acc=6
🔁 Step 300: cluster=[827, 3519, 4137] ΔE=+1.058000 accept=True
    core_region=3 delta_region=59 | E_before=3.358000 E_after=4.416000
    Tile-level changes (top 6 by |ΔE|):
      id= 4137 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2457 THICK->THICK move= 0.0000 E:  0.0500-> 0.0020 ΔE= -0.0480 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3520 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  827 THICK->THICK move= 0.3090 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4136 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1158.json (T=1.2)
   ⏳ Global 1158/3000 | Stage 300/429 | T=1.2 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1168/3000 | Stage 310/429 | T=1.2 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1178/3000 | Stage 320/429 | T=1.2 | Acc=9
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1188/3000 | Stage 330/429 | T=1.2 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1198/3000 | Stage 340/429 | T=1.2 | Acc=6
🔁 Step 350: cluster=[991, 992, 2193] ΔE=-0.000000 accept=True
    core_region=3 delta_region=58 | E_before=2.550001 E_after=2.550001
    Tile-level changes (top 6 by |ΔE|):
      id=  991 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3281 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  990 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  992 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2193 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  915 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1208.json (T=1.2)
   ⏳ Global 1208/3000 | Stage 350/429 | T=1.2 | Acc=9
✅ MC sweep: 10/10 accepted (100.0%), max drift: 0.000000
   ⏳ Global 1218/3000 | Stage 360/429 | T=1.2 | Acc=10
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1228/3000 | Stage 370/429 | T=1.2 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1238/3000 | Stage 380/429 | T=1.2 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1248/3000 | Stage 390/429 | T=1.2 | Acc=8
🔁 Step 400: cluster=[976, 2463, 3427] ΔE=+1.108000 accept=True
    core_region=3 delta_region=59 | E_before=1.950001 E_after=3.058001
    Tile-level changes (top 6 by |ΔE|):
      id= 2463 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THICK->THICK move= 0.0000 E:  0.0500-> 0.0020 ΔE= -0.0480 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  976 THICK->THICK move= 0.3090 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  973 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3427 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1258.json (T=1.2)
   ⏳ Global 1258/3000 | Stage 400/429 | T=1.2 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1268/3000 | Stage 410/429 | T=1.2 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1278/3000 | Stage 420/429 | T=1.2 | Acc=6
✅ MC sweep: 6/9 accepted (66.7%), max drift: 0.000000
   ⏳ Global 1287/3000 | Stage 429/429 | T=1.2 | Acc=6

🌡️ STAGE 4/7: Cooling to T=0.6 (429 steps)...
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1297/3000 | Stage 10/429 | T=0.6 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1307.json (T=0.6)
   ⏳ Global 1307/3000 | Stage 20/429 | T=0.6 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1317/3000 | Stage 30/429 | T=0.6 | Acc=5
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1327/3000 | Stage 40/429 | T=0.6 | Acc=9
🔁 Step 50: cluster=[682, 2344, 3562] ΔE=-0.000000 accept=True
    core_region=3 delta_region=55 | E_before=2.300000 E_after=2.300000
    Tile-level changes (top 6 by |ΔE|):
      id= 4192 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2346 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  681 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  680 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2344 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2345 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1337/3000 | Stage 50/429 | T=0.6 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1347/3000 | Stage 60/429 | T=0.6 | Acc=5
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1357.json (T=0.6)
   ⏳ Global 1357/3000 | Stage 70/429 | T=0.6 | Acc=9
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1367/3000 | Stage 80/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1377/3000 | Stage 90/429 | T=0.6 | Acc=8
🔁 Step 100: cluster=[830, 2408, 3472] ΔE=-0.100000 accept=True
    core_region=3 delta_region=59 | E_before=2.150001 E_after=2.050001
    Tile-level changes (top 6 by |ΔE|):
      id= 2406 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  832 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  830 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  903 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  833 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2408 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1387/3000 | Stage 100/429 | T=0.6 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1397/3000 | Stage 110/429 | T=0.6 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1407.json (T=0.6)
   ⏳ Global 1407/3000 | Stage 120/429 | T=0.6 | Acc=4
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1417/3000 | Stage 130/429 | T=0.6 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1427/3000 | Stage 140/429 | T=0.6 | Acc=8
🔁 Step 150: cluster=[1057, 2304, 4105] ΔE=+2.266000 accept=False
    core_region=3 delta_region=56 | E_before=2.450000 E_after=4.716000
    Tile-level changes (top 6 by |ΔE|):
      id= 1056 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2358 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1057 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3286 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2304 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1059 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1437/3000 | Stage 150/429 | T=0.6 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1447/3000 | Stage 160/429 | T=0.6 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1457.json (T=0.6)
   ⏳ Global 1457/3000 | Stage 170/429 | T=0.6 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1467/3000 | Stage 180/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1477/3000 | Stage 190/429 | T=0.6 | Acc=8
🔁 Step 200: cluster=[3513, 3514, 4243] ΔE=+0.000000 accept=True
    core_region=3 delta_region=59 | E_before=2.500000 E_after=2.500000
    Tile-level changes (top 6 by |ΔE|):
      id= 3513 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4242 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3514 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4243 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2237 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2238 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1487/3000 | Stage 200/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1497/3000 | Stage 210/429 | T=0.6 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1507.json (T=0.6)
   ⏳ Global 1507/3000 | Stage 220/429 | T=0.6 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1517/3000 | Stage 230/429 | T=0.6 | Acc=5
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1527/3000 | Stage 240/429 | T=0.6 | Acc=7
🔁 Step 250: cluster=[2290, 3561, 4217] ΔE=-0.050000 accept=True
    core_region=3 delta_region=57 | E_before=2.350000 E_after=2.300000
    Tile-level changes (top 6 by |ΔE|):
      id= 2345 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2292 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2291 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3561 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4217 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2290 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1537/3000 | Stage 250/429 | T=0.6 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1547/3000 | Stage 260/429 | T=0.6 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1557.json (T=0.6)
   ⏳ Global 1557/3000 | Stage 270/429 | T=0.6 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1567/3000 | Stage 280/429 | T=0.6 | Acc=7
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1577/3000 | Stage 290/429 | T=0.6 | Acc=8
🔁 Step 300: cluster=[822, 896, 2514] ΔE=+3.224000 accept=False
    core_region=3 delta_region=54 | E_before=2.200001 E_after=5.424001
    Tile-level changes (top 6 by |ΔE|):
      id=  822 THIN->THICK move= 0.5878 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  896 THICK->THICK move= 0.3090 E:  0.0500-> 1.1040 ΔE=+  1.0540 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2513 THIN->THIN move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2514 THICK->THIN move= 0.5878 E:  0.0500-> 0.0540 ΔE=+  0.0040 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3521 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4083 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1587/3000 | Stage 300/429 | T=0.6 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1597/3000 | Stage 310/429 | T=0.6 | Acc=8
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1607.json (T=0.6)
   ⏳ Global 1607/3000 | Stage 320/429 | T=0.6 | Acc=8
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1617/3000 | Stage 330/429 | T=0.6 | Acc=6
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1627/3000 | Stage 340/429 | T=0.6 | Acc=9
🔁 Step 350: cluster=[1127, 2466, 4052] ΔE=-0.050000 accept=True
    core_region=3 delta_region=56 | E_before=2.400001 E_after=2.350001
    Tile-level changes (top 6 by |ΔE|):
      id= 2469 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1125 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2466 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4052 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1127 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1129 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1637/3000 | Stage 350/429 | T=0.6 | Acc=9
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1647/3000 | Stage 360/429 | T=0.6 | Acc=6
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1657.json (T=0.6)
   ⏳ Global 1657/3000 | Stage 370/429 | T=0.6 | Acc=8
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1667/3000 | Stage 380/429 | T=0.6 | Acc=9
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1677/3000 | Stage 390/429 | T=0.6 | Acc=7
🔁 Step 400: cluster=[1127, 2466, 4052] ΔE=-0.000000 accept=True
    core_region=3 delta_region=56 | E_before=3.508001 E_after=3.508000
    Tile-level changes (top 6 by |ΔE|):
      id= 1125 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2467 THIN->THIN move= 0.0000 E:  0.0520-> 0.0520 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2466 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4052 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1127 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1129 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1687/3000 | Stage 400/429 | T=0.6 | Acc=5
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1697/3000 | Stage 410/429 | T=0.6 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1707.json (T=0.6)
   ⏳ Global 1707/3000 | Stage 420/429 | T=0.6 | Acc=6
✅ MC sweep: 6/9 accepted (66.7%), max drift: 0.000000
   ⏳ Global 1716/3000 | Stage 429/429 | T=0.6 | Acc=6

🌡️ STAGE 5/7: Cooling to T=0.3 (428 steps)...
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 1726/3000 | Stage 10/428 | T=0.3 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1736/3000 | Stage 20/428 | T=0.3 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1746/3000 | Stage 30/428 | T=0.3 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1756.json (T=0.3)
   ⏳ Global 1756/3000 | Stage 40/428 | T=0.3 | Acc=5
🔁 Step 50: cluster=[3513, 3514, 4243] ΔE=+1.108000 accept=False
    core_region=3 delta_region=58 | E_before=2.400000 E_after=3.508000
    Tile-level changes (top 6 by |ΔE|):
      id= 3514 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3513 THICK->THICK move= 0.3090 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2237 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  614 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4243 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4242 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 1766/3000 | Stage 50/428 | T=0.3 | Acc=1
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1776/3000 | Stage 60/428 | T=0.3 | Acc=6
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1786/3000 | Stage 70/428 | T=0.3 | Acc=8
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 1796/3000 | Stage 80/428 | T=0.3 | Acc=4
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1806.json (T=0.3)
   ⏳ Global 1806/3000 | Stage 90/428 | T=0.3 | Acc=6
🔁 Step 100: cluster=[754, 757, 830] ΔE=+0.250000 accept=False
    core_region=3 delta_region=58 | E_before=1.900001 E_after=2.150001
    Tile-level changes (top 6 by |ΔE|):
      id=  754 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2347 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2403 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  757 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2348 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  831 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1816/3000 | Stage 100/428 | T=0.3 | Acc=6
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1826/3000 | Stage 110/428 | T=0.3 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1836/3000 | Stage 120/428 | T=0.3 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1846/3000 | Stage 130/428 | T=0.3 | Acc=6
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1856.json (T=0.3)
   ⏳ Global 1856/3000 | Stage 140/428 | T=0.3 | Acc=9
🔁 Step 150: cluster=[2243, 3422, 3423] ΔE=+0.449999 accept=False
    core_region=3 delta_region=57 | E_before=0.950003 E_after=1.400002
    Tile-level changes (top 6 by |ΔE|):
      id=  839 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  836 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  837 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2243 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3423 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2241 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1866/3000 | Stage 150/428 | T=0.3 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 1876/3000 | Stage 160/428 | T=0.3 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1886/3000 | Stage 170/428 | T=0.3 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1896/3000 | Stage 180/428 | T=0.3 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1906.json (T=0.3)
   ⏳ Global 1906/3000 | Stage 190/428 | T=0.3 | Acc=5
🔁 Step 200: cluster=[918, 2190, 3328] ΔE=+0.099999 accept=True
    core_region=3 delta_region=53 | E_before=1.700006 E_after=1.800005
    Tile-level changes (top 6 by |ΔE|):
      id= 3328 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2190 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  916 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2192 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3281 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  917 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1916/3000 | Stage 200/428 | T=0.3 | Acc=7
✅ MC sweep: 9/10 accepted (90.0%), max drift: 0.000000
   ⏳ Global 1926/3000 | Stage 210/428 | T=0.3 | Acc=9
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1936/3000 | Stage 220/428 | T=0.3 | Acc=5
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1946/3000 | Stage 230/428 | T=0.3 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_1956.json (T=0.3)
   ⏳ Global 1956/3000 | Stage 240/428 | T=0.3 | Acc=6
🔁 Step 250: cluster=[2296, 2297, 4162] ΔE=+1.357999 accept=False
    core_region=3 delta_region=57 | E_before=1.800002 E_after=3.158001
    Tile-level changes (top 6 by |ΔE|):
      id=  832 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2296 THIN->THICK move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3424 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2297 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1966/3000 | Stage 250/428 | T=0.3 | Acc=7
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 1976/3000 | Stage 260/428 | T=0.3 | Acc=7
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 1986/3000 | Stage 270/428 | T=0.3 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 1996/3000 | Stage 280/428 | T=0.3 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2006.json (T=0.3)
   ⏳ Global 2006/3000 | Stage 290/428 | T=0.3 | Acc=6
🔁 Step 300: cluster=[910, 985, 2354] ΔE=+0.000000 accept=True
    core_region=3 delta_region=53 | E_before=1.750002 E_after=1.750002
    Tile-level changes (top 6 by |ΔE|):
      id= 2301 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  835 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2245 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2354 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4133 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 2016/3000 | Stage 300/428 | T=0.3 | Acc=8
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   ⏳ Global 2026/3000 | Stage 310/428 | T=0.3 | Acc=7
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2036/3000 | Stage 320/428 | T=0.3 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2046/3000 | Stage 330/428 | T=0.3 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2056.json (T=0.3)
   ⏳ Global 2056/3000 | Stage 340/428 | T=0.3 | Acc=6
🔁 Step 350: cluster=[900, 973, 2461] ΔE=+1.108000 accept=False
    core_region=3 delta_region=58 | E_before=2.450000 E_after=3.558000
    Tile-level changes (top 6 by |ΔE|):
      id=  973 THICK->THICK move= 0.3090 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3474 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2461 THIN->THICK move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  976 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  900 THICK->THIN move= 0.5878 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2066/3000 | Stage 350/428 | T=0.3 | Acc=4
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 2076/3000 | Stage 360/428 | T=0.3 | Acc=8
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2086/3000 | Stage 370/428 | T=0.3 | Acc=3
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2096/3000 | Stage 380/428 | T=0.3 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2106.json (T=0.3)
   ⏳ Global 2106/3000 | Stage 390/428 | T=0.3 | Acc=7
🔁 Step 400: cluster=[983, 2356, 4107] ΔE=+0.050000 accept=True
    core_region=3 delta_region=57 | E_before=1.750001 E_after=1.800001
    Tile-level changes (top 6 by |ΔE|):
      id= 4133 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  982 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2411 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2116/3000 | Stage 400/428 | T=0.3 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2126/3000 | Stage 410/428 | T=0.3 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2136/3000 | Stage 420/428 | T=0.3 | Acc=6
✅ MC sweep: 3/8 accepted (37.5%), max drift: 0.000000
   ⏳ Global 2144/3000 | Stage 428/428 | T=0.3 | Acc=3

🌡️ STAGE 6/7: Cooling to T=0.15 (428 steps)...
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2154.json (T=0.15)
   ⏳ Global 2154/3000 | Stage 10/428 | T=0.15 | Acc=8
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2164/3000 | Stage 20/428 | T=0.15 | Acc=3
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2174/3000 | Stage 30/428 | T=0.15 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2184/3000 | Stage 40/428 | T=0.15 | Acc=5
🔁 Step 50: cluster=[2457, 2458, 3565] ΔE=+2.365999 accept=False
    core_region=3 delta_region=57 | E_before=1.750001 E_after=4.116001
    Tile-level changes (top 6 by |ΔE|):
      id=  751 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2456 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2457 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3566 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  749 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3565 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2194/3000 | Stage 50/428 | T=0.15 | Acc=3
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2204.json (T=0.15)
   ⏳ Global 2204/3000 | Stage 60/428 | T=0.15 | Acc=6
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2214/3000 | Stage 70/428 | T=0.15 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2224/3000 | Stage 80/428 | T=0.15 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2234/3000 | Stage 90/428 | T=0.15 | Acc=5
🔁 Step 100: cluster=[838, 2242, 3422] ΔE=+1.407999 accept=False
    core_region=3 delta_region=58 | E_before=1.550002 E_after=2.958001
    Tile-level changes (top 6 by |ΔE|):
      id=  764 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3422 THIN->THICK move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3421 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2242 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3423 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  838 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2244/3000 | Stage 100/428 | T=0.15 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2254.json (T=0.15)
   ⏳ Global 2254/3000 | Stage 110/428 | T=0.15 | Acc=4
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2264/3000 | Stage 120/428 | T=0.15 | Acc=1
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 2274/3000 | Stage 130/428 | T=0.15 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2284/3000 | Stage 140/428 | T=0.15 | Acc=5
🔁 Step 150: cluster=[1050, 1126, 4053] ΔE=-0.200000 accept=True
    core_region=3 delta_region=60 | E_before=2.200001 E_after=2.000002
    Tile-level changes (top 6 by |ΔE|):
      id= 1122 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1126 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4053 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1050 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1047 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2413 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2294/3000 | Stage 150/428 | T=0.15 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2304.json (T=0.15)
   ⏳ Global 2304/3000 | Stage 160/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2314/3000 | Stage 170/428 | T=0.15 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2324/3000 | Stage 180/428 | T=0.15 | Acc=4
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2334/3000 | Stage 190/428 | T=0.15 | Acc=6
🔁 Step 200: cluster=[973, 975, 976] ΔE=-0.000000 accept=True
    core_region=3 delta_region=54 | E_before=1.850001 E_after=1.850001
    Tile-level changes (top 6 by |ΔE|):
      id=  975 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  900 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  973 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  976 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2344/3000 | Stage 200/428 | T=0.15 | Acc=1
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2354.json (T=0.15)
   ⏳ Global 2354/3000 | Stage 210/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2364/3000 | Stage 220/428 | T=0.15 | Acc=5
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2374/3000 | Stage 230/428 | T=0.15 | Acc=6
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2384/3000 | Stage 240/428 | T=0.15 | Acc=6
🔁 Step 250: cluster=[1062, 1064, 2250] ΔE=+0.099999 accept=True
    core_region=3 delta_region=56 | E_before=2.200003 E_after=2.300002
    Tile-level changes (top 6 by |ΔE|):
      id= 1062 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1065 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1064 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  988 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2250 THIN->THIN move= 0.8090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4131 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2394/3000 | Stage 250/428 | T=0.15 | Acc=6
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2404.json (T=0.15)
   ⏳ Global 2404/3000 | Stage 260/428 | T=0.15 | Acc=5
✅ MC sweep: 8/10 accepted (80.0%), max drift: 0.000000
   ⏳ Global 2414/3000 | Stage 270/428 | T=0.15 | Acc=8
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2424/3000 | Stage 280/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2434/3000 | Stage 290/428 | T=0.15 | Acc=5
🔁 Step 300: cluster=[1123, 2519, 2521] ΔE=+0.050000 accept=False
    core_region=3 delta_region=58 | E_before=2.350000 E_after=2.400000
    Tile-level changes (top 6 by |ΔE|):
      id= 1046 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2519 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2522 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3382 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2521 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1123 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2444/3000 | Stage 300/428 | T=0.15 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2454.json (T=0.15)
   ⏳ Global 2454/3000 | Stage 310/428 | T=0.15 | Acc=7
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2464/3000 | Stage 320/428 | T=0.15 | Acc=2
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2474/3000 | Stage 330/428 | T=0.15 | Acc=5
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2484/3000 | Stage 340/428 | T=0.15 | Acc=5
🔁 Step 350: cluster=[827, 2404, 3519] ΔE=-0.250000 accept=True
    core_region=3 delta_region=58 | E_before=1.700002 E_after=1.450002
    Tile-level changes (top 6 by |ΔE|):
      id= 4164 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  831 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2404 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  829 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  827 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4137 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2494/3000 | Stage 350/428 | T=0.15 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2504.json (T=0.15)
   ⏳ Global 2504/3000 | Stage 360/428 | T=0.15 | Acc=3
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2514/3000 | Stage 370/428 | T=0.15 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2524/3000 | Stage 380/428 | T=0.15 | Acc=5
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2534/3000 | Stage 390/428 | T=0.15 | Acc=4
🔁 Step 400: cluster=[826, 828, 3520] ΔE=-0.299999 accept=True
    core_region=3 delta_region=56 | E_before=1.450002 E_after=1.150003
    Tile-level changes (top 6 by |ΔE|):
      id= 4109 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3520 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2460 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4137 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  826 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2544/3000 | Stage 400/428 | T=0.15 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2554.json (T=0.15)
   ⏳ Global 2554/3000 | Stage 410/428 | T=0.15 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2564/3000 | Stage 420/428 | T=0.15 | Acc=5
✅ MC sweep: 5/8 accepted (62.5%), max drift: 0.000000
   ⏳ Global 2572/3000 | Stage 428/428 | T=0.15 | Acc=5

🌡️ STAGE 7/7: Cooling to T=0.05 (428 steps)...
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2582/3000 | Stage 10/428 | T=0.05 | Acc=4
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2592/3000 | Stage 20/428 | T=0.05 | Acc=5
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2602.json (T=0.05)
   ⏳ Global 2602/3000 | Stage 30/428 | T=0.05 | Acc=3
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2612/3000 | Stage 40/428 | T=0.05 | Acc=4
🔁 Step 50: cluster=[1045, 1046, 3383] ΔE=+0.100000 accept=False
    core_region=3 delta_region=58 | E_before=2.300001 E_after=2.400001
    Tile-level changes (top 6 by |ΔE|):
      id= 1046 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3382 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2518 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3431 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1045 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2465 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2622/3000 | Stage 50/428 | T=0.05 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2632/3000 | Stage 60/428 | T=0.05 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2642/3000 | Stage 70/428 | T=0.05 | Acc=4
✅ MC sweep: 7/10 accepted (70.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2652.json (T=0.05)
   ⏳ Global 2652/3000 | Stage 80/428 | T=0.05 | Acc=7
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2662/3000 | Stage 90/428 | T=0.05 | Acc=4
🔁 Step 100: cluster=[1062, 1064, 2250] ΔE=+0.099999 accept=False
    core_region=3 delta_region=57 | E_before=2.249999 E_after=2.349999
    Tile-level changes (top 6 by |ΔE|):
      id= 1065 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2250 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1064 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1063 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1062 THIN->THIN move= 0.8090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4131 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2672/3000 | Stage 100/428 | T=0.05 | Acc=1
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2682/3000 | Stage 110/428 | T=0.05 | Acc=5
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2692/3000 | Stage 120/428 | T=0.05 | Acc=2
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2702.json (T=0.05)
   ⏳ Global 2702/3000 | Stage 130/428 | T=0.05 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2712/3000 | Stage 140/428 | T=0.05 | Acc=4
🔁 Step 150: cluster=[1050, 1126, 4053] ΔE=+1.208000 accept=False
    core_region=3 delta_region=60 | E_before=2.100001 E_after=3.308001
    Tile-level changes (top 6 by |ΔE|):
      id= 1125 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4053 THIN->THICK move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1122 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1126 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3335 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1124 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2722/3000 | Stage 150/428 | T=0.05 | Acc=1
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2732/3000 | Stage 160/428 | T=0.05 | Acc=6
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2742/3000 | Stage 170/428 | T=0.05 | Acc=4
✅ MC sweep: 0/10 accepted (0.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2752.json (T=0.05)
   ⏳ Global 2752/3000 | Stage 180/428 | T=0.05 | Acc=0
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2762/3000 | Stage 190/428 | T=0.05 | Acc=5
🔁 Step 200: cluster=[842, 3327, 4213] ΔE=+0.449999 accept=False
    core_region=3 delta_region=54 | E_before=1.200002 E_after=1.650002
    Tile-level changes (top 6 by |ΔE|):
      id= 3327 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  841 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  843 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2189 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  840 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4213 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 0/10 accepted (0.0%), max drift: 0.000000
   ⏳ Global 2772/3000 | Stage 200/428 | T=0.05 | Acc=0
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2782/3000 | Stage 210/428 | T=0.05 | Acc=6
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2792/3000 | Stage 220/428 | T=0.05 | Acc=1
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2802.json (T=0.05)
   ⏳ Global 2802/3000 | Stage 230/428 | T=0.05 | Acc=2
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2812/3000 | Stage 240/428 | T=0.05 | Acc=5
🔁 Step 250: cluster=[826, 2459, 4110] ΔE=+1.108000 accept=False
    core_region=3 delta_region=60 | E_before=1.600002 E_after=2.708002
    Tile-level changes (top 6 by |ΔE|):
      id= 3521 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  826 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3520 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  824 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4110 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 6/10 accepted (60.0%), max drift: 0.000000
   ⏳ Global 2822/3000 | Stage 250/428 | T=0.05 | Acc=6
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2832/3000 | Stage 260/428 | T=0.05 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2842/3000 | Stage 270/428 | T=0.05 | Acc=4
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2852.json (T=0.05)
   ⏳ Global 2852/3000 | Stage 280/428 | T=0.05 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2862/3000 | Stage 290/428 | T=0.05 | Acc=3
🔁 Step 300: cluster=[768, 3419, 4241] ΔE=-0.000000 accept=True
    core_region=3 delta_region=54 | E_before=1.800001 E_after=1.800001
    Tile-level changes (top 6 by |ΔE|):
      id= 3420 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3419 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  768 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4241 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  693 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  694 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2872/3000 | Stage 300/428 | T=0.05 | Acc=4
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2882/3000 | Stage 310/428 | T=0.05 | Acc=1
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2892/3000 | Stage 320/428 | T=0.05 | Acc=3
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2902.json (T=0.05)
   ⏳ Global 2902/3000 | Stage 330/428 | T=0.05 | Acc=3
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2912/3000 | Stage 340/428 | T=0.05 | Acc=3
🔁 Step 350: cluster=[898, 2514, 2515] ΔE=+2.216000 accept=False
    core_region=3 delta_region=58 | E_before=1.900001 E_after=4.116001
    Tile-level changes (top 6 by |ΔE|):
      id=  898 THIN->THICK move= 0.5878 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2514 THICK->THICK move= 0.3090 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2516 THIN->THIN move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2515 THICK->THIN move= 0.5878 E:  0.0500-> 0.0540 ΔE=+  0.0040 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  899 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3521 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   ⏳ Global 2922/3000 | Stage 350/428 | T=0.05 | Acc=2
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2932/3000 | Stage 360/428 | T=0.05 | Acc=3
✅ MC sweep: 5/10 accepted (50.0%), max drift: 0.000000
   ⏳ Global 2942/3000 | Stage 370/428 | T=0.05 | Acc=5
✅ MC sweep: 2/10 accepted (20.0%), max drift: 0.000000
   📸 Snapshot: healing_step_2952.json (T=0.05)
   ⏳ Global 2952/3000 | Stage 380/428 | T=0.05 | Acc=2
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2962/3000 | Stage 390/428 | T=0.05 | Acc=4
🔁 Step 400: cluster=[2468, 2520, 3335] ΔE=+2.215999 accept=False
    core_region=3 delta_region=57 | E_before=2.000001 E_after=4.216001
    Tile-level changes (top 6 by |ΔE|):
      id= 2520 THIN->THICK move= 0.5878 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3335 THICK->THICK move= 0.3090 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2469 THIN->THIN move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2468 THICK->THIN move= 0.5878 E:  0.0500-> 0.0540 ΔE=+  0.0040 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1124 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1121 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 4/10 accepted (40.0%), max drift: 0.000000
   ⏳ Global 2972/3000 | Stage 400/428 | T=0.05 | Acc=4
✅ MC sweep: 3/10 accepted (30.0%), max drift: 0.000000
   ⏳ Global 2982/3000 | Stage 410/428 | T=0.05 | Acc=3
✅ MC sweep: 1/10 accepted (10.0%), max drift: 0.000000
   ⏳ Global 2992/3000 | Stage 420/428 | T=0.05 | Acc=1
✅ MC sweep: 1/8 accepted (12.5%), max drift: 0.000000
   📸 Snapshot: healing_step_3000.json (T=0.05)
   ⏳ Global 3000/3000 | Stage 428/428 | T=0.05 | Acc=1
------------------------------------------------------------
RESULTS: 23 -> 23 (Efficiency: 0.0%)
Drift: 0.000000

💾 Saved Full State: healing_base_run_001.json (for viz)
📄 Saved Summary   : healing_base_run_001_summary.json (for stats)
📌 Latest: data/experiments/healing/latest.json
randa@Randa:quasi-phason$
