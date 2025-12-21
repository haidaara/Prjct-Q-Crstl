#!/usr/bin/env python3
"""System diagnostic (non-fatal).

Checks:
- can import project modules
- base tiling file loads
- prints a few quick stats
"""
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling

REQUIRED_PATHS = [
    "data/processed/penrose_tiling_energy_initialized.json",
    "configs/phase1_baseline.toml",
]


def main() -> int:
    print("🧰 SYSTEM DIAGNOSTIC")
    print("=" * 60)

    missing = []
    for rel in REQUIRED_PATHS:
        if not (project_root / rel).exists():
            missing.append(rel)
    if missing:
        print("⚠️  Missing expected files:")
        for m in missing:
            print(f"   - {m}")
    else:
        print("✅ Core files present")

    try:
        tiling = load_tiling()
    except Exception as e:
        print(f"❌ Could not load base tiling: {e}")
        return 1

    tiles = tiling.get("tiles", [])
    adj = tiling.get("adjacency_graph", {})
    removed = sum(1 for t in tiles if t.get("removed", False))
    flippable = sum(1 for t in tiles if t.get("flippable", False) and not t.get("removed", False))
    seed = sum(1 for t in tiles if t.get("growth_status") == "seed" and not t.get("removed", False))

    print(f"Tiles: {len(tiles)} (removed: {removed})")
    print(f"Adjacency keys: {len(adj)}")
    print(f"Flippable active tiles: {flippable}")
    print(f"Seed tiles: {seed}")

    print("✅ Diagnostic complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
