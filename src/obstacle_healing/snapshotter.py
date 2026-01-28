# src/obstacle_healing/snapshotter.py
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class SnapshotIndexEntry:
    step: int
    label: str
    filename: str
    temperature: float


@dataclass
class Snapshotter:
    run_dir: Path
    snapshots_subdir: str = "snapshots"
    index: List[SnapshotIndexEntry] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.run_dir = Path(self.run_dir)
        (self.run_dir / self.snapshots_subdir).mkdir(parents=True, exist_ok=True)

    def save_snapshot(
        self, *,
        tiling: Dict,
        step: int,
        label: str,
        temperature: float,
        metrics: Optional[Dict[str, Any]] = None
    ) -> str:
        fname = f"snapshot_{step:04d}_{label}.json"
        path = self.run_dir / self.snapshots_subdir / fname

        payload = {
            "meta": {
                "run_id": str(tiling.get("metadata", {}).get("run_id", "UNKNOWN_RUN")),
                "step": int(step),
                "label": str(label),
                "temperature": float(temperature),
            },
            "metrics": metrics or {},
            "obstacle_metadata": tiling.get("obstacle_metadata"),
            "tiling": tiling,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        self.index.append(SnapshotIndexEntry(
            step=int(step),
            label=str(label),
            filename=str(path.relative_to(self.run_dir)),
            temperature=float(temperature),
        ))
        return str(path)

    def write_index(self) -> str:
        path = self.run_dir / "snapshot_index.json"
        data = [{"step": e.step, "label": e.label, "temperature": e.temperature, "file": e.filename} for e in self.index]
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"snapshots": data}, f, ensure_ascii=False, indent=2)
        return str(path)
