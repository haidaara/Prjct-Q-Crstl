# Dev tools

These are *debugging helpers*, not the GO/NO-GO gate.

## When to use what

- `system_diagnostic.py`  
  Quick check that paths + imports + base tiling load correctly.

- `diagnose_active_region_flips.py`  
  Use when MC “does nothing” (acceptance ~0, no flips). It measures how many flippable hexagons exist globally and inside the seed/active region.

- `debug_flip_geometry.py`  
  Use when flips look wrong (parity issues, geometry inconsistencies, unexpected tile center jumps). It stress-tests apply/undo on random hexagons and checks local energy deltas with cache hygiene.

- `label_diagnostics.py`  
  Use when you suspect label/caching issues (stale energy, wrong vertex classes, weird persistence). It compares “cached” vs “fresh” recomputes over a sample and after a few flips.

- `quick_mc_smoke_test.py`  
  Use to sanity-check MC runs end-to-end (proposal -> accept/reject -> drift stats) on a small number of steps.

- `temperature_probe.py`  
  Use when temperature dependence looks broken; runs multiple temperatures from the same initial state and reports acceptance and energy trend.

## Important

- For *production correctness*: always run `python scripts/validation/run_all.py`.
- Dev tools are for *finding why* a validation failed or diagnosing a suspicious symptom.
