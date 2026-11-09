"""Project-owned semantic layout. Dependency invocation stays in the verified wrapper."""
from __future__ import annotations

import hashlib
import html
import json
import math
import os
from pathlib import Path
import re
import tempfile
import textwrap
import unicodedata
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET


class BuildError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise BuildError(message)


def fields(value, allowed, required, where):
    require(isinstance(value, dict), f"{where}: expected object")
    require(not (set(value) - set(allowed)), f"{where}: unknown fields {sorted(set(value) - set(allowed))}")
    require(set(required) <= set(value), f"{where}: missing fields {sorted(set(required) - set(value))}")


def string(value, where, limit=500):
    require(isinstance(value, str) and 0 < len(value) <= limit, f"{where}: expected nonempty text (max {limit})")
    require(all((ord(c) >= 32 or c == '\n') and not (0xD800 <= ord(c) <= 0xDFFF) and ord(c) not in (0xFFFE, 0xFFFF) for c in value), f"{where}: invalid XML character")
    return value


def identifier(value, where):
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,47}", value), f"{where}: invalid ID")
    return value


def number(value, where, low, high):
    require(type(value) in (int, float) and math.isfinite(value) and low <= value <= high,
            f"{where}: expected finite number in [{low}, {high}]")


def load(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f"duplicate JSON field: {key}")
            result[key] = value
        return result
    try:
        return json.loads(path.read_text(), object_pairs_hook=pairs)
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise BuildError(f"invalid JSON: {exc}") from exc


def validate(spec, defaults):
    fields(spec, ('format', 'defaults_version', 'title', 'claim', 'explanation', 'sources', 'layout',
                  'nodes', 'links', 'scenarios', 'settings', 'side_panel', 'caption'),
           ('format', 'defaults_version', 'title', 'claim', 'explanation', 'sources', 'layout', 'nodes', 'links', 'scenarios'), 'spec')
    require(spec['format'] == 'sl-diagram/v1', 'unsupported format; expected sl-diagram/v1')
    require(spec['defaults_version'] == 'v1', 'unsupported defaults_version; expected v1')
    for key in ('title', 'claim', 'explanation'):
        string(spec[key], key, 3000 if key == 'explanation' else 160)
    string(spec.get('caption', 'Illustrative timing; not measured.'), 'caption', 240)
    require(isinstance(spec['sources'], list) and len(spec['sources']) <= 20, 'sources: expected list (max 20)')
    for source in spec['sources']:
        fields(source, ('label', 'url'), ('label', 'url'), 'source')
        string(source['label'], 'source.label', 160)
        url = string(source['url'], 'source.url', 1000)
        try:
            parsed = urlsplit(url)
            valid_url = parsed.scheme in ('https', 'http') and bool(parsed.hostname) and parsed.port != 0
        except ValueError:
            valid_url = False
        require('\n' not in url and valid_url, 'source.url: expected valid http(s) URL')
    require(spec['layout'] in ('flow', 'branch', 'grid'), 'unsupported layout; use manual template/timeline for other layouts')
    settings = dict(defaults['settings'])
    overrides = spec.get('settings', {})
    fields(overrides, settings, (), 'settings')
    ranges = {'outer_margin': (20, 100), 'panel_gutter': (20, 100), 'panel_width': (140, 400),
              'node_width': (100, 320), 'node_height': (48, 240), 'gap': (40, 160), 'font_size': (12, 24),
              'document_width': (320, 2000), 'travel': (.1, 10), 'pause': (.5, 10), 'reset': (.2, 5),
              'setup': (.1, 5), 'effect_tail': (.5, 3)}
    for key, value in overrides.items():
        number(value, 'settings.' + key, *ranges[key])
        settings[key] = value
    require(isinstance(spec['nodes'], list) and 1 <= len(spec['nodes']) <= 20, 'nodes: expected 1..20 items')
    nodes = {}
    for node in spec['nodes']:
        fields(node, ('id', 'label', 'tag'), ('id', 'label'), 'node')
        nid = identifier(node['id'], 'node.id')
        require(nid not in nodes, f'duplicate node ID: {nid}')
        string(node['label'], f'node {nid}.label', 240)
        if 'tag' in node:
            string(node['tag'], f'node {nid}.tag', 120)
        nodes[nid] = node
    require(isinstance(spec['links'], list) and len(spec['links']) <= 30, 'links: expected list (max 30)')
    links = {}
    incoming = {nid: [] for nid in nodes}
    outgoing = {nid: [] for nid in nodes}
    for link in spec['links']:
        fields(link, ('id', 'from', 'to'), ('id', 'from', 'to'), 'link')
        lid = identifier(link['id'], 'link.id')
        require(lid not in links and lid not in nodes, f'duplicate link ID: {lid}')
        require(isinstance(link['from'], str) and isinstance(link['to'], str) and link['from'] in nodes and link['to'] in nodes,
                f'link {lid}: missing node reference')
        require(link['from'] != link['to'], f'link {lid}: self links unsupported')
        links[lid] = link
        incoming[link['to']].append(link['from'])
        outgoing[link['from']].append(link['to'])
    require(len({(l['from'], l['to']) for l in links.values()}) == len(links), 'duplicate connection')
    roots = [nid for nid in nodes if not incoming[nid]]
    if spec['layout'] == 'grid':
        require(not links, 'grid requires independent nodes without links; use manual route for unsupported topology')
    else:
        require(len(roots) == 1 and len(links) == len(nodes) - 1 and all(len(v) <= 1 for v in incoming.values()),
                'flow/branch requires a rooted tree without merges or cycles; use manual route')
        seen = set()
        def visit(nid):
            require(nid not in seen, 'cycle in topology')
            seen.add(nid)
            for child in outgoing[nid]:
                visit(child)
        visit(roots[0])
        require(len(seen) == len(nodes), 'disconnected topology; use manual route')
        if spec['layout'] == 'flow':
            require(all(len(v) <= 1 for v in outgoing.values()), 'flow requires a single ordered chain; use branch or manual route')
    panel = spec.get('side_panel', [])
    require(isinstance(panel, list) and len(panel) <= 12, 'side_panel: expected list (max 12)')
    for item in panel:
        string(item, 'side_panel item', 240)
    require(isinstance(spec['scenarios'], list) and 1 <= len(spec['scenarios']) <= 8, 'scenarios: expected 1..8 items')
    ids = set()
    step_count = 0
    def step(value, nested=False):
        nonlocal step_count
        fields(value, ('node', 'link', 'parallel'), (), 'step')
        require(len(value) == 1, 'step: choose exactly one of node, link, parallel')
        if 'parallel' in value:
            group = value['parallel']
            require(not nested and isinstance(group, list) and 2 <= len(group) <= 8, 'parallel: expected 2..8 simple steps, no nesting')
            for item in group:
                step(item, True)
            require(len({json.dumps(item, sort_keys=True) for item in group}) == len(group), 'parallel: duplicate step')
        else:
            key = next(iter(value))
            require(isinstance(value[key], str) and value[key] in (nodes if key == 'node' else links), f'step: missing {key} reference')
            step_count += 1
    for scenario in spec['scenarios']:
        fields(scenario, ('id', 'label', 'steps', 'outcome'), ('id', 'label', 'steps', 'outcome'), 'scenario')
        sid = identifier(scenario['id'], 'scenario.id')
        require(sid not in ids, f'duplicate scenario ID: {sid}')
        ids.add(sid)
        string(scenario['label'], 'scenario.label', 160)
        string(scenario['outcome'], 'scenario.outcome', 240)
        require(isinstance(scenario['steps'], list) and 1 <= len(scenario['steps']) <= 30, 'scenario.steps: expected 1..30 steps')
        for value in scenario['steps']:
            step(value)
    require(step_count <= 120, 'too many steps (max 120); split diagram')
    return settings, nodes, links, roots, outgoing


def lines(text, width, font, where):
    # Monospace glyph width with extra clearance. Unsupported long words split safely.
    count = math.floor(width / (font * .7))
    require(count >= 4, f'{where}: region too narrow; increase width')
    result = []
    for paragraph in text.split('\n'):
        if paragraph.isascii():
            result.extend(textwrap.wrap(paragraph, count, break_long_words=True, break_on_hyphens=False) or [''])
            continue
        remaining = paragraph.strip()
        while remaining:
            units, cut = 0, 0
            for char in remaining:
                cost = 2 if unicodedata.east_asian_width(char) in ('W', 'F') else 1
                if units + cost > count:
                    break
                units += cost
                cut += 1
            require(cut > 0, f'{where}: cannot wrap label')
            if cut < len(remaining) and ' ' in remaining[:cut]:
                cut = remaining.rfind(' ', 0, cut)
            result.append(remaining[:cut].rstrip())
            remaining = remaining[cut:].lstrip()
        if not paragraph.strip():
            result.append('')
    return result


def normalize(spec, defaults):
    s, nodes, links, roots, outgoing = validate(spec, defaults)
    f, margin, gap = s['font_size'], s['outer_margin'], s['gap']
    nw, nh = s['node_width'], s['node_height']
    heights, wrapped = {}, {}
    for nid, node in nodes.items():
        label = lines(node['label'], nw - 24, f, nid)
        tag = lines(node.get('tag', ''), nw - 24, f, nid)
        wrapped[nid] = (label, tag if 'tag' in node else [])
        heights[nid] = max(nh, (len(label) + (len(tag) + 1 if 'tag' in node else 0)) * f * 1.4 + 24)
    row_height = max(heights.values())
    positions = {}
    if spec['layout'] == 'grid':
        cols = min(3, len(nodes))
        for i, nid in enumerate(nodes):
            positions[nid] = (i % cols, i // cols)
    else:
        leaf_index = 0
        def place(nid, depth):
            nonlocal leaf_index
            if outgoing[nid]:
                xs = [place(child, depth + 1) for child in outgoing[nid]]
                x = (xs[0] + xs[-1]) / 2
            else:
                x = leaf_index
                leaf_index += 1
            positions[nid] = (x, depth)
            return x
        place(roots[0], 0)
        cols = leaf_index
    flow_width = cols * nw + (cols - 1) * gap
    panel_width = s['panel_width'] if spec.get('side_panel') else 0
    width = 2 * margin + flow_width + (s['panel_gutter'] + panel_width if panel_width else 0)
    require(f * min(1, s['document_width'] / width) >= 11,
            f'layout unreadable at document_width={s["document_width"]}; reduce columns/labels or use manual alternate layout')
    title = lines(spec['title'], width - 2 * margin, f + 4, 'title')
    claim = lines(spec['claim'], width - 2 * margin, f, 'claim')
    header_height = len(title) * (f + 4) * 1.4 + len(claim) * f * 1.4 + 24
    top = margin + header_height
    boxes = {nid: [margin + col * (nw + gap), top + row * (row_height + gap), nw, heights[nid]]
             for nid, (col, row) in positions.items()}
    flow_bottom = max(y + h for x, y, w, h in boxes.values())
    panel_lines = []
    for item in spec.get('side_panel', []):
        panel_lines.extend(lines(item, panel_width - 24, f, 'side_panel') + [''])
    panel_bottom = top + len(panel_lines) * f * 1.4 + 24 if panel_lines else top
    content_bottom = max(flow_bottom, panel_bottom)
    footer_width = width - 2 * margin
    caption = lines(spec.get('caption', 'Illustrative timing; not measured.'), footer_width, f, 'caption')
    scenario_height = max(len(lines(sc['label'], footer_width, f, 'scenario label')) +
                          len(lines(sc['outcome'], footer_width, f, 'scenario outcome')) for sc in spec['scenarios']) * f * 1.4
    footer_top = content_bottom + gap
    height = footer_top + scenario_height + 24 + len(caption) * f * 1.4 + margin
    routes = {}
    for lid, link in links.items():
        x, y, w, h = boxes[link['from']]
        tx, ty, tw, th = boxes[link['to']]
        start, end = [x + w / 2, y + h], [tx + tw / 2, ty]
        mid = (start[1] + end[1]) / 2
        routes[lid] = [start, [start[0], mid], [end[0], mid], end]
    # Normalized windows are the sole timing authority, ready for optional preview.
    events, scenarios = [], []
    clock = 0.0
    for i, scenario in enumerate(spec['scenarios']):
        start = clock
        clock += s['setup']
        serial = 0
        for step in scenario['steps']:
            group = step.get('parallel', [step])
            for item in group:
                serial += 1
                ev = {'id': f's{i}_e{serial}', 'at': round(clock, 6)}
                if 'link' in item:
                    route = routes[item['link']]
                    dest = links[item['link']]['to']
                    x, y, w, h = boxes[dest]
                    ev.update(kind='packet', travel=s['travel'], **{'from': route[0], 'via': route[1:-1], 'to': route[-1]},
                              ring=False, glow={'x': x, 'y': y, 'w': w, 'h': h})
                else:
                    x, y, w, h = boxes[item['node']]
                    ev.update(kind='pulse', x=x + w / 2, y=y + h / 2, dur=s['travel'], ring_r=min(w, h)/3)
                events.append(ev)
            clock += s['travel'] + s['effect_tail']
        outcome_start = clock
        clock += s['pause']
        end = clock + s['reset']
        # Captions are individually wrapped, with separate label and outcome regions.
        y = footer_top + f
        for j, line in enumerate(lines(scenario['label'], footer_width, f, 'scenario label')):
            events.append({'id': f's{i}_label{j}', 'kind': 'phase', 'at': start, 'until': clock, 'text': line,
                           'x': margin, 'y': y, 'anchor': 'start', 'class': 'semantic-caption'})
            y += f * 1.4
        for j, line in enumerate(lines(scenario['outcome'], footer_width, f, 'outcome')):
            events.append({'id': f's{i}_outcome{j}', 'kind': 'phase', 'at': outcome_start, 'until': clock,
                           'text': line, 'x': margin, 'y': y, 'anchor': 'start', 'class': 'semantic-caption'})
            y += f * 1.4
        scenarios.append({'id': scenario['id'], 'label': scenario['label'], 'start': round(start, 6), 'end': round(end, 6)})
        clock = end
    motion = {'loop': round(clock, 6), 'accent': defaults['colors']['accent'],
              'glow_dur': s['effect_tail'], 'events': events}
    return {'settings': s, 'width': math.ceil(width / 4) * 4, 'height': math.ceil(height / 4) * 4, 'boxes': boxes, 'routes': routes,
            'wrapped': wrapped, 'title': title, 'claim': claim, 'top': top, 'flow_width': flow_width,
            'panel_lines': panel_lines, 'caption': caption,
            'caption_y': footer_top + scenario_height + 24, 'motion': motion, 'scenarios': scenarios}


def static_svg(spec, n, defaults, template):
    s, colors = n['settings'], defaults['colors']
    f, margin = s['font_size'], s['outer_margin']
    esc = lambda value: html.escape(str(value), quote=True)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{n["width"]}" height="{n["height"]}" '
             f'viewBox="0 0 {n["width"]} {n["height"]}" role="img" aria-label="{esc(spec["claim"])}">']
    # Retain upstream animation classes and reduced motion behavior verbatim.
    style = template[template.index('<style>'):template.index('</style>') + len('</style>')]
    style = style.replace('</style>', '')
    parts += [style, f'text {{font-family:monospace;font-size:{f}px;fill:{colors["text"]}}} .semantic-caption {{font-size:{f}px}}</style>',
              f'<rect width="100%" height="100%" fill="{colors["background"]}"/>',
              f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{colors["route"]}"/></marker></defs>']
    def text(values, x, y, size=f, fill=None):
        for line in values:
            parts.append(f'<text x="{x}" y="{y}" style="font-size:{size}px;fill:{fill or colors["text"]}">{esc(line)}</text>')
            y += size * 1.4
        return y
    y = text(n['title'], margin, margin + f + 4, f + 4)
    text(n['claim'], margin, y + 4)
    for lid, points in n['routes'].items():
        value = ' '.join(f'{x},{y}' for x, y in points)
        parts.append(f'<polyline data-link="{esc(lid)}" points="{value}" stroke="{colors["route"]}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
    for nid, (x, y, w, h) in n['boxes'].items():
        parts.append(f'<g data-node="{esc(nid)}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{colors["node"]}" stroke="{colors["route"]}"/>')
        label, tag = n['wrapped'][nid]
        next_y = text(label, x + 12, y + 12 + f)
        if tag:
            text(tag, x + 12, next_y + f * .7, fill=colors['accent'])
        parts.append('</g>')
    if n['panel_lines']:
        x = margin + n['flow_width'] + s['panel_gutter']
        text(n['panel_lines'], x + 12, n['top'] + 12 + f)
    text(n['caption'], margin, n['caption_y'] + f, fill=colors['muted'])
    parts += ['<!-- @motion:elements -->', '<!-- @/motion:elements -->', '</svg>']
    return '\n'.join(parts) + '\n'


MARKER = '<!-- sl-diagram/v1 generated; edit semantic spec and rebuild. -->'
COMPANION_MARKER = '<!-- sl-diagram/v1 generated companion; edit semantic spec and rebuild. -->'


def companion(spec, spec_path, out):
    def literal(value):
        # Markdown prose stays literal, including code fences and link syntax.
        return html.escape(value).replace('\\', '&#92;').replace('`', '&#96;').replace('[', '&#91;').replace(']', '&#93;').replace('*', '&#42;').replace('_', '&#95;').replace('#', '&#35;')
    def describe(step):
        if 'parallel' in step:
            return 'Together: ' + '; '.join(describe(item) for item in step['parallel'])
        if 'node' in step:
            node = next(n for n in spec['nodes'] if n['id'] == step['node'])
            return literal(node['label'])
        link = next(l for l in spec['links'] if l['id'] == step['link'])
        nodes = {n['id']: n['label'] for n in spec['nodes']}
        return literal(nodes[link['from']]) + ' → ' + literal(nodes[link['to']])
    parts = [COMPANION_MARKER, '# ' + literal(spec['title']), literal(spec['claim']), literal(spec['explanation']),
             'Generated from the semantic spec; timings are illustrative unless explained otherwise.']
    for scenario in spec['scenarios']:
        parts += ['## ' + literal(scenario['label'])]
        parts += [f'{i}. {describe(step)}' for i, step in enumerate(scenario['steps'], 1)]
        parts += ['Outcome: ' + literal(scenario['outcome'])]
    if spec['sources']:
        parts += ['## Sources'] + [literal(source['label']) + ': <' + html.escape(source['url'], quote=True).replace('>', '%3E').replace('<', '%3C') + '>' for source in spec['sources']]
    from urllib.parse import quote
    relative = Path(os.path.relpath(spec_path, out.parent)).as_posix()
    parts += ['[Editable semantic spec](' + quote(relative, safe='/') + ')']
    return '\n\n'.join(parts) + '\n'


def build(spec_path, out, defaults_path, data, execute, debug=None):
    require(out.suffix == '.svg', '--out must end in .svg')
    require(out.resolve() != spec_path.resolve(), 'output must not replace input')
    agent = out.with_suffix('.agent.md')
    for path, marker in ((out, MARKER), (agent, COMPANION_MARKER)):
        require(not path.is_symlink(), f'refusing linked output: {path}')
        require(not path.exists() or marker in path.read_text()[:300], f'refusing to overwrite manual file: {path}')
    spec = load(spec_path)
    defaults = load(defaults_path)
    n = normalize(spec, defaults)
    static = static_svg(spec, n, defaults, data['assets/template.svg'].decode())
    ET.fromstring(static)
    # Compilation and structural validation complete before publishing any output.
    with tempfile.TemporaryDirectory(prefix='sl-semantic-') as tmp:
        work = Path(tmp)
        motion, svg = work / 'motion.json', work / 'diagram.svg'
        motion.write_text(json.dumps(n['motion'], ensure_ascii=False))
        svg.write_text(static)
        require(execute(data, 'timeline', [str(motion), '--inject', str(svg)]) == 0, 'verified motion compiler failed')
        require(execute(data, 'check', [str(svg)]) == 0, 'verified structural checker failed')
        compiled = svg.read_text()
        ET.fromstring(compiled)
    digest = hashlib.sha256(json.dumps(spec, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    payloads = {out: MARKER + '\n<!-- semantic-sha256: ' + digest + ' -->\n' + compiled,
                agent: companion(spec, spec_path.resolve(), out.resolve())}
    if debug is not None:
        require(debug.resolve() not in {out.resolve(), agent.resolve(), spec_path.resolve()}, 'debug path conflicts with primary asset')
        require(not debug.exists(), 'debug output already exists')
        payloads[debug] = json.dumps(n, sort_keys=True, indent=2, ensure_ascii=False) + '\n'
    # Stage all writes in their destination directories before replacing files.
    staged = []
    try:
        for path, text in payloads.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, tmp = tempfile.mkstemp(prefix='.sl-build-', dir=path.parent)
            staged.append((Path(tmp), path))
            with os.fdopen(fd, 'w') as stream:
                stream.write(text)
        for tmp, path in staged:
            os.replace(tmp, path)
    finally:
        for tmp, _ in staged:
            tmp.unlink(missing_ok=True)
    print(f'Built: {out}\nCompanion: {agent}\nSpec: {spec_path}\nLayout: {spec["layout"]}; {len(spec["nodes"])} nodes; {len(spec["scenarios"])} scenarios. Structural check passed; visual verification separate.')
    return 0
