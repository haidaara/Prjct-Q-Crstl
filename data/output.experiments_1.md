randa@Randa:quasi-phason$ python scripts/experiments/01_
01_generate_tiling.py           01_prepare_processed_tiling.py
randa@Randa:quasi-phason$ python scripts/experiments/01_generate_tiling.py
🚀 Starting Milestone 1: Penrose Tiling Generation
📁 Using config: configs/phase2_experiments.toml
🔷 Generating Penrose P3 tiling...
🔄 Synchronizing neighbor lists with adjacency graph...
✅ Synchronized 4406 tile neighbor lists
✅ Neighbor list synchronization validated
Tiling validation found 1 issues:
  - Found 12 tiles with only 1 neighbor
📊 Creating visualization...
💾 Data exported to: data/raw/penrose_tiling.json

✅ Milestone 1 Complete!
   • Generated 4406 tiles
   • Thick/Thin ratio: 2718/1688
   • Adjacency computed: True
   • Window: [0.0, 0.0] to [60.0, 60.0]
randa@Randa:quasi-phason$ python scripts/experiments/01_prepare_processed_tiling.py
🎯 ENERGY LANDSCAPE VALIDATION - FIXED VERSION
==================================================
🔬 Loading configuration...
✅ Loaded energy config from phase2_experiments.toml
[load] Loaded tiling data: 4406 tiles
✅ Energy computation completed: 1.00s
✅ Total configurational energy: 307.85
🔬 Validating Physics Fields...
✅ All physics fields present
🔬 Validating Coordination Distribution...
   Coordination distribution: {1: 12, 2: 103, 3: 108, 4: 4183}
   Tiles with 0 neighbors: False
   Tiles with 1 neighbor: 12 (0.3%)
   Typical coordination (3-4): 97.4%
🔬 Validating Vertex Classification...
✅ Classification distribution: 4313/4406 low, 70/4406 medium, 23/4406 high
🔬 Validating Energy Model...
  Tile 0: LOW_ENERGY = 0.00
  Tile 100: LOW_ENERGY = 0.05
  Tile 500: MEDIUM_ENERGY = 1.10
  Tile 1000: LOW_ENERGY = 0.05
✅ Total energy: 307.85
✅ Energy range reasonable (0-2.5): True

==================================================
📊 ENERGY LANDSCAPE VALIDATION RESULTS
==================================================
✅ ENERGY LANDSCAPE VALIDATION PASSED
📝 Energy model implementation complete and paper-ready!

📁 ENERGY LANDSCAPE LOGGED:
   - Energy parameters: data/energy/energy_model_parameters.json
   - Vertex statistics: data/energy/vertex_environment_statistics.json
   - Validation report: data/energy/energy_validation_report.json
   - Simulation-ready tiling: data/processed/penrose_tiling_energy_initialized.json

🚀 ENERGY LANDSCAPE READY FOR MONTE CARLO SIMULATIONS!
   Next: Implement phason flip mechanics and Monte Carlo relaxation
randa@Randa:quasi-phason$ python scripts/experiments/02_generate_obstacles.py
🚀 MILESTONE 2A: OBSTACLE CREATION PIPELINE
============================================================
📁 Using config: configs/phase2_experiments.toml

⚠️  WARNING: data/obstacles already contains 15 JSON files
   This will overwrite existing obstacle configurations
   Run: python src/utils/archive_obstacles.py to archive existing data

Continue anyway? (y/n): y
📐 Loaded base tiling: 4406 tiles
   Source: data/processed/penrose_tiling_energy_initialized.json

🔧 Generating obstacle specifications...
📊 Generated 12 obstacle configurations
✅ Generated 12 obstacle specs

🔧 Creating obstacles: pores_density_0.005
🚀 Creating pores obstacles (density: 0.005)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: pores_density_0.005.json

🔧 Creating obstacles: fixed_defects_density_0.005
🚀 Creating fixed_defects obstacles (density: 0.005)
📊 Built spatial index with KDTree
   → Created 22 fixed defects (target: 22)
💾 Saved: fixed_defects_density_0.005.json

🔧 Creating obstacles: pores_density_0.01
🚀 Creating pores obstacles (density: 0.01)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: pores_density_0.01.json

🔧 Creating obstacles: fixed_defects_density_0.01
🚀 Creating fixed_defects obstacles (density: 0.01)
📊 Built spatial index with KDTree
   → Created 44 fixed defects (target: 44)
💾 Saved: fixed_defects_density_0.01.json

🔧 Creating obstacles: pores_density_0.02
🚀 Creating pores obstacles (density: 0.02)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: pores_density_0.02.json

🔧 Creating obstacles: fixed_defects_density_0.02
🚀 Creating fixed_defects obstacles (density: 0.02)
📊 Built spatial index with KDTree
   → Created 88 fixed defects (target: 88)
💾 Saved: fixed_defects_density_0.02.json

🔧 Creating obstacles: pores_density_0.03
🚀 Creating pores obstacles (density: 0.03)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: pores_density_0.03.json

🔧 Creating obstacles: fixed_defects_density_0.03
🚀 Creating fixed_defects obstacles (density: 0.03)
📊 Built spatial index with KDTree
   → Created 132 fixed defects (target: 132)
💾 Saved: fixed_defects_density_0.03.json

🔧 Creating obstacles: pores_density_0.05
🚀 Creating pores obstacles (density: 0.05)
📊 Built spatial index with KDTree
   → Removed 193 tiles within 2 pore regions
💾 Saved: pores_density_0.05.json

🔧 Creating obstacles: fixed_defects_density_0.05
🚀 Creating fixed_defects obstacles (density: 0.05)
📊 Built spatial index with KDTree
   → Created 220 fixed defects (target: 220)
💾 Saved: fixed_defects_density_0.05.json

🔧 Creating obstacles: pores_density_0.1
🚀 Creating pores obstacles (density: 0.1)
📊 Built spatial index with KDTree
   → Removed 481 tiles within 5 pore regions
💾 Saved: pores_density_0.1.json

🔧 Creating obstacles: fixed_defects_density_0.1
🚀 Creating fixed_defects obstacles (density: 0.1)
📊 Built spatial index with KDTree
   → Created 441 fixed defects (target: 441)
💾 Saved: fixed_defects_density_0.1.json

📊 Summary saved: experiment_summary.json

✅ MILESTONE 2A COMPLETED IN 93.60s
   • Generated 12 obstacle configurations
   • Output: data/obstacles
   • Run verification: python validation/validate_obstacles.py
randa@Randa:quasi-phason$ python scripts/experiments/01_prepare_processed_tiling.py
🎯 ENERGY LANDSCAPE VALIDATION - FIXED VERSION
==================================================
🔬 Loading configuration...
✅ Loaded energy config from phase2_experiments.toml
[load] Loaded tiling data: 4406 tiles
✅ Energy computation completed: 1.21s
✅ Total configurational energy: 307.85
🔬 Validating Physics Fields...
✅ All physics fields present
🔬 Validating Coordination Distribution...
   Coordination distribution: {1: 12, 2: 103, 3: 108, 4: 4183}
   Tiles with 0 neighbors: False
   Tiles with 1 neighbor: 12 (0.3%)
   Typical coordination (3-4): 97.4%
🔬 Validating Vertex Classification...
✅ Classification distribution: 4313/4406 low, 70/4406 medium, 23/4406 high
🔬 Validating Energy Model...
  Tile 0: LOW_ENERGY = 0.00
  Tile 100: LOW_ENERGY = 0.05
  Tile 500: MEDIUM_ENERGY = 1.10
  Tile 1000: LOW_ENERGY = 0.05
✅ Total energy: 307.85
✅ Energy range reasonable (0-2.5): True

==================================================
📊 ENERGY LANDSCAPE VALIDATION RESULTS
==================================================
✅ ENERGY LANDSCAPE VALIDATION PASSED
📝 Energy model implementation complete and paper-ready!

📁 ENERGY LANDSCAPE LOGGED:
   - Energy parameters: data/energy/energy_model_parameters.json
   - Vertex statistics: data/energy/vertex_environment_statistics.json
   - Validation report: data/energy/energy_validation_report.json
   - Simulation-ready tiling: data/processed/penrose_tiling_energy_initialized.json

🚀 ENERGY LANDSCAPE READY FOR MONTE CARLO SIMULATIONS!
   Next: Implement phason flip mechanics and Monte Carlo relaxation
randa@Randa:quasi-phason$ python scripts/experiments/0
01_generate_tiling.py           03_run_healing_test.py          06_run_phase2_batch.py
01_prepare_processed_tiling.py  04_run_growth.py
02_generate_obstacles.py        05_temperature_sweep.py
randa@Randa:quasi-phason$ python scripts/experiments/03
python: can't open file '/mnt/c/Users/randa chames/Downloads/aberration-master/interns_&_project_&_conf/Prjct_Q-Crstl/quasi-phason/scripts/experiments/03': [Errno 2] No such file or directory
randa@Randa:quasi-phason$ python scripts/experiments/03_run_healing_test.py
🧪 EXPERIMENT 03: PHASON HEALING (Refactored)
============================================================
📥 Input tiling: data/processed/penrose_tiling_energy_initialized.json
📤 Output dir : data/experiments/healing
⚙️  scenario=base seed_radius=10.0 num_defects=15 defect_threshold=1.5
⚙️  MC: T=0.8 steps=200 R=4 verify_energy=True base_steps=100
------------------------------------------------------------
  🔨 Creating 15 defects (Strict Mode)...
  ✅ Created 15 defects.
  Initial Defects: 16
🎲 Starting Monte Carlo...
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 1/200 (0.5%) | accepted=0 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 2/200 (1.0%) | accepted=0 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 3/200 (1.5%) | accepted=0 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 4/200 (2.0%) | accepted=0 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 5/200 (2.5%) | accepted=0 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 6/200 (3.0%) | accepted=0 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 7/200 (3.5%) | accepted=1 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 8/200 (4.0%) | accepted=1 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 9/200 (4.5%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 10/200 (5.0%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 11/200 (5.5%) | accepted=3 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 12/200 (6.0%) | accepted=3 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 13/200 (6.5%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 14/200 (7.0%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 15/200 (7.5%) | accepted=5 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 16/200 (8.0%) | accepted=5 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 17/200 (8.5%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 18/200 (9.0%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 19/200 (9.5%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 20/200 (10.0%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 21/200 (10.5%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 22/200 (11.0%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 23/200 (11.5%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 24/200 (12.0%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 25/200 (12.5%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 26/200 (13.0%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 27/200 (13.5%) | accepted=7 | max_drift=0.000000
⚠️  ENERGY DRIFT : 0.033816 (MC=370.874152, actual=370.907968)
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 28/200 (14.0%) | accepted=8 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 29/200 (14.5%) | accepted=9 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 30/200 (15.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 31/200 (15.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 32/200 (16.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 33/200 (16.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 34/200 (17.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 35/200 (17.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 36/200 (18.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 37/200 (18.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 38/200 (19.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 39/200 (19.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 40/200 (20.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 41/200 (20.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 42/200 (21.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 43/200 (21.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 44/200 (22.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 45/200 (22.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 46/200 (23.0%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 47/200 (23.5%) | accepted=10 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 48/200 (24.0%) | accepted=11 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 49/200 (24.5%) | accepted=11 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 50/200 (25.0%) | accepted=11 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 51/200 (25.5%) | accepted=11 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 52/200 (26.0%) | accepted=12 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 53/200 (26.5%) | accepted=12 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 54/200 (27.0%) | accepted=12 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 55/200 (27.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 56/200 (28.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 57/200 (28.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 58/200 (29.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 59/200 (29.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 60/200 (30.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 61/200 (30.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 62/200 (31.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 63/200 (31.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 64/200 (32.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 65/200 (32.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 66/200 (33.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 67/200 (33.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 68/200 (34.0%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 69/200 (34.5%) | accepted=13 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 70/200 (35.0%) | accepted=14 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 71/200 (35.5%) | accepted=14 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 72/200 (36.0%) | accepted=14 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 73/200 (36.5%) | accepted=14 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 74/200 (37.0%) | accepted=14 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 75/200 (37.5%) | accepted=15 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 76/200 (38.0%) | accepted=15 | max_drift=0.033816
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.033816
  ⏳ MC progress: 77/200 (38.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 78/200 (39.0%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 79/200 (39.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 80/200 (40.0%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 81/200 (40.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 82/200 (41.0%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 83/200 (41.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 84/200 (42.0%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 85/200 (42.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 86/200 (43.0%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 87/200 (43.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 88/200 (44.0%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 89/200 (44.5%) | accepted=16 | max_drift=0.033816
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.033816
  ⏳ MC progress: 90/200 (45.0%) | accepted=16 | max_drift=0.033816
⚠️  ENERGY DRIFT : 1.026368 (MC=369.574152, actual=368.547785)
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 91/200 (45.5%) | accepted=17 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 92/200 (46.0%) | accepted=17 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 93/200 (46.5%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 94/200 (47.0%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 95/200 (47.5%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 96/200 (48.0%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 97/200 (48.5%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 98/200 (49.0%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 99/200 (49.5%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 100/200 (50.0%) | accepted=18 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 101/200 (50.5%) | accepted=19 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 102/200 (51.0%) | accepted=19 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 103/200 (51.5%) | accepted=20 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 104/200 (52.0%) | accepted=20 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 105/200 (52.5%) | accepted=20 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 106/200 (53.0%) | accepted=20 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 107/200 (53.5%) | accepted=20 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 108/200 (54.0%) | accepted=20 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 109/200 (54.5%) | accepted=21 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 110/200 (55.0%) | accepted=22 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 111/200 (55.5%) | accepted=22 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 112/200 (56.0%) | accepted=22 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 113/200 (56.5%) | accepted=23 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 114/200 (57.0%) | accepted=23 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 115/200 (57.5%) | accepted=23 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 116/200 (58.0%) | accepted=23 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 117/200 (58.5%) | accepted=24 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 118/200 (59.0%) | accepted=24 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 119/200 (59.5%) | accepted=25 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 120/200 (60.0%) | accepted=26 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 121/200 (60.5%) | accepted=26 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 122/200 (61.0%) | accepted=26 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 123/200 (61.5%) | accepted=27 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 124/200 (62.0%) | accepted=28 | max_drift=1.026368
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.026368
  ⏳ MC progress: 125/200 (62.5%) | accepted=29 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 126/200 (63.0%) | accepted=29 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 127/200 (63.5%) | accepted=29 | max_drift=1.026368
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.026368
  ⏳ MC progress: 128/200 (64.0%) | accepted=29 | max_drift=1.026368
⚠️  ENERGY DRIFT : 2.079000 (MC=364.562118, actual=362.483118)
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 129/200 (64.5%) | accepted=30 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 130/200 (65.0%) | accepted=30 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 131/200 (65.5%) | accepted=30 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 132/200 (66.0%) | accepted=30 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 133/200 (66.5%) | accepted=30 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 134/200 (67.0%) | accepted=30 | max_drift=2.079000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 135/200 (67.5%) | accepted=31 | max_drift=2.079000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 136/200 (68.0%) | accepted=32 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 137/200 (68.5%) | accepted=32 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 138/200 (69.0%) | accepted=32 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 139/200 (69.5%) | accepted=32 | max_drift=2.079000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 140/200 (70.0%) | accepted=33 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 141/200 (70.5%) | accepted=33 | max_drift=2.079000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 142/200 (71.0%) | accepted=34 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 143/200 (71.5%) | accepted=34 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 144/200 (72.0%) | accepted=34 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 145/200 (72.5%) | accepted=34 | max_drift=2.079000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 146/200 (73.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 147/200 (73.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 148/200 (74.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 149/200 (74.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 150/200 (75.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 151/200 (75.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 152/200 (76.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 153/200 (76.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 154/200 (77.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 155/200 (77.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 156/200 (78.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 157/200 (78.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 158/200 (79.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 159/200 (79.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 160/200 (80.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 161/200 (80.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 162/200 (81.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 163/200 (81.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 164/200 (82.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 165/200 (82.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 166/200 (83.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 167/200 (83.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 168/200 (84.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 169/200 (84.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 170/200 (85.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 171/200 (85.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 172/200 (86.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 173/200 (86.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 174/200 (87.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 175/200 (87.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 176/200 (88.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 177/200 (88.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 178/200 (89.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 179/200 (89.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 180/200 (90.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 181/200 (90.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 182/200 (91.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 183/200 (91.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 184/200 (92.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 185/200 (92.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 186/200 (93.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 187/200 (93.5%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 188/200 (94.0%) | accepted=35 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 189/200 (94.5%) | accepted=35 | max_drift=2.079000
⚠️  ENERGY DRIFT : 2.077816 (MC=361.019785, actual=358.941969)
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 190/200 (95.0%) | accepted=36 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 191/200 (95.5%) | accepted=36 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 192/200 (96.0%) | accepted=36 | max_drift=2.079000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 2.079000
  ⏳ MC progress: 193/200 (96.5%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 194/200 (97.0%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 195/200 (97.5%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 196/200 (98.0%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 197/200 (98.5%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 198/200 (99.0%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 199/200 (99.5%) | accepted=37 | max_drift=2.079000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 2.079000
  ⏳ MC progress: 200/200 (100.0%) | accepted=37 | max_drift=2.079000
✅ MC finished in 23.73s | acceptance=18.5% | max_drift=2.079000
------------------------------------------------------------
RESULTS: 16 -> 8 (Efficiency: 50.0%)
Drift: 2.079000

💾 Saved: data/experiments/healing/healing_base_run_028.json
📌 Latest: data/experiments/healing/latest.json
randa@Randa:quasi-phason$ python scripts/experiments/03_run_healing_test.py
🧪 EXPERIMENT 03: PHASON HEALING (Refactored)
============================================================
📥 Input tiling: data/processed/penrose_tiling_energy_initialized.json
📤 Output dir : data/experiments/healing
⚙️  scenario=base seed_radius=10.0 num_defects=15 defect_threshold=1.5
⚙️  MC: T=0.8 steps=200 R=4 verify_energy=True base_steps=100
------------------------------------------------------------
  🔨 Creating 15 defects (Strict Mode)...
  ✅ Created 15 defects.
  Initial Defects: 21
🎲 Starting Monte Carlo...
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 1/200 (0.5%) | accepted=1 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 2/200 (1.0%) | accepted=1 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 3/200 (1.5%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 4/200 (2.0%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 5/200 (2.5%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 6/200 (3.0%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 7/200 (3.5%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 8/200 (4.0%) | accepted=2 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 9/200 (4.5%) | accepted=3 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 10/200 (5.0%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 11/200 (5.5%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 12/200 (6.0%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 13/200 (6.5%) | accepted=4 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 14/200 (7.0%) | accepted=5 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 15/200 (7.5%) | accepted=5 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 16/200 (8.0%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 17/200 (8.5%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 18/200 (9.0%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 19/200 (9.5%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 20/200 (10.0%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 21/200 (10.5%) | accepted=6 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 22/200 (11.0%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 23/200 (11.5%) | accepted=7 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 24/200 (12.0%) | accepted=8 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 25/200 (12.5%) | accepted=9 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 26/200 (13.0%) | accepted=9 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 27/200 (13.5%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 28/200 (14.0%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 29/200 (14.5%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 30/200 (15.0%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 31/200 (15.5%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 32/200 (16.0%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 33/200 (16.5%) | accepted=10 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 34/200 (17.0%) | accepted=11 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 35/200 (17.5%) | accepted=12 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 36/200 (18.0%) | accepted=12 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 37/200 (18.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 38/200 (19.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 39/200 (19.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 40/200 (20.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 41/200 (20.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 42/200 (21.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 43/200 (21.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 44/200 (22.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 45/200 (22.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 46/200 (23.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 47/200 (23.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 48/200 (24.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 49/200 (24.5%) | accepted=13 | max_drift=0.000000
🔁 Step 50: cluster=[903, 904, 2407] ΔE=+3.310333 accept=False
    core_region=4 delta_region=76 | E_before=10.277668 E_after=13.588001
    Tile-level changes (top 6 by |ΔE|):
      id= 4109 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2351 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  978 THICK->THICK move= 0.0000 E:  2.0000-> 0.0667 ΔE= -1.9333 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4134 THICK->THICK move= 0.0000 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3472 THICK->THICK move= 0.0000 E:  1.1020-> 0.0500 ΔE= -1.0520 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 50/200 (25.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 51/200 (25.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 52/200 (26.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 53/200 (26.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 54/200 (27.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 55/200 (27.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 56/200 (28.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 57/200 (28.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 58/200 (29.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 59/200 (29.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 60/200 (30.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 61/200 (30.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 62/200 (31.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 63/200 (31.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 64/200 (32.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 65/200 (32.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 66/200 (33.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 67/200 (33.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 68/200 (34.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 69/200 (34.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 70/200 (35.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 71/200 (35.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 72/200 (36.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 73/200 (36.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 74/200 (37.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 75/200 (37.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 76/200 (38.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 77/200 (38.5%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 78/200 (39.0%) | accepted=13 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 79/200 (39.5%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 80/200 (40.0%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 81/200 (40.5%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 82/200 (41.0%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 83/200 (41.5%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 84/200 (42.0%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 85/200 (42.5%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 86/200 (43.0%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 87/200 (43.5%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 88/200 (44.0%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 89/200 (44.5%) | accepted=14 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 90/200 (45.0%) | accepted=15 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 91/200 (45.5%) | accepted=15 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 92/200 (46.0%) | accepted=15 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 93/200 (46.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 94/200 (47.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 95/200 (47.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 96/200 (48.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 97/200 (48.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 98/200 (49.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 99/200 (49.5%) | accepted=16 | max_drift=0.000000
🔁 Step 100: cluster=[758, 759, 4190] ΔE=+5.131333 accept=False
    core_region=4 delta_region=79 | E_before=4.936667 E_after=10.068000
    Tile-level changes (top 6 by |ΔE|):
      id= 3470 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  830 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4216 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  684 THICK->THICK move= 0.0000 E:  2.0000-> 0.0667 ΔE= -1.9333 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  756 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 100/200 (50.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 101/200 (50.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 102/200 (51.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 103/200 (51.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 104/200 (52.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 105/200 (52.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 106/200 (53.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 107/200 (53.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 108/200 (54.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 109/200 (54.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 110/200 (55.0%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 111/200 (55.5%) | accepted=16 | max_drift=0.000000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.000000
  ⏳ MC progress: 112/200 (56.0%) | accepted=17 | max_drift=0.000000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.000000
  ⏳ MC progress: 113/200 (56.5%) | accepted=17 | max_drift=0.000000
⚠️  ENERGY DRIFT : 0.029000 (MC=355.785003, actual=355.756003)
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 114/200 (57.0%) | accepted=18 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 115/200 (57.5%) | accepted=18 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 116/200 (58.0%) | accepted=19 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 117/200 (58.5%) | accepted=19 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 118/200 (59.0%) | accepted=20 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 119/200 (59.5%) | accepted=20 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 120/200 (60.0%) | accepted=20 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 121/200 (60.5%) | accepted=21 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 122/200 (61.0%) | accepted=22 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 123/200 (61.5%) | accepted=23 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 124/200 (62.0%) | accepted=23 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 125/200 (62.5%) | accepted=23 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 126/200 (63.0%) | accepted=23 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 127/200 (63.5%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 128/200 (64.0%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 129/200 (64.5%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 130/200 (65.0%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 131/200 (65.5%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 132/200 (66.0%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 133/200 (66.5%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 134/200 (67.0%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 135/200 (67.5%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 0/1 accepted (0.0%), max drift: 0.029000
  ⏳ MC progress: 136/200 (68.0%) | accepted=24 | max_drift=0.029000
✅ MC sweep: 1/1 accepted (100.0%), max drift: 0.029000
  ⏳ MC progress: 137/200 (68.5%) | accepted=25 | max_drift=0.029000
⚠️  ENERGY DRIFT : 1.134299 (MC=354.384670, actual=353.250371)
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 138/200 (69.0%) | accepted=26 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 139/200 (69.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 140/200 (70.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 141/200 (70.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 142/200 (71.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 143/200 (71.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 144/200 (72.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 145/200 (72.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 146/200 (73.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 147/200 (73.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 148/200 (74.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 149/200 (74.5%) | accepted=27 | max_drift=1.134299
🔁 Step 150: cluster=[2412, 2413, 3334] ΔE=+1.170667 accept=False
    core_region=4 delta_region=15 | E_before=2.238334 E_after=3.409001
    Tile-level changes (top 6 by |ΔE|):
      id= 1055 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1127 THIN->THIN move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3334 THICK->THICK move= 0.3090 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2413 THIN->THICK move= 0.5878 E:  0.0717-> 0.0570 ΔE= -0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1054 THICK->THICK move= 0.0000 E:  0.0667-> 0.0687 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2412 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 150/200 (75.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 151/200 (75.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 152/200 (76.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 153/200 (76.5%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 154/200 (77.0%) | accepted=27 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 155/200 (77.5%) | accepted=28 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 156/200 (78.0%) | accepted=28 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 157/200 (78.5%) | accepted=28 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 158/200 (79.0%) | accepted=28 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 159/200 (79.5%) | accepted=29 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 160/200 (80.0%) | accepted=29 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 161/200 (80.5%) | accepted=29 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 162/200 (81.0%) | accepted=29 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 163/200 (81.5%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 164/200 (82.0%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 165/200 (82.5%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 166/200 (83.0%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 167/200 (83.5%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 168/200 (84.0%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 169/200 (84.5%) | accepted=30 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 170/200 (85.0%) | accepted=31 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 171/200 (85.5%) | accepted=32 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 172/200 (86.0%) | accepted=32 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 173/200 (86.5%) | accepted=32 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 174/200 (87.0%) | accepted=32 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 175/200 (87.5%) | accepted=32 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 176/200 (88.0%) | accepted=32 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 177/200 (88.5%) | accepted=33 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 178/200 (89.0%) | accepted=33 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 179/200 (89.5%) | accepted=34 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 180/200 (90.0%) | accepted=34 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 181/200 (90.5%) | accepted=34 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 182/200 (91.0%) | accepted=34 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 183/200 (91.5%) | accepted=35 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 184/200 (92.0%) | accepted=35 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 185/200 (92.5%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 186/200 (93.0%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 187/200 (93.5%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 188/200 (94.0%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 189/200 (94.5%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 190/200 (95.0%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 191/200 (95.5%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 192/200 (96.0%) | accepted=36 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 193/200 (96.5%) | accepted=37 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 194/200 (97.0%) | accepted=38 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 195/200 (97.5%) | accepted=38 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 196/200 (98.0%) | accepted=38 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 197/200 (98.5%) | accepted=38 | max_drift=1.134299
✅ MC sweep: 1/1 accepted (100.0%), max drift: 1.134299
  ⏳ MC progress: 198/200 (99.0%) | accepted=39 | max_drift=1.134299
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 199/200 (99.5%) | accepted=39 | max_drift=1.134299
🔁 Step 200: cluster=[3282, 3283, 4159] ΔE=+4.152667 accept=False
    core_region=4 delta_region=44 | E_before=7.658334 E_after=11.811000
    Tile-level changes (top 6 by |ΔE|):
      id= 3329 THICK->THICK move= 0.0000 E:  0.0520-> 2.0000 ΔE=+  1.9480 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  917 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3281 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  993 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2247 THIN->THIN move= 0.0000 E:  1.1000-> 0.0550 ΔE= -1.0450 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  914 THICK->THICK move= 0.0000 E:  0.0687-> 0.0000 ΔE= -0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 0/1 accepted (0.0%), max drift: 1.134299
  ⏳ MC progress: 200/200 (100.0%) | accepted=39 | max_drift=1.134299
✅ MC finished in 21.01s | acceptance=19.5% | max_drift=1.134299
------------------------------------------------------------
RESULTS: 21 -> 9 (Efficiency: 57.1%)
Drift: 1.134299

💾 Saved: data/experiments/healing/healing_base_run_029.json
📌 Latest: data/experiments/healing/latest.json
randa@Randa:quasi-phason$ python scripts/experiments/04_run_growth.py
🧪 Running growth experiment...
==================================================
🔧 debug: verbosity=2, progress_every=1, trace_every=50
Experiment: growth_pores_d0p000_run_007
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 5 growth steps...

  Step 1/5
🌿 Growth step 0...
   Running 200 MC steps for healing...
🔁 Step 50: cluster=[830, 831, 3471] ΔE=+8.155333 accept=False
    core_region=4 delta_region=85 | E_before=3.500000 E_after=11.655333
    Tile-level changes (top 6 by |ΔE|):
      id= 3473 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2295 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  903 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  758 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  827 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 100: cluster=[3468, 3469, 4189] ΔE=+1.224667 accept=False
    core_region=4 delta_region=30 | E_before=0.868667 E_after=2.093333
    Tile-level changes (top 6 by |ΔE|):
      id= 2298 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2295 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4189 THICK->THICK move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2297 THIN->THIN move= 0.0000 E:  0.0500-> 0.0687 ΔE=+  0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  837 THICK->THICK move= 0.0000 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  833 THIN->THIN move= 0.0000 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 150: cluster=[2405, 2406, 3472] ΔE=+6.328333 accept=False
    core_region=4 delta_region=86 | E_before=4.391333 E_after=10.719667
    Tile-level changes (top 6 by |ΔE|):
      id=  832 THICK->THICK move= 0.0000 E:  0.0000-> 2.1353 ΔE=+  2.1353 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2408 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2462 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4108 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  831 THIN->THIN move= 0.0000 E:  0.0000-> 0.0570 ΔE=+  0.0570 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.003000 (MC=315.967334, actual=315.970334)
⚠️  ENERGY DRIFT : 0.007000 (MC=316.654668, actual=316.661668)
🔁 Step 200: cluster=[2356, 2357, 3332] ΔE=+2.462000 accept=False
    core_region=4 delta_region=23 | E_before=1.673667 E_after=4.135667
    Tile-level changes (top 6 by |ΔE|):
      id= 3333 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2357 THIN->THICK move= 0.5878 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3331 THICK->THICK move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.3090 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4106 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 23/200 accepted (11.5%), max drift: 0.007000
✅ Growth step 1: added 29 tiles
    New tiles: 29, Defects: 0
    Acceptance rate: 11.5%

  Step 2/5
🌿 Growth step 1...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 0.012000 (MC=316.794667, actual=316.806667)
🔁 Step 250: cluster=[2403, 2404, 3519] ΔE=+8.251333 accept=False
    core_region=4 delta_region=85 | E_before=4.309000 E_after=12.560334
    Tile-level changes (top 6 by |ΔE|):
      id= 4109 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2401 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2406 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2347 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2459 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 300: cluster=[761, 2294, 4189] ΔE=+2.934667 accept=False
    core_region=4 delta_region=30 | E_before=0.987334 E_after=3.922000
    Tile-level changes (top 6 by |ΔE|):
      id= 3470 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4188 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  836 THIN->THIN move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3469 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3422 THIN->THIN move= 0.0000 E:  0.0500-> 0.0020 ΔE= -0.0480 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 350: cluster=[2408, 2409, 3427] ΔE=+4.162333 accept=False
    core_region=4 delta_region=23 | E_before=3.880667 E_after=8.043000
    Tile-level changes (top 6 by |ΔE|):
      id= 2351 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4134 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2409 THIN->THICK move= 0.5878 E:  0.0020-> 0.0687 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4135 THICK->THICK move= 0.0000 E:  0.0520-> 0.0000 ΔE= -0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2408 THICK->THIN move= 0.5878 E:  0.0520-> 0.0687 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 400: cluster=[2348, 2349, 4163] ΔE=+6.996334 accept=False
    core_region=4 delta_region=83 | E_before=5.114000 E_after=12.110334
    Tile-level changes (top 6 by |ΔE|):
      id= 2351 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4162 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3468 THIN->THIN move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4164 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4135 THICK->THICK move= 0.0000 E:  0.0520-> 1.1000 ΔE=+  1.0480 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3472 THICK->THICK move= 0.0000 E:  1.1000-> 0.0687 ΔE= -1.0313 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 14/200 accepted (7.0%), max drift: 0.012000
✅ Growth step 2: added 27 tiles
    New tiles: 27, Defects: 0
    Acceptance rate: 7.0%

  Step 3/5
🌿 Growth step 2...
   Running 200 MC steps for healing...
🔁 Step 450: cluster=[1054, 1055, 2412] ΔE=+7.156000 accept=False
    core_region=4 delta_region=81 | E_before=3.556000 E_after=10.712000
    Tile-level changes (top 6 by |ΔE|):
      id= 3379 THICK->THICK move= 0.0000 E:  0.0000-> 2.1353 ΔE=+  2.1353 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  978 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2358 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4107 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4106 THICK->THICK move= 0.0000 E:  0.0000-> 0.0550 ΔE=+  0.0550 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 500: cluster=[975, 976, 2463] ΔE=+5.355666 accept=False
    core_region=4 delta_region=27 | E_before=1.408001 E_after=6.763667
    Tile-level changes (top 6 by |ΔE|):
      id=  976 THIN->THICK move= 0.5878 E:  0.0020-> 2.1333 ΔE=+  2.1313 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2515 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2464 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2461 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  975 THICK->THIN move= 0.5878 E:  1.1000-> 0.0550 ΔE= -1.0450 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.016368 (MC=318.404003, actual=318.420370)
🔁 Step 550: cluster=[2346, 2347, 3517] ΔE=+5.777667 accept=False
    core_region=4 delta_region=80 | E_before=5.139334 E_after=10.917001
    Tile-level changes (top 6 by |ΔE|):
      id= 3561 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2404 THIN->THIN move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2295 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4164 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  758 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  755 THIN->THIN move= 0.0000 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 600: cluster=[2297, 3424, 3425] ΔE=+8.293333 accept=False
    core_region=4 delta_region=39 | E_before=6.507334 E_after=14.800667
    Tile-level changes (top 6 by |ΔE|):
      id=  984 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.0000 E:  0.0520-> 2.0000 ΔE=+  1.9480 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2350 THIN->THIN move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  911 THIN->THIN move= 0.0000 E:  0.0520-> 1.1020 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2297 THIN->THIN move= 0.8090 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 27/200 accepted (13.5%), max drift: 0.016368
✅ Growth step 3: added 30 tiles
    New tiles: 30, Defects: 0
    Acceptance rate: 13.5%

  Step 4/5
🌿 Growth step 3...
   Running 200 MC steps for healing...
🔁 Step 650: cluster=[2463, 2464, 3429] ΔE=+5.345666 accept=False
    core_region=4 delta_region=30 | E_before=1.408001 E_after=6.753667
    Tile-level changes (top 6 by |ΔE|):
      id= 2518 THICK->THICK move= 0.0000 E:  0.0000-> 2.0667 ΔE=+  2.0667 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  902 THIN->THIN move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  976 THIN->THIN move= 0.0000 E:  0.0020-> 1.1000 ΔE=+  1.0980 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  901 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  975 THICK->THICK move= 0.0000 E:  1.1000-> 0.0520 ΔE= -1.0480 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.3090 E:  0.0000-> 0.0717 ΔE=+  0.0717 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.094000 (MC=315.242704, actual=315.336704)
🔁 Step 700: cluster=[897, 898, 2514] ΔE=+5.492666 accept=False
    core_region=4 delta_region=23 | E_before=0.500000 E_after=5.992667
    Tile-level changes (top 6 by |ΔE|):
      id= 2462 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  896 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  899 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  974 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2514 THIN->THICK move= 0.5878 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  898 THICK->THICK move= 0.3090 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.096000 (MC=318.779370, actual=318.875370)
⚠️  ENERGY DRIFT : 0.117368 (MC=318.902704, actual=319.020071)
⚠️  ENERGY DRIFT : 0.145735 (MC=317.520037, actual=317.665772)
🔁 Step 750: cluster=[906, 907, 2352] ΔE=+3.436666 accept=False
    core_region=4 delta_region=31 | E_before=4.066001 E_after=7.502667
    Tile-level changes (top 6 by |ΔE|):
      id=  905 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  908 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  910 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2353 THICK->THICK move= 0.0000 E:  0.0520-> 1.1020 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3378 THIN->THIN move= 0.0000 E:  1.1000-> 0.0520 ΔE= -1.0480 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2299 THIN->THIN move= 0.0000 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 800: cluster=[972, 973, 2517] ΔE=+1.958000 accept=False
    core_region=4 delta_region=31 | E_before=2.024667 E_after=3.982667
    Tile-level changes (top 6 by |ΔE|):
      id= 3428 THICK->THICK move= 0.0000 E:  0.0020-> 2.0000 ΔE=+  1.9980 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2463 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3429 THICK->THICK move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  971 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  975 THICK->THICK move= 0.0000 E:  0.0000-> 0.0050 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  976 THIN->THIN move= 0.0000 E:  0.0520-> 0.0570 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 28/200 accepted (14.0%), max drift: 0.145735
✅ Growth step 4: added 33 tiles
    New tiles: 33, Defects: 2
    Acceptance rate: 14.0%

  Step 5/5
🌿 Growth step 4...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 1.240414 (MC=325.297370, actual=326.537784)
⚠️  ENERGY DRIFT : 1.190414 (MC=325.030703, actual=326.221118)
⚠️  ENERGY DRIFT : 1.194414 (MC=325.076703, actual=326.271118)
🔁 Step 850: cluster=[2243, 2244, 3375] ΔE=+1.032333 accept=False
    core_region=4 delta_region=15 | E_before=3.559000 E_after=4.591334
    Tile-level changes (top 6 by |ΔE|):
      id= 3375 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  836 THIN->THIN move= 0.0000 E:  0.0717-> 0.0000 ΔE= -0.0717 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  840 THIN->THIN move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  839 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2243 THICK->THICK move= 0.3090 E:  0.0500-> 0.0687 ΔE=+  0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2244 THICK->THIN move= 0.5878 E:  0.0687-> 0.0540 ΔE= -0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 900: cluster=[970, 971, 3476] ΔE=+4.122000 accept=False
    core_region=4 delta_region=22 | E_before=0.566667 E_after=4.688667
    Tile-level changes (top 6 by |ΔE|):
      id=  898 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4082 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3474 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  970 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  971 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 2.212748 (MC=328.678324, actual=330.891072)
🔁 Step 950: cluster=[3476, 3477, 4055] ΔE=+9.426000 accept=False
    core_region=4 delta_region=76 | E_before=3.000000 E_after=12.426000
    Tile-level changes (top 6 by |ΔE|):
      id= 2570 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4056 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  967 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4028 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2574 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2627 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 2.212748 (MC=326.393991, actual=328.606739)
🔁 Step 1000: cluster=[833, 2296, 4162] ΔE=+2.350333 accept=False
    core_region=4 delta_region=50 | E_before=4.522001 E_after=6.872334
    Tile-level changes (top 6 by |ΔE|):
      id= 3423 THIN->THIN move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4189 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4163 THIN->THIN move= 0.0000 E:  1.1000-> 0.0667 ΔE= -1.0333 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2295 THICK->THICK move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  833 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 31/200 accepted (15.5%), max drift: 2.212748
✅ Growth step 5: added 31 tiles
    New tiles: 31, Defects: 3
    Acceptance rate: 15.5%

✅ Experiment complete!
📊 Results saved to: data/experiments/growth/growth_pores_d0p000_run_007.json

==================================================
📈 EXPERIMENT SUMMARY:
  Total steps: 5
  Final energy: 324.11
  Final defect density: 0.012
randa@Randa:quasi-phason$ python scripts/experiments/05_temperature_sweep.py
🌡️ TEMPERATURE SWEEP
============================================================
📥 Base config: configs/phase2_experiments.toml
📤 Output dir : data/experiments/temp_sweep
⚙️  scenario=base temps=[0.8, 1.0, 1.2, 1.5]
🔧 debug: verbosity=2, progress_every=1, trace_every=50

🌡️  [1/4] Running T=0.8
🧪 Running growth experiment...
==================================================
🔧 debug: verbosity=2, progress_every=1, trace_every=50
Experiment: tempsweep_base_T0p800_run_018
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 5 growth steps...

  Step 1/5
🌿 Growth step 0...
   Running 200 MC steps for healing...
🔁 Step 50: cluster=[983, 3377, 3378] ΔE=-0.200000 accept=True
    core_region=4 delta_region=33 | E_before=1.050000 E_after=0.850000
    Tile-level changes (top 6 by |ΔE|):
      id= 2302 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  986 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4106 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2356 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  983 THICK->THICK move= 0.3090 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 100: cluster=[3471, 3472, 4135] ΔE=+6.435333 accept=False
    core_region=4 delta_region=85 | E_before=3.200000 E_after=9.635334
    Tile-level changes (top 6 by |ΔE|):
      id=  827 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4134 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4136 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2408 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4108 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2352 THIN->THIN move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 150: cluster=[830, 831, 3471] ΔE=+2.828000 accept=False
    core_region=4 delta_region=32 | E_before=1.188333 E_after=4.016334
    Tile-level changes (top 6 by |ΔE|):
      id= 2352 THIN->THIN move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  903 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  831 THIN->THIN move= 0.8090 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3471 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 200: cluster=[756, 757, 2347] ΔE=+7.208000 accept=False
    core_region=4 delta_region=81 | E_before=4.206000 E_after=11.414000
    Tile-level changes (top 6 by |ΔE|):
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2345 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3470 THICK->THICK move= 0.0000 E:  0.0020-> 1.1020 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4191 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2349 THIN->THIN move= 0.0000 E:  0.0000-> 0.0540 ΔE=+  0.0540 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 14/200 accepted (7.0%), max drift: 0.000000
✅ Growth step 1: added 26 tiles
    New tiles: 26, Defects: 1
    Acceptance rate: 7.0%

  Step 2/5
🌿 Growth step 1...
   Running 200 MC steps for healing...
🔁 Step 250: cluster=[837, 838, 4188] ΔE=+4.427000 accept=False
    core_region=4 delta_region=25 | E_before=0.266668 E_after=4.693668
    Tile-level changes (top 6 by |ΔE|):
      id= 4161 THICK->THICK move= 0.0000 E:  0.0000-> 2.0667 ΔE=+  2.0667 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3422 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3469 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  837 THICK->THICK move= 0.3090 E:  0.0000-> 0.0717 ΔE=+  0.0717 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  838 THIN->THICK move= 0.5878 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3423 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 300: cluster=[910, 911, 2300] ΔE=+7.315666 accept=False
    core_region=4 delta_region=40 | E_before=0.366669 E_after=7.682335
    Tile-level changes (top 6 by |ΔE|):
      id= 3331 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3425 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  985 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.3090 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  911 THIN->THICK move= 0.5878 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 350: cluster=[833, 3424, 4162] ΔE=+2.491332 accept=False
    core_region=4 delta_region=22 | E_before=0.216668 E_after=2.708000
    Tile-level changes (top 6 by |ΔE|):
      id= 2351 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3470 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4162 THICK->THIN move= 0.3090 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3425 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2296 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.021184 (MC=314.064002, actual=314.085186)
🔁 Step 400: cluster=[753, 754, 2403] ΔE=+6.312667 accept=False
    core_region=4 delta_region=85 | E_before=4.524667 E_after=10.837333
    Tile-level changes (top 6 by |ΔE|):
      id=  757 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2347 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4165 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4191 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  750 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  679 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
✅ MC sweep: 17/200 accepted (8.5%), max drift: 0.021184
✅ Growth step 2: added 29 tiles
    New tiles: 29, Defects: 0
    Acceptance rate: 8.5%

  Step 3/5
🌿 Growth step 2...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 1.127184 (MC=311.406669, actual=312.533853)
🔁 Step 450: cluster=[835, 836, 2296] ΔE=+5.517333 accept=False
    core_region=4 delta_region=33 | E_before=3.938667 E_after=9.456000
    Tile-level changes (top 6 by |ΔE|):
      id= 3470 THICK->THICK move= 0.0000 E:  0.0000-> 2.0667 ΔE=+  2.0667 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  758 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  835 THIN->THICK move= 0.3090 E:  2.0000-> 0.0500 ΔE= -1.9500 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  834 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3423 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  760 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 1.121184 (MC=308.721336, actual=309.842520)
🔁 Step 500: cluster=[2294, 2295, 3469] ΔE=+1.102000 accept=False
    core_region=4 delta_region=33 | E_before=3.890667 E_after=4.992667
    Tile-level changes (top 6 by |ΔE|):
      id= 2295 THICK->THIN move= 0.5878 E:  2.0000-> 0.0500 ΔE= -1.9500 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2348 THIN->THIN move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  761 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  760 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3424 THIN->THIN move= 0.0000 E:  0.0520-> 0.0000 ΔE= -0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  757 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 1.116184 (MC=306.362336, actual=307.478520)
🔁 Step 550: cluster=[824, 825, 2458] ΔE=+7.018000 accept=False
    core_region=4 delta_region=83 | E_before=2.916667 E_after=9.934667
    Tile-level changes (top 6 by |ΔE|):
      id= 2511 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  821 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  753 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3567 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  828 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2460 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 600: cluster=[912, 913, 4160] ΔE=+4.985816 accept=False
    core_region=4 delta_region=69 | E_before=2.278851 E_after=7.264667
    Tile-level changes (top 6 by |ΔE|):
      id=  837 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  983 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2353 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  988 THICK->THICK move= 0.0000 E:  0.0122-> 0.0667 ΔE=+  0.0545 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2243 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3374 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 31/200 accepted (15.5%), max drift: 1.127184
✅ Growth step 3: added 32 tiles
    New tiles: 32, Defects: 1
    Acceptance rate: 15.5%

  Step 4/5
🌿 Growth step 3...
   Running 200 MC steps for healing...
🔁 Step 650: cluster=[903, 904, 2407] ΔE=+12.461333 accept=False
    core_region=4 delta_region=63 | E_before=3.371247 E_after=15.832580
    Tile-level changes (top 6 by |ΔE|):
      id= 4109 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  830 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  908 THIN->THIN move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  978 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.0000 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2462 THICK->THICK move= 0.0000 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 2.336103 (MC=305.158664, actual=307.494767)
🔁 Step 700: cluster=[825, 826, 2459] ΔE=+7.212000 accept=False
    core_region=4 delta_region=80 | E_before=2.600001 E_after=9.812001
    Tile-level changes (top 6 by |ΔE|):
      id=  752 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3473 THIN->THIN move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  899 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2456 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3566 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2461 THIN->THIN move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 750: cluster=[824, 825, 2458] ΔE=+6.951334 accept=False
    core_region=4 delta_region=83 | E_before=2.883334 E_after=9.834667
    Tile-level changes (top 6 by |ΔE|):
      id= 2511 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  821 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  753 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3567 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4109 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 800: cluster=[2243, 2244, 3375] ΔE=+6.207667 accept=False
    core_region=4 delta_region=82 | E_before=4.959518 E_after=11.167185
    Tile-level changes (top 6 by |ΔE|):
      id=  842 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.0000 E:  0.0707-> 2.0000 ΔE=+  1.9293 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  910 THICK->THICK move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2189 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2246 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4160 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
✅ MC sweep: 23/200 accepted (11.5%), max drift: 2.336103
✅ Growth step 4: added 27 tiles
    New tiles: 27, Defects: 2
    Acceptance rate: 11.5%

  Step 5/5
🌿 Growth step 4...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 9.142688 (MC=308.434085, actual=317.576773)
🔁 Step 850: cluster=[3564, 3565, 4165] ΔE=-1.437333 accept=True
    core_region=4 delta_region=33 | E_before=4.257333 E_after=2.820000
    Tile-level changes (top 6 by |ΔE|):
      id= 4192 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  754 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  678 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3564 THICK->THIN move= 0.5878 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2402 THIN->THIN move= 0.0000 E:  0.0687-> 0.0000 ΔE= -0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2399 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 900: cluster=[901, 902, 3473] ΔE=+2.241333 accept=False
    core_region=4 delta_region=16 | E_before=0.266667 E_after=2.508000
    Tile-level changes (top 6 by |ΔE|):
      id= 4108 THICK->THICK move= 0.0000 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  903 THICK->THICK move= 0.0000 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4109 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THICK->THIN move= 0.3090 E:  0.0000-> 0.0540 ΔE=+  0.0540 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2462 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  900 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 950: cluster=[1126, 1127, 3335] ΔE=+9.475000 accept=False
    core_region=4 delta_region=73 | E_before=6.971000 E_after=16.446000
    Tile-level changes (top 6 by |ΔE|):
      id= 2522 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 1123 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4053 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1201 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1199 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4051 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 1000: cluster=[753, 754, 2403] ΔE=+4.360333 accept=False
    core_region=4 delta_region=23 | E_before=2.655000 E_after=7.015333
    Tile-level changes (top 6 by |ΔE|):
      id=  752 THICK->THICK move= 0.0000 E:  0.0000-> 2.0667 ΔE=+  2.0667 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  755 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4165 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2403 THIN->THICK move= 0.5878 E:  0.0000-> 0.0717 ΔE=+  0.0717 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  754 THICK->THICK move= 0.3090 E:  0.0500-> 0.0687 ΔE=+  0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2401 THIN->THIN move= 0.0000 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 16/200 accepted (8.0%), max drift: 9.142688
✅ Growth step 5: added 25 tiles
    New tiles: 25, Defects: 2
    Acceptance rate: 8.0%

✅ Experiment complete!
📊 Results saved to: data/experiments/temp_sweep/tempsweep_base_T0p800_run_018.json
   ↳ file=tempsweep_base_T0p800_run_018.json  acc_mean=0.101  defects=1→2  E_final=312.36675199736044

🌡️  [2/4] Running T=1.0
🧪 Running growth experiment...
==================================================
🔧 debug: verbosity=2, progress_every=1, trace_every=50
Experiment: tempsweep_base_T1p000_run_019
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 5 growth steps...

  Step 1/5
🌿 Growth step 0...
   Running 200 MC steps for healing...
🔁 Step 50: cluster=[838, 839, 2243] ΔE=+8.255333 accept=False
    core_region=4 delta_region=85 | E_before=3.450000 E_after=11.705333
    Tile-level changes (top 6 by |ΔE|):
      id= 3328 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4189 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  835 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  914 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  763 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  842 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 100: cluster=[828, 829, 2405] ΔE=+8.196333 accept=False
    core_region=4 delta_region=86 | E_before=3.500000 E_after=11.696333
    Tile-level changes (top 6 by |ΔE|):
      id= 4137 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3426 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  753 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  904 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  825 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 150: cluster=[902, 903, 4108] ΔE=+9.038000 accept=False
    core_region=4 delta_region=84 | E_before=2.800001 E_after=11.838000
    Tile-level changes (top 6 by |ΔE|):
      id=  975 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4080 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4134 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  827 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2463 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2405 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 200: cluster=[2298, 2299, 4161] ΔE=+5.189000 accept=False
    core_region=4 delta_region=80 | E_before=2.700001 E_after=7.889001
    Tile-level changes (top 6 by |ΔE|):
      id=  985 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4160 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3375 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2245 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.0000 E:  0.0000-> 0.0550 ΔE=+  0.0550 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2299 THIN->THIN move= 0.8090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 14/200 accepted (7.0%), max drift: 0.000000
✅ Growth step 1: added 27 tiles
    New tiles: 27, Defects: 0
    Acceptance rate: 7.0%

  Step 2/5
🌿 Growth step 1...
   Running 200 MC steps for healing...
🔁 Step 250: cluster=[833, 834, 4162] ΔE=+1.170667 accept=False
    core_region=4 delta_region=17 | E_before=4.443334 E_after=5.614000
    Tile-level changes (top 6 by |ΔE|):
      id=  834 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3425 THIN->THIN move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4162 THICK->THICK move= 0.3090 E:  0.0500-> 0.0687 ΔE=+  0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  833 THICK->THIN move= 0.5878 E:  0.0667-> 0.0520 ΔE= -0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3470 THICK->THICK move= 0.0000 E:  0.0550-> 0.0550 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 300: cluster=[2408, 2409, 3427] ΔE=+4.606666 accept=False
    core_region=4 delta_region=80 | E_before=3.910001 E_after=8.516668
    Tile-level changes (top 6 by |ΔE|):
      id= 2351 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  906 THIN->THIN move= 0.0000 E:  2.0000-> 0.0717 ΔE= -1.9283 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2463 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  975 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4135 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 350: cluster=[3332, 3333, 4106] ΔE=+8.384667 accept=False
    core_region=4 delta_region=70 | E_before=4.093334 E_after=12.478001
    Tile-level changes (top 6 by |ΔE|):
      id= 2358 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3379 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1059 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4105 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1129 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3334 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.061000 (MC=309.240668, actual=309.301668)
🔁 Step 400: cluster=[909, 910, 2299] ΔE=+7.982667 accept=False
    core_region=4 delta_region=37 | E_before=3.138334 E_after=11.121000
    Tile-level changes (top 6 by |ΔE|):
      id= 2244 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  838 THIN->THIN move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  986 THIN->THIN move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4160 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  913 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2243 THIN->THIN move= 0.0000 E:  0.0500-> 0.0600 ΔE=+  0.0100 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 13/200 accepted (6.5%), max drift: 0.061000
✅ Growth step 2: added 30 tiles
    New tiles: 30, Defects: 1
    Acceptance rate: 6.5%

  Step 3/5
🌿 Growth step 2...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 0.061000 (MC=309.240668, actual=309.301668)
🔁 Step 450: cluster=[2459, 2460, 3521] ΔE=+5.191000 accept=False
    core_region=4 delta_region=75 | E_before=2.650000 E_after=7.841000
    Tile-level changes (top 6 by |ΔE|):
      id=  898 THICK->THICK move= 0.0000 E:  0.0000-> 2.1353 ΔE=+  2.1353 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3523 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  897 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2514 THIN->THIN move= 0.0000 E:  0.0000-> 0.0570 ΔE=+  0.0570 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2460 THIN->THICK move= 0.5878 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  901 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.065000 (MC=310.161335, actual=310.226335)
🔁 Step 500: cluster=[908, 2353, 4134] ΔE=+1.310666 accept=True
    core_region=4 delta_region=42 | E_before=2.403335 E_after=3.714001
    Tile-level changes (top 6 by |ΔE|):
      id= 3379 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2351 THICK->THICK move= 0.0000 E:  2.0000-> 0.0500 ΔE= -1.9500 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  980 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THIN->THIN move= 0.8090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.145851 (MC=309.651335, actual=309.797186)
⚠️  ENERGY DRIFT : 0.159851 (MC=312.732002, actual=312.891852)
🔁 Step 550: cluster=[899, 2462, 3474] ΔE=-1.237333 accept=True
    core_region=4 delta_region=16 | E_before=3.542334 E_after=2.305001
    Tile-level changes (top 6 by |ΔE|):
      id= 3475 THICK->THICK move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  975 THICK->THICK move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3473 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  900 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  899 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2462 THICK->THIN move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 600: cluster=[2348, 2349, 4163] ΔE=+2.231666 accept=False
    core_region=4 delta_region=20 | E_before=0.050001 E_after=2.281667
    Tile-level changes (top 6 by |ΔE|):
      id= 2351 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4163 THIN->THICK move= 0.3090 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2350 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2349 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3470 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  831 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 26/200 accepted (13.0%), max drift: 0.159851
✅ Growth step 3: added 36 tiles
    New tiles: 36, Defects: 0
    Acceptance rate: 13.0%

  Step 4/5
🌿 Growth step 3...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 1.255850 (MC=311.003335, actual=312.259185)
🔁 Step 650: cluster=[827, 828, 4136] ΔE=+6.302149 accept=False
    core_region=4 delta_region=72 | E_before=6.659851 E_after=12.962000
    Tile-level changes (top 6 by |ΔE|):
      id= 3518 THICK->THICK move= 0.0000 E:  0.0122-> 2.0000 ΔE=+  1.9878 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  753 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  754 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3521 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4109 THICK->THICK move= 0.0000 E:  0.0520-> 1.1000 ΔE=+  1.0480 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  902 THICK->THICK move= 0.0000 E:  1.1000-> 0.0687 ΔE= -1.0313 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 700: cluster=[972, 2518, 3430] ΔE=+0.956000 accept=False
    core_region=4 delta_region=15 | E_before=2.505000 E_after=3.461000
    Tile-level changes (top 6 by |ΔE|):
      id= 3474 THIN->THIN move= 0.0000 E:  0.0667-> 1.1000 ΔE=+  1.0333 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4081 THICK->THICK move= 0.0000 E:  0.0550-> 0.0050 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  972 THIN->THIN move= 0.8090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3475 THICK->THICK move= 0.0000 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  974 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  975 THICK->THICK move= 0.0000 E:  0.0667-> 0.0687 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 1.224816 (MC=319.064335, actual=320.289151)
🔁 Step 750: cluster=[2346, 2347, 3517] ΔE=+6.901333 accept=False
    core_region=4 delta_region=83 | E_before=3.071667 E_after=9.973000
    Tile-level changes (top 6 by |ΔE|):
      id= 4164 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2404 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3561 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  754 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4163 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  686 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 1.242517 (MC=320.960669, actual=322.203186)
🔁 Step 800: cluster=[979, 980, 4107] ΔE=+1.187333 accept=False
    core_region=4 delta_region=17 | E_before=1.420667 E_after=2.608000
    Tile-level changes (top 6 by |ΔE|):
      id= 3380 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  979 THIN->THICK move= 0.5878 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THICK->THICK move= 0.3090 E:  0.0500-> 0.0687 ΔE=+  0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THICK->THICK move= 0.0000 E:  0.0667-> 0.0687 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  980 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 23/200 accepted (11.5%), max drift: 1.255850
✅ Growth step 4: added 35 tiles
    New tiles: 35, Defects: 1
    Acceptance rate: 11.5%

  Step 5/5
🌿 Growth step 4...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 2.522728 (MC=322.129090, actual=324.651818)
🔁 Step 850: cluster=[2403, 2404, 3519] ΔE=+8.178667 accept=False
    core_region=4 delta_region=82 | E_before=9.631000 E_after=17.809667
    Tile-level changes (top 6 by |ΔE|):
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4109 THICK->THICK move= 0.0000 E:  0.0520-> 2.0000 ΔE=+  1.9480 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  757 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2347 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2401 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2406 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 900: cluster=[2465, 3429, 4080] ΔE=+4.200150 accept=False
    core_region=4 delta_region=84 | E_before=9.751184 E_after=13.951334
    Tile-level changes (top 6 by |ΔE|):
      id= 1125 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  979 THIN->THIN move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4053 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4079 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4108 THICK->THICK move= 0.0000 E:  0.0520-> 1.1000 ΔE=+  1.0480 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1047 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.727727 (MC=323.996090, actual=328.723818)
⚠️  ENERGY DRIFT : 4.804360 (MC=326.855424, actual=331.659784)
⚠️  ENERGY DRIFT : 4.796360 (MC=324.422758, actual=329.219117)
🔁 Step 950: cluster=[687, 688, 4216] ΔE=+5.356667 accept=False
    core_region=4 delta_region=74 | E_before=2.533334 E_after=7.890000
    Tile-level changes (top 6 by |ΔE|):
      id= 3513 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4243 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  765 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  760 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  761 THIN->THIN move= 0.0000 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3466 THIN->THIN move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1000: cluster=[2239, 2240, 3467] ΔE=+1.187333 accept=True
    core_region=4 delta_region=14 | E_before=0.300000 E_after=1.487333
    Tile-level changes (top 6 by |ΔE|):
      id= 3466 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2239 THIN->THICK move= 0.5878 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2240 THICK->THICK move= 0.3090 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  765 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  763 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3467 THICK->THIN move= 0.5878 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.941455 (MC=324.793425, actual=329.734880)
✅ MC sweep: 34/200 accepted (17.0%), max drift: 4.941455
✅ Growth step 5: added 34 tiles
    New tiles: 34, Defects: 4
    Acceptance rate: 17.0%

✅ Experiment complete!
📊 Results saved to: data/experiments/temp_sweep/tempsweep_base_T1p000_run_019.json
   ↳ file=tempsweep_base_T1p000_run_019.json  acc_mean=0.11000000000000001  defects=0→4  E_final=324.79342497470384

🌡️  [3/4] Running T=1.2
🧪 Running growth experiment...
==================================================
🔧 debug: verbosity=2, progress_every=1, trace_every=50
Experiment: tempsweep_base_T1p200_run_020
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 5 growth steps...

  Step 1/5
🌿 Growth step 0...
   Running 200 MC steps for healing...
🔁 Step 50: cluster=[976, 977, 3428] ΔE=+7.321667 accept=False
    core_region=4 delta_region=82 | E_before=5.348333 E_after=12.670000
    Tile-level changes (top 6 by |ΔE|):
      id= 2518 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3474 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  900 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  973 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1049 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  980 THICK->THICK move= 0.0000 E:  0.0550-> 1.1000 ΔE=+  1.0450 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.064000 (MC=320.017667, actual=320.081667)
⚠️  ENERGY DRIFT : 0.156000 (MC=319.914001, actual=320.070001)
⚠️  ENERGY DRIFT : 0.156000 (MC=320.970001, actual=321.126001)
🔁 Step 100: cluster=[910, 911, 2300] ΔE=+11.403966 accept=False
    core_region=4 delta_region=73 | E_before=3.246334 E_after=14.650300
    Tile-level changes (top 6 by |ΔE|):
      id= 3424 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3331 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  985 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2297 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3375 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 150: cluster=[830, 831, 3471] ΔE=+0.094000 accept=True
    core_region=4 delta_region=49 | E_before=10.743334 E_after=10.837334
    Tile-level changes (top 6 by |ΔE|):
      id= 3473 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4163 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3472 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  904 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  827 THICK->THICK move= 0.0000 E:  2.0000-> 1.1000 ΔE= -0.9000 class:HIGH_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  903 THIN->THIN move= 0.0000 E:  0.0687-> 0.0000 ΔE= -0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 200: cluster=[2410, 2411, 3380] ΔE=+0.100000 accept=True
    core_region=4 delta_region=14 | E_before=1.270667 E_after=1.370667
    Tile-level changes (top 6 by |ΔE|):
      id= 2411 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3379 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3380 THIN->THICK move= 0.3090 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2410 THIN->THIN move= 0.8090 E:  0.0000-> 0.0000 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3332 THICK->THICK move= 0.0000 E:  1.1000-> 1.1000 ΔE=+  0.0000 class:MEDIUM_ENERGY->MEDIUM_ENERGY removed=False immobile=False
✅ MC sweep: 34/200 accepted (17.0%), max drift: 0.156000
✅ Growth step 1: added 25 tiles
    New tiles: 25, Defects: 2
    Acceptance rate: 17.0%

  Step 2/5
🌿 Growth step 1...
   Running 200 MC steps for healing...
🔁 Step 250: cluster=[984, 985, 3331] ΔE=-0.314666 accept=True
    core_region=4 delta_region=14 | E_before=2.548334 E_after=2.233668
    Tile-level changes (top 6 by |ΔE|):
      id= 2302 THICK->THICK move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  983 THIN->THIN move= 0.0000 E:  1.1000-> 2.0000 ΔE=+  0.9000 class:MEDIUM_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3331 THIN->THIN move= 0.8090 E:  0.0687-> 0.0000 ΔE= -0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3332 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0520-> 0.0550 ΔE=+  0.0030 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2355 THIN->THIN move= 0.0000 E:  0.0540-> 0.0550 ΔE=+  0.0010 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 0.331760 (MC=329.994542, actual=330.326302)
🔁 Step 300: cluster=[759, 760, 2294] ΔE=+6.012149 accept=False
    core_region=4 delta_region=85 | E_before=8.483518 E_after=14.495667
    Tile-level changes (top 6 by |ΔE|):
      id=  756 THIN->THIN move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3423 THICK->THICK move= 0.0000 E:  0.0520-> 2.0000 ΔE=+  1.9480 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2349 THICK->THICK move= 0.0000 E:  1.1020-> 0.0500 ΔE= -1.0520 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  688 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  763 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2239 THIN->THIN move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 1.411189 (MC=330.148998, actual=331.560187)
🔁 Step 350: cluster=[828, 3519, 4136] ΔE=+2.393333 accept=False
    core_region=4 delta_region=16 | E_before=4.293334 E_after=6.686667
    Tile-level changes (top 6 by |ΔE|):
      id= 3520 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2403 THICK->THICK move= 0.0000 E:  0.0667-> 1.1000 ΔE=+  1.0333 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4136 THIN->THIN move= 0.8090 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2404 THICK->THICK move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  829 THICK->THICK move= 0.0000 E:  0.0100-> 0.0600 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 2.486312 (MC=325.061542, actual=327.547853)
🔁 Step 400: cluster=[2356, 2357, 3332] ΔE=+4.175666 accept=False
    core_region=4 delta_region=29 | E_before=5.243667 E_after=9.419334
    Tile-level changes (top 6 by |ΔE|):
      id= 3377 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3333 THIN->THIN move= 0.0000 E:  0.0020-> 1.1000 ΔE=+  1.0980 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3332 THICK->THIN move= 0.5878 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4107 THICK->THICK move= 0.0000 E:  0.0550-> 1.1000 ΔE=+  1.0450 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2354 THICK->THICK move= 0.0000 E:  0.0717-> 1.1000 ΔE=+  1.0283 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  982 THIN->THIN move= 0.0000 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 64/200 accepted (32.0%), max drift: 2.486312
✅ Growth step 2: added 25 tiles
    New tiles: 25, Defects: 3
    Acceptance rate: 32.0%

  Step 3/5
🌿 Growth step 2...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 4.355101 (MC=323.550841, actual=327.905942)
🔁 Step 450: cluster=[2410, 2411, 3380] ΔE=+2.924666 accept=False
    core_region=4 delta_region=32 | E_before=7.458000 E_after=10.382667
    Tile-level changes (top 6 by |ΔE|):
      id= 3379 THICK->THICK move= 0.0000 E:  2.0000-> 0.0000 ΔE= -2.0000 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  906 THICK->THICK move= 0.0000 E:  0.0590-> 2.0000 ΔE=+  1.9410 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  981 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  982 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2408 THIN->THIN move= 0.0000 E:  0.0550-> 1.1020 ΔE=+  1.0470 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  980 THICK->THICK move= 0.0000 E:  1.1000-> 0.0550 ΔE= -1.0450 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 500: cluster=[2410, 2411, 3380] ΔE=+6.539334 accept=False
    core_region=4 delta_region=34 | E_before=8.787000 E_after=15.326334
    Tile-level changes (top 6 by |ΔE|):
      id= 3332 THIN->THIN move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  982 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  980 THICK->THICK move= 0.0000 E:  1.1020-> 0.0550 ΔE= -1.0470 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2408 THIN->THIN move= 0.0000 E:  0.0550-> 1.1020 ΔE=+  1.0470 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3427 THICK->THICK move= 0.0000 E:  0.0667-> 1.1020 ΔE=+  1.0353 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3333 THIN->THIN move= 0.0000 E:  1.1000-> 2.0000 ΔE=+  0.9000 class:MEDIUM_ENERGY->HIGH_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 3.499626 (MC=325.728913, actual=329.228540)
🔁 Step 550: cluster=[2460, 2461, 4109] ΔE=+2.220666 accept=False
    core_region=4 delta_region=15 | E_before=2.591334 E_after=4.812000
    Tile-level changes (top 6 by |ΔE|):
      id= 2459 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3473 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4109 THIN->THIN move= 0.8090 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3519 THIN->THIN move= 0.0000 E:  0.0520-> 0.0000 ΔE= -0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2461 THIN->THICK move= 0.3090 E:  0.0667-> 0.0520 ΔE= -0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4136 THICK->THICK move= 0.0000 E:  0.0520-> 0.0667 ΔE=+  0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.704411 (MC=327.182913, actual=331.887324)
🔁 Step 600: cluster=[1056, 1057, 2357] ΔE=+3.194149 accept=False
    core_region=4 delta_region=37 | E_before=8.077518 E_after=11.271667
    Tile-level changes (top 6 by |ΔE|):
      id=  981 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 1053 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3332 THIN->THIN move= 0.0000 E:  2.0000-> 0.0667 ΔE= -1.9333 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3334 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 1055 THIN->THIN move= 0.0000 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1130 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 55/200 accepted (27.5%), max drift: 4.704411
✅ Growth step 3: added 19 tiles
    New tiles: 19, Defects: 3
    Acceptance rate: 27.5%

  Step 4/5
🌿 Growth step 3...
   Running 200 MC steps for healing...
🔁 Step 650: cluster=[2356, 2357, 3332] ΔE=-2.877667 accept=True
    core_region=4 delta_region=35 | E_before=11.472334 E_after=8.594667
    Tile-level changes (top 6 by |ΔE|):
      id= 3379 THICK->THICK move= 0.0000 E:  2.0000-> 0.0000 ΔE= -2.0000 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  984 THICK->THICK move= 0.0000 E:  2.0000-> 1.1020 ΔE= -0.8980 class:HIGH_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  981 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4133 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  982 THICK->THICK move= 0.0000 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2354 THIN->THIN move= 0.0000 E:  0.0570-> 0.0667 ΔE=+  0.0097 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 7.108376 (MC=324.285765, actual=331.394141)
⚠️  ENERGY DRIFT : 9.383674 (MC=324.890765, actual=334.274439)
🔁 Step 700: cluster=[984, 986, 2302] ΔE=+3.335666 accept=False
    core_region=4 delta_region=23 | E_before=2.817000 E_after=6.152667
    Tile-level changes (top 6 by |ΔE|):
      id= 2356 THICK->THICK move= 0.0000 E:  0.0020-> 1.1050 ΔE=+  1.1030 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3331 THIN->THIN move= 0.0000 E:  0.0020-> 1.1000 ΔE=+  1.0980 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2353 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  986 THICK->THIN move= 0.5878 E:  1.1000-> 0.0550 ΔE= -1.0450 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  984 THICK->THICK move= 0.3090 E:  1.1000-> 2.1353 ΔE=+  1.0353 class:MEDIUM_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2302 THIN->THICK move= 0.5878 E:  0.0040-> 0.0737 ΔE=+  0.0697 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 9.372674 (MC=321.681152, actual=331.053826)
⚠️  ENERGY DRIFT : 9.351041 (MC=323.502574, actual=332.853615)
⚠️  ENERGY DRIFT : 9.359041 (MC=322.949574, actual=332.308616)
⚠️  ENERGY DRIFT : 9.380050 (MC=320.360907, actual=329.740957)
⚠️  ENERGY DRIFT : 9.355133 (MC=326.695205, actual=336.050339)
🔁 Step 750: cluster=[3374, 3375, 4187] ΔE=+6.085000 accept=False
    core_region=4 delta_region=16 | E_before=2.671667 E_after=8.756667
    Tile-level changes (top 6 by |ΔE|):
      id= 2244 THICK->THICK move= 0.0000 E:  0.0667-> 2.0667 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3329 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3374 THICK->THICK move= 0.3090 E:  0.0667-> 1.1000 ΔE=+  1.0333 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  911 THIN->THIN move= 0.0000 E:  0.0667-> 1.1000 ΔE=+  1.0333 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4187 THIN->THICK move= 0.5878 E:  0.0717-> 0.0570 ΔE= -0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3330 THIN->THIN move= 0.0000 E:  0.0500-> 0.0570 ΔE=+  0.0070 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 9.316247 (MC=327.906205, actual=337.222452)
⚠️  ENERGY DRIFT : 9.390798 (MC=331.036872, actual=340.427670)
⚠️  ENERGY DRIFT : 9.407806 (MC=330.920207, actual=340.328013)
🔁 Step 800: cluster=[755, 756, 3518] ΔE=+1.819483 accept=False
    core_region=4 delta_region=23 | E_before=0.578851 E_after=2.398334
    Tile-level changes (top 6 by |ΔE|):
      id=  829 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3470 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4163 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  831 THICK->THICK move= 0.0000 E:  0.0122-> 0.0000 ΔE= -0.0122 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  828 THICK->THICK move= 0.0000 E:  0.0667-> 0.0717 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  754 THICK->THICK move= 0.0000 E:  0.0500-> 0.0550 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 49/200 accepted (24.5%), max drift: 9.407806
✅ Growth step 4: added 25 tiles
    New tiles: 25, Defects: 5
    Acceptance rate: 24.5%

  Step 5/5
🌿 Growth step 4...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 9.367717 (MC=331.082539, actual=340.450256)
🔁 Step 850: cluster=[977, 978, 3427] ΔE=+3.945255 accept=False
    core_region=4 delta_region=54 | E_before=12.334841 E_after=16.280096
    Tile-level changes (top 6 by |ΔE|):
      id= 3428 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2354 THIN->THIN move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3473 THICK->THICK move= 0.0000 E:  0.0050-> 2.0000 ΔE=+  1.9950 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  905 THICK->THICK move= 0.0000 E:  2.0000-> 0.0667 ΔE= -1.9333 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  976 THICK->THICK move= 0.0000 E:  1.1353-> 0.0520 ΔE= -1.0833 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2407 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
🔁 Step 900: cluster=[688, 689, 2238] ΔE=+6.228333 accept=False
    core_region=4 delta_region=86 | E_before=4.616299 E_after=10.844633
    Tile-level changes (top 6 by |ΔE|):
      id= 2293 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  685 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  692 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  763 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4215 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3468 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 8.416958 (MC=329.463897, actual=337.880855)
⚠️  ENERGY DRIFT : 8.333030 (MC=331.077897, actual=339.410927)
⚠️  ENERGY DRIFT : 8.333030 (MC=331.127897, actual=339.460927)
⚠️  ENERGY DRIFT : 8.329030 (MC=330.057230, actual=338.386260)
🔁 Step 950: cluster=[3374, 3375, 4187] ΔE=+0.915000 accept=False
    core_region=4 delta_region=14 | E_before=2.687333 E_after=3.602334
    Tile-level changes (top 6 by |ΔE|):
      id=  914 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3374 THICK->THIN move= 0.5878 E:  1.1000-> 0.0687 ΔE= -1.0313 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4187 THICK->THICK move= 0.3090 E:  0.0687-> 0.0500 ΔE= -0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3376 THICK->THICK move= 0.0000 E:  0.0500-> 0.0667 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  910 THICK->THICK move= 0.0000 E:  0.0667-> 0.0717 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4161 THIN->THIN move= 0.0000 E:  0.0000-> 0.0050 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 1000: cluster=[976, 2463, 3429] ΔE=+3.930000 accept=False
    core_region=4 delta_region=22 | E_before=2.908000 E_after=6.838000
    Tile-level changes (top 6 by |ΔE|):
      id= 2461 THIN->THIN move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  975 THIN->THIN move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2462 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  899 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2463 THICK->THICK move= 0.3090 E:  0.0667-> 1.1020 ΔE=+  1.0353 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3475 THIN->THIN move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 57/200 accepted (28.5%), max drift: 9.407806
✅ Growth step 5: added 25 tiles
    New tiles: 25, Defects: 1
    Acceptance rate: 28.5%

✅ Experiment complete!
📊 Results saved to: data/experiments/temp_sweep/tempsweep_base_T1p200_run_020.json
   ↳ file=tempsweep_base_T1p200_run_020.json  acc_mean=0.259  defects=2→1  E_final=317.09756500841615

🌡️  [4/4] Running T=1.5
🧪 Running growth experiment...
==================================================
🔧 debug: verbosity=2, progress_every=1, trace_every=50
Experiment: tempsweep_base_T1p500_run_021
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 5 growth steps...

  Step 1/5
🌿 Growth step 0...
   Running 200 MC steps for healing...
🔁 Step 50: cluster=[833, 834, 4162] ΔE=-0.166667 accept=True
    core_region=4 delta_region=79 | E_before=4.920000 E_after=4.753333
    Tile-level changes (top 6 by |ΔE|):
      id= 3426 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  909 THICK->THICK move= 0.0000 E:  2.0000-> 0.0000 ΔE= -2.0000 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2299 THIN->THIN move= 0.0000 E:  0.0050-> 0.0667 ΔE=+  0.0617 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2294 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2348 THIN->THIN move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  837 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 100: cluster=[756, 757, 2347] ΔE=+5.010667 accept=False
    core_region=4 delta_region=81 | E_before=7.347667 E_after=12.358333
    Tile-level changes (top 6 by |ΔE|):
      id=  681 THICK->THICK move= 0.0000 E:  0.0500-> 2.1353 ΔE=+  2.0853 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2295 THICK->THICK move= 0.0000 E:  2.1333-> 0.0667 ΔE= -2.0667 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2345 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  829 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4191 THICK->THICK move= 0.0000 E:  0.0500-> 1.1050 ΔE=+  1.0550 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2294 THICK->THICK move= 0.0000 E:  0.0737-> 0.0000 ΔE= -0.0737 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 1.198551 (MC=321.131150, actual=322.329701)
⚠️  ENERGY DRIFT : 1.322919 (MC=328.086967, actual=329.409886)
⚠️  ENERGY DRIFT : 0.227919 (MC=330.296450, actual=330.524369)
🔁 Step 150: cluster=[2294, 2295, 3469] ΔE=+5.291000 accept=False
    core_region=4 delta_region=45 | E_before=4.394334 E_after=9.685334
    Tile-level changes (top 6 by |ΔE|):
      id=  685 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3517 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  757 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3470 THICK->THICK move= 0.0000 E:  1.1000-> 2.1333 ΔE=+  1.0333 class:MEDIUM_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2348 THIN->THIN move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 3.351409 (MC=335.204451, actual=338.555860)
🔁 Step 200: cluster=[838, 839, 2243] ΔE=+0.000000 accept=True
    core_region=4 delta_region=19 | E_before=1.604000 E_after=1.604001
    Tile-level changes (top 6 by |ΔE|):
      id= 3376 THIN->THIN move= 0.0000 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2243 THIN->THICK move= 0.3090 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  839 THICK->THIN move= 0.3090 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2244 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  912 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  838 THIN->THIN move= 0.8090 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 54/200 accepted (27.0%), max drift: 3.351409
✅ Growth step 1: added 22 tiles
    New tiles: 22, Defects: 4
    Acceptance rate: 27.0%

  Step 2/5
🌿 Growth step 1...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 2.503865 (MC=338.488662, actual=340.992527)
🔁 Step 250: cluster=[910, 911, 2300] ΔE=+5.143666 accept=False
    core_region=4 delta_region=26 | E_before=4.952334 E_after=10.096000
    Tile-level changes (top 6 by |ΔE|):
      id=  834 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4161 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2299 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4133 THICK->THICK move= 0.0000 E:  1.1000-> 0.0667 ΔE= -1.0333 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2300 THICK->THICK move= 0.3090 E:  0.0687-> 1.1000 ΔE=+  1.0313 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  911 THIN->THICK move= 0.5878 E:  0.0000-> 0.0707 ΔE=+  0.0707 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.648995 (MC=339.404593, actual=344.053588)
🔁 Step 300: cluster=[836, 2296, 3423] ΔE=+8.880701 accept=False
    core_region=4 delta_region=33 | E_before=4.091633 E_after=12.972334
    Tile-level changes (top 6 by |ΔE|):
      id= 3469 THICK->THICK move= 0.0000 E:  0.0687-> 2.1333 ΔE=+  2.0647 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2349 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  759 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4189 THICK->THICK move= 0.0000 E:  0.0687-> 2.0667 ΔE=+  1.9980 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  760 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2296 THIN->THICK move= 0.5878 E:  1.1000-> 0.0550 ΔE= -1.0450 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.646362 (MC=332.000007, actual=336.646369)
⚠️  ENERGY DRIFT : 5.748362 (MC=332.016673, actual=337.765036)
⚠️  ENERGY DRIFT : 5.900543 (MC=330.585341, actual=336.485884)
⚠️  ENERGY DRIFT : 5.907543 (MC=329.521341, actual=335.428884)
⚠️  ENERGY DRIFT : 7.037175 (MC=332.030340, actual=339.067515)
🔁 Step 350: cluster=[975, 2462, 4108] ΔE=+1.158000 accept=True
    core_region=4 delta_region=20 | E_before=2.641334 E_after=3.799334
    Tile-level changes (top 6 by |ΔE|):
      id= 4080 THIN->THIN move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4108 THICK->THIN move= 0.3090 E:  0.0000-> 0.0500 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2464 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2465 THICK->THICK move= 0.0000 E:  0.0667-> 0.0687 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1050 THICK->THICK move= 0.0000 E:  0.0000-> 0.0020 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1051 THIN->THIN move= 0.0000 E:  0.0000-> 0.0020 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.777811 (MC=334.756375, actual=339.534186)
⚠️  ENERGY DRIFT : 4.779811 (MC=335.927042, actual=340.706853)
🔁 Step 400: cluster=[829, 830, 2405] ΔE=+1.154000 accept=True
    core_region=4 delta_region=11 | E_before=4.429667 E_after=5.583667
    Tile-level changes (top 6 by |ΔE|):
      id=  830 THIN->THICK move= 0.5878 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4136 THIN->THIN move= 0.0000 E:  0.0040-> 0.0540 ΔE=+  0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  829 THICK->THICK move= 0.3090 E:  0.0500-> 0.0687 ΔE=+  0.0187 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2405 THICK->THIN move= 0.5878 E:  0.0667-> 0.0520 ΔE= -0.0147 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2406 THICK->THICK move= 0.0000 E:  0.0500-> 0.0500 ΔE= -0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  902 THICK->THICK move= 0.0000 E:  0.0000-> 0.0000 ΔE=+  0.0000 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 84/200 accepted (42.0%), max drift: 7.037175
✅ Growth step 2: added 19 tiles
    New tiles: 19, Defects: 6
    Acceptance rate: 42.0%

  Step 3/5
🌿 Growth step 2...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 6.877375 (MC=338.053111, actual=344.930486)
🔁 Step 450: cluster=[763, 764, 2241] ΔE=+10.297632 accept=False
    core_region=4 delta_region=81 | E_before=11.367701 E_after=21.665333
    Tile-level changes (top 6 by |ΔE|):
      id= 4214 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4216 THICK->THICK move= 0.0000 E:  2.0000-> 0.0000 ΔE= -2.0000 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  837 THICK->THICK move= 0.0000 E:  0.0667-> 2.0050 ΔE=+  1.9383 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3375 THICK->THICK move= 0.0000 E:  0.0687-> 2.0000 ΔE=+  1.9313 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4188 THICK->THICK move= 0.0000 E:  0.0622-> 1.1333 ΔE=+  1.0711 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2186 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 8.958743 (MC=338.923144, actual=347.881887)
⚠️  ENERGY DRIFT : 8.960926 (MC=337.587145, actual=346.548071)
⚠️  ENERGY DRIFT : 5.775260 (MC=336.275146, actual=342.050406)
🔁 Step 500: cluster=[839, 840, 3375] ΔE=+5.383816 accept=True
    core_region=4 delta_region=66 | E_before=5.633184 E_after=11.017000
    Tile-level changes (top 6 by |ΔE|):
      id= 2190 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3376 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 2243 THICK->THICK move= 0.0000 E:  2.0000-> 0.0000 ΔE= -2.0000 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2242 THICK->THICK move= 0.0000 E:  0.0122-> 1.1000 ΔE=+  1.0878 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  913 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2245 THICK->THICK move= 0.0000 E:  0.0500-> 1.1020 ΔE=+  1.0520 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 4.755260 (MC=341.505963, actual=346.261223)
🔁 Step 550: cluster=[837, 2297, 4161] ΔE=+6.389931 accept=False
    core_region=4 delta_region=40 | E_before=5.246403 E_after=11.636334
    Tile-level changes (top 6 by |ΔE|):
      id=  908 THICK->THICK move= 0.0000 E:  0.0244-> 2.0000 ΔE=+  1.9756 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  911 THICK->THICK move= 0.0000 E:  0.0050-> 1.1000 ΔE=+  1.0950 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  761 THICK->THICK move= 0.0000 E:  0.0540-> 1.1020 ΔE=+  1.0480 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2297 THIN->THICK move= 0.5878 E:  0.0667-> 1.1000 ΔE=+  1.0333 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2296 THICK->THICK move= 0.0000 E:  0.0687-> 1.1020 ΔE=+  1.0333 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  836 THIN->THIN move= 0.0000 E:  0.0000-> 0.0687 ΔE=+  0.0687 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
🔁 Step 600: cluster=[833, 3470, 4162] ΔE=+6.456666 accept=False
    core_region=4 delta_region=33 | E_before=3.847334 E_after=10.304000
    Tile-level changes (top 6 by |ΔE|):
      id=  907 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  759 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  832 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2294 THICK->THICK move= 0.0000 E:  0.0520-> 1.1000 ΔE=+  1.0480 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  908 THICK->THICK move= 0.0000 E:  0.0000-> 0.0717 ΔE=+  0.0717 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3470 THIN->THIN move= 0.8090 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 67/200 accepted (33.5%), max drift: 8.960926
✅ Growth step 3: added 15 tiles
    New tiles: 15, Defects: 8
    Acceptance rate: 33.5%

  Step 4/5
🌿 Growth step 3...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 8.982198 (MC=350.040778, actual=359.022976)
⚠️  ENERGY DRIFT : 7.822811 (MC=344.750111, actual=352.572923)
⚠️  ENERGY DRIFT : 8.914593 (MC=343.432289, actual=352.346882)
🔁 Step 650: cluster=[829, 2405, 4136] ΔE=+7.464666 accept=False
    core_region=4 delta_region=41 | E_before=7.290001 E_after=14.754667
    Tile-level changes (top 6 by |ΔE|):
      id= 4137 THICK->THICK move= 0.0000 E:  0.0000-> 2.0000 ΔE=+  2.0000 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  900 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  830 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  904 THICK->THICK move= 0.0000 E:  0.0520-> 1.1020 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3472 THICK->THICK move= 0.0000 E:  1.1020-> 0.0520 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  902 THICK->THICK move= 0.0000 E:  0.0550-> 1.1050 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 9.268259 (MC=350.905042, actual=360.173302)
⚠️  ENERGY DRIFT : 9.290627 (MC=351.402042, actual=360.692669)
⚠️  ENERGY DRIFT : 9.288695 (MC=349.906708, actual=359.195404)
⚠️  ENERGY DRIFT : 8.236695 (MC=351.094042, actual=359.330737)
⚠️  ENERGY DRIFT : 8.233695 (MC=350.017076, actual=358.250771)
⚠️  ENERGY DRIFT : 8.322607 (MC=355.828498, actual=364.151105)
🔁 Step 700: cluster=[985, 987, 2302] ΔE=+2.278666 accept=False
    core_region=4 delta_region=27 | E_before=0.679667 E_after=2.958334
    Tile-level changes (top 6 by |ΔE|):
      id= 3331 THICK->THICK move= 0.0000 E:  0.0000-> 1.1000 ΔE=+  1.1000 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4105 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2302 THIN->THICK move= 0.3090 E:  0.0000-> 0.0667 ΔE=+  0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  985 THICK->THIN move= 0.3090 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2303 THICK->THICK move= 0.0000 E:  0.0000-> 0.0520 ΔE=+  0.0520 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2304 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 8.334791 (MC=355.699130, actual=364.033921)
⚠️  ENERGY DRIFT : 11.405723 (MC=351.151615, actual=362.557338)
🔁 Step 750: cluster=[912, 2300, 3376] ΔE=-0.192000 accept=True
    core_region=4 delta_region=42 | E_before=8.900667 E_after=8.708667
    Tile-level changes (top 6 by |ΔE|):
      id= 2300 THICK->THIN move= 0.3090 E:  2.0000-> 0.0000 ΔE= -2.0000 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4133 THICK->THICK move= 0.0000 E:  0.0500-> 2.0000 ΔE=+  1.9500 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 4160 THICK->THICK move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2244 THICK->THICK move= 0.0000 E:  1.1000-> 0.0540 ΔE= -1.0460 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  839 THICK->THICK move= 0.0000 E:  0.0540-> 1.1000 ΔE=+  1.0460 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4187 THICK->THICK move= 0.0000 E:  0.0560-> 1.1000 ΔE=+  1.0440 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 14.739151 (MC=345.870037, actual=360.609188)
🔁 Step 800: cluster=[839, 2243, 2244] ΔE=+0.020667 accept=True
    core_region=4 delta_region=23 | E_before=2.841334 E_after=2.862001
    Tile-level changes (top 6 by |ΔE|):
      id= 2243 THIN->THICK move= 0.5878 E:  0.0020-> 1.1000 ΔE=+  1.0980 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  839 THICK->THICK move= 0.3090 E:  1.1000-> 0.0687 ΔE= -1.0313 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2298 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2244 THICK->THIN move= 0.5878 E:  0.0540-> 0.0707 ΔE=+  0.0167 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2299 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2245 THICK->THICK move= 0.0000 E:  0.0500-> 0.0520 ΔE=+  0.0020 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 87/200 accepted (43.5%), max drift: 14.739151
✅ Growth step 4: added 9 tiles
    New tiles: 9, Defects: 4
    Acceptance rate: 43.5%

  Step 5/5
🌿 Growth step 4...
   Running 200 MC steps for healing...
⚠️  ENERGY DRIFT : 14.820967 (MC=348.948037, actual=363.769004)
⚠️  ENERGY DRIFT : 15.157104 (MC=347.902037, actual=363.059141)
🔁 Step 850: cluster=[909, 910, 3377] ΔE=+0.403482 accept=False
    core_region=4 delta_region=51 | E_before=11.990852 E_after=12.394333
    Tile-level changes (top 6 by |ΔE|):
      id= 3331 THICK->THICK move= 0.0000 E:  0.0570-> 2.0000 ΔE=+  1.9430 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  984 THIN->THIN move= 0.0000 E:  2.0000-> 0.0717 ΔE= -1.9283 class:HIGH_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  907 THICK->THICK move= 0.0000 E:  0.0264-> 1.1000 ΔE=+  1.0736 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 2354 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2353 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id=  980 THIN->THIN move= 0.0000 E:  0.0550-> 1.1020 ΔE=+  1.0470 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 15.129330 (MC=347.988980, actual=363.118310)
⚠️  ENERGY DRIFT : 15.189963 (MC=346.819164, actual=362.009127)
⚠️  ENERGY DRIFT : 17.436029 (MC=348.900945, actual=366.336973)
⚠️  ENERGY DRIFT : 17.382362 (MC=348.736346, actual=366.118708)
🔁 Step 900: cluster=[2346, 3516, 3517] ΔE=-0.083333 accept=True
    core_region=4 delta_region=31 | E_before=7.435000 E_after=7.351668
    Tile-level changes (top 6 by |ΔE|):
      id= 2350 THIN->THIN move= 0.0000 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  683 THICK->THICK move= 0.0000 E:  1.1000-> 0.0000 ΔE= -1.1000 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2348 THICK->THICK move= 0.0000 E:  1.1000-> 0.0500 ΔE= -1.0500 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2349 THICK->THICK move= 0.0000 E:  0.0667-> 1.1020 ΔE=+  1.0353 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  755 THICK->THICK move= 0.0000 E:  0.0687-> 1.1000 ΔE=+  1.0313 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  759 THIN->THIN move= 0.0000 E:  1.1000-> 0.0687 ΔE= -1.0313 class:MEDIUM_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 17.436322 (MC=346.561347, actual=363.997669)
⚠️  ENERGY DRIFT : 17.427322 (MC=345.473347, actual=362.900669)
🔁 Step 950: cluster=[836, 3422, 4188] ΔE=+6.052667 accept=False
    core_region=4 delta_region=21 | E_before=4.813000 E_after=10.865667
    Tile-level changes (top 6 by |ΔE|):
      id= 2299 THICK->THICK move= 0.0000 E:  0.0520-> 2.0000 ΔE=+  1.9480 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id= 3422 THIN->THICK move= 0.5878 E:  0.0000-> 1.1020 ΔE=+  1.1020 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 3424 THICK->THICK move= 0.0000 E:  0.0500-> 1.1000 ΔE=+  1.0500 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id= 4188 THICK->THICK move= 0.3090 E:  0.0667-> 1.1020 ΔE=+  1.0353 class:LOW_ENERGY->MEDIUM_ENERGY removed=False immobile=False
      id=  839 THICK->THICK move= 0.0000 E:  1.1020-> 2.0000 ΔE=+  0.8980 class:MEDIUM_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  836 THICK->THIN move= 0.5878 E:  0.0667-> 0.0540 ΔE= -0.0127 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
⚠️  ENERGY DRIFT : 21.739023 (MC=345.140684, actual=366.879707)
⚠️  ENERGY DRIFT : 21.674356 (MC=344.170017, actual=365.844373)
🔁 Step 1000: cluster=[974, 2463, 3429] ΔE=+1.765002 accept=False
    core_region=4 delta_region=25 | E_before=2.624669 E_after=4.389671
    Tile-level changes (top 6 by |ΔE|):
      id= 2410 THICK->THICK move= 0.0000 E:  0.0667-> 2.0000 ΔE=+  1.9333 class:LOW_ENERGY->HIGH_ENERGY removed=False immobile=False
      id=  976 THICK->THICK move= 0.0000 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 2463 THICK->THIN move= 0.3090 E:  0.0667-> 0.0000 ΔE= -0.0667 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 3428 THICK->THICK move= 0.0000 E:  0.0500-> 0.0000 ΔE= -0.0500 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 4108 THICK->THICK move= 0.0000 E:  0.0000-> 0.0050 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
      id= 1053 THIN->THIN move= 0.0000 E:  0.0000-> 0.0050 ΔE=+  0.0050 class:LOW_ENERGY->LOW_ENERGY removed=False immobile=False
✅ MC sweep: 82/200 accepted (41.0%), max drift: 21.739023
✅ Growth step 5: added 21 tiles
    New tiles: 21, Defects: 7
    Acceptance rate: 41.0%

✅ Experiment complete!
📊 Results saved to: data/experiments/temp_sweep/tempsweep_base_T1p500_run_021.json
   ↳ file=tempsweep_base_T1p500_run_021.json  acc_mean=0.374  defects=4→7  E_final=348.62068354692576

✅ Temperature sweep complete!
📊 Summary saved to: data/experiments/temp_sweep/tempsweep_base_run_018.json
randa@Randa:quasi-phason$