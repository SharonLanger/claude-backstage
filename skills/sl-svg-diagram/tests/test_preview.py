#!/usr/bin/env python3
"""Scenario preview integration, validation and escaping (real pinned compiler)."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE=Path(__file__).resolve().parents[1]
CHECKOUT=Path(sys.argv.pop(1)).resolve() if len(sys.argv)>1 else None


class PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory(prefix='sl preview ')
        cls.base=Path(cls.temp.name)
        cls.dep=cls.base/'dependency'
        subprocess.run(['git','clone','--quiet','--no-hardlinks',str(CHECKOUT),str(cls.dep)],check=True)
        cls.skill=cls.base/'installed skill'
        cls.runner=cls.skill/'scripts/run-animdiagram.py'
        result=subprocess.run([sys.executable,'-I',str(SOURCE/'scripts/run-animdiagram.py'),'setup',
                               '--skill-dir',str(cls.skill),'--dependency-dir',str(cls.dep)],capture_output=True,text=True)
        if result.returncode:raise RuntimeError(result.stdout+result.stderr)
        module_spec=importlib.util.spec_from_file_location('sl_preview_tests',cls.skill/'scripts/scenario_preview.py')
        cls.module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(cls.module)

    @classmethod
    def tearDownClass(cls):cls.temp.cleanup()

    def setUp(self):
        self.work=Path(tempfile.mkdtemp(dir=self.base))
        self.spec=self.work/'diagram.spec.json';self.svg=self.work/'diagram.svg';self.preview=self.work/'diagram.preview.html'

    def run_tool(self,*args):
        return subprocess.run([sys.executable,'-I',str(self.runner),*map(str,args)],capture_output=True,text=True)

    def generated(self,name='branch',edit=None):
        spec=json.loads((SOURCE/'tests/fixtures'/(name+'.spec.json')).read_text())
        if edit:edit(spec)
        self.spec.write_text(json.dumps(spec))
        result=self.run_tool('build',self.spec,'--out',self.svg,'--preview')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        return spec

    def data(self):
        text=self.preview.read_text()
        return json.loads(re.search(r'<script type="application/json" id="sl-preview-data">(.*?)</script>',text,re.S).group(1))

    def legacy(self):
        self.svg.write_bytes((self.dep/'assets/example-async-jobs.svg').read_bytes())
        spec=json.loads((self.dep/'assets/example-async-jobs.spec.json').read_text())
        # The upstream example's return ring extends past its phase boundary.
        # Disable that ring, then compile the actual input before attaching ranges.
        next(e for e in spec['events'] if e['id']=='m3')['ring']=False
        for event in spec['events']:
            if event['kind'] in ('phase','show'):
                event['edge']=.1
                if event['at']>0:event['at']+=.1
        self.spec.write_text(json.dumps(spec))
        compiled=self.run_tool('timeline',self.spec,'--inject',self.svg)
        self.assertEqual(compiled.returncode,0,compiled.stderr)
        spec['sl']={'scenarios':[{'id':'first','label':'First','start':0,'end':3},
                                 {'id':'second','label':'Second','start':3,'end':8}],
                    'svg_sha256':hashlib.sha256(self.svg.read_bytes()).hexdigest()}
        self.spec.write_text(json.dumps(spec));return spec

    def test_build_and_preview_reuse_metadata_without_modifying_svg(self):
        for name in ('branch','enum','flow'):
            with self.subTest(name=name):
                spec=self.generated(name)
                before=self.svg.read_bytes()
                meta=self.module.metadata(self.svg.read_text(),self.svg,self.spec)
                self.assertEqual([s['label'] for s in self.data()['scenarios']],[s['label'] for s in spec['scenarios']])
                self.assertEqual(meta,self.data())
                result=self.run_tool('preview',self.svg,'--spec',self.spec)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual(before,self.svg.read_bytes())
                self.assertEqual(meta,self.data())
                self.preview.unlink()

    def test_generated_mismatches_fail_before_writing_html(self):
        spec=self.generated();self.preview.unlink()
        original=self.svg.read_text()
        self.svg.write_text(original.replace('BOOLEAN ROUTES','EDITED ROUTES'))
        result=self.run_tool('preview',self.svg)
        self.assertEqual(result.returncode,2);self.assertIn('content mismatch',result.stderr);self.assertFalse(self.preview.exists())
        self.svg.write_text(original)
        spec['nodes'][0]['label']='Changed input'
        self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg)
        self.assertEqual(result.returncode,2);self.assertIn('spec mismatch',result.stderr);self.assertFalse(self.preview.exists())

    def test_legacy_metadata_missing_metadata_and_plain_fallback(self):
        spec=self.legacy()
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(len(self.data()['scenarios']),2)
        result=self.run_tool('preview',self.svg,'--plain')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertNotIn('sl-preview-data',self.preview.read_text())
        spec.pop('sl');self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertNotIn('sl-preview-data',self.preview.read_text())

    def test_legacy_mismatch_and_loop_mismatch_fail(self):
        spec=self.legacy();self.svg.write_text(self.svg.read_text()+'\n')
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2);self.assertIn('mismatch',result.stderr)
        spec=self.legacy();spec['loop']=9;self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2);self.assertIn('story clock',result.stderr)

    def test_legacy_boundaries_cannot_cut_packets_or_effect_tails(self):
        for boundary in (.5,1.0):
            with self.subTest(boundary=boundary):
                spec=self.legacy()
                spec['sl']['scenarios'][0]['end']=boundary
                spec['sl']['scenarios'][1]['start']=boundary
                self.spec.write_text(json.dumps(spec))
                result=self.run_tool('preview',self.svg,'--spec',self.spec)
                self.assertEqual(result.returncode,2)
                self.assertIn('cuts event/effect tail m1',result.stderr)
                self.assertFalse(self.preview.exists())

    def test_legacy_changed_motion_spec_rejected_even_with_unchanged_hash(self):
        spec=self.legacy();spec['events'][0]['travel']=.6
        self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2)
        self.assertIn('motion spec mismatch',result.stderr)

    def test_skin_variants_preserve_scenarios_and_validate_pairing(self):
        self.generated()
        for theme in ('light','dark'):
            target=self.work/'variants'/(theme+'.svg')
            target.parent.mkdir(exist_ok=True)
            result=self.run_tool('skin',self.svg,'--to',theme,'--out',target)
            self.assertEqual(result.returncode,0,result.stderr)
            result=self.run_tool('preview',target)
            self.assertEqual(result.returncode,0,result.stderr)
            variant=self.module.metadata(target.read_text(),target)
            self.assertEqual(variant,self.data())
        self.assertEqual(self.run_tool('build',self.spec,'--out',self.svg,'--preview').returncode,0)
        self.assertEqual(self.run_tool('preview',self.svg).returncode,0)
        self.assertEqual(self.run_tool('build',self.spec,'--out',self.svg,'--preview').returncode,0)

    def test_output_aliases_cannot_clobber_inputs(self):
        self.generated()
        for source in (self.svg,self.spec):
            before=source.read_bytes()
            for kind in ('direct','hardlink','symlink'):
                target=source if kind=='direct' else self.work/(source.name+'.'+kind)
                if kind=='hardlink':target.hardlink_to(source)
                if kind=='symlink':target.symlink_to(source)
                result=self.run_tool('preview',self.svg,'--out',target)
                self.assertEqual(result.returncode,2,(source,kind,result.stderr))
                self.assertEqual(before,source.read_bytes())
                if kind!='direct':target.unlink()

    def test_legacy_caption_prefade_cannot_enter_previous_scenario(self):
        spec=self.legacy()
        next(e for e in spec['events'] if e['id']=='ph2')['at']=3
        self.spec.write_text(json.dumps(spec))
        self.assertEqual(self.run_tool('timeline',self.spec,'--inject',self.svg).returncode,0)
        spec['sl']['svg_sha256']=hashlib.sha256(self.svg.read_bytes()).hexdigest()
        self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2)
        self.assertIn('cuts event/effect tail ph2',result.stderr)

    def test_legacy_unrepresentable_or_nonpositive_fades_rejected(self):
        for edge in (0,-.1,float('nan'),.000001):
            with self.subTest(edge=edge):
                spec=self.legacy()
                next(e for e in spec['events'] if e['id']=='ph2')['edge']=edge
                self.spec.write_text(json.dumps(spec))
                self.assertEqual(self.run_tool('timeline',self.spec,'--inject',self.svg).returncode,0)
                spec['sl']['svg_sha256']=hashlib.sha256(self.svg.read_bytes()).hexdigest()
                self.spec.write_text(json.dumps(spec))
                result=self.run_tool('preview',self.svg,'--spec',self.spec)
                self.assertEqual(result.returncode,2)
                self.assertIn('positive',result.stderr)

    def test_legacy_actual_rounded_keyframe_cannot_enter_previous_window(self):
        spec=self.legacy()
        spec['events']=[{'id':'probe','kind':'pulse','at':3.00001,'dur':.5,'x':100,'y':100}]
        spec['sl']['scenarios'][0]['end']=3.00001
        spec['sl']['scenarios'][1]['start']=3.00001
        self.spec.write_text(json.dumps(spec))
        self.assertEqual(self.run_tool('timeline',self.spec,'--inject',self.svg).returncode,0)
        spec['sl']['svg_sha256']=hashlib.sha256(self.svg.read_bytes()).hexdigest()
        self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2)
        self.assertIn('cuts event/effect tail probe',result.stderr)

    def test_legacy_collapsed_visibility_offsets_rejected(self):
        for kind in ('packet','pulse'):
            with self.subTest(kind=kind):
                spec=self.legacy();spec['loop']=2
                event={'id':'tiny','kind':kind,'at':1}
                if kind=='packet':event.update(travel=.000001,ring=False,**{'from':[20,20],'to':[100,20]})
                else:event.update(dur=.000001,x=100,y=100)
                spec['events']=[event]
                spec['sl']['scenarios'][0].update(end=1)
                spec['sl']['scenarios'][1].update(start=1,end=2)
                self.spec.write_text(json.dumps(spec))
                self.assertEqual(self.run_tool('timeline',self.spec,'--inject',self.svg).returncode,0)
                spec['sl']['svg_sha256']=hashlib.sha256(self.svg.read_bytes()).hexdigest()
                self.spec.write_text(json.dumps(spec))
                result=self.run_tool('preview',self.svg,'--spec',self.spec)
                self.assertEqual(result.returncode,2)
                self.assertIn('collapses visibility offsets',result.stderr)

    def test_range_validation_rejects_invalid_metadata(self):
        valid=[{'id':'a','label':'A','start':0,'end':2},{'id':'b','label':'B','start':2,'end':4}]
        edits=[lambda s:s[1].update(id='a'),lambda s:s[0].update(start=-1),lambda s:s[0].update(end=5),
               lambda s:s[1].update(start=1),lambda s:s[0].update(end=0),lambda s:s[0].update(start=True),
               lambda s:s[0].update(end=float('nan')),lambda s:s[0].update(other=0),lambda s:s[0].update(label='')]
        for edit in edits:
            value=copy.deepcopy(valid);edit(value)
            with self.subTest(value=value):
                with self.assertRaises(self.module.PreviewError):self.module.ranges(4,value)
        for loop in (0,False,float('inf'),'4'):
            with self.assertRaises(self.module.PreviewError):self.module.ranges(loop,valid)

    def test_html_escaping_labels_filename_and_placeholder_text(self):
        hostile='</script><script>window.PWNED=1</script> & __SVG__ __NAME__ __DATA__'
        self.generated(edit=lambda s:s['scenarios'][0].update(label=hostile))
        self.assertEqual(self.data()['scenarios'][0]['label'],hostile)
        self.assertNotIn('<script>window.PWNED',self.preview.read_text())
        page=self.module.page(self.svg.read_text(),'x</title><script>bad()</script>',self.data())
        self.assertNotIn('<script>bad()',page)
        self.assertEqual(page.count('<script>'),1)

    def test_preview_output_and_manual_build_preservation(self):
        self.generated();before=self.svg.read_bytes()
        result=self.run_tool('preview',self.svg,'--out',self.svg)
        self.assertEqual(result.returncode,2);self.assertEqual(before,self.svg.read_bytes())
        self.preview.write_text('manual preview')
        result=self.run_tool('build',self.spec,'--out',self.svg,'--preview')
        self.assertEqual(result.returncode,2);self.assertIn('manual preview',result.stderr)
        self.assertEqual(self.preview.read_text(),'manual preview')
        self.assertEqual(before,self.svg.read_bytes())

    def test_unknown_metadata_and_duplicate_spec_keys_fail(self):
        spec=self.legacy();spec['sl']['unknown']=0;self.spec.write_text(json.dumps(spec))
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2);self.assertIn('requires',result.stderr)
        self.spec.write_text('{"loop":8,"loop":9}')
        result=self.run_tool('preview',self.svg,'--spec',self.spec)
        self.assertEqual(result.returncode,2);self.assertIn('duplicate',result.stderr)


if __name__=='__main__':
    if CHECKOUT is None:raise SystemExit('Usage: test_preview.py /path/to/audited/animdiagram')
    unittest.main(verbosity=2)
