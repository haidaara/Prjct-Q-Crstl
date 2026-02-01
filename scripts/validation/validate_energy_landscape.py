# src/validation/validate_energy_landscape.py

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier

def validate_coordination_distribution(tiling_data):
    """
    Validate coordination numbers are physically reasonable
    Uses adjacency graph as primary source
    """
    print(" Validating Coordination Distribution...")
    
    adjacency_graph = tiling_data["adjacency_graph"]
    coord_counts = {}
    
    for tile_id_str, neighbors in adjacency_graph.items():
        coord = len(neighbors)
        coord_counts[coord] = coord_counts.get(coord, 0) + 1
    
    print("   Coordination distribution:", dict(sorted(coord_counts.items())))
    
    # Check for critical issues
    has_coord_0 = coord_counts.get(0, 0) > 0
    coord_1_count = coord_counts.get(1, 0)
    coord_1_percentage = coord_1_count / len(adjacency_graph) * 100
    
    # Expected for Penrose: mostly coordination 3-4, some 2 (boundary), rare 5+
    typical_coord_count = coord_counts.get(3, 0) + coord_counts.get(4, 0)
    typical_percentage = typical_coord_count / len(adjacency_graph) * 100
    
    print(f"   Tiles with 0 neighbors: {has_coord_0}")
    print(f"   Tiles with 1 neighbor: {coord_1_count} ({coord_1_percentage:.1f}%)")
    print(f"   Typical coordination (3-4): {typical_percentage:.1f}%")
    
    # Validation criteria
    coordination_valid = (
        not has_coord_0 and                    # No isolated tiles
        coord_1_percentage < 10.0 and          # Few single-neighbor tiles  
        typical_percentage > 70.0              # Mostly typical coordination
    )
    
    return coordination_valid, coord_counts


def validate_physics_fields(tiling_data):
    """Validate that physics fields are properly set in tiling data"""
    print(" Validating Physics Fields...")
    
    required_fields = ["vertex_class", "local_energy", "growth_status", "flippable"]
    missing_fields = []
    
    for tile in tiling_data["tiles"]:
        for field in required_fields:
            if field not in tile:
                missing_fields.append(field)
                break
    
    if missing_fields:
        print(f" Missing physics fields: {set(missing_fields)}")
        return False
    else:
        print(" All physics fields present")
        return True


def validate_vertex_classification(tiling_data):
    """Validate vertex classification distribution is realistic - PROCESS ALL TILES"""
    print(" Validating Vertex Classification...")
    
    classifier = CombinatorialVertexClassifier()
    
    # VALIDATION SHOULD PROCESS ALL TILES, NOT SAMPLE
    classifications = []
    for tile_id in range(len(tiling_data["tiles"])):  # PROCESS ALL TILES
        if tile_id < len(tiling_data["tiles"]):
            classification = classifier.classify_vertex_environment(tile_id, tiling_data)
            classifications.append(classification)
    
    # Check distribution is realistic 
    low_count = classifications.count("LOW_ENERGY")
    medium_count = classifications.count("MEDIUM_ENERGY") 
    high_count = classifications.count("HIGH_ENERGY")
    
    total = len(classifications)
    print(f" Classification distribution: {low_count}/{total} low, {medium_count}/{total} medium, {high_count}/{total} high")
    
    # Realistic distribution: should have mostly low/medium energy
    realistic = (low_count + medium_count) > total * 0.6
    return realistic


def validate_energy_model(tiling_data, energy_model):
    """
    Physics-first validation consistent  (surface tension + weighted surface term).
    Returns a dict with:
      - energy_ranges_physically_reasonable (bool)
      - field presence flags for EnergyLogger
      - surface_energy_consistent (bool)
      - max_expected_energy (float) computed from model params + observed missing bonds
    """
    print(" Validating Energy Model...")

    tiles = tiling_data["tiles"]
    active_tiles = [t for t in tiles if not t.get("removed", False) and t.get("obstacle_type") != "pore"]

    # --- Robust defaults (handles empty/edge cases) ---
    if not active_tiles:
        return {
            "energy_ranges_physically_reasonable": True,
            "min_energy_observed": 0.0,
            "max_energy_observed": 0.0,
            "max_expected_energy": 0.0,
            "out_of_range_tile_ids_preview": [],

            "surface_tension_active": False,
            "boundary_tiles_detected": 0,
            "energy_class_computed": False,
            "has_energy_class": False,
            "has_boundary_kind": False,
            "has_missing_bonds": False,
            "has_surface_energy": False,
            "surface_energy_consistent": True,
            "inconsistent_surface_tile_ids_preview": [],
            "sample_energies": {},
        }

    p = energy_model.params

    # --- activation (physics meaning: surface contributes to local_energy) ---
    stpb = float(getattr(p, "surface_tension_per_bond", 0.0))
    mrw  = float(getattr(p, "matching_rule_weight", 1.0))
    ccw  = float(getattr(p, "continuous_correction_weight", 0.0))

    surface_tension_active = (stpb > 0.0) and (mrw != 0.0)

    # --- Continuous bound (by model design; use getattr so it's forward-compatible) ---
    neighbor_strength = float(getattr(p, "neighbor_interaction_strength", 0.0))
    strain_penalty    = float(getattr(p, "geometric_strain_penalty", 0.0))
    phason_penalty    = float(getattr(p, "phason_strain_penalty", 0.0))
    continuous_max = ccw * (neighbor_strength + strain_penalty + phason_penalty)

    # --- Surface contribution bound uses *weighted* term (because local_energy includes mrw * surface_energy) ---
    max_missing = max(int(t.get("missing_bonds", 0)) for t in active_tiles) if surface_tension_active else 0
    max_expected = float(getattr(p, "high_energy_penalty", 0.0)) + continuous_max + (mrw * stpb * max_missing)

    # --- Observed energies (from stored fields; requires full-field attachment upstream) ---
    energies = [float(t.get("local_energy", 0.0)) for t in active_tiles]
    min_obs, max_obs = float(min(energies)), float(max(energies))

    tol = 1e-9
    out_of_range = [
        int(t.get("id", -1)) for t in active_tiles
        if (float(t.get("local_energy", 0.0)) < -tol) or (float(t.get("local_energy", 0.0)) > max_expected + tol)
    ]
    energy_ranges_ok = (len(out_of_range) == 0)

    # --- field presence (what EnergyLogger expects to report) ---
    has_energy_class  = all("energy_class"  in t for t in active_tiles)
    has_boundary_kind = all("boundary_kind" in t for t in active_tiles)
    has_missing_bonds = all("missing_bonds" in t for t in active_tiles)
    has_surface_energy = all("surface_energy" in t for t in active_tiles)

    boundary_tiles_detected = sum(1 for t in active_tiles if int(t.get("missing_bonds", 0)) > 0)

    # --- Surface energy self-consistency (unweighted surface_energy should be mb * stpb) ---
    inconsistent_surface = []
    surface_energy_consistent = True
    if surface_tension_active and (has_missing_bonds and has_surface_energy):
        for t in active_tiles:
            mb = int(t.get("missing_bonds", 0))
            se = float(t.get("surface_energy", 0.0))
            expected_se = mb * stpb
            if abs(se - expected_se) > 1e-6:
                inconsistent_surface.append(int(t.get("id", -1)))
                if len(inconsistent_surface) >= 10:
                    break
        surface_energy_consistent = (len(inconsistent_surface) == 0)
    elif surface_tension_active:
        surface_energy_consistent = False  # active but fields missing => inconsistent

    # --- Samples for human sanity-check (no recompute) ---
    sample_ids = [0, 100, 500, 1000]
    sample_ids = [i for i in sample_ids if i < len(tiles)]
    sample_energies = {}
    for tid in sample_ids:
        t = tiles[tid]
        sample_energies[tid] = {
            "vertex_class": t.get("vertex_class", None),
            "energy_class": t.get("energy_class", None),
            "local_energy": float(t.get("local_energy", 0.0)),
            "missing_bonds": int(t.get("missing_bonds", 0)),
            "boundary_kind": t.get("boundary_kind", None),
        }
        print(f"  Tile {tid}: v={sample_energies[tid]['vertex_class']}  "
              f"e={sample_energies[tid]['local_energy']:.2f}  "
              f"mb={sample_energies[tid]['missing_bonds']}  "
              f"kind={sample_energies[tid]['boundary_kind']}")

    print(f" Observed energy: min={min_obs:.3f}, max={max_obs:.3f}")
    print(f" Expected max (Option-A aware): {max_expected:.3f}")
    print(f" Energy range OK: {energy_ranges_ok}  (out_of_range={len(out_of_range)})")
    if surface_tension_active:
        print(f" Surface energy consistent: {surface_energy_consistent}")

    return {
        "energy_ranges_physically_reasonable": energy_ranges_ok,
        "min_energy_observed": min_obs,
        "max_energy_observed": max_obs,
        "max_expected_energy": max_expected,
        "out_of_range_tile_ids_preview": out_of_range[:20],

        # payload expected by EnergyLogger.log_energy_validation_report()
        "surface_tension_active": surface_tension_active,
        "boundary_tiles_detected": boundary_tiles_detected,
        "energy_class_computed": surface_tension_active and has_energy_class,
        "has_energy_class": has_energy_class,
        "has_boundary_kind": has_boundary_kind,
        "has_missing_bonds": has_missing_bonds,
        "has_surface_energy": has_surface_energy,
        "surface_energy_consistent": surface_energy_consistent,
        "inconsistent_surface_tile_ids_preview": inconsistent_surface,

        "sample_energies": sample_energies,
    }
