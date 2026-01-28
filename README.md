# New lightweight viz layer (drop-in)

This is a **script‑first** refactor of your older `viz_scripts`.

Goals:
- Preserve the **plot logic and panels** you already rely on (2x2, 3x3, change maps, spatial profiles, strain plots, storyboard/movie).
- Avoid “over‑engineering”: everything is **direct functions** you can call from a small script in `scripts/viz/`.
- Allow optional *batch generation* driven by your **existing** `configs/publication_plots.toml` under a single `[viz_jobs]` section.

---

## What you get

### Core package
`src/viz/`
- `config.py` — read `configs/publication_plots.toml`, resolve output folders, read `[viz_jobs]`.
- `io.py` — load/validate JSON state (must contain `tiles`), snapshot helpers.
- `style.py` — publication styling + `save_figure()`.
- `panels.py` — the important part: **panel building blocks** and 2x2 / 3x3 layout helpers.
- `static_plots.py` — publication figures for a single state (2x2, 3x3, diffraction, vertex distribution, radial defect density).
- `compare_plots.py` — baseline vs current (pair), baseline vs damaged vs healed (triptych), change map, drift series.
- `spatial_plots.py` — distance‑to‑obstacle binning + defect density profile.
- `strain_plots.py` — phason strain map + histogram + time series + strain vs defects + strain vs distance.
- `movie.py` — storyboard + movie from snapshots.
- `dashboards.py` — small “multi‑plot pages” using the same panels.

### Scripts (what you actually run)
`scripts/viz/`
- `01_viz_state.py` — run plots on a single JSON state.
- `02_viz_compare.py` — pair/triptych + change map.
- `03_viz_spatial.py` — defect density vs distance to obstacle.
- `04_viz_strain_dynamics.py` — strain time series from snapshots (+ optional defect correlation, storyboard).
- `05_viz_movie.py` — movie from snapshots.
- `00_viz_from_toml.py` — batch run from `[viz_jobs]`.

---

## Input JSON expectations
The loaders accept any “state-like” JSON as long as it contains:
- `tiles: [...]`
- Each tile should have `vertices` (polygon) or at least `center`.

Optional but used when present:
- `local_energy` (for energy maps and defect thresholding)
- `energy_class` / `vertex_class` (for class panels)
- `missing_bonds` (defect indicator)
- `growth_stage` (growth panels)
- `obstacle_type` (recommended; preferred over `immobile`)
- `phason_energy` (phason strain panels)

**Important:** boundary tiles may have `immobile=True` in some states. By default we **do not** treat `immobile=True` as a fixed obstacle.
If you really want that behavior, set `treat_immobile_as_fixed=true` in `[viz_jobs]`.

---

## Add this to your `configs/publication_plots.toml`

```toml
[viz_jobs]
enabled = true

# shared defaults
outdir = "data/viz"
defect_threshold = 1.5
energy_percentile = [5, 95]
strain_percentile = [5, 95]

# Only if you really want immobile == obstacle
treat_immobile_as_fixed = false

[[viz_jobs.jobs]]
kind = "state"
input = "data/processed/penrose_tiling_energy_initialized.json"
plots = ["matrix_2x2", "grid_3x3", "diffraction", "vertex_dist", "strain_map", "strain_hist"]
outdir = "data/viz/baseline"

[[viz_jobs.jobs]]
kind = "compare"
baseline = "data/processed/penrose_tiling_energy_initialized.json"
damaged  = "data/experiments/healing/run_021/snapshots/002_after_defects.json"
healed   = "data/experiments/healing/run_021/snapshots/999_final.json"
view = "strain"
outdir = "data/viz/run_021"

[[viz_jobs.jobs]]
kind = "storyboard"
snapshot_dir = "data/experiments/healing/run_021/snapshots"
view = "strain"
n_frames = 12
ncols = 4
outdir = "data/viz/run_021"

[[viz_jobs.jobs]]
kind = "movie"
snapshot_dir = "data/experiments/healing/run_021/snapshots"
view = "strain"
fps = 12
outdir = "data/viz/run_021"

[[viz_jobs.jobs]]
kind = "spatial"
input = "data/experiments/healing/healing_base_run_001.json"
bin_edges = [0, 2, 4, 6, 8, 10, 12]
outdir = "data/viz/spatial"
```

---

## Running

From repo root:

```bash
python scripts/viz/01_viz_state.py --input data/processed/penrose_tiling_energy_initialized.json --outdir data/viz/demo \
  --plots matrix_2x2,grid_3x3,strain_map,strain_hist

python scripts/viz/02_viz_compare.py --baseline data/processed/penrose_tiling_energy_initialized.json --healed data/experiments/healing/healing_base_run_001.json \
  --view strain --outdir data/viz/compare --drift

python scripts/viz/00_viz_from_toml.py
```

---

## Notes on publication quality (phason strain)

For a strong paper, the most informative minimal set is:
- **Strain map** (spatial field): `plot_strain_energy_map()`
- **Strain distribution** (hist): `plot_strain_histogram()`
- **Strain vs distance to obstacle** (core for obstacle statistics): `plot_strain_vs_distance()`
- **Strain time series** over snapshots: `plot_strain_series()`
- Optional but useful: **drift** (changed tiles vs baseline): `plot_phason_drift_series()`

