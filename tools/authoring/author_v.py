"""Version generator: turns one verified question into a family of numeric versions, each with its own drawn figure.
Run after author_a/b/d1/d2. The formula of every family is checked against the independently written calculation for version 1."""
import json, math, os, re, statistics
from author_dsl import BANK, _load, ROOT
SL, EM, JD, BL, CR, LG, RU = '#00242E', '#00574A', '#1B795A', '#568CBB', '#EEEDE8', '#D9F1D6', '#E7E8E8'
NAMES = {k: getattr(math, k) for k in ('sqrt', 'pi', 'sin', 'cos', 'tan', 'atan', 'asin', 'acos', 'log10', 'log', 'exp', 'erf', 'hypot', 'comb')}
NAMES.update(rad=math.radians, g=9.81, gw=9.81, abs=abs, max=max, min=min, sum=sum, sd=statistics.stdev, psd=statistics.pstdev, int=int)
def nf(x, dp=None):
    if isinstance(x, str): return x
    if isinstance(x, (list, tuple)): return ', '.join(nf(v) for v in x[:-1]) + ' and ' + nf(x[-1])
    if dp is None:
        if abs(x - round(x)) < 1e-9: return f"{int(round(x)):,}"
        m = abs(x); dp = 0 if m >= 1000 else 1 if m >= 100 else 2 if m >= 1 else 3 if m >= 0.01 else 4
        s = f"{x:,.{dp}f}"; return s.rstrip('0').rstrip('.') if '.' in s else s
    return f"{x:,.{dp}f}"
def render(text, env):
    return re.sub(r'\[([^\[\]|]+)(?:\|(\d))?\]', lambda m: nf(eval(m.group(1), {'__builtins__': {}}, env), int(m.group(2)) if m.group(2) else None), text).replace(' || ', '\n\n')
def first_number(t):
    m = re.search(r'-?\d+(?:\.\d+)?', str(t).replace(',', '').replace('$', '')); return float(m.group()) if m else None
# ---------------- figures (original drawings, sized from the question's own numbers) ----------------
def T(x, y, s, a='middle', c=SL, w='400', z=12): return f"<text x='{x:.0f}' y='{y:.0f}' text-anchor='{a}' font-size='{z}' font-weight='{w}' fill='{c}'>{s}</text>"
def arrow(x, y1, y2, c=EM, wd=3):          # vertical arrow from y1 to y2
    d = 1 if y2 > y1 else -1
    return f"<line x1='{x:.0f}' y1='{y1:.0f}' x2='{x:.0f}' y2='{y2 - 8*d:.0f}' stroke='{c}' stroke-width='{wd}'/><path d='M{x:.0f} {y2:.0f} L{x-6:.0f} {y2-12*d:.0f} L{x+6:.0f} {y2-12*d:.0f} Z' fill='{c}'/>"
def dim(x1, x2, y, label): return f"<line x1='{x1:.0f}' y1='{y}' x2='{x2:.0f}' y2='{y}' stroke='{SL}'/><line x1='{x1:.0f}' y1='{y-6}' x2='{x1:.0f}' y2='{y+6}' stroke='{SL}'/><line x1='{x2:.0f}' y1='{y-6}' x2='{x2:.0f}' y2='{y+6}' stroke='{SL}'/>" + T((x1+x2)/2, y+16, label)
def beam(L, pts=(), w=None, kind='simple', R=None, unit='m', fu='kN'):
    x0, x1, yb = 50, 350, 78; X = lambda a: x0 + (x1 - x0) * a / L
    s = f"<rect x='{x0}' y='{yb}' width='{x1-x0}' height='14' fill='{CR}' stroke='{SL}' stroke-width='2'/>"
    if kind == 'simple':
        s += f"<path d='M{x0} {yb+14} L{x0-14} {yb+40} L{x0+14} {yb+40} Z' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/><circle cx='{x1}' cy='{yb+25}' r='10' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/><line x1='{x1-22}' y1='{yb+36}' x2='{x1+22}' y2='{yb+36}' stroke='{SL}' stroke-width='2'/>" + T(x0 - 24, yb + 34, 'A', w='600') + T(x1 + 26, yb + 30, 'B', w='600')
    else:
        s += f"<rect x='{x0-14}' y='{yb-30}' width='14' height='74' fill='{RU}' stroke='{SL}' stroke-width='2'/>"
    if w:
        for i in range(9): s += arrow(x0 + (x1 - x0) * i / 8, 44, yb - 1, JD, 2)
        s += f"<line x1='{x0}' y1='44' x2='{x1}' y2='44' stroke='{JD}' stroke-width='2'/>" + T((x0 + x1) / 2 + 60, 38, f"{nf(w)} {fu}/{unit}", c=JD, w='600')
    cuts = [0]
    for a, P in pts:
        s += arrow(X(a), 14 if not w else 6, yb - 1 if not w else 42) + T(X(a) + (26 if X(a) < 300 else -26), 22, f"{nf(P)} {fu}", c=EM, w='600'); cuts.append(a)
    cuts = sorted(set(cuts + [L])); alt = f"A {'simply supported' if kind == 'simple' else 'cantilever'} beam {nf(L)} {unit} long"
    for a, b in zip(cuts, cuts[1:]): s += dim(X(a), X(b), 176 if R else 136, f"{nf(b - a)} {unit}")
    if R:
        s += arrow(x0, yb + 84, yb + 44, BL) + T(x0 + 12, yb + 80, f"{nf(R[0])} {fu}", a='start', c=BL, w='600') + (arrow(x1, yb + 84, yb + 40, BL) + T(x1 - 12, yb + 80, f"{nf(R[1])} {fu}", a='end', c=BL, w='600') if R[1] is not None else '')
    return {'viewBox': '0 0 400 205' if R else '0 0 400 165', 'svg': s, 'alt': alt + (f" with a uniform load of {nf(w)} {fu}/{unit}" if w else '') + ''.join(f", a {nf(P)} {fu} point load {nf(a)} {unit} from the left end" for a, P in pts) + '.'}
def truss(span, h, P):
    s = f"<path d='M60 130 L340 130 L200 30 Z' fill='none' stroke='{SL}' stroke-width='4'/><path d='M60 130 L46 154 L74 154 Z' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/><circle cx='340' cy='142' r='9' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/>"
    s += arrow(200, 0, 28) + T(236, 12, f"{nf(P)} kN", c=EM, w='600') + dim(60, 340, 170, f"{nf(span)} m") + f"<line x1='372' y1='30' x2='372' y2='130' stroke='{SL}'/>" + T(386, 84, f"{nf(h)} m", a='start')
    return {'viewBox': '0 0 430 195', 'svg': s, 'alt': f"A symmetric triangular truss with a span of {nf(span)} m and a height of {nf(h)} m, loaded with {nf(P)} kN at the apex."}
def tsec(bf, tf, tw, hw):
    k = 150 / max(bf, hw + tf); fx, wx = 200 - bf * k / 2, 200 - tw * k / 2; top = 20
    s = f"<rect x='{fx:.0f}' y='{top}' width='{bf*k:.0f}' height='{tf*k:.0f}' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='{wx:.0f}' y='{top+tf*k:.0f}' width='{tw*k:.0f}' height='{hw*k:.0f}' fill='{CR}' stroke='{SL}' stroke-width='2'/>"
    s += T(200, top - 6, f"{nf(bf)} mm") + T(fx - 8, top + tf * k / 2 + 4, f"{nf(tf)} mm", a='end') + T(wx + tw * k + 8, top + tf * k + hw * k / 2, f"{nf(hw)} mm", a='start') + T(200, top + (tf + hw) * k + 16, f"{nf(tw)} mm")
    return {'viewBox': f"0 0 400 {top + (tf + hw) * k + 26:.0f}", 'svg': s, 'alt': f"A T-shaped section: flange {nf(bf)} by {nf(tf)} mm on a web {nf(tw)} by {nf(hw)} mm."}
def rect(b, h, u='mm'):
    k = 130 / max(b, h); x, y = 200 - b * k / 2, 20
    s = f"<rect x='{x:.0f}' y='{y}' width='{b*k:.0f}' height='{h*k:.0f}' fill='{CR}' stroke='{SL}' stroke-width='2'/><line x1='{x-20:.0f}' y1='{y+h*k/2:.0f}' x2='{x+b*k+20:.0f}' y2='{y+h*k/2:.0f}' stroke='{BL}' stroke-dasharray='6 4'/>" + T(200, y + h * k + 16, f"{nf(b)} {u}") + T(x - 8, y + h * k / 4, f"{nf(h)} {u}", a='end')
    return {'viewBox': f"0 0 400 {y + h * k + 26:.0f}", 'svg': s, 'alt': f"A rectangular section {nf(b)} {u} wide and {nf(h)} {u} deep with its horizontal centroidal axis."}
def soil(g1, g2, zw, z):
    k = 150 / z; yw = 24 + zw * k
    s = f"<rect x='30' y='24' width='300' height='{zw*k:.0f}' fill='{CR}'/><rect x='30' y='{yw:.0f}' width='300' height='{(z-zw)*k:.0f}' fill='{LG}'/><line x1='30' y1='24' x2='330' y2='24' stroke='{SL}' stroke-width='3'/><line x1='30' y1='{yw:.0f}' x2='330' y2='{yw:.0f}' stroke='{BL}' stroke-width='2' stroke-dasharray='8 4'/>"
    s += T(40, 24 + zw * k / 2 + 4, f"{nf(g1)} kN/m³", a='start') + T(40, yw + (z - zw) * k / 2 + 4, f"{nf(g2)} kN/m³ saturated", a='start') + T(322, yw - 5, 'Water table', a='end', c=BL) + f"<circle cx='300' cy='{24+z*k:.0f}' r='5' fill='{EM}'/>" + f"<line x1='350' y1='24' x2='350' y2='{24+z*k:.0f}' stroke='{SL}'/>" + T(358, 24 + z * k / 2, f"{nf(z)} m", a='start') + T(358, 24 + zw * k / 2, f"{nf(zw)} m", a='start', c=BL)
    return {'viewBox': f"0 0 420 {24 + z * k + 16:.0f}", 'svg': s, 'alt': f"A soil profile with the water table {nf(zw)} m below the surface and a point at {nf(z)} m depth."}
def wall(H, P=None):
    s = f"<rect x='150' y='20' width='24' height='130' fill='{RU}' stroke='{SL}' stroke-width='2'/><rect x='174' y='20' width='170' height='130' fill='{CR}'/><line x1='174' y1='20' x2='344' y2='20' stroke='{SL}' stroke-width='2'/><line x1='110' y1='150' x2='344' y2='150' stroke='{SL}' stroke-width='2'/><path d='M174 20 L174 150 L254 150 Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>"
    s += f"<line x1='128' y1='20' x2='128' y2='150' stroke='{SL}'/>" + T(120, 90, f"{nf(H)} m", a='end')
    if P is not None: s += f"<line x1='250' y1='107' x2='184' y2='107' stroke='{EM}' stroke-width='3'/><path d='M176 107 L190 101 L190 113 Z' fill='{EM}'/>" + T(300, 104, f"{nf(P, 1)} kN/m", c=EM, w='600') + T(300, 120, 'at H / 3', c=EM)
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': f"A retaining wall {nf(H)} m high with a triangular active pressure diagram behind it."}
def channel(b, y):
    k = 200 / max(b, 2 * y); x = 200 - b * k / 2
    s = f"<path d='M{x:.0f} 20 L{x:.0f} {30+y*k*1.4:.0f} L{x+b*k:.0f} {30+y*k*1.4:.0f} L{x+b*k:.0f} 20' fill='none' stroke='{SL}' stroke-width='3'/><rect x='{x+2:.0f}' y='{30+y*k*0.4:.0f}' width='{b*k-4:.0f}' height='{y*k:.0f}' fill='{BL}' fill-opacity='.35'/>" + T(200, 46 + y * k * 1.4, f"{nf(b)} m") + T(x + b * k + 8, 30 + y * k * 0.9, f"{nf(y)} m deep", a='start')
    return {'viewBox': f"0 0 400 {56 + y * k * 1.4:.0f}", 'svg': s, 'alt': f"A rectangular channel {nf(b)} m wide flowing {nf(y)} m deep."}
def pipe(d1, d2):
    s = f"<path d='M30 40 L170 40 L230 58 L370 58 L370 92 L230 92 L170 110 L30 110 Z' fill='{BL}' fill-opacity='.25' stroke='{SL}' stroke-width='2'/><line x1='60' y1='75' x2='110' y2='75' stroke='{EM}' stroke-width='3'/><path d='M118 75 L104 69 L104 81 Z' fill='{EM}'/>" + T(100, 30, f"{nf(d1)} mm") + T(300, 48, f"{nf(d2)} mm") + T(100, 130, 'Section 1') + T(300, 112, 'Section 2')
    return {'viewBox': '0 0 400 140', 'svg': s, 'alt': f"A pipe narrowing from {nf(d1)} mm to {nf(d2)} mm in the direction of flow."}
def vcurve(g1, g2, L):
    s = f"<path d='M40 110 Q200 10 360 96' fill='none' stroke='{SL}' stroke-width='3'/><line x1='40' y1='110' x2='200' y2='10' stroke='{BL}' stroke-dasharray='6 4'/><line x1='200' y1='10' x2='360' y2='96' stroke='{BL}' stroke-dasharray='6 4'/>" + T(40, 128, 'PVC') + T(360, 114, 'PVT') + T(200, 8, 'PVI') + T(96, 52, f"+{nf(g1)}%", c=BL) + T(304, 44, f"{nf(g2)}%", c=BL) + dim(40, 360, 146, f"{nf(L)} ft")
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': f"A crest vertical curve {nf(L)} ft long joining a +{nf(g1)}% grade to a {nf(g2)}% grade."}
def forces(F1, F2, th):
    a = math.radians(th); x2, y2 = 120 + 150 * math.cos(a), 150 - 150 * math.sin(a)
    s = f"<line x1='120' y1='150' x2='320' y2='150' stroke='{EM}' stroke-width='3'/><path d='M330 150 L316 144 L316 156 Z' fill='{EM}'/><line x1='120' y1='150' x2='{x2:.0f}' y2='{y2:.0f}' stroke='{JD}' stroke-width='3'/><circle cx='{x2:.0f}' cy='{y2:.0f}' r='5' fill='{JD}'/><circle cx='120' cy='150' r='4' fill='{SL}'/>" + T(300, 170, f"{nf(F1)} N", c=EM, w='600') + T(x2 + 34, y2 + 4, f"{nf(F2)} N", c=JD, w='600') + T(168, 142, f"{nf(th)}°")
    return {'viewBox': '0 0 400 185', 'svg': s, 'alt': f"Two forces at a point: {nf(F1)} N along the x-axis and {nf(F2)} N at {nf(th)}° above it."}
def incline(th, label=''):
    t = math.tan(math.radians(th or 25)); base = min(280, 120 / t); h = base * t; x0 = 200 - base / 2
    s = f"<path d='M{x0:.0f} 150 L{x0+base:.0f} 150 L{x0+base:.0f} {150-h:.0f} Z' fill='{CR}' stroke='{SL}' stroke-width='2'/>"
    mx, my = x0 + base * 0.55, 150 - h * 0.55
    s += f"<g transform='translate({mx:.0f} {my:.0f}) rotate({-(th or 25)})'><rect x='-24' y='-30' width='48' height='30' fill='{LG}' stroke='{JD}' stroke-width='2'/></g>"
    s += T(x0 + 44, 144, f"{nf(th)}°" if th else 'angle ?') + (T(200, 172, label) if label else '')
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"A block on an incline at {nf(th)}° to the horizontal." if th else 'A block on an incline at an unknown angle to the horizontal.'}
def harrow(x1, x2, y, c=EM, wd=3):
    d = 1 if x2 > x1 else -1
    return f"<line x1='{x1:.0f}' y1='{y:.0f}' x2='{x2-8*d:.0f}' y2='{y:.0f}' stroke='{c}' stroke-width='{wd}'/><path d='M{x2:.0f} {y:.0f} L{x2-12*d:.0f} {y-6:.0f} L{x2-12*d:.0f} {y+6:.0f} Z' fill='{c}'/>"
def cashflow(n, P=None, A=None, F=None, unit='$'):
    x0, x1, y = 40, 360, 90; X = lambda k: x0 + (x1 - x0) * k / n; step = max(1, n // 10)
    s = f"<line x1='{x0}' y1='{y}' x2='{x1}' y2='{y}' stroke='{SL}' stroke-width='2'/>"
    for k in range(0, n + 1):
        s += f"<line x1='{X(k):.0f}' y1='{y-4}' x2='{X(k):.0f}' y2='{y+4}' stroke='{SL}'/>" + (T(X(k), y + 18, str(k), z=11) if k % step == 0 or k == n else '')
    alt = f"A cash flow diagram over {n} periods"
    if P is not None: s += arrow(X(0), y, y + 56, EM) + T(X(0) + 8, y + 52, P, a='start', c=EM, w='600'); alt += f", {P} at time 0"
    if A is not None:
        for k in range(1, n + 1): s += arrow(X(k), y, y - 34, BL, 2)
        s += T((x0 + x1) / 2, y - 44, A + ' each period', c=BL, w='600'); alt += f", {A} at the end of every period"
    if F is not None: s += arrow(X(n), y, y - 66, JD) + T(X(n) - 8, y - 70, F, a='end', c=JD, w='600'); alt += f", {F} at period {n}"
    return {'viewBox': '0 0 400 160', 'svg': s + T(200, 150, 'End of period', z=11), 'alt': alt + '.'}
def mohr(sx, sy, txy):
    c = (sx + sy) / 2; r = math.hypot((sx - sy) / 2, txy); lo, hi = min(0, c - r), max(0, c + r); k = min(280 / (hi - lo), 80 / r); X = lambda v: 60 + (v - lo) * k; R = r * k; y = R + 22
    s = f"<line x1='40' y1='{y}' x2='370' y2='{y}' stroke='{SL}'/><line x1='{X(0):.0f}' y1='{y-R-12:.0f}' x2='{X(0):.0f}' y2='{y+R+12:.0f}' stroke='{SL}'/><circle cx='{X(c):.0f}' cy='{y}' r='{R:.0f}' fill='{LG}' fill-opacity='.5' stroke='{JD}' stroke-width='2'/>"
    s += f"<line x1='{X(sx):.0f}' y1='{y+txy*k:.0f}' x2='{X(sy):.0f}' y2='{y-txy*k:.0f}' stroke='{BL}' stroke-width='2'/><circle cx='{X(sx):.0f}' cy='{y+txy*k:.0f}' r='4' fill='{BL}'/><circle cx='{X(sy):.0f}' cy='{y-txy*k:.0f}' r='4' fill='{BL}'/><circle cx='{X(c):.0f}' cy='{y}' r='3' fill='{SL}'/>"
    s += T(X(c), y + 16, f"centre {nf(c)}", z=11) + T(X(sx) + 6, y + txy * k + 14, f"({nf(sx)}, {nf(txy)})", a='start', z=11, c=BL) + T(376, y - 6, 'normal', a='end', z=11) + T(X(0) + 4, y - R - 2, 'shear', a='start', z=11)
    return {'viewBox': f"0 0 400 {y + R + 20:.0f}", 'svg': s, 'alt': f"Mohr's circle for normal stresses {nf(sx)} and {nf(sy)} MPa with shear stress {nf(txy)} MPa."}
def hcurve(R, D, unit='ft'):
    a = math.radians(D) / 2; r = 130 / math.sin(a); x1, x2, y1 = 70, 330, 110; tl = r * math.tan(a); py = y1 - tl * math.sin(a); ux, uy = math.sin(a), math.cos(a)
    s = f"<path d='M{x1} {y1} A{r:.0f} {r:.0f} 0 0 1 {x2} {y1}' fill='none' stroke='{SL}' stroke-width='3'/><line x1='{x1-40*uy:.0f}' y1='{y1+40*ux:.0f}' x2='200' y2='{py:.0f}' stroke='{BL}' stroke-dasharray='6 4'/><line x1='{x2+40*uy:.0f}' y1='{y1+40*ux:.0f}' x2='200' y2='{py:.0f}' stroke='{BL}' stroke-dasharray='6 4'/>"
    s += f"<line x1='{x1}' y1='{y1}' x2='{x1+60*ux:.0f}' y2='{y1+60*uy:.0f}' stroke='{SL}'/><line x1='{x2}' y1='{y1}' x2='{x2-60*ux:.0f}' y2='{y1+60*uy:.0f}' stroke='{SL}'/>" + T(x1 - 4, y1 - 8, 'PC', a='end', w='600') + T(x2 + 4, y1 - 8, 'PT', a='start', w='600') + T(200, py - 8, 'PI', w='600') + T(200, y1 + 62, f"R = {nf(R)} {unit}, deflection angle {nf(D)}°") + T(x1 + 40, y1 + 40, 'R', z=11) + T(x2 - 40, y1 + 40, 'R', z=11)
    return {'viewBox': f"0 0 400 {y1 + 76}", 'svg': s, 'alt': f"A horizontal circular curve of radius {nf(R)} {unit} with a deflection angle of {nf(D)}°, showing PC, PI and PT."}
def level(bs, fs):
    k = 26; yl = 50
    s = f"<path d='M20 150 L120 140 L200 132 L290 150 L380 158' fill='none' stroke='{SL}' stroke-width='2'/><line x1='70' y1='{yl}' x2='330' y2='{yl}' stroke='{BL}' stroke-dasharray='6 4'/>"
    s += f"<rect x='66' y='{yl-12}' width='8' height='{145-yl+12}' fill='{CR}' stroke='{SL}'/><rect x='326' y='{yl-12}' width='8' height='{154-yl+12}' fill='{CR}' stroke='{SL}'/><rect x='186' y='{yl-7}' width='28' height='14' fill='{LG}' stroke='{JD}' stroke-width='2'/><path d='M200 {yl+7} L186 132 M200 {yl+7} L214 132' stroke='{SL}' stroke-width='2'/>"
    s += T(70, 170, 'Benchmark', w='600') + T(330, 176, 'New point', w='600') + T(84, yl + 46, f"BS {nf(bs, 2)} m", a='start') + T(316, yl + 46, f"FS {nf(fs, 2)} m", a='end') + T(200, yl - 14, 'Line of sight', c=BL, z=11)
    return {'viewBox': '0 0 400 185', 'svg': s, 'alt': f"A level set up between a benchmark and a new point, with a backsight of {nf(bs,2)} m and a foresight of {nf(fs,2)} m."}
def gate(b, h):
    s = f"<rect x='40' y='30' width='150' height='120' fill='{BL}' fill-opacity='.25'/><line x1='20' y1='30' x2='190' y2='30' stroke='{BL}' stroke-width='2'/><rect x='190' y='30' width='12' height='120' fill='{RU}' stroke='{SL}' stroke-width='2'/><line x1='20' y1='150' x2='260' y2='150' stroke='{SL}' stroke-width='2'/><path d='M190 30 L190 150 L110 150 Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>"
    s += harrow(120, 188, 110) + T(100, 24, 'Water surface', c=BL, z=11) + f"<line x1='222' y1='30' x2='222' y2='150' stroke='{SL}'/>" + T(230, 94, f"{nf(h)} m tall, {nf(b)} m wide", a='start') + T(112, 104, 'F', c=EM, w='600')
    return {'viewBox': '0 0 400 165', 'svg': s, 'alt': f"A vertical gate {nf(h)} m tall and {nf(b)} m wide with its top at the water surface and a triangular pressure diagram."}
def rcbeam(b, d, As, a=None):
    k = 130 / d; x = 110; w = b * k; h = d * k + 22
    s = f"<rect x='{x}' y='16' width='{w:.0f}' height='{h:.0f}' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + ''.join(f"<circle cx='{x + w*(i+1)/4:.0f}' cy='{16+d*k:.0f}' r='6' fill='{SL}'/>" for i in range(3))
    s += T(x + w / 2, h + 34, f"{nf(b)} mm") + f"<line x1='{x-16}' y1='16' x2='{x-16}' y2='{16+d*k:.0f}' stroke='{SL}'/>" + T(x - 22, 16 + d * k / 2, f"d = {nf(d)} mm", a='end') + T(x + w + 10, 20 + d * k, f"{nf(As)} mm² steel", a='start')
    if a: s += f"<rect x='{x}' y='16' width='{w:.0f}' height='{a*k:.0f}' fill='{JD}' fill-opacity='.35'/>" + T(x + w + 10, 16 + a * k / 2 + 4, f"a = {nf(a, 1)} mm", a='start', c=JD, w='600')
    return {'viewBox': f"0 0 400 {h + 44:.0f}", 'svg': s, 'alt': f"A reinforced concrete beam section {nf(b)} mm wide with an effective depth of {nf(d)} mm and {nf(As)} mm^2 of tension steel."}
def network(dA, dB, dC, dD):
    def box(x, y, n, d): return f"<rect x='{x}' y='{y}' width='70' height='40' rx='6' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + T(x + 35, y + 18, n, w='600') + T(x + 35, y + 33, f"{nf(d)} days", z=11)
    s = box(20, 60, 'A', dA) + box(165, 12, 'B', dB) + box(165, 108, 'C', dC) + box(310, 60, 'D', dD)
    for x1, y1, x2, y2 in ((90, 72, 165, 36), (90, 88, 165, 124), (235, 36, 310, 72), (235, 124, 310, 88)): s += f"<line x1='{x1}' y1='{y1}' x2='{x2-6}' y2='{y2 + (3 if y2>y1 else -3)}' stroke='{EM}' stroke-width='2'/><circle cx='{x2-3}' cy='{y2 + (1 if y2>y1 else -1)}' r='4' fill='{EM}'/>"
    return {'viewBox': '0 0 400 160', 'svg': s, 'alt': f"An activity network: A ({nf(dA)} days) is followed by B ({nf(dB)} days) and C ({nf(dC)} days), which are both followed by D ({nf(dD)} days)."}
def column(L, K, top='Pinned', bot='Pinned'):
    s = f"<line x1='200' y1='24' x2='200' y2='150' stroke='{RU}' stroke-width='10'/><path d='M200 24 Q{200 + (46 if K >= 1 else 30)} 87 200 150' fill='none' stroke='{JD}' stroke-width='3' stroke-dasharray='7 4'/><line x1='160' y1='150' x2='240' y2='150' stroke='{SL}' stroke-width='3'/><line x1='160' y1='24' x2='240' y2='24' stroke='{SL}' stroke-width='3'/>"
    s += arrow(200, 0, 22) + T(250, 28, top, a='start') + T(250, 154, bot, a='start') + f"<line x1='130' y1='24' x2='130' y2='150' stroke='{SL}'/>" + T(122, 90, f"{nf(L)} m", a='end') + T(214, 12, 'P', a='start', c=EM, w='600')
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': f"A column {nf(L)} m long under axial load, {bot.lower()} at the base and {top.lower()} at the top, with its buckled shape dashed."}
def footing(B, P, D=None):
    s = f"<line x1='40' y1='60' x2='360' y2='60' stroke='{SL}' stroke-width='2'/><rect x='180' y='20' width='40' height='80' fill='{RU}' stroke='{SL}' stroke-width='2'/><rect x='110' y='100' width='180' height='26' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + arrow(200, 0, 18) + T(214, 12, f"{nf(P)} kN" if P else 'load', a='start', c=EM, w='600') + dim(110, 290, 144, f"B = {nf(B)} m" if B else 'B = ?')
    if D: s += f"<line x1='320' y1='60' x2='320' y2='126' stroke='{SL}'/>" + T(328, 98, f"{nf(D)} m", a='start')
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': 'A footing below the ground surface carrying a column load.'}
def manometer(h, sg=13.6):
    s = f"<circle cx='70' cy='50' r='22' fill='{BL}' fill-opacity='.3' stroke='{SL}' stroke-width='2'/><circle cx='330' cy='50' r='22' fill='{BL}' fill-opacity='.3' stroke='{SL}' stroke-width='2'/><path d='M70 72 L70 150 L330 150 L330 72' fill='none' stroke='{SL}' stroke-width='10' stroke-opacity='.25'/><path d='M70 120 L70 150 L330 150 L330 84' fill='none' stroke='{JD}' stroke-width='8'/>"
    s += f"<line x1='90' y1='120' x2='360' y2='120' stroke='{SL}' stroke-dasharray='4 4'/><line x1='310' y1='84' x2='360' y2='84' stroke='{SL}' stroke-dasharray='4 4'/><line x1='352' y1='84' x2='352' y2='120' stroke='{SL}'/>" + T(362, 106, f"{nf(h)} m", a='start') + T(70, 20, 'Pipe 1', w='600') + T(330, 20, 'Pipe 2', w='600') + T(200, 172, f"Gauge liquid, specific gravity {nf(sg)}", c=JD)
    return {'viewBox': '0 0 420 180', 'svg': s, 'alt': f"A U-tube manometer between two water pipes at the same elevation, with a gauge liquid deflection of {nf(h)} m."}
def projectile(v, th):
    a = math.radians(th); 
    s = f"<line x1='30' y1='140' x2='380' y2='140' stroke='{SL}' stroke-width='2'/><path d='M50 140 Q200 {140 - 240*math.tan(a)/1.6:.0f} 350 140' fill='none' stroke='{JD}' stroke-width='2' stroke-dasharray='7 4'/><line x1='50' y1='140' x2='{50+70*math.cos(a):.0f}' y2='{140-70*math.sin(a):.0f}' stroke='{EM}' stroke-width='3'/><circle cx='{50+70*math.cos(a):.0f}' cy='{140-70*math.sin(a):.0f}' r='5' fill='{EM}'/>"
    s += T(50 + 70 * math.cos(a) - 12, 140 - 70 * math.sin(a) - 10, f"{nf(v)} m/s", a='end' if th > 40 else 'middle', c=EM, w='600') + T(96, 134, f"{nf(th)}°") + dim(50, 350, 156, 'Range')
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"The path of a projectile launched from level ground at {nf(v)} m/s and {nf(th)}° above the horizontal."}
def tank(h, label='Hydrant'):
    s = f"<rect x='40' y='20' width='90' height='46' fill='{BL}' fill-opacity='.3' stroke='{SL}' stroke-width='2'/><line x1='85' y1='66' x2='85' y2='150' stroke='{SL}' stroke-width='4'/><line x1='85' y1='150' x2='330' y2='150' stroke='{SL}' stroke-width='4'/><rect x='322' y='128' width='16' height='22' fill='{JD}'/><line x1='20' y1='158' x2='380' y2='158' stroke='{SL}'/>"
    s += f"<line x1='200' y1='24' x2='200' y2='150' stroke='{SL}'/><line x1='130' y1='24' x2='210' y2='24' stroke='{SL}' stroke-dasharray='4 4'/>" + T(208, 92, f"{nf(h)} m", a='start') + T(85, 14, 'Water surface', c=BL, z=11) + T(330, 122, label, w='600')
    return {'viewBox': '0 0 400 172', 'svg': s, 'alt': f"An elevated tank whose water surface is {nf(h)} m above a {label.lower()}."}
def greenshields(uf, kj):
    s = f"<line x1='50' y1='20' x2='50' y2='140' stroke='{SL}'/><line x1='50' y1='140' x2='370' y2='140' stroke='{SL}'/><line x1='50' y1='36' x2='350' y2='140' stroke='{JD}' stroke-width='3'/><circle cx='200' cy='88' r='5' fill='{EM}'/>"
    s += T(44, 40, nf(uf), a='end') + T(350, 156, nf(kj)) + T(200, 156, nf(kj / 2), c=EM) + T(44, 92, nf(uf / 2), a='end', c=EM) + T(210, 82, 'Capacity point', a='start', c=EM, w='600') + T(210, 172, 'Density, veh/mi', z=11) + T(56, 16, 'Speed, mph', a='start', z=11) + f"<line x1='200' y1='88' x2='200' y2='140' stroke='{EM}' stroke-dasharray='4 4'/><line x1='50' y1='88' x2='200' y2='88' stroke='{EM}' stroke-dasharray='4 4'/>"
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"A straight speed-density line falling from {nf(uf)} mph at zero density to zero speed at {nf(kj)} veh/mi, with the capacity point at its middle."}
def bar(d, L, P, lu='m'):
    s = f"<rect x='40' y='30' width='14' height='80' fill='{RU}' stroke='{SL}' stroke-width='2'/><rect x='54' y='60' width='240' height='20' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + harrow(294, 350, 70) + T(356, 74, f"{nf(P)} kN", a='start', c=EM, w='600') + (dim(54, 294, 104, f"{nf(L)} {lu}") if L else '') + T(174, 52, f"{nf(d)} mm diameter")
    return {'viewBox': '0 0 420 130', 'svg': s, 'alt': f"A {nf(d)} mm diameter rod fixed at one end and pulled with {nf(P)} kN at the other."}
def azimuth(az, L=None, unit='m'):
    a = math.radians(az); x, y = 200 + 100 * math.sin(a), 100 - 100 * math.cos(a) * 0.8
    s = f"<line x1='200' y1='10' x2='200' y2='190' stroke='{SL}'/><line x1='80' y1='100' x2='320' y2='100' stroke='{SL}'/>" + T(200, 8, 'N', w='600', z=11) + T(328, 104, 'E', a='start', w='600', z=11) + f"<line x1='200' y1='100' x2='{x:.0f}' y2='{y:.0f}' stroke='{EM}' stroke-width='3'/><circle cx='{x:.0f}' cy='{y:.0f}' r='5' fill='{EM}'/>"
    s += T(x + 10, y - 6 if y < 100 else y + 16, (f"{nf(L, 2)} {unit}, " if L else '') + f"azimuth {nf(az)}°", a='start' if x < 260 else 'end', c=EM, w='600')
    return {'viewBox': '0 0 400 200', 'svg': s, 'alt': f"A line drawn from the origin at an azimuth of {nf(az)}° clockwise from north."}
def parcel(pts, unit='m'):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]; k = min(300 / (max(xs) - min(xs)), 130 / (max(ys) - min(ys))); X = lambda p: (50 + (p[0] - min(xs)) * k, 160 - (p[1] - min(ys)) * k)
    s = f"<path d='M" + ' L'.join(f"{X(p)[0]:.0f} {X(p)[1]:.0f}" for p in pts) + f" Z' fill='{LG}' fill-opacity='.6' stroke='{SL}' stroke-width='2'/>"
    for p in pts: s += f"<circle cx='{X(p)[0]:.0f}' cy='{X(p)[1]:.0f}' r='4' fill='{SL}'/>" + T(X(p)[0], X(p)[1] + (16 if p[1] == min(ys) else -8), f"({nf(p[0])}, {nf(p[1])})", z=11)
    return {'viewBox': '0 0 400 185', 'svg': s, 'alt': 'A parcel with corners at ' + ', '.join(f"({nf(p[0])}, {nf(p[1])})" for p in pts) + f" {unit}."}
def triangle(a, b, C, unit='m'):
    A = math.radians(C); cx, cy = b * math.cos(A), b * math.sin(A); k = min(260 / max(a, cx), 120 / cy); X = lambda x, y: (70 + x * k, 150 - y * k); p2, p3 = X(a, 0), X(cx, cy)
    s = f"<path d='M70 150 L{p2[0]:.0f} 150 L{p3[0]:.0f} {p3[1]:.0f} Z' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + T((70 + p2[0]) / 2, 168, f"{nf(a)} {unit}") + T((70 + p3[0]) / 2 - 8, (150 + p3[1]) / 2 - 4, f"{nf(b)} {unit}", a='end') + T(70 + 34, 144, f"{nf(C)}°", z=11)
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"A triangle with sides of {nf(a)} {unit} and {nf(b)} {unit} meeting at {nf(C)}°."}
def orifice(h, d):
    s = f"<path d='M60 20 L60 150 L220 150 L220 20' fill='none' stroke='{SL}' stroke-width='3'/><rect x='62' y='40' width='156' height='108' fill='{BL}' fill-opacity='.3'/><path d='M220 126 Q280 128 320 168' fill='none' stroke='{BL}' stroke-width='5'/><line x1='250' y1='40' x2='250' y2='126' stroke='{SL}'/><line x1='220' y1='40' x2='260' y2='40' stroke='{SL}' stroke-dasharray='4 4'/>" + T(258, 86, f"{nf(h)} m", a='start') + T(300, 122, f"{nf(d)} mm orifice", a='start')
    return {'viewBox': '0 0 420 175', 'svg': s, 'alt': f"A tank discharging through a {nf(d)} mm orifice {nf(h)} m below the water surface."}
def cables(W, th):
    a = math.radians(th); dx = 120; dy = dx * math.tan(a); dy = min(dy, 90); dx = dy / math.tan(a)
    s = f"<line x1='40' y1='20' x2='360' y2='20' stroke='{SL}' stroke-width='4'/><line x1='{200-dx:.0f}' y1='20' x2='200' y2='{20+dy:.0f}' stroke='{JD}' stroke-width='3'/><line x1='{200+dx:.0f}' y1='20' x2='200' y2='{20+dy:.0f}' stroke='{JD}' stroke-width='3'/><line x1='200' y1='{20+dy:.0f}' x2='200' y2='{40+dy:.0f}' stroke='{SL}' stroke-width='2'/><rect x='176' y='{40+dy:.0f}' width='48' height='30' fill='{CR}' stroke='{SL}' stroke-width='2'/>"
    s += T(200, 60 + dy, f"{nf(W)} N", z=11, w='600') + T(200 - dx + 34, 34, f"{nf(th)}°") + T(200 + dx - 34, 34, f"{nf(th)}°")
    return {'viewBox': f"0 0 400 {84 + dy:.0f}", 'svg': s, 'alt': f"A {nf(W)} N weight hanging from two cables that each make {nf(th)}° with the horizontal."}
def lever(L, F, th):
    a = math.radians(th); x, y = 330 + 70 * math.cos(math.pi - a), 110 - 70 * math.sin(a)
    s = f"<rect x='70' y='104' width='260' height='12' fill='{CR}' stroke='{SL}' stroke-width='2'/><circle cx='70' cy='110' r='9' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/><line x1='{x:.0f}' y1='{y:.0f}' x2='330' y2='110' stroke='{EM}' stroke-width='3'/><circle cx='330' cy='110' r='5' fill='{EM}'/>" + T(x - 6, y - 6, f"{nf(F)} N", c=EM, w='600') + T(296, 100, f"{nf(th)}°", a='end') + dim(70, 330, 138, f"{nf(L)} m") + T(56, 96, 'Pivot', a='end')
    return {'viewBox': '0 0 400 165', 'svg': s, 'alt': f"A {nf(L)} m lever with a {nf(F)} N force applied at its end, {nf(th)}° from the lever axis."}
def stressblock(sx, sy, txy):
    s = f"<rect x='150' y='40' width='100' height='100' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + harrow(250, 310, 90) + harrow(150, 90, 90) + arrow(200, 40, 4) + arrow(200, 140, 176) + T(316, 94, f"{nf(sx)} MPa", a='start', c=EM, w='600') + T(212, 12, f"{nf(sy)} MPa", a='start', c=EM, w='600')
    s += harrow(160, 240, 30, BL, 2) + harrow(240, 160, 150, BL, 2) + T(250, 30, f"{nf(txy)} MPa shear", a='start', c=BL)
    return {'viewBox': '0 0 420 185', 'svg': s, 'alt': f"A stress element with normal stresses of {nf(sx)} MPa and {nf(sy)} MPa and a shear stress of {nf(txy)} MPa."}
# ---------------- generator ----------------
EXPR, STATS = {}, {'families': 0, 'versions': 0, 'figs': 0}
ERRS = []
TEMPLATES, DRY = {}, [False]
def V(*a, **k):
    names = ('base', 'stem', 'P', 'ans', 'sol', 'wrong', 'dp', 'fig', 'sfig', 'eli5'); t = dict(zip(names, a)); t.update(k)
    import fig2; f2, s2 = fig2.lookup(t['base'], t['stem'])          # figures for force, vector, beam and section questions
    if f2 and not t.get('fig'): t['fig'] = f2
    if s2 and not t.get('sfig'): t['sfig'] = s2
    TEMPLATES[a[0]] = t
    if DRY[0]: return
    try: _V(**t)
    except Exception as e: ERRS.append(f"{a[0]}: {type(e).__name__}: {e}"); [EXPR.pop(x) for x in list(EXPR) if x.startswith(a[0] + '-')]
def _V(base, stem, P, ans, sol, wrong=None, dp=None, fig=None, sfig=None, eli5=None):
    topic = base.rsplit('-', 1)[0]; bank = _load(topic)
    idx = next(i for i, x in enumerate(bank) if x['id'] == base); b = bank[idx]
    n = len(next(iter(P.values()))); out = []
    key0 = b['answer']['value'] if b['format'] == 'numeric' else first_number(next(o['text'] for o in b['options'] if o['id'] == b['answer']))
    m = None if b['format'] == 'numeric' else re.match(r'^(\$?)(-?[\d,]*\.?\d+)(.*)$', next(o['text'] for o in b['options'] if o['id'] == b['answer']))
    for k in range(n):
        env = dict(NAMES); env.update({name: vals[k] for name, vals in P.items()})
        val = eval(ans, {'__builtins__': {}}, env); env['ans'] = val
        if k == 0: assert abs(val - key0) <= 0.011 * max(abs(key0), 1e-9), f"{base}: formula gives {val}, verified key is {key0}"
        q = json.loads(json.dumps(b)); q['id'] = base if k == 0 else f"{base}-{'bcdefgh'[k-1]}"
        q.update(family=base, version=k + 1, versions=n, stem=render(stem, env), solution=render(sol, env))
        if eli5: q['eli5'] = render(eli5, env)
        if b['format'] == 'numeric':
            q['answer'] = dict(b['answer'], value=round(val, dp if dp is not None else 3))
        else:
            vals = [eval(w, {'__builtins__': {}}, env) for w in wrong]; pos = 'abcd'.index(b['answer']); allv = vals[:pos] + [val] + vals[pos:]
            texts = [m.group(1) + nf(v, dp) + m.group(3) for v in allv]
            for i in range(4):
                assert abs(first_number(texts[i]) - allv[i]) <= (0.006 if i == pos else 0.02) * max(abs(allv[i]), 1e-9), f"{q['id']}: option {texts[i]} loses precision from {allv[i]}"
                for j in range(i): assert abs(allv[i] - allv[j]) > 0.015 * max(abs(allv[i]), abs(allv[j]), 1e-9), f"{q['id']}: options {allv[j]} and {allv[i]} are too close"
            q['options'] = [{'id': 'abcd'[i], 'text': texts[i]} for i in range(4)]
        if fig: q['figure'] = fig(env); STATS['figs'] += 1
        if sfig: q['solutionFigure'] = sfig(env)
        if k: EXPR[q['id']] = f"(lambda {', '.join(P)}: {ans})({', '.join(repr(v[k]) for v in P.values())})"
        out.append(q)
    bank[idx:idx + 1] = out; STATS['families'] += 1; STATS['versions'] += n
def save():
    from author_common import dump
    for topic, items in BANK.items(): dump(topic, items)
    path = __import__('os').environ.get('FE_REPO', __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))) + '/tools/calc_expr.json'; allx = json.load(open(path)); allx.update(EXPR)
    json.dump(dict(sorted(allx.items())), open(path, 'w'), indent=1); open(path, 'a').write('\n'); print(STATS)
    for e in ERRS: print('SKIPPED', e)
