🚀 Starting Milestone 1: Penrose Tiling Generation
📁 Using config: configs/phase1_baseline.toml
🔷 Generating Penrose P3 tiling...
🔄 Synchronizing neighbor lists with adjacency graph...
✅ Synchronized 4406 tile neighbor lists
✅ Neighbor list synchronization validated
Tiling validation found 1 issues:
  - Found 12 tiles with only 1 neighbor
📊 Creating visualization...
💾 Data exported to: data/obstacles/penrose_tiling.json

✅ Milestone 1 Complete!
   • Generated 4406 tiles
   • Thick/Thin ratio: 2718/1688
   • Adjacency computed: True
   • Window: [0.0, 0.0] to [60.0, 60.0]
🚀 STARTING MILESTONE 2A: HIGH-PERFORMANCE OBSTACLE CREATION
📁 Config: configs/phase2_obstacles.toml
⚠️  WARNING: data/obstacles already has data!
   Run: python scripts/archive_obstacles.py to archive existing data
   Continue anyway? (y/n): 


   randa@Randa:quasi-phason$ python scripts/run_milestone2_obstacle.py
🚀 STARTING MILESTONE 2A: HIGH-PERFORMANCE OBSTACLE CREATION
📁 Config: configs/phase2_obstacles.toml
⚠️  WARNING: data/obstacles already has data!
   Run: python scripts/archive_obstacles.py to archive existing data
   Continue anyway? (y/n): y
📐 Loaded base tiling: 4406 tiles
📊 Generated 12 obstacle configurations

🔧 Creating pores_density_0.005...
🚀 Creating pores obstacles (density: 0.005)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: data/obstacles/pores/pores_density_0.005.json

🔧 Creating fixed_defects_density_0.005...
🚀 Creating fixed_defects obstacles (density: 0.005)
📊 Built spatial index with KDTree
   → Created 22 fixed defects (target: 22)
💾 Saved: data/obstacles/fixed_defects/fixed_defects_density_0.005.json

🔧 Creating pores_density_0.01...
🚀 Creating pores obstacles (density: 0.01)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: data/obstacles/pores/pores_density_0.01.json

🔧 Creating fixed_defects_density_0.01...
🚀 Creating fixed_defects obstacles (density: 0.01)
📊 Built spatial index with KDTree
   → Created 44 fixed defects (target: 44)
💾 Saved: data/obstacles/fixed_defects/fixed_defects_density_0.01.json

🔧 Creating pores_density_0.02...
🚀 Creating pores obstacles (density: 0.02)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: data/obstacles/pores/pores_density_0.02.json

🔧 Creating fixed_defects_density_0.02...
🚀 Creating fixed_defects obstacles (density: 0.02)
📊 Built spatial index with KDTree
   → Created 88 fixed defects (target: 88)
💾 Saved: data/obstacles/fixed_defects/fixed_defects_density_0.02.json

🔧 Creating pores_density_0.03...
🚀 Creating pores obstacles (density: 0.03)
📊 Built spatial index with KDTree
   → Removed 95 tiles within 1 pore regions
💾 Saved: data/obstacles/pores/pores_density_0.03.json

🔧 Creating fixed_defects_density_0.03...
🚀 Creating fixed_defects obstacles (density: 0.03)
📊 Built spatial index with KDTree
   → Created 132 fixed defects (target: 132)
💾 Saved: data/obstacles/fixed_defects/fixed_defects_density_0.03.json

🔧 Creating pores_density_0.05...
🚀 Creating pores obstacles (density: 0.05)
📊 Built spatial index with KDTree
   → Removed 193 tiles within 2 pore regions
💾 Saved: data/obstacles/pores/pores_density_0.05.json

🔧 Creating fixed_defects_density_0.05...
🚀 Creating fixed_defects obstacles (density: 0.05)
📊 Built spatial index with KDTree
   → Created 220 fixed defects (target: 220)
💾 Saved: data/obstacles/fixed_defects/fixed_defects_density_0.05.json

🔧 Creating pores_density_0.1...
🚀 Creating pores obstacles (density: 0.1)
📊 Built spatial index with KDTree
   → Removed 481 tiles within 5 pore regions
💾 Saved: data/obstacles/pores/pores_density_0.1.json

🔧 Creating fixed_defects_density_0.1...
🚀 Creating fixed_defects obstacles (density: 0.1)
📊 Built spatial index with KDTree
   → Created 441 fixed defects (target: 441)
💾 Saved: data/obstacles/fixed_defects/fixed_defects_density_0.1.json
📊 Experiment summary: data/obstacles/experiment_summary.json

✅ MILESTONE 2A COMPLETED IN 49.69s
   • Generated 12 obstacle configurations
   • Output: data/obstacles
   • Run verification: python scripts/verify_obstacles.py
randa@Randa:quasi-phason$

randa@Randa:quasi-phason$ python scripts/debug_validation.py
🔧 Config settings: use_sampling=True, sample_size=100
🔄 Synchronizing neighbor lists with adjacency graph...
✅ Synchronized 4406 tile neighbor lists
✅ Neighbor list synchronization validated
Tiling validation found 1 issues:
  - Found 12 tiles with only 1 neighbor
🔍 SAMPLING MODE: Processing 100 tiles (config: debug.use_sampling=true)
🔍 DEBUGGING VERTEX CLASSIFICATION
============================================================

📐 Tile 0:
   Center type: THICK
   Coordination: 2
   Angles: ['144.0°', '144.0°']
   Angle std: 0.0°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 1.00
   Coordination quality: 0.60
   🎯 FINAL CLASS: LOW_ENERGY
   ✅ LOW_ENERGY: Good Penrose environment

📐 Tile 44:
   Center type: THIN
   Coordination: 2
   Angles: ['90.0°', '90.0°']
   Angle std: 0.0°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 0.00
   Coordination quality: 0.60
   🎯 FINAL CLASS: MEDIUM_ENERGY
   ⚠️  MEDIUM: Coordination pattern issues

📐 Tile 88:
   Center type: THICK
   Coordination: 4
   Angles: ['54.0°', '144.0°', '54.0°', '108.0°']
   Angle std: 38.2°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 0.50
   Coordination quality: 0.80
   🎯 FINAL CLASS: LOW_ENERGY
   ✅ LOW_ENERGY: Good Penrose environment




..................









📐 Tile 4224:
   Center type: THICK
   Coordination: 4
   Angles: ['72.0°', '54.0°', '126.0°', '108.0°']
   Angle std: 28.5°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 0.50
   Coordination quality: 0.80
   🎯 FINAL CLASS: LOW_ENERGY
   ✅ LOW_ENERGY: Good Penrose environment

📐 Tile 4268:
   Center type: THICK
   Coordination: 4
   Angles: ['36.0°', '108.0°', '108.0°', '108.0°']
   Angle std: 31.2°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 1.00
   Coordination quality: 0.80
   🎯 FINAL CLASS: LOW_ENERGY
   ✅ LOW_ENERGY: Good Penrose environment

📐 Tile 4312:
   Center type: THICK
   Coordination: 4
   Angles: ['144.0°', '54.0°', '108.0°', '54.0°']
   Angle std: 38.2°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 0.50
   Coordination quality: 0.80
   🎯 FINAL CLASS: LOW_ENERGY
   ✅ LOW_ENERGY: Good Penrose environment

📐 Tile 4356:
   Center type: THICK
   Coordination: 4
   Angles: ['36.0°', '108.0°', '108.0°', '108.0°']
   Angle std: 31.2°
   Geometric violations: {'invalid_coordination': False, 'severe_angular_strain': np.False_, 'impossible_configuration': False}
   Angular regularity: 1.00
   Coordination quality: 0.80
   🎯 FINAL CLASS: LOW_ENERGY
   ✅ LOW_ENERGY: Good Penrose environment
🔄 Synchronizing neighbor lists with adjacency graph...
✅ Synchronized 4406 tile neighbor lists
✅ Neighbor list synchronization validated
Tiling validation found 1 issues:
  - Found 12 tiles with only 1 neighbor
📊 FULL DISTRIBUTION (4406 tiles):
   LOW_ENERGY: 4313 (97.9%)
   MEDIUM_ENERGY: 70 (1.6%)
   HIGH_ENERGY: 23 (0.5%)



   randa@Randa:quasi-phason$ python scripts/run_week2.py
🧪 Testing Week 2 Implementation
========================================
📁 Loaded tiling: 4406 tiles
📊 Metadata: 4406 tiles, WidomInspiredQuasicrystalHamiltonian
✅ Components initialized

🔍 DEBUG: Checking flippable hexagons...
   Found 3690 flippable hexagons
   First cluster: [7, 8, 2596]
     Tile 7: THICK, flippable=True
     Tile 8: THICK, flippable=True
     Tile 2596: THIN, flippable=True

🔬 Testing Monte Carlo (T=0.3)...
   Initializing energy for all tiles...
   Step 0: E=307.85, Acceptance=100.0%, Δ=-0.000
   Step 20: E=307.85, Acceptance=100.0%, Δ=-0.000
   Step 40: E=307.85, Acceptance=100.0%, Δ=0.000
   Step 60: E=307.85, Acceptance=100.0%, Δ=-0.000
   Step 80: E=307.85, Acceptance=100.0%, Δ=0.000
✅ MC test: 100/100 accepted (100.0%)
   Energy: 307.85 → 307.85

🌱 Testing growth simulation...
🌱 Initializing growth seed...
✅ Growth seed: 249 tiles initialized
   Growth status: {'ungrown': 4157, 'frontier': 45, 'seed': 204}
🌿 Growth step 0...
✅ MC sweep: 0/100 accepted (0.0%)
✅ Growth step 1: added 48 tiles
✅ Growth test: added 48 tiles
   Total growth steps: 1

📊 Final validation:
   MC energy: 307.85
   Recomputed energy: 307.85
   Energy consistent: True

📁 Data files created in data/experiments:
   • final_state.json
   • growth_diagnostics.json
   • growth_initial.json
   • mc_diagnostics.json

⚠️  Issues detected:
   - Energy didn't decrease (check energy model)
   Success conditions: [True, True, False]
randa@Randa:quasi-phason$