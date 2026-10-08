import re, os
from common import ROOT
def fr(f):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    i = s.index('fragen: ['); j = s.index('\n  ]', i)
    return re.sub(r'\s+', ' ', s[i:j])
a, b = fr('funkuebung.html'), fr('fragen.html')
ids = re.findall(r'id: (\d+), titel', a)
print(ids, a.count('ok:'), b.count('ok:'))
g = lambda s: re.findall(r"titel: '([^']*)'.*?lage: '([^']*)'.*?opt: (\[.*?\]), ok: (\d)", s)
same = g(a) == g(b)
print('Fragenpool identisch:', same)
raise SystemExit(0 if same else 1)
