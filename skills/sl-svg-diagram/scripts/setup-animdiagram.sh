#!/usr/bin/env bash
set -euo pipefail
script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 -I "$script_dir/run-animdiagram.py" setup "$@"
