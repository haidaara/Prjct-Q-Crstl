from __future__ import annotations

from pathlib import Path
import sys

# Ensure project root is on PYTHONPATH so `import src...` works
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


import sys

# Ensure project root is on PYTHONPATH so `import src...` works
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

#!/usr/bin/env python3
"""Create a movie from a snapshot directory.

Example:
  python scripts/viz/05_viz_movie.py \
    --snapshot_dir data/experiments/healing/run_021/snapshots \
    --view strain --fps 12 --outdir data/viz/run_021

Requires imageio.
"""

import argparse
import sys

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from src.viz.config import load_publication_config, get_viz_jobs
from src.viz.io import short_path
from src.viz.style import default_output_dir
from src.viz.movie import make_movie


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot_dir", default=None)
    ap.add_argument("--view", default=None)
    ap.add_argument("--fps", default=None, type=int)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--config", default=None)
    args = ap.parse_args()

    cfg = load_publication_config(args.config)
    viz = cfg.get("viz_jobs", {})

    # TOML mode
    if not args.snapshot_dir:
        if not viz.get("enabled", False):
            print("viz_jobs.enabled is false -> nothing to run")
            return 0

        jobs = [j for j in get_viz_jobs(cfg) if str(j.get("kind", "")).strip().lower() == "movie"]
        if not jobs:
            print("No movie jobs found under [viz_jobs.jobs] (kind='movie')")
            return 0

        print("\n============================================================")
        print("VIZ MOVIE: running jobs from TOML")
        print(f"Config : {short_path(Path(args.config) if args.config else (Path('configs')/'publication_plots.toml'))}")
        print("============================================================")

        for idx, j in enumerate(jobs, 1):
            snapdir = j.get("snapshot_dir")
            if not snapdir:
                print(f"  ⚠️  Job {idx}/{len(jobs)} missing snapshot_dir -> skipped")
                continue

            outdir = args.outdir or j.get("outdir")
            out_show = short_path(Path(outdir)) if outdir else short_path(default_output_dir(cfg))
            view = args.view if args.view is not None else j.get("view", "strain")
            fps = int(args.fps) if args.fps is not None else int(j.get("fps", 12))

            print(f"\n--- Job {idx}/{len(jobs)} ---")
            print(f"Snapshots: {short_path(Path(snapdir))}")
            print(f"Output   : {out_show}")
            print(f"View     : {view}")
            print(f"FPS      : {fps}")

            make_movie(snapdir, view=view, fps=fps, outdir=outdir, cfg=cfg)

        print("\n✅ Movie viz complete")
        return 0

    # Single-run mode
    view = args.view or "strain"
    fps = int(args.fps) if args.fps is not None else 12
    make_movie(args.snapshot_dir, view=view, fps=fps, outdir=args.outdir, cfg=cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
