# quick_defect_check.py
from src.utils.script_utils import setup_simulation_components, load_tiling
from scripts.experiments._003_run_healing_test import create_defects_strictly

# Load and create defects
tiling = load_tiling()
energy_model, flip_engine, mc_engine = setup_simulation_components()

# Create exactly 1 defect for debugging
defect_tiling = create_defects_strictly(tiling, energy_model, flip_engine, num_defects=1)

# Check energy before/after
E_before = energy_model.compute_total_energy(tiling)
E_after = energy_model.compute_total_energy(defect_tiling)
print(f"Energy change from 1 defect: {E_after - E_before}")

# Find flippable hexagons near defect
flippable = flip_engine.find_flippable_hexagons(defect_tiling)
print(f"Flippable hexagons in defective tiling: {len(flippable)}")