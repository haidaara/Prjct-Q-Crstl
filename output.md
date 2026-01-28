randa@Randa:quasi-phason$ python scripts/experiments/03_obstacle_healing.py --config configs/obstacle_healing.toml
===============================================================================
OBSTACLE HEALING EXPERIMENT - START
===============================================================================
Input: data/obstacles/pores/pores_density_0.1.json
Run dir: data/experiments/obstacle_healing/run_001
Tiles: total=4406 measurement=2918 active=3422
Obstacle mode: pores  meta_type=pores density=0.1
Defect threshold: local_energy > 1.5
-------------------------------------------------------------------------------
BASELINE: E=824.920833 defects=131/2918
-------------------------------------------------------------------------------
DAMAGE PHASE
-------------------------------------------------------------------------------
Target additional defects: +15 (above baseline 131)
Heating at T=5.0 (max_steps=500, check_every=50)
🔁 Step 50: cluster=[1471, 1472, 2917] ΔE=+0.000000 accept=True
    core_region=3 delta_region=53 | E_before=2.087833 E_after=2.087833
    Tile-level changes (top 6 by |ΔE|):
      id= 3889 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1471 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2918 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2917 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1473 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1470 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step    50: defects=130/2918 target=146
🔁 Step 100: cluster=[1437, 1438, 4046] ΔE=+0.000000 accept=True
    core_region=3 delta_region=59 | E_before=1.250000 E_after=1.250000
    Tile-level changes (top 6 by |ΔE|):
      id= 1438 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1439 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4046 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2261 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4019 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1436 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   100: defects=130/2918 target=146
🔁 Step 150: cluster=[2902, 2903, 3661] ΔE=+0.000000 accept=True
    core_region=3 delta_region=56 | E_before=11.262333 E_after=11.262333
    Tile-level changes (top 6 by |ΔE|):
      id=  946 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1022 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2902 THICK->THIN move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3660 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3662 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2903 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   150: defects=129/2918 target=146
🔁 Step 200: cluster=[1443, 1444, 4071] ΔE=+0.025000 accept=True
    core_region=3 delta_region=54 | E_before=1.100000 E_after=1.125000
    Tile-level changes (top 6 by |ΔE|):
      id= 3053 THIN->THIN move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1443 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4071 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3076 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1442 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1444 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   200: defects=127/2918 target=146
🔁 Step 250: cluster=[1391, 1392, 3891] ΔE=+0.025000 accept=True
    core_region=3 delta_region=54 | E_before=8.111334 E_after=8.136334
    Tile-level changes (top 6 by |ΔE|):
      id= 1465 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3491 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3891 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1391 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1392 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3445 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   250: defects=128/2918 target=146
🔁 Step 300: cluster=[325, 2013, 3595] ΔE=-0.075000 accept=True
    core_region=3 delta_region=56 | E_before=1.275000 E_after=1.200000
    Tile-level changes (top 6 by |ΔE|):
      id=  324 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3595 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2012 THIN->THIN move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  326 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2013 THIN->THIN move= 0.8090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  327 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   300: defects=126/2918 target=146
🔁 Step 350: cluster=[1985, 1986, 3070] ΔE=+0.025000 accept=True
    core_region=3 delta_region=60 | E_before=1.300000 E_after=1.325000
    Tile-level changes (top 6 by |ΔE|):
      id= 3071 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1230 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3070 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1986 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1985 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4179 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   350: defects=127/2918 target=146
🔁 Step 400: cluster=[332, 333, 4361] ΔE=-0.025000 accept=True
    core_region=3 delta_region=59 | E_before=1.275000 E_after=1.250000
    Tile-level changes (top 6 by |ΔE|):
      id=  406 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4361 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  332 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1912 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  334 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3550 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   400: defects=126/2918 target=146
🔁 Step 450: cluster=[2425, 2426, 3109] ΔE=+0.000000 accept=True
    core_region=3 delta_region=60 | E_before=1.275000 E_after=1.275000
    Tile-level changes (top 6 by |ΔE|):
      id= 2426 THICK->THIN move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3110 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3108 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1579 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1503 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3109 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   450: defects=126/2918 target=146
🔁 Step 500: cluster=[1538, 1539, 3400] ΔE=-0.075000 accept=True
    core_region=3 delta_region=50 | E_before=10.994667 E_after=10.919667
    Tile-level changes (top 6 by |ΔE|):
      id= 3882 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1537 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3400 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3875 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1540 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1538 THIN->THIN move= 0.8090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  damage step   500: defects=126/2918 target=146
DAMAGE DONE: defects=126/2918 steps=500
-------------------------------------------------------------------------------
HEALING PHASE
-------------------------------------------------------------------------------
Stage 1/7: T5.0  T=5.0  steps=100
🔁 Step 550: cluster=[599, 600, 4167] ΔE=-0.225000 accept=True
    core_region=3 delta_region=51 | E_before=8.065833 E_after=7.840834
    Tile-level changes (top 6 by |ΔE|):
      id= 3648 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3647 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  598 THIN->THIN move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2451 THIN->THIN move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  599 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  601 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 600: cluster=[1927, 1928, 3192] ΔE=+0.025000 accept=True
    core_region=3 delta_region=61 | E_before=1.226000 E_after=1.251000
    Tile-level changes (top 6 by |ΔE|):
      id= 1927 THICK->THIN move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  934 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  858 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3192 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3193 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  933 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 126→125 (Δ=-1)  E 816.668→817.405  drift_max=2.18e-11
Stage 2/7: T2.5  T=2.5  steps=200
🔁 Step 650: cluster=[3082, 3083, 3973] ΔE=-1.029000 accept=True
    core_region=3 delta_region=56 | E_before=2.329000 E_after=1.300000
    Tile-level changes (top 6 by |ΔE|):
      id= 3059 THICK->THICK move= 0.0000 E:  1.0500-> 0.0250 ΔE= -1.0250 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3972 THIN->THIN move= 0.0000 E:  0.0260-> 0.0250 ΔE= -0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3058 THICK->THICK move= 0.0000 E:  0.0260-> 0.0250 ΔE= -0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1654 THICK->THICK move= 0.0000 E:  0.0260-> 0.0250 ΔE= -0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3082 THICK->THIN move= 0.5878 E:  0.0260-> 0.0250 ΔE= -0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3973 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 700: cluster=[1623, 1624, 3261] ΔE=+0.075000 accept=True
    core_region=3 delta_region=57 | E_before=3.201000 E_after=3.276000
    Tile-level changes (top 6 by |ΔE|):
      id= 1623 THIN->THICK move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3261 THICK->THIN move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1625 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2921 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3887 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1624 THIN->THIN move= 0.8090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 750: cluster=[1485, 1486, 3255] ΔE=+0.150000 accept=True
    core_region=3 delta_region=48 | E_before=9.708334 E_after=9.858334
    Tile-level changes (top 6 by |ΔE|):
      id= 3923 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2748 THIN->THIN move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1485 THIN->THIN move= 0.8090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1484 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2693 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1486 THICK->THIN move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 800: cluster=[1631, 1632, 2806] ΔE=-0.050000 accept=True
    core_region=3 delta_region=58 | E_before=2.133334 E_after=2.083334
    Tile-level changes (top 6 by |ΔE|):
      id= 1632 THICK->THIN move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1630 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2807 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1631 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3896 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1633 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 125→127 (Δ=+2)  E 817.405→823.414  drift_max=2.54e-11
Stage 3/7: T1.2  T=1.2  steps=200
🔁 Step 850: cluster=[73, 3826, 3827] ΔE=+0.000000 accept=True
    core_region=3 delta_region=54 | E_before=9.139333 E_after=9.139333
    Tile-level changes (top 6 by |ΔE|):
      id=   73 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3827 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2490 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3826 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2491 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2489 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 900: cluster=[3587, 3588, 4393] ΔE=-0.000000 accept=True
    core_region=3 delta_region=56 | E_before=7.054000 E_after=7.054000
    Tile-level changes (top 6 by |ΔE|):
      id=  192 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1827 THIN->THIN move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  189 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3587 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4393 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  116 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 950: cluster=[1548, 2886, 2887] ΔE=-0.025000 accept=True
    core_region=3 delta_region=55 | E_before=9.219834 E_after=9.194834
    Tile-level changes (top 6 by |ΔE|):
      id= 2919 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2885 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1548 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2887 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2886 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1550 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1000: cluster=[743, 744, 2564] ΔE=+0.066667 accept=True
    core_region=3 delta_region=38 | E_before=8.728000 E_after=8.794667
    Tile-level changes (top 6 by |ΔE|):
      id=  744 THIN->THIN move= 0.8090 E:  0.0250-> 1.0000 ΔE=+  0.9750 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  743 THICK->THIN move= 0.3090 E:  2.0000-> 1.0333 ΔE= -0.9667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3650 THICK->THICK move= 0.0000 E:  1.0000-> 1.0333 ΔE=+  0.0333 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  670 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  745 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2564 THIN->THICK move= 0.3090 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 127→127 (Δ=+0)  E 823.414→817.417  drift_max=2.83e-11
Stage 4/7: T0.6  T=0.6  steps=200
🔁 Step 1050: cluster=[2315, 2316, 3107] ΔE=+0.025000 accept=True
    core_region=3 delta_region=54 | E_before=1.075000 E_after=1.100000
    Tile-level changes (top 6 by |ΔE|):
      id= 4046 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1509 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1435 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2316 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3106 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3107 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1100: cluster=[186, 187, 4385] ΔE=+0.000000 accept=True
    core_region=3 delta_region=58 | E_before=1.350000 E_after=1.350000
    Tile-level changes (top 6 by |ΔE|):
      id= 4385 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  187 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  113 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  186 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  185 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1864 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1150: cluster=[325, 2013, 3595] ΔE=-0.125000 accept=True
    core_region=3 delta_region=57 | E_before=1.300000 E_after=1.175000
    Tile-level changes (top 6 by |ΔE|):
      id= 3595 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  326 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2012 THIN->THIN move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  325 THIN->THIN move= 0.8090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2013 THICK->THIN move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2065 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1200: cluster=[1203, 1204, 2416] ΔE=-0.125000 accept=True
    core_region=3 delta_region=60 | E_before=1.952001 E_after=1.827001
    Tile-level changes (top 6 by |ΔE|):
      id= 2416 THIN->THIN move= 0.8090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1202 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2417 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2415 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1203 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4077 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 127→126 (Δ=-1)  E 817.417→807.855  drift_max=3.05e-11
Stage 5/7: T0.3  T=0.3  steps=200
🔁 Step 1250: cluster=[2488, 2489, 3840] ΔE=-0.058333 accept=True
    core_region=3 delta_region=46 | E_before=16.149667 E_after=16.091333
    Tile-level changes (top 6 by |ΔE|):
      id=   12 THICK->THICK move= 0.0000 E:  1.0343-> 1.0010 ΔE= -0.0333 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=True
      id= 3841 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3839 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2488 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2489 THICK->THIN move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=   73 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1300: cluster=[1155, 1156, 4207] ΔE=+1.029000 accept=False
    core_region=3 delta_region=57 | E_before=1.052000 E_after=2.081000
    Tile-level changes (top 6 by |ΔE|):
      id= 1081 THIN->THIN move= 0.0000 E:  0.0250-> 1.0500 ΔE=+  1.0250 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1982 THICK->THICK move= 0.0000 E:  0.0250-> 0.0260 ΔE=+  0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3124 THICK->THICK move= 0.0000 E:  0.0250-> 0.0260 ΔE=+  0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1082 THICK->THICK move= 0.0000 E:  0.0250-> 0.0260 ΔE=+  0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4207 THICK->THICK move= 0.3090 E:  0.0250-> 0.0260 ΔE=+  0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3095 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1350: cluster=[774, 775, 4264] ΔE=+0.000000 accept=True
    core_region=3 delta_region=54 | E_before=1.150000 E_after=1.150000
    Tile-level changes (top 6 by |ΔE|):
      id=  774 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  775 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2025 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  772 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2079 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4264 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1400: cluster=[2140, 2141, 3238] ΔE=+0.025000 accept=True
    core_region=3 delta_region=58 | E_before=1.225000 E_after=1.250000
    Tile-level changes (top 6 by |ΔE|):
      id= 3239 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2142 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  993 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3238 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4184 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2141 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 126→125 (Δ=-1)  E 807.855→800.819  drift_max=3.27e-11
Stage 6/7: T0.15  T=0.15  steps=200
🔁 Step 1450: cluster=[1179, 1180, 3484] ΔE=-0.125000 accept=True
    core_region=3 delta_region=42 | E_before=13.006000 E_after=12.881000
    Tile-level changes (top 6 by |ΔE|):
      id= 1179 THIN->THIN move= 0.8090 E:  1.0333-> 0.0000 ΔE= -1.0333 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1180 THIN->THICK move= 0.3090 E:  1.0333-> 2.0000 ΔE=+  0.9667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2792 THICK->THICK move= 0.0000 E:  1.0333-> 1.0000 ΔE= -0.0333 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2791 THIN->THIN move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1178 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3484 THICK->THIN move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1500: cluster=[1424, 1425, 2476] ΔE=+0.025000 accept=False
    core_region=3 delta_region=58 | E_before=2.076000 E_after=2.101000
    Tile-level changes (top 6 by |ΔE|):
      id= 1423 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1425 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3173 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1424 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3209 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2476 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1550: cluster=[2707, 2708, 3856] ΔE=-0.025000 accept=True
    core_region=3 delta_region=58 | E_before=5.883334 E_after=5.858334
    Tile-level changes (top 6 by |ΔE|):
      id= 2762 THICK->THICK move= 0.0000 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2708 THICK->THIN move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4202 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  133 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  135 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3856 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1600: cluster=[700, 701, 702] ΔE=+2.208000 accept=False
    core_region=3 delta_region=58 | E_before=1.000001 E_after=3.208000
    Tile-level changes (top 6 by |ΔE|):
      id= 4287 THICK->THICK move= 0.0000 E:  0.0250-> 1.0500 ΔE=+  1.0250 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2023 THICK->THICK move= 0.0000 E:  0.0250-> 1.0500 ΔE=+  1.0250 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3368 THICK->THICK move= 0.0000 E:  0.0000-> 0.0260 ΔE=+  0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3369 THICK->THICK move= 0.0000 E:  0.0000-> 0.0260 ΔE=+  0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  701 THICK->THIN move= 0.3090 E:  0.0000-> 0.0260 ΔE=+  0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  702 THIN->THIN move= 0.8090 E:  0.0000-> 0.0260 ΔE=+  0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 125→126 (Δ=+1)  E 800.819→795.232  drift_max=3.29e-11
Stage 7/7: T0.1  T=0.1  steps=200
🔁 Step 1650: cluster=[1370, 2152, 4099] ΔE=-2.208000 accept=True
    core_region=3 delta_region=56 | E_before=2.958001 E_after=0.750001
    Tile-level changes (top 6 by |ΔE|):
      id= 2151 THICK->THICK move= 0.0000 E:  1.0510-> 0.0250 ΔE= -1.0260 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1369 THIN->THIN move= 0.0000 E:  1.0510-> 0.0250 ΔE= -1.0260 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2152 THICK->THIN move= 0.3090 E:  0.0260-> 0.0000 ΔE= -0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1370 THIN->THIN move= 0.8090 E:  0.0260-> 0.0000 ΔE= -0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1371 THICK->THICK move= 0.0000 E:  0.0260-> 0.0000 ΔE= -0.0260 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4099 THIN->THICK move= 0.3090 E:  0.0250-> 0.0000 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1700: cluster=[1127, 1128, 2413] ΔE=+0.025000 accept=True
    core_region=3 delta_region=50 | E_before=6.741667 E_after=6.766667
    Tile-level changes (top 6 by |ΔE|):
      id= 4051 THICK->THICK move= 0.0000 E:  0.0000-> 0.0250 ΔE=+  0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1126 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1128 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1127 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3335 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2412 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1750: cluster=[956, 957, 2786] ΔE=+1.010333 accept=False
    core_region=3 delta_region=35 | E_before=9.927000 E_after=10.937333
    Tile-level changes (top 6 by |ΔE|):
      id= 2786 THICK->THICK move= 0.3090 E:  1.0333-> 3.0500 ΔE=+  2.0167 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  957 THIN->THICK move= 0.5878 E:  1.0333-> 0.0260 ΔE= -1.0073 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  956 THICK->THIN move= 0.5878 E:  0.0250-> 0.0260 ΔE=+  0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  955 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2785 THICK->THICK move= 0.0000 E:  1.0343-> 1.0343 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3576 THICK->THICK move= 0.0000 E:  0.0250-> 0.0250 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1800: cluster=[2572, 2573, 3478] ΔE=-0.025000 accept=True
    core_region=3 delta_region=52 | E_before=11.987334 E_after=11.962334
    Tile-level changes (top 6 by |ΔE|):
      id= 2571 THICK->THICK move= 0.0000 E:  0.0260-> 0.0010 ΔE= -0.0250 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1043 THIN->THIN move= 0.0000 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3477 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1041 THIN->THIN move= 0.0000 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2573 THICK->THICK move= 0.3090 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2572 THIN->THICK move= 0.5878 E:  0.0250-> 0.0250 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
  stage summary: defects 126→127 (Δ=+1)  E 795.232→785.344  drift_max=3.52e-11
-------------------------------------------------------------------------------
EXPERIMENT COMPLETE
Elapsed: 435.43 s   MC steps: 1300
Defects: 126 → 127  efficiency=-0.008
Energy:  816.668 → 785.344  ΔE=31.324
Energy drift max: 3.52e-11
===============================================================================
randa@Randa:quasi-phason$