.
├── README.md
├── __docs
│   ├── 0- Research Plan Refinement_ Quasicrystal Dynamics.md
│   ├── 1- tracker_prompt.md
│   ├── 2- tracker_week_1_implementation_core_foundatoin.md
│   ├── 2.2-tracker-may-be-usefull.md
│   ├── 3- to-use___comprehensive_implementation_of_milestone3.md
│   ├── 3- tracker_phase_production.md
│   ├── 4- ref _______3rd-milestone_detailed_medium_plan.md
│   ├── 5- architecture____modular_medium_level_pipeline.md
│   ├── INFO_while_thinking.md
│   ├── archive-theoretical-foundation-----energy_landsacpe_refining_plan.md
│   ├── current_tracker.md
│   ├── discussion.md
│   ├── log.txt
│   ├── low_level_plan.txt
│   ├── organization_of_each_file.txt
│   ├── output.txt
│   ├── package_transfer.md
│   ├── tracker_to_update_based_on_it.md
│   ├── tree.md
│   ├── ~~archive
│   │   ├── ADV-- phase 2+ --- important_physical behavior_to_tackle.md
│   │   ├── archive--- application_theory_indust.md
│   │   └── methodology-justification---about_obstacle_deterministic.md
│   └── ~~reference
├── configs
│   ├── archive_configuration
│   │   ├── phase1_baseline.toml
│   │   ├── phase1_healing.toml
│   │   ├── phase2_growth_experiments.toml
│   │   └── phase2_obstacles.toml
│   ├── cheat-sheet_phase2.toml
│   ├── config.zip
│   ├── phase2_experiments.toml
│   └── publication_plots.toml
├── data
│   
│   ├── energy
│   │   ├── energy_model_parameters.json
│   │   ├── energy_validation_report.json
│   │   └── vertex_environment_statistics.json
│   ├── experiments
│   │   ├── growth
│   │   │   ├── growth_pores_d0p000_run_001
│   │   │   │   ├── growth_pores_d0p000_run_001_final.json
│   │   │   │   └── viz
│   │   │   │       └── growth_pores_d0p000_run_001_matrix.png
│   │   │   ├── growth_pores_d0p000_run_001.json
│   │   │   └── latest.json
│   │   └── healing
│   │       ├── healing_base_run_001
│   │       │   ├── healing_base_run_001.json
│   │       │   ├── healing_base_run_001_summary.json
│   │       │   ├── healing_damaged_state_1766734394.json
│   │       │   ├── healing_damaged_state_1766741636.json
│   │       │   ├── healing_damaged_state_1766751221.json
│   │       │   ├── healing_step_0050.json
│   │       │   ├── healing_step_0100.json
│   │       │   ├── healing_step_0150.json
│   │       │   ├── healing_step_0200.json
│   │       │   ├── healing_step_0250.json
│   │       │   ├── healing_step_0300.json
│   │       │   ├── healing_step_0350.json
│   │       │   ├── healing_step_0400.json
│   │       │   ├── healing_step_0459.json
│   │       │   ├── healing_step_0509.json
│   │       │   ├── healing_step_0559.json
│   │       │   ├── healing_step_0609.json
│   │       │   ├── healing_step_0659.json
│   │       │   ├── healing_step_0709.json
│   │       │   ├── healing_step_0759.json
│   │       │   ├── healing_step_0809.json
│   │       │   ├── healing_step_0858.json
│   │       │   ├── healing_step_0908.json
│   │       │   ├── healing_step_0958.json
│   │       │   ├── healing_step_1008.json
│   │       │   ├── healing_step_1058.json
│   │       │   ├── healing_step_1108.json
│   │       │   ├── healing_step_1158.json
│   │       │   ├── healing_step_1208.json
│   │       │   ├── healing_step_1258.json
│   │       │   ├── healing_step_1307.json
│   │       │   ├── healing_step_1357.json
│   │       │   ├── healing_step_1407.json
│   │       │   ├── healing_step_1457.json
│   │       │   ├── healing_step_1507.json
│   │       │   ├── healing_step_1557.json
│   │       │   ├── healing_step_1607.json
│   │       │   ├── healing_step_1657.json
│   │       │   ├── healing_step_1707.json
│   │       │   ├── healing_step_1756.json
│   │       │   ├── healing_step_1806.json
│   │       │   ├── healing_step_1856.json
│   │       │   ├── healing_step_1906.json
│   │       │   ├── healing_step_1956.json
│   │       │   ├── healing_step_2006.json
│   │       │   ├── healing_step_2056.json
│   │       │   ├── healing_step_2106.json
│   │       │   ├── healing_step_2154.json
│   │       │   ├── healing_step_2204.json
│   │       │   ├── healing_step_2254.json
│   │       │   ├── healing_step_2304.json
│   │       │   ├── healing_step_2354.json
│   │       │   ├── healing_step_2404.json
│   │       │   ├── healing_step_2454.json
│   │       │   ├── healing_step_2504.json
│   │       │   ├── healing_step_2554.json
│   │       │   ├── healing_step_2602.json
│   │       │   ├── healing_step_2652.json
│   │       │   ├── healing_step_2702.json
│   │       │   ├── healing_step_2752.json
│   │       │   ├── healing_step_2802.json
│   │       │   ├── healing_step_2852.json
│   │       │   ├── healing_step_2902.json
│   │       │   ├── healing_step_2952.json
│   │       │   ├── healing_step_3000.json
│   │       │   └── viz
│   │       │       └── healing_base_run_001_matrix.png
│
│   ├── obstacles
│   │   ├── experiment_summary.json
│   │   ├── fixed_defects
│   │   │   ├── fixed_defects_density_0.005.json
│   │   │   ├── fixed_defects_density_0.01.json
│   │   │   ├── fixed_defects_density_0.02.json
│   │   │   ├── fixed_defects_density_0.03.json
│   │   │   ├── fixed_defects_density_0.05.json
│   │   │   └── fixed_defects_density_0.1.json
│   │   ├── healing_base_run_001.json
│   │   ├── latest.json
│   │   ├── pores
│   │   │   ├── pores_density_0.005.json
│   │   │   ├── pores_density_0.01.json
│   │   │   ├── pores_density_0.02.json
│   │   │   ├── pores_density_0.03.json
│   │   │   ├── pores_density_0.05.json
│   │   │   └── pores_density_0.1.json
│   │   └── visualizations
│   │       ├── fixed_defects_density_0.005.png
│   │       ├── fixed_defects_density_0.01.png
│   │       ├── fixed_defects_density_0.02.png
│   │       ├── fixed_defects_density_0.03.png
│   │       ├── fixed_defects_density_0.05.png
│   │       ├── fixed_defects_density_0.1.png
│   │       ├── pores_density_0.005.png
│   │       ├── pores_density_0.01.png
│   │       ├── pores_density_0.02.png
│   │       ├── pores_density_0.03.png
│   │       ├── pores_density_0.05.png
│   │       └── pores_density_0.1.png
│   ├── output.experiments_1.md
│   ├── output_experiment2.md
│   ├── processed
│   │   └── penrose_tiling_energy_initialized.json
│   ├── raw
│   │   ├── penrose_tiling.json
│   │   └── penrose_tiling.png
│   └── visualizations
│       ├── growth
│       │   ├── growth_pores_d0.100_1766524526_final_matrix.png
│       │   └── growth_pores_d0p000_run_009_final_matrix.png
│       └── growth_forensics
│           ├── growth_pores_d0.010_1766521934_final_forensic.png
│           ├── growth_pores_d0.020_1766522508_final_forensic.png
│           ├── growth_pores_d0.030_1766523116_final_matrix.png
│           ├── growth_pores_d0.050_1766523810_final_matrix.png
│           ├── healing_damaged_state_1766657338_matrix.png
│           ├── healing_damaged_state_1766666860_matrix.png
│           ├── healing_damaged_state_1766667191_matrix.png
│           ├── healing_damaged_state_1766667420_matrix.png
│           ├── healing_damaged_state_1766667680_matrix.png
│           ├── healing_damaged_state_1766668603_matrix.png
│           ├── healing_damaged_state_1766671395_matrix.png
│           ├── healing_step_0050_matrix.png
│           ├── healing_step_0100_matrix.png
│           ├── healing_step_0150_matrix.png
│           ├── healing_step_0200_matrix.png
│           ├── healing_step_0250_matrix.png
│           ├── healing_step_0300_matrix.png
│           ├── healing_step_0350_matrix.png
│           ├── healing_step_0400_matrix.png
│           ├── healing_step_0450_matrix.png
│           ├── healing_step_0459_matrix.png
│           ├── healing_step_0500_matrix.png
│           ├── healing_step_0509_matrix.png
│           ├── healing_step_0550_matrix.png
│           ├── healing_step_0559_matrix.png
│           ├── healing_step_0600_matrix.png
│           ├── healing_step_0609_matrix.png
│           ├── healing_step_0650_matrix.png
│           ├── healing_step_0659_matrix.png
│           ├── healing_step_0700_matrix.png
│           ├── healing_step_0709_matrix.png
│           ├── healing_step_0750_matrix.png
│           ├── healing_step_0759_matrix.png
│           ├── healing_step_0800_matrix.png
│           ├── healing_step_0809_matrix.png
│           ├── healing_step_0850_matrix.png
│           ├── healing_step_0858_matrix.png
│           ├── healing_step_0900_matrix.png
│           ├── healing_step_0908_matrix.png
│           ├── healing_step_0950_matrix.png
│           ├── healing_step_0958_matrix.png
│           ├── healing_step_1000_matrix.png
│           ├── healing_step_1008_matrix.png
│           ├── healing_step_1050_matrix.png
│           ├── healing_step_1058_matrix.png
│           ├── healing_step_1100_matrix.png
│           ├── healing_step_1108_matrix.png
│           ├── healing_step_1150_matrix.png
│           ├── healing_step_1158_matrix.png
│           ├── healing_step_1200_matrix.png
│           ├── healing_step_1208_matrix.png
│           ├── healing_step_1250_matrix.png
│           ├── healing_step_1258_matrix.png
│           ├── healing_step_1300_matrix.png
│           ├── healing_step_1307_matrix.png
│           ├── healing_step_1350_matrix.png
│           ├── healing_step_1357_matrix.png
│           ├── healing_step_1400_matrix.png
│           ├── healing_step_1407_matrix.png
│           ├── healing_step_1450_matrix.png
│           ├── healing_step_1457_matrix.png
│           ├── healing_step_1500_matrix.png
│           ├── healing_step_1507_matrix.png
│           ├── healing_step_1550_matrix.png
│           ├── healing_step_1557_matrix.png
│           ├── healing_step_1600_matrix.png
│           ├── healing_step_1607_matrix.png
│           ├── healing_step_1650_matrix.png
│           ├── healing_step_1657_matrix.png
│           ├── healing_step_1700_matrix.png
│           ├── healing_step_1707_matrix.png
│           ├── healing_step_1750_matrix.png
│           ├── healing_step_1756_matrix.png
│           ├── healing_step_1800_matrix.png
│           ├── healing_step_1806_matrix.png
│           ├── healing_step_1850_matrix.png
│           ├── healing_step_1856_matrix.png
│           ├── healing_step_1900_matrix.png
│           ├── healing_step_1906_matrix.png
│           ├── healing_step_1950_matrix.png
│           ├── healing_step_1956_matrix.png
│           ├── healing_step_2000_matrix.png
│           ├── healing_step_2006_matrix.png
│           ├── healing_step_2050_matrix.png
│           ├── healing_step_2056_matrix.png
│           ├── healing_step_2100_matrix.png
│           ├── healing_step_2106_matrix.png
│           ├── healing_step_2150_matrix.png
│           ├── healing_step_2154_matrix.png
│           ├── healing_step_2200_matrix.png
│           ├── healing_step_2204_matrix.png
│           ├── healing_step_2250_matrix.png
│           ├── healing_step_2254_matrix.png
│           ├── healing_step_2300_matrix.png
│           ├── healing_step_2304_matrix.png
│           ├── healing_step_2350_matrix.png
│           ├── healing_step_2354_matrix.png
│           ├── healing_step_2400_matrix.png
│           ├── healing_step_2404_matrix.png
│           ├── healing_step_2450_matrix.png
│           ├── healing_step_2454_matrix.png
│           ├── healing_step_2500_matrix.png
│           ├── healing_step_2504_matrix.png
│           ├── healing_step_2550_matrix.png
│           ├── healing_step_2554_matrix.png
│           ├── healing_step_2600_matrix.png
│           ├── healing_step_2602_matrix.png
│           ├── healing_step_2650_matrix.png
│           ├── healing_step_2652_matrix.png
│           ├── healing_step_2700_matrix.png
│           ├── healing_step_2702_matrix.png
│           ├── healing_step_2750_matrix.png
│           ├── healing_step_2752_matrix.png
│           ├── healing_step_2800_matrix.png
│           ├── healing_step_2802_matrix.png
│           ├── healing_step_2850_matrix.png
│           ├── healing_step_2852_matrix.png
│           ├── healing_step_2900_matrix.png
│           ├── healing_step_2902_matrix.png
│           ├── healing_step_2950_matrix.png
│           ├── healing_step_2952_matrix.png
│           └── healing_step_3000_matrix.png
├── environment.yml
├── output.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── analysis
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── analyze_growth_results.py
│   │   ├── analyze_temperature_results.py
│   │   ├── plot_energy_landscape.py
│   │   └── visualize_state.py
│
│   ├── dev_tools
│   │   ├── debug_flip_geometry.py
│   │   ├── diagnose_active_region_flips.py
│   │   └── system_diagnostic.py
│   ├── experiments
│   │   ├── 01_generate_tiling.py
│   │   ├── 01_prepare_processed_tiling.py
│   │   ├── 02_generate_obstacles.py
│   │   ├── 03_run_healing_test.py
│   │   ├── 04_run_growth.py
│   │   ├── 05_temperature_sweep.py
│   │   ├── 06_run_phase2_batch.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── 04_run_growth.cpython-312.pyc
│   ├── scripts.zip
│   └── validation
│       ├── README.md
│       ├── __pycache__
│       │   └── visualize_growth_fidelity.cpython-312.pyc
│       ├── run_all.py
│       ├── validate_energy.py
│       ├── validate_obstacles.py
│       ├── validate_tiling.py
│       └── visualize_growth_fidelity.py
├── src
│   ├── energy
│   │   ├── __pycache__
│   │   │   ├── combinatorial_classifier.cpython-312.pyc
│   │   │   ├── energy_logger.cpython-312.pyc
│   │   │   └── widom_inspired_energy.cpython-312.pyc
│   │   ├── combinatorial_classifier.py
│   │   ├── energy_logger.py
│   │   └── widom_inspired_energy.py
│   ├── obstacle
│   │   ├── __pycache__
│   │   │   ├── obstacle_config.cpython-312.pyc
│   │   │   ├── obstacle_creator.cpython-312.pyc
│   │   │   └── obstacle_visualizer.cpython-312.pyc
│   │   ├── fixed____current_obstalce_issue.md
│   │   ├── obstacle_config.py
│   │   ├── obstacle_creator.py
│   │   ├── obstacle_visualizer.py
│   │   └── src.obstacle.zip
│   ├── simulation
│   │   ├── __pycache__
│   │   │   ├── flip_engine.cpython-312.pyc
│   │   │   ├── growth_engine.cpython-312.pyc
│   │   │   └── mc_engine.cpython-312.pyc
│   │   ├── flip_engine.py
│   │   ├── growth_engine.py
│   │   └── mc_engine.py
│   ├── tilings
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── penrose_p3.cpython-312.pyc
│   │   └── penrose_p3.py
│   ├── utils
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── config.cpython-312.pyc
│   │   │   ├── energy_utils.cpython-312.pyc
│   │   │   ├── io.cpython-312.pyc
│   │   │   └── script_utils.cpython-312.pyc
│   │   ├── archive_obstacles.py
│   │   ├── config.py
│   │   ├── energy_utils.py
│   │   └── script_utils.py
│   └── viz
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── plotters.cpython-312.pyc
│       │   ├── static_plots.cpython-312.pyc
│       │   └── utils.cpython-312.pyc
│       ├── plotters.py
│       ├── static_plots.py
│       └── utils.py
├── src.zip
└── tree.md

66 directories, 559 files
