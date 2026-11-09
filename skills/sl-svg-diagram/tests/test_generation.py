#!/usr/bin/env python3
"""Semantic generation integration tests, using a real disposable audited checkout."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

SOURCE = Path(__file__).resolve().parents[1]
CHECKOUT = Path(sys.argv.pop(1)).resolve() if len(sys.argv) > 1 else None
PIN = 'a8edca75f041ebb75c74ac9d3b3fbec3b9cd5486'


class GenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='sl generation ')
        cls.base = Path(cls.temp.name)
        cls.dep = cls.base / 'dependency'
        subprocess.run(['git', 'clone', '--quiet', '--no-hardlinks', str(CHECKOUT), str(cls.dep)], check=True)
        subprocess.run(['git', 'checkout', '--quiet', '--detach', PIN], cwd=cls.dep, check=True)
        cls.skill = cls.base / 'installed skill'
        command = [sys.executable, '-I', str(SOURCE / 'scripts/run-animdiagram.py'), 'setup',
                   '--skill-dir', str(cls.skill), '--dependency-dir', str(cls.dep)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        cls.runner = cls.skill / 'scripts/run-animdiagram.py'
        module_spec = importlib.util.spec_from_file_location('generation_test_module', cls.skill / 'scripts/generate.py')
        cls.generator = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(cls.generator)
        cls.defaults = json.loads((cls.skill / 'defaults/v1.json').read_text())

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.work = Path(tempfile.mkdtemp(dir=self.base))
        self.spec = self.work / 'request flow.spec.json'
        self.svg = self.work / 'request flow.svg'
        self.agent = self.svg.with_suffix('.agent.md')
        self.debug = self.work / 'normalized.json'

    def fixture(self, name='flow'):
        return json.loads((SOURCE / 'tests/fixtures' / (name + '.spec.json')).read_text())

    def build(self, value, debug=True, extra=(), runner=None, env=None):
        self.spec.write_text(json.dumps(value))
        args = [sys.executable, '-I', str(runner or self.runner), 'build', str(self.spec), '--out', str(self.svg)]
        if debug:
            self.debug.unlink(missing_ok=True)
            args += ['--debug-normalized', str(self.debug)]
        return subprocess.run(args + list(extra), capture_output=True, text=True, env=env)

    def good(self, spec):
        result = self.build(spec)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertLess(len(result.stdout), 1500)
        self.assertNotIn('<svg', result.stdout)
        return json.loads(self.debug.read_text())

    def invalid(self, spec, text):
        result = self.build(spec)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn(text, result.stderr)
        self.assertFalse(self.svg.exists())
        self.assertFalse(self.agent.exists())
        self.assertFalse(self.debug.exists())

    def test_three_presets_real_compiler_and_repeatability(self):
        for name in ('flow', 'branch', 'grid'):
            with self.subTest(preset=name):
                spec = self.fixture(name)
                normalized = self.good(spec)
                root = ET.parse(self.svg).getroot()
                nodes = [e for e in root.iter() if 'data-node' in e.attrib]
                routes = [e for e in root.iter() if 'data-link' in e.attrib]
                self.assertEqual(len(nodes), len(spec['nodes']))
                self.assertEqual(len(routes), len(spec['links']))
                self.assertIn('@keyframes s0_e1', self.svg.read_text())
                self.assertIn(spec['explanation'], self.agent.read_text())
                self.assertIn('request%20flow.spec.json', self.agent.read_text())
                before = [self.svg.read_bytes(), self.agent.read_bytes()]
                self.good(spec)
                self.assertEqual(before, [self.svg.read_bytes(), self.agent.read_bytes()])
                for box in normalized['boxes'].values():
                    x, y, w, h = box
                    margin = normalized['settings']['outer_margin']
                    self.assertGreaterEqual(x, margin)
                    self.assertLessEqual(x+w, normalized['width']-margin)
                    self.assertLessEqual(y+h, normalized['height']-margin)

    def test_schema_rejects_bad_inputs_with_useful_diagnostics(self):
        cases = []
        def case(edit, message):
            spec = self.fixture()
            edit(spec)
            cases.append((spec, message))
        case(lambda s: s.update(format='future'), 'unsupported format')
        case(lambda s: s.update(defaults_version='v99'), 'unsupported defaults_version')
        case(lambda s: s.update(surprise=True), 'unknown fields')
        case(lambda s: s.pop('claim'), 'missing fields')
        case(lambda s: s['nodes'].append(copy.deepcopy(s['nodes'][0])), 'duplicate node ID')
        case(lambda s: s['links'][0].update(to='absent'), 'missing node reference')
        case(lambda s: s['scenarios'].append(copy.deepcopy(s['scenarios'][0])), 'duplicate scenario ID')
        case(lambda s: s['scenarios'][0]['steps'].append({'node':'missing'}), 'missing node reference')
        case(lambda s: s.update(settings={'gap':float('nan')}), 'finite number')
        case(lambda s: s.update(settings={'travel':float('inf')}), 'finite number')
        case(lambda s: s.update(settings={'node_width':0}), 'finite number')
        case(lambda s: s.update(settings={'pause':True}), 'finite number')
        case(lambda s: s.update(settings={'made_up':2}), 'unknown fields')
        case(lambda s: s['nodes'][0].update(id='<x>'), 'invalid ID')
        case(lambda s: s.update(layout='graph'), 'unsupported layout')
        case(lambda s: s['sources'].append({'label':'bad','url':'javascript:alert(1)'}), 'valid http(s)')
        case(lambda s: s['sources'].append({'label':'bad','url':'https://['}), 'valid http(s)')
        case(lambda s: s['nodes'][0].update(label='\ud800'), 'invalid XML character')
        case(lambda s: s['scenarios'][0]['steps'].append({'parallel':[]}), 'parallel:')
        case(lambda s: s['scenarios'][0]['steps'].append({'link':'accept', 'node':'input'}), 'exactly one')
        for spec, message in cases:
            with self.subTest(message=message):
                self.invalid(spec, message)

    def test_unsupported_topology_rejected(self):
        for name in ('flow', 'branch', 'grid'):
            spec = self.fixture(name)
            if name == 'flow':
                spec['links'][1]['from'] = 'input'  # chain is no longer linear
            elif name == 'branch':
                spec['links'].append({'id':'merge','from':'yes','to':'no'})
            else:
                spec['links'] = [{'id':'edge','from':'peer1','to':'peer2'}]
            with self.subTest(name=name):
                self.invalid(spec, 'requires')

    def test_grid_five_six_and_ordered_six(self):
        spec = self.fixture('grid')
        six = self.good(spec)
        self.assertEqual(len({b[0] for b in six['boxes'].values()}), 3)
        self.assertEqual(len({b[1] for b in six['boxes'].values()}), 2)
        spec['nodes'].pop()
        spec['scenarios'][0]['steps'][0]['parallel'].pop()
        five = self.good(spec)
        self.assertEqual(len(five['boxes']), 5)
        # Selecting the grid preset also permits five independent items.
        spec = self.fixture()
        spec['nodes'] = [{'id':f'n{i}', 'label':f'Step {i}'} for i in range(6)]
        spec['links'] = [{'id':f'l{i}', 'from':f'n{i}', 'to':f'n{i+1}'} for i in range(5)]
        spec['scenarios'][0]['steps'] = [{'link':f'l{i}'} for i in range(5)]
        ordered = self.good(spec)
        boxes = [ordered['boxes'][f'n{i}'] for i in range(6)]
        self.assertEqual(len({b[0] for b in boxes}), 1)
        self.assertEqual([b[1] for b in boxes], sorted(b[1] for b in boxes))

    def test_timing_order_parallel_branches_and_complete_tails(self):
        spec = self.fixture('branch')
        n = self.good(spec)
        events = {e['id']:e for e in n['motion']['events']}
        self.assertEqual(events['s0_e2']['to'], n['routes']['true_route'][-1])
        self.assertEqual(events['s1_e2']['to'], n['routes']['false_route'][-1])
        self.assertGreater(events['s0_e2']['at'], events['s0_e1']['at'])
        self.assertEqual(n['scenarios'][0]['end'], n['scenarios'][1]['start'])
        tail = n['settings']['effect_tail'] + n['settings']['pause'] + n['settings']['reset']
        self.assertAlmostEqual(n['scenarios'][0]['end']-events['s0_e2']['at']-n['settings']['travel'], tail)
        n = self.good(self.fixture('grid'))
        self.assertEqual(len({e['at'] for e in n['motion']['events'] if e['kind']=='pulse'}),1)

    def test_overrides_and_saved_spec_independent_of_profile(self):
        spec = self.fixture()
        before = self.good(spec)
        original = self.svg.read_bytes()
        home = self.work / 'profile'
        pref = home / '.claude/sl-svg-diagram/preferences.md'
        pref.parent.mkdir(parents=True)
        pref.write_text('Use absurdly giant labels globally.\n')
        result = self.build(spec, env={**os.environ, 'HOME':str(home)})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(original,self.svg.read_bytes())
        spec['settings']={'outer_margin':40,'gap':80, 'font_size':16}
        after = self.good(spec)
        self.assertNotEqual(before['boxes'], after['boxes'])
        self.assertEqual(after['settings']['outer_margin'],40)
        self.assertNotEqual(original,self.svg.read_bytes())

    def test_long_labels_tags_panel_caption_and_fitting_failure(self):
        spec = self.fixture('grid')
        n = self.good(spec)
        self.assertTrue(all(len(parts[1])>1 for parts in n['wrapped'].values()))
        right = max(b[0]+b[2] for b in n['boxes'].values())
        panel_x = n['settings']['outer_margin'] + n['flow_width'] + n['settings']['panel_gutter']
        self.assertGreaterEqual(panel_x-right, n['settings']['panel_gutter'])
        self.assertGreater(n['caption_y'],max(b[1]+b[3] for b in n['boxes'].values()))
        spec['settings']={'document_width':320}
        self.svg.unlink(); self.agent.unlink()
        self.invalid(spec,'unreadable')

    def test_literal_escaping_and_grounded_sources(self):
        spec = self.fixture()
        hostile = '</script><script>alert("&")</script>'
        spec['nodes'][0]['label']=hostile
        spec['scenarios'][0]['label']=hostile
        spec['title']='XML < & > " characters'
        spec['sources']=[{'label':'Source <reference>','url':'https://example.invalid/a?x=1&y=2'}]
        self.good(spec)
        root=ET.parse(self.svg).getroot()
        self.assertFalse(any(e.tag.endswith('script') for e in root.iter()))
        self.assertIn(hostile, ''.join(e.text or '' for e in root.iter() if e.tag.endswith('}text')))
        self.assertIn('https://example.invalid/a?x=1&amp;y=2',self.agent.read_text())
        self.assertNotIn('<script>',self.agent.read_text())

    def test_invalid_rebuild_and_manual_file_preservation(self):
        spec = self.fixture()
        self.good(spec)
        before = self.svg.read_bytes(), self.agent.read_bytes()
        spec['nodes'][0]['label']=''
        result=self.build(spec)
        self.assertEqual(result.returncode,2)
        self.assertEqual(before,(self.svg.read_bytes(),self.agent.read_bytes()))
        for path in (self.svg,self.agent):
            path.write_text('manual work')
            result=self.build(self.fixture())
            self.assertEqual(result.returncode,2)
            self.assertIn('manual file',result.stderr)
            self.assertEqual(path.read_text(),'manual work')
            path.unlink()

    def test_integrity_blocks_build_before_upstream_executes(self):
        for damage in ('head','file'):
            with self.subTest(damage=damage):
                dep=self.work / damage / PIN
                dep.parent.mkdir()
                subprocess.run(['git','clone','--quiet','--no-hardlinks',str(self.dep),str(dep)],check=True)
                skill=self.work / ('skill-'+damage)
                shutil.copytree(self.skill,skill)
                (skill/'.installation.json').write_text(json.dumps({'commit':PIN,'dependency':str(dep)}))
                sentinel=self.work / ('executed-'+damage)
                if damage=='head':
                    tree=subprocess.check_output(['git','rev-parse','HEAD^{tree}'],cwd=dep,text=True).strip()
                    env={**os.environ,'GIT_AUTHOR_NAME':'Test','GIT_AUTHOR_EMAIL':'test@example.invalid',
                         'GIT_COMMITTER_NAME':'Test','GIT_COMMITTER_EMAIL':'test@example.invalid'}
                    commit=subprocess.check_output(['git','commit-tree',tree,'-p',PIN,'-m','wrong head'],cwd=dep,env=env,text=True).strip()
                    subprocess.run(['git','update-ref','HEAD',commit],cwd=dep,check=True)
                else:
                    (dep/'scripts/timeline.py').write_text(f'open({str(sentinel)!r}, "w").write("BAD")\n')
                result=self.build(self.fixture(),runner=skill/'scripts/run-animdiagram.py')
                self.assertEqual(result.returncode,2)
                self.assertIn('execution blocked',result.stderr)
                self.assertFalse(sentinel.exists())
                self.assertFalse(self.svg.exists())


if __name__=='__main__':
    if CHECKOUT is None:
        raise SystemExit('Usage: test_generation.py /path/to/audited/animdiagram')
    unittest.main(verbosity=2)
