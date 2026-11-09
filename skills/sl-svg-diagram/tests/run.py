#!/usr/bin/env python3
"""Run repository integration tests against a source or installed runtime."""
import argparse
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('checkout', type=Path, help='existing audited dependency checkout')
parser.add_argument('--skill-dir', type=Path, help='runtime under test; defaults to repository skill')
args = parser.parse_args()
for suite in ('test_wrapper.py', 'test_generation.py', 'test_preview.py'):
    command = [sys.executable, '-I', str(Path(__file__).parent / suite), str(args.checkout)]
    if args.skill_dir:
        command += ['--skill-dir', str(args.skill_dir.resolve())]
    result = subprocess.run(command)
    if result.returncode:
        raise SystemExit(result.returncode)
