.
├── Makefile
├── README.md
├── __docs
│   ├── 1st_and_2nd
│   │   .......
|   |   ..
|    |   ..
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
│   ├── obstacles
│   │   ├── archive
│   │   │   ├── experiment_summary.json
│   │   │   ├── fixed_defects
│   │   │   │   ├── fixed_defects_density_0.005.json
│   │   │   │   ├── ...
│   │   │   ├── penrose_tiling.json
│   │   │   ├── penrose_tiling.png
│   │   │   ├── pores
│   │   │   │   ├── pores_density_0.005.json
│   │   │   │   ├── ...
│   │   │   └── visualizations
│   │   │       ├── fixed_defects_density_0.005.png
│   │   │       ├── ...
│   │   ├── experiment_summary.json
│   │   ├── fixed_defects
│   │   │   ├── fixed_defects_density_0.005.json
│   │   │   ├── ...
│   │   ├── pores
│   │   │   ├── pores_density_0.005.json
│   │   │   ├── ...
│   │   ├── verification_report.json
│   │   └── visualizations
│   │       ├── fixed_defects_density_0.005.png
│   │       ├── ...
│   ├── processed
│   └── raw
│       ├── New Text Document.txt
│       ├── head.json
│       ├── penrose_tiling.json
│       ├── penrose_tiling.png
│       ├── sub_results_of_penrose_tiling.json
│       └── tail.json
├── environment.yml
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── debug_validation.py
│   ├── run_milestone1.py
│   ├── run_milestone2_obstacle.py
│   ├── validate_week1_physics.py
│   └── verify_obstacles.py
├── src
│   ├── analysis
│   ├── energy
│   │   ├── __pycache__
│   │   │   ├── combinatorial_classifier.cpython-312.pyc
│   │   │   └── widom_inspired_energy.cpython-312.pyc
│   │   ├── combinatorial_classifier.py
│   │   └── widom_inspired_energy.py
│   ├── growth
│   ├── monte_carlo
│   ├── obstacle
│   │   ├── __pycache__
│   │   │   ├── obstacle_config.cpython-312.pyc
│   │   │   ├── obstacle_creator.cpython-312.pyc
│   │   │   └── obstacle_visualizer.cpython-312.pyc
│   │   ├── fixed____current_obstalce_issue.md
│   │   ├── obstacle_config.py
│   │   ├── obstacle_creator.py
│   │   └── obstacle_visualizer.py
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
└── tree.md

45 directories, 155 files
