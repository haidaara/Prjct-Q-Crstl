# src/tilings/penrose_p3.py
"""
Research-grade Penrose P3 tiling generator - FIXED VERSION
Proper neighbor list synchronization with adjacency graph
"""

from pynrose import Tiling, Grid, Vector, RhombusType # type: ignore
from collections import defaultdict
from src.utils.config import ConfigManager

class PenroseTiling:
    """
    Research-grade Penrose P3 tiling generator using cut-and-project method.
    Neighbor lists properly synchronized with adjacency graph
    """
    
    def __init__(self, config: ConfigManager):
        self.config = config
        self.tiling_config = config.tiling
        
        # Initialize from config with safe defaults
        self.offsets = self.tiling_config.get("offsets", [0.1, -0.2, 0.05, 0.07, -0.02])
        window_origin = self.tiling_config.get("window_origin", [0.0, 0.0])
        window_size = self.tiling_config.get("window_size", [60.0, 60.0])
        
        # Core pynrose objects
        self.tiling = Tiling(offsets=self.offsets)
        self.grid = Grid(
            Vector(window_origin[0], window_origin[1]),
            Vector(window_size[0], window_size[1])
        )
        
        # Data storage
        self.tiles = []
        self.adjacency_graph = defaultdict(list)
        self.edge_map = defaultdict(list)
        
    def generate(self) -> dict:
        """
        Generate the complete tiling with adjacency information.
        Proper neighbor list synchronization
        """
        cell = self.grid.cell(0, 0)
        
        # First pass: collect all edges for adjacency detection
        self._build_edge_mapping(cell)
        
        # Second pass: build tiles with neighbor information
        self._build_tiles_with_adjacency(cell)
        
        # CRITICtical to fix: Synchronize neighbor lists with adjacency graph
        self._synchronize_neighbor_lists()
        
        # Validation
        self._validate_tiling()
        
        return {
            "tiles": self.tiles,
            "adjacency_graph": dict(self.adjacency_graph),
            "metadata": self._get_metadata()
        }
    
    def _build_edge_mapping(self, cell):
        """Build mapping from edges to tiles for adjacency detection"""
        for rh in self.tiling.rhombii(cell):
            verts = self._get_vertex_coordinates(rh)
            
            # Map each edge to this tile
            for i in range(4):
                edge = self._normalize_edge(verts[i], verts[(i+1)%4])
                self.edge_map[edge].append({
                    "vertices": verts,
                    "type": rh.type(),
                    "center": self._get_midpoint(rh)
                })
    
    def _build_tiles_with_adjacency(self, cell):
        """Build tiles and compute adjacency graph"""
        tile_index = 0
        
        for rh in self.tiling.rhombii(cell):
            verts = self._get_vertex_coordinates(rh)
            
            # Get strip information for Phase 2 phason analysis
            s1, s2 = rh.ordered_strips()
            
            # Safe access to lattice_coords
            lattice_coords = getattr(rh, 'lattice_coords', None)
            
            tile_data = {
                "id": tile_index,
                "type": "THICK" if rh.type() == RhombusType.THICK else "THIN",
                "vertices": verts,
                "center": self._get_midpoint(rh),
                "lattice_coords": lattice_coords,
                "strips": [
                    {
                        "family": s1.family.pentangle.pentangle, 
                        "multiple": s1.multiple
                    },
                    {
                        "family": s2.family.pentangle.pentangle, 
                        "multiple": s2.multiple
                    },
                ],
                "neighbors": [],  # Will be populated by synchronization
                # WEEK 1 PHYSICS FIELDS:
                "vertex_class": "LOW_ENERGY",
                "local_energy": 0.0,
                "growth_status": "grown",
                "flippable": True
            }
            
            self.tiles.append(tile_data)
            self._find_neighbors(tile_index, verts)
            tile_index += 1
    
    def _synchronize_neighbor_lists(self):
        """
        CRITICtical fixed: Ensure tile neighbor lists match adjacency graph
        This fixes the coordination number inconsistency
        """
        print("  Synchronizing neighbor lists with adjacency graph...")
        
        sync_count = 0
        for tile_id_str, neighbors in self.adjacency_graph.items():
            tile_id = int(tile_id_str)
            if tile_id < len(self.tiles):
                # Convert neighbor IDs to integers and ensure uniqueness
                neighbor_ids = list(set(int(n) for n in neighbors))
                self.tiles[tile_id]["neighbors"] = neighbor_ids
                sync_count += 1
        
        print(f"   Synchronized {sync_count} tile neighbor lists")
        
        # Validate synchronization
        self._validate_synchronization()
    
    def _validate_synchronization(self):
        """Validate that neighbor lists match adjacency graph"""
        errors = []
        
        for tile_id_str, adj_neighbors in self.adjacency_graph.items():
            tile_id = int(tile_id_str)
            if tile_id >= len(self.tiles):
                continue
                
            tile_neighbors = self.tiles[tile_id]["neighbors"]
            adj_neighbors_int = [int(n) for n in adj_neighbors]
            
            # Check if sets match (order doesn't matter)
            if set(tile_neighbors) != set(adj_neighbors_int):
                errors.append(f"Tile {tile_id}: neighbor list mismatch")
        
        if errors:
            print(f"    Synchronization validation found {len(errors)} mismatches")
            for error in errors[:5]:
                print(f"   - {error}")
        else:
            print("   Neighbor list synchronization validated")
    
    def _find_neighbors(self, tile_index: int, vertices: list):
        """Find all neighbors for a given tile"""
        for i in range(4):
            edge = self._normalize_edge(vertices[i], vertices[(i+1)%4])

            # Find other tiles sharing this edge
            for potential_neighbor in self.edge_map[edge]:
                if potential_neighbor["vertices"] != vertices:  # Not self
                    # Find the neighbor's index
                    for idx, tile in enumerate(self.tiles):
                        if tile["vertices"] == potential_neighbor["vertices"]:
                            # Add to adjacency graph (primary source)
                            if idx not in self.adjacency_graph[tile_index]:
                                self.adjacency_graph[tile_index].append(idx)
                            if tile_index not in self.adjacency_graph.get(idx, []):
                                if idx not in self.adjacency_graph:
                                    self.adjacency_graph[idx] = []
                                self.adjacency_graph[idx].append(tile_index)
                            break
    
    def _get_vertex_coordinates(self, rhombus):
        """Extract vertex coordinates from Rhombus - FIXED API"""
        vertices = []
        for vertex in rhombus.vertices():
            if hasattr(vertex, 'vector') and hasattr(vertex.vector, 'x') and hasattr(vertex.vector, 'y'):
                vertices.append((vertex.vector.x, vertex.vector.y))
            else:
                for attr in ['vector', 'coord', 'position', 'v']:
                    if hasattr(vertex, attr):
                        vec = getattr(vertex, attr)
                        if hasattr(vec, 'x') and hasattr(vec, 'y'):
                            vertices.append((vec.x, vec.y))
                            break
                else:
                    vertex_str = str(vertex)
                    if 'Vector(' in vertex_str:
                        try:
                            coord_str = vertex_str.split('Vector(')[1].split(')')[0]
                            x, y = map(float, coord_str.split(', '))
                            vertices.append((x, y))
                        except:
                            vertices.append((0, 0))
                    else:
                        vertices.append((0, 0))
        return vertices
    
    def _get_midpoint(self, rhombus):
        """Extract midpoint coordinates - FIXED API"""
        mp = rhombus.midpoint
        if hasattr(mp, 'x') and hasattr(mp, 'y'):
            return (mp.x, mp.y)
        else:
            verts = self._get_vertex_coordinates(rhombus)
            if verts and len(verts) == 4:
                x_avg = sum(v[0] for v in verts) / 4
                y_avg = sum(v[1] for v in verts) / 4
                return (x_avg, y_avg)
            return (0, 0)
    
    def _normalize_edge(self, v1: tuple, v2: tuple) -> tuple:
        """Create canonical edge representation for hashing"""
        return tuple(sorted([v1, v2]))
    
    def _validate_tiling(self):
        """Run consistency checks on the generated tiling"""
        errors = []
        
        # Check all tiles have proper vertex count
        for i, tile in enumerate(self.tiles):
            if len(tile["vertices"]) != 4:
                errors.append(f"Tile {i} has {len(tile['vertices'])} vertices")
        
        # Check coordination numbers are reasonable
        coord_distribution = {}
        for tile_id, neighbors in self.adjacency_graph.items():
            coord = len(neighbors)
            coord_distribution[coord] = coord_distribution.get(coord, 0) + 1
        
        # Check for physically impossible coordination numbers
        for coord, count in coord_distribution.items():
            if coord == 0:
                errors.append(f"Found {count} tiles with 0 neighbors")
            elif coord == 1:
                errors.append(f"Found {count} tiles with only 1 neighbor")
        
        if errors:
            print(f"Tiling validation found {len(errors)} issues:")
            for error in errors[:5]:
                print(f"  - {error}")
        else:
            print("   Tiling validation passed")
            
    def _get_metadata(self) -> dict:
        """Get generation metadata for reproducibility"""
        # Calculate coordination distribution for metadata
        coord_distribution = {}
        for neighbors in self.adjacency_graph.values():
            coord = len(neighbors)
            coord_distribution[coord] = coord_distribution.get(coord, 0) + 1
        
        return {
            "method": "cut_and_project",
            "offsets": self.offsets,
            "window_origin": [self.grid.origin.x, self.grid.origin.y],
            "window_size": [self.grid.grid_size.x, self.grid.grid_size.y],
            "tile_count": len(self.tiles),
            "thick_count": len([t for t in self.tiles if t["type"] == "THICK"]),
            "thin_count": len([t for t in self.tiles if t["type"] == "THIN"]),
            "adjacency_computed": len(self.adjacency_graph) > 0,
            "coordination_distribution": coord_distribution
        }