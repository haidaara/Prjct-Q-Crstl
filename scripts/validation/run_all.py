#!/usr/bin/env python3
"""MASTER VALIDATION RUNNER (GO/NO-GO).

Runs:
- validate_tiling.py
- validate_obstacles.py
- validate_energy.py
"""
import subprocess
import sys
from pathlib import Path


def run_script(script_name: str) -> bool:
    script_path = Path(__file__).resolve().parent / script_name
    print(f"\n🏃 RUNNING: {script_name}")
    r = subprocess.run([sys.executable, str(script_path)])
    return r.returncode == 0


def main() -> None:
    scripts = ["validate_tiling.py", "validate_obstacles.py", "validate_energy.py"]
    for s in scripts:
        if not run_script(s):
            print(f"\n❌ HALT: {s} failed.")
            sys.exit(1)
    print("\n✅✅✅ ALL VALIDATION SUITES PASSED ✅✅✅")


if __name__ == "__main__":
    main()
