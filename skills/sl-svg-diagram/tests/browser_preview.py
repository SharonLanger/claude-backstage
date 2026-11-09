#!/usr/bin/env python3
"""Real Chromium scenario/playback assertions; requires OS outbound network denial.

Virtual browser time drives full cycles; an additional real-time sample verifies
normal playback speed. No browser/network mocking substitutes for rendering.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import socket
import time
from playwright.sync_api import sync_playwright

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--examples-dir',type=Path,required=True)
p.add_argument('--output-dir',type=Path,required=True)
a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
if any(line.split()[1]=='00000000' for line in Path('/proc/net/route').read_text().splitlines()[1:]):
    raise SystemExit('Refusing browser: default network route exists')
try:
    with socket.create_connection(('1.1.1.1',443),timeout=1):raise SystemExit('Refusing browser: external socket succeeded')
except OSError:pass

SNAPSHOT='''() => ({
  selected:document.querySelector('#scenario').value,
  playing:document.querySelector('#play').getAttribute('aria-pressed')==='true',
  time:+document.querySelector('#scrub').value,
  min:+document.querySelector('#scrub').min,max:+document.querySelector('#scrub').max,
  animations:document.querySelector('#wrap').getAnimations({subtree:true}).map(a=>({
    name:a.animationName,time:a.currentTime,state:a.playState,
    opacity:getComputedStyle(a.effect.target).opacity,transform:getComputedStyle(a.effect.target).transform,
    period:a.effect.getComputedTiming().duration,
    ambient:!!a.effect.target.style.animationDuration||a.effect.target.matches('.tick')
  }))
})'''
reports=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for fixture,labels in [('branch',['All','enabled=true','enabled=false']),
                           ('enum',['All','mode=read','mode=write','mode=batch','mode=skip'])]:
        html_path=a.examples_dir/(fixture+'.preview.html');svg_path=a.examples_dir/(fixture+'.svg')
        before=hashlib.sha256(svg_path.read_bytes()).hexdigest()
        page=browser.new_page(viewport={'width':1100,'height':1000})
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        page.clock.install()
        page.set_content(html_path.read_text())
        assert page.locator('#scenario option').all_text_contents()==labels
        meta=page.eval_on_selector('#sl-preview-data','e=>JSON.parse(e.textContent)')
        windows=meta['scenarios'];loop=meta['loop']
        # Sample an entire authored All cycle, plus a complete wrap.
        visited=[];outcomes=set();resets=set()
        for _ in range(int((loop+.3)/.08)+1):
            page.clock.run_for(80)
            snap=page.evaluate(SNAPSHOT);seconds=snap['time']
            selected=next(i for i,s in enumerate(windows) if s['start']<=seconds<s['end'])
            if not visited or visited[-1]!=selected:visited.append(selected)
            for animation in snap['animations']:
                if '_outcome' in animation['name'] and float(animation['opacity'])>.8:outcomes.add(selected)
            story=[v for v in snap['animations'] if '_e' in v['name']]
            if seconds>windows[selected]['end']-.15 and all(float(v['opacity'])<.01 for v in story):resets.add(selected)
        assert visited[:len(windows)]==list(range(len(windows))) and visited[len(windows)]==0,visited
        assert outcomes==set(range(len(windows))),outcomes
        assert resets==set(range(len(windows))),resets
        # Every named choice repeats exclusively; computed effect visibility follows that route.
        for index,window in enumerate(windows):
            page.select_option('#scenario',window['id'])
            was=page.evaluate(SNAPSHOT);assert was['playing']
            assert abs(was['time']-window['start'])<.001
            for _ in range(int((window['end']-window['start']+.25)/.08)+1):
                page.clock.run_for(80);snap=page.evaluate(SNAPSHOT)
                assert window['start']<=snap['time']<window['end'],snap
                for animation in snap['animations']:
                    if animation['name'].startswith('s') and not animation['name'].startswith(f's{index}_'):
                        assert float(animation['opacity'])<.01,animation
            # Arrival glow and full tail are inside the selected range, followed by outcome pause/reset.
            page.click('#play');assert not page.evaluate(SNAPSHOT)['playing']
            pause=page.evaluate(SNAPSHOT)
            page.clock.run_for(250)
            assert page.evaluate(SNAPSHOT)['animations']==pause['animations']
            page.select_option('#scenario',windows[(index+1)%len(windows)]['id'])
            assert not page.evaluate(SNAPSHOT)['playing']
            page.select_option('#scenario',window['id'])
            # Scrubbing and static frame stay in the selected range while paused.
            mid=(window['start']+window['end'])/2
            page.eval_on_selector('#scrub','(e,v)=>{e.value=v;e.dispatchEvent(new Event("input"))}',mid)
            assert abs(page.evaluate(SNAPSHOT)['time']-mid)<.002
            # Immediately before each boundary, other scenario captions/effects stay hidden.
            page.eval_on_selector('#scrub','(e,v)=>{e.value=v;e.dispatchEvent(new Event("input"))}',window['end']-.025)
            boundary=page.evaluate(SNAPSHOT)
            for animation in boundary['animations']:
                if animation['name'].startswith('s') and not animation['name'].startswith(f's{index}_'):
                    assert float(animation['opacity'])<.01,animation
            page.select_option('#scenario',window['id'])
            for animation in page.evaluate(SNAPSHOT)['animations']:
                if animation['name'].startswith('s') and not animation['name'].startswith(f's{index}_'):
                    assert float(animation['opacity'])<.01,animation
            page.click('#static');static=page.evaluate(SNAPSHOT)
            assert abs(static['time']-(window['end']-.001))<.002 and not static['playing']
            page.locator('#scenario').focus()
            page.keyboard.press('Space');page.keyboard.press('ArrowLeft');page.keyboard.press('Escape')
            assert not page.evaluate(SNAPSHOT)['playing'], 'select keyboard toggled playback'
            page.click('#play')
        page.click('#bg');assert 'light' in page.locator('body').get_attribute('class')
        page.click('#zoom');assert page.locator('#wrap').evaluate('e=>e.style.transform')=='scale(2)'
        page.click('#zoom')
        # Keyboard works outside controls, including selected-range wrapping.
        page.locator('main').click(position={'x':2,'y':2});page.keyboard.press('Space')
        assert not page.evaluate(SNAPSHOT)['playing']
        page.keyboard.press('ArrowRight');snap=page.evaluate(SNAPSHOT)
        assert snap['min']<=snap['time']<=snap['max']
        page.select_option('#scenario',windows[-1]['id'])
        representative=windows[-1]['start']+(windows[-1]['end']-windows[-1]['start'])*.45
        page.eval_on_selector('#scrub','(e,v)=>{e.value=v;e.dispatchEvent(new Event("input"))}',representative)
        page.screenshot(path=str(a.output_dir/(fixture+'-selection.png')),full_page=True)
        page.set_viewport_size({'width':360,'height':1000});page.clock.run_for(200)
        assert page.locator('#fit').is_visible(), (fixture,'narrow unreadability warning missing',page.evaluate('({width:innerWidth,svg:document.querySelector("svg").getBoundingClientRect().width,hidden:document.querySelector("#fit").hidden})'))
        page.screenshot(path=str(a.output_dir/(fixture+'-narrow.png')),full_page=True)
        assert not errors,errors
        assert before==hashlib.sha256(svg_path.read_bytes()).hexdigest()
        reports.append({'fixture':fixture,'all_order':visited,'outcomes':sorted(outcomes),'resets':sorted(resets),
                        'choices':labels,'exclusive_repeat':True,'pause_scrub_static_keyboard':True,'narrow_readability':'alternate layout required'})
        page.close()
    # Real elapsed-time speed sample, separate from virtual full-cycle tests.
    page=browser.new_page();page.set_content((a.examples_dir/'branch.preview.html').read_text())
    page.wait_for_timeout(80);t0=page.evaluate(SNAPSHOT)['time'];wall=time.monotonic()
    page.wait_for_timeout(240);elapsed=time.monotonic()-wall;t1=page.evaluate(SNAPSHOT)['time']
    assert abs((t1-t0)-elapsed)<.12,(t0,t1,elapsed)
    page.click('#play');paused=page.evaluate(SNAPSHOT)
    page.wait_for_timeout(120);assert page.evaluate(SNAPSHOT)['animations']==paused['animations']
    page.click('#play');page.wait_for_timeout(180)
    assert .08<page.evaluate(SNAPSHOT)['time']-paused['time']<.35
    page.close()
    # Ambient stream and idle tick keep their unbounded elapsed clock across scenario resets.
    ambient=a.examples_dir/'ambient.preview.html'
    if not ambient.is_file():raise AssertionError('Missing ambient legacy fixture')
    page=browser.new_page();page.clock.install();page.set_content(ambient.read_text())
    page.clock.run_for(550);first=page.evaluate(SNAPSHOT)
    page.select_option('#scenario','second');second=page.evaluate(SNAPSHOT)
    before_ambient={v['name']:v for v in first['animations'] if v['ambient']}
    after_ambient={v['name']:v for v in second['animations'] if v['ambient']}
    assert before_ambient and set(before_ambient)==set(after_ambient)
    deltas=[]
    for name,before in before_ambient.items():
        after=after_ambient[name]
        assert before['period']==after['period']
        delta=after['time']-before['time']
        assert 0<=delta<200,(before,after)
        deltas.append(delta)
    assert max(deltas)-min(deltas)<2, 'ambient clocks must advance together without reset'
    assert {v['period'] for v in after_ambient.values()}=={1200,2600}
    page.clock.run_for(600);later=page.evaluate(SNAPSHOT)
    for v in later['animations']:
        if v['ambient']:assert 500<v['time']-after_ambient[v['name']]['time']<700
    page.click('#play');frozen=page.evaluate(SNAPSHOT)['animations'];page.clock.run_for(500)
    assert frozen==page.evaluate(SNAPSHOT)['animations'];page.close()
    # Metadata-free preview keeps ordinary controls and no selector.
    page=browser.new_page();page.set_content((a.examples_dir/'plain.preview.html').read_text())
    assert page.locator('#scenario').count()==0 and page.locator('#play').count()==1;page.close()
    # Standalone SVG image genuinely animates without HTML controls; reduced motion stays meaningful.
    svg=(a.examples_dir/'branch.svg').read_bytes()
    source='data:image/svg+xml;base64,'+base64.b64encode(svg).decode()
    images=[]
    for reduce in ('no-preference','reduce'):
        image_browser=browser if reduce=='no-preference' else pw.chromium.launch(
            executable_path='/usr/bin/chromium',args=['--no-sandbox','--force-prefers-reduced-motion=reduce'])
        page=image_browser.new_page(viewport={'width':800,'height':800},reduced_motion=reduce)
        assert page.evaluate('matchMedia("(prefers-reduced-motion: reduce)").matches') == (reduce=='reduce')
        page.set_content('<img alt="Boolean flow" src="'+source+'">')
        page.locator('img').evaluate('e=>e.decode()')
        page.wait_for_timeout(350);first=page.locator('img').screenshot()
        page.wait_for_timeout(650);second=page.locator('img').screenshot()
        if reduce=='no-preference':assert first!=second,'standalone image did not animate'
        else:assert first==second,'reduced-motion image changed'
        (a.output_dir/('standalone-'+reduce+'.png')).write_bytes(second)
        page.close()
        if image_browser is not browser:image_browser.close()
    browser.close()
(a.output_dir/'playback.json').write_text(json.dumps({'fixtures':reports,'real_speed_seconds':elapsed,'ambient_continuity':True,
                                                    'standalone_animation':True,'reduced_motion':True,'reduced_motion_environment':'browser-wide --force-prefers-reduced-motion=reduce; per-page emulation does not propagate to SVG image documents here','network':'isolated namespace, no default route, external socket failed'},indent=2)+'\n')
print(f'PASS: full scenario cycles, exclusive selection, effects/pauses/resets, controls, ambient clocks, standalone image/reduced motion. Artifacts: {a.output_dir}')
