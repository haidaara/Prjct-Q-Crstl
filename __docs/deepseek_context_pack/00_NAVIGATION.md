# PROJECT: Phason Dynamics in Quasicrystal Growth

## NORTH STAR (Immutable)

**Project definition:** *Phason Dynamics in Quasicrystal Growth*

**Core research question (verbatim):**
> "How do phason dynamics enable defect-free growth around obstacles in quasicrystals, and can we model this healing process as an emergent many-body system?"

**Primary Phase Focus (now):** Phase 1 — classical phason healing model (Penrose tilings + phason flips + growth around obstacles + quantitative healing metrics).

**Baseline stance:** deterministic, low-noise runs first (random ensembles later, only when explicitly enabled).


## CURRENT STATE (Update this often)

- **Last updated:** 2025-12-26
- **Repo snapshot inputs:** `src/`, `experiments/`, `analysis/`, `validation/`, `dev_tools/`, `phase2_experiments.toml`, `cheat-sheet_phase2.toml`
- **Milestones (from tracker):**
  - ✅ Milestone 1: Penrose tiling generation + topology foundations
  - ✅ Milestone 2: Obstacle creation & validation (pores + fixed defects)
  - ✅ Milestone 3: Energy landscape initialization (Widom-inspired discrete classes + limited corrections)
  - ⚠️ Next: Flip dynamics + healing (MC) + growth fidelity + temperature studies

- **Known "big knobs":** see `01_ARCHITECTURE.yaml > parameters` (T, steps, defect densities, pore radii, etc.)


## SEMANTIC ANCHORS (use these as bookmarks)

- `[#TILINGS-CORE]` Penrose tiling generation + topology
- `[#OBSTACLES]` Obstacles: pores (removed tiles) + fixed defects (immobile tiles)
- `[#ENERGY-CALC]` Vertex classification + Widom-inspired energy model
- `[#FLIP-ENGINE]` Local phason flips and flip validation
- `[#MC-HEALING]` Monte Carlo healing / annealing schedules
- `[#GROWTH]` Growth simulation around obstacles
- `[#VALIDATION]` Validation scripts + checks
- `[#VIZ]` Visualization + plotting utilities
- `[#ENTRYPOINTS]` Top-level experiment scripts
- `[#DEV-TOOLS]` One-off diagnostics and debug tooling


## REASONING FRAMEWORK (how to think about this system)

This codebase is a **stateful simulation pipeline**.

**Canonical objects:**
- `TilingState` (JSON): global tiling + `tiles[]` + `adjacency_graph` + `metadata`.
- `Tile` (dict inside `tiles[]`): geometric + topological + obstacle flags + energy fields.

**Canonical stages:**
1) Generate tiling (Penrose P3)
2) Build topology (adjacency + lattice coords/strip families)
3) Apply obstacles (pores/fixed defects)
4) Initialize energy landscape (vertex_class + local_energy)
5) Dynamics (flip proposals + MC acceptance + growth rule)
6) Validate + analyze + plots

**Always debug in this order:**
(1) schema/keys → (2) invariants → (3) topology → (4) energy correctness → (5) dynamics acceptance & drift → (6) plots/metrics.


## COMMON FAILURE PATTERNS (high signal)

When something breaks, it’s usually one of these:

1) **Import path mismatch** (singular vs plural package paths)
   - Symptom: `ModuleNotFoundError`
   - Fix: ensure scripts add project root to `sys.path` consistently.

2) **ID normalization mismatch (string ↔ int)**
   - Symptom: adjacency graph lookup fails, KeyError on IDs
   - Policy: **in-memory ints**, JSON-export string keys only (then re-normalize on load).

3) **Removed tiles still have neighbors**
   - Symptom: growth / MC visits removed nodes → weird behavior
   - Contract: removed tiles must have `neighbors = []` (or be excluded everywhere).

4) **Contradictory tile flags**
   - Symptom: a tile marked both `removed` and `immobile`
   - Contract: forbidden; validation must fail.

5) **Non-determinism sneaks in**
   - Symptom: different results for same config
   - Fix: seed discipline + deterministic placement; avoid implicit RNG.

6) **Energy hierarchy broken**
   - Symptom: LOW/MEDIUM/HIGH overlap, or pores contribute nonzero energy
   - Fix: keep base class separation; pores/removed must contribute 0 energy.

7) **Performance cliffs**
   - Symptom: obstacle placement scales badly
   - Fix: spatial indexing; avoid O(n²) scans; keep active-tile policy consistent.


## REASONING TEMPLATES (copy/paste mental macros)

```yaml
REASONING_TEMPLATES:
  debugging: >
    When debugging [X], first verify schema keys + invariants,
    then check component outputs feeding into [X],
    common mismatch is [ID type / removed neighbors / missing energy fields].

  optimization: >
    To optimize [A], identify the hotspot (profile if possible),
    reduce repeated scans (cache, spatial index),
    preserve determinism and invariants.

  extension: >
    To add [C], modify [D], update (01_ARCHITECTURE.yaml + schema glossary),
    add a validation check, then add a minimal reproduction script.
```


## CONTEXT CARRIAGE (how to resume after breaks)

When starting a new session, paste:

1) “Continuing from: [last topic]”
2) “Current focus: [file + function/class]”
3) “Recent change: [1–2 lines]”
4) “Immediate question: [exact ask]”
5) “Minimal context: [10–80 lines or signature list + tiny JSON example]”


## NEXT FOCUS AREAS (edit as you go)

1) **Flip engine correctness**
   - DoD: flip proposal/accept preserves topology & energy consistency; no drift when `verify_energy=True`.
   - Artifacts: validation report + small reproducible case.

2) **Healing experiment (MC schedules)**
   - DoD: damage → anneal stages produce measurable reduction in defect metrics around obstacles.
   - Artifacts: `data/experiments/healing/*.json` + plots.

3) **Growth fidelity around obstacles**
   - DoD: growth engine respects pores/immobile constraints; produces stable growth metrics.
   - Artifacts: `data/experiments/growth/*.json` + `validation/visualize_growth_fidelity.py` plots.

4) **Temperature sweep summary**
   - DoD: run a sweep; produce summary stats & acceptance vs T curves.
   - Artifacts: `data/experiments/temp_sweep/*.json` + `analysis/analyze_temperature_results.py`.


## SESSION TEMPLATES (what to send to DeepSeek each time)

### A) Debugging template
```
PROBLEM: [one sentence]
WHERE: [file + function/class]
EXPECTED: [...]
OBSERVED: [...]
MIN REPRO:
- config excerpt: [...]
- tiny input JSON snippet: [...]
- stack trace / log: [...]
QUESTION: Why is this happening and what is the smallest safe fix that preserves invariants?
```

### B) Design / refactor template
```
GOAL: [what you want to improve]
CONSTRAINTS: [invariants from 01_ARCHITECTURE.yaml]
SCOPE: [which modules]
PROPOSE: [two options max]
QUESTION: Which option best preserves determinism + correctness? Provide minimal diff plan.
```

### C) Performance template
```
BOTTLENECK: [function + approximate runtime]
PROFILE: [if available]
DATA SIZES: [n tiles, densities, steps]
QUESTION: Provide 2–3 optimizations with tradeoffs, preserving determinism and contracts.
```


## CHANGELOG (append-only)

- (init) Created DeepSeek context pack skeleton and deep code index.
