# Validation Suite (GO/NO-GO)

Run this before experiments (or after any change to `src/energy`, `src/simulation`, or data generation):

```bash
python scripts/validation/run_all.py
```

What it guarantees:
- `validate_tiling.py`: topology/adjacency is sane (IDs, symmetry, no active orphans).
- `validate_obstacles.py`: pore JSONs are consistent with metadata when present.
- `validate_energy.py`: physics engine is deterministic, convention-consistent, and MC drift is contained (fresh-model ground truth).

If anything fails: stop and debug using `scripts/dev_tools/*`.
