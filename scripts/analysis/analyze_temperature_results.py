#!/usr/bin/env python3
"""
Analyze temperature sweep experiment outputs written by growth / temperature sweep runners.

Expected input files (default):
  data/growth_experiments/temp_sweep_T*.json

Each JSON typically contains:
  - config.monte_carlo.temperature
  - growth_steps: [{acceptance_rate, defect_count, total_energy, ...}, ...]

Outputs:
  - results/analysis/temperature_sweep_summary.csv
  - results/analysis/temperature_sweep.png

This script is intentionally tolerant: if some fields are missing, it will still summarize what it can.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _get_nested(d: Dict[str, Any], path: List[str], default=None):
    cur: Any = d
    for k in path:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def _safe_float(x, default=None) -> Optional[float]:
    try:
        return float(x)
    except Exception:
        return default


def load_results_files(input_dir: Path, pattern: str) -> List[Path]:
    files = sorted(input_dir.glob(pattern))
    return files


def parse_one_file(fp: Path) -> Dict[str, Any]:
    with open(fp, "r", encoding="utf-8") as f:
        data = json.load(f)

    T = _get_nested(data, ["config", "monte_carlo", "temperature"], None)
    T = _safe_float(T, None)

    steps = data.get("growth_steps", []) or []
    acc = [_safe_float(s.get("acceptance_rate", None), None) for s in steps]
    acc = [a for a in acc if a is not None]

    defects = [s.get("defect_count", None) for s in steps]
    defects = [int(d) for d in defects if d is not None]

    energies = [_safe_float(s.get("total_energy", None), None) for s in steps]
    energies = [e for e in energies if e is not None]

    out = {
        "file": fp.name,
        "temperature": T,
        "n_steps": len(steps),
        "acceptance_mean": (sum(acc) / len(acc)) if acc else None,
        "defects_start": defects[0] if defects else None,
        "defects_end": defects[-1] if defects else None,
        "energy_start": energies[0] if energies else None,
        "energy_end": energies[-1] if energies else None,
    }

    if out["defects_start"] is not None and out["defects_end"] is not None:
        healed = out["defects_start"] - out["defects_end"]
        out["healed"] = healed
        out["heal_efficiency"] = healed / max(1, out["defects_start"])
    else:
        out["healed"] = None
        out["heal_efficiency"] = None

    return out


def plot_summary(rows: List[Dict[str, Any]], out_png: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Keep only rows with temperature
    rows = [r for r in rows if r.get("temperature") is not None]
    rows.sort(key=lambda r: r["temperature"])

    T = [r["temperature"] for r in rows]
    acc = [r["acceptance_mean"] for r in rows]
    eff = [r["heal_efficiency"] for r in rows]
    d0 = [r["defects_start"] for r in rows]
    d1 = [r["defects_end"] for r in rows]

    fig = plt.figure(figsize=(10, 8))

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(T, acc, marker="o")
    ax1.set_xlabel("Temperature")
    ax1.set_ylabel("Mean acceptance rate")
    ax1.set_title("Temperature sweep: acceptance")

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(T, eff, marker="o", label="healing efficiency")
    ax2.plot(T, d0, marker="x", label="defects start")
    ax2.plot(T, d1, marker="x", label="defects end")
    ax2.set_xlabel("Temperature")
    ax2.set_ylabel("Defects / Efficiency")
    ax2.set_title("Temperature sweep: defects / healing")
    ax2.legend()

    fig.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="data/growth_experiments", help="Directory containing experiment JSON files.")
    ap.add_argument("--pattern", default="temp_sweep_T*.json", help="Glob pattern for files.")
    ap.add_argument("--outdir", default="results/analysis", help="Output directory for plots/tables.")
    args = ap.parse_args()

    input_dir = PROJECT_ROOT / args.dir
    if not input_dir.exists():
        print(f"   Input dir not found: {input_dir}")
        return 1

    files = load_results_files(input_dir, args.pattern)
    if not files:
        print(f"    No files found in {input_dir} matching {args.pattern}")
        return 0

    rows = [parse_one_file(fp) for fp in files]

    # Print summary
    rows_with_T = [r for r in rows if r.get("temperature") is not None]
    rows_with_T.sort(key=lambda r: r["temperature"])
    print("\n=== Temperature sweep summary ===")
    for r in rows_with_T:
        print(
            f"T={r['temperature']:.3f}  "
            f"acc={r['acceptance_mean'] if r['acceptance_mean'] is not None else 'NA'}  "
            f"defects: {r['defects_start']} -> {r['defects_end']}  "
            f"eff={r['heal_efficiency'] if r['heal_efficiency'] is not None else 'NA'}  "
            f"({r['file']})"
        )

    outdir = PROJECT_ROOT / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    # Write CSV
    out_csv = outdir / "temperature_sweep_summary.csv"
    fieldnames = [
        "file", "temperature", "n_steps",
        "acceptance_mean",
        "defects_start", "defects_end",
        "healed", "heal_efficiency",
        "energy_start", "energy_end",
    ]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in fieldnames})
    print(f"\n   Wrote CSV: {out_csv}")

    # Plot
    out_png = outdir / "temperature_sweep.png"
    plot_summary(rows, out_png)
    print(f"    Wrote plot: {out_png}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
