# 02_CODE_INDEX.md — Deep API & Repo Map

This file is auto-derivable from the repo. It lists **every module**, with **classes/methods/functions**, constants, and best-effort dictionary key usage.

## Tag index (semantic anchors)
- [#DEV-TOOLS]: 3 modules
- [#ENERGY-CALC]: 3 modules
- [#ENTRYPOINTS]: 8 modules
- [#FLIP-ENGINE]: 1 modules
- [#GROWTH]: 1 modules
- [#MC-HEALING]: 1 modules
- [#OBSTACLES]: 3 modules
- [#TILINGS-CORE]: 1 modules
- [#UTILS]: 4 modules
- [#VALIDATION]: 5 modules
- [#VIZ]: 8 modules

---

# [#DEV-TOOLS]

[#DEV-TOOLS]
## MODULE: `dev_tools/debug_flip_geometry.py`
PURPOSE: Flip geometry + energy delta smoke test.

### FUNCTIONS
- `main(trials: int=20) -> int`
- `region_energy(energy_model, tiling_data, region)`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['tiles']
- writes: ['flippable']
- validates: []
[/#DEV-TOOLS]

[#DEV-TOOLS]
## MODULE: `dev_tools/diagnose_active_region_flips.py`
PURPOSE: Diagnostic: flippable hexagons in active region vs globally.

### FUNCTIONS
- `main(seed_radius: float=10.0) -> int`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['id', 'tiles']
- writes: ['flippable']
- validates: []
[/#DEV-TOOLS]

[#DEV-TOOLS]
## MODULE: `dev_tools/system_diagnostic.py`
PURPOSE: System diagnostic (non-fatal).

### CONSTANTS
- `REQUIRED_PATHS` = `['data/processed/penrose_tiling_energy_initialized.json', 'configs/phase1_baseline.toml']`

### FUNCTIONS
- `main() -> int`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#DEV-TOOLS]

# [#ENERGY-CALC]

[#ENERGY-CALC]
## MODULE: `src/energy/combinatorial_classifier.py`
PURPOSE: Physically accurate vertex classification for Penrose tilings

### CLASSES
- **`CombinatorialVertexClassifier`**: Classifies vertex environments using physically meaningful criteria
  - `__init__(self, angle_tolerance: float=15.0)`
  - `_analyze_coordination_pattern(self, environment: VertexEnvironment) -> Dict` — Analyze coordination pattern with physically meaningful metrics
  - `_analyze_vertex_environment(self, tile_id: int, tiling_data: Dict) -> VertexEnvironment` — Comprehensive physical analysis using adjacency graph
  - `_assess_coordination_quality(self, environment: VertexEnvironment) -> float` — Assess quality with realistic boundary handling
  - `_check_geometric_constraints(self, environment: VertexEnvironment) -> Dict[str, bool]`
  - `_check_impossible_configuration(self, environment: VertexEnvironment) -> bool` — Check for configurations that violate basic Penrose constraints
  - `_compute_neighbor_vectors(self, center_tile: Dict, neighbors: List[Dict], tiling_data: Dict) -> List[np.ndarray]` — Compute vectors from center to each neighbor
  - `_compute_relative_angles(self, vectors: List[np.ndarray]) -> List[float]` — Compute angles between consecutive neighbor vectors in sorted order
  - `_get_immediate_neighbors(self, tile_id: int, tiling_data: Dict) -> List[Dict]` — FIXED: Uses adjacency graph as primary source for correct coordination
  - `_sort_neighbors_by_angle(self, vectors: List[np.ndarray], neighbors: List[Dict]) -> Tuple[List[np.ndarray], List[Dict]]` — Sort neighbors by polar angle for proper geometric analysis
  - `_synthesize_energy_classification(self, environment: VertexEnvironment, geometric_violations: Dict, coordination_analysis: Dict) -> str` — Realistic classification thresholds
  - `classify_vertex_environment(self, tile_id: int, tiling_data: Dict) -> str` — Main classification method - uses adjacency graph for correct coordination
  - `clear_cache(self)` — Clear any internal caches
- **`VertexEnvironment`**: Complete physical description of vertex local environment

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'angular_regularity', 'center', 'coordination_quality', 'tiles', 'type']
- writes: ['angular_regularity', 'severe_angular_strain']
- validates: []
[/#ENERGY-CALC]

[#ENERGY-CALC]
## MODULE: `src/energy/energy_logger.py`
PURPOSE: Research-grade energy landscape logging - ENHANCED VERSION

### CLASSES
- **`EnergyLogger`**: Logs energy landscape concepts for research reproducibility
  - `__init__(self, base_data_dir: str='data')`
  - `_assess_coordination_quality(self, coordination_numbers: List[int]) -> Dict[str, Any]` — Assess the quality of coordination number distribution
  - `_calculate_energy_statistics(self, energies: List[float]) -> Dict[str, float]` — Calculate comprehensive energy statistics
  - `_calculate_kurtosis(self, data: List[float]) -> float` — Calculate kurtosis of energy distribution
  - `_calculate_skewness(self, data: List[float]) -> float` — Calculate skewness of energy distribution
  - `_get_coordination_from_adjacency(self, tiling_data: Dict) -> List[int]` — Get coordination numbers from adjacency graph - FIXED KEY HANDLING
  - `_save_json(self, relative_path: str, data: Dict) -> str` — Save JSON with directory creation, return filepath
  - `_validate_coordination_data(self, coordination_numbers: List[int]) -> bool` — Validate coordination numbers are physically plausible
  - `log_energy_parameters(self, energy_model) -> str` — Log the fundamental energy model parameters
  - `log_energy_validation_report(self, validation_results: Dict, computation_time: float) -> str` — Log validation and performance metrics for energy calculations
  - `log_vertex_environment_statistics(self, tiling_data: Dict) -> str` — Log comprehensive vertex environment and energy statistics
  - `save_energy_initialized_tiling(self, tiling_data: Dict) -> str` — Save tiling with energy landscape initialized for simulation phases

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'id', 'tiles']
- writes: []
- validates: []
[/#ENERGY-CALC]

[#ENERGY-CALC]
## MODULE: `src/energy/widom_inspired_energy.py`
PURPOSE: Widom-inspired energy model for Penrose tilings with LIMITED continuous corrections

### CLASSES
- **`EnergyParameters`**: Physical parameters for Widom-inspired energy model
- **`WidomInspiredEnergy`**: Energy model inspired by Widom's quasicrystal Hamiltonian concept
  - `__init__(self, parameters: Optional[EnergyParameters]=None)`
  - `_compute_continuous_geometric_strain(self, tile_id: int, tiling_data: Dict) -> float` — Compute LIMITED energy from local geometric strain
  - `_compute_continuous_neighbor_interaction(self, tile_id: int, tiling_data: Dict) -> float` — Compute LIMITED energy from interactions with neighboring tiles
  - `_compute_phason_strain_energy(self, tile_id: int, tiling_data: Dict) -> float` — PHASON STRAIN ENERGY - CURRENTLY DISABLED
  - `_get_cached_vertex_class(self, tile_id: int, tiling_data: Dict) -> str` — OPTIMIZED: Get vertex class with caching
  - `clear_cache(self)`
  - `compute_local_energy(self, tile_id: int, tiling_data: Dict) -> float` — Compute local energy with LIMITED continuous corrections
  - `compute_total_energy(self, tiling_data: Dict) -> float` — Compute total energy of the tiling with caching optimization
  - `from_config(cls, config_manager: ConfigManager) -> 'WidomInspiredEnergy'` — Create energy model from ConfigManager instance
  - `update_tiling_energy(self, tiling_data: Dict) -> Dict` — Update energy fields for all tiles in tiling data

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['id', 'tiles']
- writes: ['local_energy', 'vertex_class']
- validates: []
[/#ENERGY-CALC]

# [#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/01_generate_tiling.py`
PURPOSE: (no module docstring)

### FUNCTIONS
- `main()`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_computed', 'metadata', 'thick_count', 'thin_count', 'tile_count', 'window_size']
- writes: []
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/01_prepare_processed_tiling.py`
PURPOSE: Energy Landscape Validation Script - FIXED VERSION

### FUNCTIONS
- `main()` — Run complete energy landscape validation and logging
- `validate_coordination_distribution(tiling_data)` — FIXED: Validate coordination numbers are physically reasonable
- `validate_energy_model(tiling_data, energy_model)` — Validate energy model produces physically reasonable results
- `validate_physics_fields(tiling_data)` — Validate that physics fields are properly set in tiling data
- `validate_vertex_classification(tiling_data)` — Validate vertex classification distribution is realistic - PROCESS ALL TILES

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'monte_carlo_ready', 'simulation_readiness', 'tiles', 'tiling_json', 'vertex_class']
- writes: []
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/02_generate_obstacles.py`
PURPOSE: 🚀 MILESTONE 2A: HIGH-PERFORMANCE OBSTACLE CREATION PIPELINE

### FUNCTIONS
- `create_obstacle_configurations(obstacle_creator, visualizer, base_tiling, obstacle_specs, output_dir)` — Create all obstacle configurations efficiently
- `load_base_tiling()` — Load canonical tiling for obstacle generation.
- `main()`
- `save_experiment_summary(results, output_dir, start_time)` — Save comprehensive experiment summary
- `save_obstacle_config(obstacle_tiling, spec_name, output_dir)` — Save obstacle configuration to appropriate subdirectory
- `setup_output_directory()` — Create organized output directory structure - FIXED PATH

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'metadata', 'obstacle_metadata', 'tile_count']
- writes: ['adjacency_graph']
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/03_run_healing_test.py`
PURPOSE: Experiment 03: Run Healing Test

### FUNCTIONS
- `_make_logger(verbosity: int)`
- `_next_run_id(out_dir: Path, prefix: str) -> int`
- `create_defects_strictly(tiling_data, energy_model, flip_engine, num_defects=10, log=None)`
- `run_experiment()`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'id', 'tiles']
- writes: ['adjacency_graph', 'flippable']
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/04_run_growth.py`
PURPOSE: Run config-driven growth experiments with obstacle healing

### CONSTANTS
- `PROJECT_ROOT` = `Path(__file__).resolve().parents[2]`

### FUNCTIONS
- `density_token(d: float) -> str`
- `find_obstacle_file(obstacle_type: str, density: float) -> Path` — Find obstacle file with flexible naming
- `load_config(config_path: str='configs/phase2_experiments.toml') -> dict` — Load experiment configuration from TOML
- `next_run_id(folder: Path) -> int`
- `overwrite_latest(run_file: Path, latest_path: Path) -> None`
- `run_growth_experiment(config: dict, experiment_name: str=None)` — Run a single growth experiment
- `short_path(p) -> str`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['acceptance_rate', 'active_type', 'defect_density', 'growth_steps', 'obstacles', 'series', 'test_densities', 'tiles']
- writes: ['_meta_config_path', 'defect_count', 'defect_density', 'metrics', 'trace_every', 'verbosity']
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/05_temperature_sweep.py`
PURPOSE: (no module docstring)

### CONSTANTS
- `PROJECT_ROOT` = `Path(__file__).resolve().parents[2]`

### FUNCTIONS
- `load_config(config_path: str) -> dict`
- `load_growth_runner()`
- `main() -> int`
- `next_run_id(folder: Path) -> int`
- `overwrite_latest(run_file: Path, latest_path: Path) -> None`
- `run_temperature_sweep(config: dict, cli_verbosity=None) -> dict`
- `short_path(p) -> str`
- `temp_token(T: float) -> str`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['debug', 'defects_end', 'defects_start', 'file', 'final_energy', 'mean_acceptance_rate', 'monte_carlo', 'project']
- writes: ['_meta_config_path', 'healed', 'healing_efficiency', 'output_dir', 'progress_every', 'temperature', 'trace_every', 'verbosity']
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/06_run_phase2_batch.py`
PURPOSE: 🚀 MILESTONE 2B: BATCH SIMULATION RUNNER (FIXED & ROBUST)

### FUNCTIONS
- `clean_path(p: Path) -> str`
- `import_numbered_script(path_from_root, module_name)`
- `main()`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['meta', 'project', 'tiling']
- writes: ['defects_end', 'density', 'duration', 'file', 'final_energy', 'input_tiling', 'meta', 'project', 'tiling']
- validates: []
[/#ENTRYPOINTS]

[#ENTRYPOINTS]
## MODULE: `experiments/__init__.py`
PURPOSE: (no module docstring)

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#ENTRYPOINTS]

# [#FLIP-ENGINE]

[#FLIP-ENGINE]
## MODULE: `src/simulation/flip_engine.py`
PURPOSE: Penrose phason flip engine with robust physical constraints

### CLASSES
- **`FlipEngine`**:
  - `__init__(self, vertex_classifier, energy_model, verbose=False)`
  - `_build_edge_maps(self, tids, data)`
  - `_compute_new_interior(self, target_verts, L)`
  - `_determine_tile_type(self, verts)`
  - `_distance(self, v1, v2)`
  - `_find_best_permutation(self, old, new)`
  - `_find_interior_vertex(self, edges, L, eps)`
  - `_get_k_ring_neighborhood(self, tile_ids: List[int], tiling_data: Dict, k: int=3) -> Set[int]` — Get tiles within k steps
  - `_get_tolerance(self, scale=1.0)`
  - `_get_two_ring_neighborhood(self, tile_ids: List[int], tiling_data: Dict) -> Set[int]`
  - `_normalize_edge(self, v1, v2)`
  - `_order_vertices_clockwise(self, verts)`
  - `_rebuild_adjacency_global(self, tiling_data: Dict) -> None` — PHYSICS FIX: Global Adjacency Rebuild (Rigorous).
  - `_recompute_energy_for_region(self, tile_ids: Set[int], tiling_data: Dict)` — Recompute energy for affected region, invalidating caches for 4-ring
  - `_trace_boundary_cycle(self, edges)`
  - `_update_adjacency_from_edges(self, cids, aff, e2t, data)`
  - `_update_edge_maps_after_flip(self, cids, t2e, e2t, data)`
  - `_verify_hexagon_structure(self, cluster, tiling_data, edge_to_tiles)`
  - `_verify_rhombus(self, verts, L, eps_len, eps_cross)`
  - `apply_flip(self, cluster_ids: List[int], tiling_data: Dict) -> bool` — Apply phason flip
  - `capture_state(self, tile_ids, tiling_data)` — Capture state for undo.
  - `compute_edge_length(self, tiling_data: Dict) -> float` — Compute Penrose edge length from tiling data
  - `find_flippable_hexagons(self, tiling_data: Dict) -> List[List[int]]` — Find flippable hexagons using EDGE-BASED detection
  - `restore_state(self, undo_info, tiling_data)` — Restore state from undo

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'center', 'tile_states', 'tiles', 'type', 'vertices']
- writes: ['adjacency_graph', 'center', 'id', 'neighbors', 'type', 'vertices']
- validates: []
[/#FLIP-ENGINE]

# [#GROWTH]

[#GROWTH]
## MODULE: `src/simulation/growth_engine.py`
PURPOSE: Growth simulator with working constraints and config-driven parameters

### CLASSES
- **`GrowthSimulator`**: Simulator for growth front propagation with healing
  - `__init__(self, mc_engine, config: Optional[Dict]=None)`
  - `_add_growth_layer(self, tiling_data: Dict, obstacles: Dict) -> List[int]` — Add new growth layer around current frontier
  - `_apply_growth_constraints(self, tiling_data: Dict)` — CRITICAL FIX: Actually constrain flips by modifying tile["flippable"]
  - `_can_grow_into(self, tile: Dict, obstacles: Dict) -> bool` — Check if growth can proceed into this tile
  - `_find_tiles_in_radius(self, center: List[float], radius: float, tiling_data: Dict) -> List[Dict]` — Find tiles within radius of center point
  - `_get_frontier_tiles(self, tiling_data: Dict) -> List[Dict]` — Get current frontier tiles
  - `_get_neighbors(self, tile_id: int, tiling_data: Dict) -> List[Dict]` — FIXED: Get neighbors using adjacency graph directly
  - `_remove_constraints(self, tiling_data: Dict)` — Restore original flippable state, except for immobile/pore tiles
  - `_update_frontier(self, tiling_data: Dict)` — Update growth frontier
  - `get_diagnostics(self) -> Dict[str, Any]` — Return growth diagnostics
  - `grow_step(self, tiling_data: Dict, obstacles: Dict) -> Tuple[Dict, List[int], Dict]` — Single growth step with healing - returns MC stats
  - `initialize_seed(self, tiling_data: Dict, seed_center: Optional[List[float]]=None) -> Dict` — Initialize growth from seed region with configurable center

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['_flippable_backup', 'adjacency_graph', 'center', 'growth_status', 'id', 'tiles']
- writes: ['_flippable_backup', 'flippable', 'growth_status']
- validates: []
[/#GROWTH]

# [#MC-HEALING]

[#MC-HEALING]
## MODULE: `src/simulation/mc_engine.py`
PURPOSE: Monte Carlo engine with proper energy consistency verification

### CLASSES
- **`MonteCarloEngine`**: Monte Carlo engine that preserves detailed balance with verified energy consistency
  - `__init__(self, temperature: float=0.3, energy_model=None, flip_engine=None, config: Optional[Dict]=None)`
  - `_compute_region_energy_fresh(self, tile_ids, tiling_data, extra_ring: int=1, return_map: bool=False)` — Compute total energy of region with fresh computation.
  - `_metropolis_accept(self, delta_energy: float) -> bool`
  - `_verify_energy_consistency(self, tiling_data: Dict, message: str='') -> float` — Verify current_energy matches recomputed total energy
  - `_vprint(self, msg: str, level: int=1)`
  - `get_diagnostics(self) -> Dict[str, Any]`
  - `initialize_energy(self, tiling_data: Dict) -> None` — Compute initial total energy with fresh computation
  - `run_debug_validation(self, tiling_data: Dict, steps: int=200) -> Dict` — Run MC with full verification for debugging
  - `run_step(self, tiling_data: Dict, debug_mode: bool=False) -> Tuple[bool, float]` — Single MC step with verified energy consistency
  - `run_sweep(self, tiling_data: Dict, steps: Optional[int]=None, debug_mode: bool=False) -> Dict` — Run multiple MC steps with verification

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['abs_de', 'class_after', 'class_before', 'computation_times', 'de', 'delta_energy_history', 'ea', 'eb', 'energy_drift_history', 'energy_history', 'flip_stats', 'immobile', 'max_drift', 'move', 'removed', 'tid', 'tiles', 'type_after', 'type_before']
- writes: ['accepted', 'energy_drift_history', 'proposed', 'rejected']
- validates: []
[/#MC-HEALING]

# [#OBSTACLES]

[#OBSTACLES]
## MODULE: `src/obstacle/obstacle_config.py`
PURPOSE: Efficient obstacle configuration generation for systematic studies.

### CLASSES
- **`ObstacleConfig`**: High-performance obstacle configuration generator
  - `__init__(self, config: ConfigManager)`
  - `_generate_grid_positions(self, n_obstacles: int, window_size: List[float], origin: List[float]) -> List[Tuple[float, float]]` — Simple deterministic grid-based placement
  - `_generate_positions_radius_aware(self, n_obstacles: int, window_size: List[float], origin: List[float], radii: List[float], min_separation: float, rng) -> List[Tuple[float, float]]` — Generate positions with edge-to-edge separation
  - `_generate_random_radii(self, n_obstacles: int, rng) -> List[float]` — Generate random radii with research-appropriate range
  - `generate_scalable_obstacles(self, tiling_data: Dict) -> Dict[str, ObstacleSpec]` — Generate obstacle specs for systematic density studies

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['metadata', 'tile_count', 'tiles', 'window_size']
- writes: []
- validates: []
[/#OBSTACLES]

[#OBSTACLES]
## MODULE: `src/obstacle/obstacle_creator.py`
PURPOSE: High-performance obstacle creation with spatial indexing for research scalability.

### CLASSES
- **`ObstacleCreator`**: High-performance obstacle creation with spatial indexing
  - `__init__(self, config: ConfigManager)`
  - `_build_spatial_index(self, tiling_data: Dict)` — Build KDTree for O(log n) tile lookups with normalized integer IDs
  - `_create_fixed_defects_optimized(self, tiling_data: Dict, spec: ObstacleSpec) -> Dict` — Deterministic fixed defect placement
  - `_create_pores_optimized(self, tiling_data: Dict, spec: ObstacleSpec) -> Dict` — Optimized pore creation using spatial queries
  - `_fast_deep_copy(self, data: Dict) -> Dict` — Optimized deep copy preserving integer keys
  - `_finalize_obstacle_data(self, tiling_data: Dict, spec: ObstacleSpec) -> Dict` — Add research metadata efficiently
  - `_update_adjacency_batch(self, tiling_data: Dict, removed_mask: np.ndarray)` — Batch update adjacency graph for optimal performance with proper blanking
  - `create_obstacles(self, tiling_data: Dict, obstacle_spec: ObstacleSpec) -> Dict` — Main entry point - create obstacles with optimal performance
- **`ObstacleSpec`**: Efficient obstacle specification for scalable studies

### FUNCTIONS
- `adjacency_intkeys_to_str(adjacency_dict: Dict) -> Dict[str, List[int]]` — Convert adjacency graph integer keys to strings for JSON export

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'center', 'id', 'neighbors', 'tiles']
- writes: ['flippable', 'immobile', 'local_energy', 'neighbors', 'obstacle_metadata', 'obstacle_type', 'removed', 'vertex_class']
- validates: []
[/#OBSTACLES]

[#OBSTACLES]
## MODULE: `src/obstacle/obstacle_visualizer.py`
PURPOSE: High-performance obstacle visualization for research analysis.

### CLASSES
- **`ObstacleVisualizer`**: Research-grade obstacle visualization
  - `__init__(self, config: ConfigManager)`
  - `_format_obstacle_plot(self, ax, tiling_data: Dict, obstacle_meta: Dict)` — Research-grade plot formatting
  - `_get_figsize(self)` — Get optimized figure size
  - `_plot_obstacles(self, ax, tiling_data: Dict)` — Plot obstacle regions with proper styling and clipping
  - `_plot_tile_collection(self, ax, tiles, tile_type)` — Optimized tile plotting
  - `plot_obstacles(self, tiling_data: Dict, save_path: str=None)` — Create publication-quality obstacle visualization

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['positions', 'radii', 'tiles', 'type', 'vertices']
- writes: []
- validates: []
[/#OBSTACLES]

# [#TILINGS-CORE]

[#TILINGS-CORE]
## MODULE: `src/tilings/penrose_p3.py`
PURPOSE: Research-grade Penrose P3 tiling generator - FIXED VERSION

### CLASSES
- **`PenroseTiling`**: Research-grade Penrose P3 tiling generator using cut-and-project method.
  - `__init__(self, config: ConfigManager)`
  - `_build_edge_mapping(self, cell)` — Build mapping from edges to tiles for adjacency detection
  - `_build_tiles_with_adjacency(self, cell)` — Build tiles and compute adjacency graph
  - `_find_neighbors(self, tile_index: int, vertices: list)` — Find all neighbors for a given tile
  - `_get_metadata(self) -> dict` — Get generation metadata for reproducibility
  - `_get_midpoint(self, rhombus)` — Extract midpoint coordinates - FIXED API
  - `_get_vertex_coordinates(self, rhombus)` — Extract vertex coordinates from Rhombus - FIXED API
  - `_normalize_edge(self, v1: tuple, v2: tuple) -> tuple` — Create canonical edge representation for hashing
  - `_synchronize_neighbor_lists(self)` — CRITICAL FIX: Ensure tile neighbor lists match adjacency graph
  - `_validate_synchronization(self)` — Validate that neighbor lists match adjacency graph
  - `_validate_tiling(self)` — Run consistency checks on the generated tiling
  - `generate(self) -> dict` — Generate the complete tiling with adjacency information.

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['neighbors', 'type', 'vertices']
- writes: ['neighbors']
- validates: []
[/#TILINGS-CORE]

# [#UTILS]

[#UTILS]
## MODULE: `src/utils/archive_obstacles.py`
PURPOSE: Simple obstacle archiving utility - run this before milestone2 to clean data

### FUNCTIONS
- `main()` — Archive existing obstacle data to prevent mixing

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#UTILS]

[#UTILS]
## MODULE: `src/utils/config.py`
PURPOSE: (no module docstring)

### CLASSES
- **`ConfigManager`**: Central configuration management for reproducible research
  - `__init__(self, config_path: str='configs/phase2_experiments.toml')`
  - `_load_config(self) -> Dict[str, Any]` — Load and merge configuration with includes
  - `analysis(self) -> Dict[str, Any]` — Access analysis configuration section
  - `energy(self) -> Dict[str, Any]` — Access energy configuration section
  - `exports(self) -> Dict[str, Any]`
  - `growth(self) -> Dict[str, Any]` — Access growth configuration section
  - `monte_carlo(self) -> Dict[str, Any]` — Access Monte Carlo configuration section
  - `obstacles(self) -> Dict[str, Any]`
  - `tiling(self) -> Dict[str, Any]`
  - `visualization(self) -> Dict[str, Any]`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#UTILS]

[#UTILS]
## MODULE: `src/utils/energy_utils.py`
PURPOSE: Utilities for consistent energy computation and cache management

### FUNCTIONS
- `clear_all_caches(energy_model) -> None`
- `compute_total_energy_fresh(energy_model, tiling_data: Dict) -> float` — Compute total energy with guaranteed fresh computation
- `get_k_ring_neighborhood(tile_ids: List[int], tiling_data: Dict, k: int=3) -> Set[int]` — Get k-ring neighborhood using BFS
- `verify_energy_convention(energy_model, tiling_data: Dict) -> Dict` — Verify energy counting convention and return which one is correct
- `wipe_all_energy_fields(tiling_data: Dict) -> None` — Remove all stored energy fields to force fresh computation

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['adjacency_graph', 'tiles']
- writes: ['convention', 'status']
- validates: []
[/#UTILS]

[#UTILS]
## MODULE: `src/utils/script_utils.py`
PURPOSE: (no module docstring)

### CONSTANTS
- `ROOT_DIR` = `Path(__file__).parent.parent.parent`

### FUNCTIONS
- `initialize_seed_region(tiling_data: Dict, seed_center: Optional[list]=None, seed_radius: float=10.0, set_flippable: bool=True) -> None` — Standard seed initialization.
- `load_tiling(path: str='data/processed/penrose_tiling_energy_initialized.json') -> Dict` — Robust loader that checks multiple paths
- `setup_simulation_components(config_path: str='configs/phase2_experiments.toml', verbose: bool=False)` — Factory for engines - Returns FRESH instances every time

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['center', 'tiles']
- writes: ['flippable', 'growth_status']
- validates: []
[/#UTILS]

# [#VALIDATION]

[#VALIDATION]
## MODULE: `validation/run_all.py`
PURPOSE: MASTER VALIDATION RUNNER (GO/NO-GO).

### FUNCTIONS
- `main() -> None`
- `run_script(script_name: str) -> bool`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#VALIDATION]

[#VALIDATION]
## MODULE: `validation/validate_energy.py`
PURPOSE: VALIDATION 3: ENERGY & PHYSICS ENGINE (Phase 1)

### FUNCTIONS
- `check_convention(tiling_data) -> bool`
- `check_determinism(tiling_data) -> bool`
- `check_mc_drift(tiling_data, steps: int=100) -> bool`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#VALIDATION]

[#VALIDATION]
## MODULE: `validation/validate_obstacles.py`
PURPOSE: VALIDATION 2: OBSTACLES (Milestone 2)

### FUNCTIONS
- `check_obstacles() -> bool`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#VALIDATION]

[#VALIDATION]
## MODULE: `validation/validate_tiling.py`
PURPOSE: VALIDATION 1: TILING STRUCTURE (Milestone 1)

### FUNCTIONS
- `_to_int(x)`
- `check_structure(ignore_removed_in_symmetry: bool=True) -> bool`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['id', 'tiles']
- writes: []
- validates: []
[/#VALIDATION]

[#VALIDATION]
## MODULE: `validation/visualize_growth_fidelity.py`
PURPOSE: (no module docstring)

### FUNCTIONS
- `_render_collection(ax, polys, colors)`
- `get_tile_fingerprints(tiles)` — Creates a set of unique strings representing the center position of each tile.
- `plot_growth_forensics(tiling_data, output_path, input_tiling_path=None)` — Generates a 4-Panel Matrix Report.

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['vertices']
- writes: []
- validates: []
[/#VALIDATION]

# [#VIZ]

[#VIZ]
## MODULE: `analysis/__init__.py`
PURPOSE: (no module docstring)

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `analysis/analyze_growth_results.py`
PURPOSE: Analyze growth experiment outputs written by run_growth_experiment.py.

### CONSTANTS
- `PROJECT_ROOT` = `Path(__file__).resolve().parents[2]`

### FUNCTIONS
- `_safe_float(x, default=None) -> Optional[float]`
- `load_json(fp: Path) -> Dict[str, Any]`
- `main() -> int`
- `plot_series(steps: List[Dict[str, Any]], out_png: Path, title: str) -> None`
- `select_file(input_dir: Path, pattern: str, latest: bool) -> Optional[Path]`
- `write_csv(steps: List[Dict[str, Any]], out_csv: Path) -> None`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `analysis/analyze_temperature_results.py`
PURPOSE: Analyze temperature sweep experiment outputs written by growth / temperature sweep runners.

### CONSTANTS
- `PROJECT_ROOT` = `Path(__file__).resolve().parents[2]`

### FUNCTIONS
- `_get_nested(d: Dict[str, Any], path: List[str], default=None)`
- `_safe_float(x, default=None) -> Optional[float]`
- `load_results_files(input_dir: Path, pattern: str) -> List[Path]`
- `main() -> int`
- `parse_one_file(fp: Path) -> Dict[str, Any]`
- `plot_summary(rows: List[Dict[str, Any]], out_png: Path) -> None`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['acceptance_mean', 'defects_end', 'defects_start', 'file', 'heal_efficiency', 'temperature']
- writes: ['heal_efficiency', 'healed']
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `analysis/plot_energy_landscape.py`
PURPOSE: Plot / diagnose the energy landscape by sampling phason flips and measuring ΔE.

### CONSTANTS
- `PROJECT_ROOT` = `Path(__file__).resolve().parents[2]`

### FUNCTIONS
- `_region_energy(tiling: dict, region_ids: Sequence[int], energy_model) -> float`
- `_seed_only_filter(hexagons: List[List[int]], tiling: dict) -> List[List[int]]`
- `_set_all_flippable(tiling: dict) -> None`
- `_wipe_tile_fields(tiling: dict, tile_ids: Iterable[int]) -> None`
- `main() -> int`
- `measure_delta_e_for_hexagon(tiling: dict, hexagon: Sequence[int], flip_engine, energy_model, k: int=4) -> Optional[float]` — Returns ΔE (after - before) for this hexagon, or None if the flip could not be applied.
- `plot_histogram(deltas: List[float], out_png: Path, title: str) -> None`

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['tiles']
- writes: ['flippable']
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `analysis/visualize_state.py`
PURPOSE: VISUALIZATION DRIVER: 2x2 Physics Matrix

### FUNCTIONS
- `clean_path(p: Path) -> str`
- `find_latest_experiment(search_dir: Path) -> Path`
- `get_config_format() -> str` — Reads plot_format from phase2_experiments.toml (The Contract).
- `main()`

### DATA_KEYS_USED (best-effort static extraction)
- reads: []
- writes: []
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `src/viz/plotters.py`
PURPOSE: (no module docstring)

### CLASSES
- **`TilingVisualizer`**: Research-grade visualization for Penrose tilings
  - `__init__(self, config: ConfigManager)`
  - `_format_plot(self, ax, tile_count: int, thick_count: int, thin_count: int)` — Format the plot with research standards
  - `plot_tiling(self, tiling_data: dict, save_path: str=None)` — Create publication-quality tiling visualization

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['center', 'id', 'tiles', 'type', 'vertices']
- writes: []
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `src/viz/static_plots.py`
PURPOSE: (no module docstring)

### FUNCTIONS
- `_add_legend(ax, items: List[tuple], loc='upper right', title='Legend', font_size=10)`
- `_generate_subtitle(data: Dict[str, Any]) -> str`
- `_load_publication_config() -> Dict[str, Any]` — Loads aesthetics from configs/publication_plots.toml.
- `plot_physics_matrix(tiling_data: Dict[str, Any], save_path: Optional[str]=None)` — Generates the 2x2 Diagnostic Matrix.

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['tiles', 'type', 'vertices']
- writes: []
- validates: []
[/#VIZ]

[#VIZ]
## MODULE: `src/viz/utils.py`
PURPOSE: (no module docstring)

### FUNCTIONS
- `extract_physics_fields(tiling_data: Dict[str, Any]) -> Tuple[Dict[int, float], Dict[int, str]]` — Safely extracts energy and class fields with type sanitation.
- `extract_topology(tiling_data: Dict[str, Any]) -> Optional[Dict[int, List[int]]]` — Extracts adjacency graph with STRICT integer typing.
- `get_growth_mask(tiling_data: Dict[str, Any]) -> Dict[int, str]`
- `get_obstacle_mask(tiling_data: Dict[str, Any]) -> Dict[int, str]` — Identify tiles that are obstacles.
- `load_tiling_state(file_path: Union[str, Path]) -> Dict[str, Any]` — Robustly load a tiling state JSON.

### DATA_KEYS_USED (best-effort static extraction)
- reads: ['tiles']
- writes: []
- validates: ['tiles']
[/#VIZ]

