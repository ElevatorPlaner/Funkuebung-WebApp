from playwright.sync_api import sync_playwright
from common import ROOT, launch
import os
URL = 'file://' + os.path.join(ROOT, 'standalone.html')
res = []
def chk(n, c, extra=''): res.append(bool(c)); print(('OK  ' if c else 'FAIL'), n, extra)
with sync_playwright() as p:
    b = launch(p)
    for n, tr in (('1', "['43']"), ('2', "['43','44']"), ('4', "['33','43','44','65']")):
        pg = b.new_page(viewport={'width': 1366, 'height': 768}); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(URL); pg.evaluate(f"S.trupps={tr}; S.mode='limit'; S.limit=15; saveS()"); pg.reload()
        pg.fill('#team1', 'T'); pg.click('#go'); pg.wait_for_timeout(700)
        chk(n + ' Spiel sichtbar', pg.evaluate("document.querySelector('#game').classList.contains('on')"))
        chk(n + ' Module gesperrt, Uhr steht', pg.evaluate("G.t0===null && document.querySelectorAll('#game .tbox.tlock').length===document.querySelectorAll('#game .tbox').length"))
        pg.click('#fcAll'); pg.wait_for_timeout(800)
        chk(n + ' Uhr laeuft nach Schritt 1', pg.evaluate("G.t0!==null"))
        pg.evaluate("G.mods.forEach(m=>onSolved(m))"); pg.wait_for_timeout(1500)
        chk(n + ' Lage gesichert', pg.evaluate("G.ended===true && G.rec.ok===true"))
        chk(n + ' keine JS-Fehler', not errs, '; '.join(errs)[:200]); pg.close()
    b.close()
raise SystemExit(0 if all(res) else 1)
