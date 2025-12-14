randa@Randa:quasi-phason$ python scripts/test_growth_baseline.py
🧪 Testing growth system baseline...
✅ All imports successful
✅ All components instantiated

System is ready for testing!
randa@Randa:quasi-phason$ python scripts/run_growth_experiment.py --config configs/phase2_growth_experiments.toml
🧪 Running growth experiment...
==================================================
Experiment: pores_0.0_20251214_193349
⚙️  Initializing simulation components...
🌱 Initializing growth seed...
✅ Growth seed: 95 tiles initialized at [30.0, 30.0]
📊 Initial energy: 307.85
🌱 Running 10 growth steps...

  Step 1/10
🌿 Growth step 0...
   Running 50 MC steps for healing...
   Running 20 burn-in steps...
📏 Penrose edge length: 1.000000 (from 524 valid edges)

🔄 Physical flip on [3519, 3520, 4136]
  Tile 3519: THIN→THICK, center moved 0.588
  Tile 3520: THICK→THICK, center moved 0.309
  Tile 4136: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3377, 3378, 4133]
  Tile 3377: THIN→THICK, center moved 0.588
  Tile 3378: THICK→THIN, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3471, 3472, 4135]
  Tile 3471: THIN→THICK, center moved 0.588
  Tile 3472: THICK→THICK, center moved 0.309
  Tile 4135: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2410, 2411, 3380]
  Tile 2410: THICK→THIN, center moved 0.309
  Tile 2411: THIN→THICK, center moved 0.309
  Tile 3380: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [979, 980, 4107]
  Tile 979: THIN→THICK, center moved 0.588
  Tile 980: THICK→THICK, center moved 0.309
  Tile 4107: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [903, 904, 2407]
  Tile 903: THICK→THIN, center moved 0.588
  Tile 904: THICK→THICK, center moved 0.309
  Tile 2407: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [901, 902, 3473]
  Tile 901: THIN→THICK, center moved 0.309
  Tile 902: THIN→THIN, center moved 0.809
  Tile 3473: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THIN, center moved 0.809
  Tile 977: THICK→THIN, center moved 0.309
  Tile 3428: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2460, 2461, 4109]
  Tile 2460: THIN→THICK, center moved 0.309
  Tile 2461: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1053, 1054, 2411]
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 1054: THICK→THIN, center moved 0.588
  Tile 2411: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2301, 2302, 3331]
  Tile 2301: THICK→THICK, center moved 0.309
  Tile 2302: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THIN→THICK, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [827, 828, 4136]
  Tile 827: THICK→THIN, center moved 0.588
  Tile 828: THIN→THICK, center moved 0.588
  Tile 4136: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2301, 2302, 3331]
  Tile 2301: THICK→THICK, center moved 0.309
  Tile 2302: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [912, 913, 4160]
  Tile 912: THIN→THICK, center moved 0.588
  Tile 913: THICK→THICK, center moved 0.309
  Tile 4160: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2460, 2461, 4109]
  Tile 2460: THIN→THICK, center moved 0.309
  Tile 2461: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2243, 2244, 3375]
  Tile 2243: THIN→THICK, center moved 0.588
  Tile 2244: THICK→THICK, center moved 0.309
  Tile 3375: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2353, 2354, 3378]
  Tile 2353: THIN→THICK, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
  Tile 3378: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THIN→THICK, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2405, 2406, 3472]
  Tile 2405: THIN→THICK, center moved 0.588
  Tile 2406: THICK→THIN, center moved 0.588
  Tile 3472: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [907, 908, 2352]
  Tile 907: THICK→THIN, center moved 0.588
  Tile 908: THICK→THICK, center moved 0.309
  Tile 2352: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2351, 2352, 3425]
  Tile 2351: THICK→THIN, center moved 0.309
  Tile 2352: THIN→THIN, center moved 0.809
  Tile 3425: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [979, 980, 4107]
  Tile 979: THIN→THICK, center moved 0.588
  Tile 980: THICK→THICK, center moved 0.309
  Tile 4107: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3379, 3380, 4107]
  Tile 3379: THICK→THIN, center moved 0.588
  Tile 3380: THIN→THICK, center moved 0.588
  Tile 4107: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2294, 2295, 3469]
  Tile 2294: THIN→THICK, center moved 0.588
  Tile 2295: THICK→THICK, center moved 0.309
  Tile 3469: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3468, 3469, 4189]
  Tile 3468: THIN→THICK, center moved 0.588
  Tile 3469: THICK→THIN, center moved 0.588
  Tile 4189: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3379, 3380, 4107]
  Tile 3379: THICK→THIN, center moved 0.588
  Tile 3380: THIN→THICK, center moved 0.588
  Tile 4107: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2460, 2461, 4109]
  Tile 2460: THIN→THICK, center moved 0.309
  Tile 2461: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2301, 2302, 3331]
  Tile 2301: THICK→THICK, center moved 0.309
  Tile 2302: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [757, 758, 2348]
  Tile 757: THICK→THIN, center moved 0.588
  Tile 758: THICK→THICK, center moved 0.309
  Tile 2348: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3377, 3378, 4133]
  Tile 3377: THIN→THICK, center moved 0.588
  Tile 3378: THICK→THIN, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THIN, center moved 0.809
  Tile 977: THICK→THIN, center moved 0.309
  Tile 3428: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2301, 2302, 3331]
  Tile 2301: THICK→THICK, center moved 0.309
  Tile 2302: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THIN→THICK, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [903, 904, 2407]
  Tile 903: THIN→THICK, center moved 0.588
  Tile 904: THICK→THICK, center moved 0.309
  Tile 2407: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [904, 905, 2408]
  Tile 904: THICK→THICK, center moved 0.309
  Tile 905: THIN→THICK, center moved 0.588
  Tile 2408: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [827, 828, 4136]
  Tile 827: THICK→THIN, center moved 0.588
  Tile 828: THIN→THICK, center moved 0.588
  Tile 4136: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [978, 979, 2409]
  Tile 978: THICK→THIN, center moved 0.309
  Tile 979: THIN→THIN, center moved 0.809
  Tile 2409: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [907, 908, 2352]
  Tile 907: THICK→THIN, center moved 0.588
  Tile 908: THICK→THICK, center moved 0.309
  Tile 2352: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [758, 759, 4190]
  Tile 758: THICK→THIN, center moved 0.588
  Tile 759: THIN→THICK, center moved 0.588
  Tile 4190: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [979, 980, 4107]
  Tile 979: THIN→THICK, center moved 0.588
  Tile 980: THICK→THICK, center moved 0.309
  Tile 4107: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2349, 2350, 3470]
  Tile 2349: THIN→THICK, center moved 0.588
  Tile 2350: THICK→THICK, center moved 0.309
  Tile 3470: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [759, 760, 2294]
  Tile 759: THIN→THICK, center moved 0.309
  Tile 760: THICK→THIN, center moved 0.309
  Tile 2294: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [830, 831, 3471]
  Tile 830: THICK→THIN, center moved 0.309
  Tile 831: THIN→THIN, center moved 0.809
  Tile 3471: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [756, 757, 2347]
  Tile 756: THIN→THICK, center moved 0.588
  Tile 757: THICK→THIN, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [982, 983, 2355]
  Tile 982: THICK→THICK, center moved 0.309
  Tile 983: THICK→THIN, center moved 0.588
  Tile 2355: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [758, 759, 4190]
  Tile 758: THICK→THIN, center moved 0.588
  Tile 759: THIN→THICK, center moved 0.588
  Tile 4190: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2353, 2354, 3378]
  Tile 2353: THIN→THICK, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
  Tile 3378: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THICK→THIN, center moved 0.588
  Tile 986: THIN→THICK, center moved 0.588
  Tile 2301: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [835, 836, 2297]
  Tile 835: THICK→THIN, center moved 0.588
  Tile 836: THIN→THICK, center moved 0.588
  Tile 2297: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [978, 979, 2409]
  Tile 978: THICK→THIN, center moved 0.309
  Tile 979: THIN→THIN, center moved 0.809
  Tile 2409: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2298, 2299, 4161]
  Tile 2298: THIN→THICK, center moved 0.309
  Tile 2299: THIN→THIN, center moved 0.809
  Tile 4161: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [758, 759, 4190]
  Tile 758: THICK→THIN, center moved 0.588
  Tile 759: THIN→THICK, center moved 0.588
  Tile 4190: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [975, 976, 2463]
  Tile 975: THICK→THIN, center moved 0.588
  Tile 976: THIN→THICK, center moved 0.588
  Tile 2463: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THICK→THIN, center moved 0.588
  Tile 986: THIN→THICK, center moved 0.588
  Tile 2301: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [830, 831, 3471]
  Tile 830: THIN→THIN, center moved 0.809
  Tile 831: THIN→THICK, center moved 0.309
  Tile 3471: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [910, 911, 2300]
  Tile 910: THICK→THIN, center moved 0.588
  Tile 911: THIN→THICK, center moved 0.588
  Tile 2300: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [904, 905, 2408]
  Tile 904: THICK→THICK, center moved 0.309
  Tile 905: THIN→THICK, center moved 0.588
  Tile 2408: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [756, 757, 2347]
  Tile 756: THICK→THIN, center moved 0.588
  Tile 757: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [902, 903, 4108]
  Tile 902: THIN→THICK, center moved 0.588
  Tile 903: THICK→THIN, center moved 0.588
  Tile 4108: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2356, 2357, 3332]
  Tile 2356: THICK→THICK, center moved 0.309
  Tile 2357: THIN→THICK, center moved 0.588
  Tile 3332: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ MC sweep: 8/50 accepted (16.0%)
✅ Growth step 1: added 30 tiles
    New tiles: 30, Defects: 3
    Acceptance rate: 16.0%

  Step 2/10
🌿 Growth step 1...
   Running 50 MC steps for healing...

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THIN, center moved 0.809
  Tile 977: THICK→THIN, center moved 0.309
  Tile 3428: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [986, 987, 3330]
  Tile 986: THIN→THICK, center moved 0.309
  Tile 987: THICK→THIN, center moved 0.309
  Tile 3330: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2298, 2299, 4161]
  Tile 2298: THIN→THICK, center moved 0.309
  Tile 2299: THIN→THIN, center moved 0.809
  Tile 4161: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THIN→THICK, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2356, 2357, 3332]
  Tile 2356: THICK→THICK, center moved 0.309
  Tile 2357: THIN→THICK, center moved 0.588
  Tile 3332: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [975, 976, 2463]
  Tile 975: THICK→THIN, center moved 0.588
  Tile 976: THIN→THICK, center moved 0.588
  Tile 2463: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [982, 983, 2355]
  Tile 982: THICK→THICK, center moved 0.309
  Tile 983: THICK→THIN, center moved 0.588
  Tile 2355: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1053, 1054, 2411]
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 1054: THICK→THIN, center moved 0.588
  Tile 2411: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3332, 3333, 4106]
  Tile 3332: THICK→THIN, center moved 0.588
  Tile 3333: THIN→THICK, center moved 0.588
  Tile 4106: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2346, 2347, 3517]
  Tile 2346: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
  Tile 3517: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2353, 2354, 3378]
  Tile 2353: THIN→THICK, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
  Tile 3378: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [755, 756, 3518]
  Tile 755: THIN→THIN, center moved 0.809
  Tile 756: THIN→THICK, center moved 0.309
  Tile 3518: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3329, 3330, 4160]
  Tile 3329: THICK→THICK, center moved 0.309
  Tile 3330: THIN→THICK, center moved 0.588
  Tile 4160: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THIN, center moved 0.809
  Tile 977: THICK→THIN, center moved 0.309
  Tile 3428: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3329, 3330, 4160]
  Tile 3329: THICK→THICK, center moved 0.309
  Tile 3330: THIN→THICK, center moved 0.588
  Tile 4160: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [982, 983, 2355]
  Tile 982: THICK→THICK, center moved 0.309
  Tile 983: THICK→THIN, center moved 0.588
  Tile 2355: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [907, 908, 2352]
  Tile 907: THICK→THIN, center moved 0.588
  Tile 908: THICK→THICK, center moved 0.309
  Tile 2352: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [986, 987, 3330]
  Tile 986: THIN→THICK, center moved 0.309
  Tile 987: THICK→THIN, center moved 0.309
  Tile 3330: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [910, 911, 2300]
  Tile 910: THICK→THIN, center moved 0.588
  Tile 911: THIN→THICK, center moved 0.588
  Tile 2300: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2241, 2242, 3422]
  Tile 2241: THIN→THIN, center moved 0.809
  Tile 2242: THICK→THIN, center moved 0.309
  Tile 3422: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2346, 2347, 3517]
  Tile 2346: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
  Tile 3517: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [909, 910, 2299]
  Tile 909: THICK→THIN, center moved 0.588
  Tile 910: THICK→THICK, center moved 0.309
  Tile 2299: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2351, 2352, 3425]
  Tile 2351: THICK→THIN, center moved 0.309
  Tile 2352: THIN→THIN, center moved 0.809
  Tile 3425: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [832, 2350, 3471]
  Tile 832: THICK→THICK, center moved 0.309
  Tile 2350: THICK→THIN, center moved 0.588
  Tile 3471: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THICK→THIN, center moved 0.588
  Tile 2298: THIN→THICK, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 829, 2405]
  Tile 828: THIN→THICK, center moved 0.309
  Tile 829: THICK→THIN, center moved 0.309
  Tile 2405: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THICK→THIN, center moved 0.588
  Tile 901: THIN→THICK, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THICK→THIN, center moved 0.588
  Tile 986: THIN→THICK, center moved 0.588
  Tile 2301: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [973, 974, 4081]
  Tile 973: THICK→THIN, center moved 0.588
  Tile 974: THIN→THICK, center moved 0.588
  Tile 4081: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [825, 826, 2459]
  Tile 825: THICK→THICK, center moved 0.309
  Tile 826: THIN→THICK, center moved 0.588
  Tile 2459: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [825, 826, 2459]
  Tile 825: THICK→THICK, center moved 0.309
  Tile 826: THIN→THICK, center moved 0.588
  Tile 2459: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3329, 3330, 4160]
  Tile 3329: THICK→THICK, center moved 0.309
  Tile 3330: THIN→THICK, center moved 0.588
  Tile 4160: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THICK→THIN, center moved 0.588
  Tile 986: THIN→THICK, center moved 0.588
  Tile 2301: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [761, 762, 3468]
  Tile 761: THICK→THIN, center moved 0.309
  Tile 762: THIN→THIN, center moved 0.809
  Tile 3468: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [978, 979, 2409]
  Tile 978: THIN→THICK, center moved 0.309
  Tile 979: THIN→THIN, center moved 0.809
  Tile 2409: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1053, 1054, 2411]
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 1054: THICK→THIN, center moved 0.588
  Tile 2411: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2301, 2302, 3331]
  Tile 2301: THICK→THICK, center moved 0.309
  Tile 2302: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2346, 2347, 3517]
  Tile 2346: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
  Tile 3517: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THICK→THIN, center moved 0.588
  Tile 2298: THIN→THICK, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2353, 2354, 3378]
  Tile 2353: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
  Tile 3378: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3332, 3333, 4106]
  Tile 3332: THICK→THIN, center moved 0.588
  Tile 3333: THIN→THICK, center moved 0.588
  Tile 4106: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [904, 905, 2408]
  Tile 904: THICK→THICK, center moved 0.309
  Tile 905: THIN→THICK, center moved 0.588
  Tile 2408: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2298, 2299, 4161]
  Tile 2298: THIN→THICK, center moved 0.309
  Tile 2299: THIN→THIN, center moved 0.809
  Tile 4161: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3332, 3333, 4106]
  Tile 3332: THICK→THIN, center moved 0.588
  Tile 3333: THIN→THICK, center moved 0.588
  Tile 4106: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ MC sweep: 6/50 accepted (12.0%)
✅ Growth step 2: added 34 tiles
    New tiles: 34, Defects: 5
    Acceptance rate: 12.0%

  Step 3/10
🌿 Growth step 2...
   Running 50 MC steps for healing...

🔄 Physical flip on [2403, 2404, 3519]
  Tile 2403: THIN→THICK, center moved 0.309
  Tile 2404: THICK→THIN, center moved 0.309
  Tile 3519: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1050, 1051, 2466]
  Tile 1050: THICK→THIN, center moved 0.588
  Tile 1051: THIN→THICK, center moved 0.588
  Tile 2466: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2457, 2458, 4137]
  Tile 2457: THIN→THIN, center moved 0.809
  Tile 2458: THIN→THICK, center moved 0.309
  Tile 4137: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [902, 903, 4108]
  Tile 902: THICK→THIN, center moved 0.588
  Tile 903: THIN→THICK, center moved 0.588
  Tile 4108: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2459, 2460, 3521]
  Tile 2459: THICK→THIN, center moved 0.588
  Tile 2460: THIN→THICK, center moved 0.588
  Tile 3521: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [909, 910, 2299]
  Tile 909: THICK→THIN, center moved 0.588
  Tile 910: THICK→THICK, center moved 0.309
  Tile 2299: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3374, 3375, 4187]
  Tile 3374: THIN→THICK, center moved 0.588
  Tile 3375: THICK→THICK, center moved 0.309
  Tile 4187: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [901, 902, 3473]
  Tile 901: THIN→THICK, center moved 0.309
  Tile 902: THIN→THIN, center moved 0.809
  Tile 3473: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2294, 2295, 3469]
  Tile 2294: THIN→THICK, center moved 0.588
  Tile 2295: THICK→THICK, center moved 0.309
  Tile 3469: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 914: THICK→THICK, center moved 0.309
  Tile 2245: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [902, 903, 4108]
  Tile 902: THIN→THICK, center moved 0.588
  Tile 903: THICK→THIN, center moved 0.588
  Tile 4108: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [755, 756, 3518]
  Tile 755: THIN→THICK, center moved 0.309
  Tile 756: THICK→THIN, center moved 0.309
  Tile 3518: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3332, 3333, 4106]
  Tile 3332: THICK→THIN, center moved 0.588
  Tile 3333: THIN→THICK, center moved 0.588
  Tile 4106: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [899, 900, 2461]
  Tile 899: THICK→THIN, center moved 0.588
  Tile 900: THICK→THICK, center moved 0.309
  Tile 2461: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2241, 2242, 3422]
  Tile 2241: THIN→THIN, center moved 0.809
  Tile 2242: THICK→THIN, center moved 0.309
  Tile 3422: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [975, 976, 2463]
  Tile 975: THICK→THIN, center moved 0.588
  Tile 976: THIN→THICK, center moved 0.588
  Tile 2463: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THICK→THIN, center moved 0.588
  Tile 2298: THIN→THICK, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [899, 900, 2461]
  Tile 899: THICK→THIN, center moved 0.588
  Tile 900: THICK→THICK, center moved 0.309
  Tile 2461: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [837, 838, 4188]
  Tile 837: THICK→THICK, center moved 0.309
  Tile 838: THIN→THICK, center moved 0.588
  Tile 4188: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2351, 2352, 3425]
  Tile 2351: THICK→THIN, center moved 0.309
  Tile 2352: THIN→THIN, center moved 0.809
  Tile 3425: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [978, 979, 2409]
  Tile 978: THIN→THICK, center moved 0.309
  Tile 979: THIN→THIN, center moved 0.809
  Tile 2409: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1057, 1058, 2357]
  Tile 1057: THICK→THIN, center moved 0.309
  Tile 1058: THIN→THIN, center moved 0.809
  Tile 2357: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1051, 1052, 3381]
  Tile 1051: THIN→THIN, center moved 0.809
  Tile 1052: THIN→THICK, center moved 0.309
  Tile 3381: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THIN→THICK, center moved 0.588
  Tile 914: THICK→THIN, center moved 0.588
  Tile 2245: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THICK→THIN, center moved 0.588
  Tile 901: THIN→THICK, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [913, 915, 2246]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 915: THIN→THICK, center moved 0.588
  Tile 2246: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [910, 911, 2300]
  Tile 910: THICK→THIN, center moved 0.588
  Tile 911: THIN→THICK, center moved 0.588
  Tile 2300: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [905, 906, 3426]
  Tile 905: THIN→THICK, center moved 0.309
  Tile 906: THIN→THIN, center moved 0.809
  Tile 3426: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [763, 764, 2241]
  Tile 763: THICK→THICK, center moved 0.309
  Tile 764: THICK→THIN, center moved 0.588
  Tile 2241: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1050, 1051, 2466]
  Tile 1050: THICK→THIN, center moved 0.588
  Tile 1051: THIN→THICK, center moved 0.588
  Tile 2466: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [838, 839, 2243]
  Tile 838: THIN→THIN, center moved 0.809
  Tile 839: THICK→THIN, center moved 0.309
  Tile 2243: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2356, 2357, 3332]
  Tile 2356: THICK→THICK, center moved 0.309
  Tile 2357: THIN→THICK, center moved 0.588
  Tile 3332: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [910, 911, 2300]
  Tile 910: THICK→THIN, center moved 0.588
  Tile 911: THIN→THICK, center moved 0.588
  Tile 2300: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [838, 839, 2243]
  Tile 838: THIN→THIN, center moved 0.809
  Tile 839: THIN→THICK, center moved 0.309
  Tile 2243: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [833, 834, 4162]
  Tile 833: THIN→THICK, center moved 0.588
  Tile 834: THICK→THIN, center moved 0.588
  Tile 4162: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [761, 762, 3468]
  Tile 761: THICK→THIN, center moved 0.309
  Tile 762: THIN→THIN, center moved 0.809
  Tile 3468: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [986, 987, 3330]
  Tile 986: THIN→THICK, center moved 0.309
  Tile 987: THICK→THIN, center moved 0.309
  Tile 3330: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2460, 2461, 4109]
  Tile 2460: THIN→THICK, center moved 0.309
  Tile 2461: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2463, 2464, 3429]
  Tile 2463: THICK→THIN, center moved 0.588
  Tile 2464: THIN→THICK, center moved 0.588
  Tile 3429: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2457, 2458, 4137]
  Tile 2457: THIN→THIN, center moved 0.809
  Tile 2458: THIN→THICK, center moved 0.309
  Tile 4137: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [840, 841, 3374]
  Tile 840: THICK→THIN, center moved 0.309
  Tile 841: THIN→THIN, center moved 0.809
  Tile 3374: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [910, 911, 2300]
  Tile 910: THICK→THIN, center moved 0.588
  Tile 911: THIN→THICK, center moved 0.588
  Tile 2300: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 829, 2405]
  Tile 828: THICK→THIN, center moved 0.309
  Tile 829: THIN→THIN, center moved 0.809
  Tile 2405: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2294, 2295, 3469]
  Tile 2294: THIN→THICK, center moved 0.588
  Tile 2295: THICK→THICK, center moved 0.309
  Tile 3469: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1050, 1051, 2466]
  Tile 1050: THICK→THIN, center moved 0.588
  Tile 1051: THIN→THICK, center moved 0.588
  Tile 2466: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2517, 2518, 3430]
  Tile 2517: THIN→THICK, center moved 0.309
  Tile 2518: THICK→THIN, center moved 0.309
  Tile 3430: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3521, 3522, 4110]
  Tile 3521: THICK→THICK, center moved 0.309
  Tile 3522: THIN→THICK, center moved 0.588
  Tile 4110: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [840, 841, 3374]
  Tile 840: THICK→THIN, center moved 0.309
  Tile 841: THIN→THIN, center moved 0.809
  Tile 3374: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ MC sweep: 11/50 accepted (22.0%)
✅ Growth step 3: added 31 tiles
    New tiles: 31, Defects: 5
    Acceptance rate: 22.0%

  Step 4/10
🌿 Growth step 3...
   Running 50 MC steps for healing...

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THICK→THIN, center moved 0.588
  Tile 901: THIN→THICK, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2464, 2465, 4080]
  Tile 2464: THIN→THIN, center moved 0.809
  Tile 2465: THIN→THICK, center moved 0.309
  Tile 4080: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3468, 3469, 4189]
  Tile 3468: THIN→THICK, center moved 0.588
  Tile 3469: THICK→THIN, center moved 0.588
  Tile 4189: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2243, 2244, 3375]
  Tile 2243: THIN→THICK, center moved 0.588
  Tile 2244: THICK→THICK, center moved 0.309
  Tile 3375: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [762, 763, 2240]
  Tile 762: THIN→THICK, center moved 0.588
  Tile 763: THICK→THIN, center moved 0.588
  Tile 2240: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [830, 831, 3471]
  Tile 830: THIN→THICK, center moved 0.309
  Tile 831: THICK→THIN, center moved 0.309
  Tile 3471: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [904, 905, 2408]
  Tile 904: THICK→THICK, center moved 0.309
  Tile 905: THIN→THICK, center moved 0.588
  Tile 2408: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [837, 838, 4188]
  Tile 837: THICK→THICK, center moved 0.309
  Tile 838: THIN→THICK, center moved 0.588
  Tile 4188: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [763, 764, 2241]
  Tile 763: THICK→THICK, center moved 0.309
  Tile 764: THICK→THIN, center moved 0.588
  Tile 2241: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THIN→THICK, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [835, 836, 2297]
  Tile 835: THICK→THIN, center moved 0.588
  Tile 836: THIN→THICK, center moved 0.588
  Tile 2297: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 2406, 3472]
  Tile 828: THIN→THICK, center moved 0.588
  Tile 2406: THICK→THICK, center moved 0.309
  Tile 3472: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2239, 2240, 3467]
  Tile 2239: THIN→THICK, center moved 0.588
  Tile 2240: THICK→THICK, center moved 0.309
  Tile 3467: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3430, 3431, 4054]
  Tile 3430: THIN→THICK, center moved 0.588
  Tile 3431: THICK→THIN, center moved 0.588
  Tile 4054: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 2406, 3472]
  Tile 828: THIN→THICK, center moved 0.588
  Tile 2406: THICK→THICK, center moved 0.309
  Tile 3472: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3379, 3380, 4107]
  Tile 3379: THICK→THIN, center moved 0.588
  Tile 3380: THIN→THICK, center moved 0.588
  Tile 4107: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1061, 1062, 3284]
  Tile 1061: THIN→THICK, center moved 0.309
  Tile 1062: THIN→THIN, center moved 0.809
  Tile 3284: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THICK→THIN, center moved 0.588
  Tile 901: THIN→THICK, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2346, 2347, 3517]
  Tile 2346: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
  Tile 3517: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [686, 687, 3515]
  Tile 686: THIN→THIN, center moved 0.809
  Tile 687: THIN→THICK, center moved 0.309
  Tile 3515: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1051, 1052, 3381]
  Tile 1051: THIN→THIN, center moved 0.809
  Tile 1052: THIN→THICK, center moved 0.309
  Tile 3381: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3329, 3330, 4160]
  Tile 3329: THICK→THICK, center moved 0.309
  Tile 3330: THIN→THICK, center moved 0.588
  Tile 4160: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 829, 2405]
  Tile 828: THIN→THICK, center moved 0.309
  Tile 829: THIN→THIN, center moved 0.809
  Tile 2405: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2348, 2349, 4163]
  Tile 2348: THIN→THIN, center moved 0.809
  Tile 2349: THIN→THICK, center moved 0.309
  Tile 4163: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [902, 903, 4108]
  Tile 902: THICK→THIN, center moved 0.588
  Tile 903: THIN→THICK, center moved 0.588
  Tile 4108: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1057, 1058, 2357]
  Tile 1057: THICK→THIN, center moved 0.309
  Tile 1058: THIN→THIN, center moved 0.809
  Tile 2357: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2246, 2247, 3329]
  Tile 2246: THICK→THIN, center moved 0.588
  Tile 2247: THIN→THICK, center moved 0.588
  Tile 3329: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2348, 2349, 4163]
  Tile 2348: THIN→THIN, center moved 0.809
  Tile 2349: THIN→THICK, center moved 0.309
  Tile 4163: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2460, 2461, 4109]
  Tile 2460: THIN→THICK, center moved 0.309
  Tile 2461: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3430, 3431, 4054]
  Tile 3430: THIN→THICK, center moved 0.588
  Tile 3431: THICK→THIN, center moved 0.588
  Tile 4054: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [751, 752, 3565]
  Tile 751: THIN→THICK, center moved 0.309
  Tile 752: THICK→THIN, center moved 0.309
  Tile 3565: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2457, 2458, 4137]
  Tile 2457: THIN→THIN, center moved 0.809
  Tile 2458: THIN→THICK, center moved 0.309
  Tile 4137: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [840, 841, 3374]
  Tile 840: THIN→THIN, center moved 0.809
  Tile 841: THIN→THICK, center moved 0.309
  Tile 3374: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THIN, center moved 0.809
  Tile 977: THICK→THIN, center moved 0.309
  Tile 3428: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [838, 839, 2243]
  Tile 838: THIN→THIN, center moved 0.809
  Tile 839: THICK→THIN, center moved 0.309
  Tile 2243: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [761, 762, 3468]
  Tile 761: THICK→THIN, center moved 0.309
  Tile 762: THIN→THIN, center moved 0.809
  Tile 3468: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1051, 1052, 3381]
  Tile 1051: THIN→THIN, center moved 0.809
  Tile 1052: THIN→THICK, center moved 0.309
  Tile 3381: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 914: THIN→THICK, center moved 0.588
  Tile 2245: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [830, 831, 3471]
  Tile 830: THIN→THICK, center moved 0.309
  Tile 831: THICK→THIN, center moved 0.309
  Tile 3471: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [825, 826, 2459]
  Tile 825: THICK→THICK, center moved 0.309
  Tile 826: THIN→THICK, center moved 0.588
  Tile 2459: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1060, 1061, 2304]
  Tile 1060: THICK→THICK, center moved 0.309
  Tile 1061: THIN→THICK, center moved 0.588
  Tile 2304: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2460, 2461, 4109]
  Tile 2460: THIN→THICK, center moved 0.309
  Tile 2461: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ MC sweep: 6/50 accepted (12.0%)
✅ Growth step 4: added 29 tiles
    New tiles: 29, Defects: 6
    Acceptance rate: 12.0%

  Step 5/10
🌿 Growth step 4...
   Running 50 MC steps for healing...

🔄 Physical flip on [971, 972, 2516]
  Tile 971: THIN→THICK, center moved 0.588
  Tile 972: THICK→THIN, center moved 0.588
  Tile 2516: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1126, 1127, 3335]
  Tile 1126: THIN→THIN, center moved 0.809
  Tile 1127: THICK→THIN, center moved 0.309
  Tile 3335: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2459, 2460, 3521]
  Tile 2459: THICK→THIN, center moved 0.588
  Tile 2460: THIN→THICK, center moved 0.588
  Tile 3521: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [754, 756, 4164]
  Tile 754: THICK→THICK, center moved 0.309
  Tile 756: THIN→THICK, center moved 0.588
  Tile 4164: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [751, 752, 3565]
  Tile 751: THIN→THICK, center moved 0.309
  Tile 752: THICK→THIN, center moved 0.309
  Tile 3565: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2515, 2516, 3475]
  Tile 2515: THIN→THICK, center moved 0.588
  Tile 2516: THICK→THICK, center moved 0.309
  Tile 3475: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1053, 1054, 2411]
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 1054: THIN→THICK, center moved 0.588
  Tile 2411: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [975, 976, 2463]
  Tile 975: THICK→THIN, center moved 0.588
  Tile 976: THIN→THICK, center moved 0.588
  Tile 2463: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2401, 2402, 3564]
  Tile 2401: THICK→THIN, center moved 0.588
  Tile 2402: THIN→THICK, center moved 0.588
  Tile 3564: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THIN, center moved 0.809
  Tile 977: THICK→THIN, center moved 0.309
  Tile 3428: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1130, 1131, 3287]
  Tile 1130: THIN→THIN, center moved 0.809
  Tile 1131: THIN→THICK, center moved 0.309
  Tile 3287: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [899, 900, 2461]
  Tile 899: THICK→THIN, center moved 0.588
  Tile 900: THICK→THICK, center moved 0.309
  Tile 2461: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THICK→THIN, center moved 0.588
  Tile 901: THIN→THICK, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [832, 2350, 3471]
  Tile 832: THICK→THICK, center moved 0.309
  Tile 2350: THICK→THIN, center moved 0.588
  Tile 3471: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1062, 1063, 4131]
  Tile 1062: THIN→THICK, center moved 0.588
  Tile 1063: THICK→THICK, center moved 0.309
  Tile 4131: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2401, 2402, 3564]
  Tile 2401: THICK→THIN, center moved 0.588
  Tile 2402: THIN→THICK, center moved 0.588
  Tile 3564: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [842, 2189, 3374]
  Tile 842: THICK→THICK, center moved 0.309
  Tile 2189: THICK→THIN, center moved 0.588
  Tile 3374: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [897, 898, 2514]
  Tile 897: THICK→THIN, center moved 0.588
  Tile 898: THICK→THICK, center moved 0.309
  Tile 2514: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [837, 838, 4188]
  Tile 837: THICK→THICK, center moved 0.309
  Tile 838: THIN→THICK, center moved 0.588
  Tile 4188: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [684, 685, 2292]
  Tile 684: THICK→THIN, center moved 0.588
  Tile 685: THICK→THICK, center moved 0.309
  Tile 2292: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [840, 3375, 4187]
  Tile 840: THIN→THICK, center moved 0.588
  Tile 3375: THICK→THIN, center moved 0.588
  Tile 4187: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2348, 2349, 4163]
  Tile 2348: THIN→THIN, center moved 0.809
  Tile 2349: THIN→THICK, center moved 0.309
  Tile 4163: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2346, 2347, 3517]
  Tile 2346: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
  Tile 3517: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3468, 3469, 4189]
  Tile 3468: THIN→THICK, center moved 0.588
  Tile 3469: THICK→THIN, center moved 0.588
  Tile 4189: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [989, 990, 4159]
  Tile 989: THIN→THICK, center moved 0.588
  Tile 990: THICK→THIN, center moved 0.588
  Tile 4159: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2348, 2349, 4163]
  Tile 2348: THIN→THIN, center moved 0.809
  Tile 2349: THIN→THICK, center moved 0.309
  Tile 4163: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THIN→THICK, center moved 0.588
  Tile 914: THICK→THIN, center moved 0.588
  Tile 2245: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [915, 916, 3328]
  Tile 915: THIN→THICK, center moved 0.309
  Tile 916: THIN→THIN, center moved 0.809
  Tile 3328: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2291, 2292, 4217]
  Tile 2291: THIN→THICK, center moved 0.309
  Tile 2292: THIN→THIN, center moved 0.809
  Tile 4217: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THICK→THIN, center moved 0.588
  Tile 2298: THIN→THICK, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2349, 2350, 3470]
  Tile 2349: THIN→THICK, center moved 0.588
  Tile 2350: THICK→THICK, center moved 0.309
  Tile 3470: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [981, 982, 2354]
  Tile 981: THIN→THICK, center moved 0.588
  Tile 982: THICK→THIN, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3285, 3286, 4105]
  Tile 3285: THICK→THIN, center moved 0.588
  Tile 3286: THIN→THICK, center moved 0.588
  Tile 4105: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 829, 2405]
  Tile 828: THICK→THIN, center moved 0.309
  Tile 829: THIN→THIN, center moved 0.809
  Tile 2405: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [910, 911, 2300]
  Tile 910: THICK→THIN, center moved 0.588
  Tile 911: THIN→THICK, center moved 0.588
  Tile 2300: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [758, 759, 4190]
  Tile 758: THIN→THICK, center moved 0.588
  Tile 759: THICK→THIN, center moved 0.588
  Tile 4190: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [764, 765, 4215]
  Tile 764: THICK→THICK, center moved 0.309
  Tile 765: THIN→THICK, center moved 0.588
  Tile 4215: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1051, 1052, 3381]
  Tile 1051: THIN→THIN, center moved 0.809
  Tile 1052: THIN→THICK, center moved 0.309
  Tile 3381: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [823, 824, 4110]
  Tile 823: THIN→THICK, center moved 0.588
  Tile 824: THICK→THICK, center moved 0.309
  Tile 4110: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [986, 987, 3330]
  Tile 986: THIN→THICK, center moved 0.309
  Tile 987: THICK→THIN, center moved 0.309
  Tile 3330: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THICK→THIN, center moved 0.588
  Tile 2298: THIN→THICK, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2463, 2464, 3429]
  Tile 2463: THICK→THIN, center moved 0.588
  Tile 2464: THIN→THICK, center moved 0.588
  Tile 3429: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2291, 2292, 4217]
  Tile 2291: THIN→THICK, center moved 0.309
  Tile 2292: THIN→THIN, center moved 0.809
  Tile 4217: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [838, 839, 2243]
  Tile 838: THIN→THIN, center moved 0.809
  Tile 839: THICK→THIN, center moved 0.309
  Tile 2243: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2243, 2244, 3375]
  Tile 2243: THIN→THICK, center moved 0.588
  Tile 2244: THICK→THICK, center moved 0.309
  Tile 3375: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [682, 683, 2346]
  Tile 682: THIN→THICK, center moved 0.309
  Tile 683: THICK→THIN, center moved 0.309
  Tile 2346: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ MC sweep: 11/50 accepted (22.0%)
✅ Growth step 5: added 24 tiles
    New tiles: 24, Defects: 7
    Acceptance rate: 22.0%

  Step 6/10
🌿 Growth step 5...
   Running 50 MC steps for healing...

🔄 Physical flip on [1058, 1059, 4105]
  Tile 1058: THIN→THICK, center moved 0.588
  Tile 1059: THICK→THIN, center moved 0.588
  Tile 4105: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2248, 2249, 3283]
  Tile 2248: THICK→THIN, center moved 0.309
  Tile 2249: THIN→THICK, center moved 0.309
  Tile 3283: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2248, 2249, 3283]
  Tile 2248: THIN→THICK, center moved 0.309
  Tile 2249: THICK→THIN, center moved 0.309
  Tile 3283: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [988, 989, 2247]
  Tile 988: THICK→THIN, center moved 0.309
  Tile 989: THIN→THICK, center moved 0.309
  Tile 2247: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [684, 685, 2292]
  Tile 684: THICK→THIN, center moved 0.588
  Tile 685: THICK→THICK, center moved 0.309
  Tile 2292: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1132, 1133, 2359]
  Tile 1132: THICK→THICK, center moved 0.309
  Tile 1133: THICK→THIN, center moved 0.588
  Tile 2359: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2291, 2292, 4217]
  Tile 2291: THIN→THICK, center moved 0.309
  Tile 2292: THIN→THIN, center moved 0.809
  Tile 4217: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [832, 2350, 3471]
  Tile 832: THICK→THICK, center moved 0.309
  Tile 2350: THICK→THIN, center moved 0.588
  Tile 3471: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [976, 977, 3428]
  Tile 976: THIN→THICK, center moved 0.309
  Tile 977: THIN→THIN, center moved 0.809
  Tile 3428: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2457, 2458, 4137]
  Tile 2457: THIN→THIN, center moved 0.809
  Tile 2458: THIN→THICK, center moved 0.309
  Tile 4137: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [975, 2463, 3428]
  Tile 975: THICK→THICK, center moved 0.309
  Tile 2463: THICK→THIN, center moved 0.588
  Tile 3428: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [686, 687, 3515]
  Tile 686: THIN→THIN, center moved 0.809
  Tile 687: THICK→THIN, center moved 0.309
  Tile 3515: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3332, 3333, 4106]
  Tile 3332: THICK→THIN, center moved 0.588
  Tile 3333: THIN→THICK, center moved 0.588
  Tile 4106: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2464, 2465, 4080]
  Tile 2464: THIN→THIN, center moved 0.809
  Tile 2465: THIN→THICK, center moved 0.309
  Tile 4080: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2459, 2460, 3521]
  Tile 2459: THIN→THICK, center moved 0.588
  Tile 2460: THICK→THICK, center moved 0.309
  Tile 3521: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [903, 904, 2407]
  Tile 903: THICK→THICK, center moved 0.309
  Tile 904: THICK→THIN, center moved 0.588
  Tile 2407: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [682, 683, 2346]
  Tile 682: THICK→THIN, center moved 0.309
  Tile 683: THIN→THICK, center moved 0.309
  Tile 2346: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [827, 829, 4136]
  Tile 827: THICK→THICK, center moved 0.309
  Tile 829: THIN→THICK, center moved 0.588
  Tile 4136: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [751, 752, 3565]
  Tile 751: THIN→THICK, center moved 0.309
  Tile 752: THICK→THIN, center moved 0.309
  Tile 3565: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2517, 2518, 3430]
  Tile 2517: THIN→THICK, center moved 0.309
  Tile 2518: THICK→THIN, center moved 0.309
  Tile 3430: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [912, 2245, 4160]
  Tile 912: THIN→THICK, center moved 0.588
  Tile 2245: THICK→THIN, center moved 0.588
  Tile 4160: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [823, 824, 4110]
  Tile 823: THICK→THIN, center moved 0.588
  Tile 824: THICK→THICK, center moved 0.309
  Tile 4110: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2513, 2514, 3522]
  Tile 2513: THICK→THIN, center moved 0.309
  Tile 2514: THIN→THIN, center moved 0.809
  Tile 3522: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [684, 685, 2292]
  Tile 684: THICK→THIN, center moved 0.588
  Tile 685: THICK→THICK, center moved 0.309
  Tile 2292: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1053, 1054, 2411]
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 1054: THICK→THIN, center moved 0.588
  Tile 2411: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1051, 1052, 3381]
  Tile 1051: THIN→THIN, center moved 0.809
  Tile 1052: THIN→THICK, center moved 0.309
  Tile 3381: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1130, 1131, 3287]
  Tile 1130: THIN→THIN, center moved 0.809
  Tile 1131: THICK→THIN, center moved 0.309
  Tile 3287: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THIN→THICK, center moved 0.588
  Tile 901: THICK→THIN, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2401, 2402, 3564]
  Tile 2401: THICK→THIN, center moved 0.588
  Tile 2402: THIN→THICK, center moved 0.588
  Tile 3564: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [824, 825, 2458]
  Tile 824: THICK→THICK, center moved 0.309
  Tile 825: THICK→THIN, center moved 0.588
  Tile 2458: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 914: THIN→THICK, center moved 0.588
  Tile 2245: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [840, 3375, 4187]
  Tile 840: THIN→THICK, center moved 0.588
  Tile 3375: THICK→THIN, center moved 0.588
  Tile 4187: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [840, 3375, 4187]
  Tile 840: THIN→THICK, center moved 0.588
  Tile 3375: THICK→THIN, center moved 0.588
  Tile 4187: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [909, 910, 2299]
  Tile 909: THICK→THIN, center moved 0.588
  Tile 910: THICK→THICK, center moved 0.309
  Tile 2299: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2515, 2516, 3475]
  Tile 2515: THIN→THICK, center moved 0.588
  Tile 2516: THICK→THICK, center moved 0.309
  Tile 3475: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3332, 3333, 4106]
  Tile 3332: THIN→THICK, center moved 0.588
  Tile 3333: THICK→THIN, center moved 0.588
  Tile 4106: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [897, 898, 2514]
  Tile 897: THICK→THIN, center moved 0.588
  Tile 898: THICK→THICK, center moved 0.309
  Tile 2514: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1132, 1133, 2359]
  Tile 1132: THICK→THIN, center moved 0.588
  Tile 1133: THIN→THICK, center moved 0.588
  Tile 2359: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [755, 756, 3518]
  Tile 755: THICK→THIN, center moved 0.309
  Tile 756: THIN→THIN, center moved 0.809
  Tile 3518: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [764, 765, 4215]
  Tile 764: THICK→THIN, center moved 0.588
  Tile 765: THICK→THICK, center moved 0.309
  Tile 4215: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [824, 825, 2458]
  Tile 824: THICK→THICK, center moved 0.309
  Tile 825: THIN→THICK, center moved 0.588
  Tile 2458: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2459, 3522, 4110]
  Tile 2459: THICK→THIN, center moved 0.588
  Tile 3522: THIN→THICK, center moved 0.588
  Tile 4110: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3329, 3330, 4160]
  Tile 3329: THICK→THICK, center moved 0.309
  Tile 3330: THIN→THICK, center moved 0.588
  Tile 4160: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [682, 683, 2346]
  Tile 682: THIN→THICK, center moved 0.309
  Tile 683: THICK→THIN, center moved 0.309
  Tile 2346: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [764, 766, 3421]
  Tile 764: THIN→THIN, center moved 0.809
  Tile 766: THIN→THICK, center moved 0.309
  Tile 3421: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1058, 1059, 4105]
  Tile 1058: THIN→THICK, center moved 0.588
  Tile 1059: THICK→THIN, center moved 0.588
  Tile 4105: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THIN→THICK, center moved 0.588
  Tile 4133: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2243, 2244, 3375]
  Tile 2243: THIN→THICK, center moved 0.588
  Tile 2244: THICK→THICK, center moved 0.309
  Tile 3375: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ MC sweep: 23/50 accepted (46.0%)
✅ Growth step 6: added 16 tiles
    New tiles: 16, Defects: 7
    Acceptance rate: 46.0%

  Step 7/10
🌿 Growth step 6...
   Running 50 MC steps for healing...

🔄 Physical flip on [832, 2350, 3471]
  Tile 832: THICK→THICK, center moved 0.309
  Tile 2350: THICK→THIN, center moved 0.588
  Tile 3471: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2301, 2302, 3331]
  Tile 2301: THICK→THICK, center moved 0.309
  Tile 2302: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [897, 898, 2514]
  Tile 897: THICK→THIN, center moved 0.588
  Tile 898: THICK→THICK, center moved 0.309
  Tile 2514: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [828, 2406, 3472]
  Tile 828: THIN→THICK, center moved 0.588
  Tile 2406: THICK→THICK, center moved 0.309
  Tile 3472: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [748, 749, 4138]
  Tile 748: THICK→THIN, center moved 0.588
  Tile 749: THIN→THICK, center moved 0.588
  Tile 4138: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [754, 756, 2404]
  Tile 754: THICK→THIN, center moved 0.309
  Tile 756: THIN→THICK, center moved 0.309
  Tile 2404: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [827, 829, 4136]
  Tile 827: THICK→THICK, center moved 0.309
  Tile 829: THICK→THIN, center moved 0.588
  Tile 4136: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2248, 2249, 3283]
  Tile 2248: THICK→THIN, center moved 0.309
  Tile 2249: THIN→THICK, center moved 0.309
  Tile 3283: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [682, 683, 2346]
  Tile 682: THICK→THIN, center moved 0.309
  Tile 683: THIN→THICK, center moved 0.309
  Tile 2346: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THICK→THIN, center moved 0.588
  Tile 901: THIN→THICK, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [613, 614, 2236]
  Tile 613: THICK→THIN, center moved 0.309
  Tile 614: THIN→THIN, center moved 0.809
  Tile 2236: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [823, 824, 4110]
  Tile 823: THIN→THICK, center moved 0.588
  Tile 824: THICK→THIN, center moved 0.588
  Tile 4110: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2517, 2518, 3430]
  Tile 2517: THIN→THICK, center moved 0.309
  Tile 2518: THICK→THIN, center moved 0.309
  Tile 3430: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [977, 3427, 4108]
  Tile 977: THIN→THICK, center moved 0.588
  Tile 3427: THICK→THIN, center moved 0.588
  Tile 4108: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THICK→THIN, center moved 0.588
  Tile 986: THIN→THICK, center moved 0.588
  Tile 2301: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [903, 904, 2407]
  Tile 903: THICK→THIN, center moved 0.588
  Tile 904: THIN→THICK, center moved 0.588
  Tile 2407: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [754, 756, 2404]
  Tile 754: THIN→THICK, center moved 0.309
  Tile 756: THICK→THIN, center moved 0.309
  Tile 2404: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2290, 2291, 3561]
  Tile 2290: THICK→THIN, center moved 0.588
  Tile 2291: THIN→THICK, center moved 0.588
  Tile 3561: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [906, 907, 4134]
  Tile 906: THIN→THICK, center moved 0.588
  Tile 907: THICK→THICK, center moved 0.309
  Tile 4134: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2513, 2514, 3522]
  Tile 2513: THICK→THIN, center moved 0.309
  Tile 2514: THIN→THIN, center moved 0.809
  Tile 3522: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2290, 2291, 3561]
  Tile 2290: THIN→THICK, center moved 0.588
  Tile 2291: THICK→THIN, center moved 0.588
  Tile 3561: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [897, 898, 2514]
  Tile 897: THICK→THIN, center moved 0.588
  Tile 898: THICK→THICK, center moved 0.309
  Tile 2514: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2291, 2292, 4217]
  Tile 2291: THIN→THICK, center moved 0.309
  Tile 2292: THIN→THIN, center moved 0.809
  Tile 4217: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2304, 2305, 3285]
  Tile 2304: THICK→THIN, center moved 0.588
  Tile 2305: THIN→THICK, center moved 0.588
  Tile 3285: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2517, 2518, 3430]
  Tile 2517: THIN→THICK, center moved 0.309
  Tile 2518: THICK→THIN, center moved 0.309
  Tile 3430: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2403, 2404, 3519]
  Tile 2403: THICK→THIN, center moved 0.309
  Tile 2404: THIN→THICK, center moved 0.309
  Tile 3519: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1063, 1064, 2249]
  Tile 1063: THICK→THICK, center moved 0.309
  Tile 1064: THICK→THIN, center moved 0.588
  Tile 2249: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [764, 765, 4215]
  Tile 764: THIN→THICK, center moved 0.588
  Tile 765: THICK→THICK, center moved 0.309
  Tile 4215: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3422, 3423, 4188]
  Tile 3422: THIN→THICK, center moved 0.588
  Tile 3423: THICK→THIN, center moved 0.588
  Tile 4188: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [902, 904, 4108]
  Tile 902: THIN→THICK, center moved 0.588
  Tile 904: THICK→THIN, center moved 0.588
  Tile 4108: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [826, 3520, 4136]
  Tile 826: THIN→THICK, center moved 0.309
  Tile 3520: THICK→THIN, center moved 0.309
  Tile 4136: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [613, 614, 2236]
  Tile 613: THICK→THIN, center moved 0.309
  Tile 614: THIN→THIN, center moved 0.809
  Tile 2236: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [913, 915, 2246]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 915: THIN→THICK, center moved 0.588
  Tile 2246: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2360, 2361, 3244]
  Tile 2360: THIN→THICK, center moved 0.588
  Tile 2361: THICK→THICK, center moved 0.309
  Tile 3244: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2457, 2458, 4137]
  Tile 2457: THIN→THICK, center moved 0.309
  Tile 2458: THIN→THIN, center moved 0.809
  Tile 4137: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3282, 3283, 4159]
  Tile 3282: THICK→THIN, center moved 0.588
  Tile 3283: THIN→THICK, center moved 0.588
  Tile 4159: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THIN→THICK, center moved 0.588
  Tile 986: THICK→THICK, center moved 0.309
  Tile 2301: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2241, 2242, 3422]
  Tile 2241: THIN→THIN, center moved 0.809
  Tile 2242: THICK→THIN, center moved 0.309
  Tile 3422: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [988, 989, 2247]
  Tile 988: THIN→THICK, center moved 0.309
  Tile 989: THICK→THIN, center moved 0.309
  Tile 2247: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [829, 2405, 3519]
  Tile 829: THICK→THIN, center moved 0.588
  Tile 2405: THICK→THICK, center moved 0.309
  Tile 3519: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [838, 839, 2243]
  Tile 838: THIN→THIN, center moved 0.809
  Tile 839: THICK→THIN, center moved 0.309
  Tile 2243: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [764, 765, 4215]
  Tile 764: THIN→THICK, center moved 0.588
  Tile 765: THICK→THICK, center moved 0.309
  Tile 4215: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [827, 828, 829]
  Tile 827: THICK→THIN, center moved 0.309
  Tile 828: THIN→THIN, center moved 0.809
  Tile 829: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2459, 2460, 3521]
  Tile 2459: THICK→THICK, center moved 0.309
  Tile 2460: THICK→THIN, center moved 0.588
  Tile 3521: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 914: THIN→THICK, center moved 0.588
  Tile 2245: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [907, 908, 2352]
  Tile 907: THICK→THIN, center moved 0.588
  Tile 908: THICK→THICK, center moved 0.309
  Tile 2352: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [990, 991, 3282]
  Tile 990: THICK→THIN, center moved 0.309
  Tile 991: THIN→THICK, center moved 0.309
  Tile 3282: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [611, 612, 3560]
  Tile 611: THIN→THIN, center moved 0.809
  Tile 612: THICK→THIN, center moved 0.309
  Tile 3560: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2349, 2350, 3470]
  Tile 2349: THIN→THICK, center moved 0.588
  Tile 2350: THICK→THICK, center moved 0.309
  Tile 3470: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ MC sweep: 16/50 accepted (32.0%)
✅ Growth step 7: added 13 tiles
    New tiles: 13, Defects: 12
    Acceptance rate: 32.0%

  Step 8/10
🌿 Growth step 7...
   Running 50 MC steps for healing...

🔄 Physical flip on [2355, 2356, 3332]
  Tile 2355: THIN→THICK, center moved 0.309
  Tile 2356: THICK→THIN, center moved 0.309
  Tile 3332: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2412, 2413, 3334]
  Tile 2412: THICK→THICK, center moved 0.309
  Tile 2413: THIN→THICK, center moved 0.588
  Tile 3334: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [988, 989, 2247]
  Tile 988: THICK→THIN, center moved 0.309
  Tile 989: THIN→THIN, center moved 0.809
  Tile 2247: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2360, 2361, 3244]
  Tile 2360: THIN→THICK, center moved 0.588
  Tile 2361: THICK→THICK, center moved 0.309
  Tile 3244: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [686, 687, 3515]
  Tile 686: THIN→THIN, center moved 0.809
  Tile 687: THICK→THIN, center moved 0.309
  Tile 3515: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2241, 2242, 3422]
  Tile 2241: THIN→THIN, center moved 0.809
  Tile 2242: THICK→THIN, center moved 0.309
  Tile 3422: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [675, 676, 2455]
  Tile 675: THICK→THICK, center moved 0.309
  Tile 676: THIN→THICK, center moved 0.588
  Tile 2455: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [827, 3519, 4136]
  Tile 827: THIN→THICK, center moved 0.309
  Tile 3519: THICK→THIN, center moved 0.309
  Tile 4136: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1126, 1127, 3335]
  Tile 1126: THIN→THIN, center moved 0.809
  Tile 1127: THICK→THIN, center moved 0.309
  Tile 3335: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2348, 2349, 4163]
  Tile 2348: THIN→THIN, center moved 0.809
  Tile 2349: THIN→THICK, center moved 0.309
  Tile 4163: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [833, 834, 4162]
  Tile 833: THICK→THIN, center moved 0.588
  Tile 834: THIN→THICK, center moved 0.588
  Tile 4162: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [755, 756, 3518]
  Tile 755: THIN→THICK, center moved 0.309
  Tile 756: THIN→THIN, center moved 0.809
  Tile 3518: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [902, 904, 4108]
  Tile 902: THICK→THICK, center moved 0.309
  Tile 904: THIN→THICK, center moved 0.588
  Tile 4108: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2401, 2402, 3564]
  Tile 2401: THICK→THIN, center moved 0.588
  Tile 2402: THIN→THICK, center moved 0.588
  Tile 3564: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1062, 1063, 4131]
  Tile 1062: THIN→THICK, center moved 0.588
  Tile 1063: THICK→THICK, center moved 0.309
  Tile 4131: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2243, 2244, 3375]
  Tile 2243: THIN→THICK, center moved 0.588
  Tile 2244: THICK→THICK, center moved 0.309
  Tile 3375: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3334, 3335, 4079]
  Tile 3334: THICK→THIN, center moved 0.588
  Tile 3335: THIN→THICK, center moved 0.588
  Tile 4079: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2302, 2303, 4132]
  Tile 2302: THIN→THIN, center moved 0.809
  Tile 2303: THIN→THICK, center moved 0.309
  Tile 4132: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [754, 756, 2404]
  Tile 754: THICK→THIN, center moved 0.309
  Tile 756: THIN→THICK, center moved 0.309
  Tile 2404: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [827, 3519, 4136]
  Tile 827: THIN→THICK, center moved 0.309
  Tile 3519: THICK→THIN, center moved 0.309
  Tile 4136: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [984, 2356, 3331]
  Tile 984: THICK→THICK, center moved 0.309
  Tile 2356: THIN→THICK, center moved 0.588
  Tile 3331: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1134, 1135, 2305]
  Tile 1134: THICK→THIN, center moved 0.309
  Tile 1135: THIN→THICK, center moved 0.309
  Tile 2305: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3379, 3380, 4107]
  Tile 3379: THICK→THIN, center moved 0.588
  Tile 3380: THIN→THICK, center moved 0.588
  Tile 4107: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [690, 691, 3466]
  Tile 690: THICK→THIN, center moved 0.309
  Tile 691: THIN→THICK, center moved 0.309
  Tile 3466: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2351, 2352, 3425]
  Tile 2351: THICK→THIN, center moved 0.309
  Tile 2352: THIN→THIN, center moved 0.809
  Tile 3425: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2291, 2292, 4217]
  Tile 2291: THICK→THIN, center moved 0.309
  Tile 2292: THIN→THICK, center moved 0.309
  Tile 4217: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [686, 687, 3515]
  Tile 686: THIN→THIN, center moved 0.809
  Tile 687: THICK→THIN, center moved 0.309
  Tile 3515: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2513, 2514, 3522]
  Tile 2513: THICK→THIN, center moved 0.309
  Tile 2514: THIN→THIN, center moved 0.809
  Tile 3522: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [916, 917, 4186]
  Tile 916: THIN→THICK, center moved 0.588
  Tile 917: THICK→THIN, center moved 0.588
  Tile 4186: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1132, 3287, 4077]
  Tile 1132: THICK→THIN, center moved 0.588
  Tile 3287: THIN→THICK, center moved 0.588
  Tile 4077: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [827, 828, 829]
  Tile 827: THIN→THIN, center moved 0.809
  Tile 828: THIN→THICK, center moved 0.309
  Tile 829: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [987, 988, 3329]
  Tile 987: THICK→THICK, center moved 0.309
  Tile 988: THIN→THICK, center moved 0.588
  Tile 3329: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [684, 685, 2291]
  Tile 684: THICK→THIN, center moved 0.588
  Tile 685: THICK→THICK, center moved 0.309
  Tile 2291: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1053, 1054, 2411]
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 1054: THIN→THICK, center moved 0.588
  Tile 2411: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1062, 1063, 4131]
  Tile 1062: THICK→THICK, center moved 0.309
  Tile 1063: THICK→THIN, center moved 0.588
  Tile 4131: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [754, 756, 2404]
  Tile 754: THICK→THIN, center moved 0.309
  Tile 756: THIN→THICK, center moved 0.309
  Tile 2404: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THIN→THICK, center moved 0.588
  Tile 2298: THICK→THIN, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [988, 989, 2247]
  Tile 988: THIN→THIN, center moved 0.809
  Tile 989: THIN→THICK, center moved 0.309
  Tile 2247: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1052, 1053, 4079]
  Tile 1052: THIN→THICK, center moved 0.588
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 4079: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [748, 749, 4138]
  Tile 748: THICK→THIN, center moved 0.588
  Tile 749: THIN→THICK, center moved 0.588
  Tile 4138: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [900, 901, 2462]
  Tile 900: THIN→THICK, center moved 0.588
  Tile 901: THICK→THIN, center moved 0.588
  Tile 2462: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2239, 2240, 3467]
  Tile 2239: THICK→THIN, center moved 0.588
  Tile 2240: THICK→THICK, center moved 0.309
  Tile 3467: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2459, 2460, 3521]
  Tile 2459: THICK→THICK, center moved 0.309
  Tile 2460: THICK→THIN, center moved 0.588
  Tile 3521: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2517, 2518, 3430]
  Tile 2517: THIN→THICK, center moved 0.309
  Tile 2518: THICK→THIN, center moved 0.309
  Tile 3430: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [762, 763, 2240]
  Tile 762: THIN→THICK, center moved 0.588
  Tile 763: THICK→THIN, center moved 0.588
  Tile 2240: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1064, 2249, 4131]
  Tile 1064: THICK→THIN, center moved 0.588
  Tile 2249: THIN→THICK, center moved 0.588
  Tile 4131: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [980, 981, 3379]
  Tile 980: THICK→THIN, center moved 0.309
  Tile 981: THIN→THICK, center moved 0.309
  Tile 3379: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [902, 903, 2407]
  Tile 902: THICK→THICK, center moved 0.309
  Tile 903: THIN→THICK, center moved 0.588
  Tile 2407: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2515, 2516, 3475]
  Tile 2515: THIN→THICK, center moved 0.588
  Tile 2516: THICK→THICK, center moved 0.309
  Tile 3475: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [751, 752, 3565]
  Tile 751: THIN→THICK, center moved 0.309
  Tile 752: THICK→THIN, center moved 0.309
  Tile 3565: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ MC sweep: 23/50 accepted (46.0%)
✅ Growth step 8: added 17 tiles
    New tiles: 17, Defects: 16
    Acceptance rate: 46.0%

  Step 9/10
🌿 Growth step 8...
   Running 50 MC steps for healing...

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THIN→THICK, center moved 0.588
  Tile 984: THICK→THICK, center moved 0.309
  Tile 4133: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [840, 3375, 4187]
  Tile 840: THIN→THICK, center moved 0.588
  Tile 3375: THICK→THIN, center moved 0.588
  Tile 4187: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2304, 2305, 3285]
  Tile 2304: THICK→THIN, center moved 0.588
  Tile 2305: THIN→THICK, center moved 0.588
  Tile 3285: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [975, 2463, 3428]
  Tile 975: THICK→THIN, center moved 0.588
  Tile 2463: THIN→THICK, center moved 0.588
  Tile 3428: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [897, 898, 2514]
  Tile 897: THICK→THIN, center moved 0.588
  Tile 898: THICK→THICK, center moved 0.309
  Tile 2514: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1064, 2249, 4131]
  Tile 1064: THICK→THIN, center moved 0.588
  Tile 2249: THIN→THICK, center moved 0.588
  Tile 4131: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [913, 915, 2246]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 915: THIN→THICK, center moved 0.588
  Tile 2246: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2360, 2361, 3244]
  Tile 2360: THIN→THICK, center moved 0.588
  Tile 2361: THICK→THICK, center moved 0.309
  Tile 3244: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3288, 3289, 4051]
  Tile 3288: THIN→THICK, center moved 0.588
  Tile 3289: THICK→THIN, center moved 0.588
  Tile 4051: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [685, 686, 2292]
  Tile 685: THICK→THICK, center moved 0.309
  Tile 686: THIN→THICK, center moved 0.588
  Tile 2292: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2187, 2188, 4214]
  Tile 2187: THIN→THIN, center moved 0.809
  Tile 2188: THIN→THICK, center moved 0.309
  Tile 4214: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2513, 2514, 3522]
  Tile 2513: THICK→THIN, center moved 0.309
  Tile 2514: THIN→THIN, center moved 0.809
  Tile 3522: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [830, 831, 3471]
  Tile 830: THIN→THICK, center moved 0.309
  Tile 831: THICK→THIN, center moved 0.309
  Tile 3471: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [613, 614, 2236]
  Tile 613: THICK→THIN, center moved 0.309
  Tile 614: THIN→THIN, center moved 0.809
  Tile 2236: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2464, 2465, 4080]
  Tile 2464: THIN→THIN, center moved 0.809
  Tile 2465: THIN→THICK, center moved 0.309
  Tile 4080: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3608, 3609, 4138]
  Tile 3608: THIN→THICK, center moved 0.588
  Tile 3609: THICK→THIN, center moved 0.588
  Tile 4138: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [897, 898, 2514]
  Tile 897: THICK→THIN, center moved 0.588
  Tile 898: THICK→THICK, center moved 0.309
  Tile 2514: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2459, 3522, 4110]
  Tile 2459: THICK→THIN, center moved 0.588
  Tile 3522: THIN→THICK, center moved 0.588
  Tile 4110: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THICK→THICK, center moved 0.309
  Tile 4133: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2511, 2512, 3567]
  Tile 2511: THICK→THIN, center moved 0.588
  Tile 2512: THIN→THICK, center moved 0.588
  Tile 3567: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2461, 3521, 4109]
  Tile 2461: THIN→THICK, center moved 0.309
  Tile 3521: THIN→THIN, center moved 0.809
  Tile 4109: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2290, 3561, 4217]
  Tile 2290: THICK→THIN, center moved 0.588
  Tile 3561: THICK→THICK, center moved 0.309
  Tile 4217: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1132, 2359, 2360]
  Tile 1132: THIN→THICK, center moved 0.309
  Tile 2359: THICK→THIN, center moved 0.309
  Tile 2360: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [837, 838, 4188]
  Tile 837: THICK→THICK, center moved 0.309
  Tile 838: THIN→THICK, center moved 0.588
  Tile 4188: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [990, 991, 3282]
  Tile 990: THIN→THIN, center moved 0.809
  Tile 991: THICK→THIN, center moved 0.309
  Tile 3282: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [827, 828, 829]
  Tile 827: THIN→THIN, center moved 0.809
  Tile 828: THICK→THIN, center moved 0.309
  Tile 829: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2353, 2354, 3378]
  Tile 2353: THIN→THICK, center moved 0.588
  Tile 2354: THICK→THICK, center moved 0.309
  Tile 3378: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [830, 3472, 4135]
  Tile 830: THIN→THICK, center moved 0.588
  Tile 3472: THICK→THIN, center moved 0.588
  Tile 4135: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [690, 691, 3466]
  Tile 690: THIN→THICK, center moved 0.309
  Tile 691: THICK→THIN, center moved 0.309
  Tile 3466: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [747, 748, 2510]
  Tile 747: THICK→THIN, center moved 0.588
  Tile 748: THICK→THICK, center moved 0.309
  Tile 2510: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2290, 3561, 4217]
  Tile 2290: THIN→THICK, center moved 0.588
  Tile 3561: THICK→THICK, center moved 0.309
  Tile 4217: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1061, 1063, 3284]
  Tile 1061: THIN→THICK, center moved 0.309
  Tile 1063: THIN→THIN, center moved 0.809
  Tile 3284: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [3564, 3565, 4165]
  Tile 3564: THICK→THIN, center moved 0.588
  Tile 3565: THIN→THICK, center moved 0.588
  Tile 4165: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2348, 2349, 4163]
  Tile 2348: THIN→THIN, center moved 0.809
  Tile 2349: THICK→THIN, center moved 0.309
  Tile 4163: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2187, 2188, 4214]
  Tile 2187: THIN→THIN, center moved 0.809
  Tile 2188: THIN→THICK, center moved 0.309
  Tile 4214: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [983, 984, 4133]
  Tile 983: THICK→THIN, center moved 0.588
  Tile 984: THICK→THICK, center moved 0.309
  Tile 4133: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2464, 2465, 4080]
  Tile 2464: THIN→THIN, center moved 0.809
  Tile 2465: THIN→THICK, center moved 0.309
  Tile 4080: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2508, 2509, 3609]
  Tile 2508: THIN→THICK, center moved 0.588
  Tile 2509: THICK→THICK, center moved 0.309
  Tile 3609: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [990, 991, 3282]
  Tile 990: THIN→THIN, center moved 0.809
  Tile 991: THICK→THIN, center moved 0.309
  Tile 3282: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [916, 917, 4186]
  Tile 916: THIN→THICK, center moved 0.588
  Tile 917: THICK→THIN, center moved 0.588
  Tile 4186: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1132, 2359, 2360]
  Tile 1132: THICK→THIN, center moved 0.309
  Tile 2359: THIN→THIN, center moved 0.809
  Tile 2360: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1052, 1053, 4079]
  Tile 1052: THICK→THIN, center moved 0.588
  Tile 1053: THICK→THICK, center moved 0.309
  Tile 4079: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3288, 3289, 4051]
  Tile 3288: THIN→THICK, center moved 0.588
  Tile 3289: THICK→THIN, center moved 0.588
  Tile 4051: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [991, 3283, 4159]
  Tile 991: THIN→THICK, center moved 0.588
  Tile 3283: THICK→THICK, center moved 0.309
  Tile 4159: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2355, 2356, 3332]
  Tile 2355: THICK→THIN, center moved 0.309
  Tile 2356: THIN→THICK, center moved 0.309
  Tile 3332: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1050, 1051, 2466]
  Tile 1050: THICK→THIN, center moved 0.588
  Tile 1051: THIN→THICK, center moved 0.588
  Tile 2466: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [990, 992, 2193]
  Tile 990: THIN→THICK, center moved 0.588
  Tile 992: THICK→THICK, center moved 0.309
  Tile 2193: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [970, 971, 3476]
  Tile 970: THICK→THIN, center moved 0.309
  Tile 971: THIN→THICK, center moved 0.309
  Tile 3476: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2515, 2516, 3475]
  Tile 2515: THIN→THICK, center moved 0.588
  Tile 2516: THICK→THICK, center moved 0.309
  Tile 3475: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485
✅ MC sweep: 16/50 accepted (32.0%)
✅ Growth step 9: added 13 tiles
    New tiles: 13, Defects: 18
    Acceptance rate: 32.0%

  Step 10/10
🌿 Growth step 9...
   Running 50 MC steps for healing...

🔄 Physical flip on [907, 908, 2352]
  Tile 907: THICK→THIN, center moved 0.588
  Tile 908: THICK→THICK, center moved 0.309
  Tile 2352: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2412, 2413, 3334]
  Tile 2412: THICK→THICK, center moved 0.309
  Tile 2413: THIN→THICK, center moved 0.588
  Tile 3334: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1132, 2359, 2360]
  Tile 1132: THIN→THICK, center moved 0.309
  Tile 2359: THIN→THIN, center moved 0.809
  Tile 2360: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [910, 911, 4161]
  Tile 910: THICK→THICK, center moved 0.309
  Tile 911: THIN→THICK, center moved 0.588
  Tile 4161: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [833, 834, 4162]
  Tile 833: THIN→THICK, center moved 0.588
  Tile 834: THICK→THIN, center moved 0.588
  Tile 4162: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [910, 911, 4161]
  Tile 910: THICK→THICK, center moved 0.309
  Tile 911: THIN→THICK, center moved 0.588
  Tile 4161: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2357, 3332, 3333]
  Tile 2357: THIN→THIN, center moved 0.809
  Tile 3332: THIN→THICK, center moved 0.309
  Tile 3333: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2248, 2249, 4159]
  Tile 2248: THICK→THIN, center moved 0.309
  Tile 2249: THIN→THICK, center moved 0.309
  Tile 4159: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [985, 986, 2301]
  Tile 985: THICK→THIN, center moved 0.588
  Tile 986: THICK→THICK, center moved 0.309
  Tile 2301: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [758, 759, 4190]
  Tile 758: THIN→THICK, center moved 0.588
  Tile 759: THICK→THIN, center moved 0.588
  Tile 4190: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3564, 3565, 4165]
  Tile 3564: THICK→THIN, center moved 0.588
  Tile 3565: THIN→THICK, center moved 0.588
  Tile 4165: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [748, 749, 4138]
  Tile 748: THICK→THIN, center moved 0.588
  Tile 749: THIN→THICK, center moved 0.588
  Tile 4138: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2414, 2415, 3288]
  Tile 2414: THIN→THIN, center moved 0.809
  Tile 2415: THICK→THIN, center moved 0.309
  Tile 3288: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [975, 2463, 3428]
  Tile 975: THICK→THIN, center moved 0.588
  Tile 2463: THIN→THICK, center moved 0.588
  Tile 3428: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [909, 910, 2299]
  Tile 909: THIN→THICK, center moved 0.588
  Tile 910: THICK→THICK, center moved 0.309
  Tile 2299: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [824, 825, 2458]
  Tile 824: THICK→THICK, center moved 0.309
  Tile 825: THICK→THIN, center moved 0.588
  Tile 2458: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2294, 2295, 3469]
  Tile 2294: THIN→THICK, center moved 0.588
  Tile 2295: THICK→THICK, center moved 0.309
  Tile 3469: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2517, 2518, 3430]
  Tile 2517: THIN→THICK, center moved 0.309
  Tile 2518: THICK→THIN, center moved 0.309
  Tile 3430: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [913, 914, 2245]
  Tile 913: THICK→THIN, center moved 0.588
  Tile 914: THIN→THICK, center moved 0.588
  Tile 2245: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [682, 683, 2346]
  Tile 682: THICK→THIN, center moved 0.309
  Tile 683: THIN→THICK, center moved 0.309
  Tile 2346: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1061, 1063, 3284]
  Tile 1061: THIN→THICK, center moved 0.309
  Tile 1063: THIN→THIN, center moved 0.809
  Tile 3284: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [978, 979, 2409]
  Tile 978: THIN→THICK, center moved 0.309
  Tile 979: THIN→THIN, center moved 0.809
  Tile 2409: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2187, 2188, 4214]
  Tile 2187: THIN→THIN, center moved 0.809
  Tile 2188: THIN→THICK, center moved 0.309
  Tile 4214: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [830, 831, 3471]
  Tile 830: THIN→THICK, center moved 0.309
  Tile 831: THICK→THIN, center moved 0.309
  Tile 3471: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [691, 692, 2185]
  Tile 691: THIN→THICK, center moved 0.588
  Tile 692: THICK→THICK, center moved 0.309
  Tile 2185: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2357, 3332, 3333]
  Tile 2357: THIN→THIN, center moved 0.809
  Tile 3332: THIN→THICK, center moved 0.309
  Tile 3333: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THICK→THIN, center moved 0.309
  Tile 3376: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [747, 748, 2510]
  Tile 747: THICK→THIN, center moved 0.588
  Tile 748: THICK→THICK, center moved 0.309
  Tile 2510: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [838, 839, 2243]
  Tile 838: THIN→THIN, center moved 0.809
  Tile 839: THICK→THIN, center moved 0.309
  Tile 2243: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [819, 820, 2567]
  Tile 819: THICK→THIN, center moved 0.588
  Tile 820: THIN→THICK, center moved 0.588
  Tile 2567: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [684, 2293, 3516]
  Tile 684: THIN→THIN, center moved 0.809
  Tile 2293: THICK→THIN, center moved 0.309
  Tile 3516: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [613, 614, 2236]
  Tile 613: THIN→THICK, center moved 0.309
  Tile 614: THIN→THIN, center moved 0.809
  Tile 2236: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2304, 2305, 3285]
  Tile 2304: THIN→THICK, center moved 0.588
  Tile 2305: THICK→THIN, center moved 0.588
  Tile 3285: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [840, 841, 3374]
  Tile 840: THIN→THIN, center moved 0.809
  Tile 841: THICK→THIN, center moved 0.309
  Tile 3374: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1126, 1127, 3335]
  Tile 1126: THIN→THIN, center moved 0.809
  Tile 1127: THICK→THIN, center moved 0.309
  Tile 3335: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [979, 2410, 4107]
  Tile 979: THIN→THICK, center moved 0.588
  Tile 2410: THICK→THICK, center moved 0.309
  Tile 4107: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [826, 3520, 4136]
  Tile 826: THIN→THICK, center moved 0.309
  Tile 3520: THICK→THIN, center moved 0.309
  Tile 4136: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [1133, 2358, 3286]
  Tile 1133: THIN→THIN, center moved 0.809
  Tile 2358: THICK→THIN, center moved 0.309
  Tile 3286: THIN→THICK, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [2297, 2298, 3424]
  Tile 2297: THICK→THIN, center moved 0.588
  Tile 2298: THIN→THICK, center moved 0.588
  Tile 3424: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [901, 3473, 4108]
  Tile 901: THIN→THICK, center moved 0.309
  Tile 3473: THICK→THIN, center moved 0.309
  Tile 4108: THIN→THIN, center moved 0.809
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [755, 756, 3518]
  Tile 755: THIN→THICK, center moved 0.309
  Tile 756: THIN→THIN, center moved 0.809
  Tile 3518: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [691, 692, 2185]
  Tile 691: THIN→THICK, center moved 0.588
  Tile 692: THICK→THICK, center moved 0.309
  Tile 2185: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [2346, 2347, 3517]
  Tile 2346: THIN→THICK, center moved 0.588
  Tile 2347: THICK→THICK, center moved 0.309
  Tile 3517: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1060, 1061, 2304]
  Tile 1060: THICK→THIN, center moved 0.588
  Tile 1061: THIN→THICK, center moved 0.588
  Tile 2304: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [3329, 3330, 4160]
  Tile 3329: THICK→THIN, center moved 0.588
  Tile 3330: THICK→THICK, center moved 0.309
  Tile 4160: THIN→THICK, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [1062, 1063, 4131]
  Tile 1062: THICK→THICK, center moved 0.309
  Tile 1063: THIN→THICK, center moved 0.588
  Tile 4131: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: even)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [760, 2293, 4190]
  Tile 760: THICK→THICK, center moved 0.309
  Tile 2293: THIN→THICK, center moved 0.588
  Tile 4190: THICK→THIN, center moved 0.588
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [911, 912, 3376]
  Tile 911: THIN→THIN, center moved 0.809
  Tile 912: THIN→THICK, center moved 0.309
  Tile 3376: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: even)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427

🔄 Physical flip on [916, 917, 4186]
  Tile 916: THIN→THICK, center moved 0.588
  Tile 917: THICK→THIN, center moved 0.588
  Tile 4186: THICK→THICK, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.382 units
   Tile assignment distance: 1.485

🔄 Physical flip on [684, 2293, 3516]
  Tile 684: THIN→THICK, center moved 0.309
  Tile 2293: THIN→THIN, center moved 0.809
  Tile 3516: THICK→THIN, center moved 0.309
✅ Flip successful (old parity: odd)
   Interior moved: 0.618 units
   Tile assignment distance: 1.427
✅ MC sweep: 14/50 accepted (28.0%)
✅ Growth step 10: added 19 tiles
    New tiles: 19, Defects: 12
    Acceptance rate: 28.0%

✅ Experiment complete!
📊 Results saved to: data/growth_experiments/pores_0.0_20251214_193349.json

==================================================
📈 EXPERIMENT SUMMARY:
  Total steps: 10
  Final energy: 345.15
  Final defect density: 0.037
randa@Randa:quasi-phason$ python scripts/analyze_growth_results.py data/growth_experiments/baseline_*.json
python: can't open file '/mnt/c/Users/randa chames/Downloads/aberration-master/interns_&_project_&_conf/Prjct_Q-Crstl/quasi-phason/scripts/analyze_growth_results.py': [Errno 2] No such file or directory
randa@Randa:quasi-phason$