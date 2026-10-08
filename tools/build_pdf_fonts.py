"""Erzeugt die eingebetteten PDF-Schriften (Liberation Sans, SIL OFL 1.1) als JS-Block und setzt ihn in die HTML-Dateien ein.
Aufruf: python3 tools/build_pdf_fonts.py   (braucht fonttools und die Liberation-Fonts)"""
import base64, io, os, re, sys
from fontTools import subset
from fontTools.ttLib import TTFont
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = '/usr/share/fonts/truetype/liberation/'
FONTS = [('AAAAAA+LiberationSans', 'LiberationSans-Regular.ttf', 0), ('AAAAAB+LiberationSans-Bold', 'LiberationSans-Bold.ttf', 0), ('AAAAAC+LiberationSans-Italic', 'LiberationSans-Italic.ttf', 1)]
# WinAnsi (cp1252): alle Zeichen 32 bis 255, die es dort gibt
codes = [c for c in range(32, 256)]
def uni(c):
    try: return ord(bytes([c]).decode('cp1252'))
    except Exception: return None
unis = sorted({u for u in map(uni, codes) if u})
out = []
for name, fn, it in FONTS:
    opts = subset.Options(); opts.hinting = False; opts.layout_features = []; opts.name_IDs = [1, 2, 4, 6]; opts.notdef_outline = True; opts.glyph_names = False; opts.legacy_kern = False
    f = TTFont(SRC + fn); sub = subset.Subsetter(opts); sub.populate(unicodes=unis); sub.subset(f)
    buf = io.BytesIO(); f.save(buf); data = buf.getvalue()
    g = TTFont(io.BytesIO(data)); upm = g['head'].unitsPerEm; cmap = g.getBestCmap(); hm = g['hmtx']
    w = []
    for c in range(32, 256):
        u = uni(c); gn = cmap.get(u) if u else None
        w.append(round(hm[gn][0] * 1000 / upm) if gn else 0)
    bb = [round(g['head'].xMin * 1000 / upm), round(g['head'].yMin * 1000 / upm), round(g['head'].xMax * 1000 / upm), round(g['head'].yMax * 1000 / upm)]
    hh = g['hhea']; os2 = g['OS/2']
    out.append("{n:'%s',it:%d,w:[%s],bb:[%s],a:%d,d:%d,c:%d,s:%d,b64:'%s'}" % (name, it, ','.join(map(str, w)), ','.join(map(str, bb)), round(hh.ascent * 1000 / upm), round(hh.descent * 1000 / upm), round(getattr(os2, 'sCapHeight', 700) * 1000 / upm) or 700, 140 if 'Bold' in name else 80, base64.b64encode(data).decode()))
    print(name, len(data), 'Byte')
js = "/*PDFFONTS*/\nconst PDF_FONTS = [\n  " + ",\n  ".join(out) + """
];
/* Liberation Sans (SIL Open Font License 1.1), metrisch gleich Helvetica und Arial. Als Teilmenge in die PDFs eingebettet. */
function fontSet(first, count) {
  const d = [], extra = [];
  for (let k = 0; k < count; k++) {
    const f = PDF_FONTS[k], bin = atob(f.b64), fd = first + extra.length, ff = fd + 1;
    d.push(`<< /Type /Font /Subtype /TrueType /BaseFont /${f.n} /FirstChar 32 /LastChar 255 /Widths [${f.w.join(' ')}] /Encoding /WinAnsiEncoding /FontDescriptor ${fd} 0 R >>`);
    extra.push(`<< /Type /FontDescriptor /FontName /${f.n} /Flags ${f.it ? 96 : 32} /FontBBox [${f.bb.join(' ')}] /ItalicAngle ${f.it ? -12 : 0} /Ascent ${f.a} /Descent ${f.d} /CapHeight ${f.c} /StemV ${f.s} /FontFile2 ${ff} 0 R >>`);
    extra.push(`<< /Length ${bin.length} /Length1 ${bin.length} >>\\nstream\\n${bin}\\nendstream`);
  }
  return { d, extra };
}
/*ENDPDFFONTS*/"""
for p in ('funkuebung.html', 'standalone.html'):
    path = os.path.join(R, p); s = open(path, encoding='utf-8').read()
    if '/*PDFFONTS*/' in s:
        s = re.sub(r'/\*PDFFONTS\*/.*?/\*ENDPDFFONTS\*/', lambda m: js, s, flags=re.S)
    else:
        marker = 'function makePdf(lines) {'
        assert s.count(marker) == 1, p
        s = s.replace(marker, js + '\n' + marker)
    open(path, 'w', encoding='utf-8').write(s)
print('ok')
