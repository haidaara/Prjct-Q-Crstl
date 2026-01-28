# scripts/experiments/03_obstacle_healing.py
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]  # quasi-phason/
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore

from src.obstacle_healing.experiment import ObstacleHealingExperiment


def load_toml(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config not found: {p}")
    with open(p, "rb") as f:
        return tomllib.load(f)


def main() -> None:
    ap = argparse.ArgumentParser(description="Obstacle healing experiment (damage → anneal → snapshots)")
    ap.add_argument("--config", required=True, help="Path to configs/obstacle_healing.toml")
    ap.add_argument("--input", default=None, help="Override [run].input")
    ap.add_argument("--out", default=None, help="Override [run].output_dir")
    ap.add_argument("--run-name", default=None, help="Override [run].run_name")
    args = ap.parse_args()

    cfg = load_toml(args.config)

    run_cfg = cfg.get("run", {}) or {}
    input_path = args.input or run_cfg.get("input")
    output_dir = args.out or run_cfg.get("output_dir")
    run_name = args.run_name or run_cfg.get("run_name", "obstacle_healing_run")

    if not input_path:
        raise ValueError("Missing [run].input in TOML (or pass --input)")
    if not output_dir:
        raise ValueError("Missing [run].output_dir in TOML (or pass --out)")

    exp = ObstacleHealingExperiment(
        input_path=str(input_path),
        output_dir=str(output_dir),
        run_name=str(run_name),
        cfg=cfg,
    )
    exp.run()


if __name__ == "__main__":
    main()
