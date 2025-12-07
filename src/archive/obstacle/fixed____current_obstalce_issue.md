Got it. Here’s a concise, **issue-by-issue brief** with: problem → why it matters → **exact place to fix** → tiny patch. I’m only covering the essentials you approved (1–4, 6–11), and I’m skipping any verification framework as requested.

---

## 1) Import path mismatch (singular vs plural)

**Problem.** `obstacle_config.py` imports from `src.obstacle...` but the codebase uses `src.obstacles...` → runtime ImportError.
**Why it matters.** Blocks the whole pipeline.
**Where to fix.** `obstacle_config.py` import lines. 
**Patch.**

```python
# obstacle_config.py
-from src.obstacle.obstacle_creator import ObstacleSpec
+from src.obstacles.obstacle_creator import ObstacleSpec
```

---

## 2) ID map normalization (string ↔ int)

**Problem.** `_id_to_index` keeps raw IDs; later code assumes `int(n)` → potential `KeyError`/mismatches.
**Why it matters.** Incorrect adjacency updates, flaky behavior.
**Where to fix.** `_build_spatial_index()` ID map. 
**Patch.**

```python
# obstacle_creator.py
-self._id_to_index = {tile["id"]: i for i, tile in enumerate(tiles)}
+self._id_to_index = {int(tile["id"]): i for i, tile in enumerate(tiles)}
```

---

## 3) Adjacency doesn’t blank removed nodes

**Problem.** After removals, you filter neighbors but keep neighbor lists for **removed** tiles (non-empty key persists).
**Why it matters.** Connectivity is inconsistent for later relaxation/healing steps.
**Where to fix.** `_update_adjacency_batch()` loop over `adjacency_graph`. 
**Patch.**

```python
for tile_id, neighbors in list(adjacency_graph.items()):
    tile_id_int = int(tile_id) if isinstance(tile_id, str) else tile_id
+   if removed_mask[self._id_to_index[tile_id_int]]:
+       adjacency_graph[tile_id] = []
+       continue
    adjacency_graph[tile_id] = [
        int(n) for n in neighbors
        if not removed_mask[self._id_to_index[int(n)]]
    ]
```

---

## 4) Pore spacing not radius-aware (+ hardcoded separation)

**Problem.** Position sampler uses a flat `min_separation=2.0` between **centers** and ignores actual radii → overlapping pores.
**Why it matters.** Over-removal and geometry inconsistencies.
**Where to fix.** In pores branch of `generate_scalable_obstacles` (compute **radii first**) and replace `_generate_random_positions(...)` with a radius-aware sampler; also read `min_separation` from TOML. Pores branch & helper appear here.   
**Minimal patch.**

```python
# obstacle_config.py (inside pores branch)
-positions = self._generate_random_positions(n_obstacles, window_size, window_origin)
-radii = self._generate_random_radii(n_obstacles)
+radii = self._generate_random_radii(n_obstacles)
+min_sep = float(self.config.obstacles.get("min_separation", 2.0))
+positions = self._generate_positions_radius_aware(
+    n_obstacles, window_size, window_origin, radii, min_sep, self.rng
+)

# add this helper near _generate_random_positions
def _generate_positions_radius_aware(self, n:int, size, origin, radii, min_sep, rng):
    positions = []
    for k in range(n):
        r_k = radii[k]; placed = False
        for _ in range(n*100):
            cand = tuple(rng.uniform([0.0,0.0],[size[0],size[1]],size=2) + np.array(origin))
            ok = all(np.linalg.norm(np.array(cand)-np.array(p)) >= (r_k + radii[j] + min_sep)
                     for j,p in enumerate(positions))
            if ok: positions.append(cand); placed=True; break
        if not placed: positions.append(cand)
    return positions
```

---

## 6) Misleading pores console message

**Problem.** Prints “Created X pores across Y obstacles” where X = **removed tiles**, Y = **pore regions**.
**Why it matters.** Confusing logs during sweeps.
**Where to fix.** `_create_pores_optimized()` print. 
**Patch.**

```python
print(f"   → Removed {removed_count} tiles within {len(spec.positions)} pore regions")
```

---

## 7) Fixed-defect contract (positions vs tile-based)

**Problem.** Spec currently includes `positions` for fixed defects, but implementation samples tiles directly and **ignores** those positions.
**Why it matters.** Metadata drift and confusion; simpler to keep **tile-based** for M2.
**Where to fix.**
• Stop generating positions for fixed_defects in `generate_scalable_obstacles`. 
• Make `ObstacleSpec.positions` optional/empty for fixed_defects. 
**Minimal patch.**

```python
# obstacle_config.py (fixed defects branch)
-positions = self._generate_random_positions(n_obstacles, window_size, window_origin)
-radii = []
+positions = []  # tile-based; positions not used
+radii = []

# obstacle_creator.py (dataclass; if you prefer not to edit types now, keep empty lists)
# from typing import Optional, List, Tuple
# positions: Optional[List[Tuple[float, float]]] = None
# radii: Optional[List[float]] = None
```

---

## 8) Key type policy (int in-memory; str on JSON)

**Problem.** Mixing str/int in `adjacency_graph` causes subtle bugs.
**Why it matters.** Consistent in-memory math; JSON requires string keys.
**Where to fix.** Keep **ints** everywhere in memory (already handled by item 2 + 3). When you **save to JSON** (e.g., in your orchestrator or a small export helper), convert keys to strings at the last mile. (No exporter in repo right now; plan it where you serialize the tiling dict.)
**Tiny utility (drop-in where you export).**

```python
def _adjacency_intkeys_to_str(d: Dict[int, list[int]]) -> Dict[str, list[int]]:
    return {str(k): [int(x) for x in v] for k, v in d.items()}
```

---

## 9) Deterministic sub-seeds per (type, density)

**Problem.** Using one global RNG can correlate placements across specs in a sweep.
**Why it matters.** Reproducibility & debuggability of experiments.
**Where to fix.** In `generate_scalable_obstacles` inside the loop over densities/types: derive a **local RNG** from `(seed, obstacle_type, density)` and pass it to samplers. 
**Minimal patch.**

```python
# obstacle_config.py (inside for density ... for obstacle_type ...)
root = int(self.config.tiling.get("seed", 42))
subseed = np.uint32(abs(hash((root, obstacle_type, float(density)))) % (2**32-1))
local_rng = np.random.default_rng(subseed)

# then use local_rng in _generate_* calls
radii = self._generate_random_radii(n_obstacles)              # can stay on class rng
positions = self._generate_positions_radius_aware(..., local_rng)
# or pass local_rng everywhere for full determinism
```

---

## 10) Boundary policy for pores (clip visually)

**Problem.** Some pores straddle the window boundary. You prefer to **cut what’s outside** (visual clipping), not reject.
**Why it matters.** Keeps input intact while plots remain clean.
**Where to fix.** Visualizer: ensure circles are clipped to axes patch. 
**Patch.**

```python
# obstacle_visualizer._plot_obstacles
circle = plt.Circle(center, radius, linewidth=2, fill=False)  # also fixes item 11
circle.set_clip_path(ax.patch)  # hard clip to axes rectangle
ax.add_patch(circle)
```

---

## 11) Circle linestyle hidden (fill=True)

**Problem.** With `fill=True`, dashed/edge styling isn’t visible.
**Why it matters.** Hard to validate regions by eye.
**Where to fix.** `_plot_obstacles()` circle creation. 
**Patch.**

```python
# obstacle_visualizer.py
-circle = plt.Circle(center, radius, color='black', alpha=0.3, linewidth=2, fill=True, linestyle='--')
+circle = plt.Circle(center, radius, linewidth=2, fill=False, linestyle='--')
```

---

### Quick sanity checks (no verification framework)

* **Run pores once** and confirm log reads “…Removed N tiles within M pore regions”. 
* **Pick one removed tile ID**; assert it has `neighbors: []` and the graph key (same ID) has `[]`. (After patch in item 3.) 
* **Plot** and verify circles are edge-only and clipped at the frame. 

If you want, I can bundle these patches into a single diff that only touches the lines above and nothing else.


------------------------------------

 adding thsi list: 

 ------------------------------------
 
 here’s the short “end list” you asked for—each item has a 1-line problem, **where** to touch, and a tiny **how**. i’ve kept only the items from the small tail section and reflected your accept/skip notes.

1. RNG re-initialized per call (pattern repetition) — **accepted**

* **Where:** `obstacle_creator._create_fixed_defects_optimized`
* **How:** remove local `np.random.default_rng(...)`; pass in a per-spec RNG from `ObstacleConfig.generate_scalable_obstacles` (derive sub-seed from `(global_seed, obstacle_type, density)`), and use that inside the function.

2. Trusting `metadata.tile_count` blindly — **accepted**

* **Where:** `obstacle_config.generate_scalable_obstacles`
* **How:** set `tile_count = len(tiling_data["tiles"])` if the array exists; only fall back to `metadata["tile_count"]` when tiles aren’t present.

3. Visualizer ignores `plot_dpi` in TOML — **accepted**

* **Where:** `obstacle_visualizer.plot_obstacles → plt.savefig(...)`
* **How:** read `dpi = self.viz_config.get("plot_dpi", 300)` and pass it to `savefig`.

4. Pore color hardcoded (config not applied) — **accepted**

* **Where:** `obstacle_visualizer._plot_obstacles` (circle creation)
* **How:** get `color = self.viz_config.get("obstacle_colors", {}).get("pore", "black")`; use it when creating `plt.Circle(...)`.

5. SciPy optional → O(N·M) fallback performance — **accepted**

* **Where:** optional KDTree import and the spatial-index build path in `ObstacleCreator`
* **How:** if `KDTree` is missing and `len(tiles)` is large, print a one-line advisory (“SciPy recommended for performance”); add to README/env notes.

6. Fixed-defect density denominator ambiguity — **defer (study & document)**

* **Where:** `obstacle_creator._create_fixed_defects_optimized` (computes `n_target`)
* **How:** pick and **document** one policy:

  * **Active-tiles policy (suggested):** `n_target = round(density * len(active_indices))`, or
  * **Total-tiles policy:** keep `len(tiles)` and accept clamp/under-hit post-pores.

7. Metadata consistency: positions stored for all types — **keep as is**

* **Where:** `obstacle_creator._finalize_obstacle_data`
* **How:** no code change; keep `positions` for all types per your preference. (Optionally add a note in metadata like `"positions_semantics": "centers for pores; unused for fixed_defects"` for clarity.)


