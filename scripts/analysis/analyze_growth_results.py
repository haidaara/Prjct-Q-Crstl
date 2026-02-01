#!/usr/bin/env python3
"""
Analyze growth experiment outputs written by run_growth_experiment.py.

Expected default input:
  data/growth_experiments/growth_experiment_*.json

Each JSON typically contains:
  - metadata.timestamp
  - config (growth + monte_carlo)
  - growth_steps: list of per-step metrics

Outputs (default):
  results/analysis/growth_<file_stem>.png
  results/analysis/growth_<file_stem>.csv

This is a plotting/summary script only; it does not touch simulation code.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _safe_float(x, default=None) -> Optional[float]:
    try:
        return float(x)
    except Exception:
        return default


def load_json(fp: Path) -> Dict[str, Any]:
    with open(fp, "r", encoding="utf-8") as f:
        return json.load(f)


def select_file(input_dir: Path, pattern: str, latest: bool) -> Optional[Path]:
    files = list(input_dir.glob(pattern))
    if not files:
        return None
    if latest:
        return max(files, key=lambda p: p.stat().st_mtime)
    return sorted(files)[0]


def plot_series(steps: List[Dict[str, Any]], out_png: Path, title: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    xs = [s.get("step") for s in steps]
    acc = [_safe_float(s.get("acceptance_rate"), None) for s in steps]
    defects = [s.get("defect_count") for s in steps]
    energy = [_safe_float(s.get("total_energy"), None) for s in steps]
    active = [s.get("active_tiles") for s in steps]

    fig = plt.figure(figsize=(10, 10))

    ax1 = fig.add_subplot(4, 1, 1)
    ax1.plot(xs, active, marker="o")
    ax1.set_ylabel("Active tiles")
    ax1.set_title(title)

    ax2 = fig.add_subplot(4, 1, 2)
    ax2.plot(xs, acc, marker="o")
    ax2.set_ylabel("Acceptance rate")

    ax3 = fig.add_subplot(4, 1, 3)
    ax3.plot(xs, defects, marker="o")
    ax3.set_ylabel("Defect count")

    ax4 = fig.add_subplot(4, 1, 4)
    ax4.plot(xs, energy, marker="o")
    ax4.set_ylabel("Total energy")
    ax4.set_xlabel("Step")

    fig.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


def write_csv(steps: List[Dict[str, Any]], out_csv: Path) -> None:
    # Collect union of keys (stable order where possible)
    preferred = [
        "step", "active_tiles", "accepted_flips", "total_flips",
        "acceptance_rate", "defect_count",
        "total_energy", "energy_change",
    ]
    keys = set()
    for s in steps:
        keys.update(s.keys())
    fieldnames = [k for k in preferred if k in keys] + [k for k in sorted(keys) if k not in preferred]

    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for s in steps:
            w.writerow({k: s.get(k) for k in fieldnames})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="data/growth_experiments", help="Directory containing experiment JSON files.")
    ap.add_argument("--pattern", default="growth_experiment_*.json", help="Glob pattern (default growth_experiment_*.json).")
    ap.add_argument("--file", default="", help="Explicit file path (overrides --dir/--pattern).")
    ap.add_argument("--latest", action="store_true", help="Use the most recently modified file.")
    ap.add_argument("--outdir", default="results/analysis", help="Output directory for plots/tables.")
    args = ap.parse_args()

    if args.file:
        fp = Path(args.file)
        if not fp.is_absolute():
            fp = PROJECT_ROOT / fp
    else:
        input_dir = PROJECT_ROOT / args.dir
        if not input_dir.exists():
            print(f"❌ Input dir not found: {input_dir}")
            return 1
        fp = select_file(input_dir, args.pattern, args.latest)

    if fp is None or not fp.exists():
        print("   No matching growth experiment files found.")
        return 0

    data = load_json(fp)
    steps = data.get("growth_steps", []) or []
    if not steps:
        print(f"   File has no growth_steps: {fp}")
        return 1

    # quick summary
    first = steps[0]
    last = steps[-1]
    print("\n=== Growth experiment summary ===")
    print(f"File: {fp}")
    print(f"Steps: {len(steps)}")
    print(f"Active tiles: {first.get('active_tiles')} -> {last.get('active_tiles')}")
    print(f"Acceptance rate (last): {last.get('acceptance_rate')}")
    print(f"Defects: {first.get('defect_count')} -> {last.get('defect_count')}")
    print(f"Energy: {first.get('total_energy')} -> {last.get('total_energy')}")

    outdir = PROJECT_ROOT / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)
    stem = fp.stem

    out_png = outdir / f"growth_{stem}.png"
    plot_series(steps, out_png, title=f"Growth results: {stem}")
    print(f"   Wrote plot: {out_png}")

    out_csv = outdir / f"growth_{stem}.csv"
    write_csv(steps, out_csv)
    print(f"   Wrote CSV: {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
