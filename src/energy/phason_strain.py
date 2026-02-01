"""
src/energy/phason_strain.py

Discrete phason-elastic ("Option A-lite") energy for Penrose tilings.

Physics:
    E_phason(i) = (K/2) * (1/N_i) * sum_{j in N(i)} ||w_i - w_j||^2

Where w_i is the perpendicular-space coordinate derived from a calibrated lift:
    center == M_par @ n + origin
    w = M_perp^T @ n
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import json
import numpy as np


@dataclass(frozen=True)
class PerpendicularState:
    indices: np.ndarray            # (5,) int
    r_perp: np.ndarray             # (3,) float
    reconstruction_error: float    # ||center - (M_par@n + origin)||
    gauge_sum: int                 # sum(indices)


class PhasonStrainCalculator:
    def __init__(
        self,
        calibration: Dict[str, Any],
        stiffness: float,
        *,
        max_cache_size: int = 200_000,
    ) -> None:
        self.stiffness = float(stiffness)
        self.max_cache_size = int(max_cache_size)

        self.M_par = np.array(calibration["M_par"], dtype=float)            # (2,5)
        self.M_perp = np.array(calibration["M_perp"], dtype=float)          # (5,3)
        self.pinv_M_par = np.array(calibration["pinv_M_par"], dtype=float)  # (5,2)
        self.origin = np.array(calibration["origin"], dtype=float).reshape(2,)
        self.target_sum = int(calibration.get("target_sum", 0))

        # Some datasets use multiple valid hyperplane layers (e.g. sum=-2 and sum=-3).
        # We allow those sums and pick the best one per tile by reconstruction error.
        dist = calibration.get("gauge_sum_distribution", {}) or {}
        try:
            self.allowed_sums = sorted({int(k) for k in dist.keys()}) if dist else [self.target_sum]
        except Exception:
            self.allowed_sums = [self.target_sum]
        if self.target_sum not in self.allowed_sums:
            self.allowed_sums.append(self.target_sum)
            self.allowed_sums.sort()


        # Strip-pair offsets learned during calibration: key "a,b" -> [dx, dy]
        self.pair_offsets = calibration.get("pair_offsets", {}) or {}
        self._pair_keys = list(self.pair_offsets.keys())

        # If strips are correct, we can accept quickly; otherwise fall back to brute-force
        self._pair_accept_tol = 1e-8
        self.lift_tol = 1e-10
        self.lift_search_depth = 2   # 2 is usually enough; 3 is safer but heavier



        if self.M_par.shape != (2, 5):
            raise ValueError(f"M_par must be (2,5), got {self.M_par.shape}")
        if self.M_perp.shape != (5, 3):
            raise ValueError(f"M_perp must be (5,3), got {self.M_perp.shape}")
        if self.pinv_M_par.shape != (5, 2):
            raise ValueError(f"pinv_M_par must be (5,2), got {self.pinv_M_par.shape}")

        # Cache keyed by (tile_id, (x,y)) so flips auto-invalidate by center change.
        self._perp_cache: Dict[Tuple[int, Tuple[float, float]], np.ndarray] = {}

    @classmethod
    def from_calibration_file(
        cls,
        calibration_file: str,
        stiffness: float,
        *,
        max_cache_size: int = 200_000,
    ) -> "PhasonStrainCalculator":
        with open(calibration_file, "r", encoding="utf-8") as f:
            calibration = json.load(f)
        return cls(calibration, stiffness, max_cache_size=max_cache_size)

    def clear_cache(self, tile_ids: Optional[List[int]] = None) -> None:
        if tile_ids is None:
            self._perp_cache.clear()
            return
        keys = [k for k in self._perp_cache.keys() if k[0] in tile_ids]
        for k in keys:
            self._perp_cache.pop(k, None)

    def get_perpendicular_state(self, center: np.ndarray) -> PerpendicularState:
        r = np.asarray(center, dtype=float).reshape(2,)
        r_shift = r - self.origin

        n_float = self.pinv_M_par @ r_shift            # (5,)
        n_round = np.rint(n_float).astype(int)         # nearest integers

        # Try the allowed sums (often 1–2 values) and pick the one with smallest reconstruction error.
        best_n = None
        best_err = float("inf")
        best_sum = None

        for s in self.allowed_sums:
            n0 = self._enforce_sum_gauge_to(n_float, n_round, int(s))

            # Local integer refinement (sum-preserving moves) to minimize reconstruction error
            n1 = self._refine_indices_local(r_shift, n0)

            # reconstruction error in shifted space (origin removed)
            e1 = float(np.linalg.norm(r_shift - (self.M_par @ n1)))

            # tie-break: if equal within tiny tol, prefer the dataset's primary target_sum
            if (e1 < best_err - 1e-15) or (abs(e1 - best_err) <= 1e-15 and int(s) == self.target_sum):
                best_err = e1
                best_n = n1
                best_sum = int(s)

        n_int = best_n if best_n is not None else self._refine_indices_local(r_shift, self._enforce_sum_gauge(n_float, n_round))

        w = self.M_perp.T @ n_int                      # (3,)
        r_rec = (self.M_par @ n_int) + self.origin
        err = float(np.linalg.norm(r - r_rec))

        return PerpendicularState(
            indices=n_int,
            r_perp=w.astype(float),
            reconstruction_error=err,
            gauge_sum=int(np.sum(n_int)),
        )

    def get_perp_coordinate(self, tile_id: int, tiling_data: Dict) -> np.ndarray:
        tile = tiling_data["tiles"][tile_id]
        c = tile.get("center", (0.0, 0.0))
        center = (float(c[0]), float(c[1]))
        key = (int(tile_id), center)

        w = self._perp_cache.get(key)
        if w is not None:
            return w

        # Simple bound: if cache grows too big, drop all (safe + simple).
        if len(self._perp_cache) >= self.max_cache_size:
            self._perp_cache.clear()

        pair_hint = self._pair_key_hint(tile)
        state, best_key = self._best_state_for_center(center, pair_hint)
        self._perp_cache[key] = state.r_perp

        return state.r_perp

    def compute_energy_for_tile(
        self,
        tile_id: int,
        tiling_data: Dict,
        *,
        normalize_by_degree: bool = True,
        treat_ungrown_as_vacuum: bool = False,
    ) -> float:
        tile = tiling_data["tiles"][tile_id]

        if tile.get("removed", False) or tile.get("obstacle_type") == "pore":
            return 0.0
        if treat_ungrown_as_vacuum and tile.get("growth_status") == "ungrown":
            return 0.0

        neighbors = self._get_active_neighbors(
            tile_id, tiling_data, treat_ungrown_as_vacuum=treat_ungrown_as_vacuum
        )
        if not neighbors:
            return 0.0

        w_i = self.get_perp_coordinate(tile_id, tiling_data)

        total = 0.0
        for nid in neighbors:
            w_j = self.get_perp_coordinate(nid, tiling_data)
            d = w_i - w_j
            total += float(np.dot(d, d))

        if normalize_by_degree:
            return (self.stiffness / (2.0 * len(neighbors))) * total
        return (self.stiffness / 2.0) * total

    def diagnostics_for_tile(self, tile_id: int, tiling_data: Dict) -> Dict[str, Any]:
        tile = tiling_data["tiles"][tile_id]
        center = np.array(tile.get("center", (0.0, 0.0)), dtype=float)
        pair_hint = self._pair_key_hint(tile)
        state, best_key = self._best_state_for_center((float(center[0]), float(center[1])), pair_hint)
        
        return {
            "tile_id": int(tile_id),
            "center": [float(center[0]), float(center[1])],
            "indices": [int(x) for x in state.indices.tolist()],
            "gauge_sum": int(state.gauge_sum),
            "target_sum": int(self.target_sum),
            "gauge_ok": bool(state.gauge_sum in getattr(self, "allowed_sums", [self.target_sum])),
            "perp": [float(x) for x in state.r_perp.tolist()],
            "reconstruction_error": float(state.reconstruction_error),
            "best_pair_key": best_key,

        }

    def _enforce_sum_gauge_to(self, n_float: np.ndarray, n_int: np.ndarray, target_sum: int) -> np.ndarray:
        """
        Enforce sum(n_i) = target_sum with minimal change relative to n_float.
        Same logic as _enforce_sum_gauge, but with an explicit target_sum.
        """
        out = n_int.copy()
        diff = int(target_sum - np.sum(out))
        if diff == 0:
            return out

        resid = n_float - out.astype(float)  # in [-0.5, 0.5]
        direction = 1 if diff > 0 else -1

        for _ in range(abs(diff)):
            idx = int(np.argmax(resid)) if direction > 0 else int(np.argmin(resid))
            out[idx] += direction
            resid[idx] -= direction

        return out


    def _enforce_sum_gauge(self, n_float: np.ndarray, n_int: np.ndarray) -> np.ndarray:
        """ Enforce sum(n_i) = target_sum with minimal change relative to n_float."""
        return self._enforce_sum_gauge_to(n_float, n_int, self.target_sum)


    def _get_active_neighbors(
        self,
        tile_id: int,
        tiling_data: Dict,
        *,
        treat_ungrown_as_vacuum: bool,
    ) -> List[int]:
        tiles = tiling_data["tiles"]
        adj = tiling_data.get("adjacency_graph", None)

        if isinstance(adj, dict):
            k = str(tile_id)
            if k in adj:
                neighbor_ids = adj[k]
            elif tile_id in adj:
                neighbor_ids = adj[tile_id]
            else:
                neighbor_ids = tiles[tile_id].get("neighbors", [])
        else:
            neighbor_ids = tiles[tile_id].get("neighbors", [])

        out: List[int] = []
        for nid in neighbor_ids:
            try:
                j = int(nid)
            except Exception:
                continue
            if j < 0 or j >= len(tiles):
                continue

            tj = tiles[j]
            if tj.get("removed", False) or tj.get("obstacle_type") == "pore":
                continue
            if treat_ungrown_as_vacuum and tj.get("growth_status") == "ungrown":
                continue

            out.append(j)
        return out


    def _pair_key_hint(self, tile: Dict) -> Optional[str]:
        strips = tile.get("strips", [])
        if len(strips) != 2:
            return None
        try:
            fams = sorted([int(strips[0]["family"]), int(strips[1]["family"])])
            return f"{fams[0]},{fams[1]}"
        except Exception:
            return None

    def _best_state_for_center(
        self,
        center: Tuple[float, float],
        pair_hint: Optional[str],
    ) -> Tuple[PerpendicularState, Optional[str]]:
        """
        Choose the strip-pair offset using a purely linear projection residual,
        then lift once (integer rounding/refinement happens only after the pair is chosen).
        """
        c = np.array([float(center[0]), float(center[1])], dtype=float)
    
        # If no offsets available, fall back to raw lift (coarser)
        if not self._pair_keys:
            return self.get_perpendicular_state(c), None
    
        # Pick best pair key using projection residual (no integer rounding involved)
        best_key = self._best_pair_key_by_projection((float(center[0]), float(center[1])), pair_hint)
    
        if best_key is None or best_key not in self.pair_offsets:
            return self.get_perpendicular_state(c), None
    
        off = self.pair_offsets[best_key]
        c_eff = np.array([c[0] - float(off[0]), c[1] - float(off[1])], dtype=float)
    
        state = self.get_perpendicular_state(c_eff)
    
        # Optional safety fallback (keep simple): if something is very off, fall back to raw
        # (This should almost never trigger if calibration is correct.)
        if state.reconstruction_error > 1e-6:
            return self.get_perpendicular_state(c), None
    
        return state, best_key



    def _force_target_sum(self, n: np.ndarray) -> np.ndarray:
        n = n.astype(int).copy()
        diff = int(self.target_sum - np.sum(n))
        if diff == 0:
            return n
        # adjust the component with smallest |column| so it perturbs geometry least
        col_norm = np.sum(self.M_par * self.M_par, axis=0)  # (5,)
        k = int(np.argmin(col_norm))
        n[k] += diff
        return n
    
    def _refine_indices_local(self, r_shift: np.ndarray, n0: np.ndarray) -> np.ndarray:
        """
        Improve integer lifting by searching nearby indices with sum(n)=target_sum.
        Uses moves: n[i]+=1, n[j]-=1 which preserve the sum.
        """
        def err(nv: np.ndarray) -> float:
            return float(np.linalg.norm(r_shift - (self.M_par @ nv)))

        best = n0.astype(int).copy()
        best_err = err(best)
        if best_err <= self.lift_tol:
            return best

        visited = {tuple(best.tolist())}
        frontier = [best]

        for _ in range(int(self.lift_search_depth)):
            nxt = []
            for n in frontier:
                for i in range(5):
                    for j in range(5):
                        if i == j:
                            continue
                        m = n.copy()
                        m[i] += 1
                        m[j] -= 1
                        key = tuple(m.tolist())
                        if key in visited:
                            continue
                        visited.add(key)

                        e = err(m)
                        if e < best_err:
                            best_err = e
                            best = m
                            if best_err <= self.lift_tol:
                                return best
                        nxt.append(m)
            frontier = nxt

        return best


    def _best_pair_key_by_projection(self, center: tuple[float, float], pair_hint: str | None) -> str | None:
        if not self.pair_offsets:
            return None

        c = np.array([float(center[0]), float(center[1])], dtype=float)
        r = c - self.origin  # 2D

        def residual_for(key: str) -> float:
            off = self.pair_offsets[key]
            r_eff = r - np.array([float(off[0]), float(off[1])], dtype=float)
            proj = self.M_par @ (self.pinv_M_par @ r_eff)  # projection onto col(M_par)
            return float(np.linalg.norm(r_eff - proj))

        # fast path: trust hint if it lands in colspace
        tol = 1e-10
        if pair_hint and pair_hint in self.pair_offsets:
            res = residual_for(pair_hint)
            if res <= tol:
                return pair_hint

        # brute-force over the 10 pairs (cheap)
        best_key = None
        best_res = float("inf")
        for key in self.pair_offsets.keys():
            res = residual_for(key)
            if res < best_res:
                best_res = res
                best_key = key

        return best_key




