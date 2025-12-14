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
│   ├── phase1_baseline.toml
│   ├── phase2_obstacles.toml
│   ├── phase2_phason_dynamics.toml
│   └── phase3_healing_dynamics.toml
├── data
│   ├── cache
│   ├── energy
│   │   ├── energy_model_parameters.json
│   │   ├── energy_validation_report.json
│   │   └── vertex_environment_statistics.json
│   ├── obstacles
│   │   ├── archive
│   │   │   ├── experiment_summary.json
│   │   │   ├── fixed_defects
│   │   │   ├── penrose_tiling.json
│   │   │   ├── penrose_tiling.png
│   │   │   ├── pores
│   │   │   └── visualizations
│   │   ├── experiment_summary.json
│   │   ├── fixed_defects
│   │   │   ├── fixed_defects_density_0.005.json
│   │   │   ├................
│   │   ├── penrose_tiling.json
│   │   ├── penrose_tiling.png
│   │   ├── pores
│   │   │   ├── pores_density_0.005.json
│   │   │   ├── ....
│   │   ├── verification_report.json
│   │   └── visualizations
│   │       ├── fixed_defects_density_0.005.png
                    ..............
│   │  
│   │      
│   ├── processed
│   │   ├── head_adjacency_graph.md
│   │   ├── head_tiles_process.md
│   │   ├── head_tiles_processed.md
│   │   ├── penrose_tiling_energy_initialized.json
│   │   ├── tail_tiles_process.md
│   │   └── tails_tiles_process.md
│   └── raw
│       ├── New Text Document.txt
│       ├── head.json
│       ├── penrose_tiling.json
│       ├── penrose_tiling.png
│       ├── sub_results_of_penrose_tiling.json
│       └── tail.json
├── environment.yml
├── output_debug_validation.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── __sequence_of_command_to_run.md
│   ├── debug_validation.py
│   ├── run_milestone1.py
│   ├── run_milestone2_obstacle.py
│   ├── run_week2.py
│   ├── validate_week1_physics.py
│   └── verify_obstacles.py
├── src
│   ├── analysis
│   ├── archive
│   │   ├── analysis
│   │   ├── energy
│   │   │   ├── __pycache__
│   │   │   ├── combinatorial_classifier.py
│   │   │   ├── energy_logger.py
│   │   │   └── widom_inspired_energy.py
│   │   ├── growth
│   │   ├── monte_carlo
│   │   ├── obstacle
│   │   │   ├── __pycache__
│   │   │   ├── fixed____current_obstalce_issue.md
│   │   │   ├── obstacle_config.py
│   │   │   ├── obstacle_creator.py
│   │   │   └── obstacle_visualizer.py
│   │   ├── tilings
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── penrose_p3.py
│   │   │   └── validation.py
│   │   ├── utils
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── archive_obstacles.py
│   │   │   ├── config.py
│   │   │   ├── io.py
│   │   │   └── reproducibility.py
│   │   └── viz
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       ├── animations.py
│   │       ├── dashboards.py
│   │       └── plotters.py
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
├── tree.md
└── tree_src.md

55 directories, 147 files
