#!/usr/bin/env python3
"""Smoke an installed skill; all outputs and damaged integrity fixtures are disposable."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--skill-dir', type=Path, required=True)
parser.add_argument('--output-dir', type=Path, help='fresh directory; default retained temporary directory')
args = parser.parse_args()
skill = args.skill_dir.resolve()
if args.output_dir:
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=False)
else:
    out = Path(tempfile.mkdtemp(prefix='sl-smoke-'))
runner = skill / 'scripts/run-animdiagram.py'


def run(*arguments):
    result = subprocess.run([sys.executable, '-I', str(runner), *map(str, arguments)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result


try:
    run('verify')
    for preset in ('flow', 'branch', 'grid', 'enum'):
        spec, svg = out / (preset+'.spec.json'), out / (preset+'.svg')
        shutil.copyfile(skill / 'tests/fixtures' / spec.name, spec)
        run('build', spec, '--out', svg, '--preview')
        run('check', svg)
        ET.parse(svg)
        companion = svg.with_suffix('.agent.md')
        assert companion.is_file() and spec.name in companion.read_text()
        digest = hashlib.sha256(svg.read_bytes()).hexdigest()
        run('build', spec, '--out', svg, '--preview')
        assert digest == hashlib.sha256(svg.read_bytes()).hexdigest(), 'non-deterministic build'
        (out / (preset+'.md')).write_text(f'![{preset}]({svg.name})\n[Diagram semantics]({companion.name})\n')
    config = json.loads((skill / '.installation.json').read_text())
    dependency = Path(config['dependency'])
    ambient_svg, ambient_spec = out / 'ambient.svg', out / 'ambient.spec.json'
    source = (dependency / 'assets/example-async-jobs.svg').read_text()
    source = source.replace('<!-- @motion:elements -->', '<circle class="tick" cx="580" cy="300" r="3" fill="#4CF490"/>\n<!-- @motion:elements -->')
    ambient_svg.write_text(source)
    legacy = json.loads((dependency / 'assets/example-async-jobs.spec.json').read_text())
    next(e for e in legacy['events'] if e['id']=='m3')['ring'] = False
    for event in legacy['events']:
        if event['kind'] in ('phase','show'):
            event['edge'] = .1
            if event['at'] > 0:
                event['at'] += .1
    ambient_spec.write_text(json.dumps(legacy, indent=2))
    run('timeline', ambient_spec, '--inject', ambient_svg)
    legacy['sl'] = {'svg_sha256':hashlib.sha256(ambient_svg.read_bytes()).hexdigest(),
                    'scenarios':[{'id':'first','label':'First','start':0,'end':3},
                                 {'id':'second','label':'Second','start':3,'end':8}]}
    ambient_spec.write_text(json.dumps(legacy, indent=2))
    run('preview', ambient_svg, '--spec', ambient_spec)
    run('preview', ambient_svg, '--plain', '--out', out / 'plain.preview.html')
    result = subprocess.run([sys.executable, '-I', str(skill / 'tests/run.py'), config['dependency']], capture_output=True, text=True)
    (out / 'integration.log').write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError('integration/integrity suite failed; see integration.log')
    print(f'PASS: three presets/four fixtures, compiler/checker/scenario metadata, companions, repeatability, schema and integrity regressions.\nArtifacts: {out}\nVisual and live Claude acceptance are separate checks.')
except (OSError, ValueError, RuntimeError, AssertionError, ET.ParseError) as exc:
    print(f'FAIL: {exc}\nArtifacts: {out}', file=sys.stderr)
    raise SystemExit(1)
