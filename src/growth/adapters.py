"""Thin adapters for legacy engines used by growth SSOT.

This module contains only wrappers/helpers; it does not implement a growth loop.
"""

from __future__ import annotations

import inspect
from typing import Any, Dict, Iterable, List, Optional, Tuple


def resolve_neighbors_of(tiling_data: Dict[str, Any]):
    """Return neighbors_of(i)->list[int] using either per-tile 'neighbors' or 'adjacency_graph'.

    Legacy reality:
    - adjacency_graph keys may be strings.
    """

    tiles = tiling_data["tiles"]

    # Prefer per-tile neighbors only if EVERY tile has a neighbors list.
    # This prevents silent mixed-mode bugs (some tiles missing neighbors).
    if tiles and all(isinstance(t.get("neighbors"), list) for t in tiles):

        def neighbors_of(i: int) -> List[int]:
            return list(tiles[i].get("neighbors") or [])

        return neighbors_of


    g = tiling_data.get("adjacency_graph")
    if not isinstance(g, dict):
        raise ValueError("No adjacency source: missing tile.neighbors and tiling_data['adjacency_graph']")

    def neighbors_of(i: int) -> List[int]:
        return list(g.get(str(i), []) or [])

    return neighbors_of


# --------------------------------------------------------------------------------------
# Energy SSOT (L1/L2)
# --------------------------------------------------------------------------------------

def _get_tiling_from_ctx(ctx: Any) -> Dict[str, Any]:
    tiling = getattr(ctx, "tiling_data", None)
    if not isinstance(tiling, dict):
        raise ValueError("ctx.tiling_data must be set to the working-copy tiling dict")
    if not isinstance(tiling.get("tiles"), list):
        raise ValueError("ctx.tiling_data missing 'tiles' list")
    return tiling


def _get_energy_model(ctx: Any, energy_model: Optional[Any]) -> Any:
    if energy_model is not None:
        return energy_model
    em = getattr(ctx, "energy_model", None)
    if em is None:
        raise ValueError("energy_model not provided and ctx.energy_model is missing")
    return em


def _clear_energy_cache(energy_model: Any, *, tile_ids: Optional[List[int]] = None) -> None:
    """Clear caches. Prefer tile-local clear if supported; else global clear."""
    if not hasattr(energy_model, "clear_cache"):
        raise RuntimeError("Energy model does not support cache clearing (missing clear_cache).")

    clear_fn = getattr(energy_model, "clear_cache")
    try:
        sig = inspect.signature(clear_fn)
    except Exception:
        sig = None

    if sig is not None and "tile_ids" in sig.parameters:
        clear_fn(tile_ids=tile_ids)
    else:
        clear_fn()


def _locate_vacuum_flag(energy_model: Any) -> Tuple[Any, str]:
    """Return (container_obj, attr_name) for treat_ungrown_as_vacuum."""
    for container_name in ("params", "energy_params"):
        container = getattr(energy_model, container_name, None)
        if container is not None and hasattr(container, "treat_ungrown_as_vacuum"):
            return container, "treat_ungrown_as_vacuum"
    raise RuntimeError(
        "Vacuum-by-state flag not found. Expected energy_model.params.treat_ungrown_as_vacuum "
        "or energy_model.energy_params.treat_ungrown_as_vacuum"
    )


def energy_region_fresh(
    region_ids: Iterable[int],
    ctx: Any,
    *,
    energy_model: Optional[Any] = None,
    present_only: bool = True,
) -> float:
    """SSOT L1: fresh total energy over a region.

    region_ids must be indices in the working-copy tiling (id == index).
    If present_only=True, only tiles with removed==False and growth_status in {'seed','grown'} contribute.
    """

    tiling_data = _get_tiling_from_ctx(ctx)
    em = _get_energy_model(ctx, energy_model)

    if not hasattr(em, "compute_local_energy"):
        raise RuntimeError("Energy model missing compute_local_energy(tile_id, tiling_data)")

    region_list = [int(i) for i in region_ids]
    _clear_energy_cache(em, tile_ids=region_list)

    tiles = tiling_data["tiles"]
    total = 0.0

    for tid in region_list:
        t = tiles[tid]

        if present_only:
            if t.get("removed", False):
                continue
            if t.get("growth_status") not in ("seed", "grown"):
                continue

        total += float(em.compute_local_energy(int(tid), tiling_data))

    return float(total)


def deltaE_local_for_attachment(
    tile_id: int,
    region_ids: Iterable[int],
    ctx: Any,
    mu_attach: float,
    *,
    energy_model: Optional[Any] = None,
    present_only: bool = True,
) -> Tuple[float, float]:
    """SSOT L2: ΔE_local and ΔE_eff for attaching a candidate tile.

    Operates on working-copy tiling where tile_id == index.
    Returns (deltaE_local, deltaE_eff=deltaE_local - mu_attach).
    """

    tiling_data = _get_tiling_from_ctx(ctx)
    em = _get_energy_model(ctx, energy_model)

    tile_id = int(tile_id)
    region_list = [int(i) for i in region_ids]
    if tile_id < 0 or tile_id >= len(tiling_data["tiles"]):
        raise ValueError(f"tile_id out of range: {tile_id}")

    if tile_id not in region_list:
        region_list = [tile_id] + region_list

    flag_obj, flag_name = _locate_vacuum_flag(em)
    flag_orig = bool(getattr(flag_obj, flag_name))

    tiles = tiling_data["tiles"]
    cand = tiles[tile_id]

    cand_growth_orig = cand.get("growth_status")
    cand_removed_orig = bool(cand.get("removed", False))
    if cand_removed_orig:
        raise ValueError("Candidate tile is removed=True; attachment energy is undefined")

    try:
        setattr(flag_obj, flag_name, True)

        cand["growth_status"] = "ungrown"
        cand["removed"] = False
        E_before = energy_region_fresh(region_list, ctx, energy_model=em, present_only=present_only)

        cand["growth_status"] = "grown"
        E_after = energy_region_fresh(region_list, ctx, energy_model=em, present_only=present_only)

    finally:
        cand["growth_status"] = cand_growth_orig
        cand["removed"] = cand_removed_orig
        setattr(flag_obj, flag_name, flag_orig)

        try:
            _clear_energy_cache(em, tile_ids=region_list)
        except Exception:
            pass

    deltaE_local = float(E_after - E_before)
    deltaE_eff = float(deltaE_local - float(mu_attach))
    return deltaE_local, deltaE_eff

# --------------------------------------------------------------------------------------
# MC region adapter + leak tripwire (SSOT/Contract: C3, C3a; SSOT M, M2)
# --------------------------------------------------------------------------------------

_INTRINSIC_C3A_FIELDS = (
    "removed",
    "immobile",
    "growth_status",
    "birth_cycle",
    "birth_mode",
    "birth_family",
    "type",
)


def _snapshot_intrinsic_fields(tiling_data: Dict[str, Any], tile_ids: List[int]) -> Dict[int, Tuple[Any, ...]]:
    """Return per-tile tuples of intrinsic fields for C3a tripwire."""
    tiles = tiling_data["tiles"]
    out: Dict[int, Tuple[Any, ...]] = {}
    for tid in tile_ids:
        t = tiles[tid]
        out[tid] = tuple(t.get(k) for k in _INTRINSIC_C3A_FIELDS)
    return out


def _diff_intrinsic(before: Dict[int, Tuple[Any, ...]], after: Dict[int, Tuple[Any, ...]]) -> List[int]:
    changed: List[int] = []
    for tid, b in before.items():
        if after.get(tid) != b:
            changed.append(tid)
    return changed


def _run_sweep_with_temperature(mc_engine: Any, tiling_data: Dict[str, Any], *, steps: int, temperature: float) -> Any:
    """Run mc_engine.run_sweep with best-effort temperature injection."""
    if not hasattr(mc_engine, "run_sweep"):
        raise RuntimeError("MC engine missing run_sweep(...)")

    run_sweep = getattr(mc_engine, "run_sweep")

    # Decide whether run_sweep accepts 'temperature'. If not, set mc_engine.temperature.
    accepts_temperature = False
    try:
        sig = inspect.signature(run_sweep)
        if "temperature" in sig.parameters:
            accepts_temperature = True
        else:
            # If **kwargs exists, we can pass temperature safely.
            for p in sig.parameters.values():
                if p.kind == inspect.Parameter.VAR_KEYWORD:
                    accepts_temperature = True
                    break
    except Exception:
        # If we can't inspect, attempt passing temperature and fall back.
        accepts_temperature = True

    old_temp = getattr(mc_engine, "temperature", None)
    can_set_temp = hasattr(mc_engine, "temperature")

    if accepts_temperature:
        try:
            return run_sweep(tiling_data, steps=steps, temperature=temperature)
        except TypeError:
            # Some implementations don't accept temperature; fall back to attribute injection.
            pass

    # Attribute injection path
    if can_set_temp:
        mc_engine.temperature = temperature

    try:
        try:
            return run_sweep(tiling_data, steps=steps)
        except TypeError:
            # Positional fallback
            return run_sweep(tiling_data, steps)
    finally:
        if can_set_temp and old_temp is not None:
            mc_engine.temperature = old_temp


def mc_run_region(
    active_ids: List[int],
    steps: int,
    temperature: float,
    ctx: Any,
    mc_engine: Any,
    *,
    strict: bool | str = False,   # False | True | "sample"
    sample_size: int = 200,
) -> Dict[str, Any]:
    """SSOT M/M2: run MC restricted to active_ids via flippable masking + C3a tripwire.

    Assumptions:
      - Working copy where tile_id == index (probe reality).
      - Legacy engines may rebuild adjacency globally (derived fields) -> explicitly ignored by tripwire.

    Returns normalized stats:
      {
        "proposed": int,
        "accepted": int,
        "rejected": int,
        "acceptance_rate": float | None,
        "warnings": List[str],
      }
    """
    warnings: List[str] = []
    tiling_data = _get_tiling_from_ctx(ctx)

    # Early exits
    if not active_ids:
        warnings.append("empty_active_ids")
        return {"proposed": 0, "accepted": 0, "rejected": 0, "acceptance_rate": None, "warnings": warnings}
    if steps <= 0:
        warnings.append("nonpositive_steps")
        return {"proposed": 0, "accepted": 0, "rejected": 0, "acceptance_rate": None, "warnings": warnings}

    tiles = tiling_data["tiles"]
    n_tiles = len(tiles)

    active_set = {int(x) for x in active_ids if 0 <= int(x) < n_tiles}
    if not active_set:
        warnings.append("active_ids_out_of_range")
        return {"proposed": 0, "accepted": 0, "rejected": 0, "acceptance_rate": None, "warnings": warnings}

    outside_ids = [i for i in range(n_tiles) if i not in active_set]

    # Tripwire selection (C3a)
    check_ids: List[int] = []
    do_tripwire = strict is True or strict == "sample"
    if do_tripwire and outside_ids:
        if strict == "sample":
            rng = getattr(ctx, "rng", None)
            k = min(int(sample_size), len(outside_ids))
            try:
                check_ids = list(rng.sample(outside_ids, k)) if rng is not None else outside_ids[:k]
            except Exception:
                check_ids = outside_ids[:k]
        else:
            check_ids = outside_ids

    before_tripwire: Dict[int, Tuple[Any, ...]] = {}
    if check_ids:
        before_tripwire = _snapshot_intrinsic_fields(tiling_data, check_ids)

    # Snapshot original flippable states (including "missing key" case)
    _MISSING = object()
    flippable_orig: List[Any] = []
    for t in tiles:
        flippable_orig.append(t["flippable"] if "flippable" in t else _MISSING)

    # Snapshot MC flip_stats (if available) for delta accounting
    before_fs: Dict[str, int] = {}
    try:
        metrics = getattr(mc_engine, "metrics", None)
        if isinstance(metrics, dict):
            fs = metrics.get("flip_stats")
            if isinstance(fs, dict):
                before_fs = {k: int(fs.get(k, 0)) for k in ("proposed", "accepted", "rejected")}
    except Exception:
        before_fs = {}

    stats = None
    try:
        # Apply mask: flippable True inside region, False outside
        for i in range(n_tiles):
            tiles[i]["flippable"] = (i in active_set)

        # Run sweep
        stats = _run_sweep_with_temperature(mc_engine, tiling_data, steps=int(steps), temperature=float(temperature))

    finally:
        # Restore flippable exactly
        for i, orig in enumerate(flippable_orig):
            if orig is _MISSING:
                if "flippable" in tiles[i]:
                    del tiles[i]["flippable"]
            else:
                tiles[i]["flippable"] = orig

    # Tripwire after
    if check_ids:
        after_tripwire = _snapshot_intrinsic_fields(tiling_data, check_ids)
        changed = _diff_intrinsic(before_tripwire, after_tripwire)
        if changed:
            warnings.append("Mutations detected outside active_ids (intrinsic fields)")
            warnings.append(f"c3a_changed_sample={changed[:10]}")

    # Normalize stats (prefer flip_stats deltas; fall back to stats dict; else warn)
    proposed = accepted = rejected = 0

    after_fs: Dict[str, int] = {}
    try:
        metrics = getattr(mc_engine, "metrics", None)
        if isinstance(metrics, dict):
            fs = metrics.get("flip_stats")
            if isinstance(fs, dict):
                after_fs = {k: int(fs.get(k, 0)) for k in ("proposed", "accepted", "rejected")}
    except Exception:
        after_fs = {}

    if before_fs and after_fs:
        proposed = max(0, after_fs.get("proposed", 0) - before_fs.get("proposed", 0))
        accepted = max(0, after_fs.get("accepted", 0) - before_fs.get("accepted", 0))
        rejected = max(0, after_fs.get("rejected", 0) - before_fs.get("rejected", 0))
        # Normalize: some legacy engines do not track rejected correctly.
        rejected = max(int(rejected), max(0, int(proposed) - int(accepted)))

    elif isinstance(stats, dict):
        accepted = int(stats.get("accepted", 0))
        proposed = int(stats.get("proposed", stats.get("steps", 0)))
        rejected = int(stats.get("rejected", max(0, proposed - accepted)))
        if proposed == 0 and accepted == 0:
            warnings.append("stats_unavailable")
    else:
        warnings.append("stats_unavailable")

    acceptance_rate = (accepted / proposed) if proposed > 0 else None

    return {
        "proposed": int(proposed),
        "accepted": int(accepted),
        "rejected": int(rejected),
        "acceptance_rate": float(acceptance_rate) if acceptance_rate is not None else None,
        "warnings": warnings,
    }
