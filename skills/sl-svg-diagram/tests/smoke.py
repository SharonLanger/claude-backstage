#!/usr/bin/env python3
"""Repository smoke for installed native AnimDiagram workflow; disposable outputs only."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote
import xml.etree.ElementTree as ET

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--skill-dir', type=Path, required=True)
p.add_argument('--output-dir', type=Path, help='fresh output directory; default retained temporary directory')
p.add_argument('--preview', action='store_true', help='explicitly create native preview HTML')
p.add_argument('--skip-integration', action='store_true', help='fixture smoke only, explicitly skip integrity test suite')
a = p.parse_args()
skill = a.skill_dir.resolve()
out = a.output_dir.resolve() if a.output_dir else Path(tempfile.mkdtemp(prefix='sl-native-smoke-'))
if a.output_dir:
    out.mkdir(parents=True, exist_ok=False)
runner = skill / 'scripts/run-animdiagram.py'


def run(*arguments):
    result = subprocess.run([sys.executable, '-I', str(runner), *map(str, arguments)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result


try:
    run('verify')
    folder = out / 'nested docs/diagrams'
    svg, spec, agent = [folder / ('request flow' + suffix) for suffix in ('.svg', '.spec.json', '.agent.md')]
    document = folder.parent / 'design notes.md'
    run('template', svg)
    source = svg.read_text().replace('TITLE IN CAPS', 'NATIVE REQUEST').replace(
        'One sentence: the claim this animation demonstrates', 'Illustrative client request, server work, then reply.').replace(
        'WHAT THE PACKETS ARE', 'REQUEST / REPLY')
    # Static SVG is authored here, just as Claude authors geometry in the native route.
    source = source.replace('  <!-- nodes -->', '''  <!-- nodes -->
  <g stroke="#363840" fill="none">
    <line x1="208" y1="148" x2="320" y2="148"/>
    <line x1="320" y1="164" x2="208" y2="164"/>
  </g>
  <g fill="#6F7987">
    <polygon points="314,145 320,148 314,151"/>
    <polygon points="214,161 208,164 214,167"/>
  </g>
  <rect x="96" y="120" width="112" height="56" rx="7" fill="#141416" stroke="#363840"/>
  <rect x="320" y="120" width="112" height="56" rx="7" fill="#141416" stroke="#363840"/>
  <text class="t-name" x="120" y="144">CLIENT</text>
  <text class="t-desc" x="108" y="164">sends / receives</text>
  <text class="t-name" x="344" y="144">SERVER</text>
  <text class="t-desc" x="332" y="164">handles request</text>''')
    svg.write_text(source)
    schedule = {'loop': 4, 'events': [
        {'id':'request', 'kind':'packet', 'at':.3, 'travel':.8, 'from':[208,148], 'to':[320,148],
         'ring':False, 'glow':{'x':320,'y':120,'w':112,'h':56}},
        {'id':'reply', 'kind':'packet', 'after':'request', 'gap':.6, 'travel':.8,
         'from':[320,164], 'to':[208,164], 'ring':False},
        {'id':'phase', 'kind':'phase', 'at':0, 'until':3.7, 'text':'REQUEST THEN REPLY', 'x':632,'y':96}
    ]}
    spec.write_text(json.dumps(schedule, indent=2) + '\n')
    # Hand-authored meaning from the known fixture, not inferred from SVG coordinates.
    agent.write_text('''# Illustrative request/reply

Purpose: explain a client asking a server and receiving a reply.
Input: one hypothetical client request; no branch condition.
Order: client sends request; server handles it; server replies to client.
Concurrency: none asserted. Outcome: client receives the reply, then the loop rests.
Assumptions: durations are illustrative; this is not measured execution.
Sources: self-contained hypothetical fixture, not repository behavior.
[Editable motion JSON](request%20flow.spec.json)
''')
    run('timeline', spec, '--inject', svg)
    run('check', svg, '--strict')
    ET.parse(svg)
    first = svg.read_bytes()
    run('timeline', spec, '--inject', svg)
    assert svg.read_bytes() == first, 'native compilation is not repeatable'
    document.write_text('![Animated request/reply](diagrams/request%20flow.svg)\n'
                        '[Diagram meaning](diagrams/request%20flow.agent.md)\n')
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', document.read_text()):
        assert (document.parent / unquote(link)).is_file(), link
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', agent.read_text()):
        assert (agent.parent / unquote(link)).is_file(), link
    assert not list(out.rglob('*.html')), 'HTML appeared without an explicit preview request'
    if a.preview:
        run('preview', svg)
        assert svg.with_suffix('.preview.html').is_file()
        assert svg.read_bytes() == first, 'preview changed standalone SVG'
    if not a.skip_integration:
        config = json.loads((skill / '.installation.json').read_text())
        result = subprocess.run([sys.executable, '-I', str(Path(__file__).parent / 'run.py'), config['dependency'],
                                 '--skill-dir', str(skill)], capture_output=True, text=True)
        (out / 'integration.log').write_text(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError('integration tests failed; see integration.log')
    print(f'PASS: native template/timeline/check, repeatability, companion and relative Markdown links.\n'
          f'HTML: {"explicit native preview" if a.preview else "none (default)"}. '
          f'Integration: {"SKIPPED by request" if a.skip_integration else "PASS"}.\n'
          f'Artifacts: {out}\nVisual/live Claude checks are separate.')
except (OSError, ValueError, RuntimeError, AssertionError, ET.ParseError) as exc:
    print(f'FAIL: {exc}\nArtifacts: {out}', file=sys.stderr)
    raise SystemExit(1)
