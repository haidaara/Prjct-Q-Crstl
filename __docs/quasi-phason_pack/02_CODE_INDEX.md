# Code Index (Hot Map)

This is a **curated** index: only the entrypoints and core modules you edit most.
For full, auto-generated listings, keep them outside the context pack.

## Entrypoint scripts
### Experiments
- `scripts/experiments/01_generate_tiling.py` — generate raw Penrose P3 tiling
- `scripts/experiments/01_prepare_processed_tiling.py` — stage-01 energy landscape init + validation + logging
- `scripts/experiments/02_generate_obstacles.py` — apply pores/fixed defects
- `scripts/experiments/03_run_healing_test.py` — damage + anneal healing
- `scripts/experiments/04_run_growth.py` — growth simulation
- `scripts/experiments/05_temperature_sweep.py` — temperature sweep
- `scripts/experiments/06_run_phase2_batch.py` — batch runner

### Validation
- `scripts/validation/validate_energy_landscape.py` — stage-01 validator (Option-A aware)
- `scripts/validation/validate_tiling.py` — structural sanity (adjacency / neighbors)
- `scripts/validation/validate_obstacles.py` — obstacle masks & invariants

### Analysis / Viz
- `scripts/analysis/visualize_state.py` — visualize a state JSON
- `scripts/analysis/plot_energy_landscape.py` — energy landscape plots

## Core library modules (src)
### Tiling
- `src/tilings/penrose_p3.py` → `PenroseTiling.generate()`

### Energy
- `src/energy/widom_inspired_energy.py` → `WidomInspiredEnergy.update_tiling_energy()` + `compute_total_energy()`
- `src/energy/combinatorial_classifier.py` → vertex class mapping
- `src/energy/energy_logger.py` → writes stage-01 JSON reports

### Simulation
- `src/simulation/flip_engine.py` → legal flips + apply flip mutation
- `src/simulation/mc_engine.py` → MC driver (delta-E, acceptance, verify_energy)
- `src/simulation/growth_engine.py` → growth rules

### Obstacles
- `src/obstacle/obstacle_creator.py` → apply pores/fixed defects

### Viz
- `src/viz/utils.py` → robust loaders + adjacency normalization + masks
- `src/viz/static_plots.py` → publication plots driven by `configs/publication_plots.toml`
- `src/viz/plotters.py` → quick tiling plotter

### Utilities
- `src/utils/config.py` → `ConfigManager`
- `src/utils/energy_utils.py` → wipe/verify helpers for consistent energy computations
- `src/utils/script_utils.py` → shared script helpers

## “Where do I change X?”
- Energy physics (surface / strain / thresholds): `src/energy/widom_inspired_energy.py`
- Vertex class rules: `src/energy/combinatorial_classifier.py`
- Energy logging schema: `src/energy/energy_logger.py`
- MC acceptance / delta-E / verification: `src/simulation/mc_engine.py`
- Flip legality: `src/simulation/flip_engine.py`
- Why a plot looks “different”: `src/viz/utils.py` (which field the panel reads)
