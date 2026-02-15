#!/usr/bin/env python3
"""Tiny contract tests for Step 3 (gateway+context+predicates).

Run from repo root:
  python scripts/test_growth_gateway.py

These tests are intentionally minimal and run on your real JSON if present:
  data/processed/penrose_tiling_energy_initialized.json

If that file is missing, tests are skipped.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

# Ensure repo root is on sys.path (when running `python scripts/...`, sys.path[0] is scripts/)
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.growth.gateway import (  # noqa: E402
    validate_tiling_schema,
    ensure_constraint_fields,
    ensure_mc_fields,
    ensure_growth_fields,
    reset_growth_state_for_run,
    normalize_adjacency_graph_keys,
)
from src.growth.context import create_growth_context, make_working_copy_index_ids  # noqa: E402
from src.growth.adapters import resolve_neighbors_of  # noqa: E402
from src.growth.core import is_present, compute_frontier  # noqa: E402


DEFAULT_JSON = REPO_ROOT / "data" / "processed" / "penrose_tiling_energy_initialized.json"

# Parse --input early (BEFORE decorators/classes), otherwise skipUnless will evaluate wrong.
import argparse  # noqa: E402

_parser = argparse.ArgumentParser(add_help=False)
_parser.add_argument("--input", dest="input_json", default=None)
_args, _unknown = _parser.parse_known_args()

if _args.input_json:
    p = Path(_args.input_json)
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    INPUT_JSON = p
else:
    INPUT_JSON = DEFAULT_JSON



def _load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


@unittest.skipUnless(INPUT_JSON.exists(), "tiling JSON not found; pass path as argv[1] or place it under data/processed/")
class TestGrowthGateway(unittest.TestCase):
    def setUp(self):
        self.tiling = _load_json(INPUT_JSON)


    def test_schema_and_fields(self):
        validate_tiling_schema(self.tiling)
        ensure_constraint_fields(self.tiling)
        ensure_mc_fields(self.tiling)
        ensure_growth_fields(self.tiling)

        tiles = self.tiling["tiles"]
        for t in tiles[:100]:
            self.assertIn("removed", t)
            self.assertIn("immobile", t)
            self.assertIn("flippable", t)
            self.assertIn("growth_status", t)
            self.assertIn("birth_cycle", t)
            self.assertIn("birth_mode", t)

    def test_adjacency_normalization(self):
        normalize_adjacency_graph_keys(self.tiling)
        g = self.tiling.get("adjacency_graph")
        if isinstance(g, dict):
            self.assertTrue(all(isinstance(k, str) for k in g.keys()))

    def test_reset_and_frontier(self):
        ensure_constraint_fields(self.tiling)
        ensure_mc_fields(self.tiling)
        ensure_growth_fields(self.tiling)
        reset_growth_state_for_run(self.tiling)

        tiles = self.tiling["tiles"]

        # Seed 5 non-removed tiles
        seeds = []
        for i, t in enumerate(tiles):
            if not t["removed"]:
                seeds.append(i)
            if len(seeds) >= 5:
                break
        for i in seeds:
            tiles[i]["growth_status"] = "seed"

        neighbors_of = resolve_neighbors_of(self.tiling)
        frontier = compute_frontier(self.tiling, neighbors_of=neighbors_of)

        # Frontier tiles must be ungrown and have at least one present neighbor
        for u in list(frontier)[:200]:
            tu = tiles[u]
            self.assertEqual(tu["growth_status"], "ungrown")
            self.assertFalse(tu["removed"])
            self.assertFalse(tu["immobile"])
            self.assertTrue(any(is_present(tiles[v]) for v in neighbors_of(u)))

    def test_working_copy_id_normalization(self):
        ensure_constraint_fields(self.tiling)
        ensure_mc_fields(self.tiling)
        ensure_growth_fields(self.tiling)
        ctx = create_growth_context(config=None, seed=0)
        work, id_map, inv = make_working_copy_index_ids(self.tiling, ctx=ctx)

        # In work copy, ids must match indices
        for idx, t in enumerate(work["tiles"][:500]):
            self.assertEqual(int(t["id"]), idx)

        self.assertEqual(ctx.id_mode, "normalized")
        self.assertEqual(len(id_map), len(work["tiles"]))
        self.assertEqual(len(inv), len(work["tiles"]))


if __name__ == "__main__":
    # IMPORTANT: prevent unittest from interpreting --input as test-name selectors.
    unittest.main(argv=[sys.argv[0]], verbosity=2)

