# src/utils/energy_utils.py
"""
Utilities for consistent energy computation and cache management
"""

import numpy as np
from typing import Dict, List, Set

def wipe_all_energy_fields(tiling_data: Dict) -> None:
    """Remove all stored energy fields to force fresh computation"""
    for tile in tiling_data["tiles"]:
        tile.pop("local_energy", None)
        tile.pop("vertex_class", None)

def clear_all_caches(energy_model) -> None:
    # 1) model method
    if hasattr(energy_model, "clear_cache"):
        energy_model.clear_cache()

    # 2) common known caches
    for name in ["_vertex_class_cache", "_local_energy_cache", "_energy_cache"]:
        if hasattr(energy_model, name):
            obj = getattr(energy_model, name)
            if hasattr(obj, "clear"):
                obj.clear()

    # 3) classifier caches (if attached)
    if hasattr(energy_model, "classifier"):
        classifier = energy_model.classifier
        for name in ["_cache", "_vertex_cache", "_class_cache"]:
            if hasattr(classifier, name):
                obj = getattr(classifier, name)
                if hasattr(obj, "clear"):
                    obj.clear()

    # 4) last-resort: clear any attribute ending with "cache" that is a dict
    for attr in dir(energy_model):
        if attr.lower().endswith("cache"):
            try:
                obj = getattr(energy_model, attr)
                if isinstance(obj, dict):
                    obj.clear()
            except Exception:
                pass


def get_k_ring_neighborhood(tile_ids: List[int], tiling_data: Dict, k: int = 3) -> Set[int]:
    """
    Get k-ring neighborhood using BFS
    Returns set of tile IDs within k steps of input tiles
    """
    neighborhood = set(tile_ids)
    frontier = set(tile_ids)
    
    for _ in range(k):
        new_frontier = set()
        for tile_id in frontier:
            neighbors = tiling_data["adjacency_graph"].get(str(tile_id), [])
            for n in neighbors:
                nid = int(n) if isinstance(n, str) else n
                if nid not in neighborhood:
                    new_frontier.add(nid)
        neighborhood.update(new_frontier)
        frontier = new_frontier
    
    return neighborhood

def compute_total_energy_fresh(energy_model, tiling_data: Dict) -> float:
    """
    Compute total energy with guaranteed fresh computation
    (no reliance on stored fields)
    """
    wipe_all_energy_fields(tiling_data)
    clear_all_caches(energy_model)
    return energy_model.compute_total_energy(tiling_data)

# src/utils/energy_utils.py - FIXED verify_energy_convention
def verify_energy_convention(energy_model, tiling_data: Dict) -> Dict:
    """
    Verify energy counting convention and return which one is correct
    FIXED: Proper wiping to avoid contamination
    """
    # Compute total energy fresh
    wipe_all_energy_fields(tiling_data)
    clear_all_caches(energy_model)
    total_energy = energy_model.compute_total_energy(tiling_data)
    
    # WIPE AGAIN - total_energy may have populated fields
    wipe_all_energy_fields(tiling_data)
    clear_all_caches(energy_model)
    
    # Compute sum of local energies fresh
    sum_local = 0
    for tile_id, tile in enumerate(tiling_data["tiles"]):
        if not tile.get("removed", False):
            # Compute fresh each time
            sum_local += energy_model.compute_local_energy(tile_id, tiling_data)
    
    # Check both conventions
    diff_sum = abs(total_energy - sum_local)
    diff_half_sum = abs(total_energy - 0.5 * sum_local)
    
    result = {
        'total_energy': total_energy,
        'sum_local': sum_local,
        'diff_sum': diff_sum,
        'diff_half_sum': diff_half_sum
    }
    
    if diff_sum < 1e-6:
        result['status'] = 'pass'
        result['convention'] = 'sum'
    elif diff_half_sum < 1e-6:
        result['status'] = 'pass'
        result['convention'] = 'half-sum'
    else:
        result['status'] = 'fail'
        result['convention'] = None
    
    return result