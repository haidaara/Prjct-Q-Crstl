randa@Randa:quasi-phason$ python scripts/validation/validate_energy.py
⚡ ENERGY ENGINE VALIDATOR
============================================================

1) 🔄 Determinism
   ✅ PASS: deterministic (E=307.855000)

2) ⚖️  Convention (Total vs Sum(Local))
   ✅ PASS: convention consistent

3) 🌊 MC drift (internal + ground truth)
✅ MC sweep: 96/100 accepted (96.0%), max drift: 0.000000
   MC internal max drift: 0.000000
   True final drift:      0.000000
   ✅ PASS: drift contained

🎉 ALL PHYSICS CHECKS PASSED.
randa@Randa:quasi-phason$ python scripts/experiments/0
01_generate_tiling.py           03_run_healing_test.py          06_run_phase2_batch.py
01_prepare_processed_tiling.py  04_run_growth.py
02_generate_obstacles.py        05_temperature_sweep.py
randa@Randa:quasi-phason$ python scripts/experiments/03_run_healing_test.py
🧪 EXPERIMENT 03: PHASON HEALING (Refactored)
============================================================
📥 Input tiling: data/processed/penrose_tiling_energy_initialized.json
📤 Output dir : data/experiments/healing
⚙️  scenario=base seed_radius=10.0 num_defects=15 defect_threshold=1.5
⚙️  MC: T=0.8 steps=200 R=4 verify_energy=True base_steps=100
------------------------------------------------------------
  🔨 Creating 15 defects (Strict Mode)...
  ✅ Created 0 defects.
  Initial Defects: 0
🎲 Starting Monte Carlo...
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 1/200 (0.5%) | accepted=1 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 2/200 (1.0%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 3/200 (1.5%) | accepted=3 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 4/200 (2.0%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 5/200 (2.5%) | accepted=5 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 6/200 (3.0%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 7/200 (3.5%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 8/200 (4.0%) | accepted=8 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 9/200 (4.5%) | accepted=9 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 10/200 (5.0%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 11/200 (5.5%) | accepted=11 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 12/200 (6.0%) | accepted=12 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 13/200 (6.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 14/200 (7.0%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 15/200 (7.5%) | accepted=15 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 16/200 (8.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 17/200 (8.5%) | accepted=17 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 18/200 (9.0%) | accepted=18 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 19/200 (9.5%) | accepted=19 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 20/200 (10.0%) | accepted=20 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 21/200 (10.5%) | accepted=21 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 22/200 (11.0%) | accepted=22 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 23/200 (11.5%) | accepted=23 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 24/200 (12.0%) | accepted=24 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 25/200 (12.5%) | accepted=25 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 26/200 (13.0%) | accepted=25 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 27/200 (13.5%) | accepted=26 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 28/200 (14.0%) | accepted=27 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 29/200 (14.5%) | accepted=28 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 30/200 (15.0%) | accepted=29 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 31/200 (15.5%) | accepted=30 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 32/200 (16.0%) | accepted=31 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 33/200 (16.5%) | accepted=32 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 34/200 (17.0%) | accepted=33 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 35/200 (17.5%) | accepted=34 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 36/200 (18.0%) | accepted=35 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 37/200 (18.5%) | accepted=36 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 38/200 (19.0%) | accepted=37 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 39/200 (19.5%) | accepted=38 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 40/200 (20.0%) | accepted=39 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 41/200 (20.5%) | accepted=40 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 42/200 (21.0%) | accepted=41 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 43/200 (21.5%) | accepted=42 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 44/200 (22.0%) | accepted=43 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 45/200 (22.5%) | accepted=44 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 46/200 (23.0%) | accepted=45 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 47/200 (23.5%) | accepted=46 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 48/200 (24.0%) | accepted=47 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 49/200 (24.5%) | accepted=48 | max_drift=0.000000
🔁 Step 50: cluster=[2511, 2512, 3567] ΔE=+0.000000 accept=True
    core_region=4 delta_region=85 | E_before=3.650000 E_after=3.650000
    Tile-level changes (top 6 by |ΔE|):
      id=  822 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2512 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3568 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4111 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2510 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3567 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 50/200 (25.0%) | accepted=49 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 51/200 (25.5%) | accepted=50 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 52/200 (26.0%) | accepted=50 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 53/200 (26.5%) | accepted=51 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 54/200 (27.0%) | accepted=52 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 55/200 (27.5%) | accepted=53 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 56/200 (28.0%) | accepted=54 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 57/200 (28.5%) | accepted=55 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 58/200 (29.0%) | accepted=56 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 59/200 (29.5%) | accepted=57 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 60/200 (30.0%) | accepted=58 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 61/200 (30.5%) | accepted=59 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 62/200 (31.0%) | accepted=60 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 63/200 (31.5%) | accepted=61 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 64/200 (32.0%) | accepted=62 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 65/200 (32.5%) | accepted=63 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 66/200 (33.0%) | accepted=64 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 67/200 (33.5%) | accepted=65 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 68/200 (34.0%) | accepted=66 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 69/200 (34.5%) | accepted=67 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 70/200 (35.0%) | accepted=68 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 71/200 (35.5%) | accepted=69 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 72/200 (36.0%) | accepted=70 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 73/200 (36.5%) | accepted=71 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 74/200 (37.0%) | accepted=71 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 75/200 (37.5%) | accepted=72 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 76/200 (38.0%) | accepted=73 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 77/200 (38.5%) | accepted=74 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 78/200 (39.0%) | accepted=75 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 79/200 (39.5%) | accepted=76 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 80/200 (40.0%) | accepted=77 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 81/200 (40.5%) | accepted=78 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 82/200 (41.0%) | accepted=79 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 83/200 (41.5%) | accepted=80 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 84/200 (42.0%) | accepted=81 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 85/200 (42.5%) | accepted=82 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 86/200 (43.0%) | accepted=83 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 87/200 (43.5%) | accepted=84 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 88/200 (44.0%) | accepted=84 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 89/200 (44.5%) | accepted=85 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 90/200 (45.0%) | accepted=86 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 91/200 (45.5%) | accepted=87 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 92/200 (46.0%) | accepted=87 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 93/200 (46.5%) | accepted=88 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 94/200 (47.0%) | accepted=89 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 95/200 (47.5%) | accepted=89 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 96/200 (48.0%) | accepted=89 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 97/200 (48.5%) | accepted=90 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 98/200 (49.0%) | accepted=91 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 99/200 (49.5%) | accepted=92 | max_drift=0.000000
🔁 Step 100: cluster=[2463, 2464, 3429] ΔE=+0.000000 accept=True
    core_region=4 delta_region=88 | E_before=3.550001 E_after=3.550001
    Tile-level changes (top 6 by |ΔE|):
      id=  975 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4080 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2464 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2463 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 100/200 (50.0%) | accepted=93 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 101/200 (50.5%) | accepted=93 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 102/200 (51.0%) | accepted=94 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 103/200 (51.5%) | accepted=95 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 104/200 (52.0%) | accepted=96 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 105/200 (52.5%) | accepted=97 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 106/200 (53.0%) | accepted=98 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 107/200 (53.5%) | accepted=99 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 108/200 (54.0%) | accepted=99 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 109/200 (54.5%) | accepted=100 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 110/200 (55.0%) | accepted=100 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 111/200 (55.5%) | accepted=101 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 112/200 (56.0%) | accepted=102 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 113/200 (56.5%) | accepted=103 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 114/200 (57.0%) | accepted=104 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 115/200 (57.5%) | accepted=105 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 116/200 (58.0%) | accepted=106 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 117/200 (58.5%) | accepted=107 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 118/200 (59.0%) | accepted=108 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 119/200 (59.5%) | accepted=109 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 120/200 (60.0%) | accepted=110 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 121/200 (60.5%) | accepted=111 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 122/200 (61.0%) | accepted=112 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 123/200 (61.5%) | accepted=113 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 124/200 (62.0%) | accepted=114 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 125/200 (62.5%) | accepted=115 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 126/200 (63.0%) | accepted=116 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 127/200 (63.5%) | accepted=117 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 128/200 (64.0%) | accepted=118 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 129/200 (64.5%) | accepted=119 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 130/200 (65.0%) | accepted=120 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 131/200 (65.5%) | accepted=121 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 132/200 (66.0%) | accepted=122 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 133/200 (66.5%) | accepted=123 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 134/200 (67.0%) | accepted=124 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 135/200 (67.5%) | accepted=125 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 136/200 (68.0%) | accepted=126 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 137/200 (68.5%) | accepted=127 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 138/200 (69.0%) | accepted=128 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 139/200 (69.5%) | accepted=128 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 140/200 (70.0%) | accepted=129 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 141/200 (70.5%) | accepted=130 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 142/200 (71.0%) | accepted=131 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 143/200 (71.5%) | accepted=132 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 144/200 (72.0%) | accepted=133 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 145/200 (72.5%) | accepted=134 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 146/200 (73.0%) | accepted=135 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 147/200 (73.5%) | accepted=136 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 148/200 (74.0%) | accepted=137 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 149/200 (74.5%) | accepted=138 | max_drift=0.000000
🔁 Step 150: cluster=[2359, 2360, 4077] ΔE=+0.200000 accept=False
    core_region=4 delta_region=83 | E_before=5.366001 E_after=5.566000
    Tile-level changes (top 6 by |ΔE|):
      id= 1131 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1205 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3244 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2359 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1133 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4077 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 150/200 (75.0%) | accepted=138 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 151/200 (75.5%) | accepted=139 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 152/200 (76.0%) | accepted=140 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 153/200 (76.5%) | accepted=140 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 154/200 (77.0%) | accepted=141 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 155/200 (77.5%) | accepted=142 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 156/200 (78.0%) | accepted=143 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 157/200 (78.5%) | accepted=144 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 158/200 (79.0%) | accepted=145 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 159/200 (79.5%) | accepted=146 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 160/200 (80.0%) | accepted=147 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 161/200 (80.5%) | accepted=148 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 162/200 (81.0%) | accepted=149 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 163/200 (81.5%) | accepted=150 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 164/200 (82.0%) | accepted=151 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 165/200 (82.5%) | accepted=152 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 166/200 (83.0%) | accepted=153 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 167/200 (83.5%) | accepted=153 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 168/200 (84.0%) | accepted=153 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 169/200 (84.5%) | accepted=154 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 170/200 (85.0%) | accepted=155 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 171/200 (85.5%) | accepted=156 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 172/200 (86.0%) | accepted=157 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 173/200 (86.5%) | accepted=158 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 174/200 (87.0%) | accepted=159 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 175/200 (87.5%) | accepted=160 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 176/200 (88.0%) | accepted=161 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 177/200 (88.5%) | accepted=162 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 178/200 (89.0%) | accepted=163 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 179/200 (89.5%) | accepted=164 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 180/200 (90.0%) | accepted=164 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 181/200 (90.5%) | accepted=165 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 182/200 (91.0%) | accepted=166 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 183/200 (91.5%) | accepted=167 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 184/200 (92.0%) | accepted=168 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 185/200 (92.5%) | accepted=169 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 186/200 (93.0%) | accepted=170 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 187/200 (93.5%) | accepted=171 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 188/200 (94.0%) | accepted=172 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 189/200 (94.5%) | accepted=173 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 190/200 (95.0%) | accepted=174 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 191/200 (95.5%) | accepted=175 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 192/200 (96.0%) | accepted=176 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 193/200 (96.5%) | accepted=177 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 194/200 (97.0%) | accepted=178 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 195/200 (97.5%) | accepted=179 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 196/200 (98.0%) | accepted=180 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 197/200 (98.5%) | accepted=181 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 198/200 (99.0%) | accepted=182 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 199/200 (99.5%) | accepted=182 | max_drift=0.000000
🔁 Step 200: cluster=[3562, 3563, 4191] ΔE=-0.000000 accept=True
    core_region=4 delta_region=81 | E_before=2.700001 E_after=2.700001
    Tile-level changes (top 6 by |ΔE|):
      id= 4191 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3562 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  679 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2345 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  682 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 200/200 (100.0%) | accepted=183 | max_drift=0.000000
✅ MC finished in 35.58s | acceptance=91.5% | max_drift=0.000000
------------------------------------------------------------
RESULTS: 0 -> 0 (Efficiency: 0.0%)
Drift: 0.000000

💾 Saved: data/experiments/healing/healing_base_run_030.json
📌 Latest: data/experiments/healing/latest.json
randa@Randa:quasi-phason$ python scripts/experiments/04_run_growth.py
🧪 Running growth experiment...
==================================================
🔧 debug: verbosity=2, progress_every=1, trace_every=50
Experiment: growth_pores_d0p000_run_008
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 5 growth steps...

  Step 1/5
🌿 Growth step 0...
   Running 200 MC steps for healing...
🔁 Step 50: cluster=[3519, 3520, 4136] ΔE=-0.050000 accept=True
    core_region=4 delta_region=85 | E_before=3.550000 E_after=3.500001
    Tile-level changes (top 6 by |ΔE|):
      id= 4137 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3520 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2404 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2403 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4136 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 100: cluster=[828, 3519, 3520] ΔE=+0.050000 accept=True
    core_region=4 delta_region=87 | E_before=3.900000 E_after=3.950000
    Tile-level changes (top 6 by |ΔE|):
      id= 4137 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  827 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3520 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2404 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 150: cluster=[903, 2406, 3428] ΔE=+0.349999 accept=False
    core_region=4 delta_region=82 | E_before=2.400002 E_after=2.750002
    Tile-level changes (top 6 by |ΔE|):
      id= 3428 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2462 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  903 THIN->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3472 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  902 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 200: cluster=[986, 2301, 3331] ΔE=-0.000000 accept=True
    core_region=4 delta_region=83 | E_before=3.550000 E_after=3.550000
    Tile-level changes (top 6 by |ΔE|):
      id= 3331 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2302 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  986 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  987 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 160/200 accepted (80.0%), max drift: 0.000000
✅ Growth step 1: added 32 tiles
    New tiles: 32, Defects: 0
    Acceptance rate: 80.0%

  Step 2/5
🌿 Growth step 1...
   Running 200 MC steps for healing...
🔁 Step 250: cluster=[832, 833, 3470] ΔE=+0.349999 accept=True
    core_region=4 delta_region=80 | E_before=4.156001 E_after=4.506000
    Tile-level changes (top 6 by |ΔE|):
      id= 3518 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3470 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  831 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  833 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2351 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 300: cluster=[982, 983, 3332] ΔE=+0.100000 accept=True
    core_region=4 delta_region=84 | E_before=4.558001 E_after=4.658000
    Tile-level changes (top 6 by |ΔE|):
      id= 3379 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3332 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3377 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2355 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 350: cluster=[986, 2302, 3331] ΔE=-1.358000 accept=True
    core_region=4 delta_region=79 | E_before=4.558000 E_after=3.200000
    Tile-level changes (top 6 by |ΔE|):
      id=  984 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THICK->THICK move= 0.0000 E:  0.0520-> 0.0000 ΔE= -0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  986 THIN->THIN move= 0.8090 E:  0.0520-> 0.0000 ΔE= -0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4132 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  987 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2302 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 400: cluster=[826, 828, 4109] ΔE=-0.000000 accept=True
    core_region=4 delta_region=81 | E_before=3.000001 E_after=3.000000
    Tile-level changes (top 6 by |ΔE|):
      id= 4109 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  826 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  902 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2459 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  825 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 160/200 accepted (80.0%), max drift: 0.000000
✅ Growth step 2: added 39 tiles
    New tiles: 39, Defects: 0
    Acceptance rate: 80.0%

  Step 3/5
🌿 Growth step 2...
   Running 200 MC steps for healing...
🔁 Step 450: cluster=[982, 983, 3332] ΔE=+0.000000 accept=True
    core_region=4 delta_region=80 | E_before=3.250000 E_after=3.250001
    Tile-level changes (top 6 by |ΔE|):
      id=  986 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3332 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3377 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2355 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 500: cluster=[2352, 3426, 4134] ΔE=-1.008000 accept=True
    core_region=4 delta_region=83 | E_before=4.558000 E_after=3.550000
    Tile-level changes (top 6 by |ΔE|):
      id= 2352 THICK->THICK move= 0.3090 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4135 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3426 THICK->THIN move= 0.5878 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2351 THICK->THICK move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THIN->THIN move= 0.0000 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4134 THIN->THICK move= 0.5878 E:  0.0520-> 0.0500 ΔE= -0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 550: cluster=[683, 2346, 3517] ΔE=-0.000000 accept=True
    core_region=4 delta_region=84 | E_before=4.310001 E_after=4.310001
    Tile-level changes (top 6 by |ΔE|):
      id= 3517 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2346 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3516 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  758 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  683 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  682 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 600: cluster=[832, 3424, 4161] ΔE=+3.223999 accept=False
    core_region=4 delta_region=79 | E_before=2.950001 E_after=6.174001
    Tile-level changes (top 6 by |ΔE|):
      id= 4161 THIN->THICK move= 0.5878 E:  0.0000-> 1.1040 ΔE=+  1.1040 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.3090 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3425 THIN->THIN move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3424 THICK->THIN move= 0.5878 E:  0.0500-> 0.0540 ΔE=+  0.0040 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2298 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 160/200 accepted (80.0%), max drift: 0.000000
✅ Growth step 3: added 50 tiles
    New tiles: 50, Defects: 0
    Acceptance rate: 80.0%

  Step 4/5
🌿 Growth step 3...
   Running 200 MC steps for healing...
🔁 Step 650: cluster=[974, 975, 2464] ΔE=-0.050000 accept=True
    core_region=4 delta_region=84 | E_before=3.250001 E_after=3.200001
    Tile-level changes (top 6 by |ΔE|):
      id= 2518 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2463 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  975 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2464 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  976 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 700: cluster=[827, 828, 3519] ΔE=+0.000000 accept=True
    core_region=4 delta_region=84 | E_before=3.300000 E_after=3.300001
    Tile-level changes (top 6 by |ΔE|):
      id=  827 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2404 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2460 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4109 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 750: cluster=[754, 2402, 3565] ΔE=+0.050000 accept=True
    core_region=4 delta_region=84 | E_before=3.750000 E_after=3.800000
    Tile-level changes (top 6 by |ΔE|):
      id= 3520 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  752 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2401 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2402 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3565 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3564 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 800: cluster=[754, 2402, 3565] ΔE=-0.050000 accept=True
    core_region=4 delta_region=85 | E_before=3.550001 E_after=3.500001
    Tile-level changes (top 6 by |ΔE|):
      id= 3520 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  752 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2401 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2402 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3565 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3564 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 183/200 accepted (91.5%), max drift: 0.000000
✅ Growth step 4: added 60 tiles
    New tiles: 60, Defects: 0
    Acceptance rate: 91.5%

  Step 5/5
🌿 Growth step 4...
   Running 200 MC steps for healing...
🔁 Step 850: cluster=[3521, 3522, 4110] ΔE=+0.000000 accept=True
    core_region=4 delta_region=81 | E_before=3.100001 E_after=3.100001
    Tile-level changes (top 6 by |ΔE|):
      id=  825 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3521 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  902 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  822 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  824 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3522 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 900: cluster=[2345, 3562, 3563] ΔE=+0.000000 accept=True
    core_region=4 delta_region=80 | E_before=2.950001 E_after=2.950001
    Tile-level changes (top 6 by |ΔE|):
      id= 2344 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4191 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  680 THIN->THIN move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2345 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3563 THIN->THICK move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2347 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 950: cluster=[1057, 1058, 2357] ΔE=+0.100000 accept=False
    core_region=4 delta_region=82 | E_before=2.850001 E_after=2.950001
    Tile-level changes (top 6 by |ΔE|):
      id= 1058 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1055 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2357 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1059 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1057 THIN->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1000: cluster=[2295, 2350, 4162] ΔE=+1.207999 accept=False
    core_region=4 delta_region=84 | E_before=3.000002 E_after=4.208001
    Tile-level changes (top 6 by |ΔE|):
      id= 3468 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  757 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2295 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2350 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  760 THIN->THIN move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 169/200 accepted (84.5%), max drift: 0.000000
✅ Growth step 5: added 60 tiles
    New tiles: 60, Defects: 0
    Acceptance rate: 84.5%

✅ Experiment complete!
📊 Results saved to: data/experiments/growth/growth_pores_d0p000_run_008.json

==================================================
📈 EXPERIMENT SUMMARY:
  Total steps: 5
  Final energy: 306.01
  Final defect density: 0.000
randa@Randa:quasi-phason$