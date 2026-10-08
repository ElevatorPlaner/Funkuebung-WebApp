import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
APP = 'file://' + os.path.join(ROOT, 'funkuebung.html')
FRAGEN = 'file://' + os.path.join(ROOT, 'fragen.html')
CHROMIUM = os.environ.get('CHROMIUM', '/opt/pw-browsers/chromium')
def launch(p):
    return p.chromium.launch(executable_path=CHROMIUM) if os.path.exists(CHROMIUM) else p.chromium.launch()
