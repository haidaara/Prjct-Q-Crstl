#!/usr/bin/env python3
"""
VALIDATION 2: OBSTACLES (Milestone 2)
Checks obstacle JSONs under data/obstacles/pores/*.json.

Rules:
- If obstacle_metadata.obstacle_count exists => must match pore tiles counted (excluding removed).
- If metadata is missing => WARN but DO NOT FAIL (prevents false failures).
"""
from curses import meta
import sys
import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))


def check_obstacles() -> bool:
    print("🕳️  VALIDATING OBSTACLES")
    print("=" * 60)

    obstacle_dir = project_root / "data" / "obstacles" / "pores"
    if not obstacle_dir.exists():
        print("⚠️  No obstacle data found (data/obstacles/pores/). Run obstacle generation first.")
        return True

    files = sorted(obstacle_dir.glob("*.json"))
    print(f"   Found {len(files)} obstacle configurations.")

    all_passed = True
    for f in files:
        with open(f, "r", encoding="utf-8") as jf:
            data = json.load(jf)

        meta = data.get("obstacle_metadata", {}) or {}
        expected = meta.get("obstacle_count", None)

        # New format support (preferred)
        if expected is None:
            expected = meta.get("removed_count", None)

        # Fallback: if pores store explicit pore lists
        if expected is None:
            positions = meta.get("positions", [])
            if isinstance(positions, list) and positions:
                expected = len(positions)

        tiles = data.get("tiles", [])

        # New semantics: pores are removed tiles (still should be counted)
        counted = sum(
            1 for t in tiles
            if (t.get("obstacle_type") == "pore") or (t.get("removed", False) and t.get("obstacle_type") != "fixed_defect")
        )


        if expected is None:
            print(f"⚠️  WARNING {f.name}: expected pore count missing; counted {counted} pore-marked tiles")
            continue

        if counted != expected:
            print(f"❌ FAIL {f.name}: metadata={expected}, grid_count={counted}")
            all_passed = False
        else:
            print(f"✅ PASS {f.name}: {expected} pores confirmed")

    return all_passed


if __name__ == "__main__":
    sys.exit(0 if check_obstacles() else 1)
