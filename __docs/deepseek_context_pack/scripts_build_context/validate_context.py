#!/usr/bin/env python3
"""
scripts/build_context/validate_context.py

Quick sanity checks for the context pack:
- every python file is represented in 02_CODE_INDEX.md
- required pack files exist
"""

from pathlib import Path

REQUIRED = ["00_NAVIGATION.md", "01_ARCHITECTURE.yaml", "02_CODE_INDEX.md"]

def main():
    repo = Path(__file__).resolve().parents[2]
    missing = [p for p in REQUIRED if not (repo / p).exists()]
    if missing:
        raise SystemExit(f"[fail] missing required files: {missing}")

    code_index = (repo / "02_CODE_INDEX.md").read_text(encoding="utf-8", errors="ignore")
    py_files = []
    for sub in ["src", "experiments", "analysis", "validation", "dev_tools"]:
        d = repo / sub
        if d.exists():
            py_files += [str(p.relative_to(repo)) for p in d.rglob("*.py") if "__pycache__" not in str(p)]

    not_listed = [p for p in sorted(py_files) if f"`{p}`" not in code_index]
    if not_listed:
        raise SystemExit("[fail] these python files are not listed in 02_CODE_INDEX.md:\n- " + "\n- ".join(not_listed))

    print("[ok] context pack seems consistent")

if __name__ == "__main__":
    main()
