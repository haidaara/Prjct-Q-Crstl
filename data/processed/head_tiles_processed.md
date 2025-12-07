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
    "energy_model": "WidomInspiredQuasicrystalHamiltonian",
    "energy_initialization_timestamp": "2025-11-16T22:38:28.380348",
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
      "neighbors": [],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.010000000000000476,
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
        0
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.15,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 2,
      "type": "THIN",
      "vertices": [
        [
          -0.809017,
          2.489898
        ],
        [
          -0.0,
          3.077684
        ],
        [
          1.0,
          3.077684
        ],
        [
          0.190983,
          2.489898
        ]
      ],
      "center": [
        0.09549150281252611,
        2.783790911029017
      ],
      "lattice_coords": [
        0,
        -2,
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
          "family": 2,
          "multiple": -1
        }
      ],
      "neighbors": [],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999997,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 3,
      "type": "THICK",
      "vertices": [
        [
          1.309017,
          4.02874
        ],
        [
          1.0,
          3.077684
        ],
        [
          -0.0,
          3.077684
        ],
        [
          0.309017,
          4.02874
        ]
      ],
      "center": [
        0.6545084971874734,
        3.553211795322831
      ],
      "lattice_coords": [
        0,
        -2,
        -2,
        0,
        1
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 4,
          "multiple": 1
        }
      ],
      "neighbors": [
        2
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.005000000000000199,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 4,
      "type": "THICK",
      "vertices": [
        [
          0.309017,
          4.02874
        ],
        [
          -0.0,
          4.979797
        ],
        [
          1.0,
          4.979797
        ],
        [
          1.309017,
          4.02874
        ]
      ],
      "center": [
        0.6545084971874733,
        4.5042683116179845
      ],
      "lattice_coords": [
        0,
        -2,
        -2,
        0,
        1
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 1,
          "multiple": -2
        }
      ],
      "neighbors": [
        3
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.00500000000000008,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 5,
      "type": "THIN",
      "vertices": [
        [
          0.190983,
          5.567582
        ],
        [
          1.0,
          4.979797
        ],
        [
          -0.0,
          4.979797
        ],
        [
          -0.809017,
          5.567582
        ]
      ],
      "center": [
        0.09549150281252577,
        5.273689195911797
      ],
      "lattice_coords": [
        0,
        -3,
        -2,
        1,
        1
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 3,
          "multiple": 1
        }
      ],
      "neighbors": [
        4
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.15,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 6,
      "type": "THIN",
      "vertices": [
        [
          -0.5,
          6.518638
        ],
        [
          0.309017,
          7.106424
        ],
        [
          1.309017,
          7.106424
        ],
        [
          0.5,
          6.518638
        ]
      ],
      "center": [
        0.40450849718747284,
        6.812530964499424
      ],
      "lattice_coords": [
        0,
        -3,
        -2,
        1,
        2
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 2,
          "multiple": -2
        }
      ],
      "neighbors": [],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999997,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 7,
      "type": "THICK",
      "vertices": [
        [
          0.309017,
          7.106424
        ],
        [
          -0.0,
          8.05748
        ],
        [
          1.0,
          8.05748
        ],
        [
          1.309017,
          7.106424
        ]
      ],
      "center": [
        0.6545084971874728,
        7.5819518487932385
      ],
      "lattice_coords": [
        0,
        -3,
        -3,
        1,
        2
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 1,
          "multiple": -3
        }
      ],
      "neighbors": [
        6
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.10500000000000013,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 8,
      "type": "THICK",
      "vertices": [
        [
          1.309017,
          9.008537
        ],
        [
          1.0,
          8.05748
        ],
        [
          -0.0,
          8.05748
        ],
        [
          0.309017,
          9.008537
        ]
      ],
      "center": [
        0.6545084971874726,
        8.533008365088392
      ],
      "lattice_coords": [
        0,
        -4,
        -3,
        1,
        3
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 4,
          "multiple": 3
        }
      ],
      "neighbors": [
        7
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.10500000000000004,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 9,
      "type": "THIN",
      "vertices": [
        [
          0.5,
          9.596322
        ],
        [
          1.309017,
          9.008537
        ],
        [
          0.309017,
          9.008537
        ],
        [
          -0.5,
          9.596322
        ]
      ],
      "center": [
        0.40450849718747245,
        9.302429249382204
      ],
      "lattice_coords": [
        0,
        -4,
        -3,
        2,
        3
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 3,
          "multiple": 2
        }
      ],
      "neighbors": [
        8
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999995,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 10,
      "type": "THIN",
      "vertices": [
        [
          -0.809017,
          10.547378
        ],
        [
          -0.0,
          11.135164
        ],
        [
          1.0,
          11.135164
        ],
        [
          0.190983,
          10.547378
        ]
      ],
      "center": [
        0.09549150281252494,
        10.84127101796983
      ],
      "lattice_coords": [
        0,
        -5,
        -3,
        2,
        3
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 2,
          "multiple": -3
        }
      ],
      "neighbors": [],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.15,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 11,
      "type": "THICK",
      "vertices": [
        [
          1.309017,
          12.08622
        ],
        [
          1.0,
          11.135164
        ],
        [
          -0.0,
          11.135164
        ],
        [
          0.309017,
          12.08622
        ]
      ],
      "center": [
        0.6545084971874723,
        11.610691902263644
      ],
      "lattice_coords": [
        0,
        -5,
        -4,
        2,
        4
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 4,
          "multiple": 4
        }
      ],
      "neighbors": [
        10
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.00500000000000008,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 12,
      "type": "THICK",
      "vertices": [
        [
          0.309017,
          12.08622
        ],
        [
          -0.0,
          13.037277
        ],
        [
          1.0,
          13.037277
        ],
        [
          1.309017,
          12.08622
        ]
      ],
      "center": [
        0.6545084971874722,
        12.561748418558798
      ],
      "lattice_coords": [
        0,
        -5,
        -4,
        2,
        4
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 1,
          "multiple": -5
        }
      ],
      "neighbors": [
        11
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.005000000000000001,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 13,
      "type": "THIN",
      "vertices": [
        [
          0.190983,
          13.625062
        ],
        [
          1.0,
          13.037277
        ],
        [
          -0.0,
          13.037277
        ],
        [
          -0.809017,
          13.625062
        ]
      ],
      "center": [
        0.09549150281252461,
        13.331169302852611
      ],
      "lattice_coords": [
        0,
        -6,
        -4,
        3,
        4
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 3,
          "multiple": 3
        }
      ],
      "neighbors": [
        12
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.15,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 14,
      "type": "THIN",
      "vertices": [
        [
          -0.809017,
          15.527175
        ],
        [
          -0.0,
          16.11496
        ],
        [
          1.0,
          16.11496
        ],
        [
          0.190983,
          15.527175
        ]
      ],
      "center": [
        0.09549150281252405,
        15.82106758773539
      ],
      "lattice_coords": [
        0,
        -7,
        -4,
        3,
        5
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 2,
          "multiple": -4
        }
      ],
      "neighbors": [],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999997,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 15,
      "type": "THICK",
      "vertices": [
        [
          1.309017,
          17.066017
        ],
        [
          1.0,
          16.11496
        ],
        [
          -0.0,
          16.11496
        ],
        [
          0.309017,
          17.066017
        ]
      ],
      "center": [
        0.6545084971874712,
        16.590488472029204
      ],
      "lattice_coords": [
        0,
        -7,
        -5,
        3,
        6
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 4,
          "multiple": 6
        }
      ],
      "neighbors": [
        14
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.10999999999999996,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 16,
      "type": "THIN",
      "vertices": [
        [
          0.5,
          17.653802
        ],
        [
          1.309017,
          17.066017
        ],
        [
          0.309017,
          17.066017
        ],
        [
          -0.5,
          17.653802
        ]
      ],
      "center": [
        0.40450849718747106,
        17.359909356323016
      ],
      "lattice_coords": [
        0,
        -7,
        -5,
        4,
        6
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 3,
          "multiple": 4
        }
      ],
      "neighbors": [
        15
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999997,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 17,
      "type": "THIN",
      "vertices": [
        [
          -0.5,
          19.555915
        ],
        [
          0.309017,
          20.1437
        ],
        [
          1.309017,
          20.1437
        ],
        [
          0.5,
          19.555915
        ]
      ],
      "center": [
        0.4045084971874706,
        19.8498076412058
      ],
      "lattice_coords": [
        0,
        -8,
        -5,
        4,
        7
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 2,
          "multiple": -5
        }
      ],
      "neighbors": [],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.149999999999999,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 18,
      "type": "THICK",
      "vertices": [
        [
          0.309017,
          20.1437
        ],
        [
          -0.0,
          21.094757
        ],
        [
          1.0,
          21.094757
        ],
        [
          1.309017,
          20.1437
        ]
      ],
      "center": [
        0.6545084971874706,
        20.619228525499608
      ],
      "lattice_coords": [
        0,
        -8,
        -6,
        4,
        7
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 1,
          "multiple": -8
        }
      ],
      "neighbors": [
        17
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.105,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 19,
      "type": "THICK",
      "vertices": [
        [
          1.309017,
          22.045813
        ],
        [
          1.0,
          21.094757
        ],
        [
          -0.0,
          21.094757
        ],
        [
          0.309017,
          22.045813
        ]
      ],
      "center": [
        0.6545084971874706,
        21.57028504179476
      ],
      "lattice_coords": [
        0,
        -9,
        -6,
        4,
        8
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 4,
          "multiple": 8
        }
      ],
      "neighbors": [
        18
      ],
      "vertex_class": "LOW_ENERGY",
      "local_energy": 0.10500000000000016,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 20,
      "type": "THIN",
      "vertices": [
        [
          0.5,
          22.633599
        ],
        [
          1.309017,
          22.045813
        ],
        [
          0.309017,
          22.045813
        ],
        [
          -0.5,
          22.633599
        ]
      ],
      "center": [
        0.4045084971874704,
        22.339705926088577
      ],
      "lattice_coords": [
        0,
        -9,
        -6,
        5,
        8
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 3,
          "multiple": 5
        }
      ],
      "neighbors": [
        19
      ],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999988,
      "growth_status": "ungrown",
      "flippable": true
    },
    {
      "id": 21,
      "type": "THIN",
      "vertices": [
        [
          -0.809017,
          23.584655
        ],
        [
          -0.0,
          24.17244
        ],
        [
          1.0,
          24.17244
        ],
        [
          0.190983,
          23.584655
        ]
      ],
      "center": [
        0.09549150281252272,
        23.878547694676204
      ],
      "lattice_coords": [
        0,
        -10,
        -6,
        5,
        8
      ],
      "strips": [
        {
          "family": 0,
          "multiple": 0
        },
        {
          "family": 2,
          "multiple": -6
        }
      ],
      "neighbors": [],
      "vertex_class": "MEDIUM_ENERGY",
      "local_energy": 1.1499999999999995,
      "growth_status": "ungrown",
      "flippable": true
    },