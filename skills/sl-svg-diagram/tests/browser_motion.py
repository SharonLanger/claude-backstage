#!/usr/bin/env python3
"""Repository browser animation smoke; run with enforced outbound network denial."""
import argparse
import json
from pathlib import Path
import socket
from playwright.sync_api import sync_playwright

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--examples-dir', type=Path, required=True)
p.add_argument('--output-dir', type=Path, required=True)
p.add_argument('--names', nargs='+', default=['flow','branch','grid','enum'])
a = p.parse_args()
a.output_dir.mkdir(parents=True, exist_ok=True)
assert not any(line.split()[1] == '00000000' for line in Path('/proc/net/route').read_text().splitlines()[1:]), 'Network isolation required'
try:
    socket.create_connection(('1.1.1.1', 443), timeout=1).close()
except OSError:
    pass
else:
    raise AssertionError('External networking available')

reports = []
with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    for name in a.names:
        svg = a.examples_dir/(name+'.svg')
        spec = json.loads((a.examples_dir/(name+'.spec.json')).read_text())
        expected = {}
        concurrent_groups = []
        for i, scenario in enumerate(spec['scenarios']):
            serial = 0
            for step in scenario['steps']:
                group = []
                for item in step.get('parallel', [step]):
                    serial += 1
                    event_id = f's{i}_e{serial}'
                    expected[event_id] = 'packet' if 'link' in item else 'pulse'
                    group.append(event_id)
                if len(group) > 1:
                    concurrent_groups.append(group)
        assert expected, f'{name}: no expected semantic motion events'
        page = browser.new_page(viewport={'width':1000,'height':1600}, reduced_motion='no-preference')
        page.set_content('<style>body{margin:0}svg{max-width:100%;height:auto}</style>'+svg.read_text())
        page.wait_for_timeout(50)
        initial = page.evaluate('''() => {
          const animations=document.getAnimations();
          const duration=animations[0]?.effect.getTiming().duration;
          const svg=document.querySelector('svg'),vb=svg.viewBox.baseVal;
          const clearance=[...svg.querySelectorAll('text')].filter(e=>{const b=e.getBBox();return b.width>0&&(b.x<19||b.y<19||b.x+b.width>vb.width-19||b.y+b.height>vb.height-19)}).map(e=>e.textContent);
          const nodeFailures=[];
          for(const g of svg.querySelectorAll('[data-node]')){
            const r=g.querySelector('rect'),x=+r.getAttribute('x'),y=+r.getAttribute('y'),w=+r.getAttribute('width'),h=+r.getAttribute('height');
            for(const t of g.querySelectorAll('text')){const b=t.getBBox();if(b.x<x+2||b.y<y+2||b.x+b.width>x+w-2||b.y+b.height>y+h-2)nodeFailures.push(g.dataset.node)}
          }
          const events=animations.filter(a=>/^s\\d+_e\\d+$/.test(a.animationName)).map(a=>{
            const frames=a.effect.getKeyframes().filter(f=>f.opacity!==undefined);
            const positive=frames.filter(f=>+f.opacity>.1).map(f=>f.offset);
            const first=Math.min(...positive);
            const onset=Math.max(...frames.filter(f=>+f.opacity===0&&f.offset<first).map(f=>f.offset));
            return {name:a.animationName,kind:a.effect.target.classList.contains('pkt')?'packet':'pulse',positive,onset};
          });
          return {animations:animations.length,duration,clearance,nodeFailures,events,
            packetCount:document.querySelectorAll('.pkt').length,
            labels:[...document.querySelectorAll('[data-node]')].map(n=>n.dataset.node)};
        }''')
        assert initial['animations'] > 0, f'{name}: no running animation'
        assert not initial['clearance'] and not initial['nodeFailures'], (name,initial)
        assert set(initial['labels']) == {n['id'] for n in spec['nodes']}
        observed = {event['name']: event for event in initial['events']}
        assert set(observed) == set(expected), f'{name}: missing or extra semantic animations'
        for event_id, kind in expected.items():
            event = observed[event_id]
            assert event['kind'] == kind and event['positive'], (name, event_id, event)
            assert event['onset'] is not None, f'{name}: missing visibility onset for {event_id}'
        for group in concurrent_groups:
            onsets = {observed[event_id]['onset'] for event_id in group}
            assert len(onsets) == 1, f'{name}: authored parallel group has different starts: {group}'
        samples = page.evaluate('''async ({duration,events}) => {
          const animations=document.getAnimations(), samples=[];
          for(const anim of animations)anim.pause();
          // Include exact seam and a dense cycle sweep to detect overlapping scenarios.
          // Target every expected event's positive keyframes as well as the
          // cycle grid, so short packets/pulses cannot evade the assertions.
          const times=new Set(Array.from({length:241},(_,i)=>duration*i/240));
          for(const event of events)for(const offset of event.positive)times.add(duration*offset);
          for(const time of [...times].sort((a,b)=>a-b)){
            for(const anim of animations)anim.currentTime=time;
            await new Promise(requestAnimationFrame);
            const visible=[...document.querySelectorAll('.story')].filter(e=>+getComputedStyle(e).opacity>.05).map(e=>({name:e.style.animationName,text:e.textContent}));
            const scenarioIds=[...new Set(visible.map(e=>(e.name.match(/^s(\\d+)_/)||[])[1]).filter(Boolean))];
            const packets=[...document.querySelectorAll('.pkt')].map(e=>({name:e.style.animationName,opacity:+getComputedStyle(e).opacity,transform:getComputedStyle(e).transform}));
            const pulses=[...document.querySelectorAll('.ring')].filter(e=>/^s\\d+_e\\d+$/.test(e.style.animationName)).map(e=>({name:e.style.animationName,opacity:+getComputedStyle(e).opacity,transform:getComputedStyle(e).transform}));
            samples.push({time,visible,scenarioIds,packets,pulses});
          }
          return samples;
        }''', {'duration':initial['duration'],'events':initial['events']})
        assert all(len(s['scenarioIds']) <= 1 for s in samples), f'{name}: captions from different scenarios overlap'
        for i, scenario in enumerate(spec['scenarios']):
            visible=[s for s in samples if str(i) in s['scenarioIds']]
            assert visible, f'{name}: scenario {i} never visible'
            combined=' '.join(x['text'] for sample in visible for x in sample['visible'])
            assert all(word in combined for word in scenario['label'].split()), f'{name}: missing scenario label'
            assert all(word in combined for word in scenario['outcome'].split()), f'{name}: missing outcome'
            # Capture each scenario near its active middle using observed caption window.
            capture_time=visible[len(visible)//2]['time']
            page.evaluate('t=>document.getAnimations().forEach(a=>a.currentTime=t)',capture_time)
            page.locator('svg').screenshot(path=str(a.output_dir/f'{name}-scenario-{i}.png'),animations='allow')
        transforms={}
        for sample in samples:
            for packet in sample['packets']:
                if packet['opacity']>.1:
                    transforms.setdefault(packet['name'],set()).add(packet['transform'])
        expected_packets={key for key,kind in expected.items() if kind=='packet'}
        assert set(transforms)==expected_packets, f'{name}: expected packet was never visibly sampled'
        assert all(len(transforms[key])>1 for key in expected_packets), f'{name}: packet failed to travel'
        expected_pulses={key for key,kind in expected.items() if kind=='pulse'}
        visible_pulses={pulse['name'] for sample in samples for pulse in sample['pulses'] if pulse['opacity']>.1}
        assert visible_pulses==expected_pulses, f'{name}: expected pulse was never visibly sampled'
        # Resume our inspection pauses so reduced-motion cannot pass merely
        # because the test itself left the animations paused.
        page.evaluate('()=>document.getAnimations().forEach(a=>a.play())')
        page.emulate_media(reduced_motion='reduce')
        page.wait_for_timeout(50)
        reduced=page.evaluate('''() => ({
          animations:document.getAnimations().length,
          active:document.getAnimations().filter(a=>a.playState==='running').length,
          nodes:document.querySelectorAll('[data-node]').length,
          external:[...document.querySelectorAll('[href],[src]')].map(e=>e.getAttribute('href')||e.getAttribute('src')).filter(s=>/^(https?:)?\\/\\//.test(s))
        })''')
        assert reduced['animations']==0 and reduced['active']==0 and reduced['nodes']==len(spec['nodes']) and not reduced['external'], (name,reduced)
        reports.append({'fixture':name,**initial,'scenarios_checked':len(spec['scenarios']),'cycle_samples':len(samples),'caption_exclusivity':True,'packet_travel':True if expected_packets else 'not_applicable','pulses_checked':len(expected_pulses),'parallel_groups_checked':len(concurrent_groups),'reduced_motion':reduced})
        page.close()
    browser.close()
(a.output_dir/'motion.json').write_text(json.dumps(reports,indent=2)+'\n')
print(json.dumps({'passed':True,'fixtures':len(reports),'scenarios':sum(r['scenarios_checked'] for r in reports),'report':str(a.output_dir/'motion.json')}))
