import base64, os, subprocess, tempfile
from playwright.sync_api import sync_playwright
from common import APP, launch
out = tempfile.mkdtemp(); bad = []
with sync_playwright() as p:
    b = launch(p); pg = b.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(APP); pg.evaluate("S.tqUrl='https://example.org/fragen.html'; saveS()"); pg.reload()
    for k in range(3):
        r = pg.evaluate(f"""async()=>{{const [bl,name]=PL[{k}].f(); const buf=await bl.arrayBuffer(); let s='';const u=new Uint8Array(buf);for(let i=0;i<u.length;i+=8192)s+=String.fromCharCode.apply(null,u.subarray(i,i+8192));return [name,btoa(s)]}}""")
        f = os.path.join(out, r[0]); open(f, 'wb').write(base64.b64decode(r[1]))
        info = subprocess.run(['pdfinfo', f], capture_output=True, text=True).stdout
        txt = subprocess.run(['pdftotext', f, '-'], capture_output=True, text=True).stdout
        pages = [l for l in info.splitlines() if l.startswith('Pages')]
        dash = ('—' in txt) or ('–' in txt)
        fonts = subprocess.run(['pdffonts', f], capture_output=True, text=True).stdout.strip().splitlines()[2:]
        embedded = all(l.split()[-5] == 'yes' for l in fonts) if fonts else None   # QR-PDF hat keinen Text
        print(r[0], pages, 'Gedankenstrich' if dash else 'ok', len(txt), 'Schriften eingebettet:' if fonts else 'ohne Textschrift', embedded if fonts else '')
        if dash or not pages or embedded is False: bad.append(r[0])
    print(errs); b.close()
raise SystemExit(1 if bad or errs else 0)
