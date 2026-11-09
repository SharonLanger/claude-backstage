#!/usr/bin/env python3
"""Run all deterministic integration tests with an existing pinned checkout."""
from pathlib import Path
import subprocess
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 -I tests/run.py /path/to/audited/animdiagram')
for suite in ('test_wrapper.py', 'test_generation.py', 'test_preview.py'):
    result = subprocess.run([sys.executable, '-I', str(Path(__file__).parent / suite), sys.argv[1]])
    if result.returncode:
        raise SystemExit(result.returncode)
