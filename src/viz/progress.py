from __future__ import annotations

from typing import Iterable, Iterator, Optional, TypeVar
import time
import sys
import os

T = TypeVar("T")


def progress(items: Iterable[T], *, desc: str = "", total: Optional[int] = None) -> Iterator[T]:
    """Lightweight progress helper with timing.

    - Uses tqdm if available with academic formatting.
    - Otherwise prints occasional progress messages with timing (no overhead).

    This is intentionally tiny and dependency-light.
    """
    # NOTE: avoid `yield` in this outer function.
    try:
        from tqdm import tqdm  # type: ignore

        seq = list(items) if total is None else items
        # Academic formatting: no emojis, clear description, timing
        return iter(tqdm(seq, desc=desc, total=total, leave=False,
                        bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"))
    except Exception:
        # Fallback: simple academic logger with timing
        lst = list(items)
        n = len(lst)
        if n == 0:
            return iter(lst)

        step = max(1, n // 20)  # ~5% updates
        start_time = time.time()

        def _gen() -> Iterator[T]:
            for i, x in enumerate(lst, 1):
                if i == 1 or i % step == 0 or i == n:
                    elapsed = time.time() - start_time
                    pct = 100.0 * i / n
                    # Academic format: no fancy symbols, single line
                    # Get terminal width for clean output
                    try:
                        width = os.get_terminal_size().columns
                    except (OSError, AttributeError):
                        width = 80
                    
                    # Create a clean progress message
                    msg = f"Progress {desc}: {i}/{n} ({pct:.1f}%) | Elapsed: {elapsed:.1f}s"
                    if len(msg) > width - 10:
                        msg = msg[:width - 10] + "..."
                    
                    # Clear line and print
                    sys.stdout.write("\r" + " " * (width - 1) + "\r")
                    sys.stdout.write(msg)
                    sys.stdout.flush()
                    
                    if i == n:  # Final update, move to next line
                        sys.stdout.write("\n")
                yield x

        return _gen()