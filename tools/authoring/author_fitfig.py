"""Last build step: keeps every figure label inside its drawing and puts every figure in the brand palette. A label that would run past an edge is moved in;
one wider than the drawing is set a little smaller. Widths are estimated for Albert Sans."""
import json, os, re, glob
from author_common import ROOT
TXT = re.compile(r"<text x='([\d.-]+)' y='([\d.-]+)' text-anchor='(\w+)' font-size='([\d.]+)' font-weight='(\d+)'([^>]*)>([^<]*)</text>")
# Figures are drawn with working colour names; this maps them onto the personal brand palette
# (Charcoal, Chaparral, Manzanita, the two tints, Sand, Ground), so every drawing matches the site.
PALETTE = {'#00242E': '#22221F', '#00574A': '#2E563B', '#1B795A': '#2E563B', '#568CBB': '#6E2B3F', '#FF6622': '#6E2B3F', '#EEEDE8': '#E2CBA0',
           '#D9F1D6': '#CACFC1', '#6BD688': '#CACFC1', '#E7E8E8': '#D8C5C2', '#FFFFFF': '#F6F1E7', '#F2F2F2': '#F6F1E7'}
BRAND = re.compile('|'.join(PALETTE), re.I)
moved = shrunk = 0
def fit(f):
    global moved, shrunk
    if not isinstance(f, dict) or 'svg' not in f: return
    W = float(f['viewBox'].split()[2]); H = float(f['viewBox'].split()[3])
    def one(m):
        global moved, shrunk
        x, y, a, z, wt, rest, t = float(m[1]), m[2], m[3], float(m[4]), m[5], m[6], m[7]
        k = 0.52 if wt == '600' else 0.49; w = len(t) * z * k
        if w > W - 8:
            z2 = max(8.0, z * (W - 8) / w); shrunk += 1; w = len(t) * z2 * k; z = z2
        x0 = x if a == 'start' else x - w if a == 'end' else x - w / 2
        if x0 < 3: x += 3 - x0; moved += 1
        elif x0 + w > W - 3: x -= x0 + w - (W - 3); moved += 1
        yv = float(y); yv = min(max(yv, z * 0.8 + 1), H - 3); y = f'{yv:g}'
        return f"<text x='{x:.0f}' y='{y}' text-anchor='{a}' font-size='{z:g}' font-weight='{wt}'{rest}>{t}</text>"
    f['svg'] = BRAND.sub(lambda m: PALETTE[m[0].upper()], TXT.sub(one, f['svg']))
for path in glob.glob(os.path.join(ROOT, 'questions', '*.json')):
    bank = json.load(open(path))
    for q in bank: fit(q.get('figure')); fit(q.get('solutionFigure'))
    json.dump(bank, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
for path in glob.glob(os.path.join(ROOT, 'guide', '*.json')):
    g = json.load(open(path))
    for s in g['sections']:
        fit(s.get('figure')); [fit(f) for f in s.get('figures', [])]; [fit(e.get('figure')) for e in s.get('examples', []) if isinstance(e, dict)]
        if isinstance(s.get('example'), dict): fit(s['example'].get('figure'))
    json.dump(g, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
print(f'figure labels moved inside: {moved} | set smaller to fit: {shrunk}')
