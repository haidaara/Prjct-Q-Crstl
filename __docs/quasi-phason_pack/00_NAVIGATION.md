# Project Navigation (Context Pack)

## North Star
Build a **research-grade, reproducible** simulation pipeline for **phason dynamics / healing** in a Penrose P3 tiling with:
- a physically motivated (Widom-inspired) **local energy** model,
- Monte Carlo flips that respect **geometry consistency** and **energy bookkeeping**,
- obstacles (pores / fixed defects) + growth/healing experiments,
- analysis & visualization that make failures obvious.

## Quickstart (Milestone Commands)
Run from project root:
```bash
python scripts/experiments/01_generate_tiling.py
python scripts/experiments/01_prepare_processed_tiling.py
python scripts/experiments/02_generate_obstacles.py
python scripts/experiments/03_run_healing_test.py
# optional
python scripts/experiments/05_temperature_sweep.py
```

## Canonical Data Objects
**Tiling state JSON** is the single source of truth.
- `tiles[]` list: per-tile geometry + physics fields
- `adjacency_graph`: neighborhood topology (keys often serialized as strings)
- `metadata`: generation info, window origin/size, counts

## Pipeline Stages
0) **Generate** raw tiling + adjacency
1) **Prepare / initialize** physics fields + energy landscape + validation
2) **Obstacles**: pores / fixed defects / masks
3) **Healing**: MC damage + annealing schedule
4) **Growth**: seed region + frontier rules
5) **Sweeps / batch**: temperature & scenario grids

## Debug Order (fast → deep)
1) **Imports & packaging**: `from src.utils.config import ConfigManager` works.
2) **Schema sanity**: `tiles[]` exists, `id` is stable, `adjacency_graph` present.
3) **Energy fields**: `vertex_class`, `local_energy`, (optionally) `surface_energy`, `missing_bonds`.
4) **Flip legality**: do not flip removed/ungrown tiles; ensure k-ring neighborhoods are consistent.
5) **Energy verification**: delta-E computed locally matches global recompute.

## Common Silent Failure Patterns
- **Adjacency typing drift**: JSON forces string keys → neighbor lookups silently return empty.
- **Package shadowing**: a file named `src/utils.py` breaks `src.utils.*` imports.
- **Boundary masquerading as defects**: surface energy dominates; boundary tiles must be treated explicitly.
- **Cached vertex classes not cleared**: energy inconsistencies that vanish on recompute.
- **Validator drift**: validation thresholds hard-coded to old energy ranges.

## Current Focus
- **Stage 01**: energy landscape consistency (new surface + phason terms)
- **Stage 03**: healing metrics & “silent” metadata mismatches not visible in plots
