#!/usr/bin/env python3
"""Reproducible authoring-surface proxies; no model or token measurement."""
import argparse
import copy
import difflib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--skill-dir',type=Path,required=True)
parser.add_argument('--output-dir',type=Path,required=True,help='fresh directory')
a=parser.parse_args(); a.output_dir.mkdir(parents=True,exist_ok=False)
runner=a.skill_dir/'scripts/run-animdiagram.py'
module_spec=importlib.util.spec_from_file_location('sl_cost',a.skill_dir/'scripts/generate.py')
g=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(g)
defaults=g.load(a.skill_dir/'defaults/v1.json')
config=json.loads((a.skill_dir/'.installation.json').read_text())
template=(Path(config['dependency'])/'assets/template.svg').read_text()
spec=g.load(a.skill_dir/'tests/fixtures/flow.spec.json')
refined=copy.deepcopy(spec);refined['nodes'][1]['label']='Validate incoming request carefully'

def surfaces(value):
    normalized=g.normalize(value,defaults)
    return (g.static_svg(value,normalized,defaults,template),json.dumps(normalized['motion'],indent=2),json.dumps(value,indent=2))

before=surfaces(spec);after=surfaces(refined)
def changed(a,b):
    return sum(len(line[2:]) for line in difflib.ndiff(a.splitlines(keepends=True),b.splitlines(keepends=True)) if line.startswith(('+ ','- ')))
report={'measurement':'Characters are authoring-surface proxies, not tokens or model context usage. Manual inputs are a layout-equivalent reconstruction, not a live Claude baseline.',
        'actual_model_usage':None,'model_source_reads':None,'manual_creation_characters':len(before[0])+len(before[1]),
        'semantic_creation_characters':len(before[2]),'manual_refinement_changed_characters':changed(before[0],after[0])+changed(before[1],after[1]),
        'semantic_refinement_changed_characters':changed(before[2],after[2]),'runs':[]}
for label,value,surface in [('creation',spec,before),('refinement',refined,after)]:
    folder=a.output_dir/label;folder.mkdir()
    semantic=folder/'semantic.spec.json';semantic.write_text(json.dumps(value,indent=2))
    manual=folder/'manual.svg';motion=folder/'manual.spec.json';motion.write_text(surface[1])
    metrics={}
    for route in ('manual','semantic'):
        manual_commands = [['timeline',str(motion),'--inject',str(manual)],['check',str(manual)]]
        if label == 'creation':
            manual_commands.insert(0, ['template',str(manual)])
        else:
            manual.write_text(surface[0])
        commands=(manual_commands if route=='manual' else
                  [['build',str(semantic),'--out',str(folder/'semantic.svg')]])
        returned=0
        for index,command in enumerate(commands):
            if route=='manual' and command[0]=='timeline':
                manual.write_text(surface[0])
            result=subprocess.run([sys.executable,'-I',str(runner),*command],capture_output=True,text=True)
            if result.returncode: raise RuntimeError(result.stdout+result.stderr)
            returned+=len(result.stdout)+len(result.stderr)
        metrics[route]={'wrapper_calls':len(commands),'tool_output_characters':returned,'model_svg_source_reads':None}
    report['runs'].append({'operation':label,**metrics})
(a.output_dir/'report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
