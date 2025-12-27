# src/viz/utils.py
import json
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List, Union

def load_tiling_state(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Robustly load a tiling state JSON.
    Raises strict error if file is a 'Summary' (metrics only, no tiles).
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if "tiles" not in data:
        raise ValueError(f"Input file '{path.name}' appears to be a Summary (no 'tiles' field). "
                         "Please provide a State file (*_final.json or snapshot).")
    
    return data

def extract_topology(tiling_data: Dict[str, Any]) -> Optional[Dict[int, List[int]]]:
    """
    Extracts adjacency graph with STRICT integer typing.
    Fixes silent failure where string keys "123" caused 0-neighbor lookups.
    """
    raw_adj = tiling_data.get("adjacency_graph")
    
    if not raw_adj:
        return None
        
    normalized_adj = {}
    for k, v in raw_adj.items():
        try:
            # Force keys and values to int
            key_int = int(k)
            # Filter None and ensure list of ints
            val_list = [int(n) for n in v if n is not None]
            normalized_adj[key_int] = val_list
        except (ValueError, TypeError):
            continue
            
    return normalized_adj

# src/viz/utils.py

def extract_physics_fields(tiling_data: Dict[str, Any]) -> Tuple[Dict[int, float], Dict[int, str]]:
    """
    Extract energy and classification maps.
    Refined: Prefers 'energy_class' (Physics) over 'vertex_class' (Geometry) for visualization.
    """
    energy_map = {}
    class_map = {}
    
    for i, tile in enumerate(tiling_data["tiles"]):
        # Robust ID extraction
        tid = int(tile.get("id", i))
        
        # 1. Extract Energy
        try:
            val = tile.get("local_energy", 0.0)
            energy_map[tid] = float(val)
        except (ValueError, TypeError):
            energy_map[tid] = 0.0
            
        # 2. Extract Class (Prefer Energy Class for Viz)
        # # This makes the "Red Corona" visible in Panel 3
        if "energy_class" in tile:
            cls = tile["energy_class"]
        #revert to this if no energy class
        # else:
        #     cls = tile.get("vertex_class", "UNKNOWN")

        # uncomment: to show geometric class instead of energy class
        #  Healing/order parameter must be geometric
        #cls = tile.get("vertex_class", tile.get("energy_class", "UNKNOWN"))

            
        class_map[tid] = str(cls)
            
    return energy_map, class_map

def get_growth_mask(tiling_data: Dict[str, Any]) -> Dict[int, str]:
    status_map = {}
    for i, tile in enumerate(tiling_data["tiles"]):
        tid = int(tile.get("id", i))
        status_map[tid] = tile.get("growth_status", "ungrown")
    return status_map

def get_obstacle_mask(tiling_data: Dict[str, Any]) -> Dict[int, str]:
    """
    Identify tiles that are obstacles.
    Fixes silent failure: Catches 'fixed_defect' and 'immobile' explicitly.
    """
    obs_map = {}
    for i, tile in enumerate(tiling_data["tiles"]):
        tid = int(tile.get("id", i))
        
        # 1. Check for Pore
        if tile.get("removed", False) or tile.get("obstacle_type") == "pore":
            obs_map[tid] = "pore"
            continue
            
        # 2. Check for Fixed Defect (Strict Check)
        obs_type = tile.get("obstacle_type", "")
        if (obs_type == "fixed_defect") or (obs_type == "fixed") or tile.get("immobile", False):
            obs_map[tid] = "fixed"
        else:
            obs_map[tid] = None
            
    return obs_map
