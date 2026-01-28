# **REFINED MODULAR ARCHITECTURE WITH FLAT STRUCTURE**

You're right. Let me refine the architecture to match your preference for a flat structure while maintaining modularity. Here's the optimized design:

## **1. FINAL FILE STRUCTURE**

```
src/output/
├── __init__.py           # Exports main classes
├── experiment_output.py  # Main orchestrator class
├── managers.py          # All manager classes
├── logging.py           # Logging system
├── metrics.py           # Metrics collection & aggregation
├── analysis.py          # Post-run analysis & plotting
└── config_schema.py     # Configuration validation
```

## **2. FUNCTION SIGNATURES & BEHAVIORS**

### **A. `experiment_output.py` - Main Orchestrator**

```python
"""
Main ExperimentOutput orchestrator - Single entry point for all output operations.
Handles initialization, coordination, and finalization of all output components.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Optional

@dataclass
class ExperimentConfig:
    """Configuration for experiment output system."""
    experiment_type: str  # "healing", "growth", "obstacle_sweep"
    name_suffix: str = ""  # Optional suffix for run name
    base_dir: str = "data/experiments"
    console_verbosity: int = 1  # 1 (stage-level) or 2 (detailed)
    file_verbosity: int = 2  # Always save detailed logs
    generate_plots_after: bool = True
    light_snapshots_enabled: bool = True  # If False, always use full snapshots


class ExperimentOutput:
    """
    Main orchestrator for experiment output system.
    Provides unified interface for logging, snapshots, and metrics.
    """
    
    def __init__(self, config: ExperimentConfig | Dict[str, Any]):
        """
        Initialize complete output system.
        
        Args:
            config: ExperimentConfig or dictionary with configuration.
                   If dict, will be converted to ExperimentConfig.
        """
        # 1. Validate and store config
        # 2. Initialize RunManager to create directory
        # 3. Initialize StatusManager (status.json)
        # 4. Initialize Logging system
        # 5. Initialize SnapshotManager
        # 6. Initialize MetricsCollector
        # 7. Write initial metadata
        
        # Internal components (initialized in __init__)
        self.run_dir: Path  # Experiment directory
        self.run_id: int    # Run number (001, 002, ...)
        self._status_manager: Any
        self._logger: Any
        self._snapshot_manager: Any
        self._metrics: Any
    
    def log(self, 
            message: str, 
            level: int = 1,
            event_type: Optional[str] = None,
            details: Optional[Dict] = None) -> None:
        """
        Smart logging with verbosity filtering.
        
        Args:
            message: Human-readable message
            level: 1 (stage-level) or 2 (detailed)
            event_type: Predefined event type for filtering
            details: Additional structured data for machine logging
        """
        # 1. Apply verbosity filters
        # 2. Write to console.log/detailed.log based on level
        # 3. Write to events.jsonl if event_type provided
        # 4. Write to errors.log if level == "error"
    
    def log_stage_start(self, 
                       stage_name: str,
                       stage_params: Optional[Dict] = None) -> None:
        """
        Mark beginning of a major experimental stage.
        
        Args:
            stage_name: e.g., "defect_creation", "healing_T5.0"
            stage_params: Dictionary of stage parameters
        """
        # 1. Log stage start with parameters
        # 2. Update internal stage tracking
        # 3. Take optional snapshot if configured
    
    def log_stage_end(self,
                     stage_name: str,
                     stage_results: Optional[Dict] = None) -> None:
        """
        Mark completion of a major experimental stage.
        
        Args:
            stage_name: Must match a started stage
            stage_results: Dictionary of stage outcomes
        """
        # 1. Log stage results
        # 2. Compute stage aggregates
        # 3. Take optional snapshot if configured
    
    def take_snapshot(self,
                     tiling_state: Dict,
                     reason: str = "",
                     metadata: Optional[Dict] = None,
                     force_full: bool = False) -> Path:
        """
        Capture current tiling state.
        
        Args:
            tiling_state: Complete tiling dictionary
            reason: Why snapshot taken (step_100, stage_end, error, etc.)
            metadata: Additional context for snapshot
            force_full: If True, override config to take full snapshot
        Returns:
            Path to saved snapshot file (.json.gz)
        """
        # 1. Determine snapshot type (full/light) based on config & force_full
        # 2. Create appropriate snapshot format
        # 3. Add metadata (step, reason, timestamp)
        # 4. Compress with gzip
        # 5. Save with naming: {counter:03d}_{reason}.json.gz
        # 6. Return file path
    
    def record_metrics(self,
                      step: int,
                      metrics: Dict) -> None:
        """
        Record time-series metrics for current step.
        
        Args:
            step: Current simulation step (or "final" for aggregates)
            metrics: Dictionary of metrics (energy, defects, acceptance, etc.)
        """
        # 1. Validate metrics schema
        # 2. Add timestamp and step
        # 3. Buffer in memory
        # 4. Flush to disk when buffer full (configurable)
        # 5. For spatial metrics, compute obstacle distances if needed
    
    def record_error(self,
                    error_type: str,
                    message: str,
                    context: Optional[Dict] = None,
                    recoverable: bool = True) -> None:
        """
        Record error with appropriate handling.
        
        Args:
            error_type: e.g., "energy_drift", "adjacency_inconsistency"
            message: Human-readable error description
            context: Additional error context (step, tile IDs, etc.)
            recoverable: Whether experiment can continue
        """
        # 1. Always log to errors.log
        # 2. Log to console if verbosity >= 1
        # 3. Take recovery snapshot if severe
        # 4. Update error statistics
    
    def finalize(self,
                success: bool = True,
                error_info: Optional[Dict] = None) -> None:
        """
        Complete experiment and write final outputs.
        
        Args:
            success: Whether experiment completed successfully
            error_info: Details if experiment failed
        """
        # 1. Update status to DONE/FAILED
        # 2. Write final metrics aggregates
        # 3. Generate plots if configured
        # 4. Create human-readable summary.txt
        # 5. Close all file handles
        # 6. Return success/failure status
```

### **B. `managers.py` - All Manager Classes**

```python
"""
All manager classes in one file for cohesion.
Includes RunManager, StatusManager, SnapshotManager, and SnapshotScheduler.
"""

import fcntl
import json
import gzip
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass

@dataclass
class RunInfo:
    """Information about a run."""
    run_id: int
    run_dir: Path
    experiment_type: str
    config: Dict[str, Any]


class RunManager:
    """Manages experiment directory creation and atomic run numbering."""
    
    @staticmethod
    def create_experiment_directory(config: Dict[str, Any]) -> RunInfo:
        """
        Create directory for new experiment.
        
        Returns:
            RunInfo with run_id, run_dir, and metadata
        """
        # 1. Get next run number atomically (with file locking)
        # 2. Create directory: run_{N:03d}_{suffix}
        # 3. Create subdirectories: snapshots/, analysis/
        # 4. Return RunInfo
    
    @staticmethod
    def get_next_run_number(base_dir: str) -> int:
        """
        Atomic run number allocation with file locking.
        
        Uses .runid.lock file for atomicity.
        Handles existing patterns: run_001, healing_run_001, etc.
        """
        # 1. Create lock file if doesn't exist
        # 2. Acquire exclusive lock
        # 3. Scan for existing run numbers
        # 4. Return max + 1
        # 5. Release lock
    
    @staticmethod
    def get_existing_runs(base_dir: str) -> Dict[int, Path]:
        """
        Get all existing runs for batch analysis.
        
        Returns:
            Dictionary mapping run_id to run directory
        """
        # Scan directory for run_* patterns
        # Return sorted dictionary


class StatusManager:
    """Manages experiment lifecycle state."""
    
    def __init__(self, run_dir: Path):
        self.status_file = run_dir / "status.json"
        self._ensure_status_file()
    
    def update(self,
              state: str,
              error_info: Optional[Dict] = None) -> None:
        """
        Update experiment status.
        
        Args:
            state: "RUNNING", "DONE", or "FAILED"
            error_info: Details if state is "FAILED"
        """
        # 1. Validate state transition (RUNNING → DONE, not DONE → RUNNING)
        # 2. Update with timestamp
        # 3. Write atomic update to status.json
    
    def get_status(self) -> Dict[str, Any]:
        """Return current status."""
        # Read and parse status.json
        # Return dict with state and metadata


class SnapshotManager:
    """Handles full and light snapshots with compression."""
    
    def __init__(self,
                 run_dir: Path,
                 config: Dict[str, Any]):
        self.snapshot_dir = run_dir / "snapshots"
        self.snapshot_dir.mkdir(exist_ok=True)
        self.config = config
        self.snapshot_counter = 0
        self.scheduler = SnapshotScheduler(config)
    
    def take_snapshot(self,
                     tiling_state: Dict[str, Any],
                     snapshot_type: str,
                     reason: str,
                     metadata: Optional[Dict] = None) -> Path:
        """
        Create and save snapshot.
        
        Args:
            tiling_state: Complete tiling dictionary
            snapshot_type: "full" or "light"
            reason: Description of why snapshot taken
            metadata: Additional context
        Returns:
            Path to saved snapshot file (.json.gz)
        """
        # 1. Determine filename: {counter:03d}_{reason}.json.gz
        # 2. Create snapshot data based on type
        # 3. Add metadata (step, timestamp, reason)
        # 4. Compress with gzip
        # 5. Write to file
        # 6. Increment counter
    
    def _create_full_snapshot(self,
                             tiling_state: Dict[str, Any],
                             metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create complete snapshot for reproducibility.
        """
        # Include everything needed to restart simulation:
        # - All tiles with vertices, centers, types
        # - Adjacency graph
        # - All physics fields (energy, vertex_class, etc.)
        # - Obstacle information
        # - Current random seed state
        # Return complete dictionary
    
    def _create_light_snapshot(self,
                              tiling_state: Dict[str, Any],
                              metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create visualization-ready snapshot (minimal).
        """
        # Include only what's needed for plotting:
        # - Tile IDs and positions (x, y)
        # - Current energies (if changed from last snapshot)
        # - Defect locations (tile IDs with HIGH_ENERGY class)
        # - Obstacle centers and radii
        # - Region boundaries (core/buffer)
        # Return minimal dictionary
    
    def load_snapshot(self, snapshot_path: Path) -> Dict[str, Any]:
        """
        Load snapshot from compressed file.
        
        Args:
            snapshot_path: Path to .json.gz file
        Returns:
            Deserialized snapshot data
        """
        # Decompress and load JSON
        # Return snapshot data


class SnapshotScheduler:
    """Decides when to take snapshots based on configuration."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.last_full_snapshot = None
        self.last_light_snapshot_step = 0
    
    def should_snapshot(self,
                       step: int,
                       event_type: str,
                       context: Optional[Dict] = None) -> Tuple[bool, str, str]:
        """
        Determine if snapshot should be taken.
        
        Args:
            step: Current step number
            event_type: Type of event (STAGE_START, MILESTONE, ERROR, etc.)
            context: Additional context
        Returns:
            (should_snapshot, snapshot_type, reason)
        """
        # Check config rules:
        # 1. Always on full_snapshot_points (initial, final, stage boundaries)
        # 2. Every N steps if light_snapshots_enabled
        # 3. On specific milestones (defect count reached, etc.)
        # 4. On errors if configured
        # Return (True/False, "full"/"light", reason_string)
```

### **C. `logging.py` - Logging System**

```python
"""
Complete logging system with verbosity filtering and machine-readable events.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, TextIO
from enum import Enum

class EventType(Enum):
    """Predefined event types for structured logging."""
    RUN_START = "run_start"
    RUN_END = "run_end"
    STAGE_START = "stage_start"
    STAGE_END = "stage_end"
    DEFECT_CREATE_ATTEMPT = "defect_create_attempt"
    DEFECT_CREATED = "defect_created"
    FLIP_ATTEMPT = "flip_attempt"
    FLIP_ACCEPT = "flip_accept"
    FLIP_REJECT = "flip_reject"
    ENERGY_CHECK = "energy_check"
    ENERGY_DRIFT = "energy_drift"
    ADJACENCY_CHECK = "adjacency_check"
    ADJACENCY_ERROR = "adjacency_error"
    MILESTONE = "milestone"
    ERROR = "error"
    WARNING = "warning"


class DualLogger:
    """Manages console and file logging with verbosity control."""
    
    def __init__(self,
                 run_dir: Path,
                 console_verbosity: int,
                 file_verbosity: int,
                 config: Dict[str, Any]):
        """
        Initialize logging system.
        
        Args:
            run_dir: Experiment directory
            console_verbosity: 1 or 2 for console output
            file_verbosity: 1 or 2 for file output
            config: Logging configuration
        """
        # Open file handles:
        # - console.log (verbosity 1)
        # - detailed.log (verbosity 2)
        # - errors.log (all errors)
        # - events.jsonl (machine-readable)
        self.console_file: TextIO
        self.detailed_file: TextIO
        self.errors_file: TextIO
        self.events_file: TextIO
        self.filter = VerbosityFilter(config)
    
    def log(self,
            message: str,
            level: int,
            event_type: Optional[EventType] = None,
            details: Optional[Dict] = None) -> None:
        """
        Main logging method.
        
        Args:
            message: Human-readable message
            level: 1 (stage-level) or 2 (detailed)
            event_type: EventType enum value
            details: Structured data for machine logging
        """
        # 1. Format timestamp
        # 2. Write to console if level <= console_verbosity
        # 3. Write to detailed.log if level <= file_verbosity
        # 4. Write to events.jsonl if event_type provided
        # 5. Write to errors.log if event_type == EventType.ERROR
    
    def log_error(self,
                  error_type: str,
                  message: str,
                  context: Optional[Dict] = None,
                  recoverable: bool = True) -> None:
        """
        Special handling for errors.
        """
        # Always log to errors.log
        # Also log to console with [ERROR] prefix
        # Include stack trace if available


class EventLogger:
    """Writes structured events for programmatic analysis."""
    
    def __init__(self, events_file: Path):
        self.events_file = events_file
    
    def log_event(self,
                  event_type: EventType,
                  data: Dict[str, Any],
                  step: Optional[int] = None,
                  timestamp: Optional[float] = None) -> None:
        """
        Write structured event to JSONL file.
        
        Args:
            event_type: EventType enum
            data: Event-specific data
            step: Current simulation step
            timestamp: Event timestamp (defaults to now)
        """
        # Create event dict with metadata
        # Write as JSON line to events.jsonl


class VerbosityFilter:
    """Filters events based on configuration."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def should_log(self,
                   event_type: Optional[EventType],
                   level: int,
                   details: Optional[Dict] = None) -> bool:
        """
        Determine if event should be logged.
        
        Args:
            event_type: Type of event
            level: Verbosity level (1 or 2)
            details: Event details for filtering
        Returns:
            True if should log to detailed.log
        """
        # Rules:
        # 1. Always log errors (EventType.ERROR)
        # 2. Log level 1 events to console.log
        # 3. Log level 2 events if matches filters:
        #    - energy_change > threshold
        #    - class_changes = True
        #    - near_obstacle = True
        #    - milestone_steps list
```

### **D. `metrics.py` - Metrics Collection**

```python
"""
Metrics collection and aggregation system.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class TimeSeriesPoint:
    """Single time-series data point."""
    step: int
    timestamp: float
    energy_total: float
    defect_count: int
    acceptance_rate: Optional[float] = None
    temperature: Optional[float] = None
    # Additional metrics as needed


class MetricsCollector:
    """Collects and stores time-series metrics."""
    
    def __init__(self,
                 run_dir: Path,
                 config: Dict[str, Any]):
        self.run_dir = run_dir
        self.config = config
        self.buffer: List[Dict[str, Any]] = []
        self.buffer_size = config.get('metrics_buffer_size', 100)
        self.time_series_file = run_dir / "metrics_timeseries.jsonl"
        self.aggregates_file = run_dir / "metrics_aggregates.json"
    
    def record(self,
               step: int,
               metrics: Dict[str, Any]) -> None:
        """
        Record metrics for current step.
        
        Args:
            step: Current step number
            metrics: Dictionary of metrics
        """
        # 1. Add step and timestamp
        # 2. Compute spatial metrics if configured
        # 3. Add to buffer
        # 4. Flush if buffer full
    
    def flush(self) -> None:
        """Write buffered metrics to disk."""
        # Append to JSONL file
        # Clear buffer
    
    def compute_spatial_metrics(self,
                               tiling_state: Dict[str, Any],
                               step: int) -> Dict[str, Any]:
        """
        Compute spatial metrics for obstacle studies.
        
        Args:
            tiling_state: Current tiling state
            step: Current step
        Returns:
            Dictionary with spatial breakdown
        """
        # Bin tiles by distance from nearest obstacle
        # Compute metrics per bin:
        # - defect density
        # - average energy
        # - healing efficiency
        # Return spatial metrics dict
    
    def write_final_aggregates(self, aggregates: Dict[str, Any]) -> None:
        """
        Write aggregate metrics to file.
        
        Args:
            aggregates: Dictionary of aggregate metrics
        """
        # Write to metrics_aggregates.json
        # Include healing efficiency, total energy change, etc.
```

### **E. `analysis.py` - Post-Run Analysis**

```python
"""
Post-experiment analysis and visualization generation.
"""

import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, Any, List
import json

class PlotGenerator:
    """Generates plots from experiment data (post-run)."""
    
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.plot_dir = run_dir / "analysis"
        self.plot_dir.mkdir(exist_ok=True)
    
    def generate_all_plots(self,
                          config: Dict[str, Any]) -> List[Path]:
        """
        Generate standard set of plots.
        
        Args:
            config: Plot configuration
        Returns:
            List of paths to generated plot files
        """
        # 1. Load metrics from files
        # 2. Generate each plot type:
        #    - Healing dashboard (4-panel)
        #    - Defect creation timeline
        #    - Spatial healing efficiency
        #    - Temperature effect on acceptance
        # 3. Save to analysis/ directory
        # 4. Return list of file paths
    
    def _plot_healing_dashboard(self,
                               metrics: Dict[str, Any],
                               output_path: Path) -> None:
        """
        Create multi-panel healing progress dashboard.
        
        Args:
            metrics: Loaded metrics data
            output_path: Where to save the plot
        """
        # Subplots:
        # 1. Energy vs steps (line plot)
        # 2. Defect count vs steps (line plot)
        # 3. Acceptance rate vs temperature (scatter)
        # 4. Final defect spatial distribution (heatmap)


class SummaryGenerator:
    """Creates human-readable experiment summary."""
    
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.summary_file = run_dir / "summary.txt"
    
    def generate_summary(self,
                        config: Dict[str, Any],
                        status: Dict[str, Any],
                        metrics: Dict[str, Any]) -> str:
        """
        Generate one-page text summary.
        
        Args:
            config: Experiment configuration
            status: Experiment status (from status.json)
            metrics: Aggregate metrics
        Returns:
            Formatted summary text
        """
        # Format includes:
        # - Experiment parameters
        # - Key results (healing efficiency, etc.)
        # - Status (success/failure)
        # - Runtime statistics
        # - Recommendations
        # Save to summary.txt
        # Return formatted string
```

### **F. `config_schema.py` - Configuration Validation**

```python
"""
Configuration schema and validation for output system.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import tomli

@dataclass
class OutputConfig:
    """Complete output system configuration."""
    
    # Experiment
    experiment_type: str = "healing"
    name_suffix: str = ""
    base_dir: str = "data/experiments"
    
    # Logging
    console_verbosity: int = 1
    file_verbosity: int = 2
    log_interval: int = 10
    
    # Verbosity 2 filters
    energy_change_threshold: float = 0.5
    log_class_changes: bool = True
    log_boundary_transitions: bool = True
    log_near_obstacle_events: bool = True
    milestone_steps: List[int] = field(default_factory=lambda: [10, 50, 100, 500, 1000])
    
    # Snapshots
    full_snapshots: List[str] = field(default_factory=lambda: ["initial", "after_defects", "final"])
    light_snapshot_interval: int = 50  # Steps between light snapshots
    light_snapshots_enabled: bool = True
    compression: bool = True
    
    # Metrics
    record_spatial_metrics: bool = True
    obstacle_distance_bins: List[int] = field(default_factory=lambda: [0, 2, 5, 10])
    metrics_buffer_size: int = 100
    
    # Error checks
    local_checks_every_flip: bool = True
    global_checks_interval: int = 200
    check_energy_drift: bool = True
    check_adjacency: bool = True
    
    # Analysis
    generate_plots_after: bool = True
    plot_dpi: int = 300
    
    @classmethod
    def from_toml(cls, toml_path: str) -> 'OutputConfig':
        """Load configuration from TOML file."""
        with open(toml_path, 'rb') as f:
            data = tomli.load(f)
        return cls(**data)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return self.__dict__.copy()
```

## **3. INTEGRATION WITH EXISTING CODE**

### **Updated `03_run_healing_test.py` Structure:**

```python
#!/usr/bin/env python3
"""
Healing experiment script with new output system.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.output.experiment_output import ExperimentOutput, ExperimentConfig
from src.output.config_schema import OutputConfig
from src.simulation.mc_engine import MonteCarloEngine
from src.simulation.flip_engine import FlipEngine
from src.energy.widom_inspired_energy import WidomInspiredEnergy

def main():
    # 1. Parse command line arguments
    args = parse_arguments()
    
    # 2. Load configuration
    if args.config:
        config = OutputConfig.from_toml(args.config)
    else:
        # Use defaults with command line overrides
        config = OutputConfig(
            name_suffix=args.experiment_suffix,
            console_verbosity=args.verbosity,
            light_snapshot_interval=args.snapshot_interval,
            light_snapshots_enabled=not args.full_snapshots
        )
    
    # 3. Initialize output system
    output = ExperimentOutput(config)
    
    # 4. Load tiling
    tiling = load_tiling(args.input)
    output.log(f"Loaded tiling with {len(tiling['tiles'])} tiles", level=1)
    
    # 5. Take initial snapshot
    output.take_snapshot(tiling, reason="initial", force_full=True)
    
    # 6. Run defect creation
    output.log_stage_start("defect_creation", 
                          {"target_defects": args.target_defects})
    
    for attempt in range(max_attempts):
        # ... defect creation logic ...
        
        # Log interesting attempts
        if success or attempt % 10 == 0:
            output.log(f"Attempt {attempt}: {'success' if success else 'failed'}",
                      level=2 if success else 1,
                      event_type="DEFECT_CREATE_ATTEMPT")
        
        # Record metrics
        output.record_metrics(step=attempt,
                             metrics={"defects": current_defects})
    
    output.log_stage_end("defect_creation",
                        {"defects_created": final_defects})
    
    # 7. Run healing
    output.log_stage_start("healing",
                          {"temperature_schedule": temp_schedule})
    
    for step in range(total_steps):
        # ... MC healing logic ...
        
        # Log interesting flips (filtered by verbosity)
        if flip_accepted and interesting:
            output.log(f"Step {step}: Flip accepted ΔE={delta_e:.3f}",
                      level=2,
                      event_type="FLIP_ACCEPT",
                      details={"cluster": cluster_ids, "delta_e": delta_e})
        
        # Record metrics every step
        output.record_metrics(
            step=step,
            metrics={
                "energy": current_energy,
                "defects": defect_count,
                "temperature": current_temp,
                "acceptance_rate": acceptance_rate
            }
        )
    
    output.log_stage_end("healing",
                        {"final_defects": final_defects})
    
    # 8. Finalize
    output.finalize(success=True)
    
    print(f"Experiment completed. Results in: {output.run_dir}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## **4. KEY DESIGN DECISIONS**

### **1. Flat Structure Benefits:**
- **Easier navigation**: All output logic in one place
- **Simplified imports**: `from src.output import ExperimentOutput`
- **Cohesive modules**: Related functionality grouped logically
- **Maintainable**: Clear separation of concerns without deep hierarchy

### **2. Configuration Strategy:**
- **Primary**: TOML files (existing pattern in your project)
- **Secondary**: Python dataclass with sensible defaults
- **Override**: Command line arguments for quick adjustments

### **3. Snapshot Strategy (Your Suggestion):**
```python
# In config:
light_snapshots_enabled = true  # Use light snapshots for intervals
light_snapshot_interval = 50    # Steps between light snapshots
full_snapshots = ["initial", "after_defects", "final"]  # Always full

# In code:
if config.light_snapshots_enabled and should_take_interval_snapshot(step):
    snapshot_type = "light"
else:
    snapshot_type = "full"
```

### **4. Error Detection Integration:**
```python
# In healing engines, add error detection:
def check_for_errors(tiling, output):
    # Local checks (cheap)
    if energy_drift > threshold:
        output.record_error("energy_drift", 
                          f"Energy drift detected: {energy_drift}",
                          {"step": current_step},
                          recoverable=True)
    
    # Global checks (expensive, less frequent)
    if step % config.global_checks_interval == 0:
        if adjacency_inconsistency:
            output.record_error("adjacency_inconsistency",
                              "Graph-geometry mismatch",
                              recoverable=False)
```

## **5. IMPLEMENTATION PRIORITY**

### **Phase 1 (Week 1): Core Foundation**
1. `config_schema.py` - Configuration dataclass
2. `managers.py` - RunManager, StatusManager, SnapshotManager
3. `logging.py` - Basic DualLogger without filtering

### **Phase 2 (Week 2): Integration**
1. `experiment_output.py` - Main orchestrator
2. `metrics.py` - Basic metrics collection
3. Update `03_run_healing_test.py` to use new system

### **Phase 3 (Week 3): Advanced Features**
1. `logging.py` - Add verbosity filtering
2. `metrics.py` - Add spatial metrics
3. `analysis.py` - Plot generation

### **Phase 4 (Week 4): Polish**
1. Error detection integration
2. Performance optimization
3. Documentation and examples

## **6. VALIDATION CRITERIA**

The system is successful if:

1. **Single command**: `python 03_run_healing_test.py` produces organized output
2. **Verbosity works**: Console shows stage-level, files have details
3. **Snapshots usable**: Can reload and plot any snapshot
4. **Metrics complete**: Can compute healing efficiency from metrics.json
5. **Performance**: <5% overhead compared to current version
6. **Extensible**: Easy to add new metrics or plot types

---

**Ready to start implementation?** I'll begin with `config_schema.py` and `managers.py` to establish the foundation, then we can integrate with your existing code.



==========================================================================================
some key suggsetion were also given and we were going to see if they really match our need 
==========================================================================================


P0 — Fix these before you write the full logical flow
1) You currently have two config types (ExperimentConfig and OutputConfig)

That will drift and become a bug source.

Refinement: pick one canonical config object:

keep OutputConfig (schema + defaults) as the single source of truth

ExperimentOutput.__init__ accepts OutputConfig | dict and normalizes internally

Also: your ExperimentConfig uses experiment_type/base_dir/verbosity but OutputConfig also does. Duplication guaranteed.

2) Your from_toml() is wrong for nested TOML

Right now you do return cls(**data). But your TOML design is sectioned like:

[output]
[logging]
[snapshots]
...


So data will be nested dicts, and cls(**data) will fail (or worse: silently ignore fields if you flatten later inconsistently).

Refinement: decide now whether:

(A) your dataclass matches nested TOML sections (recommended), OR

(B) you flatten TOML into one dict before constructing the dataclass

If you don’t lock this now, config handling becomes brittle across scripts.

3) Run ID allocator needs a cluster-safe mode

You correctly plan a lock + scan, but on HPC you often run multiple jobs concurrently; scanning directories + incrementing is okay only if the lock is truly shared across processes on the same filesystem.

Refinement: add support for:

run_id override (passed by batch script)

OR a manifest/allocator file (append-only) updated under lock

Also: your allocator says it handles patterns like healing_run_001, etc — good — but ensure it won’t miss your existing healing_base_run_001 style.

4) Light snapshot definition: you’re missing the “canvas”

Your current light snapshot proposes storing positions with energies only “if changed” or “if energy > threshold”. That can make plots impossible or misleading because you lose the full spatial support.

Refinement: add a geometry artifact saved once per run:

geometry.json.gz: for all tiles {id, x, y} (optionally vertices)
Then each light snapshot can be sparse and still render correctly.

This is the single best improvement for disk + visualization consistency.

P1 — Strongly recommended tweaks
5) Make event_type an Enum everywhere (not sometimes string)

Right now ExperimentOutput.log(... event_type: Optional[str]) conflicts with logging.py where you have EventType(Enum). Mixing string/Enum will create subtle filter bugs.

Refinement: normalize on EventType | None everywhere.


8) Keep src/output dependency-free

Your current design is compatible with this, but be strict:

Rule: output code must not import energy / mc / healing modules.
It should accept plain dicts / primitives only.

This prevents circular imports later.

9) analysis.py should be “post-run only”

You already want that. It’s fine for finalize() to optionally call plot generation, but for batch sweeps it’s better to run analysis as a separate script.

So keep:

generate_plots_after default true for local interactive runs

easy CLI --no-plots for cluster







=============================
take these comment ( if needed ) into consideration, 

provide again ( only the same thing the function signatures and behaviors in the fixed way, 

( the same one you lastly generate, but taking care of these fixes)

the same follow do not change only the minimal change, for the fixes, then plan we created was perfect and match my preferences perfectly, 