# **RESEARCH OUTPUT STRUCTURE ANALYSIS & DESIGN**

Let's systematically design a research-grade output structure for your phason healing experiments.

## **1. CURRENT OUTPUT ASSESSMENT**

Looking at `03_run_healing_test.py`, the current output is:
```
data/experiments/healing/
├── healing_1704221234_random_tiling.json
├── healing_1704221234_random_metrics.json
├── healing_1704221234_random_summary.json
└── healing_1704221234_random_config.json
```

**Problems:**
1. **Non-informative naming** (timestamp + random)
2. **No organization** by experiment parameters
3. **Missing snapshots** at key stages
4. **No visual hierarchy** for quick analysis

## **2. RESEARCH OUTPUT REQUIREMENTS**

For effective study, we need:

### **A. Structured Experiment Tracking**
- **Human-readable experiment IDs** that encode parameters
- **Consistent directory structure** across all experiments
- **Quick visual assessment** of success/failure

### **B. Verbose Logging for Debugging**
- **Per-tile details** for selected flips (verbosity=2)
- **Stage-by-stage progress** with clear milestones
- **Energy conservation verification** at each step

### **C. Analysis-Ready Data**
- **Time-series data** for all metrics
- **Snapshots at key moments** (initial, defect creation, after each temperature)
- **Visualizations** that reveal patterns

### **D. Reproducibility**
- **Complete configuration** saved with results
- **Random seeds** recorded
- **Environment info** (Python version, package versions)

## **3. PROPOSED OUTPUT STRUCTURE**

```
data/experiments/
└── healing/
    ├── experiments.manifest.json                    # All experiment metadata
    └── run_{N:03d}_{experiment_name}/              # Per-experiment directory
        ├── README.md                               # Human summary
        ├── config.json                             # Complete configuration
        ├── environment.json                        # Software environment
        ├── summary.json                            # Key results
        ├── metrics_full.json                       # Complete time-series data
        ├── seed.txt                                # Random seed used
        ├── logs/
        │   ├── healing.log                         # Verbose text log
        │   ├── debug_verbosity2.log                # High-verbosity debug
        │   └── errors.log                          # Any errors encountered
        ├── snapshots/
        │   ├── 000_initial.json                    # Before defect creation
        │   ├── 001_after_defects.json              # After defect creation
        │   ├── 002_T=5.0_steps=100.json           # After each temperature
        │   ├── 003_T=3.0_steps=200.json
        │   └── 999_final.json                      # Final state
        ├── plots/
        │   ├── energy_evolution.png
        │   ├── defect_count_evolution.png
        │   ├── acceptance_rate.png
        │   ├── snapshot_comparison.png
        │   └── healing_efficiency_by_parameter.png
        └── analysis/
            ├── per_tile_changes.csv                # Tile-level statistics
            ├── flip_statistics.json                # Which flips happened where
            └── correlation_analysis.json           # Spatial correlations
```

## **4. EXPERIMENT NAMING CONVENTION**

Instead of timestamps, use **parameter-encoded names**:

```python
def generate_experiment_name(args):
    """Generate informative experiment name from parameters"""
    parts = []
    
    # Core parameters
    parts.append(f"core{args.R_core}")
    parts.append(f"buf{args.R_buffer}")
    
    # Defects
    if args.create_defects:
        parts.append(f"def{args.target_defects}")
    
    # Temperature schedule (simplified)
    if args.temperature_schedule:
        parts.append(f"T{args.temperature_schedule[0]}-{args.temperature_schedule[-1]}")
    
    # Steps
    parts.append(f"steps{args.steps_per_t * len(args.temperature_schedule)}")
    
    # Criterion
    parts.append(f"crit{args.defect_criterion[:3]}")
    
    return "_".join(parts)

# Example: core15_buf25_def15_T5.0-0.1_steps700_critphy
```

## **5. VERBOSE LOGGING ARCHITECTURE**

### **Three-Tier Verbosity System:**

```python
class ResearchLogger:
    def __init__(self, verbosity=1):
        self.verbosity = verbosity
        self.loggers = {}
    
    def log_level1(self, message):
        """Stage-level progress"""
        print(f"[{time.strftime('%H:%M:%S')}] {message}")
    
    def log_level2(self, message, details=None):
        """Tile-level details (verbosity=2)"""
        if self.verbosity >= 2:
            print(f"[DEBUG] {message}")
            if details:
                for key, value in details.items():
                    print(f"    {key}: {value}")
    
    def log_level3(self, tile_id, before, after, delta):
        """Per-tile physics changes (selected flips)"""
        if self.verbosity >= 2 and self._is_interesting_tile(tile_id):
            print(f"[TILE {tile_id}] E: {before:.3f} → {after:.3f} (Δ={delta:+.3f})")
```

### **Verbosity 1 vs Verbosity 2:**

```python
# Verbosity 1 (default) - Stage-level
[14:32:15] Starting defect creation...
[14:32:16] Created 15/15 defects (after 42 attempts)
[14:32:17] Starting healing: T=5.0, steps=100
[14:32:18] Stage complete: accepted 23/100 flips (23.0%)

# Verbosity 2 (debug) - Tile-level
[14:32:15] Starting defect creation...
[14:32:15] Attempt 1: Flip hexagon [123, 456, 789]
[DEBUG] Hexagon eligibility: True (all in buffer, not immobile)
[TILE 123] E: 0.450 → 1.230 (Δ=+0.780) class: LOW_ENERGY → HIGH_ENERGY
[TILE 456] E: 0.320 → 0.980 (Δ=+0.660) class: LOW_ENERGY → MEDIUM_ENERGY
[14:32:15] Defect count: 0 → 2
```

## **6. SNAPSHOT SYSTEM DESIGN**

### **Snapshot Manager Class:**

```python
class SnapshotManager:
    """Manages tiling state snapshots at key moments"""
    
    def __init__(self, base_dir, experiment_id):
        self.base_dir = Path(base_dir) / "snapshots"
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.snapshot_counter = 0
        self.key_snapshots = {}
    
    def take_snapshot(self, tiling_data, description="", metadata=None):
        """Save current tiling state with metadata"""
        snapshot_id = f"{self.snapshot_counter:03d}"
        filename = f"{snapshot_id}_{description.replace(' ', '_')}.json"
        filepath = self.base_dir / filename
        
        # Lightweight snapshot (don't save full adjacency every time)
        snapshot = {
            "snapshot_id": snapshot_id,
            "timestamp": time.time(),
            "description": description,
            "metadata": metadata or {},
            "tile_summary": self._create_tile_summary(tiling_data),
            "energy_summary": self._create_energy_summary(tiling_data),
            "defect_summary": self._create_defect_summary(tiling_data),
            # Optional: Save only changed tiles for efficiency
            "tiles": [self._compress_tile(t) for t in tiling_data["tiles"]]
        }
        
        with open(filepath, 'w') as f:
            json.dump(snapshot, f, indent=2)
        
        self.snapshot_counter += 1
        return filepath
    
    def _compress_tile(self, tile):
        """Create minimal tile representation for snapshots"""
        return {
            "id": tile["id"],
            "type": tile["type"],
            "center": tile["center"],
            "vertex_class": tile.get("vertex_class"),
            "energy_class": tile.get("energy_class"),
            "local_energy": tile.get("local_energy"),
            "is_boundary": tile.get("is_boundary", False),
            "is_core": tile.get("is_core", False)
        }
```

### **Key Snapshot Moments:**

```python
# In healing_engine.py
def run_full_experiment(self, ...):
    snapshot_manager = SnapshotManager(output_dir, experiment_id)
    
    # 1. Initial state
    snapshot_manager.take_snapshot(
        baseline_tiling, 
        description="initial_baseline",
        metadata={"defect_count": 0, "energy": baseline_energy}
    )
    
    # 2. After defect creation
    if create_defects:
        snapshot_manager.take_snapshot(
            tiling_data,
            description=f"after_defect_creation_{defects_created}",
            metadata={"defects_created": defects_created}
        )
    
    # 3. After each temperature stage
    for temp, steps in temperature_schedule:
        # ... run healing ...
        snapshot_manager.take_snapshot(
            tiling_data,
            description=f"T_{temp}_steps_{steps}",
            metadata={"temperature": temp, "steps": steps, 
                     "acceptance_rate": acceptance_rate}
        )
    
    # 4. Final state
    snapshot_manager.take_snapshot(
        tiling_data,
        description="final_healed",
        metadata={"healing_efficiency": healing_efficiency}
    )
```

## **7. SHALLOW STRUCTURE DESIGN**

Instead of deep nesting, use **flat structure with clear prefixes**:

```python
# BAD: Deep nesting
{
    "healing_results": {
        "stage_1": {
            "temperature": 5.0,
            "statistics": {
                "acceptance": {
                    "rate": 0.23,
                    "counts": {"accepted": 23, "rejected": 77}
                }
            }
        }
    }
}

# GOOD: Flat with prefixes
{
    "experiment_id": "run_001_core15_def15_T5.0",
    "timestamp": "2024-01-04T14:32:15",
    
    # Stage results in flat list
    "stage_results": [
        {
            "stage_id": "stage_1",
            "temperature": 5.0,
            "steps": 100,
            "accepted_flips": 23,
            "rejected_flips": 77,
            "acceptance_rate": 0.23,
            "energy_start": 450.2,
            "energy_end": 420.5,
            "defects_start": 15,
            "defects_end": 12
        },
        # ... more stages
    ],
    
    # Summary metrics (flat)
    "total_energy_change": -29.7,
    "total_defects_healed": 3,
    "healing_efficiency": 0.2,
    "converged": false,
    "stagnated": false
}
```

## **8. VERBOSE DEBUG OUTPUT FOR TILES**

### **Tile Debug Formatter:**

```python
class TileDebugFormatter:
    """Formats tile information for verbose debugging"""
    
    @staticmethod
    def format_tile(tile_id, tile_data):
        """Format single tile for debugging"""
        return (
            f"Tile {tile_id:4d} | "
            f"Type: {tile_data.get('type', '?'):5s} | "
            f"Class: {tile_data.get('vertex_class', '?'):12s} | "
            f"E: {tile_data.get('local_energy', 0):6.3f} | "
            f"Coords: ({tile_data.get('center', (0,0))[0]:6.2f}, "
            f"{tile_data.get('center', (0,0))[1]:6.2f}) | "
            f"Neighbors: {len(tile_data.get('neighbors', [])):2d}"
        )
    
    @staticmethod
    def format_flip_details(cluster_ids, before_states, after_states):
        """Format detailed flip information"""
        lines = ["╔══════════════════════════════════════╗"]
        lines.append("║         PHASON FLIP DETAILS         ║")
        lines.append("╠══════════════════════════════════════╣")
        
        for tile_id in cluster_ids:
            before = before_states[tile_id]
            after = after_states[tile_id]
            
            energy_change = after['energy'] - before['energy']
            energy_arrow = "↗" if energy_change > 0 else "↘"
            
            lines.append(f"║ Tile {tile_id:4d}:")
            lines.append(f"║   Energy: {before['energy']:6.3f} → {after['energy']:6.3f} "
                        f"({energy_arrow} {energy_change:+.3f})")
            lines.append(f"║   Class:  {before['class']:>10} → {after['class']:10}")
            lines.append(f"║   Type:   {before['type']:>10} → {after['type']:10}")
            
            if before['class'] != after['class']:
                lines.append(f"║           {'CLASS CHANGE!':^20}")
            
            if tile_id != cluster_ids[-1]:
                lines.append("╟──────────────────────────────────────╢")
        
        lines.append("╚══════════════════════════════════════╝")
        return "\n".join(lines)
```

## **9. AUTOMATED VISUAL SNAPSHOTS**

### **Visual Snapshot Generator:**

```python
class VisualSnapshotGenerator:
    """Generates visual snapshots at key moments"""
    
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir) / "visual_snapshots"
        self.output_dir.mkdir(exist_ok=True)
        self.figures = []
    
    def generate_snapshot(self, tiling_data, step, title_suffix=""):
        """Generate multi-panel visualization"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Panel 1: Energy map
        self._plot_energy_map(axes[0, 0], tiling_data)
        
        # Panel 2: Defect distribution
        self._plot_defect_distribution(axes[0, 1], tiling_data)
        
        # Panel 3: Vertex classes
        self._plot_vertex_classes(axes[1, 0], tiling_data)
        
        # Panel 4: Flip history (if available)
        self._plot_flip_history(axes[1, 1], step)
        
        # Title with experiment info
        fig.suptitle(f"Healing Progress - Step {step}{title_suffix}", fontsize=14)
        plt.tight_layout()
        
        # Save
        filename = self.output_dir / f"snapshot_step_{step:06d}.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        self.figures.append(str(filename))
        return filename
    
    def generate_comparison_gif(self):
        """Create animated GIF from snapshots"""
        # Use imageio to create GIF
        pass
```

## **10. IMPLEMENTATION PLAN**

### **Phase 1: Output Structure (1-2 days)**
```python
# 1. Update experiment script with sequential numbering
def get_next_run_number(base_dir="data/experiments/healing"):
    existing = [d for d in os.listdir(base_dir) if d.startswith("run_")]
    numbers = [int(d.split("_")[1]) for d in existing if d.split("_")[1].isdigit()]
    return max(numbers, default=0) + 1

# 2. Create ExperimentLogger class
class ExperimentLogger:
    def __init__(self, experiment_id, verbosity=1):
        self.experiment_id = experiment_id
        self.verbosity = verbosity
        self.setup_directories()
        
    def setup_directories(self):
        """Create standard directory structure"""
        dirs = ["logs", "snapshots", "plots", "analysis"]
        for dir_name in dirs:
            (self.base_dir / dir_name).mkdir(exist_ok=True)
```

### **Phase 2: Verbose Logging (1 day)**
- Integrate `ResearchLogger` with existing `verbosity` parameter
- Add tile-level debugging for verbosity=2
- Create progress bars for long operations

### **Phase 3: Snapshot System (1 day)**
- Implement `SnapshotManager` with lightweight snapshots
- Add automatic snapshots at key moments
- Create snapshot comparison visualization

### **Phase 4: Visualization (1 day)**
- Multi-panel figures for quick assessment
- Animated GIF of healing process
- Parameter sweep visualizations

## **11. MINIMAL VIABLE STRUCTURE**

If you want to start with the **minimum effective structure**:

```python
# data/experiments/healing/manifest.json
{
  "experiments": [
    {
      "id": "run_001",
      "name": "core15_buf25_def15_T5.0-0.1",
      "status": "completed",
      "summary": "Healing efficiency: 23.4%",
      "path": "run_001_core15_buf25_def15_T5.0-0.1",
      "timestamp": "2024-01-04T14:32:15"
    }
  ],
  "next_experiment_id": 2
}

# Each experiment directory has:
run_001_core15_buf25_def15_T5.0-0.1/
├── QUICK_READ.txt        # Human-readable 10-line summary
├── config.json           # Parameters
├── metrics.csv           # Time-series data (CSV for Excel)
├── final_state.json      # Final tiling (minimal)
└── progress.png          # Single multi-panel progress figure
```

## **12. IMMEDIATE ACTION**

Start with this **simple update** to your existing script:

```python
# Add to 03_run_healing_test.py after argument parsing:
import os

def get_next_run_number(base_dir="data/experiments/healing"):
    """Get next sequential run number"""
    os.makedirs(base_dir, exist_ok=True)
    
    existing = []
    for item in os.listdir(base_dir):
        if item.startswith("run_") and os.path.isdir(os.path.join(base_dir, item)):
            # Extract number from "run_001_something"
            parts = item.split("_")
            if len(parts) > 1 and parts[1].isdigit():
                existing.append(int(parts[1]))
    
    return max(existing, default=0) + 1

# Generate experiment name
run_number = get_next_run_number()
exp_name = generate_experiment_name(args)  # Implement this
experiment_dir = f"run_{run_number:03d}_{exp_name}"
output_dir = Path("data/experiments/healing") / experiment_dir
output_dir.mkdir(parents=True, exist_ok=True)

print(f"📁 Experiment directory: {output_dir}")
```

**This gives you immediate organization** while we refine the detailed structure.

---

**Which aspect should we implement first?**
1. Sequential numbering + organized directories
2. Verbose tile-level debugging
3. Snapshot system for key moments
4. Multi-panel visualization for quick assessment


------------------------


the proposed structure is professional and that is what we want, 

for logs, its good to always save the verbosity in file, and when specifying we manage their appearance in console then 

isn't the readme and summary the same why complicating it, keep it simple, 

its important to not that if defect tooked many steps, to be done, we should record these intermediate steps to make sure we have the ability to diagonize the even the defect creation process, 

for the plots is really important to have some metrics plot directly existed, 

for the name as you mentionnned 
run_{number}_{experimentname} now if experiment name is not provided, he just save the run_XXX version if provide he extend the name with the given argument, 

it very good to make sure everything is modular from the toml configuration file, 
( the better is modular with conf it better so we don't need to change the scripts code every time ) 

for verbosity i prefer only 2, one is too verbose, and another is lesser but still informative in good way 

in the snapshot, 
your example of verbosity 2 it could be even more imformative, and the one like the 2 ( maybe a little less but even like this no problem ) 



=========================

stufy these consideration and take each into account, and give me the plan again



--------------------




# **REFINED RESEARCH OUTPUT STRUCTURE PLAN**

Based on your excellent considerations, here's the refined plan:

## **1. REVISED DIRECTORY STRUCTURE**

```
data/experiments/healing/
├── experiments.json                    # Central registry of all runs
└── run_{N:03d}_{experiment_name}/
    ├── config.toml                     # TOML configuration used
    ├── summary.txt                     # Human-readable 1-page summary
    ├── metrics.json                    # All quantitative results
    ├── seed.txt                        # Random seed
    ├── verbosity1.log                  # Console output (timestamps)
    ├── verbosity2.log                  # Detailed tile-level debug
    ├── defects_creation_log.json       # Step-by-step defect creation
    ├── snapshots/
    │   ├── 000_initial.json.gz         # Compressed initial state
    │   ├── 001_defect_step_001.json.gz # Intermediate defect steps
    │   ├── 002_defect_step_010.json.gz
    │   ├── ... (every N steps, configurable)
    │   ├── 050_healing_T5.0_step001.json.gz
    │   └── 999_final.json.gz
    └── plots/
        ├── healing_progress.png        # Multi-panel: Energy + Defects + Accept Rate
        ├── defect_creation_timeline.png
        ├── final_state_map.png
        └── metrics_comparison.png
```

## **2. KEY DESIGN DECISIONS**

### **A. Sequential Numbering with Optional Name**
```python
# Always sequential: run_001, run_002, run_003
# With optional name: run_001_core15_def15, run_002_core20_def20

def get_experiment_path(base_dir, experiment_name=""):
    """Get next sequential run directory"""
    next_id = get_next_run_number(base_dir)
    dir_name = f"run_{next_id:03d}"
    if experiment_name:
        dir_name = f"{dir_name}_{experiment_name}"
    return Path(base_dir) / dir_name
```

### **B. Dual Logging System**
```python
class DualLogger:
    """Logs to both file (always full) and console (verbosity controlled)"""
    
    def __init__(self, log_dir, console_verbosity=1):
        self.log_dir = Path(log_dir)
        self.console_verbosity = console_verbosity
        
        # Always create both log files
        self.file_log1 = open(log_dir / "verbosity1.log", "w")
        self.file_log2 = open(log_dir / "verbosity2.log", "w")
    
    def log(self, message, verbosity_level=1, tile_details=None):
        """Log message with verbosity control"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        full_message = f"[{timestamp}] {message}"
        
        # Always write to appropriate file log
        if verbosity_level == 1:
            self.file_log1.write(full_message + "\n")
        else:  # verbosity_level == 2
            self.file_log2.write(full_message + "\n")
        
        # Console output controlled by verbosity
        if verbosity_level <= self.console_verbosity:
            if tile_details and verbosity_level == 2:
                print(full_message)
                for tile_id, details in tile_details.items():
                    print(f"    Tile {tile_id}: {details}")
            else:
                print(full_message)
```

### **C. Defect Creation Step Tracking**
```python
class DefectCreationTracker:
    """Records every attempt during defect creation"""
    
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.attempts = []
        self.current_state_snapshots = {}
    
    def record_attempt(self, attempt_num, hexagon, success, 
                       defect_count_before, defect_count_after,
                       tile_changes=None):
        """Record one attempt"""
        record = {
            "attempt": attempt_num,
            "hexagon": hexagon,
            "success": success,
            "defects_before": defect_count_before,
            "defects_after": defect_count_after,
            "tile_changes": tile_changes or {},
            "timestamp": time.time()
        }
        self.attempts.append(record)
        
        # Save snapshot every N attempts (configurable)
        if attempt_num % 10 == 0:  # Configurable via TOML
            self.save_snapshot(attempt_num)
    
    def save_final_report(self):
        """Save complete defect creation log"""
        report = {
            "total_attempts": len(self.attempts),
            "successful_attempts": sum(1 for a in self.attempts if a["success"]),
            "final_defect_count": self.attempts[-1]["defects_after"] if self.attempts else 0,
            "attempts": self.attempts,
            "statistics": self.compute_statistics()
        }
        
        with open(self.output_dir / "defects_creation_log.json", "w") as f:
            json.dump(report, f, indent=2)
```

### **D. TOML-Driven Configuration**
```toml
# configs/healing_experiment.toml

[experiment]
name = "core15_def15_T5-0.1"  # Optional, appended to run_XXX
description = "Healing experiment with moderate defect density"

[regions]
center_x = 0.0
center_y = 0.0
R_core = 15.0
R_buffer = 25.0

[defects]
create_defects = true
target_defects = 15
criterion = "physics"  # "geometry" or "physics"
record_every_attempt = false  # Record every defect creation attempt?
snapshot_every_n_attempts = 10  # Save state every N attempts

[healing]
temperature_schedule = [
    [5.0, 100],
    [3.0, 200],
    [2.0, 300],
    [1.0, 400],
    [0.5, 500],
    [0.2, 600],
    [0.1, 700]
]

[snapshots]
enabled = true
compression = true  # Use gzip for storage
snapshots_to_keep = [
    "initial",
    "after_defects",
    "each_temperature",
    "every_n_steps = 50",  # During healing
    "final"
]

[logging]
console_verbosity = 1  # 1 or 2
file_verbosity = 2     # Always save verbosity 2 to file

[visualization]
generate_plots = true
plot_types = [
    "energy_evolution",
    "defect_count",
    "acceptance_rate",
    "heating_map"
]
dpi = 300
```

## **3. VERBOSITY LEVEL SPECIFICATION**

### **Verbosity 1 (Default - Console)**
```
[14:32:15.123] Starting defect creation (target: 15 defects)
[14:32:16.456] Attempt 42/5000: Created 1 defect (total: 8/15)
[14:32:17.789] Defect creation complete: 15 defects after 123 attempts
[14:32:18.012] Starting healing: T=5.0, steps=100
[14:32:19.345] Step 23/100: Accepted flip ΔE=-1.234 (cluster: [123, 456, 789])
[14:32:20.678] Stage complete: 34/100 accepted (34.0%), energy: 450.2 → 420.5
```

### **Verbosity 2 (File - Tile Details)**
```
[14:32:15.123] DEFECT_CREATION_START target=15
[14:32:15.456] ATTEMPT 1: Hexagon [123, 456, 789]
[14:32:15.457]   Tile 123: E=0.450→1.230 (Δ=+0.780), class=LOW→HIGH, coords=(12.3, 45.6)
[14:32:15.458]   Tile 456: E=0.320→0.980 (Δ=+0.660), class=LOW→MEDIUM, type=THICK
[14:32:15.459]   Tile 789: E=0.210→0.890 (Δ=+0.680), class=LOW→MEDIUM, neighbors=4
[14:32:15.460]   Defect count: 0 → 2 (change: +2)
[14:32:15.461] ATTEMPT 2: Hexagon [234, 567, 890] - REJECTED (not in buffer)
[14:32:15.462]   Reason: Tile 234 not in buffer region
```

## **4. SNAPSHOT SYSTEM ENHANCEMENT**

### **Lightweight Compressed Snapshots**
```python
import gzip
import json

class CompressedSnapshot:
    """Save only essential data for quick loading"""
    
    def save(self, tiling_data, filepath, compress=True):
        """Save minimal tiling representation"""
        minimal = {
            "metadata": {
                "timestamp": time.time(),
                "total_tiles": len(tiling_data["tiles"]),
                "energy": sum(t.get("local_energy", 0) for t in tiling_data["tiles"]),
                "defect_count": sum(1 for t in tiling_data["tiles"] 
                                   if t.get("energy_class") == "HIGH_ENERGY")
            },
            "tiles": [
                {
                    "id": t["id"],
                    "type": t["type"],
                    "center": t["center"],
                    "vertex_class": t.get("vertex_class"),
                    "energy_class": t.get("energy_class"),
                    "local_energy": t.get("local_energy"),
                    "is_boundary": t.get("is_boundary", False),
                    "is_core": t.get("is_core", False)
                }
                for t in tiling_data["tiles"]
                if not t.get("removed", False)  # Skip removed/pores
            ]
        }
        
        if compress:
            with gzip.open(f"{filepath}.gz", "wt", encoding="utf-8") as f:
                json.dump(minimal, f)
        else:
            with open(filepath, "w") as f:
                json.dump(minimal, f, indent=2)
```

### **Snapshot Trigger Points**
```python
# Based on TOML configuration
snapshot_points = {
    "initial": True,
    "after_defects": True,
    "each_temperature": True,
    "every_n_steps": 50,  # During healing
    "final": True,
    
    # Defect creation specific
    "defect_every_n_attempts": 10,
    "defect_milestones": [1, 5, 10, 15]  # When reaching these counts
}
```

## **5. AUTOMATED PLOT GENERATION**

### **Essential Plots (Generated Post-Experiment)**
```python
class AutoPlotter:
    """Generates publication-ready plots from experiment data"""
    
    def generate_all_plots(self, experiment_dir):
        """Generate standard set of plots"""
        plots = []
        
        # 1. Healing Progress Dashboard (4-panel)
        plots.append(self.plot_healing_dashboard(experiment_dir))
        
        # 2. Defect Creation Timeline
        plots.append(self.plot_defect_creation_timeline(experiment_dir))
        
        # 3. Final State Visualization
        plots.append(self.plot_final_state(experiment_dir))
        
        # 4. Temperature Schedule Effect
        plots.append(self.plot_temperature_effect(experiment_dir))
        
        return plots
    
    def plot_healing_dashboard(self, experiment_dir):
        """Multi-panel: Energy, Defects, Acceptance, Configuration"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Panel 1: Energy evolution
        # Panel 2: Defect count over time
        # Panel 3: Acceptance rate per temperature
        # Panel 4: Final defect spatial distribution
        
        plt.savefig(experiment_dir / "plots" / "healing_dashboard.png", dpi=300)
        return "healing_dashboard.png"
```

## **6. MODULAR INTEGRATION WITH TOML**

### **Main Script Refactoring**
```python
# 03_run_healing_test.py - Updated

import tomli
from dataclasses import dataclass

@dataclass
class HealingConfig:
    """Configuration from TOML"""
    experiment_name: str = ""
    regions: dict = None
    defects: dict = None
    healing: dict = None
    snapshots: dict = None
    logging: dict = None
    visualization: dict = None
    
    @classmethod
    def from_toml(cls, toml_path):
        with open(toml_path, "rb") as f:
            data = tomli.load(f)
        return cls(**data)

def main():
    # Load configuration
    config = HealingConfig.from_toml("configs/healing_experiment.toml")
    
    # Get experiment directory
    experiment_dir = get_experiment_path(
        "data/experiments/healing",
        config.experiment_name
    )
    
    # Initialize structured logging
    logger = DualLogger(
        log_dir=experiment_dir,
        console_verbosity=config.logging["console_verbosity"]
    )
    
    # Initialize snapshot manager
    snapshotter = SnapshotManager(
        experiment_dir / "snapshots",
        config=config.snapshots
    )
    
    # Initialize defect tracker
    defect_tracker = DefectCreationTracker(experiment_dir)
    
    # Run experiment with structured logging
    run_experiment_with_logging(
        config, logger, snapshotter, defect_tracker
    )
    
    # Generate plots
    if config.visualization["generate_plots"]:
        plotter = AutoPlotter()
        plotter.generate_all_plots(experiment_dir)
```

## **7. IMPLEMENTATION PHASES**

### **Phase 1: Core Infrastructure (2 days)**
1. **Sequential numbering system** with optional naming
2. **Dual logging system** (console + file with verbosity control)
3. **TOML configuration integration**
4. **Basic directory structure creation**

### **Phase 2: Enhanced Tracking (2 days)**
1. **Defect creation step tracking** with intermediate snapshots
2. **Compressed snapshot system** (gzip JSON)
3. **Verbosity 2 detailed tile logging**
4. **Central experiments.json registry**

### **Phase 3: Visualization & Analysis (1 day)**
1. **AutoPlotter** for standard plots
2. **Dashboard generation** (multi-panel)
3. **Summary.txt generation** (one-page overview)
4. **Metrics aggregation** for quick comparison

### **Phase 4: Polish & Validation (1 day)**
1. **Performance optimization** for large experiments
2. **Error handling** and recovery
3. **Validation scripts** to verify data consistency
4. **Documentation** for the output structure

## **8. IMMEDIATE START: MINIMAL VIABLE OUTPUT**

Start with this **immediate improvement** to your current script:

```python
# Add to the beginning of 03_run_healing_test.py
import tomli
from pathlib import Path
import json
from datetime import datetime

def setup_experiment_directory(args):
    """Create organized experiment directory"""
    base_dir = Path("data/experiments/healing")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Get next run number
    existing = [d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("run_")]
    run_numbers = []
    for d in existing:
        try:
            num = int(d.name.split("_")[1])
            run_numbers.append(num)
        except (ValueError, IndexError):
            continue
    
    next_run = max(run_numbers, default=0) + 1
    
    # Create directory name
    dir_name = f"run_{next_run:03d}"
    if args.experiment_name:
        dir_name = f"{dir_name}_{args.experiment_name}"
    
    exp_dir = base_dir / dir_name
    exp_dir.mkdir()
    
    # Create subdirectories
    (exp_dir / "snapshots").mkdir()
    (exp_dir / "plots").mkdir()
    
    return exp_dir

# In main(), before running experiment:
experiment_dir = setup_experiment_directory(args)
print(f"📁 Experiment directory: {experiment_dir}")

# Save configuration
config_data = vars(args)
with open(experiment_dir / "config.json", "w") as f:
    json.dump(config_data, f, indent=2)

# Redirect prints to log file
import sys
log_file = open(experiment_dir / "experiment.log", "w")
sys.stdout = Tee(sys.stdout, log_file)  # Implement Tee class
```

## **9. ADVANTAGES OF THIS STRUCTURE**

1. **Research-Ready**: Suitable for direct inclusion in papers
2. **Self-Documenting**: Each experiment contains all needed information
3. **Scalable**: Works for single runs or parameter sweeps
4. **Reproducible**: TOML + seed + environment = exact replication
5. **Analyzable**: Standardized format for batch analysis
6. **Storage Efficient**: Compressed snapshots, selective logging

## **10. NEXT STEPS**

**Start with Phase 1 immediately**:
1. Modify `03_run_healing_test.py` to use TOML configuration
2. Implement sequential numbering system
3. Create basic DualLogger for verbosity control

This gives you **immediate organization** while building toward the complete system.

**Would you like me to provide the code for any specific component first?** The TOML integration and sequential numbering would be quick wins.