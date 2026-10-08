import os
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import re
f = open(os.path.join(R,'fragen.html'), encoding='utf-8').read()
i = f.index('fragen: ['); j = f.index('\n  ]', i)
pool = 'const POOL = [' + f[i + len('fragen: ['):j] + '\n];'
t = open(os.path.join(R,'uebungsleiter.template.html'), encoding='utf-8').read()
open(os.path.join(R,'uebungsleiter.html'), 'w', encoding='utf-8').write(t.replace('/*@@POOL@@*/', pool))
