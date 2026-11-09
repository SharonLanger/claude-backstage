#!/usr/bin/env python3
"""Real Chromium layout checks. Run only inside enforced outbound network denial."""
import argparse
import json
from pathlib import Path
import socket
from playwright.sync_api import sync_playwright

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--examples-dir',type=Path,required=True)
p.add_argument('--output-dir',type=Path,required=True)
a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
# Evidence of the OS boundary: require a separate network namespace with no default route.
route=Path('/proc/net/route').read_text().splitlines()[1:]
if any(line.split()[1]=='00000000' for line in route):
    raise SystemExit('Refusing browser: default network route exists; run in isolated network namespace.')
try:
    with socket.create_connection(('1.1.1.1',443),timeout=1):
        raise SystemExit('Refusing browser: external socket succeeded')
except OSError:
    pass
reports=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for path in sorted(a.examples_dir.glob('*.svg')):
        for width in (1000,360):
            page=browser.new_page(viewport={'width':width,'height':1800},reduced_motion='reduce')
            # file:// is blocked by the managed browser; inspect identical local bytes inline.
            page.set_content('<style>body{margin:0}svg{max-width:100%;height:auto}</style>'+path.read_text())
            page.wait_for_timeout(50)
            report=page.evaluate('''() => {
              const svg=document.querySelector('svg'), vb=svg.viewBox.baseVal;
              const texts=[...svg.querySelectorAll('text')].map(e=>{
                const b=e.getBBox(); return {text:e.textContent,x:b.x,y:b.y,w:b.width,h:b.height};
              });
              const nodeFailures=[];
              for(const g of svg.querySelectorAll('[data-node]')){
                const r=g.querySelector('rect'),x=+r.getAttribute('x'),y=+r.getAttribute('y'),w=+r.getAttribute('width'),h=+r.getAttribute('height');
                for(const t of g.querySelectorAll('text')){const b=t.getBBox();
                  if(b.x<x+2||b.y<y+2||b.x+b.width>x+w-2||b.y+b.height>y+h-2)nodeFailures.push(g.dataset.node+': '+t.textContent);
                }
              }
              const clearance=texts.filter(b=>b.w>0 && (b.x<19||b.y<19||b.x+b.w>vb.width-19||b.y+b.h>vb.height-19));
              return {canvas:[vb.width,vb.height],texts:texts.length,nodeFailures,clearance,
                      effectiveFont:parseFloat(getComputedStyle(svg.querySelector('[data-node] text')).fontSize)*svg.getBoundingClientRect().width/vb.width};
            }''')
            report.update(file=path.name,document_width=width)
            # Narrow embeds can be unreadable: report explicitly, never treat shrinking as a pass.
            report['readable']=report['effectiveFont']>=11
            reports.append(report)
            page.screenshot(path=str(a.output_dir/(path.stem+f'-{width}.png')),full_page=True)
            page.close()
    browser.close()
(a.output_dir/'layout.json').write_text(json.dumps(reports,indent=2)+'\n')
assert reports, 'No generated SVG examples'
assert all(not r['nodeFailures'] and not r['clearance'] for r in reports), reports
assert all(r['readable'] for r in reports if r['document_width']==1000), reports
print(f'PASS: {len(reports)} real-browser layouts; narrow-width readability reported separately. Artifacts: {a.output_dir}')
