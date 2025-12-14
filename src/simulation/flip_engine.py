# src/simulation/flip_engine.py - FIXED VERSION WITH ROBUST GEOMETRY
"""
Penrose phason flip engine with robust physical constraints
"""

import math
import numpy as np
from typing import Dict, List, Set, Tuple, Any, Optional
from collections import defaultdict, Counter
import itertools

class FlipEngine:
    def __init__(self, vertex_classifier, energy_model):
        self.classifier = vertex_classifier
        self.energy_model = energy_model
        self.L = None  # Penrose edge length
        self.tolerance_relative = 1e-4  # Relative to L
        self.tolerance_absolute = 1e-6
    
    def compute_edge_length(self, tiling_data: Dict) -> float:
        """Compute Penrose edge length from tiling data"""
        if self.L is not None:
            return self.L
        
        # Sample edges to find consistent length
        edge_lengths = []
        for tile in tiling_data["tiles"][:200]:
            vertices = tile["vertices"]
            for i in range(4):
                v1 = np.array(vertices[i], dtype=np.float64)
                v2 = np.array(vertices[(i + 1) % 4], dtype=np.float64)
                length = np.linalg.norm(v2 - v1)
                if length > 0.1:  # Avoid tiny edges from artifacts
                    edge_lengths.append(length)
        
        # Use robust statistics: median with IQR filtering
        edge_lengths = np.array(edge_lengths)
        q25, q75 = np.percentile(edge_lengths, [25, 75])
        iqr = q75 - q25
        valid_mask = (edge_lengths > q25 - 1.5*iqr) & (edge_lengths < q75 + 1.5*iqr)
        filtered_lengths = edge_lengths[valid_mask]
        
        if len(filtered_lengths) == 0:
            self.L = 1.0  # Default fallback
        else:
            self.L = float(np.median(filtered_lengths))
        
        print(f"📏 Penrose edge length: {self.L:.6f} (from {len(filtered_lengths)} valid edges)")
        return self.L
    
    def find_flippable_hexagons(self, tiling_data: Dict) -> List[List[int]]:
        """Find flippable hexagons using EDGE-BASED detection (robust)"""
        self.compute_edge_length(tiling_data)
        L = self.L
        
        # Build edge to tiles mapping
        edge_to_tiles = defaultdict(set)
        for tile_id, tile in enumerate(tiling_data["tiles"]):
            if tile.get("removed", False) or not tile.get("flippable", True):
                continue
            
            vertices = tile["vertices"]
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                edge_to_tiles[edge].add(tile_id)
        
        # Look for clusters of 3 tiles with the right edge pattern
        clusters = []
        visited = set()
        
        # Build tile connectivity from shared edges
        tile_neighbors = defaultdict(set)
        for edge, tiles in edge_to_tiles.items():
            if len(tiles) == 2:
                t1, t2 = list(tiles)
                tile_neighbors[t1].add(t2)
                tile_neighbors[t2].add(t1)
        
        # Find triangles in the neighbor graph
        for tile_id in tile_neighbors:
            for n1 in tile_neighbors[tile_id]:
                if n1 <= tile_id:
                    continue
                for n2 in tile_neighbors[tile_id]:
                    if n2 <= n1:
                        continue
                    # Check if n1 and n2 are also neighbors
                    if n2 in tile_neighbors[n1]:
                        cluster = tuple(sorted([tile_id, n1, n2]))
                        if cluster not in visited:
                            # Verify hexagon structure
                            if self._verify_hexagon_structure(cluster, tiling_data, edge_to_tiles):
                                clusters.append(list(cluster))
                                visited.add(cluster)
        
        return clusters
    
    def _verify_hexagon_structure(self, cluster: Tuple[int, int, int], 
                                 tiling_data: Dict, edge_to_tiles: Dict) -> bool:
        """Verify 3 tiles form a valid hexagon"""
        # Collect all edges
        all_edges = []
        for tile_id in cluster:
            tile = tiling_data["tiles"][tile_id]
            vertices = tile["vertices"]
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                all_edges.append(edge)
        
        edge_counts = Counter(all_edges)
        
        # Count edges by multiplicity
        boundary_count = sum(1 for count in edge_counts.values() if count == 1)
        internal_count = sum(1 for count in edge_counts.values() if count == 2)
        
        # Should have 6 boundary edges (hexagon perimeter) and 3 internal edges
        if boundary_count != 6 or internal_count != 3:
            return False
        
        # Check that internal edges form a Y shape (share a common vertex)
        internal_edges = [edge for edge, count in edge_counts.items() if count == 2]
        
        # Extract vertices from internal edges
        internal_vertices = set()
        for edge in internal_edges:
            v1, v2 = edge
            internal_vertices.add(v1)
            internal_vertices.add(v2)
        
        # One vertex should appear in all 3 internal edges (the center)
        vertex_counts = Counter()
        for edge in internal_edges:
            v1, v2 = edge
            vertex_counts[v1] += 1
            vertex_counts[v2] += 1
        
        center_vertices = [v for v, count in vertex_counts.items() if count == 3]
        if len(center_vertices) != 1:
            return False
        
        return True
    
    def _get_tolerance(self, scale: float = 1.0) -> float:
        """Get scale-aware tolerance"""
        return max(self.tolerance_absolute, abs(scale) * self.tolerance_relative)
    
    def _distance(self, v1, v2) -> float:
        """Robust Euclidean distance"""
        return np.linalg.norm(np.array(v1, dtype=np.float64) - np.array(v2, dtype=np.float64))
    
    def _normalize_edge(self, v1, v2) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """Create canonical edge representation"""
        # Use high precision for geometry
        v1_t = tuple(round(float(x), 12) for x in v1)
        v2_t = tuple(round(float(x), 12) for x in v2)
        return tuple(sorted([v1_t, v2_t]))
    
    def apply_flip(self, cluster_ids: List[int], tiling_data: Dict) -> bool:
        """Apply physically correct Penrose phason flip with robust geometry"""
        if len(cluster_ids) != 3:
            raise ValueError("Hexagon flip requires exactly 3 tiles")
        
        print(f"\n🔄 Physical flip on {cluster_ids}")
        
        # ==============================================
        # 1. COMPUTE EDGE LENGTH AND BUILD EDGE MAPPING
        # ==============================================
        L = self.compute_edge_length(tiling_data)
        eps_len = self._get_tolerance(L)  # Scale-aware tolerance
        eps_cross = self._get_tolerance(L * L)
        
        # Build edge mapping for affected region
        affected_tiles = self._get_two_ring_neighborhood(cluster_ids, tiling_data)
        edge_to_tiles, tile_to_edges = self._build_edge_maps(affected_tiles, tiling_data)
        
        # ==============================================
        # 2. ANALYZE HEXAGON STRUCTURE
        # ==============================================
        # Get all edges of the 3 tiles
        cluster_edges = []
        for tile_id in cluster_ids:
            cluster_edges.extend(tile_to_edges[tile_id])
        
        edge_counts = Counter(cluster_edges)
        boundary_edges = [edge for edge, count in edge_counts.items() if count == 1]
        internal_edges = [edge for edge, count in edge_counts.items() if count == 2]
        
        if len(boundary_edges) != 6 or len(internal_edges) != 3:
            print(f"❌ Invalid hexagon: {len(boundary_edges)} boundary, {len(internal_edges)} internal")
            return False
        
        # ==============================================
        # 3. TRACE BOUNDARY CYCLE
        # ==============================================
        boundary_cycle = self._trace_boundary_cycle(boundary_edges)
        if len(boundary_cycle) != 6:
            print(f"❌ Boundary cycle has {len(boundary_cycle)} vertices, expected 6")
            return False
        
        # ==============================================
        # 4. FIND INTERIOR VERTEX (ROBUST METHOD)
        # ==============================================
        interior_vertex = self._find_interior_vertex(internal_edges, L, eps_len)
        if interior_vertex is None:
            print("❌ Could not find interior vertex")
            return False
        
        # ==============================================
        # 5. DETERMINE CONNECTED BOUNDARY VERTICES (FIXED)
        # ==============================================
        # **CRITICAL FIX**: Don't use distance < L, use distance ≈ L
        # In Penrose hexagon: connected vertices are exactly distance L
        # Non-connected vertices are at distance L * φ or L / φ
        connected_indices = []
        for i, vertex in enumerate(boundary_cycle):
            dist = self._distance(vertex, interior_vertex)
            # Check if distance is approximately L (within 0.01 * L)
            if abs(dist - L) < 0.01 * L:
                connected_indices.append(i)
        
        if len(connected_indices) != 3:
            print(f"❌ Interior connects to {len(connected_indices)} vertices, expected 3")
            print(f"   Distances: {[self._distance(boundary_cycle[i], interior_vertex) for i in range(6)]}")
            return False
        
        # Determine parity (even: 0,2,4 or odd: 1,3,5)
        is_even_parity = all(i % 2 == 0 for i in connected_indices)
        is_odd_parity = all(i % 2 == 1 for i in connected_indices)
        
        if not (is_even_parity or is_odd_parity):
            print("❌ Boundary connections not in consistent parity")
            print(f"   Connected indices: {connected_indices}")
            return False
        
        # ==============================================
        # 6. COMPUTE NEW INTERIOR VERTEX
        # ==============================================
        # New interior connects to opposite parity
        if is_even_parity:
            # Old connects to even (0,2,4), new connects to odd (1,3,5)
            target_indices = [1, 3, 5]
            old_parity = "even"
        else:
            # Old connects to odd (1,3,5), new connects to even (0,2,4)
            target_indices = [0, 2, 4]
            old_parity = "odd"
        
        target_vertices = [boundary_cycle[i] for i in target_indices]
        new_interior = self._compute_new_interior(target_vertices, L)
        
        if new_interior is None:
            print("❌ Could not compute new interior vertex")
            return False
        
        # Verify new interior is sufficiently different
        if self._distance(new_interior, interior_vertex) < 0.1 * L:
            print("❌ New interior too close to old interior")
            return False
        
        # ==============================================
        # 7. CONSTRUCT AND ORDER NEW RHOMBI (FIXED)
        # ==============================================
        V = boundary_cycle  # Boundary vertices in cyclic order
        
        if is_even_parity:
            # New interior connects to odd vertices (1,3,5)
            raw_rhombi = [
                [new_interior, V[1], V[2], V[3]],
                [new_interior, V[3], V[4], V[5]],
                [new_interior, V[5], V[0], V[1]]
            ]
        else:
            # New interior connects to even vertices (0,2,4)
            raw_rhombi = [
                [new_interior, V[0], V[1], V[2]],
                [new_interior, V[2], V[3], V[4]],
                [new_interior, V[4], V[5], V[0]]
            ]
        
        # **CRITICAL FIX**: Order vertices clockwise for each rhombus
        new_rhombi_vertices = [self._order_vertices_clockwise(verts) for verts in raw_rhombi]
        
        # ==============================================
        # 8. VERIFY NEW RHOMBI GEOMETRY (WITH RELAXED TOLERANCES)
        # ==============================================
        for i, vertices in enumerate(new_rhombi_vertices):
            if not self._verify_rhombus(vertices, L, eps_len, eps_cross):
                print(f"❌ New rhombus {i} fails geometry check")
                # Debug information
                for j in range(4):
                    v1 = np.array(vertices[j])
                    v2 = np.array(vertices[(j + 1) % 4])
                    length = np.linalg.norm(v2 - v1)
                    print(f"    Edge {j}: length = {length:.6f}, expected {L:.6f}")
                return False
        
        # ==============================================
        # 9. ASSIGN RHOMBI TO TILES (MINIMAL DISPLACEMENT)
        # ==============================================
        # Compute old centers
        old_centers = []
        for tile_id in cluster_ids:
            tile = tiling_data["tiles"][tile_id]
            vertices = [np.array(v, dtype=np.float64) for v in tile["vertices"]]
            center = np.mean(vertices, axis=0)
            old_centers.append(center)
        
        # Compute new centers
        new_centers = [np.mean(verts, axis=0) for verts in new_rhombi_vertices]
        
        # Find best permutation
        best_perm, best_dist = self._find_best_permutation(old_centers, new_centers)
        
        # ==============================================
        # 10. UPDATE TILE GEOMETRY
        # ==============================================
        for i, tile_id in enumerate(cluster_ids):
            tile = tiling_data["tiles"][tile_id]
            rhombus_idx = best_perm[i]
            
            # Store old for comparison
            old_center = tile["center"]
            old_type = tile["type"]
            
            # Update geometry
            tile["vertices"] = new_rhombi_vertices[rhombus_idx]
            tile["center"] = new_centers[rhombus_idx].tolist()
            tile["type"] = self._determine_tile_type(tile["vertices"])
            
            print(f"  Tile {tile_id}: {old_type}→{tile['type']}, "
                  f"center moved {self._distance(old_center, tile['center']):.3f}")
        
        # ==============================================
        # 11. UPDATE EDGE MAPPING AND ADJACENCY
        # ==============================================
        self._update_edge_maps_after_flip(cluster_ids, tile_to_edges, edge_to_tiles, tiling_data)
        self._update_adjacency_from_edges(cluster_ids, affected_tiles, edge_to_tiles, tiling_data)
        
        # ==============================================
        # 12. CLEAR CACHE AND RECOMPUTE ENERGY
        # ==============================================
        self._recompute_energy_for_region(affected_tiles, tiling_data)
        
        print(f"✅ Flip successful (old parity: {old_parity})")
        print(f"   Interior moved: {self._distance(new_interior, interior_vertex):.3f} units")
        print(f"   Tile assignment distance: {best_dist:.3f}")
        
        return True
    
    def _find_interior_vertex(self, internal_edges: List[Tuple], L: float, eps: float) -> Optional[List[float]]:
        """Find interior vertex where 3 internal edges meet"""
        # Count vertex appearances in internal edges
        vertex_counts = Counter()
        for edge in internal_edges:
            v1, v2 = edge
            vertex_counts[v1] += 1
            vertex_counts[v2] += 1
        
        # Vertex appearing 3 times is the interior
        for vertex, count in vertex_counts.items():
            if count == 3:
                return list(vertex)
        
        return None
    
    def _compute_new_interior(self, target_vertices: List[List[float]], L: float) -> Optional[List[float]]:
        """Compute new interior as intersection of 3 circles radius L"""
        A, B, C = [np.array(v, dtype=np.float64) for v in target_vertices]
        
        # Use two circles to find intersection candidates, third to choose
        # Solve for intersection of circles centered at A and B
        
        # Vector from A to B
        AB = B - A
        d = np.linalg.norm(AB)
        
        # Check if circles intersect
        if d > 2 * L or d < self._get_tolerance(L):
            return None
        
        # Distance from A to midpoint of intersection line
        a = d / 2
        
        # Height of intersection triangle
        h_sq = L * L - a * a
        if h_sq < 0:
            return None
        h = np.sqrt(h_sq)
        
        # Midpoint between A and B
        M = (A + B) / 2
        
        # Perpendicular direction (normalized)
        if abs(AB[0]) < abs(AB[1]):
            perp = np.array([-AB[1], AB[0]], dtype=np.float64)
        else:
            perp = np.array([AB[1], -AB[0]], dtype=np.float64)
        perp = perp / np.linalg.norm(perp)
        
        # Two intersection points
        P1 = M + h * perp
        P2 = M - h * perp
        
        # Choose the one closer to being distance L from C
        dist1 = abs(np.linalg.norm(P1 - C) - L)
        dist2 = abs(np.linalg.norm(P2 - C) - L)
        
        if dist1 < dist2:
            return P1.tolist()
        else:
            return P2.tolist()
    
    def _order_vertices_clockwise(self, vertices: List[List[float]]) -> List[List[float]]:
        """Order 4 vertices of a convex quadrilateral clockwise"""
        pts = np.array(vertices, dtype=np.float64)
        
        # Compute center
        center = np.mean(pts, axis=0)
        
        # Compute angles from center
        dx = pts[:, 0] - center[0]
        dy = pts[:, 1] - center[1]
        angles = np.arctan2(dy, dx)  # Returns in [-π, π]
        
        # Sort clockwise (decreasing angle)
        order = np.argsort(-angles)
        
        return pts[order].tolist()
    
    def _verify_rhombus(self, vertices: List[List[float]], L: float, 
                       eps_len: float, eps_cross: float) -> bool:
        """Verify 4 vertices form a valid rhombus with relaxed tolerances"""
        if len(vertices) != 4:
            return False
        
        v = [np.array(vertex, dtype=np.float64) for vertex in vertices]
        
        # Check all edges have approximately length L
        for i in range(4):
            edge_len = np.linalg.norm(v[(i + 1) % 4] - v[i])
            if abs(edge_len - L) > eps_len:
                return False
        
        # Check opposite sides are parallel (cross product ≈ 0)
        for i in range(2):
            vec1 = v[i + 1] - v[i]
            vec2 = v[(i + 3) % 4] - v[(i + 2) % 4]
            cross = abs(np.cross(vec1, vec2))
            if cross > eps_cross:
                return False
        
        # Check convexity (all cross products same sign)
        cross_signs = []
        for i in range(4):
            vec1 = v[(i + 1) % 4] - v[i]
            vec2 = v[(i + 2) % 4] - v[(i + 1) % 4]
            cross = np.cross(vec1, vec2)
            cross_signs.append(np.sign(cross))
        
        # All should be same sign (non-zero)
        if len(set(cross_signs)) != 1 or cross_signs[0] == 0:
            return False
        
        return True
    
    def _find_best_permutation(self, old_centers: List[np.ndarray], 
                             new_centers: List[np.ndarray]) -> Tuple[List[int], float]:
        """Find best tile assignment with minimal total displacement"""
        best_perm = None
        best_dist = float('inf')
        
        for perm in itertools.permutations(range(3)):
            total_dist = 0
            for i, j in enumerate(perm):
                total_dist += np.linalg.norm(new_centers[j] - old_centers[i])
            
            if total_dist < best_dist:
                best_dist = total_dist
                best_perm = perm
        
        return list(best_perm), best_dist
    
    def _determine_tile_type(self, vertices: List[List[float]]) -> str:
        """Determine if thick (72°) or thin (36°) from vertex angles"""
        if len(vertices) < 3:
            return "THICK"
        
        v = [np.array(vertex, dtype=np.float64) for vertex in vertices]
        
        # Compute smallest interior angle
        min_angle = 360.0
        for i in range(4):
            vec1 = v[(i - 1) % 4] - v[i]
            vec2 = v[(i + 1) % 4] - v[i]
            
            norm1 = np.linalg.norm(vec1)
            norm2 = np.linalg.norm(vec2)
            
            if norm1 < self._get_tolerance() or norm2 < self._get_tolerance():
                continue
            
            cos_angle = np.dot(vec1, vec2) / (norm1 * norm2)
            cos_angle = np.clip(cos_angle, -1.0, 1.0)
            angle = math.degrees(math.acos(cos_angle))
            
            if angle < min_angle:
                min_angle = angle
        
        # Thin rhombus has 36° angles, thick has 72° angles
        if abs(min_angle - 36.0) < 5.0:
            return "THIN"
        else:
            return "THICK"
    
    def _build_edge_maps(self, tile_ids: Set[int], tiling_data: Dict):
        """Build edge to tiles and tile to edges mappings"""
        edge_to_tiles = defaultdict(set)
        tile_to_edges = defaultdict(set)
        
        for tile_id in tile_ids:
            tile = tiling_data["tiles"][tile_id]
            vertices = tile["vertices"]
            
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                edge_to_tiles[edge].add(tile_id)
                tile_to_edges[tile_id].add(edge)
        
        return edge_to_tiles, tile_to_edges
    
    def _update_edge_maps_after_flip(self, cluster_ids: List[int], 
                                   tile_to_edges: Dict, edge_to_tiles: Dict,
                                   tiling_data: Dict):
        """Update edge mappings after flip"""
        # Remove old edges of flipped tiles
        for tile_id in cluster_ids:
            for edge in tile_to_edges[tile_id]:
                if tile_id in edge_to_tiles[edge]:
                    edge_to_tiles[edge].remove(tile_id)
                if not edge_to_tiles[edge]:
                    del edge_to_tiles[edge]
        
        # Add new edges
        for tile_id in cluster_ids:
            tile = tiling_data["tiles"][tile_id]
            vertices = tile["vertices"]
            
            new_edges = set()
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                edge_to_tiles[edge].add(tile_id)
                new_edges.add(edge)
            
            tile_to_edges[tile_id] = new_edges
    
    def _update_adjacency_from_edges(self, cluster_ids: List[int], affected_tiles: Set[int],
                                   edge_to_tiles: Dict, tiling_data: Dict):
        """Update adjacency from edge mappings"""
        adjacency = tiling_data["adjacency_graph"]
        
        for tile_id in affected_tiles:
            # Find neighbors by edge sharing (at least 2 shared vertices = edge)
            neighbors = set()
            
            # Get this tile's edges
            tile_edges = set()
            tile = tiling_data["tiles"][tile_id]
            vertices = tile["vertices"]
            for i in range(4):
                edge = self._normalize_edge(vertices[i], vertices[(i + 1) % 4])
                tile_edges.add(edge)
            
            # Check each edge for other tiles
            for edge in tile_edges:
                if edge in edge_to_tiles:
                    for other_id in edge_to_tiles[edge]:
                        if other_id != tile_id:
                            neighbors.add(other_id)
            
            # Update
            adjacency[str(tile_id)] = list(neighbors)
            tile["neighbors"] = list(neighbors)
    
    def _recompute_energy_for_region(self, tile_ids: Set[int], tiling_data: Dict):
        """Recompute energy for affected region"""
        # Clear cache for affected tiles
        if hasattr(self.energy_model, '_vertex_class_cache'):
            cache = self.energy_model._vertex_class_cache
            for tile_id in tile_ids:
                cache.pop(tile_id, None)
        
        # Recompute
        for tile_id in tile_ids:
            tile = tiling_data["tiles"][tile_id]
            if not tile.get("removed", False):
                self.energy_model.compute_local_energy(tile_id, tiling_data)
    
    def _get_two_ring_neighborhood(self, tile_ids: List[int], tiling_data: Dict) -> Set[int]:
        """Get tiles within 2 steps"""
        neighborhood = set(tile_ids)
        
        # First ring
        for tile_id in tile_ids:
            neighbors = tiling_data["adjacency_graph"].get(str(tile_id), [])
            neighborhood.update(neighbors)
        
        # Second ring
        first_ring = list(neighborhood - set(tile_ids))
        for tile_id in first_ring:
            neighbors = tiling_data["adjacency_graph"].get(str(tile_id), [])
            neighborhood.update(neighbors)
        
        return neighborhood
    
    def _trace_boundary_cycle(self, boundary_edges: List[Tuple]) -> List[List[float]]:
        """Trace boundary edges to get vertices in cyclic order"""
        if not boundary_edges:
            return []
        
        # Build graph
        graph = defaultdict(set)
        for edge in boundary_edges:
            v1, v2 = edge
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        # Find starting vertex (degree 2 in boundary)
        start = None
        for vertex, neighbors in graph.items():
            if len(neighbors) == 2:
                start = vertex
                break
        
        if start is None:
            return []
        
        # Trace cycle
        cycle = [list(start)]
        current = start
        prev = None
        
        for _ in range(6):
            neighbors = list(graph[current])
            # Find next vertex (not previous)
            for neighbor in neighbors:
                if neighbor != prev:
                    next_vertex = neighbor
                    break
            
            cycle.append(list(next_vertex))
            prev = current
            current = next_vertex
        
        # Remove duplicate start
        return cycle[:-1]
    
    # Existing methods for undo/redo (unchanged)
    def capture_state(self, cluster_ids, tiling_data):
        """Capture state for undo"""
        affected_tiles = self._get_two_ring_neighborhood(cluster_ids, tiling_data)
        
        undo_info = {
            "tile_states": {},
            "adjacency_graph": {},
            "cluster_ids": cluster_ids
        }
        
        for tile_id in affected_tiles:
            tile = tiling_data["tiles"][tile_id]
            undo_info["tile_states"][tile_id] = {
                "type": tile["type"],
                "vertex_class": tile.get("vertex_class"),
                "local_energy": tile.get("local_energy"),
                "neighbors": tile.get("neighbors", [])[:],
                "vertices": [v[:] for v in tile["vertices"]],
                "center": tile["center"][:],
                "flippable": tile.get("flippable", True),
                "growth_status": tile.get("growth_status", "ungrown")
            }
        
        # Copy adjacency
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
        
        # Restore adjacency
        for key, neighbors in undo_info["adjacency_graph"].items():
            tiling_data["adjacency_graph"][key] = neighbors
        
        # Clear cache
        if hasattr(self.energy_model, '_vertex_class_cache'):
            for tile_id in undo_info["tile_states"]:
                self.energy_model._vertex_class_cache.pop(tile_id, None)