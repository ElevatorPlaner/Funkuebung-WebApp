from playwright.sync_api import sync_playwright
from common import FRAGEN, launch
with sync_playwright() as p:
    b = launch(p); pg = b.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(FRAGEN + '?s=1&k=test'); pg.wait_for_timeout(500)
    r = pg.evaluate("""()=>{const o={};for(const run of ['a','b','c']){for(const e of ['43','44']){const all=[1,2,4].map(s=>fragenFuer(run,e,s));const flat=all.flat();o[run+e]=[all.map(x=>x.join('/')).join(' | '), new Set(flat).size===6];}}return o}""")
    bad = [k for k, v in r.items() if not v[1]]
    for k, v in r.items(): print(k, v)
    print('errors', errs, 'bad', bad); b.close()
    raise SystemExit(1 if errs or bad else 0)
