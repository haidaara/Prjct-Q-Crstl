# verification.py
import json
from src.simulation.flip_engine import FlipEngine
from src.simulation.mc_engine import MonteCarloEngine
from src.energy.widom_inspired_energy import WidomInspiredEnergy

def verify_current_state():
    """Check what we have before starting"""
    print("=== VERIFYING CURRENT STATE ===")
    
    # Load a small tiling
    with open('data/processed/penrose_tiling_energy_initialized.json') as f:
        tiling = json.load(f)
    
    # Check existing APIs
    # Placeholder: replace with actual vertex_classifier and energy_model as needed
    vertex_classifier = None  # TODO: Replace with actual classifier
    energy_model = WidomInspiredEnergy()
    flip_engine = FlipEngine(vertex_classifier, energy_model)
    mc_engine = MonteCarloEngine()
    # energy_model already defined above
    
    print("\n1. FlipEngine methods:")
    methods = [m for m in dir(flip_engine) if not m.startswith('_')]
    print(methods)
    
    print("\n2. MC Engine stats:")
    print("Has get_stats?", hasattr(mc_engine, 'get_stats'))
    
    print("\n3. Energy model cache:")
    print("Has clear_cache?", hasattr(energy_model, 'clear_cache'))
    
    print("\n4. Test flip + restore:")
    hexagons = flip_engine.find_flippable_hexagons(tiling)
    if hexagons:
        hexagon = hexagons[0]
        state = flip_engine.capture_state(hexagon, tiling)
        flip_engine.apply_flip(hexagon, tiling)
        flip_engine.restore_state(state, tiling)
        print("✓ Flip + restore completed")
    else:
        print("✗ No flippable hexagons found")
    
    return tiling, flip_engine, mc_engine, energy_model

if __name__ == "__main__":
    verify_current_state()