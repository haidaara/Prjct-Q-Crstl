# src/obstacle_healing/metrics.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class RunMetrics:
    """Minimal time-series metrics for one obstacle-healing run."""

    steps: List[int] = field(default_factory=list)
    temperatures: List[float] = field(default_factory=list)
    energies: List[float] = field(default_factory=list)
    defects: List[int] = field(default_factory=list)
    defect_density: List[float] = field(default_factory=list)
    acceptance_rates: List[float] = field(default_factory=list)  # 0..1
    energy_drifts: List[float] = field(default_factory=list)     # absolute drift

    stage_transitions: List[Dict[str, Any]] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)

    def add_stage_transition(self, *, step: int, T: float, name: str, steps_in_stage: int) -> None:
        self.stage_transitions.append({
            "step": int(step),
            "T": float(T),
            "name": str(name),
            "steps_in_stage": int(steps_in_stage),
        })

    def record(
        self, *,
        step: int, T: float, energy: float,
        defects: int, defect_density: float,
        acceptance_rate: float, energy_drift: float
    ) -> None:
        self.steps.append(int(step))
        self.temperatures.append(float(T))
        self.energies.append(float(energy))
        self.defects.append(int(defects))
        self.defect_density.append(float(defect_density))
        self.acceptance_rates.append(float(acceptance_rate))
        self.energy_drifts.append(float(energy_drift))

    def finalize_summary(
        self, *,
        baseline_defects: int, damaged_defects: int, final_defects: int,
        baseline_energy: float, damaged_energy: float, final_energy: float,
        drift_max: float, measurement_tiles: int,
        total_mc_steps: int, damage_steps: int
    ) -> None:
        initial = max(int(damaged_defects), 1)
        removed = int(damaged_defects) - int(final_defects)
        efficiency = removed / initial

        self.summary = {
            "baseline_defects": int(baseline_defects),
            "damaged_defects": int(damaged_defects),
            "final_defects": int(final_defects),
            "defect_reduction": removed,
            "healing_efficiency": efficiency,
            "baseline_energy": float(baseline_energy),
            "damaged_energy": float(damaged_energy),
            "final_energy": float(final_energy),
            "energy_reduction": float(damaged_energy - final_energy),
            "energy_drift_max": float(drift_max),
            "measurement_tiles": int(measurement_tiles),
            "total_mc_steps": int(total_mc_steps),
            "damage_steps": int(damage_steps),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "series": {
                "steps": self.steps,
                "temperatures": self.temperatures,
                "energies": self.energies,
                "defects": self.defects,
                "defect_density": self.defect_density,
                "acceptance_rates": self.acceptance_rates,
                "energy_drifts": self.energy_drifts,
            },
            "stage_transitions": self.stage_transitions,
            "summary": self.summary,
        }
