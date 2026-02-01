# src/simulation/flip_engine.py
"""
Penrose phason flip engine with robust physical constraints
Consistent neighborhood radius handling (Radius 3)
"""

import math
import numpy as np
from typing import Dict, List, Set, Tuple, Any, Optional
from collections import defaultdict, Counter
import itertools

class FlipEngine:
    def __init__(self, vertex_classifier, energy_model, verbose=False): 
        self.classifier = vertex_classifier
        self.energy_model = energy_model
        self.L = None
        self.tolerance_relative = 1e-4
        self.tolerance_absolute = 1e-6
        self.verbose = verbose
    
    def _rebuild_adjacency_global(self, tiling_data: Dict) -> None:
        """
        Global Adjacency Rebuild.
        Recomputes the entire graph topology from scratch based on current geometry.
        
        Improvements over standard rebuild:
        1. Deterministic: Neighbor lists are sorted.
        2. Hygienic: 'removed' tiles are explicitly cleared.
        3. ID Discipline: Uses list index as canonical ID.
        4. Geometry Safety: Detects non-manifold edges (shared by >2 tiles).
        """
        tiles = tiling_data["tiles"]
        edge_to_tiles = defaultdict(list)
        
        # --- PASS 1: Build Geometry Map (Active Tiles Only) ---
        for idx, tile in enumerate(tiles):
            # Enforce ID discipline: The index is the ID.
            if tile.get("id") != idx:
                tile["id"] = idx
            
            # if tile.get("removed", False):
            #     continue

            vertices = tile["vertices"]
            for i in range(4):
                # Normalize edge to ensure direction-independence
                p1, p2 = vertices[i], vertices[(i + 1) % 4]
                edge = self._normalize_edge(p1, p2)
                edge_to_tiles[edge].append(idx)

        # --- PASS 2: Reconstruct Graph (All Tiles) ---
        adjacency_graph = {}
        
        for idx, tile in enumerate(tiles):
            # Case A: Removed Tile -> WIPE EVERYTHING
            if tile.get("removed", False):
                tile["neighbors"] = []
                tile["neighbors_full"] = []
                adjacency_graph[str(idx)] = []
                continue

            # Case B: Active Tile -> Rebuild from map
            full_neighbors = set()
            active_neighbors = set()

            vertices = tile["vertices"]
            for i in range(4):
                p1, p2 = vertices[i], vertices[(i + 1) % 4]
                edge = self._normalize_edge(p1, p2)

                connected_indices = edge_to_tiles.get(edge, [])

                if self.verbose and len(connected_indices) > 2:
                    print(f"   WARN: Edge {edge} shared by {len(connected_indices)} tiles: {connected_indices}")

                for neighbor_idx in connected_indices:
                    if neighbor_idx == idx:
                        continue

                    # neighbors_full sees everything (including removed tiles)
                    full_neighbors.add(neighbor_idx)

                    # neighbors excludes removed tiles (active-only graph)
                    if not tiles[neighbor_idx].get("removed", False):
                        active_neighbors.add(neighbor_idx)

            # Determinism: sort both lists
            sorted_neighbors = sorted(active_neighbors)
            sorted_neighbors_full = sorted(full_neighbors)

            # Update both fields
            tile["neighbors"] = sorted_neighbors
            tile["neighbors_full"] = sorted_neighbors_full

            # adjacency_graph remains the active-only graph
            adjacency_graph[str(idx)] = sorted_neighbors


        tiling_data["adjacency_graph"] = adjacency_graph

        # --- DEBUG: adjacency health check (high signal, low spam) ---
        if getattr(self, "verbosity", 0) >= 2:
            n_tiles = len(tiles)
            n_keys = len(adjacency_graph)
            n_removed = sum(1 for t in tiles if t.get("removed", False))
        
            if n_keys != n_tiles:
                missing = [i for i in range(n_tiles) if str(i) not in adjacency_graph][:15]
                print(
                    f"[ADJ-ERR] adjacency_graph keys={n_keys}/{n_tiles} removed={n_removed} "
                    f"missing_keys(sample)={missing}",
                    flush=True,
                )
            else:
                # Optional: only print occasionally if you want (comment this out if too chatty)
                print(
                    f"[ADJ-OK] adjacency_graph keys={n_keys}/{n_tiles} removed={n_removed}",
                    flush=True,
                )
        


    def compute_edge_length(self, tiling_data: Dict) -> float:
        """Compute Penrose edge length from tiling data"""
        if self.L is not None:
            return self.L
        
        edge_lengths = []
        for tile in tiling_data["tiles"][:200]:
            vertices = tile["vertices"]
            for i in range(4):
                v1 = np.array(vertices[i], dtype=np.float64)
                v2 = np.array(vertices[(i + 1) % 4], dtype=np.float64)
                length = np.linalg.norm(v2 - v1)
                if length > 0.1:
                    edge_lengths.append(length)
        
        edge_lengths = np.array(edge_lengths)
        if len(edge_lengths) == 0:
            self.L = 1.0
        else:
            self.L = float(np.median(edge_lengths))
        return self.L
    
    def find_flippable_hexagons(self, tiling_data: Dict) -> List[List[int]]:
        """Find flippable hexagons using EDGE-BASED detection"""
        self.compute_edge_length(tiling_data)
        
        edge_to_tiles = defaultdict(set)
        for tile_id, tile in enumerate(tiling_data["tiles"]):
            if tile.get("removed", False) or not tile.get("flippable", True):
                continue
            vertices = tile["vertices"]
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                edge_to_tiles[edge].add(tile_id)
        
        clusters = []
        visited = set()
        
        # Build connectivity
        tile_neighbors = defaultdict(set)
        for edge, tiles in edge_to_tiles.items():
            if len(tiles) == 2:
                t1, t2 = list(tiles)
                tile_neighbors[t1].add(t2)
                tile_neighbors[t2].add(t1)
        
        # Find triangles
        for tile_id in tile_neighbors:
            for n1 in tile_neighbors[tile_id]:
                if n1 <= tile_id: continue
                for n2 in tile_neighbors[tile_id]:
                    if n2 <= n1: continue
                    if n2 in tile_neighbors[n1]:
                        cluster = tuple(sorted([tile_id, n1, n2]))
                        if cluster not in visited:
                            if self._verify_hexagon_structure(cluster, tiling_data, edge_to_tiles):
                                clusters.append(list(cluster))
                                visited.add(cluster)
        return clusters

    def capture_state(self, tile_ids, tiling_data):
        """
        Capture state for undo. 
        Accepts specific tile_ids (e.g., the energy calculation region).
        """
        # If passed a list/set of specific IDs (like from MC engine), use those.
        # Otherwise calculate neighborhood (legacy behavior fallback).
        if (isinstance(tile_ids, list) or isinstance(tile_ids, set)) and len(tile_ids) > 3:
             affected_tiles = set(tile_ids)
        else:
             affected_tiles = self._get_k_ring_neighborhood(tile_ids, tiling_data, k=3)

        undo_info = {
            "tile_states": {},
            "adjacency_graph": {},
            "captured_ids": list(affected_tiles)
        }
        
        for tile_id in affected_tiles:
            tile = tiling_data["tiles"][tile_id]
            undo_info["tile_states"][tile_id] = {
                "type": tile["type"],
                "vertex_class": tile.get("vertex_class"),
                "local_energy": tile.get("local_energy"),
                "phason_energy": tile.get("phason_energy"),
                "neighbors": tile.get("neighbors", [])[:],
                "neighbors_full": tile.get("neighbors_full", [])[:],
                "vertices": [v[:] for v in tile["vertices"]],
                "center": tile["center"][:],
                "flippable": tile.get("flippable", True),
                "growth_status": tile.get("growth_status", "ungrown")
            }
        
        # Copy adjacency for affected tiles
        for tile_id in affected_tiles:
            key = str(tile_id)
            if key in tiling_data["adjacency_graph"]:
                undo_info["adjacency_graph"][key] = tiling_data["adjacency_graph"][key][:]
        
        return undo_info
    
    def restore_state(self, undo_info, tiling_data):
        """Restore state from undo"""
        # Restore tiles
        for tile_id, state in undo_info["tile_states"].items():
            tile = tiling_data["tiles"][tile_id]
            for key, value in state.items():
                tile[key] = value
        
        # If the flip attempt performed a global rebuild, we MUST rebuild globally again
        # after restoring tile geometry; otherwise we leave neighbors/graph inconsistent.
        did_rebuild = bool(tiling_data.get("_flip_did_global_rebuild", False))
        
        if did_rebuild:
            # Reconstruct neighbors + adjacency from the restored geometry
            self._rebuild_adjacency_global(tiling_data)
        else:
            # Lightweight restore path (used when apply_flip failed before rebuild)
            for key, neighbors in undo_info["adjacency_graph"].items():
                tiling_data["adjacency_graph"][key] = neighbors
        
        # Clear cache for a safety neighborhood (energies depend on neighbors)
        if hasattr(self.energy_model, "clear_cache"):
            self.energy_model.clear_cache(tile_ids=list(undo_info["tile_states"].keys()))



    def apply_flip(self, cluster_ids: List[int], tiling_data: Dict) -> bool:
        """Apply phason flip"""
        # Track whether we performed a full adjacency rebuild in this attempt
        tiling_data["_flip_did_global_rebuild"] = False

        if len(cluster_ids) != 3:
            return False

        
        L = self.compute_edge_length(tiling_data)
        eps_len = self._get_tolerance(L)
        eps_cross = self._get_tolerance(L * L)
        
        # Determine affected region (Radius 3 for physics)
        affected_tiles = self._get_k_ring_neighborhood(cluster_ids, tiling_data, k=3)
        edge_to_tiles, tile_to_edges = self._build_edge_maps(affected_tiles, tiling_data)
        
        # 1. Analyze Hexagon Structure
        cluster_edges = []
        for tile_id in cluster_ids: cluster_edges.extend(tile_to_edges[tile_id])
        edge_counts = Counter(cluster_edges)
        boundary_edges = [edge for edge, count in edge_counts.items() if count == 1]
        internal_edges = [edge for edge, count in edge_counts.items() if count == 2]
        
        if len(boundary_edges) != 6 or len(internal_edges) != 3: return False
        
        boundary_cycle = self._trace_boundary_cycle(boundary_edges)
        if len(boundary_cycle) != 6: return False
        
        interior_vertex = self._find_interior_vertex(internal_edges, L, eps_len)
        if interior_vertex is None: return False
        
        connected_indices = []
        for i, vertex in enumerate(boundary_cycle):
            if abs(self._distance(vertex, interior_vertex) - L) < 0.01 * L:
                connected_indices.append(i)
        
        if len(connected_indices) != 3: return False
        
        is_even_parity = all(i % 2 == 0 for i in connected_indices)
        is_odd_parity = all(i % 2 == 1 for i in connected_indices)
        if not (is_even_parity or is_odd_parity): return False
        
        target_indices = [1, 3, 5] if is_even_parity else [0, 2, 4]
        target_vertices = [boundary_cycle[i] for i in target_indices]
        new_interior = self._compute_new_interior(target_vertices, L)
        if new_interior is None: return False
        if self._distance(new_interior, interior_vertex) < 0.1 * L: return False
        
        V = boundary_cycle
        if is_even_parity:
            raw_rhombi = [[new_interior, V[1], V[2], V[3]], [new_interior, V[3], V[4], V[5]], [new_interior, V[5], V[0], V[1]]]
        else:
            raw_rhombi = [[new_interior, V[0], V[1], V[2]], [new_interior, V[2], V[3], V[4]], [new_interior, V[4], V[5], V[0]]]
            
        new_rhombi_vertices = [self._order_vertices_clockwise(verts) for verts in raw_rhombi]
        
        for vertices in new_rhombi_vertices:
            if not self._verify_rhombus(vertices, L, eps_len, eps_cross): return False
            
        old_centers = [np.mean(tiling_data["tiles"][tid]["vertices"], axis=0) for tid in cluster_ids]
        new_centers = [np.mean(verts, axis=0) for verts in new_rhombi_vertices]
        best_perm, _ = self._find_best_permutation(old_centers, new_centers)
        
        # Apply updates
        for i, tile_id in enumerate(cluster_ids):
            tile = tiling_data["tiles"][tile_id]
            rhombus_idx = best_perm[i]
            tile["vertices"] = new_rhombi_vertices[rhombus_idx]
            tile["center"] = new_centers[rhombus_idx].tolist()
            tile["type"] = self._determine_tile_type(tile["vertices"])
            
        # ---------------------------------------------------------
        # CRITICAL FIX: Replaced local updates with Global Rebuild
        # ---------------------------------------------------------
        self._rebuild_adjacency_global(tiling_data)
        tiling_data["_flip_did_global_rebuild"] = True
        # ---------------------------------------------------------
        
        # CRITICAL: Recompute energy for the affected radius 3 region
        # (Neighbors are now correct, so this calculation is safe)
        self._recompute_energy_for_region(affected_tiles, tiling_data)
        
        return True
    def _recompute_energy_for_region(self, tile_ids: Set[int], tiling_data: Dict):
        """Recompute energy for affected region, invalidating caches for 4-ring"""
        # Get 4-ring neighborhood for cache invalidation (Safety margin)
        four_ring = self._get_k_ring_neighborhood(list(tile_ids), tiling_data, k=4)
        
        # Clear cache for 4-ring
        if hasattr(self.energy_model, "clear_cache"):
            self.energy_model.clear_cache(tile_ids=list(four_ring))

        
        # Recompute for original region (3-ring)
        for tile_id in tile_ids:
            tile = tiling_data["tiles"][tile_id]
            if not tile.get("removed", False):
                self.energy_model.compute_local_energy(tile_id, tiling_data)

    def _get_k_ring_neighborhood(self, tile_ids: List[int], tiling_data: Dict, k: int = 3) -> Set[int]:
        """Get tiles within k steps"""
        neighborhood = set(tile_ids)
        frontier = set(tile_ids)
        for _ in range(k):
            new_frontier = set()
            for tile_id in frontier:
                neighbors = tiling_data["adjacency_graph"].get(str(tile_id), [])
                for n in neighbors:
                    nid = int(n) if isinstance(n, str) else n
                    if nid not in neighborhood:
                        new_frontier.add(nid)
            neighborhood.update(new_frontier)
            frontier = new_frontier
        return neighborhood
    
    # Backward compatibility wrapper
    def _get_two_ring_neighborhood(self, tile_ids: List[int], tiling_data: Dict) -> Set[int]:
        return self._get_k_ring_neighborhood(tile_ids, tiling_data, k=2)


    def _verify_hexagon_structure(self, cluster, tiling_data, edge_to_tiles):
        all_edges = []
        for tile_id in cluster:
            tile = tiling_data["tiles"][tile_id]
            vertices = tile["vertices"]
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                all_edges.append(edge)
        edge_counts = Counter(all_edges)
        boundary = sum(1 for c in edge_counts.values() if c==1)
        internal = sum(1 for c in edge_counts.values() if c==2)
        if boundary != 6 or internal != 3: return False
        
        # Check center vertex
        internal_edges = [e for e, c in edge_counts.items() if c==2]
        vertex_counts = Counter()
        for e in internal_edges:
            vertex_counts[e[0]] += 1
            vertex_counts[e[1]] += 1
        return len([v for v, c in vertex_counts.items() if c==3]) == 1

    def _normalize_edge(self, v1, v2):
        v1_t = tuple(round(float(x), 10) for x in v1)
        v2_t = tuple(round(float(x), 10) for x in v2)
        return tuple(sorted([v1_t, v2_t]))

    def _get_tolerance(self, scale=1.0): return max(1e-6, abs(scale)*1e-4)
    def _distance(self, v1, v2): return np.linalg.norm(np.array(v1)-np.array(v2))
    def _trace_boundary_cycle(self, edges): 
        if not edges: return []
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v); graph[v].add(u)
        start = next((v for v, n in graph.items() if len(n)==2), None)
        if not start: return []
        cycle = [start]
        curr, prev = start, None
        for _ in range(6):
            nxt = next((n for n in graph[curr] if n != prev), None)
            if not nxt: return []
            cycle.append(nxt)
            prev, curr = curr, nxt
        return cycle[:-1]

    def _find_interior_vertex(self, edges, L, eps):
        cnt = Counter()
        for u, v in edges: cnt[u]+=1; cnt[v]+=1
        return next((list(v) for v, c in cnt.items() if c==3), None)

    def _compute_new_interior(self, target_verts, L):
        A, B, C = [np.array(v) for v in target_verts]
        AB = B - A
        d = np.linalg.norm(AB)
        if d > 2*L or d < 1e-6: return None
        h = np.sqrt(max(0, L*L - (d/2)**2))
        M = (A+B)/2
        perp = np.array([-AB[1], AB[0]]) if abs(AB[0]) < abs(AB[1]) else np.array([AB[1], -AB[0]])
        perp /= np.linalg.norm(perp)
        P1, P2 = M + h*perp, M - h*perp
        return P1.tolist() if abs(np.linalg.norm(P1-C)-L) < abs(np.linalg.norm(P2-C)-L) else P2.tolist()

    def _order_vertices_clockwise(self, verts):
        pts = np.array(verts)
        center = np.mean(pts, axis=0)
        angles = np.arctan2(pts[:,1]-center[1], pts[:,0]-center[0])
        return pts[np.argsort(-angles)].tolist()

    def _verify_rhombus(self, verts, L, eps_len, eps_cross):
        if len(verts) != 4: return False
        v = [np.array(x) for x in verts]
        for i in range(4):
            if abs(np.linalg.norm(v[(i+1)%4]-v[i])-L) > eps_len: return False
        return True

    def _find_best_permutation(self, old, new):
        best_p, best_d = None, float('inf')
        for p in itertools.permutations(range(3)):
            d = sum(np.linalg.norm(new[p[i]]-old[i]) for i in range(3))
            if d < best_d: best_p, best_d = p, d
        return best_p, best_d

    def _determine_tile_type(self, verts):
        if len(verts) < 3: return "THICK"
        v = [np.array(x) for x in verts]
        min_a = 360
        for i in range(4):
            v1, v2 = v[(i-1)%4]-v[i], v[(i+1)%4]-v[i]
            n1, n2 = np.linalg.norm(v1), np.linalg.norm(v2)
            if n1<1e-6 or n2<1e-6: continue
            a = math.degrees(math.acos(np.clip(np.dot(v1, v2)/(n1*n2), -1, 1)))
            min_a = min(min_a, a)
        return "THIN" if abs(min_a-36)<5 else "THICK"

    def _build_edge_maps(self, tids, data):
        e2t, t2e = defaultdict(set), defaultdict(set)
        for tid in tids:
            for i in range(4):
                vs = data["tiles"][tid]["vertices"]
                e = self._normalize_edge(vs[i], vs[(i+1)%4])
                e2t[e].add(tid); t2e[tid].add(e)
        return e2t, t2e

    def _update_edge_maps_after_flip(self, cids, t2e, e2t, data):
        for tid in cids:
            for e in t2e[tid]:
                if tid in e2t[e]: e2t[e].remove(tid)
                if not e2t[e]: del e2t[e]
        for tid in cids:
            new_es = set()
            vs = data["tiles"][tid]["vertices"]
            for i in range(4):
                e = self._normalize_edge(vs[i], vs[(i+1)%4])
                e2t[e].add(tid); new_es.add(e)
            t2e[tid] = new_es

    def _update_adjacency_from_edges(self, cids, aff, e2t, data):
        adj = data["adjacency_graph"]
        for tid in aff:
            ns = set()
            vs = data["tiles"][tid]["vertices"]
            for i in range(4):
                e = self._normalize_edge(vs[i], vs[(i+1)%4])
                if e in e2t:
                    for oid in e2t[e]:
                        if oid != tid: ns.add(oid)
            adj[str(tid)] = list(ns)
            data["tiles"][tid]["neighbors"] = list(ns)