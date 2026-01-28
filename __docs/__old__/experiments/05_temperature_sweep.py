#!/usr/bin/env python3
import sys
import json
import toml
import copy
import re
import shutil
import importlib.util
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def short_path(p) -> str:
    p = Path(p)
    try:
        return str(p.resolve().relative_to(PROJECT_ROOT.resolve()))
    except Exception:
        parts = p.parts
        return str(Path(*parts[-4:])) if len(parts) > 4 else str(p)


def temp_token(T: float) -> str:
    return "T" + f"{T:.3f}".replace(".", "p")


def next_run_id(folder: Path) -> int:
    nums = []
    for p in folder.glob("tempsweep_*_run_*.json"):
        m = re.search(r"_run_(\d+)$", p.stem)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def overwrite_latest(run_file: Path, latest_path: Path) -> None:
    shutil.copyfile(run_file, latest_path)


def load_config(config_path: str) -> dict:
    cp = Path(config_path)
    if not cp.is_absolute():
        cp = PROJECT_ROOT / cp
    if not cp.exists():
        raise FileNotFoundError(f"Config file not found: {cp}")

    with open(cp, "r", encoding="utf-8") as f:
        config = toml.load(f)

    config["_meta_config_path"] = str(config_path)
    return config


def load_growth_runner():
    growth_path = PROJECT_ROOT / "scripts" / "experiments" / "04_run_growth.py"
    if not growth_path.exists():
        raise FileNotFoundError(f"04_run_growth.py not found at: {growth_path}")

    spec = importlib.util.spec_from_file_location("growth04", str(growth_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run_growth_experiment


def run_temperature_sweep(config: dict, cli_verbosity=None) -> dict:
    debug = config.get("debug", {})
    verbosity = int(cli_verbosity if cli_verbosity is not None else (debug.get("verbosity", 1) or 1))
    verbosity = 2 if verbosity >= 2 else 1

    progress_every = int(debug.get("progress_every", 1) or 1)
    progress_every = max(1, progress_every)

    trace_every = int(debug.get("trace_every", 50) or 50)
    trace_every = max(1, trace_every)

    sweep_cfg = config.get("temp_sweep", {})
    scenario = str(sweep_cfg.get("scenario", "base"))
    temps = list(sweep_cfg.get("temperatures", [0.8, 1.0, 1.2, 1.5]))

    out_dir = Path(sweep_cfg.get("output_dir", "data/experiments/temp_sweep"))
    if not out_dir.is_absolute():
        out_dir = PROJECT_ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    sweep_run_id = next_run_id(out_dir)
    sweep_name = f"tempsweep_{scenario}_run_{sweep_run_id:03d}"
    sweep_file = out_dir / f"{sweep_name}.json"
    latest_file = out_dir / "latest.json"

    if verbosity >= 1:
        print("🌡️ TEMPERATURE SWEEP")
        print("=" * 60)
        print(f"📥 Base config: {short_path(config.get('_meta_config_path', ''))}")
        print(f"📤 Output dir : {short_path(out_dir)}")
        print(f"⚙️  scenario={scenario} temps={temps}")
        print(f"🔧 debug: verbosity={verbosity}, progress_every={progress_every}, trace_every={trace_every}")

    growth_run = load_growth_runner()

    per_T = []
    for i, T in enumerate(temps, start=1):
        T = float(T)
        t_tok = temp_token(T)

        if verbosity >= 1:
            print(f"\n🌡️  [{i}/{len(temps)}] Running T={T}")

        cfg = copy.deepcopy(config)
        cfg.setdefault("monte_carlo", {})
        cfg["monte_carlo"]["temperature"] = T

        cfg.setdefault("debug", {})
        cfg["debug"]["verbosity"] = verbosity
        cfg["debug"]["progress_every"] = progress_every
        cfg["debug"]["trace_every"] = trace_every

        cfg.setdefault("project", {})
        cfg["project"]["output_dir"] = str(out_dir)

        t_run_id = next_run_id(out_dir)
        exp_name = f"tempsweep_{scenario}_{t_tok}_run_{t_run_id:03d}"

        result = growth_run(cfg, exp_name)

        series = result.get("series", {}).get("growth_steps", [])
        first = series[0] if series else {}
        last = series[-1] if series else {}

        row = {
            "temperature": T,
            "file": f"{exp_name}.json",
            "mean_acceptance_rate": result.get("metrics", {}).get("mean_acceptance_rate"),
            "defects_start": first.get("defect_count"),
            "defects_end": last.get("defect_count"),
            "final_energy": result.get("metrics", {}).get("final_energy"),
            "total_new_tiles": result.get("metrics", {}).get("total_new_tiles"),
        }

        if row["defects_start"] is not None and row["defects_end"] is not None:
            healed = row["defects_start"] - row["defects_end"]
            row["healed"] = healed
            row["healing_efficiency"] = healed / max(1, row["defects_start"])
        else:
            row["healed"] = None
            row["healing_efficiency"] = None

        per_T.append(row)

        if verbosity >= 1:
            print(
                f"   ↳ file={row['file']}  acc_mean={row['mean_acceptance_rate']}  "
                f"defects={row['defects_start']}→{row['defects_end']}  "
                f"E_final={row['final_energy']}"
            )

    sweep_out = {
        "meta": {
            "experiment": "temp_sweep",
            "scenario": scenario,
            "run_id": sweep_run_id,
            "config": short_path(config.get("_meta_config_path", "")),
            "output_dir": short_path(out_dir),
        },
        "params": {
            "temperatures": temps,
            "progress_every": progress_every,
            "trace_every": trace_every,
        },
        "series": {
            "by_temperature": per_T
        }
    }

    with open(sweep_file, "w", encoding="utf-8") as f:
        json.dump(sweep_out, f, indent=2)

    overwrite_latest(sweep_file, latest_file)

    if verbosity >= 1:
        print("\n✅ Temperature sweep complete!")
        print(f"📊 Summary saved to: {short_path(sweep_file)}")

    return sweep_out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Run temperature sweep (calls 04 per temperature)")
    ap.add_argument("--config", "-c", default="configs/phase2_experiments.toml")
    ap.add_argument("--verbosity", type=int, choices=[1, 2], help="Override debug verbosity (1 or 2)")
    args = ap.parse_args()

    config = load_config(args.config)
    run_temperature_sweep(config, args.verbosity)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
