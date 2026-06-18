#!/usr/bin/env python3
"""Example helper script invoked via the run_script tool.

run_script targets live in scripts/ and must be .py. They run with a real system
Python (not the frozen sidecar), a 120s timeout, and output capped at 8000 chars.

Usage (args are passed positionally by the agent):
    count_lines.py <path> [<glob>]
Prints a per-extension line count under <path>, restricted to the workspace.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    pattern = argv[2] if len(argv) > 2 else "**/*"
    counts: Counter[str] = Counter()
    for p in root.glob(pattern):
        if p.is_file():
            try:
                counts[p.suffix or "<none>"] += sum(1 for _ in p.open("r", encoding="utf-8", errors="replace"))
            except OSError:
                continue
    for ext, n in counts.most_common():
        print(f"{ext}\t{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
