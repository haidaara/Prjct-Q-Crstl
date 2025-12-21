#!/usr/bin/env python3
"""
VALIDATION 1: TILING STRUCTURE (Milestone 1)
Checks:
- adjacency_graph exists and is parseable
- tile id == index
- neighbor id range
- no self-neighbors
- symmetry (A->B implies B->A), optionally ignoring removed endpoints
- no orphan active tiles
"""
import sys
from pathlib import Path
from collections import Counter

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.script_utils import load_tiling


def _to_int(x):
    if isinstance(x, int):
        return x
    if isinstance(x, str):
        return int(x.strip())
    raise TypeError(f"Unsupported id type: {type(x)}")


def check_structure(ignore_removed_in_symmetry: bool = True) -> bool:
    print("🏗️  VALIDATING TILING STRUCTURE")
    print("=" * 60)

    tiling = load_tiling()
    tiles = tiling["tiles"]
    adj = tiling.get("adjacency_graph", {})
    num_tiles = len(tiles)

    if not adj:
        print("❌ FAIL: adjacency_graph is empty or missing.")
        return False

    print("1) ID consistency (id == index)")
    for i, t in enumerate(tiles):
        if t.get("id") != i:
            print(f"❌ FAIL: tiles[{i}].id = {t.get('id')} (expected {i})")
            return False

    print("2) Parse adjacency + invariants")
    norm_adj = {}
    for k, neighbors in adj.items():
        try:
            kid = _to_int(k)
            nlist = [_to_int(n) for n in neighbors]
        except Exception as e:
            print(f"❌ FAIL: invalid adjacency entry for key={k!r}: {e}")
            return False

        if not (0 <= kid < num_tiles):
            print(f"❌ FAIL: adjacency key out of range: {kid}")
            return False

        norm_adj[kid] = nlist

    for a, nlist in norm_adj.items():
        for b in nlist:
            if not (0 <= b < num_tiles):
                print(f"❌ FAIL: neighbor id out of range: {a} -> {b}")
                return False
            if a == b:
                print(f"❌ FAIL: self-neighbor detected: tile {a} lists itself")
                return False

            if ignore_removed_in_symmetry and (tiles[a].get("removed", False) or tiles[b].get("removed", False)):
                continue

            if a not in norm_adj.get(b, []):
                print(f"❌ FAIL: asymmetry detected: {a}->{b} but {b} does not list {a}")
                return False

    print("3) Coordination (active tiles only)")
    coords = []
    orphans = 0
    active = 0
    for t in tiles:
        if t.get("removed", False):
            continue
        active += 1
        c = len(norm_adj.get(t["id"], []))
        coords.append(c)
        if c == 0:
            orphans += 1

    counts = Counter(coords)
    print(f"   Active tiles: {active}")
    print(f"   Coordination distribution: {dict(sorted(counts.items()))}")
    if orphans:
        print(f"❌ FAIL: {orphans} active tiles have 0 neighbors.")
        return False

    print("✅ PASS: tiling topology looks healthy.")
    return True


if __name__ == "__main__":
    ok = check_structure(ignore_removed_in_symmetry=True)
    sys.exit(0 if ok else 1)
