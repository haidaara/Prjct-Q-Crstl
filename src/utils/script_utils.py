# src/utils/script_utils.py
import json
import sys
import os
from pathlib import Path
from typing import Tuple, Dict, Any, Optional

# Ensure project root is in path
ROOT_DIR = Path(__file__).parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine
from src.utils.config import ConfigManager

def load_tiling(path: str = "data/processed/penrose_tiling_energy_initialized.json") -> Dict:
    """Robust loader that checks multiple paths"""
    file_path = Path(path)
    if not file_path.exists():
        file_path = ROOT_DIR / path
    if not file_path.exists():
        raise FileNotFoundError(f"Missing data file: {path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def setup_simulation_components(config_path: str = "configs/phase2_experiments.toml", verbose: bool = False):
    """Factory for engines - Returns FRESH instances every time"""
    config = ConfigManager(config_path)
    classifier = CombinatorialVertexClassifier()
    
    # Safe key filtering to avoid crashes on extra config fields
    valid_keys = EnergyParameters.__dataclass_fields__.keys()
    energy_config = {k: v for k, v in config.energy.items() if k in valid_keys}
    
    energy_params = EnergyParameters(**energy_config)
    energy_model = WidomInspiredEnergy(energy_params)
    flip_engine = FlipEngine(classifier, energy_model, verbose=verbose)
    return classifier, energy_model, flip_engine

def initialize_seed_region(tiling_data: Dict, seed_center: Optional[list] = None, 
                         seed_radius: float = 10.0, set_flippable: bool = True) -> None:
    """
    Standard seed initialization.
    set_flippable=True: Overwrites 'flippable' status.
    set_flippable=False: Only marks 'growth_status'.
    """
    if seed_center is None:
        window_size = tiling_data.get('window_size', [60.0, 60.0])
        seed_center = [window_size[0]/2, window_size[1]/2]
    
    for tile in tiling_data['tiles']:
        if tile.get('removed', False):
            continue
        dx = tile['center'][0] - seed_center[0]
        dy = tile['center'][1] - seed_center[1]
        
        if (dx*dx + dy*dy) <= seed_radius*seed_radius:
            tile['growth_status'] = 'seed'
            if set_flippable: tile['flippable'] = True
        else:
            tile['growth_status'] = 'ungrown'
            if set_flippable: tile['flippable'] = False