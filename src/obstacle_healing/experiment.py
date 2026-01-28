# src/obstacle_healing/experiment.py
from __future__ import annotations

import json
import random
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

from src.energy.combinatorial_classifier import CombinatorialVertexClassifier
from src.energy.widom_inspired_energy import WidomInspiredEnergy, EnergyParameters
from src.simulation.flip_engine import FlipEngine
from src.simulation.mc_engine import MonteCarloEngine

from src.obstacle_healing.metrics import RunMetrics
from src.obstacle_healing.snapshotter import Snapshotter
from src.obstacle_healing.regions import select_measurement_tiles, select_active_tiles
from src.obstacle_healing.damage import count_defects_fast, damage_by_heating


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def parse_anneal_schedule(ann_cfg: Dict[str, Any]) -> List[Tuple[float, int, str]]:
    """Parse [anneal].schedule = [{T=..., steps=..., name="..."}, ...]."""
    schedule = ann_cfg.get("schedule")
    if not isinstance(schedule, list) or not schedule:
        raise ValueError("[anneal].schedule must be a non-empty list")

    out: List[Tuple[float, int, str]] = []
    for i, st in enumerate(schedule):
        if not isinstance(st, dict):
            raise TypeError(f"[anneal].schedule[{i}] must be a dict, got {type(st)}")
        if "T" not in st or "steps" not in st:
            raise ValueError(f"[anneal].schedule[{i}] must contain keys T and steps")
        T = float(st["T"])
        steps = int(st["steps"])
        if steps <= 0:
            raise ValueError(f"[anneal].schedule[{i}] steps must be > 0 (got {steps})")
        name = str(st.get("name", f"T{T:g}"))
        out.append((T, steps, name))
    return out


def _apply_flippable_mask(tiling: Dict, active_ids: List[int]) -> None:
    active = set(active_ids)
    for i, t in enumerate(tiling["tiles"]):
        if t.get("removed", False) or t.get("immobile", False):
            t["flippable"] = False
        else:
            t["flippable"] = (i in active)


@dataclass
class ObstacleHealingExperiment:
    input_path: str
    output_dir: str
    run_name: str = "obstacle_healing_run"

    cfg: Dict[str, Any] = None

    # optional injection
    energy_model: Any = None
    flip_engine: Any = None
    mc_engine: Any = None

    def run(self) -> Dict[str, Any]:
        assert self.cfg is not None, "cfg must be provided"

        run_cfg = self.cfg.get("run", {}) or {}
        log_cfg = self.cfg.get("logging", {}) or {}
        obs_cfg = self.cfg.get("obstacles", {}) or {}
        reg_cfg = self.cfg.get("regions", {}) or {}
        dmg_cfg = self.cfg.get("damage", {}) or {}
        def_cfg = self.cfg.get("defects", {}) or {}
        ann_cfg = self.cfg.get("anneal", {}) or {}

        mode = str(log_cfg.get("mode", "normal")).lower()
        debug = (mode == "debug")

        seed = run_cfg.get("seed", None)
        if seed is not None:
            seed_i = int(seed)
            random.seed(seed_i)
            np.random.seed(seed_i)

        t0 = time.time()

        # ---- load tiling
        with open(self.input_path, "r", encoding="utf-8") as f:
            tiling = json.load(f)

        total_tiles = len(tiling.get("tiles", []))
        obstacle_meta = tiling.get("obstacle_metadata") or {}
        obstacle_mode = str(obs_cfg.get("mode", obstacle_meta.get("type", "pores"))).lower()
        if obstacle_mode == "pores":
            obstacle_mode = "pores"
        if obstacle_mode == "fixed_defects":
            obstacle_mode = "fixed_defects"

        # ---- engines (same physics as your original healing: Widom energy + MC phason flips)
        if self.energy_model is None:
            params = EnergyParameters()
            self.energy_model = WidomInspiredEnergy(params)

        if self.flip_engine is None:
            classifier = CombinatorialVertexClassifier()
            self.flip_engine = FlipEngine(classifier, self.energy_model, verbose=debug)

        if self.mc_engine is None:
            mc_conf = {
                "verbosity": 2 if debug else 1,
                "trace_every": int(log_cfg.get("trace_every", 50)),
                "neighborhood_radius": int(ann_cfg.get("neighborhood_radius", 3)),
            }
            self.mc_engine = MonteCarloEngine(
                temperature=float(ann_cfg.get("initial_T", 0.3)),
                energy_model=self.energy_model,
                flip_engine=self.flip_engine,
                config=mc_conf,
            )

        # ---- regions
        inner = float(reg_cfg.get("annulus_inner", 2.0))
        outer = float(reg_cfg.get("annulus_outer", 16.0))
        relative = bool(reg_cfg.get("relative_to_obstacle_radius", True))
        fixed_k = int(reg_cfg.get("fixed_k", 2))

        measurement_ids = select_measurement_tiles(
            tiling, mode=obstacle_mode, inner=inner, outer=outer,
            relative_to_radius=relative, fixed_k=fixed_k
        )

        active_buffer = float(reg_cfg.get("active_buffer", 6.0))
        fixed_active_k = int(reg_cfg.get("fixed_active_k", 3))
        active_ids = select_active_tiles(
            tiling, mode=obstacle_mode, measurement_ids=measurement_ids,
            active_buffer=active_buffer, fixed_active_k=fixed_active_k
        )
        _apply_flippable_mask(tiling, active_ids)

        # ---- output
        run_dir = Path(self.output_dir) / self.run_name
        _ensure_dir(run_dir)
        snapshotter = Snapshotter(run_dir)
        metrics = RunMetrics()

        defect_threshold = float(def_cfg.get("threshold", 1.5))

        # baseline init (fills local_energy)
        self.energy_model.update_tiling_energy(tiling)
        self.mc_engine.initialize_energy(tiling)

        baseline_energy = float(self.mc_engine.current_energy)
        baseline_defects = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)

        def _p(msg: str) -> None:
            print(msg, flush=True)

        _p("=" * 79)
        _p("OBSTACLE HEALING EXPERIMENT - START")
        _p("=" * 79)
        _p(f"Input: {self.input_path}")
        _p(f"Run dir: {run_dir}")
        _p(f"Tiles: total={total_tiles} measurement={len(measurement_ids)} active={len(active_ids)}")
        _p(f"Obstacle mode: {obstacle_mode}  meta_type={obstacle_meta.get('type','')} density={obstacle_meta.get('density','')}")
        _p(f"Defect threshold: local_energy > {defect_threshold}")
        _p("-" * 79)

        snapshotter.save_snapshot(
            tiling=tiling, step=0, label="baseline",
            temperature=float(ann_cfg.get("initial_T", 0.0)),
            metrics={"energy": baseline_energy, "defects": baseline_defects},
        )
        _p(f"BASELINE: E={baseline_energy:.6f} defects={baseline_defects}/{len(measurement_ids)}")

        # ---- damage (publication-meaningful: still MC dynamics, just at high T)
        damage_enabled = bool(dmg_cfg.get("enabled", True))
        target_additional = int(dmg_cfg.get("target_defects", 15))  # additional defects above baseline
        damage_T = float(dmg_cfg.get("temperature", 5.0))
        damage_max_steps = int(dmg_cfg.get("max_steps", 5000))
        damage_check_every = int(dmg_cfg.get("check_every", 200))
        damage_print_every = int(dmg_cfg.get("print_every", 200))

        damaged_energy = baseline_energy
        damaged_defects = baseline_defects
        damage_steps = 0

        if damage_enabled and target_additional > 0:
            _p("-" * 79)
            _p("DAMAGE PHASE")
            _p("-" * 79)
            _p(f"Target additional defects: +{target_additional} (above baseline {baseline_defects})")
            _p(f"Heating at T={damage_T} (max_steps={damage_max_steps}, check_every={damage_check_every})")

            last_print = 0

            def log_cb(**kw):
                nonlocal last_print
                steps = kw.get("steps", 0)
                defects_now = kw.get("defects", 0)
                target_total = kw.get("target", 0)
                if steps - last_print >= damage_print_every or defects_now >= target_total or steps == damage_max_steps:
                    _p(f"  damage step {steps:5d}: defects={defects_now}/{len(measurement_ids)} target={target_total}")
                    last_print = steps

            _target_total, damaged_defects, damage_steps = damage_by_heating(
                tiling,
                mc_engine=self.mc_engine,
                measurement_ids=measurement_ids,
                defect_threshold=defect_threshold,
                baseline_defects=baseline_defects,
                target_additional_defects=target_additional,
                max_steps=damage_max_steps,
                temperature=damage_T,
                check_every=damage_check_every,
                log_cb=log_cb,
            )

            # refresh local_energy for snapshot correctness
            self.energy_model.update_tiling_energy(tiling)
            damaged_energy = float(self.mc_engine.current_energy)
            
            # Recompute defects AFTER the refresh so the scalar matches the saved tile energies
            damaged_defects = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)
            
            snapshotter.save_snapshot(
                tiling=tiling, step=1, label="damaged", temperature=damage_T,
                metrics={"energy": damaged_energy, "defects": damaged_defects, "damage_steps": damage_steps},
            )

            _p(f"DAMAGE DONE: defects={damaged_defects}/{len(measurement_ids)} steps={damage_steps}")

        # ---- annealing / healing
        _p("-" * 79)
        _p("HEALING PHASE")
        _p("-" * 79)

        stages = parse_anneal_schedule(ann_cfg)
        metrics_every = int(ann_cfg.get("metrics_every", 10))
        snapshot_every = int(ann_cfg.get("snapshot_every", 50))
        verify_every = int(ann_cfg.get("verify_every", 50))
        print_every = int(log_cfg.get("print_every", 50))

        global_step = 0
        drift_max = 0.0

        for si, (T, steps_in_stage, name) in enumerate(stages, start=1):
            metrics.add_stage_transition(step=global_step, T=T, name=name, steps_in_stage=steps_in_stage)
            self.mc_engine.temperature = float(T)

            stage_start_defects = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)
            stage_start_energy = float(self.mc_engine.current_energy)

            acc_accepted = 0
            acc_proposed = 0

            _p(f"Stage {si}/{len(stages)}: {name}  T={T}  steps={steps_in_stage}")

            for k in range(1, steps_in_stage + 1):
                accepted, _dE = self.mc_engine.run_step(tiling, debug_mode=False)
                acc_proposed += 1
                if accepted:
                    acc_accepted += 1
                global_step += 1

                drift = 0.0
                if global_step % max(1, verify_every) == 0:
                    drift = float(self.mc_engine._verify_energy_consistency(tiling, message=f"step {global_step}"))
                    drift_max = max(drift_max, abs(drift))

                if global_step % metrics_every == 0 or (k == steps_in_stage):
                    E = float(self.mc_engine.current_energy)
                    dcount = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)
                    density = dcount / max(1, len(measurement_ids))
                    acc_rate = (acc_accepted / max(1, acc_proposed))
                    metrics.record(
                        step=global_step, T=T, energy=E,
                        defects=dcount, defect_density=density,
                        acceptance_rate=acc_rate, energy_drift=drift
                    )

                if global_step % snapshot_every == 0:
                    snapshotter.save_snapshot(
                        tiling=tiling, step=global_step, label="healing", temperature=T,
                        metrics={"energy": float(self.mc_engine.current_energy),
                                 "defects": count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)}
                    )

                if (global_step % print_every == 0) and (not debug) and metrics.steps:
                    i = len(metrics.steps) - 1
                    _p(
                        f"  step {global_step:5d}: "
                        f"E={metrics.energies[i]:.3f} defects={metrics.defects[i]} "
                        f"acc={metrics.acceptance_rates[i]*100:.1f}% drift={metrics.energy_drifts[i]:.2e}"
                    )

            stage_end_defects = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)
            stage_end_energy = float(self.mc_engine.current_energy)
            _p(
                f"  stage summary: defects {stage_start_defects}→{stage_end_defects} "
                f"(Δ={stage_end_defects - stage_start_defects:+d})  "
                f"E {stage_start_energy:.3f}→{stage_end_energy:.3f}  drift_max={drift_max:.2e}"
            )

        final_defects = count_defects_fast(tiling, measurement_ids, defect_threshold=defect_threshold)
        final_energy = float(self.mc_engine.current_energy)

        snapshotter.save_snapshot(
            tiling=tiling, step=global_step, label="final", temperature=float(stages[-1][0]),
            metrics={"energy": final_energy, "defects": final_defects}
        )

        metrics.finalize_summary(
            baseline_defects=baseline_defects,
            damaged_defects=damaged_defects,
            final_defects=final_defects,
            baseline_energy=baseline_energy,
            damaged_energy=damaged_energy,
            final_energy=final_energy,
            drift_max=drift_max,
            measurement_tiles=len(measurement_ids),
            total_mc_steps=global_step,
            damage_steps=damage_steps,
        )

        with open(run_dir / "run_metrics.json", "w", encoding="utf-8") as f:
            json.dump(metrics.to_dict(), f, ensure_ascii=False, indent=2)
        snapshotter.write_index()

        dt = time.time() - t0
        _p("-" * 79)
        _p("EXPERIMENT COMPLETE")
        _p(f"Elapsed: {dt:.2f} s   MC steps: {global_step}")
        _p(f"Defects: {damaged_defects} → {final_defects}  efficiency={metrics.summary.get('healing_efficiency',0.0):.3f}")
        _p(f"Energy:  {damaged_energy:.3f} → {final_energy:.3f}  ΔE={damaged_energy - final_energy:.3f}")
        _p(f"Energy drift max: {drift_max:.2e}")
        _p("=" * 79)

        return {
            "run_dir": str(run_dir),
            "metrics_file": str(run_dir / "run_metrics.json"),
            "snapshot_index": str(run_dir / "snapshot_index.json"),
            "summary": metrics.summary,
        }
