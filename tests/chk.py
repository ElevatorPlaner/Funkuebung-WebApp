import re, os
from common import ROOT
def fr(f):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    m = 'const POOL = [' if 'const POOL = [' in s else 'fragen: ['
    i = s.index(m); j = s.index('\n  ]' if m == 'fragen: [' else '\n];', i)
    return re.sub(r'\s+', ' ', s[i + len(m):j])
a, b, c = fr('funkuebung.html'), fr('fragen.html'), fr('uebungsleiter.html')
ids = re.findall(r'id: (\d+), titel', a)
print(ids, a.count('ok:'), b.count('ok:'))
g = lambda s: re.findall(r"titel: '([^']*)'.*?lage: '([^']*)'.*?opt: (\[.*?\]), ok: (\d)", s)
same = g(a) == g(b) == g(c)
print('Fragenpool identisch:', same)
raise SystemExit(0 if same else 1)
