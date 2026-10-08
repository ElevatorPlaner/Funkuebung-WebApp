import re, os, subprocess
from common import ROOT
bad = []
for f in ('funkuebung.html', 'fragen.html'):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    for ch, name in (('—', 'Geviertstrich'), ('–', 'Halbgeviertstrich')):
        if ch in s: bad.append(f'{f}: {name} x{s.count(ch)}')
    html = re.sub(r'<script>.*?</script>', '', s, flags=re.S)
    ids = re.findall(r'\bid="([^"]+)"', html)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup: bad.append(f'{f}: doppelte IDs {dup}')
    js = re.findall(r'<script>(.*?)</script>', s, re.S)[-1]
    open('/tmp/_chk.js', 'w', encoding='utf-8').write(js)
    r = subprocess.run(['node', '--check', '/tmp/_chk.js'], capture_output=True, text=True)
    if r.returncode: bad.append(f'{f}: Syntaxfehler {r.stderr[:200]}')
print('Probleme:', bad or 'keine'); raise SystemExit(1 if bad else 0)
