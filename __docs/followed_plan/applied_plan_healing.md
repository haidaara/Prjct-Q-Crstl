# **DETAILED HEALING ARCHITECTURE - FUNCTION-LEVEL SPECIFICATION**

## **1. HEALING ENGINE - ORCHESTRATION LAYER**

### **Function: prepare_healing_region(tiling, center, R_core, R_buffer)**
**Purpose:** Apply healing-specific constraints to raw tiling

**Logic Flow:**
1. **Input:** Raw tiling + parameters (center, R_core, R_buffer)
2. **Deep copy** tiling (preserve original)
3. **Mark regions:**
   - Core: distance(tile_center, center) ≤ R_core
   - Buffer: R_core < distance ≤ R_buffer
   - Frozen: distance > R_buffer
4. **Enforce constraints:**
   - Convert all `"ungrown"` → `"frozen"` (healing ≠ growth)
   - Set `flippable=True` only for tiles in Buffer
   - Ensure `immobile=True` tiles never become `flippable`
   - Mark region flags: `tile["region"] = "core"/"buffer"/"frozen"`
5. **Return:** Prepared tiling with region metadata

**Contracts:**
- NEVER modifies original tiling
- ALWAYS respects existing `immobile=True`
- ALWAYS converts `ungrown` for healing semantics

### **Function: compute_baseline_signature(tiling)**
**Purpose:** Create reference signature for convergence validation

**Logic Flow:**
1. **Input:** Prepared healing tiling (from prepare_healing_region)
2. **Refresh energy:** Call `energy_model.update_tiling_energy(tiling)`
3. **Compute signature:**
   - Core metrics:
     - `defect_count = defect_policy.count_defects(tiling, region="core")`
     - `energy_density = sum(local_energy in core) / core_area`
     - `vertex_distribution = histogram(vertex_class in core)`
   - Buffer metrics:
     - `energy_density_buffer = ...`
   - Global metrics:
     - `total_energy`
     - `boundary_stats = histogram(boundary_kind)`
4. **Output:** Dictionary with all signature metrics

### **Function: create_controlled_defects(tiling, target_defects)**
**Purpose:** Create exact number of defects in core region

**Logic Flow:**
1. **Input:** Prepared tiling + target defect count
2. **Current defects = defect_policy.count_defects(tiling, "core")**
3. **While |current_defects - target_defects| > 0:**
   a. **Select candidate flip:** Random hexagon in buffer where ALL tiles are:
      - In buffer region
      - Not `immobile=True`
      - Not `removed=True`
      - Not `obstacle_type="pore"`
   
   b. **Apply flip tentatively:** Use `flip_engine.force_flip()` (ignore energy)
   
   c. **Refresh energy:** Update affected region
   
   d. **New defects = defect_policy.count_defects(tiling, "core")**
   
   e. **Decision logic:**
      - If moving TOWARD target (abs(new-target) < abs(current-target)): **Keep**
      - Else: **Revert** (store previous state or re-apply inverse)
   
   f. **Update current_defects**
   
4. **Verification:** Ensure final defect count == target (± tolerance)
5. **Return:** Modified tiling with exact defect count

**Contracts:**
- ALWAYS maintain exact defect count within tolerance
- NEVER flip tiles outside buffer
- ALWAYS respect immobile constraints
- ALWAYS refresh energy before counting defects

### **Function: anneal_with_constraints(tiling, temperature_schedule)**
**Purpose:** Run annealing while enforcing all constraints

**Logic Flow:**
1. **Input:** Prepared tiling + schedule [(T, steps), ...]
2. **For each (temperature, n_steps) in schedule:**
   a. **Set MC temperature:** `mc_engine.temperature = temperature`
   
   b. **Run MC steps:**
      - For step in range(n_steps):
        1. **Select flip candidate:** Only hexagons where ALL tiles in buffer
        2. **Check immobile:** Reject if any tile `immobile=True`
        3. **Compute ΔE:** Using `energy_model.compute_energy_change()`
        4. **Metropolis acceptance:** Existing logic
        5. **If accepted:** Apply flip, update local energy
      
      - **Every N steps (checkpoint):**
        1. **Refresh energy** (full buffer region)
        2. **Record metrics:** Call `metrics_tracker.record()`
        3. **Early stopping check:** If defects stable for K checkpoints
   
   c. **End temperature stage:** Record final metrics for this T
   
3. **Return:** Annealed tiling + metrics history

**Contracts:**
- ALWAYS respect buffer boundary
- ALWAYS reject flips with immobile tiles
- REGULAR energy refresh (every checkpoint)
- NO flips outside buffer region

## **2. DEFECT ANALYZER - POLICY LAYER**

### **Class: RegionPolicy**
**Purpose:** Define region membership and eligibility

**Attributes:**
- `center`, `R_core`, `R_buffer` (immutable after creation)
- `core_mask`, `buffer_mask`, `frozen_mask` (boolean arrays)

**Methods:**
1. **is_in_core(tile_id):** Check if tile in core region
2. **is_in_buffer(tile_id):** Check if tile in buffer (includes core)
3. **get_region(tile_id):** Return "core"/"buffer"/"frozen"
4. **get_buffer_tiles():** Return list of tile IDs in buffer region

**Contracts:**
- Core ⊂ Buffer (strict hierarchy)
- Frozen = everything outside buffer

### **Class: DefectPolicy**
**Purpose:** Centralized defect definition

**Configuration:**
```python
DEFECT_CRITERION = "physics"  # Options: "geometry" or "physics"
# "geometry": vertex_class == "HIGH_ENERGY"
# "physics": energy_class == "HIGH_ENERGY"
```

**Methods:**
1. **is_eligible_for_defect_counting(tile):**
   **Logic:**
   - MUST be in core region
   - MUST be active (not removed, not pore)
   - MUST NOT be immobile
   - MUST be bulk: `boundary_kind == "bulk"` AND `is_boundary == False`
   - Return: True if all conditions met

2. **is_defect(tile):**
   **Logic:**
   - If not eligible: return False
   - If DEFECT_CRITERION == "geometry": return tile["vertex_class"] == "HIGH_ENERGY"
   - If DEFECT_CRITERION == "physics": return tile["energy_class"] == "HIGH_ENERGY"

3. **count_defects(tiling, region="core"):**
   **Logic:**
   - Initialize count = 0
   - For each tile in specified region:
     - If is_eligible_for_defect_counting(tile) AND is_defect(tile):
       - count += 1
   - Return count

**Contracts:**
- Single source of truth for defect definition
- Consistent eligibility criteria across all calls
- Defect criterion fixed per experiment

### **Function: compute_signature(tiling, region_policy)**
**Purpose:** Compute observable signature for comparison

**Logic Flow:**
1. **Input:** Tiling with fresh energy fields + region_policy
2. **Compute per region (core, buffer, global):**
   - Defect count (using DefectPolicy)
   - Energy metrics:
     - `total_energy = sum(local_energy)`
     - `energy_density = total_energy / area`
     - `energy_histogram = distribution of local_energy values`
   - Vertex distribution:
     - `vertex_counts = Counter(vertex_class)`
     - `vertex_percentages = normalize(vertex_counts)`
   - Boundary statistics:
     - `boundary_counts = Counter(boundary_kind)`
     - `is_boundary_count = sum(is_boundary)`
3. **Output:**
```python
signature = {
    "core": {defects, energy_density, vertex_dist, ...},
    "buffer": {energy_density, ...},
    "global": {total_energy, boundary_stats, ...},
    "timestamp": ...,
    "region_params": {"R_core": ..., "R_buffer": ...}
}
```

## **3. METRICS TRACKER - TELEMETRY LAYER**

### **Function: initialize_tracker(baseline_signature)**
**Purpose:** Setup tracking with baseline reference

**Logic:**
1. Store baseline signature
2. Initialize empty history list
3. Set convergence thresholds:
   - `ENERGY_TOLERANCE = 0.01` (1% of baseline)
   - `DEFECT_TOLERANCE = 0` (exact for defects)
   - `DISTRIBUTION_TOLERANCE = 0.05` (5% difference)

### **Function: record_checkpoint(step, temperature, tiling, region_policy)**
**Purpose:** Record snapshot of current state

**Logic Flow:**
1. **Input:** Current state (step, T, tiling)
2. **REFRESH ENERGY FIRST:** Call `energy_model.update_tiling_energy(tiling)`
3. **Compute current signature:** Use `compute_signature(tiling, region_policy)`
4. **Compute distances from baseline:**
   - `defect_distance = current_core_defects - baseline_core_defects`
   - `energy_distance = (current_energy_density - baseline_energy_density) / baseline_energy_density`
   - `distribution_distance = KL_divergence(current_vertex_dist, baseline_vertex_dist)`
5. **Record:**
```python
checkpoint = {
    "step": step,
    "temperature": temperature,
    "signature": current_signature,
    "distances": {
        "defects": defect_distance,
        "energy": energy_distance,
        "distribution": distribution_distance
    },
    "acceptance_rate": mc_engine.get_acceptance_rate(),
    "flip_count": mc_engine.get_flip_count()
}
history.append(checkpoint)
```

### **Function: compute_convergence_metrics()**
**Purpose:** Analyze healing progression

**Logic:**
1. **Healing efficiency:**
   ```
   initial_defects = history[0]["signature"]["core"]["defects"]
   final_defects = history[-1]["signature"]["core"]["defects"]
   efficiency = (initial_defects - final_defects) / initial_defects
   ```

2. **Energy recovery:**
   ```
   initial_energy = history[0]["signature"]["global"]["total_energy"]
   final_energy = history[-1]["signature"]["global"]["total_energy"]
   baseline_energy = baseline_signature["global"]["total_energy"]
   recovery = 1 - abs(final_energy - baseline_energy) / abs(initial_energy - baseline_energy)
   ```

3. **Convergence detection:**
   - Check last K checkpoints for stability
   - Defects stable within tolerance
   - Energy changing less than threshold per step

4. **Return:** Comprehensive metrics dictionary

## **4. VALIDATION LOGIC**

### **Function: validate_convergence(final_tiling, baseline_signature)**
**Purpose:** Determine if healing succeeded

**Logic Flow:**
1. **Refresh energy** on final tiling
2. **Compute final signature**
3. **Check each criterion:**

   **Criterion 1: Defects healed**
   ```
   if final_core_defects > baseline_core_defects + DEFECT_TOLERANCE:
       return False, "Defects not healed"
   ```

   **Criterion 2: Energy recovered**
   ```
   energy_diff = abs(final_energy_density - baseline_energy_density) / baseline_energy_density
   if energy_diff > ENERGY_TOLERANCE:
       return False, f"Energy not recovered: diff={energy_diff:.2%}"
   ```

   **Criterion 3: Distribution matches**
   ```
   dist_diff = compute_distribution_distance(final_vertex_dist, baseline_vertex_dist)
   if dist_diff > DISTRIBUTION_TOLERANCE:
       return False, f"Distribution mismatch: diff={dist_diff:.2%}"
   ```

   **Criterion 4: Boundaries stable**
   ```
   if boundary_degraded(final_boundary_stats, baseline_boundary_stats):
       return False, "Boundary degraded"
   ```

4. **If all pass:** Return True, "Healing successful"
5. **Else:** Return False with detailed failure reasons

## **5. ENERGY REFRESH CONTRACT IMPLEMENTATION**

### **Function: refresh_energy_for_metrics(tiling, region="buffer")**
**Purpose:** Ensure energy fields are consistent for metrics

**Logic:**
1. **If region == "full":**
   - Call `energy_model.update_tiling_energy(tiling)`
   
2. **If region == "buffer":**
   - For each tile in buffer:
     - Compute `local_energy` using `energy_model.compute_local_energy()`
     - Update tile fields: `local_energy`, `energy_class`, etc.
   - Also update any tiles whose neighbors changed (cascade effect)

3. **Guarantee:** After this call, all tiles in specified region have consistent energy fields

**When to call:**
- Before computing baseline signature
- After defect creation (each flip)
- At every checkpoint during annealing
- Before final validation

## **6. FLIP ELIGIBILITY LOGIC**

### **Function: is_flip_allowed(hexagon_tiles, tiling, region_policy)**
**Purpose:** Check if a flip is permitted under constraints

**Logic:**
1. **Input:** List of tile IDs in hexagon
2. **Check each tile:**
   - MUST be in buffer region (all tiles)
   - MUST NOT be `immobile=True` (any tile)
   - MUST NOT be `removed=True` (any tile)
   - MUST NOT be `obstacle_type="pore"` (any tile)
3. **If all pass:** Return True
4. **Else:** Return False with reason

**Called by:**
- `create_controlled_defects`: Before applying flip
- `mc_engine`: Before attempting flip

## **7. HEALING PIPELINE - COMPLETE FLOW**

### **Step 0: Setup**
```
1. Load raw processed tiling
2. Initialize engines (energy, flip, MC) ← EXISTING
3. Create HealingEngine with engines
4. Define parameters:
   - center = (x, y)
   - R_core = 10.0
   - R_buffer = 15.0 (R_core + 5.0 buffer)
```

### **Step 1: Baseline Preparation**
```
1. tiling_baseline = prepare_healing_region(copy(raw_tiling), center, R_core, R_buffer)
2. refresh_energy_for_metrics(tiling_baseline, "full")
3. baseline_signature = compute_signature(tiling_baseline, region_policy)
4. metrics_tracker.initialize(baseline_signature)
```

### **Step 2: Experiment Setup**
```
1. tiling_experiment = prepare_healing_region(copy(raw_tiling), same params)
2. refresh_energy_for_metrics(tiling_experiment, "full")
3. initial_signature = compute_signature(tiling_experiment, region_policy)
4. Record initial state
```

### **Step 3: Controlled Damage (Optional)**
```
if CREATE_DEFECTS:
    target_defects = 15
    create_controlled_defects(tiling_experiment, target_defects)
    Verify: defect_count == target_defects ± tolerance
```

### **Step 4: Annealing**
```
temperature_schedule = [
    (5.0, 100),  # High T, few steps
    (3.0, 200),  # Medium-high
    (2.0, 300),  # Medium
    (1.0, 400),  # Medium-low
    (0.5, 500),  # Low
    (0.2, 600),  # Very low
    (0.1, 700)   # Freezing
]

for T, steps in temperature_schedule:
    anneal_with_constraints(tiling_experiment, T, steps)
    Check: acceptance rate > 0.01 (or adjust schedule)
```

### **Step 5: Validation**
```
success, message = validate_convergence(tiling_experiment, baseline_signature)
if success:
    Log: "Healing successful"
    Record metrics
else:
    Log: f"Healing failed: {message}"
    Analyze failure mode
```

### **Step 6: Output**
```
1. Save final tiling (with region metadata)
2. Export metrics history to JSON
3. Generate plots:
   - Defect count vs step
   - Energy vs temperature
   - Distribution evolution
   - Before/after comparison
```

## **8. KEY INVARIANTS (Must Always Hold)**

### **During Healing:**
1. **No vacuum boundaries:** All `ungrown` converted to `frozen`
2. **Immobile stays immobile:** Never flipped, never marked `flippable`
3. **Buffer boundary respected:** No flips outside buffer
4. **Energy consistency:** Metrics computed only after energy refresh
5. **Defect counting consistency:** Same policy used throughout

### **For Validation:**
1. **Baseline computed under same constraints** as experiment
2. **Tolerances defined and documented**
3. **All criteria must pass** for success
4. **Failure reasons logged** for debugging

## **9. INTEGRATION POINTS WITH EXISTING CODE**

### **MonteCarloEngine Integration:**
- **Call:** `mc_engine.run_step(tiling)` 
- **Enhancement:** Add `get_acceptance_rate()`, `get_flip_count()`
- **Constraint:** MC only selects from buffer-eligible hexagons

### **FlipEngine Integration:**
- **Call:** `flip_engine.apply_flip(hexagon, tiling)`
- **Enhancement:** Add `force_flip()` for defect creation
- **Constraint:** Reject flips with immobile tiles

### **Energy Model Integration:**
- **Call:** `energy_model.update_tiling_energy(tiling)`
- **Call:** `energy_model.compute_local_energy(tile_id)`
- **Constraint:** Set `treat_ungrown_as_vacuum=False` for healing

### **Visualization Integration:**
- **Call:** `src.viz.static_plots.plot_energy_map(tiling)`
- **Enhancement:** Overlay region boundaries (core/buffer)
- **Color coding:** Red=defect, Yellow=natural MEDIUM, Green=LOW

## **10. FAILURE MODES AND MITIGATION**

### **Failure: Defect count doesn't decrease**
**Check:**
1. Are defects actually in core? (Verify region masks)
2. Is defect policy correct? (Check eligibility)
3. Is temperature too low? (Check acceptance rate)
4. Are flips actually happening? (Check flip count)

### **Failure: Energy increases**
**Check:**
1. Is energy refresh working? (Compare before/after)
2. Are surface terms correct? (Check boundary energy)
3. Is MC accepting uphill moves? (Should at high T)

### **Failure: Convergence unstable**
**Check:**
1. Buffer too small? (Increase R_buffer - R_core)
2. Schedule too fast? (Add more steps at critical T)
3. Random seed? (Use fixed seed for reproducibility)

## **11. TESTING STRATEGY**

### **Unit Tests:**
1. **RegionPolicy:** Verify core ⊂ buffer ⊂ global
2. **DefectPolicy:** Count defects in known configurations
3. **Energy refresh:** Compare local vs full update
4. **Flip eligibility:** Test with immobile/removed tiles

### **Integration Tests:**
1. **Full pipeline:** From damage to healing
2. **Reproducibility:** Same seed → same results
3. **Boundary conditions:** Verify no vacuum artifacts
4. **Metrics consistency:** Compare manual vs automatic

### **Validation Tests:**
1. **Against perfect tiling:** Should converge perfectly
2. **Against damaged tiling:** Should heal to baseline
3. **Edge cases:** Single defect, multiple defects, boundary defects

This detailed specification provides complete logic flow while maintaining the architectural separation and respecting all physical constraints. Each function has clear inputs, logic, outputs, and contracts that ensure correctness.-




-------------------
--------------------

# **DETAILED FUNCTION IMPLEMENTATION SPECIFICATIONS**

## **1. HEALING ENGINE - CORE ORCHESTRATION**

```python
def prepare_healing_region(tiling_data, center, R_core, R_buffer):
    """
    Prepare tiling for healing by applying region masks and constraints.
    
    Args:
        tiling_data: Raw tiling dictionary
        center: (x, y) coordinates for region center
        R_core: Radius of core region (measurement)
        R_buffer: Radius of buffer region (mobility)
    
    Returns:
        Prepared tiling with region metadata
    """
    # 1. Create deep copy
    tiling = copy.deepcopy(tiling_data)
    
    # 2. Compute tile centers if not present
    if 'center' not in tiling['tiles'][0]:
        for tile in tiling['tiles']:
            tile['center'] = calculate_polygon_center(tile['vertices'])
    
    # 3. Mark regions
    for tile in tiling['tiles']:
        distance = euclidean_distance(tile['center'], center)
        
        if distance <= R_core:
            tile['region'] = 'core'
            tile['distance_to_center'] = distance
        elif distance <= R_buffer:
            tile['region'] = 'buffer'
            tile['distance_to_center'] = distance
        else:
            tile['region'] = 'frozen'
            tile['distance_to_center'] = distance
    
    # 4. Convert ungrown to frozen for healing semantics
    for tile in tiling['tiles']:
        if tile.get('growth_status') == 'ungrown':
            tile['growth_status'] = 'frozen'
    
    # 5. Set flippable flags
    for tile in tiling['tiles']:
        if (tile['region'] in ['core', 'buffer'] and 
            not tile.get('removed', False) and
            not tile.get('immobile', False) and
            tile.get('obstacle_type') != 'pore'):
            tile['flippable'] = True
        else:
            tile['flippable'] = False
    
    # 6. Add region statistics to metadata
    tiling['metadata']['healing_region'] = {
        'center': center,
        'R_core': R_core,
        'R_buffer': R_buffer,
        'core_count': count_tiles_by_region(tiling, 'core'),
        'buffer_count': count_tiles_by_region(tiling, 'buffer'),
        'frozen_count': count_tiles_by_region(tiling, 'frozen')
    }
    
    return tiling
```

```python
def create_controlled_defects(tiling_data, target_defect_count, max_attempts=5000):
    """
    Create exact number of defects in core region using reversible flips.
    
    Args:
        tiling_data: Prepared tiling with region metadata
        target_defect_count: Exact number of defects to create
        max_attempts: Safety limit to prevent infinite loop
    
    Returns:
        Modified tiling with controlled defect count
    """
    # 1. Initialize
    current_defects = defect_policy.count_defects(tiling_data, region='core')
    attempt_count = 0
    flip_history = []  # For reverting if overshoot
    
    # 2. Main loop
    while current_defects != target_defect_count and attempt_count < max_attempts:
        # 2.1 Select candidate hexagon in buffer region
        candidate_hexagon = None
        for _ in range(100):  # Try 100 times to find valid hexagon
            hexagon = flip_engine.find_random_flippable_hexagon(tiling_data)
            if hexagon and is_hexagon_in_buffer(hexagon, tiling_data):
                candidate_hexagon = hexagon
                break
        
        if not candidate_hexagon:
            attempt_count += 1
            continue
        
        # 2.2 Store current state of hexagon tiles
        hexagon_state = save_hexagon_state(candidate_hexagon, tiling_data)
        
        # 2.3 Apply flip (force mode, ignore energy change)
        flip_engine.force_flip(candidate_hexagon, tiling_data)
        
        # 2.4 Refresh energy for affected tiles
        affected_tiles = get_affected_tiles_by_flip(candidate_hexagon, tiling_data, radius=2)
        refresh_energy_for_tiles(affected_tiles, tiling_data)
        
        # 2.5 Count new defects
        new_defects = defect_policy.count_defects(tiling_data, region='core')
        
        # 2.6 Decision logic
        distance_old = abs(current_defects - target_defect_count)
        distance_new = abs(new_defects - target_defect_count)
        
        if distance_new < distance_old:
            # Better: accept flip
            current_defects = new_defects
            flip_history.append({
                'hexagon': candidate_hexagon,
                'state': hexagon_state,
                'accepted': True,
                'defects_before': current_defects,
                'defects_after': new_defects
            })
        elif distance_new == distance_old:
            # Same distance: 50% chance to accept (prevent loops)
            if random.random() < 0.5:
                current_defects = new_defects
                flip_history.append({
                    'hexagon': candidate_hexagon,
                    'state': hexagon_state,
                    'accepted': True,
                    'defects_before': current_defects,
                    'defects_after': new_defects
                })
            else:
                # Revert
                restore_hexagon_state(candidate_hexagon, hexagon_state, tiling_data)
                flip_history.append({
                    'hexagon': candidate_hexagon,
                    'state': hexagon_state,
                    'accepted': False
                })
        else:
            # Worse: revert
            restore_hexagon_state(candidate_hexagon, hexagon_state, tiling_data)
            flip_history.append({
                'hexagon': candidate_hexagon,
                'state': hexagon_state,
                'accepted': False
            })
        
        attempt_count += 1
    
    # 3. Verification
    final_defects = defect_policy.count_defects(tiling_data, region='core')
    
    if final_defects == target_defect_count:
        log_info(f"Successfully created {final_defects} defects in core")
    else:
        log_warning(f"Created {final_defects} defects (target: {target_defect_count})")
    
    # 4. Store defect creation metadata
    tiling_data['metadata']['defect_creation'] = {
        'target': target_defect_count,
        'achieved': final_defects,
        'attempts': attempt_count,
        'flip_history': flip_history,
        'success': (final_defects == target_defect_count)
    }
    
    return tiling_data
```

```python
def anneal_with_constraints(tiling_data, temperature_schedule, steps_per_T, checkpoint_interval=10):
    """
    Run constrained annealing with regular energy refresh and metrics recording.
    
    Args:
        tiling_data: Prepared tiling with defects
        temperature_schedule: List of (temperature, steps) tuples
        steps_per_T: Steps per temperature if schedule is list of temperatures
        checkpoint_interval: How often to record metrics
    
    Returns:
        Annealed tiling and metrics history
    """
    # 1. Initialize tracking
    metrics_history = []
    total_steps = 0
    
    # 2. Parse schedule
    if isinstance(temperature_schedule[0], (int, float)):
        schedule = [(T, steps_per_T) for T in temperature_schedule]
    else:
        schedule = temperature_schedule
    
    # 3. Main annealing loop
    for temperature, steps_at_T in schedule:
        # 3.1 Set MC temperature
        mc_engine.temperature = temperature
        
        # 3.2 Run steps at this temperature
        for step in range(steps_at_T):
            # 3.2.1 Get list of flippable hexagons in buffer region
            flippable_hexagons = []
            for hexagon in flip_engine.find_all_flippable_hexagons(tiling_data):
                if is_hexagon_in_buffer(hexagon, tiling_data):
                    flippable_hexagons.append(hexagon)
            
            # 3.2.2 Select random hexagon (or biased toward defects)
            if flippable_hexagons:
                if BIAS_TOWARD_DEFECTS:
                    # Weight by nearby defect density
                    weights = compute_defect_density_near_hexagons(flippable_hexagons, tiling_data)
                    hexagon = random.choices(flippable_hexagons, weights=weights)[0]
                else:
                    hexagon = random.choice(flippable_hexagons)
                
                # 3.2.3 Check immobile constraint
                if not any(tiling_data['tiles'][t]['immobile'] for t in hexagon):
                    # 3.2.4 Attempt flip
                    accepted = mc_engine.attempt_flip(hexagon, tiling_data)
                    
                    # 3.2.5 Update local energy if accepted
                    if accepted:
                        affected_tiles = get_affected_tiles_by_flip(hexagon, tiling_data, radius=2)
                        update_local_energy_for_tiles(affected_tiles, tiling_data)
            
            # 3.2.6 Checkpoint
            total_steps += 1
            if total_steps % checkpoint_interval == 0:
                # Refresh energy for entire buffer region
                refresh_energy_for_region(tiling_data, region='buffer')
                
                # Record metrics
                checkpoint = {
                    'step': total_steps,
                    'temperature': temperature,
                    'defects_core': defect_policy.count_defects(tiling_data, 'core'),
                    'defects_buffer': defect_policy.count_defects(tiling_data, 'buffer'),
                    'energy_total': compute_total_energy(tiling_data),
                    'energy_core_density': compute_energy_density(tiling_data, 'core'),
                    'energy_buffer_density': compute_energy_density(tiling_data, 'buffer'),
                    'acceptance_rate': mc_engine.get_acceptance_rate(),
                    'vertex_distribution': compute_vertex_distribution(tiling_data, 'core')
                }
                metrics_history.append(checkpoint)
        
        # 3.3 End of temperature stage
        log_info(f"Temperature {temperature:.2f} complete: {steps_at_T} steps")
    
    # 4. Final energy refresh
    refresh_energy_for_region(tiling_data, region='full')
    
    # 5. Store annealing metadata
    tiling_data['metadata']['annealing'] = {
        'schedule': schedule,
        'total_steps': total_steps,
        'final_temperature': schedule[-1][0],
        'metrics_checkpoints': len(metrics_history)
    }
    
    return tiling_data, metrics_history
```

## **2. DEFECT ANALYZER - POLICY IMPLEMENTATION**

```python
class DefectPolicy:
    """
    Centralized defect definition with configurable criteria.
    """
    
    def __init__(self, defect_criterion='physics', geometry_threshold=1.5, physics_threshold=1.5):
        """
        Initialize defect policy.
        
        Args:
            defect_criterion: 'geometry' (vertex_class) or 'physics' (energy_class)
            geometry_threshold: Threshold for vertex_class (if using custom threshold)
            physics_threshold: Threshold for energy_class (if using custom threshold)
        """
        self.defect_criterion = defect_criterion
        self.geometry_threshold = geometry_threshold
        self.physics_threshold = physics_threshold
        
        # Eligibility criteria (hard constraints)
        self.ELIGIBILITY_RULES = {
            'must_be_in_core': True,
            'must_not_be_removed': True,
            'must_not_be_pore': True,
            'must_not_be_immobile': True,
            'must_be_bulk': True,  # boundary_kind == 'bulk'
            'must_not_be_boundary': True,  # is_boundary == False
        }
    
    def is_eligible_for_defect_counting(self, tile):
        """
        Check if tile is eligible to be counted as a defect.
        
        Returns:
            Boolean indicating eligibility
        """
        # 1. Check region (must be in core for healing experiments)
        if self.ELIGIBILITY_RULES['must_be_in_core']:
            if tile.get('region') != 'core':
                return False
        
        # 2. Check activity constraints
        if self.ELIGIBILITY_RULES['must_not_be_removed']:
            if tile.get('removed', False):
                return False
        
        if self.ELIGIBILITY_RULES['must_not_be_pore']:
            if tile.get('obstacle_type') == 'pore':
                return False
        
        if self.ELIGIBILITY_RULES['must_not_be_immobile']:
            if tile.get('immobile', False):
                return False
        
        # 3. Check boundary constraints
        if self.ELIGIBILITY_RULES['must_be_bulk']:
            if tile.get('boundary_kind') != 'bulk':
                return False
        
        if self.ELIGIBILITY_RULES['must_not_be_boundary']:
            if tile.get('is_boundary', False):
                return False
        
        return True
    
    def is_defect(self, tile):
        """
        Determine if tile is a defect based on chosen criterion.
        
        Returns:
            Boolean indicating defect status
        """
        if not self.is_eligible_for_defect_counting(tile):
            return False
        
        if self.defect_criterion == 'geometry':
            # Option A: Use vertex_class field
            if 'vertex_class' in tile:
                return tile['vertex_class'] == 'HIGH_ENERGY'
            # Option B: Use local_energy with geometry threshold
            else:
                return tile.get('local_energy', 0) > self.geometry_threshold
        
        elif self.defect_criterion == 'physics':
            # Option A: Use energy_class field
            if 'energy_class' in tile:
                return tile['energy_class'] == 'HIGH_ENERGY'
            # Option B: Use local_energy with physics threshold
            else:
                return tile.get('local_energy', 0) > self.physics_threshold
        
        return False
    
    def count_defects(self, tiling_data, region='core'):
        """
        Count defects in specified region.
        
        Args:
            tiling_data: Tiling to analyze
            region: 'core', 'buffer', or 'all'
        
        Returns:
            Number of defects
        """
        count = 0
        for tile in tiling_data['tiles']:
            # Filter by region if specified
            if region == 'core' and tile.get('region') != 'core':
                continue
            elif region == 'buffer' and tile.get('region') not in ['core', 'buffer']:
                continue
            
            if self.is_defect(tile):
                count += 1
        
        return count
    
    def get_defect_tiles(self, tiling_data, region='core'):
        """
        Get list of defect tile IDs.
        
        Returns:
            List of tile IDs that are defects
        """
        defect_ids = []
        for i, tile in enumerate(tiling_data['tiles']):
            # Filter by region if specified
            if region == 'core' and tile.get('region') != 'core':
                continue
            elif region == 'buffer' and tile.get('region') not in ['core', 'buffer']:
                continue
            
            if self.is_defect(tile):
                defect_ids.append(i)
        
        return defect_ids
```

```python
def compute_signature(tiling_data, region_policy, defect_policy):
    """
    Compute comprehensive signature of tiling state.
    
    Returns:
        Dictionary with all signature metrics
    """
    signature = {
        'timestamp': time.time(),
        'region_params': {
            'center': region_policy.center,
            'R_core': region_policy.R_core,
            'R_buffer': region_policy.R_buffer
        },
        'core': {
            'tile_count': 0,
            'defect_count': 0,
            'energy_total': 0.0,
            'energy_density': 0.0,
            'vertex_distribution': {'LOW_ENERGY': 0, 'MEDIUM_ENERGY': 0, 'HIGH_ENERGY': 0},
            'energy_class_distribution': {'LOW_ENERGY': 0, 'MEDIUM_ENERGY': 0, 'HIGH_ENERGY': 0},
            'boundary_stats': {'bulk': 0, 'outer_edge': 0, 'pore_edge': 0, 'growth_front': 0}
        },
        'buffer': {
            'tile_count': 0,
            'energy_total': 0.0,
            'energy_density': 0.0,
            'vertex_distribution': {'LOW_ENERGY': 0, 'MEDIUM_ENERGY': 0, 'HIGH_ENERGY': 0}
        },
        'global': {
            'tile_count': len(tiling_data['tiles']),
            'energy_total': 0.0,
            'energy_density': 0.0,
            'boundary_stats': {'bulk': 0, 'outer_edge': 0, 'pore_edge': 0, 'growth_front': 0}
        }
    }
    
    # Collect statistics
    for tile in tiling_data['tiles']:
        region = tile.get('region', 'frozen')
        energy = tile.get('local_energy', 0.0)
        
        # Update global stats
        signature['global']['energy_total'] += energy
        
        # Update region-specific stats
        if region in ['core', 'buffer']:
            signature[region]['tile_count'] += 1
            signature[region]['energy_total'] += energy
            
            # Vertex distribution
            vertex_class = tile.get('vertex_class')
            if vertex_class in signature[region]['vertex_distribution']:
                signature[region]['vertex_distribution'][vertex_class] += 1
            
            # Energy class distribution (only for core)
            if region == 'core':
                energy_class = tile.get('energy_class')
                if energy_class in signature['core']['energy_class_distribution']:
                    signature['core']['energy_class_distribution'][energy_class] += 1
        
        # Boundary stats (all regions)
        boundary_kind = tile.get('boundary_kind', 'bulk')
        if boundary_kind in signature['global']['boundary_stats']:
            signature['global']['boundary_stats'][boundary_kind] += 1
        
        # Core-specific boundary stats
        if region == 'core' and boundary_kind in signature['core']['boundary_stats']:
            signature['core']['boundary_stats'][boundary_kind] += 1
    
    # Compute densities and finalize
    for region in ['core', 'buffer', 'global']:
        if signature[region]['tile_count'] > 0:
            signature[region]['energy_density'] = (
                signature[region]['energy_total'] / signature[region]['tile_count']
            )
    
    # Count defects using policy
    signature['core']['defect_count'] = defect_policy.count_defects(tiling_data, region='core')
    
    return signature
```

## **3. METRICS TRACKER - TELEMETRY IMPLEMENTATION**

```python
class MetricsTracker:
    """
    Track and analyze healing metrics with baseline comparison.
    """
    
    def __init__(self, baseline_signature, convergence_tolerances=None):
        """
        Initialize tracker with baseline for comparison.
        
        Args:
            baseline_signature: Signature of baseline (perfect) tiling
            convergence_tolerances: Dictionary of tolerance values
        """
        self.baseline = baseline_signature
        self.history = []
        
        # Default tolerances
        self.tolerances = convergence_tolerances or {
            'defects': 0,  # Must match exactly (no tolerance)
            'energy_density': 0.01,  # 1% tolerance
            'vertex_distribution': 0.05,  # 5% KL divergence
            'boundary_stats': 0.02,  # 2% change allowed
        }
        
        # Tracking buffers for convergence detection
        self.defect_history = []
        self.energy_history = []
        self.stable_steps_threshold = 20  # Steps without change to declare stable
    
    def record_checkpoint(self, step, temperature, tiling_data, 
                          region_policy, defect_policy):
        """
        Record comprehensive checkpoint with baseline comparison.
        """
        # 1. Compute current signature
        current_signature = compute_signature(tiling_data, region_policy, defect_policy)
        
        # 2. Compute distances from baseline
        distances = self._compute_distances(current_signature)
        
        # 3. Create checkpoint record
        checkpoint = {
            'step': step,
            'temperature': temperature,
            'signature': current_signature,
            'distances': distances,
            'convergence_status': self._check_convergence_status(distances)
        }
        
        # 4. Add to history
        self.history.append(checkpoint)
        
        # 5. Update convergence buffers
        self.defect_history.append(current_signature['core']['defect_count'])
        self.energy_history.append(current_signature['core']['energy_density'])
        
        # Keep only recent history for convergence detection
        if len(self.defect_history) > 50:
            self.defect_history.pop(0)
            self.energy_history.pop(0)
        
        return checkpoint
    
    def _compute_distances(self, current_signature):
        """
        Compute distances between current and baseline signatures.
        """
        distances = {}
        
        # 1. Defect distance
        current_defects = current_signature['core']['defect_count']
        baseline_defects = self.baseline['core']['defect_count']
        distances['defects'] = {
            'current': current_defects,
            'baseline': baseline_defects,
            'difference': current_defects - baseline_defects,
            'normalized': (current_defects - baseline_defects) / max(baseline_defects, 1)
        }
        
        # 2. Energy density distances (core and buffer)
        for region in ['core', 'buffer']:
            current_energy = current_signature[region]['energy_density']
            baseline_energy = self.baseline[region]['energy_density']
            
            if baseline_energy != 0:
                relative_diff = abs(current_energy - baseline_energy) / baseline_energy
            else:
                relative_diff = abs(current_energy - baseline_energy)
            
            distances[f'energy_{region}'] = {
                'current': current_energy,
                'baseline': baseline_energy,
                'absolute_difference': abs(current_energy - baseline_energy),
                'relative_difference': relative_diff
            }
        
        # 3. Vertex distribution distance (KL divergence)
        current_dist = current_signature['core']['vertex_distribution']
        baseline_dist = self.baseline['core']['vertex_distribution']
        distances['vertex_distribution'] = {
            'kl_divergence': compute_kl_divergence(current_dist, baseline_dist),
            'current': dict(current_dist),
            'baseline': dict(baseline_dist)
        }
        
        # 4. Boundary statistics distance
        current_boundary = current_signature['core']['boundary_stats']
        baseline_boundary = self.baseline['core']['boundary_stats']
        distances['boundary_stats'] = {
            'total_variation': compute_total_variation(current_boundary, baseline_boundary),
            'current': dict(current_boundary),
            'baseline': dict(baseline_boundary)
        }
        
        return distances
    
    def _check_convergence_status(self, distances):
        """
        Check if current state meets convergence criteria.
        """
        status = {
            'defects_converged': False,
            'energy_converged': False,
            'distribution_converged': False,
            'boundary_converged': False,
            'fully_converged': False
        }
        
        # 1. Defects convergence
        defect_diff = distances['defects']['difference']
        status['defects_converged'] = abs(defect_diff) <= self.tolerances['defects']
        
        # 2. Energy convergence (both core and buffer must converge)
        energy_core_diff = distances['energy_core']['relative_difference']
        energy_buffer_diff = distances['energy_buffer']['relative_difference']
        status['energy_converged'] = (
            energy_core_diff <= self.tolerances['energy_density'] and
            energy_buffer_diff <= self.tolerances['energy_density']
        )
        
        # 3. Distribution convergence
        kl_divergence = distances['vertex_distribution']['kl_divergence']
        status['distribution_converged'] = kl_divergence <= self.tolerances['vertex_distribution']
        
        # 4. Boundary convergence
        total_variation = distances['boundary_stats']['total_variation']
        status['boundary_converged'] = total_variation <= self.tolerances['boundary_stats']
        
        # 5. Fully converged if all criteria met
        status['fully_converged'] = all([
            status['defects_converged'],
            status['energy_converged'],
            status['distribution_converged'],
            status['boundary_converged']
        ])
        
        return status
    
    def compute_healing_efficiency(self):
        """
        Compute healing efficiency metrics.
        """
        if not self.history:
            return {}
        
        initial = self.history[0]['signature']
        final = self.history[-1]['signature']
        
        initial_defects = initial['core']['defect_count']
        final_defects = final['core']['defect_count']
        
        if initial_defects == 0:
            healing_efficiency = 1.0
        else:
            healing_efficiency = (initial_defects - final_defects) / initial_defects
        
        # Energy recovery
        initial_energy = initial['core']['energy_density']
        final_energy = final['core']['energy_density']
        baseline_energy = self.baseline['core']['energy_density']
        
        if abs(initial_energy - baseline_energy) > 0:
            energy_recovery = 1 - abs(final_energy - baseline_energy) / abs(initial_energy - baseline_energy)
        else:
            energy_recovery = 1.0
        
        # Time to converge
        convergence_step = None
        for i, checkpoint in enumerate(self.history):
            if checkpoint['convergence_status']['fully_converged']:
                convergence_step = checkpoint['step']
                break
        
        return {
            'healing_efficiency': healing_efficiency,
            'energy_recovery': energy_recovery,
            'defects_initial': initial_defects,
            'defects_final': final_defects,
            'defects_baseline': self.baseline['core']['defect_count'],
            'convergence_step': convergence_step,
            'total_steps': self.history[-1]['step'] if self.history else 0
        }
    
    def detect_stagnation(self):
        """
        Detect if healing has stalled.
        
        Returns:
            True if no progress in last N steps
        """
        if len(self.defect_history) < self.stable_steps_threshold:
            return False
        
        # Check if defects have been constant
        recent_defects = self.defect_history[-self.stable_steps_threshold:]
        defects_stable = all(d == recent_defects[0] for d in recent_defects)
        
        # Check if energy has been constant (within tolerance)
        recent_energy = self.energy_history[-self.stable_steps_threshold:]
        energy_range = max(recent_energy) - min(recent_energy)
        energy_stable = energy_range < self.tolerances['energy_density']
        
        return defects_stable and energy_stable
    
    def export_metrics(self, filepath):
        """
        Export metrics to JSON file.
        """
        export_data = {
            'baseline_signature': self.baseline,
            'tolerances': self.tolerances,
            'history': self.history,
            'summary': self.compute_healing_efficiency(),
            'timestamp': time.time(),
            'version': '1.0'
        }
        
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2, cls=NumpyEncoder)
```

## **4. ENERGY REFRESH CONTRACT IMPLEMENTATION**

```python
def refresh_energy_for_region(tiling_data, region='buffer', energy_model=None):
    """
    Ensure energy fields are consistent for metrics.
    
    Args:
        tiling_data: Tiling to refresh
        region: 'full', 'buffer', or 'core'
        energy_model: Energy model instance
    
    Returns:
        Updated tiling
    """
    if energy_model is None:
        energy_model = WidomInspiredEnergy.from_config()
    
    if region == 'full':
        # Full update
        energy_model.update_tiling_energy(tiling_data)
    
    elif region in ['buffer', 'core']:
        # Partial update for specific region
        region_tiles = []
        for i, tile in enumerate(tiling_data['tiles']):
            if tile.get('region') == region or (
                region == 'buffer' and tile.get('region') in ['core', 'buffer']
            ):
                region_tiles.append(i)
        
        # Also include neighbors (radius 2) for cascading effects
        affected_tiles = set(region_tiles)
        for tile_id in region_tiles:
            neighbors = get_neighbors_within_radius(tile_id, tiling_data, radius=2)
            affected_tiles.update(neighbors)
        
        # Update energy for affected tiles
        for tile_id in affected_tiles:
            energy = energy_model.compute_local_energy(tile_id, tiling_data)
            tiling_data['tiles'][tile_id]['local_energy'] = energy
            
            # Update energy class based on thresholds
            thresholds = energy_model.get_energy_thresholds()
            if energy < thresholds[0]:
                tiling_data['tiles'][tile_id]['energy_class'] = 'LOW_ENERGY'
            elif energy < thresholds[1]:
                tiling_data['tiles'][tile_id]['energy_class'] = 'MEDIUM_ENERGY'
            else:
                tiling_data['tiles'][tile_id]['energy_class'] = 'HIGH_ENERGY'
    
    return tiling_data
```

## **5. FLIP ELIGIBILITY AND CONSTRAINT CHECKS**

```python
def is_hexagon_eligible_for_flip(hexagon, tiling_data, region_policy=None):
    """
    Check if hexagon can be flipped under all constraints.
    
    Returns:
        (eligible: bool, reason: str if not eligible)
    """
    # 1. Basic hexagon check
    if not hexagon or len(hexagon) != 3:
        return False, "Invalid hexagon"
    
    # 2. Check all tiles are in buffer region
    if region_policy:
        for tile_id in hexagon:
            tile = tiling_data['tiles'][tile_id]
            if tile.get('region') not in ['core', 'buffer']:
                return False, f"Tile {tile_id} not in buffer region"
    
    # 3. Check immobile constraint
    for tile_id in hexagon:
        tile = tiling_data['tiles'][tile_id]
        if tile.get('immobile', False):
            return False, f"Tile {tile_id} is immobile"
    
    # 4. Check removed/pore constraint
    for tile_id in hexagon:
        tile = tiling_data['tiles'][tile_id]
        if tile.get('removed', False):
            return False, f"Tile {tile_id} is removed"
        if tile.get('obstacle_type') == 'pore':
            return False, f"Tile {tile_id} is pore"
    
    # 5. Check flippable flag (optional, for compatibility)
    for tile_id in hexagon:
        tile = tiling_data['tiles'][tile_id]
        if not tile.get('flippable', True):
            return False, f"Tile {tile_id} is not flippable"
    
    # 6. Check geometric validity (existing flip_engine check)
    if not flip_engine.is_hexagon_valid_for_flip(hexagon, tiling_data):
        return False, "Geometric constraints not satisfied"
    
    return True, "Eligible"
```

## **6. UTILITY FUNCTIONS**

```python
def get_neighbors_within_radius(tile_id, tiling_data, radius=1):
    """
    Get all neighbors within given radius using adjacency graph.
    
    Returns:
        List of tile IDs within radius
    """
    if 'adjacency_graph' not in tiling_data:
        return []
    
    visited = set([tile_id])
    current_frontier = [tile_id]
    
    for _ in range(radius):
        next_frontier = []
        for current_id in current_frontier:
            neighbors = tiling_data['adjacency_graph'].get(str(current_id), [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_frontier.append(neighbor)
        current_frontier = next_frontier
    
    visited.remove(tile_id)  # Remove self
    return list(visited)
```

```python
def compute_kl_divergence(dist1, dist2):
    """
    Compute KL divergence between two distributions.
    
    Note: Handles zero probabilities safely.
    """
    # Normalize distributions
    total1 = sum(dist1.values())
    total2 = sum(dist2.values())
    
    if total1 == 0 or total2 == 0:
        return float('inf')
    
    p = {k: v/total1 for k, v in dist1.items()}
    q = {k: v/total2 for k, v in dist2.items()}
    
    # Ensure same keys
    all_keys = set(p.keys()) | set(q.keys())
    
    kl = 0.0
    for key in all_keys:
        p_val = p.get(key, 1e-10)  # Small epsilon to avoid log(0)
        q_val = q.get(key, 1e-10)
        
        if p_val > 0:
            kl += p_val * math.log(p_val / q_val)
    
    return kl
```

This detailed implementation specification provides complete logic flows for all functions while maintaining the architectural separation. Each function has clear inputs, logic, outputs, and error handling, ready for direct translation to production code.



