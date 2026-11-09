#!/usr/bin/env python3
"""Run a wrapper with Path.home mocked to a disposable profile; environment stays intact."""
from pathlib import Path
import runpy
import sys
from unittest.mock import patch

profile = Path(sys.argv.pop(1)).resolve()
sys.argv.pop(0)
with patch.object(Path, 'home', return_value=profile):
    runpy.run_path(sys.argv[0], run_name='__main__')
