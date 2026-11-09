"""Project-owned offline scenario preview; upstream plain preview remains available.

The controls are adapted from animdiagram preview.py (MIT), pinned at the audited
commit. Full copyright/permission notice: ../notices/animdiagram-MIT.txt
(relative to this script directory). Timing/range validation and independent clocks are Claude Backstage code.
"""
from __future__ import annotations

import hashlib
import html
import json
import math
import os
import tempfile
from pathlib import Path
import re
import xml.etree.ElementTree as ET


class PreviewError(ValueError):
    pass


def require(value, message):
    if not value:
        raise PreviewError(message)


def canonical_hash(spec):
    return hashlib.sha256(json.dumps(spec, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f'duplicate metadata/spec key: {key}')
            result[key] = value
        return result
    try:
        return json.loads(path.read_text(), object_pairs_hook=pairs)
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise PreviewError(f'invalid spec JSON: {exc}') from exc


def ranges(loop, scenarios):
    require(type(loop) in (int, float) and math.isfinite(loop) and 0 < loop <= 10000, 'loop must be finite and positive (max 10000s)')
    require(isinstance(scenarios, list) and 1 <= len(scenarios) <= 100, 'scenarios must contain 1..100 ranges')
    ids, previous = set(), 0
    for scenario in scenarios:
        require(isinstance(scenario, dict) and set(scenario) == {'id', 'label', 'start', 'end'}, 'scenario metadata requires exactly id, label, start, end')
        sid, label = scenario['id'], scenario['label']
        require(isinstance(sid, str) and re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{0,47}', sid) and sid not in ids, 'scenario ID invalid or duplicated')
        require(isinstance(label, str) and 0 < len(label) <= 500, 'scenario label must be nonempty text (max 500)')
        start, end = scenario['start'], scenario['end']
        require(all(type(v) in (int,float) and math.isfinite(v) for v in (start,end)), 'scenario boundaries must be finite numbers')
        require(previous <= start < end <= loop, 'scenario ranges must be ordered, non-overlapping and within loop')
        ids.add(sid)
        previous = end
    return {'version':'sl-preview/v1', 'loop':loop, 'scenarios':scenarios}


def stamp(svg, metadata):
    """Embed inert metadata and a digest of the complete SVG bytes before digest line."""
    payload = html.escape(json.dumps(metadata, sort_keys=True, ensure_ascii=False), quote=False)
    svg = svg.replace('</svg>', f'<metadata id="sl-scenarios">{payload}</metadata>\n</svg>', 1)
    return svg + '<!-- sl-svg-sha256: ' + hashlib.sha256(svg.encode()).hexdigest() + ' -->\n'


def metadata(svg, svg_path, spec_path=None):
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as exc:
        raise PreviewError(f'invalid SVG XML: {exc}') from exc
    entries = [e for e in root.iter() if e.get('id') == 'sl-scenarios']
    require(len(entries) <= 1, 'duplicate scenario metadata')
    spec = read_json(spec_path) if spec_path else None
    if entries:
        match = re.search(r'<!-- sl-svg-sha256: ([0-9a-f]{64}) -->\n?$', svg)
        require(match and hashlib.sha256(svg[:match.start()].encode()).hexdigest() == match.group(1), 'SVG content mismatch; rebuild SVG and preview together')
        try:
            meta = json.loads(entries[0].text or '')
        except json.JSONDecodeError as exc:
            raise PreviewError('invalid embedded scenario metadata') from exc
        require(isinstance(meta, dict) and set(meta) == {'version','loop','scenarios','spec_sha256','spec_path'}, 'invalid generated scenario metadata fields')
        require(meta['version']=='sl-preview/v1', 'unsupported preview metadata version')
        require(isinstance(meta['spec_path'], str) and isinstance(meta['spec_sha256'], str), 'invalid spec provenance')
        if spec is None:
            spec = read_json(svg_path.parent / meta['spec_path'])
        require(isinstance(spec, dict) and spec.get('format') == 'sl-diagram/v1' and canonical_hash(spec)==meta['spec_sha256'], 'semantic spec mismatch; rebuild SVG and preview together')
        return ranges(meta['loop'], meta['scenarios'])
    if spec is None:
        return None
    require(isinstance(spec, dict), 'spec must be an object')
    if 'sl' not in spec:
        return None
    sl = spec['sl']
    require(isinstance(sl, dict) and set(sl) == {'scenarios','svg_sha256'}, 'legacy sl metadata requires scenarios and svg_sha256')
    require(sl['svg_sha256'] == hashlib.sha256(svg.encode()).hexdigest(), 'legacy SVG/spec mismatch; recompile and update sl.svg_sha256')
    result = ranges(spec.get('loop'), sl['scenarios'])
    clock = re.search(r'\.story,\s*\.pkt,\s*\.ring,\s*\.glow,\s*\.bar\s*\{\s*animation-duration:\s*([0-9.]+)s', svg)
    require(clock and math.isclose(float(clock.group(1)), result['loop'], abs_tol=.000001), 'legacy loop does not match compiled SVG story clock')
    return result


def validate_visibility(css):
    """Reject actual emitted duplicate opacity offsets with conflicting values.

    Pinned CSS combines duplicate offsets using the later value; a rounded-away
    zero-opacity boundary can otherwise reveal a later event in an earlier window.
    """
    names = set()
    for match in re.finditer(r'@keyframes\s+([\w-]+)\s*\{((?:[^{}]|\{[^{}]*\})*)\}', css):
        name, body = match.groups()
        require(name not in names, f'duplicate animation name: {name}; use --plain or rename effects')
        names.add(name)
        stops = {}
        for selectors, declarations in re.findall(r'([^{}]+)\{([^{}]*)\}', body):
            opacity = re.search(r'opacity\s*:\s*([0-9.]+)', declarations)
            if not opacity:
                continue
            value = float(opacity.group(1))
            for offset in re.findall(r'([0-9.]+)%', selectors):
                point = float(offset)
                require(point not in stops or stops[point] == value,
                        f'compiler collapses visibility offsets for {name}; shorten loop or lengthen effect, or use --plain')
                stops[point] = value


def validate_legacy_effects(report, meta):
    require(report['matches'], 'legacy motion spec mismatch; recompile SVG before preview')
    table = {row[0]:row for row in report['table']}
    cfg, loop = report['settings'], report['loop']
    require(math.isclose(loop, meta['loop'], abs_tol=.000001) and math.isclose(loop, report['rendered_loop'], abs_tol=1e-8), 'legacy loop is not representable at compiler centisecond precision; use --plain or adjust loop')
    for event in report['events']:
        kind = event.get('kind', 'packet')
        if kind == 'stream':
            continue  # Truly ambient: keeps its independent clock across selections.
        require(kind in ('packet','pulse','phase','show'),
                f'legacy scenario selection does not support {kind}; use --plain or semantic generation')
        start, end = map(float, table[event['id']][2:4])
        require(math.isfinite(start) and math.isfinite(end), 'legacy event times must be finite')
        if kind == 'packet':
            tail = max(float(cfg['fade']), float(cfg['ring_dur']) if event.get('ring', True) else 0,
                       float(cfg['glow_dur']) if event.get('glow') else 0)
            end += tail
        elif kind in ('phase','show'):
            edge = float(event.get('edge',cfg['hold']))
            require(math.isfinite(edge) and edge / loop * 100 >= .02, 'legacy phase/show edge must be positive and exceed compiler percentage precision; use --plain or a longer edge')
            start = max(0, start - edge)
            end += edge
        elif kind == 'pulse':
            end = start + float(event.get('dur',cfg['ring_dur']))
        # Validate the emitted two-decimal percentage offsets, including rounding.
        rounded_start = float(f'{max(0,min(100,start / loop * 100)):.2f}') / 100 * loop
        rounded_end = float(f'{max(0,min(100,end / loop * 100)):.2f}') / 100 * loop
        require(end <= loop and any(s['start'] <= min(start,rounded_start) + 1e-8 and max(end,rounded_end) <= s['end'] + 1e-8 for s in meta['scenarios']),
                f'legacy scenario boundary cuts event/effect tail {event["id"]}; include the complete event and reset')


PAGE = '''<!-- sl-diagram/v1 generated preview -->
<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>preview · __NAME__</title>
<style>
:root{color-scheme:dark}body{margin:0;font:14px/1.4 system-ui,sans-serif;background:#0a0a0b;color:#b6c0cf}
body.light{background:#f5f5f5;color:#2d3142}header{display:flex;gap:12px;align-items:center;padding:12px 16px;flex-wrap:wrap;border-bottom:1px solid #666}
button,select,input{font:inherit}button,select{padding:4px 10px;border:1px solid #888;border-radius:6px;background:transparent;color:inherit}
select option{background:#202126;color:#f4f6fc}button[aria-pressed=true]{border-color:#4cf490}input[type=range]{width:260px}#t{min-width:110px}
main{display:grid;grid-template-columns:minmax(0,1fr);place-items:start center;padding:32px 16px;overflow:auto}#wrap{transform-origin:top center;max-width:100%;min-width:0}#wrap svg{display:block;max-width:100%;height:auto}
.hint{font-size:12px}#fit{padding:0 16px;color:#fbdc8e}
</style>
<header><b>__NAME__</b>
<label id="scenario-control">Scenario <select id="scenario" aria-label="Scenario"><option value="@all">All</option></select></label>
<button id="play" aria-pressed="true">pause</button><button id="static">static frame</button>
<label>Time <input id="scrub" type="range" min="0" max="1" step="0.001" value="0"></label><span id="t">0.00 s</span>
<button id="bg">light bg</button><button id="zoom">2×</button><span class="hint">space = play/pause · ←/→ = ±0.1 s · shift = ±1 s</span>
</header><p id="fit" role="status" hidden>Labels are too small at this width. Use a narrower alternate layout.</p>
<main><div id="wrap">__SVG__</div></main>
<script type="application/json" id="sl-preview-data">__DATA__</script>
<script>
'use strict';
(() => {
  const metadata=JSON.parse(document.getElementById('sl-preview-data').textContent);
  const wrap=document.getElementById('wrap'), play=document.getElementById('play'), scrub=document.getElementById('scrub');
  const select=document.getElementById('scenario'), tOut=document.getElementById('t');
  const loop=metadata.loop*1000;
  for(const s of metadata.scenarios){const o=document.createElement('option');o.value=s.id;o.textContent=s.label;select.append(o)}
  document.getElementById('scenario-control').hidden=metadata.scenarios.length<2;
  // Story classes use the authored loop. Ambient .pkt streams have their own explicit duration;
  // ticks and other independent animations use an unbounded elapsed clock.
  const animations=wrap.getAnimations({subtree:true});
  const story=[], ambient=[];
  for(const a of animations){
    const target=a.effect.target;
    const isStory=target.matches('.story,.pkt,.ring,.glow,.bar') && !target.style.animationDuration;
    (isStory?story:ambient).push(a);a.pause();
  }
  let start=0,end=loop,time=0,elapsed=0,playing=true,last=null;
  function draw(){
    for(const a of story)a.currentTime=time;
    for(const a of ambient)a.currentTime=elapsed;
    scrub.value=(time/1000).toFixed(3);
    tOut.textContent=(time/1000).toFixed(2)+' s';
  }
  function setPlaying(p){playing=p;last=null;play.setAttribute('aria-pressed',String(p));play.textContent=p?'pause':'play'}
  function seek(ms){time=Math.max(start,Math.min(end-.001,ms));draw()}
  function frame(now){
    if(playing&&last!==null){const delta=now-last;elapsed+=delta;time=start+((time-start+delta)%(end-start));draw()}
    last=now;requestAnimationFrame(frame);
  }
  select.addEventListener('change',()=>{
    const s=metadata.scenarios.find(s=>s.id===select.value);
    start=s?s.start*1000:0;end=s?s.end*1000:loop;
    scrub.min=String(start/1000);scrub.max=String((end-.001)/1000);last=null;seek(start);
  });
  play.onclick=()=>setPlaying(!playing);
  scrub.oninput=()=>{setPlaying(false);seek(Number(scrub.value)*1000)};
  document.getElementById('static').onclick=()=>{setPlaying(false);seek(end-1)};
  document.getElementById('bg').onclick=e=>{document.body.classList.toggle('light');e.target.textContent=document.body.classList.contains('light')?'dark bg':'light bg'};
  document.getElementById('zoom').onclick=e=>{const z=wrap.style.transform==='scale(2)'?'':'scale(2)';wrap.style.transform=z;e.target.textContent=z?'1×':'2×'};
  document.addEventListener('keydown',e=>{
    if(e.target.closest('input,select,button,textarea,[contenteditable]'))return;
    if(e.code==='Space'){e.preventDefault();setPlaying(!playing)}
    if(e.code==='ArrowRight'||e.code==='ArrowLeft'){
      e.preventDefault();setPlaying(false);const delta=(e.shiftKey?1000:100)*(e.code==='ArrowRight'?1:-1);
      seek(start+((time-start+delta+end-start)%(end-start)));
    }
  });
  function fit(){
    const svg=wrap.querySelector('svg'),text=svg.querySelector('[data-node] text')||svg.querySelector('text');
    if(text){const effective=parseFloat(getComputedStyle(text).fontSize)*svg.getBoundingClientRect().width/svg.viewBox.baseVal.width;
      document.getElementById('fit').hidden=effective>=11}
  }
  addEventListener('resize',fit);new ResizeObserver(fit).observe(wrap);scrub.max=String((loop-.001)/1000);draw();fit();requestAnimationFrame(frame);
})();
</script>
'''


def page(svg, name, meta):
    serialized = json.dumps(meta, ensure_ascii=True).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    # Single substitution pass prevents user text from becoming another placeholder.
    values = {'__NAME__':html.escape(name), '__SVG__':svg, '__DATA__':serialized}
    return re.sub('|'.join(values), lambda match: values[match.group()], PAGE)


def aliases(first, second):
    return first.resolve() == second.resolve() or (first.exists() and second.exists() and first.samefile(second))


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.sl-preview-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            stream.write(text)
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def converted(source, changed, source_path, out):
    """Retain validated semantic provenance/ranges after the verified palette conversion."""
    metadata(source, source_path)  # Reject stale bytes/spec before accepting conversion.
    original = next(e for e in ET.fromstring(source).iter() if e.get('id') == 'sl-scenarios')
    raw = json.loads(original.text)
    spec = (source_path.parent / raw['spec_path']).resolve()
    raw['spec_path'] = Path(os.path.relpath(spec, out.resolve().parent)).as_posix()
    require(not out.is_symlink() and not aliases(out, spec), 'skin output conflicts with semantic spec')
    require(not out.exists() or '<!-- sl-diagram/v1 generated;' in out.read_text()[:300], 'refusing to overwrite manual skin output')
    changed = re.sub(r'<metadata id="sl-scenarios">.*?</metadata>\s*', '', changed, flags=re.S)
    changed = re.sub(r'<!-- sl-svg-sha256: [0-9a-f]{64} -->\n?$', '', changed)
    return stamp(changed, raw)


def render(svg_path, out=None, spec_path=None, inspect_motion=None):
    svg = svg_path.read_text()
    meta = metadata(svg, svg_path, spec_path)
    if meta is None:
        return None
    if spec_path and not any(e.get('id') == 'sl-scenarios' for e in ET.fromstring(svg).iter()):
        require(inspect_motion is not None, 'verified legacy compiler inspection required')
        try:
            report = inspect_motion(spec_path, svg)
        except ValueError as exc:
            raise PreviewError(str(exc)) from exc
        validate_legacy_effects(report, meta)
        validate_visibility('\n'.join(e.text or '' for e in ET.fromstring(svg).iter() if e.tag.endswith('}style')))
    out = out or svg_path.with_suffix('.preview.html')
    protected = [svg_path]
    if spec_path:
        protected.append(spec_path)
    for entry in ET.fromstring(svg).iter():
        if entry.get('id') == 'sl-scenarios':
            protected.append(svg_path.parent / json.loads(entry.text)['spec_path'])
    require(not out.is_symlink() and all(not aliases(out, path) for path in protected), 'preview output conflicts with input')
    atomic_write(out, page(svg,svg_path.name,meta))
    print(out)
    return 0
