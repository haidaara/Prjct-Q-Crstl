# src/simulation/mc_engine.py
"""
Monte Carlo engine with proper energy consistency verification
Implements Option A (Radius 4 for Delta E, Radius 3 for Geometry)
"""

import math
import random
import time
from typing import Dict, List, Tuple, Any, Optional
import numpy as np
from numbers import Integral

from src.utils.energy_utils import (
    wipe_all_energy_fields, clear_all_caches,
    get_k_ring_neighborhood, compute_total_energy_fresh,
    verify_energy_convention
)

class MonteCarloEngine:
    """
    Monte Carlo engine that preserves detailed balance with verified energy consistency
    """

    def __init__(self, temperature: float = 0.3, energy_model=None,
                 flip_engine=None, config: Optional[Dict] = None):
        self.temperature = temperature
        self.energy_model = energy_model
        self.flip_engine = flip_engine
        self.config = config or {}
        
        self.trace_every = int(self.config.get("trace_every", 50))
        self.trace_every = max(1, self.trace_every)

        self.verbosity = int(self.config.get("verbosity", 1))
        self.verbosity = 2 if self.verbosity >= 2 else 1

        self._step_counter= 0

        # CRITICAL PHYSICS PARAMETER:
        # Radius 3 is required for geometry/class propagation consistency.
        # However, delta_E calculation requires Radius 4 due to asymmetric neighbor terms.
        req_radius = self.config.get("neighborhood_radius", 3)
        self.neighborhood_radius = max(req_radius, 3)

        # Global energy tracking
        self.current_energy = 0.0

        # Configurable parameters
        self.base_steps = self.config.get("base_steps", 500)
        self.burn_in_steps = self.config.get("burn_in_steps", 100)

        # Verification settings
        self.verify_frequency = self.config.get("verify_frequency", 0.1)
        self.verify_energy = self.config.get("verify_energy", False)

        # Diagnostics
        self.metrics = {
            "energy_history": [],
            "acceptance_rates": [],
            "computation_times": [],
            "flip_stats": {"proposed": 0, "accepted": 0, "rejected": 0},
            "energy_drift_history": [],
            "delta_energy_history": []
        }

    def _ensure_adjacency_graph_int_keys(self, tiling_data: Dict) -> None:
        """
        Normalize adjacency_graph to *string* keys only.
        """
        g = tiling_data.get("adjacency_graph")
        if not isinstance(g, dict) or not g:
            return

        # First, sanitize values for existing string keys
        for k, v in list(g.items()):
            if isinstance(k, str) and isinstance(v, list):
                try:
                    g[k] = [int(x) for x in v]
                except Exception:
                    pass

        # Then, delete int keys (but if a string twin doesn't exist, keep it by migrating)
        int_keys = [k for k in list(g.keys()) if isinstance(k, Integral) and not isinstance(k, bool)]
        if not int_keys:
            return

        for ik in int_keys:
            sk = str(ik)
            if sk not in g:
                g[sk] = g[ik]
                if isinstance(g[sk], list):
                    try:
                        g[sk] = [int(x) for x in g[sk]]
                    except Exception:
                        pass
            del g[ik]



    def _vprint(self, msg: str, level: int = 1):
        if self.verbosity >= level:
            print(msg, flush=True)

    def initialize_energy(self, tiling_data: Dict) -> None:
        """Compute initial total energy with fresh computation"""
        self._ensure_adjacency_graph_int_keys(tiling_data)
        self.current_energy = compute_total_energy_fresh(self.energy_model, tiling_data)

        self.metrics["energy_history"].append(self.current_energy)

    def _compute_region_energy_fresh(self, tile_ids, tiling_data, extra_ring: int = 1,
                                     return_map: bool = False):
        """
        Compute total energy of region with fresh computation.
        Wipes region + extra_ring to prevent neighbor contamination.

        return_map=False -> returns float energy  (same as before)
        return_map=True  -> returns (energy, energy_map) for printing only
        """
        self._ensure_adjacency_graph_int_keys(tiling_data)
        wipe_region = get_k_ring_neighborhood(tile_ids, tiling_data, k=extra_ring)

        # Freshness should come from cache invalidation, not deleting stored fields.
        clear_all_caches(self.energy_model)
        
        if self.energy_model is None:
            raise ValueError("energy_model is not set. Cannot compute local energy.")
        
        energy = 0.0
        energy_map = {} if return_map else None
        
        for tile_id in tile_ids:
            # Always recompute local energy so tile fields remain consistent,
            # including removed/pore tiles (energy model defines them as zero-energy).
            e = self.energy_model.compute_local_energy(tile_id, tiling_data)
        
            # Keep the same convention as before: removed tiles do not contribute to region sum.
            if not tiling_data["tiles"][tile_id].get("removed", False):
                energy += e
        
            if return_map:
                energy_map[tile_id] = float(e)
        

        if return_map:
            return energy, energy_map
        return energy

    def _verify_energy_consistency(self, tiling_data: Dict, message: str = "") -> float:
        """Verify current_energy matches recomputed total energy"""
        actual_energy = compute_total_energy_fresh(self.energy_model, tiling_data)
        drift = abs(actual_energy - self.current_energy)

        if drift > 0.001:
            print(f"    ENERGY DRIFT {message}: {drift:.6f} "
                  f"(MC={self.current_energy:.6f}, actual={actual_energy:.6f})")

        self.metrics["energy_drift_history"].append(drift)
        return drift

    def run_step(self, tiling_data: Dict, debug_mode: bool = False) -> Tuple[bool, float]:
        """Single MC step with verified energy consistency"""
        step_start = time.time()
        self.metrics["flip_stats"]["proposed"] += 1
        self._step_counter += 1

        # Find flippable clusters
        flippable_clusters = self.flip_engine.find_flippable_hexagons(tiling_data)
        if not flippable_clusters:
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0

        cluster_ids = random.choice(flippable_clusters)

        # ---------------------------------------------------------
        # OPTION A FIX: Split Physics Radius vs Energy Radius
        # ---------------------------------------------------------

        # 1. Core Region (Radius 3): The region physically affected by the flip
        #    This is used for geometry updates and adjacency consistency.
        self._ensure_adjacency_graph_int_keys(tiling_data)
        core_region = get_k_ring_neighborhood(
            cluster_ids, tiling_data, k=self.neighborhood_radius
        )



        # 2. Delta Region (Radius 4): The region needed for Energy Summation
        #    Because neighbor interactions are asymmetric, an update in the Core Region
        #    changes the computed energy of tiles one step further out.
        delta_region = get_k_ring_neighborhood(
            list(core_region), tiling_data, k=2
        )

        do_detail = (self.verbosity >= 2) and (self._step_counter % self.trace_every == 0)
        # #### DETAIL PRINTING  to debug #### 
        if do_detail:
            g = tiling_data.get("adjacency_graph", {})
            print(
                f"[MC] step={self._step_counter} T={self.temperature:.3g} "
                f"cluster={len(cluster_ids)} core={len(core_region)} delta={len(delta_region)} "
                f"adj_keys={len(g)}",
                flush=True,
            )
        
            # Only deep-dump if neighborhood did NOT expand (suspicious)
            if len(core_region) <= len(cluster_ids) or len(delta_region) <= len(core_region):
                sample = list(cluster_ids)[:3]
                print(f"[MC-WARN] k-ring not expanding; cluster sample={sample}", flush=True)
                if g:
                    k0 = next(iter(g.keys()))
                    print(f"[MC-WARN] adjacency_graph key example={k0!r} type={type(k0).__name__}", flush=True)
                for tid in sample:
                    nb = g.get(str(tid), g.get(tid, None))
                    nb_len = None if nb is None else len(nb)
                    print(f"[MC-WARN] tid={tid} neighbors_in_graph={nb_len}", flush=True)
        
        # ##### ---------------------------------------------------------
        
               

        # 3. Capture State (Use Delta Region)
        #    We must capture the full delta_region so that if we reject,
        #    we restore the energy values of the 4th ring too.
        undo_info = self.flip_engine.capture_state(list(delta_region), tiling_data)

        # 4. Compute Energy BEFORE (Sum over Delta Region)
        if do_detail:
            energy_before, e_before_map = self._compute_region_energy_fresh(
                list(delta_region), tiling_data, extra_ring=1, return_map=True
            )
        else:
            energy_before = self._compute_region_energy_fresh(
                list(delta_region), tiling_data, extra_ring=1
            )
            e_before_map = None

        # Snapshot BEFORE (only when printing details)
        if do_detail and e_before_map is not None:
            before_state = {}
            for tid in delta_region:
                t = tiling_data["tiles"][tid]
                before_state[tid] = {
                    "type": t.get("type"),
                    "center": tuple(t.get("center", (0.0, 0.0))),
                    "vertex_class": t.get("vertex_class"),
                    "removed": bool(t.get("removed", False)),
                    "immobile": bool(t.get("immobile", False)),
                }

        # 5. Apply Flip (Uses Core Region Logic internally)
        success = self.flip_engine.apply_flip(cluster_ids, tiling_data)
        if not success:
            self.flip_engine.restore_state(undo_info, tiling_data)
            self.metrics["flip_stats"]["rejected"] += 1
            self.metrics["computation_times"].append(time.time() - step_start)
            return False, 0.0

        # HARD OBSTACLE CONSTRAINT: no non-removed tile center may enter a pore disk
        meta = tiling_data.get("obstacle_metadata") or {}
        if meta.get("type") == "pores":
            positions = meta.get("positions") or []
            radii = meta.get("radii") or []
            tol = 1e-6  # strict barrier (only allow boundary contact)
            for tid in delta_region:  # delta_region is safest: all tiles whose geometry/energy may change
                t = tiling_data["tiles"][tid]
                if t.get("removed", False) or t.get("immobile", False):
                    continue
                cx, cy = t.get("center", (0.0, 0.0))
                for (px, py), R in zip(positions, radii):
                    if (cx - px) ** 2 + (cy - py) ** 2 < (float(R) - tol) ** 2:
                        # invalid move -> reject and restore
                        self.flip_engine.restore_state(undo_info, tiling_data)
                        self.metrics["flip_stats"]["rejected"] += 1
                        self.metrics["computation_times"].append(time.time() - step_start)
                        return False, 0.0


        # 6. Compute Energy AFTER (Sum over Delta Region)
        if do_detail:
            energy_after, e_after_map = self._compute_region_energy_fresh(
                list(delta_region), tiling_data, extra_ring=1, return_map=True
            )
        else:
            energy_after = self._compute_region_energy_fresh(
                list(delta_region), tiling_data, extra_ring=1
            )
            e_after_map = None

        delta_energy = energy_after - energy_before

        # 7. Metropolis Acceptance
        accepted = self._metropolis_accept(delta_energy)

        if do_detail and e_before_map is not None and e_after_map is not None:
            sign = "+" if delta_energy >= 0 else ""
            self._vprint(
                f"   Step {self._step_counter}: cluster={cluster_ids} ΔE={sign}{delta_energy:.6f} accept={accepted}",
                level=2
            )
            self._vprint(
                f"    radius={self.neighborhood_radius} core_region={len(core_region)} delta_region={len(delta_region)} | "
                f"E_before={energy_before:.6f} E_after={energy_after:.6f}",
                level=2
            )


            changes = []
            for tid in delta_region:
                eb = float(e_before_map.get(tid, 0.0))
                ea = float(e_after_map.get(tid, 0.0))
                de = ea - eb

                tb = before_state.get(tid, {})
                t = tiling_data["tiles"][tid]

                c0 = tb.get("center", (0.0, 0.0))
                c1 = tuple(t.get("center", (0.0, 0.0)))
                dx = (c1[0] - c0[0])
                dy = (c1[1] - c0[1])
                move = (dx * dx + dy * dy) ** 0.5

                changes.append({
                    "abs_de": abs(de),
                    "tid": tid,
                    "eb": eb,
                    "ea": ea,
                    "de": de,
                    "type_before": tb.get("type"),
                    "type_after": t.get("type"),
                    "move": move,
                    "class_before": tb.get("vertex_class"),
                    "class_after": t.get("vertex_class"),
                    "removed": bool(t.get("removed", False)),
                    "immobile": bool(t.get("immobile", False)),
                })

            changes.sort(key=lambda x: x["abs_de"], reverse=True)
            self._vprint("    Tile-level changes (top 6 by |ΔE|):", level=2)
            for row in changes[:6]:
            # to print all : for every tiles use, print every tile
            #for row in changes:
                sgn = "+" if row["de"] >= 0 else ""
                tb = row["type_before"] or "?"
                ta = row["type_after"] or "?"
                cb = row["class_before"] or "?"
                ca = row["class_after"] or "?"
                self._vprint(
                    f"      id={row['tid']:5d} {tb}->{ta} move={row['move']:7.4f} "
                    f"E: {row['eb']:7.4f}->{row['ea']:7.4f} ΔE={sgn}{row['de']:8.4f} "
                    f"class:{cb}->{ca} removed={row['removed']} immobile={row['immobile']}",
                    level=2
                )

        if accepted:
            # Update global energy
            self.current_energy += delta_energy
            self.metrics["flip_stats"]["accepted"] += 1

            if debug_mode:
                self._verify_energy_consistency(tiling_data, f"step {len(self.metrics['energy_history'])}")
            elif self.verify_energy and random.random() < self.verify_frequency:
                self._verify_energy_consistency(tiling_data)
        else:
            # REJECT: Restore state (Restores Delta Region)
            self.flip_engine.restore_state(undo_info, tiling_data)

            # Safety: Wipe and recompute to ensure no stale cache remains after restore
            self._compute_region_energy_fresh(list(delta_region), tiling_data, extra_ring=1)

            self.metrics["flip_stats"]["rejected"] += 1

        # Record metrics
        self.metrics["energy_history"].append(self.current_energy)
        self.metrics["delta_energy_history"].append(delta_energy)
        self.metrics["computation_times"].append(time.time() - step_start)

        return accepted, delta_energy

    def run_debug_validation(self, tiling_data: Dict, steps: int = 200) -> Dict:
        """Run MC with full verification for debugging"""
        print(f"   Running debug validation for {steps} steps...")
        self.metrics["energy_drift_history"] = []
        stats = self.run_sweep(tiling_data, steps=steps, debug_mode=True)
        return stats

    def run_sweep(self, tiling_data: Dict, steps: Optional[int] = None,
                  debug_mode: bool = False) -> Dict:
        """Run multiple MC steps with verification"""
        if steps is None:
            steps = self.base_steps

        acceptance_count = 0
        delta_energies = []

        for step in range(steps):
            accepted, delta = self.run_step(tiling_data, debug_mode=debug_mode)
            if accepted:
                acceptance_count += 1
                delta_energies.append(delta)

        final_rate = acceptance_count / steps if steps > 0 else 0.0

        stats = {
            "steps": steps,
            "accepted": acceptance_count,
            "acceptance_rate": final_rate,
            "final_energy": self.current_energy,
            "delta_mean": np.mean(delta_energies) if delta_energies else 0.0,
            "delta_std": np.std(delta_energies) if len(delta_energies) > 1 else 0.0,
            "positive_ratio": np.sum(np.array(delta_energies) > 0) / len(delta_energies) if delta_energies else 0.0,
            "max_drift": max(self.metrics["energy_drift_history"]) if self.metrics["energy_drift_history"] else 0.0
        }

        print(f"   MC sweep: {acceptance_count}/{steps} accepted ({final_rate:.1%}), max drift: {stats['max_drift']:.6f}")
        return stats

    def _metropolis_accept(self, delta_energy: float) -> bool:
        if delta_energy <= 0:
            return True
        return random.random() < math.exp(-delta_energy / self.temperature)

    def get_diagnostics(self) -> Dict[str, Any]:
        return {
            "temperature": self.temperature,
            "final_energy": self.current_energy,
            "config": {"neighborhood_radius": self.neighborhood_radius}
        }
