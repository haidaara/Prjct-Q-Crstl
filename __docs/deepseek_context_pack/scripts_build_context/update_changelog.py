#!/usr/bin/env python3
"""
scripts/build_context/update_changelog.py

Append a one-line changelog entry to 00_NAVIGATION.md.
Usage:
  python scripts/build_context/update_changelog.py "Fixed obstacle ID normalization"
"""

from datetime import datetime
from pathlib import Path
import sys

def main():
    msg = " ".join(sys.argv[1:]).strip()
    if not msg:
        raise SystemExit("Usage: update_changelog.py \"your message\"")

    repo = Path(__file__).resolve().parents[2]
    nav = repo / "00_NAVIGATION.md"
    text = nav.read_text(encoding="utf-8", errors="ignore").splitlines()

    stamp = datetime.now().strftime("%Y-%m-%d")
    entry = f"- ({stamp}) {msg}"

    # append at end
    text.append(entry)
    nav.write_text("\n".join(text) + "\n", encoding="utf-8")
    print(f"[ok] appended changelog entry to {nav}")

if __name__ == "__main__":
    main()
