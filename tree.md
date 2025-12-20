.
├── Makefile
├── README.md
├── __docs
│   ├── 0- Research Plan Refinement_ Quasicrystal Dynamics.md
│   ├── 1- tracker_prompt.md
│   ├── 2- tracker_week_1_implementation_core_foundatoin.md
│   ├── 2.2-tracker-may-be-usefull.md
│   ├── 3- to-use___comprehensive_implementation_of_milestone3.md
│   ├── 4- ref _______3rd-milestone_detailed_medium_plan.md
│   ├── 5- architecture____modular_medium_level_pipeline.md
│   ├── INFO_while_thinking.md
│   ├── archive-theoretical-foundation-----energy_landsacpe_refining_plan.md
│   ├── log.txt
│   ├── low_level_plan.txt
│   ├── organization_of_each_file.txt
│   ├── output.txt
│   ├── package_transfer.md
│   ├── tree.md
│   ├── ~~archive
│   │   ├── ADV-- phase 2+ --- important_physical behavior_to_tackle.md
│   │   ├── archive--- application_theory_indust.md
│   │   └── methodology-justification---about_obstacle_deterministic.md
│   └── ~~reference
├── __experiments
│   ├── phase1
│   │   ├── growth_dynamics
│   │   └── obstacle_healing
│   └── phase2
│       └── many_body_phasons
├── __notebooks
│   ├── 01_tiling_visualization.ipynb
│   ├── 02_phason_flip_analysis.ipynb
│   └── 03_healing_metrics.ipynb
├── __tests
│   ├── __init__.py
│   ├── test_metrics.py
│   ├── test_phason_flips.py
│   └── test_tilings.py
├── configs
│   ├── all_config_file.zip
│   ├── control_growth_only.toml
│   ├── phase1_baseline.toml
│   ├── phase2_growth_experiments.toml
│   ├── phase2_obstacles.toml
│   ├── phase2_phason_dynamics.toml
│   └── phase3_healing_dynamics.toml
├── data
│   ├── cache
│   ├── control_experiments
│   ├── control_tests
│   │   └── control_growth_only_20251215_233501.json
│   ├── data_extraction_command_head_tails.txt
│   ├── diagnostics
│   │   └── delta_E_distribution_proposed.png
│   ├── energy
│   │   ├── energy_model_parameters.json
│   │   ├── energy_validation_report.json
│   │   └── vertex_environment_statistics.json
│   ├── experiments
│   │   ├── energy_validation_report.json
│   │   ├── experment_data_also.zip
│   │   ├── final_state.json
│   │   ├── growth_diagnostics.json
│   │   ├── growth_initial.json
│   │   ├── head_growth_initial.md
│   │   ├── mc_diagnostics.json
│   │   ├── mc_test_T1.0.json
│   │   ├── mc_test_T1.5.json
│   │   ├── mc_test_T2.0.json
│   │   ├── mc_test_T3.0.json
│   │   ├── some_output.md
│   │   ├── tail_growth_initial.md
│   │   ├── temperature_sweep_raw.json
│   │   ├── temperature_sweep_results.json
│   │   └── temperature_sweep_summary.json
│   ├── growth_experiments
│   │   ├── data_growth_experiment.zip
│   │   ├── json_pores_0.0_20251214_193349.zip
│   │   ├── plots
│   │   │   ├── plot_pores_0.0_20251214_195846_analysis.zip
│   │   │   ├── pores_0.0_20251214_193208_analysis.png
│   │   │   ├── pores_0.0_20251214_193243_analysis.png
│   │   │   ├── pores_0.0_20251214_193349_analysis.png
│   │   │   ├── pores_0.0_20251214_194224_analysis.png
│   │   │   ├── pores_0.0_20251214_194244_analysis.png
│   │   │   └── pores_0.0_20251214_195846_analysis.png
│   │   ├── pores_0.0_20251214_193208.json
│   │   ├── pores_0.0_20251214_193243.json
│   │   ├── pores_0.0_20251214_193349.json
│   │   ├── pores_0.0_20251214_194224.json
│   │   ├── pores_0.0_20251214_194244.json
│   │   ├── pores_0.0_20251214_195846.json
│   │   ├── temp_sweep_T0.8.json
│   │   ├── temp_sweep_T1.0.json
│   │   ├── temp_sweep_T1.2.json
│   │   └── temp_sweep_T1.5.json
│   ├── obstacles
│   │   ├── archive
│   │   │   ├── experiment_summary.json
│   │   │   ├── fixed_defects
│   │   │   │   ├── fixed_defects_density_0.005.json
│   │   │   │   ├── fixed_defects_density_0.009.json
│   │   │   │   ├── fixed_defects_density_0.01.json
│   │   │   │   ├── fixed_defects_density_0.02.json
│   │   │   │   ├── fixed_defects_density_0.03.json
│   │   │   │   ├── fixed_defects_density_0.04.json
│   │   │   │   ├── fixed_defects_density_0.05.json
│   │   │   │   ├── fixed_defects_density_0.075.json
│   │   │   │   ├── fixed_defects_density_0.09.json
│   │   │   │   ├── fixed_defects_density_0.1.json
│   │   │   │   └── fixed_defects_density_0.2.json
│   │   │   ├── penrose_tiling.json
│   │   │   ├── penrose_tiling.png
│   │   │   ├── pores
│   │   │   │   ├── pores_density_0.005.json
│   │   │   │   ├── pores_density_0.009.json
│   │   │   │   ├── pores_density_0.01.json
│   │   │   │   ├── pores_density_0.02.json
│   │   │   │   ├── pores_density_0.03.json
│   │   │   │   ├── pores_density_0.04.json
│   │   │   │   ├── pores_density_0.05.json
│   │   │   │   ├── pores_density_0.075.json
│   │   │   │   ├── pores_density_0.09.json
│   │   │   │   ├── pores_density_0.1.json
│   │   │   │   └── pores_density_0.2.json
│   │   │   └── visualizations
│   │   │       ├── fixed_defects_density_0.005.png
│   │   │       ├── fixed_defects_density_0.01.png
│   │   │       ├── fixed_defects_density_0.02.png
│   │   │       ├── fixed_defects_density_0.03.png
│   │   │       ├── fixed_defects_density_0.05.png
│   │   │       ├── fixed_defects_density_0.1.png
│   │   │       ├── pores_density_0.005.png
│   │   │       ├── pores_density_0.01.png
│   │   │       ├── pores_density_0.02.png
│   │   │       ├── pores_density_0.03.png
│   │   │       ├── pores_density_0.05.png
│   │   │       └── pores_density_0.1.png
│   │   ├── experiment_summary.json
│   │   ├── fixed_defects
│   │   │   ├── fixed_defects_density_0.005.json
│   │   │   ├── fixed_defects_density_0.01.json
│   │   │   ├── fixed_defects_density_0.02.json
│   │   │   ├── fixed_defects_density_0.03.json
│   │   │   ├── fixed_defects_density_0.05.json
│   │   │   └── fixed_defects_density_0.1.json
│   │   ├── penrose_tiling.json
│   │   ├── penrose_tiling.png
│   │   ├── pores
│   │   │   ├── pores_density_0.005.json
│   │   │   ├── pores_density_0.01.json
│   │   │   ├── pores_density_0.02.json
│   │   │   ├── pores_density_0.03.json
│   │   │   ├── pores_density_0.05.json
│   │   │   └── pores_density_0.1.json
│   │   ├── verification_report.json
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
│   ├── processed
│   │   ├── head_tiles_process.md
│   │   ├── penrose_tiling_energy_initialized.json
│   │   └── tails_penrose_tiling_energy_initialized_process.md
│   └── raw
│       ├── New Text Document.txt
│       ├── head.json
│       ├── penrose_tiling.json
│       ├── penrose_tiling.png
│       ├── sub_results_of_penrose_tiling.json
│       └── tail.json
├── debug.md
├── environment.yml
├── output__first debug.md
├── output_debug_validation.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── __sequence_of_command_to_run.md
│   ├── a.py
│   ├── analyze_growth_results.py
│   ├── analyze_temperature_results.py
│   ├── check_vertex_class.py
│   ├── debug_energy_distribution.py
│   ├── debug_energy_model.py
│   ├── debug_validation.py
│   ├── diagnose_active_region_flips.py
│   ├── diagnose_energy_landscape.py
│   ├── diagnose_flip_physics.py
│   ├── diagnose_mc_healing.py
│   ├── diagnose_temperature_effect.py
│   ├── output.md
│   ├── quick_control.py
│   ├── quick_label_check.py
│   ├── run_growth_experiment.py
│   ├── run_milestone1.py
│   ├── run_milestone2_obstacle.py
│   ├── run_week2.py
│   ├── system_diagnostic.py
│   ├── temperature_sweep_physics.py
│   ├── test_correct_flip.py
│   ├── test_energy_sensitivity.py
│   ├── test_growth_baseline.py
│   ├── test_manual_defects.py
│   ├── test_mc_quick.py
│   ├── test_mc_temperature.py
│   ├── test_quick_growth.py
│   ├── test_temperature_effect.py
│   ├── test_temperature_summary.py
│   ├── validate_energy_consistency.py
│   ├── validate_robust_flip.py
│   ├── validate_week1_physics.py
│   ├── verify_label_persistence.py
│   └── verify_obstacles.py
├── src
│   ├── all_src_file.zip
│   ├── analysis
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
│   │   └── obstacle_visualizer.py
│   ├── simulation
│   │   ├── __pycache__
│   │   │   ├── flip_engine.cpython-312.pyc
│   │   │   ├── growth_engine.cpython-312.pyc
│   │   │   └── mc_engine.cpython-312.pyc
│   │   ├── flip_engine.py
│   │   ├── growth_engine.py
│   │   └── mc_engine.py
│   ├── tilings
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── penrose_p3.cpython-312.pyc
│   │   ├── penrose_p3.py
│   │   └── validation.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── config.cpython-312.pyc
│   │   │   └── io.cpython-312.pyc
│   │   ├── archive_obstacles.py
│   │   ├── config.py
│   │   ├── io.py
│   │   └── reproducibility.py
│   └── viz
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   └── plotters.cpython-312.pyc
│       ├── animations.py
│       ├── dashboards.py
│       └── plotters.py
├── test_mc_basics_output.md
└── tree.md

47 directories, 232 files
