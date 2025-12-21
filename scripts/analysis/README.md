# scripts/analysis

This folder contains **post-run analysis** utilities.  
They do **not** change physics code; they read experiment outputs and generate plots/CSVs.

## Recommended usage

### 1) ΔE distribution / energy landscape sanity check
Use this when you change energy parameters, flip logic, or cache logic.

```bash
python scripts/analysis/plot_energy_landscape.py \
  --config configs/phase1_baseline.toml \
  --sample 500 --k 4 \
  --outdir results/analysis
```

- `--seed-only` restricts flips to the seed region (useful if your experiments only flip in the seed).
- `--k` is the safety neighborhood for manual ΔE; `k=4` is conservative.

Outputs:
- `results/analysis/deltaE_hist_*.png`
- optional `results/analysis/deltaE_samples_*.json` with `--save-deltas`

---

### 2) Temperature sweep summary
Use after running a sweep that writes files like:
`data/growth_experiments/temp_sweep_T*.json`

```bash
python scripts/analysis/analyze_temperature_results.py
```

Outputs:
- `results/analysis/temperature_sweep_summary.csv`
- `results/analysis/temperature_sweep.png`

---

### 3) Growth experiment time-series
Use after running `run_growth_experiment.py` (or any script that saves a `growth_steps` list).

```bash
python scripts/analysis/analyze_growth_results.py --latest
```

Outputs:
- `results/analysis/growth_<file>.png`
- `results/analysis/growth_<file>.csv`

## Archiving legacy analysis scripts

If you still have older duplicated scripts (e.g. `debug_energy_distribution.py`), move them to
`scripts/archive/analysis_legacy/` instead of deleting them.
