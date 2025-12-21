{
  "metadata": {
    "method": "cut_and_project",
    "offsets": [
      0.0625,
      0.1875,
      0.34375,
      0.15625,
      0.25
    ],
    "window_origin": [
      0.0,
      0.0
    ],
    "window_size": [
      60.0,
      60.0
    ],
    "tile_count": 4406,
    "thick_count": 2718,
    "thin_count": 1688,
    "adjacency_computed": true,
    "coordination_distribution": {
      "2": 103,
      "3": 108,
      "1": 12,
      "4": 4183
    },
    "energy_model": "WidomInspiredQuasicrystalHamiltonian",
    "energy_initialization_timestamp": "2025-11-29T19:06:04.481381",
    "simulation_ready": true,
    "next_phases": [
      "monte_carlo_relaxation",
      "growth_dynamics",
      "phason_analysis"
    ]
  },
  "tiles": [
    {
      "id": 0,
      "type": "THICK",
      "vertices": [
        [
          1.309017,
          0.951057
        ],
        [
          1.0,
          0.0
        ],
        [
          0.0,
          0.0
        ],
        [
          0.309017,
          0.951057
        ]
      ],
      "center": [
        0.6545084971874738,
        0.47552825814757693
      ],
      "lattice_coords": [
        0,
        -1,
        -1,
        -1,
        0
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 4,
          "multiple": 0
        }
      ],
      "neighbors": [
        1,
        2757
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.004000000000000316,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 1,
      "type": "THIN",
      "vertices": [
        [
          0.5,
          1.538842
        ],
        [
          1.309017,
          0.951057
        ],
        [
          0.309017,
          0.951057
        ],
        [
          -0.5,
          1.538842
        ]
      ],
      "center": [
        0.40450849718747367,
        1.2449491424413903
      ],
      "lattice_coords": [
        0,
        -1,
        -1,
        0,
        0
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 3,
          "multiple": 0
        }
      ],
      "neighbors": [
        0,
        3865
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1,
      "growth_status": "ungrown",
      "flippable": true
    },
........