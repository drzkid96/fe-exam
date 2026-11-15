"""Figures for force, vector, beam and cross-section questions, in the question and in the explanation.
Every figure is drawn from the question's own numbers. `lookup` is called by the version generator for each question type:
it returns (question figure, solution figure) functions, either of which may be None. `post` adds vector diagrams to the
written-out vector questions that have no numeric template."""
import math, re
from author_v import T, arrow, harrow, dim, nf, beam, incline, wall, mohr, projectile, rect, SL, EM, JD, BL, CR, LG, RU
sin, cos, rad = math.sin, math.cos, math.radians
def arr(x1, y1, x2, y2, c=EM, wd=3, dash=False):
    a = math.atan2(y2 - y1, x2 - x1); bx, by = x2 - 11 * cos(a), y2 - 11 * sin(a); px, py = 5.5 * sin(a), -5.5 * cos(a)
    return f"<line x1='{x1:.0f}' y1='{y1:.0f}' x2='{bx:.0f}' y2='{by:.0f}' stroke='{c}' stroke-width='{wd}'" + (" stroke-dasharray='6 4'" if dash else '') + f"/><path d='M{x2:.0f} {y2:.0f} L{bx+px:.0f} {by+py:.0f} L{bx-px:.0f} {by-py:.0f} Z' fill='{c}'/>"
def vec(items, at=None, unit=''):
    """items: (label, x, y[, colour[, dashed]]) drawn from the origin, or from the point `at`."""
    ox, oy = at or (0, 0)
    if at:
        fs = 0.7 * max(abs(ox), abs(oy), 1e-9) / max(max(abs(i[1]), abs(i[2])) for i in items); items = [(i[0], i[1] * fs, i[2] * fs) + tuple(i[3:]) for i in items]
    pts = [(0, 0), (ox, oy)] + [(ox + i[1], oy + i[2]) for i in items]
    x0, x1, y0, y1 = min(p[0] for p in pts), max(p[0] for p in pts), min(p[1] for p in pts), max(p[1] for p in pts); k = min(250 / max(x1 - x0, 1e-9), 130 / max(y1 - y0, 1e-9))
    X = lambda x: 70 + (x - x0) * k; Y = lambda y: 160 - (y - y0) * k
    s = f"<line x1='40' y1='{Y(0):.0f}' x2='370' y2='{Y(0):.0f}' stroke='{RU}' stroke-width='2'/><line x1='{X(0):.0f}' y1='14' x2='{X(0):.0f}' y2='176' stroke='{RU}' stroke-width='2'/>" + T(372, Y(0) - 5, 'x', a='end', z=11) + T(X(0) + 8, 22, 'y', a='start', z=11)
    if at: s += f"<line x1='{X(0):.0f}' y1='{Y(0):.0f}' x2='{X(ox):.0f}' y2='{Y(oy):.0f}' stroke='{SL}' stroke-dasharray='5 4'/><circle cx='{X(ox):.0f}' cy='{Y(oy):.0f}' r='4' fill='{SL}'/>" + T(X(ox) - 8, Y(oy) + 16, f"({nf(ox)}, {nf(oy)})", a='end', z=11)
    cols = [EM, JD, BL, SL]; alt = []
    for n, i in enumerate(items):
        c = i[3] if len(i) > 3 and i[3] else cols[n % 4]; tx, ty = X(ox + i[1]), Y(oy + i[2])
        s += arr(X(ox), Y(oy), tx, ty, c, 3, len(i) > 4 and i[4]) + T(tx + (10 if i[1] > 0 else -10), ty + (-8 if i[2] >= 0 else 16), i[0], a='start' if i[1] > 0 else 'end', c=c, w='600'); alt.append(i[0])
    return {'viewBox': '0 0 400 190', 'svg': s, 'alt': 'Vector diagram: ' + '; '.join(alt) + '.'}
def vec3(a, b, c, lab='vector'):
    m = max(abs(a), abs(b), abs(c), 1e-9); k = 95 / m; P = lambda x, y, z: (190 + (x - 0.5 * z) * k, 120 - (y - 0.4 * z) * k); O = P(0, 0, 0)
    s = ''.join(f"<line x1='{O[0]:.0f}' y1='{O[1]:.0f}' x2='{p[0]:.0f}' y2='{p[1]:.0f}' stroke='{RU}' stroke-width='2'/>" + T(p[0] + 8, p[1] + 4, n, a='start', z=11) for n, p in (('x', P(m * 1.2, 0, 0)), ('y', P(0, m * 1.2, 0)), ('z', P(0, 0, m * 1.2))))
    p1, p2, p3 = P(a, 0, 0), P(a, 0, c), P(a, b, c)
    s += ''.join(f"<line x1='{u[0]:.0f}' y1='{u[1]:.0f}' x2='{v[0]:.0f}' y2='{v[1]:.0f}' stroke='{BL}' stroke-dasharray='5 4'/>" for u, v in ((O, p1), (p1, p2), (p2, p3)))
    s += arr(O[0], O[1], p3[0], p3[1]) + T((O[0] + p1[0]) / 2, p1[1] + 14, nf(a), c=BL, z=11) + T(p2[0] - 8, (p1[1] + p2[1]) / 2 + 12, nf(c), a='end', c=BL, z=11) + T(p3[0] + 8, (p2[1] + p3[1]) / 2, nf(b), a='start', c=BL, z=11) + T(p3[0] + 6, p3[1] - 8, lab, a='start', c=EM, w='600')
    return {'viewBox': '0 0 400 200', 'svg': s, 'alt': f"A three-dimensional sketch of the {lab} with components {nf(a)}, {nf(b)} and {nf(c)} along x, y and z."}
def fbd(forces, tilt=0, note=''):
    """Free-body diagram of a block. forces: (label, direction in degrees counterclockwise from +x, colour)."""
    cx, cy = 200, 100
    s = f"<g transform='rotate({-tilt} {cx} {cy})'><line x1='70' y1='{cy+20}' x2='330' y2='{cy+20}' stroke='{SL}' stroke-width='2'/><rect x='{cx-30}' y='{cy-20}' width='60' height='40' fill='{LG}' stroke='{JD}' stroke-width='2'/></g>"
    alt = []
    for lab, ang, col in forces:
        a = rad(ang); x1, y1 = cx + 24 * cos(a), cy - 24 * sin(a); x2, y2 = cx + 84 * cos(a), cy - 84 * sin(a)
        s += arr(x1, y1, x2, y2, col or EM) + T(x2 + 12 * cos(a) + (0 if abs(cos(a)) > 0.3 else 8), y2 - 12 * sin(a) + 4, lab, a='start' if cos(a) > 0.3 else 'end' if cos(a) < -0.3 else 'start', c=col or EM, w='600', z=11); alt.append(lab)
    return {'viewBox': '0 0 400 224', 'svg': s + (T(200, 218, note, z=11) if note else ''), 'alt': 'Free-body diagram' + (f" on a surface inclined at {nf(tilt)}°" if tilt else '') + ' showing ' + ', '.join(alt) + '.'}
def gbeam(total, sup=(), pts=(), udl=None, tri=None, R=None, fix=(0, 0), mom=None, unit='m', fu='kN'):
    """A beam of length `total`. sup: (x, 'pin'|'roller'); pts: (x, load); udl: (x0, x1, w); tri: (x0, x1, peak at x1); R: (x, value) reactions."""
    x0, x1, yb = 50, 350, 78; X = lambda a: x0 + (x1 - x0) * a / total
    s = f"<rect x='{x0}' y='{yb}' width='{x1-x0}' height='14' fill='{CR}' stroke='{SL}' stroke-width='2'/>"; alt = f"A beam {nf(total)} {unit} long"
    for i, side in enumerate(fix):
        if side: s += f"<rect x='{(x0-14) if i == 0 else x1}' y='{yb-30}' width='14' height='74' fill='{RU}' stroke='{SL}' stroke-width='2'/>"; alt += f", fixed at the {'left' if i == 0 else 'right'} end"
    for x, kind in sup:
        px = X(x); s += (f"<path d='M{px:.0f} {yb+14} L{px-14:.0f} {yb+40} L{px+14:.0f} {yb+40} Z' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/>" if kind == 'pin' else f"<circle cx='{px:.0f}' cy='{yb+25}' r='10' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/><line x1='{px-22:.0f}' y1='{yb+36}' x2='{px+22:.0f}' y2='{yb+36}' stroke='{SL}' stroke-width='2'/>"); alt += f", a {kind} support at {nf(x)} {unit}"
    if udl:
        a, b, w = udl; n = max(2, int(8 * (b - a) / total))
        for i in range(n + 1): s += arrow(X(a) + (X(b) - X(a)) * i / n, 46, yb - 1, JD, 2)
        s += f"<line x1='{X(a):.0f}' y1='46' x2='{X(b):.0f}' y2='46' stroke='{JD}' stroke-width='2'/>" + T((X(a) + X(b)) / 2, 38, f"{nf(w)} {fu}/{unit}", c=JD, w='600'); alt += f", a uniform load of {nf(w)} {fu}/{unit} from {nf(a)} to {nf(b)} {unit}"
    if tri:
        a, b, w = tri; s += f"<path d='M{X(a):.0f} {yb-2} L{X(b):.0f} {yb-2} L{X(b):.0f} 34 Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>" + T(X(b) + (-8 if b > a else 8), 28, f"{nf(w)} {fu}/{unit}", a='end' if b > a else 'start', c=JD, w='600'); alt += f", a triangular load rising to {nf(w)} {fu}/{unit} at {nf(b)} {unit}"
    cuts = {0, total} | {x for x, _ in sup}
    for n, (a, P) in enumerate(pts):
        top = 10 if not (udl or tri) else 2; s += arrow(X(a), top, (yb - 1) if not udl else 44) + T(X(a) + (8 if X(a) < 300 else -8), top + 10 + 12 * (n % 2), f"{nf(P)} {fu}", a='start' if X(a) < 300 else 'end', c=EM, w='600'); cuts.add(a); alt += f", a {nf(P)} {fu} load at {nf(a)} {unit}"
    if mom: s += f"<path d='M{X(mom[0])-16:.0f} {yb-6} A18 18 0 1 1 {X(mom[0])+16:.0f} {yb-6}' fill='none' stroke='{EM}' stroke-width='3'/><path d='M{X(mom[0])+16:.0f} {yb-2} l-9 -7 l11 -3 Z' fill='{EM}'/>" + T(X(mom[0]), 30, mom[1], c=EM, w='600'); cuts.add(mom[0]); alt += f", a couple of {mom[1]} at {nf(mom[0])} {unit}"
    cuts = sorted(cuts)
    for a, b in zip(cuts, cuts[1:]):
        if X(b) - X(a) > 26: s += dim(X(a), X(b), 176 if R else 136, f"{nf(b - a)} {unit}")
    for x, v in (R or ()):
        s += arrow(X(x), yb + 84, yb + 42, BL) + T(X(x) + (10 if X(x) < 200 else -10), yb + 82, f"{nf(v)} {fu}", a='start' if X(x) < 200 else 'end', c=BL, w='600')
    return {'viewBox': '0 0 400 205' if R else '0 0 400 165', 'svg': s, 'alt': alt + ('. Reactions: ' + ', '.join(f"{nf(v)} {fu} at {nf(x)} {unit}" for x, v in R) if R else '') + '.'}
def shape(polys, circles=(), holes=(), labels=(), mark=None, unit='mm', alt=''):
    """A cross-section. polys and holes: lists of (x, y) corners, y upward; circles: (cx, cy, r, is_hole); labels: (x, y, text, anchor)."""
    pts = [p for g in polys for p in g] + [(c[0] + d * c[2], c[1] + e * c[2]) for c in circles for d, e in ((1, 0), (-1, 0), (0, 1), (0, -1))]
    x0, x1, y0, y1 = min(p[0] for p in pts), max(p[0] for p in pts), min(p[1] for p in pts), max(p[1] for p in pts); k = min(240 / (x1 - x0), 130 / (y1 - y0)); X = lambda x: 80 + (x - x0) * k; Y = lambda y: 150 - (y - y0) * k
    path = lambda g, fill: f"<path d='M" + ' L'.join(f"{X(x):.0f} {Y(y):.0f}" for x, y in g) + f" Z' fill='{fill}' stroke='{SL}' stroke-width='2'/>"
    s = ''.join(path(g, CR) for g in polys) + ''.join(path(g, '#FFFFFF') for g in holes) + ''.join(f"<circle cx='{X(c[0]):.0f}' cy='{Y(c[1]):.0f}' r='{c[2]*k:.0f}' fill='{'#FFFFFF' if c[3] else CR}' stroke='{SL}' stroke-width='2'/>" for c in circles)
    s += ''.join(T(X(x), Y(y), t, a=a, z=11) for x, y, t, a in labels)
    if mark: s += f"<circle cx='{X(mark[0]):.0f}' cy='{Y(mark[1]):.0f}' r='5' fill='{EM}'/>" + T(X(mark[0]) + 9, Y(mark[1]) - 7, mark[2], a='start', c=EM, w='600')
    return {'viewBox': '0 0 400 185', 'svg': s, 'alt': alt}
def couple(F, d, M):
    s = f"<rect x='90' y='84' width='220' height='12' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + arrow(120, 30, 82) + arrow(280, 150, 98) + T(120, 22, f"{nf(F)} N", c=EM, w='600') + T(280, 168, f"{nf(F)} N", c=EM, w='600') + dim(120, 280, 118, f"{nf(d)} m") + T(200, 60, f"M = {nf(M)} N·m, the same about any point", c=BL, w='600')
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"Two equal and opposite {nf(F)} N forces {nf(d)} m apart, forming a couple of {nf(M)} N·m."}
def cables2(al, be, W, T1=None):
    a, b = rad(al), rad(be); h = 90; xa, xb = 200 - h / math.tan(a), 200 + h / math.tan(b); xa, xb = max(xa, 30), min(xb, 370)
    s = f"<line x1='20' y1='20' x2='380' y2='20' stroke='{SL}' stroke-width='4'/><line x1='{xa:.0f}' y1='20' x2='200' y2='110' stroke='{JD}' stroke-width='3'/><line x1='{xb:.0f}' y1='20' x2='200' y2='110' stroke='{JD}' stroke-width='3'/>" + arrow(200, 112, 160) + T(210, 158, f"{nf(W, 1)} N", a='start', c=EM, w='600')
    s += T(xa + 30, 36, f"{nf(al)}°", z=11) + T(xb - 30, 36, f"{nf(be)}°", z=11) + T((xa + 200) / 2 - 10, 72, 'Cable 1' + (f", {nf(T1, 1)} N" if T1 else ''), a='end', c=JD, w='600', z=11) + T((xb + 200) / 2 + 10, 72, 'Cable 2', a='start', c=JD, w='600', z=11)
    return {'viewBox': '0 0 400 175', 'svg': s, 'alt': f"A {nf(W, 1)} N load hanging from two cables at {nf(al)}° and {nf(be)}° to the horizontal."}
def sheard(V1, V2, d, x0=None, M=None):
    k = 90 / (V1 + V2); yz = 30 + V1 * k; X = lambda x: 60 + 280 * x / d; xz = d * V1 / (V1 + V2)
    s = f"<line x1='40' y1='{yz:.0f}' x2='370' y2='{yz:.0f}' stroke='{SL}'/><path d='M60 {yz:.0f} L60 30 L{X(xz):.0f} {yz:.0f} Z' fill='{LG}' stroke='{JD}' stroke-width='2'/><path d='M{X(xz):.0f} {yz:.0f} L340 120 L340 {yz:.0f} Z' fill='{CR}' stroke='{SL}' stroke-width='2'/>"
    s += T(54, 34, f"+{nf(V1)} kN", a='end', z=11) + T(346, 124, f"-{nf(V2)} kN", a='start', z=11) + dim(60, 340, 142, f"{nf(d)} m") + T(46, 20, 'Shear', a='start', z=11)
    if x0: s += f"<line x1='{X(xz):.0f}' y1='24' x2='{X(xz):.0f}' y2='128' stroke='{BL}' stroke-dasharray='5 4'/>" + T(200, 166, f"Zero shear at {nf(x0, 2)} m. Area of the shaded triangle: M = {nf(M, 2)} kN·m", c=BL, w='600', z=11)
    return {'viewBox': '0 0 400 176', 'svg': s, 'alt': f"A shear diagram falling in a straight line from +{nf(V1)} kN to -{nf(V2)} kN over {nf(d)} m."}
W, N, Fr = 'W', 'N', 'Friction'
def L(k, f): return lambda e: f(type('E', (), {x: e[x] for x in e if isinstance(x, str) and x.isidentifier()}))
RECT = lambda b, h: [[(0, 0), (b, 0), (b, h), (0, h)]]
BY_ID = {
 'statics-0001': (None, L(0, lambda e: vec([('F1', e.F1, 0), ('F2', e.F2 * cos(rad(e.th)), e.F2 * sin(rad(e.th))), (f"R = {nf(e.ans, 1)} N", e.F1 + e.F2 * cos(rad(e.th)), e.F2 * sin(rad(e.th)), BL)]))),
 'statics-0004': (None, L(0, lambda e: fbd([(W, 270, EM), (N, 90 + e.ans, JD), ('Friction = (coefficient) N', e.ans, BL)], e.ans, 'On the point of sliding: tan(angle) = coefficient of friction'))),
 'statics-0006': (None, L(0, lambda e: couple(e.Fc, e.d, e.ans))),
 'statics-0014': (L(0, lambda e: fbd([(f"{nf(e.W)} N", 270, EM), ('P', e.th, BL)])), L(0, lambda e: fbd([(f"W = {nf(e.W)} N", 270, EM), (N, 90, JD), (f"P = {nf(e.ans, 1)} N", e.th, BL), (Fr, 180, SL)]))),
 'statics-0015': (None, L(0, lambda e: fbd([(f"W = {nf(e.W)} N", 270, EM), (f"T = {nf(e.ans, 1)} N", e.th, JD), (f"T = {nf(e.ans, 1)} N", 180 - e.th, JD)], 0, 'Free-body diagram of the knot'))),
 'statics-0016': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], tri=(0, e.L, e.w0))), L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], pts=[(2 * e.L / 3, e.w0 * e.L / 2)], R=[(0, e.w0 * e.L / 6), (e.L, e.ans)]))),
 'statics-0018': (L(0, lambda e: vec([(f"{nf(e.Fm)} N", e.s, e.r)])), L(0, lambda e: vec([(f"F = {nf(e.Fm)} N", e.Fm * e.s / math.hypot(e.r, e.s), e.Fm * e.r / math.hypot(e.r, e.s)), (f"Fx = {nf(e.ans, 1)} N", e.Fm * e.s / math.hypot(e.r, e.s), 0, BL, True)]))),
 'dynamics-0002': (None, L(0, lambda e: fbd([(f"W = {nf(e.m * 9.81, 1)} N", 270, EM), (f"N = {nf(e.m * 9.81, 1)} N", 90, JD), (f"Pull = {nf(e.Fp)} N", 0, BL), (f"Friction = {nf(e.mu * e.m * 9.81, 1)} N", 180, SL)]))),
 'dynamics-0008': (None, L(0, lambda e: fbd([('W = m g', 270, EM), (N, 90 + e.th, JD)], e.th, 'Only the weight component along the slope, m g sin(angle), causes acceleration'))),
 'dynamics-0013': (None, L(0, lambda e: fbd([(W, 270, EM), (N, 90 + math.degrees(math.atan(e.G / 100)), JD), ('Braking force', 180 + math.degrees(math.atan(e.G / 100)), BL)], math.degrees(math.atan(e.G / 100)), 'On an upgrade the weight component along the slope also slows the car'))),
 'dynamics-0014': (None, L(0, lambda e: fbd([(W, 270, EM), (N, 90, JD), ('Friction, toward the centre of the curve', 180, BL)], 0, 'View along the direction of travel'))),
 'dynamics-0015': (None, L(0, lambda e: fbd([(f"W = {nf(e.m2 * 9.81, 1)} N", 270, EM), (f"T = {nf(e.m1 * e.ans, 1)} N", 90, JD)], 0, f"Hanging block: accelerates downward at {nf(e.ans, 2)} m/s²"))),
 'math-0012': (None, L(0, lambda e: vec([('A', e.a1, e.a2), ('B', e.b1, e.b2)]))),
 'math-0013': (None, L(0, lambda e: vec3(e.a1, e.a2, e.a3))),
 'structural-0012': (L(0, lambda e: gbeam(e.L, [(e.L, 'roller')], udl=(0, e.L, e.w), fix=(1, 0))), None),
 'structural-0013': (L(0, lambda e: gbeam(e.L, [], udl=(0, e.L, e.w), fix=(1, 1))), None),
 'structural-0021': (L(0, lambda e: gbeam(e.L, [], pts=[(e.a, e.P)], fix=(1, 1))), None),
 'structural-0023': (L(0, lambda e: gbeam(2 * e.L, [(0, 'pin'), (e.L, 'roller'), (2 * e.L, 'roller')], udl=(0, 2 * e.L, e.w))), L(0, lambda e: gbeam(2 * e.L, [(0, 'pin'), (e.L, 'roller'), (2 * e.L, 'roller')], udl=(0, 2 * e.L, e.w), R=[(0, 0.375 * e.w * e.L), (e.L, e.ans), (2 * e.L, 0.375 * e.w * e.L)]))),
 'fluids-0010': (None, L(0, lambda e: fbd([('Weight', 270, EM), ('Buoyant force = weight of water displaced', 90, BL)], 0, 'A floating body: buoyant force equals weight'))),
 'fluids-0017': (None, L(0, lambda e: fbd([('Raft weight + cargo', 270, EM), ('Buoyant force on the whole volume', 90, BL)]))),
}
BY_STEM = {
 'Two forces act at a point: [F1] N at [t1]°': (L(0, lambda e: vec([(f"{nf(e.F1)} N", e.F1 * cos(rad(e.t1)), e.F1 * sin(rad(e.t1))), (f"{nf(e.F2)} N", e.F2 * cos(rad(e.t2)), e.F2 * sin(rad(e.t2)))])),
   L(0, lambda e: vec([('F1', e.F1 * cos(rad(e.t1)), e.F1 * sin(rad(e.t1))), ('F2', e.F2 * cos(rad(e.t2)), e.F2 * sin(rad(e.t2))), (f"R at {nf(e.ans, 1)}°", e.F1 * cos(rad(e.t1)) + e.F2 * cos(rad(e.t2)), e.F1 * sin(rad(e.t1)) + e.F2 * sin(rad(e.t2)), BL)]))),
 'A force has components F_{x} = [a] kN': (None, L(0, lambda e: vec3(e.a, e.b, e.c, 'force'))),
 'Three parallel downward forces act on a beam': (L(0, lambda e: gbeam(e.x3, [], pts=[(0, e.F1), (e.x2, e.F2), (e.x3, e.F3)])), L(0, lambda e: gbeam(e.x3, [], pts=[(e.ans, e.F1 + e.F2 + e.F3)]))),
 'A distributed load on a beam [L] m long increases': (L(0, lambda e: gbeam(e.L, [], udl=(0, e.L, e.w1), tri=(0, e.L, e.w2))), L(0, lambda e: gbeam(e.L, [], pts=[(e.ans, (e.w1 + e.w2) * e.L / 2)]))),
 'A force with components F_{x} = [Fx] N': (L(0, lambda e: vec([('Fx', e.Fx, 0), ('Fy', 0, e.Fy, JD)], at=(e.x, e.y))), L(0, lambda e: vec([(f"Fx = {nf(e.Fx)} N, arm {nf(e.y)} m", e.Fx, 0), (f"Fy = {nf(e.Fy)} N, arm {nf(e.x)} m", 0, e.Fy, JD)], at=(e.x, e.y)))),
 'A beam rests on a pin at A and a roller at B, [L] m apart': (L(0, lambda e: gbeam(e.L + e.a, [(0, 'pin'), (e.L, 'roller')], pts=[(e.c, e.Q), (e.L + e.a, e.P)])), L(0, lambda e: gbeam(e.L + e.a, [(0, 'pin'), (e.L, 'roller')], pts=[(e.c, e.Q), (e.L + e.a, e.P)], R=[(0, e.Q + e.P - e.ans), (e.L, e.ans)]))),
 'A uniform horizontal bar weighing [Wb] N': (None, L(0, lambda e: fbd([(f"Load {nf(e.W)} N", 270, EM), (f"T = {nf(e.ans, 1)} N", 180 - e.th, JD), ('Pin reaction', 200, SL)], 0, f"Bar: weight {nf(e.Wb)} N acts at mid-length; moments are taken about the pin"))),
 'A [m] kg load hangs from two cables': (L(0, lambda e: cables2(e.al, e.be, e.m * 9.81)), L(0, lambda e: cables2(e.al, e.be, e.m * 9.81, e.ans))),
 'A [W] N block rests on a plane inclined at [th]°': (L(0, lambda e: incline(e.th)), L(0, lambda e: fbd([(f"W = {nf(e.W)} N", 270, EM), (f"N = {nf(e.W * cos(rad(e.th)), 1)} N", 90 + e.th, JD), (f"P = {nf(e.ans, 1)} N", e.th, BL), (f"Friction = {nf(e.mu * e.W * cos(rad(e.th)), 1)} N", 180 + e.th, SL)], e.th))),
 'A [W] N crate is [b|1] m wide': (None, L(0, lambda e: fbd([(f"W = {nf(e.W)} N at mid-width", 270, EM), (f"P = {nf(e.ans)} N at the top", 0, BL), ('Floor reaction at the tipping edge', 90, JD)], 0, f"Moments about the tipping edge: P × {nf(e.h)} = W × {nf(e.b / 2, 2)}"))),
 'A plate is a rectangle [b] mm wide': (L(0, lambda e: shape([[(0, 0), (e.b, 0), (e.b, e.h), (0, e.h)], [(e.b, 0), (e.b + e.bt, 0), (e.b, e.h)]], labels=[(e.b / 2, -e.h * 0.12, f"{nf(e.b)} mm", 'middle'), (e.b + e.bt / 2, -e.h * 0.12, f"{nf(e.bt)} mm", 'middle'), (-e.b * 0.04, e.h / 2, f"{nf(e.h)} mm", 'end')], alt='A rectangle with a right triangle attached to its right side.')),
   L(0, lambda e: shape([[(0, 0), (e.b, 0), (e.b, e.h), (0, e.h)], [(e.b, 0), (e.b + e.bt, 0), (e.b, e.h)]], mark=(e.ans, e.h * 0.42, f"centroid, {nf(e.ans, 2)} mm from the left"), alt='The same plate with its centroid marked.'))),
 'A rectangular plate [W] mm wide and [H] mm high has a [d] mm': (L(0, lambda e: shape(RECT(e.W, e.H), circles=[(e.xh, e.H / 2, e.d / 2, True)], labels=[(e.W / 2, -e.H * 0.14, f"{nf(e.W)} mm", 'middle'), (-e.W * 0.03, e.H / 2, f"{nf(e.H)} mm", 'end'), (e.xh, e.H / 2, f"{nf(e.d)}", 'middle')], alt='A rectangular plate with a circular hole.')),
   L(0, lambda e: shape(RECT(e.W, e.H), circles=[(e.xh, e.H / 2, e.d / 2, True)], mark=(e.ans, e.H / 2, f"centroid, {nf(e.ans, 2)} mm"), alt='The plate with its centroid marked, shifted away from the hole.'))),
 'A channel section has two flanges [b] mm long': (L(0, lambda e: shape([[(0, 0), (e.b, 0), (e.b, e.t), (e.t, e.t), (e.t, e.h - e.t), (e.b, e.h - e.t), (e.b, e.h), (0, e.h)]], labels=[(e.b / 2, -e.h * 0.1, f"{nf(e.b)} mm", 'middle'), (-e.b * 0.08, e.h / 2, f"{nf(e.h)} mm", 'end'), (e.b * 1.05, e.h - e.t / 2, f"{nf(e.t)} mm thick", 'start')], alt='A channel section with its web on the left.')),
   L(0, lambda e: shape([[(0, 0), (e.b, 0), (e.b, e.t), (e.t, e.t), (e.t, e.h - e.t), (e.b, e.h - e.t), (e.b, e.h), (0, e.h)]], mark=(e.ans, e.h / 2, f"centroid, {nf(e.ans, 2)} mm from the back"), alt='The channel with its centroid marked.'))),
 'A hollow rectangular section is [B] mm wide': (L(0, lambda e: shape(RECT(e.B, e.H), holes=[[((e.B - e.bi) / 2, (e.H - e.hi) / 2), ((e.B + e.bi) / 2, (e.H - e.hi) / 2), ((e.B + e.bi) / 2, (e.H + e.hi) / 2), ((e.B - e.bi) / 2, (e.H + e.hi) / 2)]], labels=[(e.B / 2, -e.H * 0.1, f"{nf(e.B)} mm", 'middle'), (-e.B * 0.06, e.H / 2, f"{nf(e.H)} mm", 'end'), (e.B / 2, e.H / 2, f"{nf(e.bi)} × {nf(e.hi)} opening", 'middle')], alt='A hollow rectangular section.')), None),
 'A symmetric I-section has flanges [bf] mm wide': (L(0, lambda e: shape([[(0, 0), (e.bf, 0), (e.bf, e.tf), ((e.bf + e.tw) / 2, e.tf), ((e.bf + e.tw) / 2, e.tf + e.hw), (e.bf, e.tf + e.hw), (e.bf, 2 * e.tf + e.hw), (0, 2 * e.tf + e.hw), (0, e.tf + e.hw), ((e.bf - e.tw) / 2, e.tf + e.hw), ((e.bf - e.tw) / 2, e.tf), (0, e.tf)]], labels=[(e.bf / 2, -(e.hw) * 0.1, f"{nf(e.bf)} mm", 'middle'), (e.bf * 1.04, e.tf / 2, f"{nf(e.tf)} mm", 'start'), ((e.bf + e.tw) / 2 + e.bf * 0.04, e.tf + e.hw / 2, f"web {nf(e.tw)} × {nf(e.hw)} mm", 'start')], alt='A symmetric I-section.')), None),
 'A rectangular section is [b] mm wide and [h] mm deep. What is its radius': (L(0, lambda e: rect(e.b, e.h)), None),
 'A car moving at [v] m/s on a curve of radius [r] m is speeding up': (None, L(0, lambda e: vec([(f"tangential {nf(e.at, 1)}", e.at, 0), (f"normal {nf(e.v * e.v / e.r, 2)}", 0, e.v * e.v / e.r, JD), (f"total {nf(e.ans, 2)} m/s²", e.at, e.v * e.v / e.r, BL)]))),
 'A projectile is launched from level ground at [v] m/s': (L(0, lambda e: projectile(e.v, e.th)), None),
 'A [m] kg person stands on a scale': (None, L(0, lambda e: fbd([(f"W = {nf(e.m * 9.81, 1)} N", 270, EM), (f"N = {nf(e.ans, 1)} N", 90, JD)], 0, f"Net upward force = m a = {nf(e.m * e.a, 1)} N"))),
 'A curve of radius [r] m is banked': (None, L(0, lambda e: fbd([(W, 270, EM), ('N, perpendicular to the road', 90 + e.th, JD)], e.th, 'The horizontal part of N supplies m v² / r; the vertical part balances the weight'))),
 'Masses of [m1] kg and [m2] kg hang': (None, L(0, lambda e: fbd([(f"W = {nf(e.m1 * 9.81, 1)} N", 270, EM), ('T', 90, JD)], 0, f"Heavier mass: accelerates downward at {nf(e.ans, 3)} m/s²"))),
 'A solid uniform disk rolls without slipping': (None, L(0, lambda e: fbd([('W = m g', 270, EM), (N, 90 + e.th, JD), ('Friction, up the slope, which spins the disk', e.th, BL)], e.th))),
 'A car travelling at [v] m/s locks its wheels': (None, L(0, lambda e: fbd([(W, 270, EM), (N, 90, JD), ('Friction = (coefficient) N', 180, BL)], 0, 'Friction is the only force doing work'))),
 'A [m] kg truck climbs a [G]% grade': (None, L(0, lambda e: fbd([('W = m g', 270, EM), (N, 90 + math.degrees(math.atan(e.G / 100)), JD), ('Driving force', math.degrees(math.atan(e.G / 100)), BL)], math.degrees(math.atan(e.G / 100)), 'At steady speed the driving force equals the weight component along the slope'))),
 'A block starts from rest and slides [d] m down': (L(0, lambda e: incline(e.th)), L(0, lambda e: fbd([('W = m g', 270, EM), (N, 90 + e.th, JD), ('Friction', e.th, BL)], e.th))),
 'A simply supported beam spans [L] m. A uniform load of [w] kN/m covers the first': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], udl=(0, e.a, e.w))), L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], udl=(0, e.a, e.w), R=[(0, e.w * e.a * (e.L - e.a / 2) / e.L), (e.L, e.w * e.a * e.a / 2 / e.L)]))),
 'A beam rests on supports A and B, [L] m apart, and overhangs': (L(0, lambda e: gbeam(e.L + e.a, [(0, 'pin'), (e.L, 'roller')], pts=[(e.c, e.P1), (e.L + e.a, e.P2)])), L(0, lambda e: gbeam(e.L + e.a, [(0, 'pin'), (e.L, 'roller')], pts=[(e.c, e.P1), (e.L + e.a, e.P2)], R=[(0, (e.P1 * (e.L - e.c) - e.P2 * e.a) / e.L), (e.L, e.P1 + e.P2 - (e.P1 * (e.L - e.c) - e.P2 * e.a) / e.L)]))),
 'The shear diagram of a beam starts at +[V1] kN': (L(0, lambda e: sheard(e.V1, e.V2, e.d)), L(0, lambda e: sheard(e.V1, e.V2, e.d, e.d * e.V1 / (e.V1 + e.V2), e.ans))),
 'A cantilever beam [L|1] m long carries a uniform load of [w] kN/m over its whole length and a [P] kN': (L(0, lambda e: gbeam(e.L, [], pts=[(e.L, e.P)], udl=(0, e.L, e.w), fix=(1, 0))), None),
 'A simply supported beam spans [L] m and carries a uniform load of [w] kN/m over the whole span. What is the shear': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], udl=(0, e.L, e.w))), L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], udl=(0, e.L, e.w), R=[(0, e.w * e.L / 2), (e.L, e.w * e.L / 2)]))),
 'At a point on a shaft surface there is a bending stress': (None, L(0, lambda e: mohr(e.s, 0, e.t))),
 'A simply supported beam spans [L] m. A clockwise couple': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], mom=(e.L / 2, f"{nf(e.M0)} kN·m"))), None),
 'A simply supported beam spans [L|1] m and carries a triangular load': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], tri=(0, e.L, e.w0))), L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], tri=(0, e.L, e.w0), R=[(0, e.w0 * e.L / 6), (e.L, e.w0 * e.L / 3)]))),
 'A beam [L|1] m long is fixed at one end and simply supported': (L(0, lambda e: gbeam(e.L, [(e.L, 'roller')], udl=(0, e.L, e.w), fix=(1, 0))), None),
 'A cantilever [L|1] m long carries a uniform load': (L(0, lambda e: gbeam(e.L, [], udl=(0, e.L, e.w), fix=(1, 0))), None),
 'A single concentrated load of [P] kN can be anywhere': (None, L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], pts=[(e.L / 2, e.P)], R=[(0, e.P / 2), (e.L, e.P / 2)]))),
 'The toe of a retaining wall is embedded': (L(0, lambda e: wall(e.H)), None), 'A rigid basement wall that cannot move': (L(0, lambda e: wall(e.z)), None), 'A uniform surcharge of [q] kPa': (L(0, lambda e: wall(e.H)), None),
 'A dry soil layer [H] m thick': (L(0, lambda e: incline(e.bt)), None), 'A long slope of cohesionless soil stands at [bt]°': (L(0, lambda e: incline(e.bt)), None),
 'A [W1] N block rests on a [W2] N block': (None, L(0, lambda e: fbd([(f"Pull = {nf(e.ans, 1)} N", 0, BL), (f"Friction from the upper block, {nf(e.m1 * e.W1, 1)} N", 160, JD), (f"Friction from the floor, {nf(e.m2 * (e.W1 + e.W2), 1)} N", 200, SL)], 0, 'Lower block: both friction forces oppose the pull'))),
 'Vectors **A** = [a1]**i** + [a2]**j** and **B** = [b1]**i** + [b2]**j** form': (None, L(0, lambda e: vec([('A', e.a1, e.a2), ('B', e.b1, e.b2), ('A + B', e.a1 + e.b1, e.a2 + e.b2, BL, True)]))),
 'What is the x-component of the unit vector': (None, L(0, lambda e: vec3(e.a, e.b, e.c))),
 'What is the scalar projection of **A**': (None, L(0, lambda e: vec([('A', e.a1, e.a2), ('B', e.b1, e.b2), (f"projection = {nf(e.ans, 2)}", e.ans * e.b1 / math.hypot(e.b1, e.b2), e.ans * e.b2 / math.hypot(e.b1, e.b2), BL, True)]))),
}
# ---------------- further generators ----------------
from author_v import footing, column, rcbeam, hcurve, vcurve, pipe, triangle, tsec
def dam(b, h, F=None, Wt=None):
    k = min(150 / h, 120 / b); x = 200; s = f"<rect x='40' y='{170-h*k:.0f}' width='{x-40}' height='{h*k:.0f}' fill='{BL}' fill-opacity='.25'/><rect x='{x}' y='{170-h*k:.0f}' width='{b*k:.0f}' height='{h*k:.0f}' fill='{RU}' stroke='{SL}' stroke-width='2'/><line x1='20' y1='170' x2='380' y2='170' stroke='{SL}' stroke-width='2'/>"
    s += f"<path d='M{x} {170-h*k:.0f} L{x} 170 L{x-0.45*h*k:.0f} 170 Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>" + T(x + b * k / 2, 186, f"{nf(b)} m") + T(x + b * k + 8, 170 - h * k / 2, f"{nf(h)} m", a='start')
    if F: s += harrow(x - 70, x - 4, 170 - h * k / 3, EM) + T(x - 74, 170 - h * k / 3 + 4, f"{nf(F, 1)} kN/m at h / 3", a='end', c=EM, w='600', z=11) + arrow(x + b * k / 2, 170 - h * k / 2 - 20, 170 - h * k / 2 + 20, BL) + T(x + b * k / 2, 170 - h * k / 2 - 26, f"{nf(Wt, 1)} kN/m", c=BL, w='600', z=11)
    return {'viewBox': '0 0 400 195', 'svg': s, 'alt': f"A rectangular concrete dam {nf(b)} m wide and {nf(h)} m high with water level with its top on one side and a triangular pressure diagram."}
def trap(b, y, z):
    k = min(240 / (b + 2 * z * y * 1.3), 110 / (y * 1.3)); cx = 200; yb = 150; top = lambda d: (cx - (b / 2 + z * d) * k, cx + (b / 2 + z * d) * k, yb - d * k)
    l, r, yt = top(y * 1.3); wl, wr, yw = top(y)
    s = f"<path d='M{l:.0f} {yt:.0f} L{cx-b/2*k:.0f} {yb} L{cx+b/2*k:.0f} {yb} L{r:.0f} {yt:.0f}' fill='none' stroke='{SL}' stroke-width='3'/><path d='M{wl:.0f} {yw:.0f} L{cx-b/2*k:.0f} {yb} L{cx+b/2*k:.0f} {yb} L{wr:.0f} {yw:.0f} Z' fill='{BL}' fill-opacity='.3'/>"
    s += T(cx, yb + 16, f"{nf(b)} m") + T(cx, (yw + yb) / 2 + 4, f"{nf(y)} m deep") + T(wr + 10, yw + 20, f"{nf(z)} : 1", a='start', z=11)
    return {'viewBox': '0 0 400 175', 'svg': s, 'alt': f"A trapezoidal channel with a {nf(b)} m bottom, side slopes of {nf(z)} horizontal to 1 vertical, flowing {nf(y)} m deep."}
def pile(d, L, lab=''):
    s = f"<rect x='40' y='40' width='320' height='130' fill='{CR}'/><line x1='40' y1='40' x2='360' y2='40' stroke='{SL}' stroke-width='3'/><rect x='188' y='24' width='24' height='128' fill='{RU}' stroke='{SL}' stroke-width='2'/>" + arrow(200, 0, 22) + ''.join(arrow(x, 136 - 26 * i, 112 - 26 * i, BL, 2) for i in range(4) for x in (178, 222))
    s += arrow(200, 176, 154, JD) + T(232, 100, 'Skin friction', a='start', c=BL, z=11) + T(210, 176, 'End bearing', a='start', c=JD, z=11) + f"<line x1='120' y1='40' x2='120' y2='152' stroke='{SL}'/>" + T(112, 100, f"{nf(L)} m", a='end') + T(214, 18, lab or f"{nf(d)} m wide", a='start', z=11)
    return {'viewBox': '0 0 400 185', 'svg': s, 'alt': f"A pile {nf(L)} m long carrying load by skin friction along its shaft and end bearing at its tip."}
def layer(H, note, double=True):
    s = f"<rect x='40' y='20' width='320' height='34' fill='{CR}'/><rect x='40' y='54' width='320' height='70' fill='{LG}' stroke='{JD}' stroke-width='2'/><rect x='40' y='124' width='320' height='34' fill='{CR if double else RU}'/>" + T(200, 42, 'Sand (drains freely)', z=11) + T(200, 146, 'Sand (drains freely)' if double else 'Rock (no drainage)', z=11) + T(200, 86, f"Clay, {nf(H)} thick", w='600') + T(200, 104, note, z=11)
    s += arrow(120, 76, 58, BL, 2) + (arrow(120, 102, 120, BL, 2) if double else '')
    return {'viewBox': '0 0 400 172', 'svg': s, 'alt': f"A clay layer {nf(H)} thick between two other layers; {note}."}
def offsets(dx, o):
    n = len(o); k = 110 / max(o); X = lambda i: 60 + 280 * i / (n - 1)
    s = f"<path d='M60 150 " + ' '.join(f"L{X(i):.0f} {150-v*k:.0f}" for i, v in enumerate(o)) + f" L340 150 Z' fill='{LG}' stroke='{JD}' stroke-width='2'/><line x1='40' y1='150' x2='360' y2='150' stroke='{SL}' stroke-width='2'/>"
    s += ''.join(f"<line x1='{X(i):.0f}' y1='150' x2='{X(i):.0f}' y2='{150-v*k:.0f}' stroke='{SL}' stroke-dasharray='4 3'/>" + T(X(i), 150 - v * k - 6, nf(v), z=11) for i, v in enumerate(o)) + dim(X(0), X(1), 160, f"{nf(dx)} m")
    return {'viewBox': '0 0 400 185', 'svg': s, 'alt': 'Offsets of ' + nf(list(o)) + f" m from a baseline to a curved boundary at {nf(dx)} m intervals."}
def sag(g1, g2, L):
    s = f"<path d='M40 50 Q200 150 360 64' fill='none' stroke='{SL}' stroke-width='3'/><line x1='40' y1='50' x2='200' y2='150' stroke='{BL}' stroke-dasharray='6 4'/><line x1='200' y1='150' x2='360' y2='64' stroke='{BL}' stroke-dasharray='6 4'/>" + T(40, 40, 'PVC') + T(360, 54, 'PVT') + T(200, 166, 'PVI') + T(96, 112, f"{nf(g1)}%", c=BL) + T(304, 122, f"+{nf(g2)}%", c=BL) + dim(40, 360, 178, f"{nf(L)} ft")
    return {'viewBox': '0 0 400 200', 'svg': s, 'alt': f"A sag vertical curve {nf(L)} ft long joining a {nf(g1)}% grade to a +{nf(g2)}% grade."}
def ptruss(p, h, lab=''):
    x = [60 + 70 * i for i in range(5)]; s = f"<path d='M60 130 L340 130 M60 50 L340 50' stroke='{SL}' stroke-width='4'/>" + ''.join(f"<line x1='{a}' y1='50' x2='{a}' y2='130' stroke='{SL}' stroke-width='3'/>" for a in x) + ''.join(f"<line x1='{x[i]}' y1='50' x2='{x[i+1]}' y2='130' stroke='{SL}' stroke-width='3'/>" for i in range(4))
    s += f"<line x1='165' y1='30' x2='165' y2='150' stroke='{EM}' stroke-width='2' stroke-dasharray='7 4'/>" + T(165, 24, 'cut', c=EM, w='600', z=11) + dim(130, 200, 150, f"{nf(p)} m" if p else 'panel') + f"<line x1='356' y1='50' x2='356' y2='130' stroke='{SL}'/>" + T(362, 94, f"{nf(h)} m", a='start') + (T(200, 184, lab, c=BL, w='600', z=11) if lab else '')
    return {'viewBox': '0 0 420 192', 'svg': s, 'alt': f"A parallel-chord truss {nf(h)} m deep with a vertical cut through one panel."}
def drum(wrap, T2, T1=None):
    a = rad(wrap); s = f"<circle cx='200' cy='90' r='50' fill='{RU}' stroke='{SL}' stroke-width='2'/><path d='M150 90 A50 50 0 {1 if wrap > 180 else 0} 1 {200+50*cos(math.pi-a):.0f} {90-50*sin(math.pi-a):.0f}' fill='none' stroke='{JD}' stroke-width='5'/>" + arrow(150, 92, 170, EM) + T(140, 168, f"slack side {nf(T2)} N", a='end', c=EM, w='600', z=11) + T(200, 94, f"wrap {nf(wrap)}°", z=11)
    return {'viewBox': '0 0 400 185', 'svg': s + (T(200, 22, f"tight side {nf(T1, 1)} N", c=BL, w='600') if T1 else ''), 'alt': f"A rope wrapped {nf(wrap)}° around a fixed drum with {nf(T2)} N on the slack side."}
def gate2(a, h, ycp=None, circ=None):
    k = 120 / (a + h); yt = 30 + a * k
    s = f"<rect x='60' y='30' width='150' height='{(a+h)*k+10:.0f}' fill='{BL}' fill-opacity='.25'/><line x1='40' y1='30' x2='210' y2='30' stroke='{BL}' stroke-width='2'/><line x1='210' y1='14' x2='210' y2='{40+(a+h)*k:.0f}' stroke='{SL}' stroke-width='3'/><rect x='205' y='{yt:.0f}' width='10' height='{h*k:.0f}' fill='{JD}'/>"
    s += f"<path d='M205 {yt:.0f} L{205-a*k*0.5:.0f} {yt:.0f} L{205-(a+h)*k*0.5:.0f} {yt+h*k:.0f} L205 {yt+h*k:.0f} Z' fill='{LG}' stroke='{JD}'/>" + f"<line x1='240' y1='30' x2='240' y2='{yt:.0f}' stroke='{SL}'/>" + T(248, 30 + a * k / 2 + 4, f"{nf(a)} m", a='start') + T(248, yt + h * k / 2 + 4, (f"{nf(h)} m diameter cover" if circ else f"gate {nf(h)} m tall"), a='start')
    if ycp: s += harrow(120, 203, 30 + ycp * k, EM) + T(116, 34 + ycp * k, f"F at {nf(ycp, 3)} m", a='end', c=EM, w='600', z=11)
    return {'viewBox': f"0 0 400 {50+(a+h)*k:.0f}", 'svg': s, 'alt': f"A vertical {'circular cover' if circ else 'gate'} {nf(h)} m high whose top is {nf(a)} m below the water surface, with the pressure diagram on it."}
CIRC = lambda do, di=0: dict(polys=[[(-do / 2, -do / 2), (-do / 2, -do / 2)]], circles=[(0, 0, do / 2, False)] + ([(0, 0, di / 2, True)] if di else []))
def ring(do, di=0): return shape([[(-do * 0.5, -do * 0.5), (do * 0.5, -do * 0.5), (do * 0.5, -do * 0.5)]], circles=[(0, 0, do / 2, False)] + ([(0, 0, di / 2, True)] if di else []), labels=[(0, -do * 0.62, f"{nf(do)} mm outside" + (f", {nf(di)} mm inside" if di else ' diameter'), 'middle')], alt=f"A {'hollow ' if di else ''}circular section {nf(do)} mm in diameter" + (f" with a {nf(di)} mm bore." if di else '.'))
ENDS = {0.5: ('Fixed', 'Fixed'), 0.7: ('Pinned', 'Fixed'), 2.0: ('Free', 'Fixed'), 1.0: ('Pinned', 'Pinned')}
BY_ID.update({
 'statics-0008': (None, L(0, lambda e: fbd([(f"Reaction = {nf(e.P / 2, 1)} kN", 90, BL), ('Sloping member', math.degrees(math.atan(e.h / (e.span / 2))), EM), ('Bottom chord', 0, JD)], 0, 'Free-body diagram of the support joint; unknown member forces drawn as tension'))),
 'statics-0009': (None, L(0, lambda e: fbd([(f"Reaction = {nf(e.P / 2, 1)} kN", 90, BL), ('Sloping member', math.degrees(math.atan(e.h / (e.span / 2))), EM), ('Bottom chord', 0, JD)], 0, 'Free-body diagram of the support joint; unknown member forces drawn as tension'))),
 'dynamics-0010': (None, L(0, lambda e: fbd([('Weight = m g', 270, EM), ('Cable force = m g at constant speed', 90, JD)], 0, 'Constant speed means zero net force'))),
 'mechmat-0009': (L(0, lambda e: ring(e.d)), None), 'mechmat-0012': (None, L(0, lambda e: mohr(e.s1, e.s2, 0))),
 'geotech-0014': (L(0, lambda e: footing(0, 0, e.D)), None), 'geotech-0016': (L(0, lambda e: pile(e.s, e.L, f"{nf(e.s)} m square")), None), 'geotech-0018': (L(0, lambda e: layer(f"{nf(e.H)} m", f"effective stress rises from {nf(e.p1)} to {nf(e.p2)} kPa")), None),
 'geotech-0019': (L(0, lambda e: layer(f"{nf(e.H)} m", 'drains to the top and the bottom')), None), 'geotech-0027': (L(0, lambda e: footing(e.B, e.P)), None),
 'structural-0018': (L(0, lambda e: rect(e.b, e.b * 1.8)), None), 'structural-0019': (L(0, lambda e: rect(e.b, e.d)), None), 'structural-0020': (L(0, lambda e: rect(e.sd0, e.sd0)), None),
 'surveying-0012': (L(0, lambda e: offsets(e.dx, [e.o0, e.o1, e.o2, e.o3, e.o4])), None), 'water-0027': (L(0, lambda e: dam(e.b, e.h)), L(0, lambda e: dam(e.b, e.h, 0.5 * 9.81 * e.h ** 2, 23.5 * e.b * e.h))),
})
BY_STEM.update({
 'A parallel-chord truss is [h] m deep': (L(0, lambda e: ptruss(0, e.h)), L(0, lambda e: ptruss(0, e.h, f"Moments about the top joint: bottom chord = {nf(e.M)} / {nf(e.h)} = {nf(e.ans, 1)} kN"))),
 'A parallel-chord truss has panels [p] m long': (L(0, lambda e: ptruss(e.p, e.h)), L(0, lambda e: ptruss(e.p, e.h, f"Vertical part of the diagonal = {nf(e.V)} kN, so the diagonal carries {nf(e.ans, 2)} kN"))),
 'A hollow circular shaft has an outside diameter': (L(0, lambda e: ring(e.do, e.di)), None), 'A hollow shaft with an outside diameter': (L(0, lambda e: ring(e.do, e.di)), None),
 'A rope passes over a fixed drum': (L(0, lambda e: drum(e.wrap, e.T2)), L(0, lambda e: drum(e.wrap, e.T2, e.ans))),
 'A rectangular beam [b] mm wide and [h] mm deep carries a shear': (L(0, lambda e: rect(e.b, e.h)), None),
 'A square column [b] mm on a side carries a compressive load': (L(0, lambda e: shape(RECT(e.b, e.b), mark=(min(e.b / 2 + e.ec, e.b * 1.6), e.b / 2, f"load, {nf(e.ec)} mm from the centroid"), labels=[(e.b / 2, -e.b * 0.12, f"{nf(e.b)} mm square", 'middle')], alt='A square column section with the load point offset from the centroid along one axis.')), None),
 'A bar carries a uniaxial tensile stress': (None, L(0, lambda e: mohr(e.s, 0, 0))),
 'A simply supported beam spans [L] m and carries a uniform load of [w] kN/m. Its flexural rigidity': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], udl=(0, e.L, e.w))), None),
 'A simply supported steel beam (E = 200 GPa) spans': (L(0, lambda e: gbeam(e.L, [(0, 'pin'), (e.L, 'roller')], udl=(0, e.L, e.w))), None),
 'A steel column (E = 200 GPa) [L] m long is [ends]': (L(0, lambda e: column(e.L, e.K, *ENDS.get(e.K, ('Pinned', 'Pinned')))), None),
 'A singly reinforced beam is [b] mm wide with an effective depth': (L(0, lambda e: rcbeam(e.b, e.d, e.As)), L(0, lambda e: rcbeam(e.b, e.d, e.As, e.As * 420 / (0.85 * e.fc * e.b)))),
 'A rectangular concrete beam is [b] mm wide and [h] mm deep overall': (L(0, lambda e: rect(e.b, e.h)), None),
 'A vertical rectangular gate is [h|1] m tall': (L(0, lambda e: gate2(e.a, e.h)), L(0, lambda e: gate2(e.a, e.h, e.ans))),
 'A circular access cover [d|1] m in diameter': (L(0, lambda e: gate2(e.hc - e.d / 2, e.d, None, True)), None),
 'A venturi meter in a [d1] mm water pipe': (L(0, lambda e: pipe(e.d1, e.d2)), None),
 'A strip footing [B|1] m wide is founded': (L(0, lambda e: footing(e.B, 0, e.D)), None), 'A strip footing [B|1] m wide carries [P] kN per metre and a moment of [M] kN·m per metre. Using': (L(0, lambda e: footing(e.B, e.P)), None),
 'A round pile [d|1] m in diameter': (L(0, lambda e: pile(e.d, e.L, f"{nf(e.d)} m diameter")), None),
 'Two columns [s] m apart carry': (None, L(0, lambda e: gbeam(e.ans, [], pts=[(e.a, e.P1), (e.a + e.s, e.P2)], R=[(e.ans / 2, e.P1 + e.P2)]))),
 'A consolidation test specimen [H] mm thick': (L(0, lambda e: layer(f"{nf(e.H)} mm", 'drains from both faces, so the drainage path is half the thickness')), None),
 'An overconsolidated clay layer [H] m thick': (L(0, lambda e: layer(f"{nf(e.H)} m", f"effective stress rises from {nf(e.s0)} to {nf(e.sf)} kPa")), None),
 'A trapezoidal roadside channel': (L(0, lambda e: trap(e.b, e.y, e.z)), None),
 'A concrete gravity dam with a rectangular section is [b|1] m wide': (L(0, lambda e: dam(e.b, e.h)), L(0, lambda e: dam(e.b, e.h, 0.5 * 9.81 * e.h ** 2, 23.5 * e.b * e.h))),
 'Offsets from a baseline to a curved boundary': (L(0, lambda e: offsets(e.dx, [e.o0, e.o1, e.o2, e.o3, e.o4])), None),
 'A triangular parcel has sides of': (L(0, lambda e: triangle(e.a, e.b, math.degrees(math.acos((e.a ** 2 + e.b ** 2 - e.c ** 2) / (2 * e.a * e.b))))), None),
 'A roadway cut on level ground': (L(0, lambda e: shape([[(0, 0), (e.b, 0), (e.b + e.s * e.d, e.d), (-e.s * e.d, e.d)]], labels=[(e.b / 2, -e.d * 0.16, f"{nf(e.b)} m", 'middle'), (e.b / 2, e.d / 2, f"{nf(e.d)} m deep", 'middle'), (e.b + e.s * e.d, e.d * 0.4, f"{nf(e.s)} : 1", 'start')], alt='A level-section cut: a trapezoid wider at the top than at the base.')), None),
 'A horizontal curve has a radius of [R] ft and a deflection angle of [I]°. What is its middle': (L(0, lambda e: hcurve(e.R, e.I)), None),
 'A sag vertical curve [L] ft long': (L(0, lambda e: sag(e.g1, e.g2, e.L)), None),
 'A vertical curve [L] ft long joins': (L(0, lambda e: vcurve(e.g1, e.g2, e.L) if e.g1 > e.g2 else sag(e.g1, e.g2, e.L)), None),
 'A [W] N crate is [b|1] m wide': (L(0, lambda e: shape(RECT(e.b, e.h), labels=[(e.b / 2, -e.h * 0.12, f"{nf(e.b)} m", 'middle'), (-e.b * 0.06, e.h / 2, f"{nf(e.h)} m", 'end'), (e.b * 1.05, e.h, 'P', 'start'), (e.b / 2, e.h / 2, f"{nf(e.W)} N", 'middle')], unit='m', alt='A crate pushed horizontally at its top edge.')), BY_STEM['A [W] N crate is [b|1] m wide'][1]),
})
def bmd(L, kind, M, unit='kN·m'):
    """Bending moment diagram on a baseline: 'simple' (sagging parabola), 'cant' (zero at the free end), 'fixed', 'propped'."""
    X = lambda t: 60 + 280 * t; y0 = 70; k = 46; pts = [i / 40 for i in range(41)]
    f = {'simple': lambda t: 4 * t * (1 - t), 'cant': lambda t: -(1 - t) ** 2, 'cantl': lambda t: -(1 - t), 'fixed': lambda t: 1.5 * (4 * t * (1 - t)) - 1, 'propped': lambda t: -(1 - t) * (1 - 4 * t)}[kind]
    s = f"<path d='M60 {y0} " + ' '.join(f"L{X(t):.0f} {y0 + f(t) * k:.0f}" for t in pts) + f" L340 {y0} Z' fill='{LG}' stroke='{JD}' stroke-width='2'/><line x1='40' y1='{y0}' x2='360' y2='{y0}' stroke='{SL}' stroke-width='2'/>"
    where = {'simple': (200, y0 + k + 16, 'at midspan'), 'cant': (64, y0 - k - 8, 'at the fixed support'), 'cantl': (64, y0 - k - 8, 'at the fixed support'), 'fixed': (64, y0 - k - 8, 'at each fixed end'), 'propped': (64, y0 - k - 8, 'at the fixed end')}[kind]
    s += T(where[0], where[1], f"{nf(M)} {unit} {where[2]}", a='middle' if kind == 'simple' else 'start', c=EM, w='600') + dim(60, 340, 138, f"{nf(L)} m") + T(200, 172, 'Bending moment along the beam (sagging plotted downward)', z=11)
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"Bending moment diagram for a {nf(L)} m beam with a largest moment of {nf(M)} {unit} {where[2]}."}
def ssd(react, brake, unit='ft'):
    tot = react + brake; a = 60 + 280 * react / tot
    s = f"<rect x='60' y='60' width='{a-60:.0f}' height='26' fill='{LG}' stroke='{JD}' stroke-width='2'/><rect x='{a:.0f}' y='60' width='{340-a:.0f}' height='26' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + T((60 + a) / 2, 50, 'Reaction', c=JD, w='600') + T((a + 340) / 2, 50, 'Braking', w='600') + T((60 + a) / 2, 104, f"{nf(react, 1)} {unit}", z=11) + T((a + 340) / 2, 104, f"{nf(brake, 1)} {unit}", z=11) + dim(60, 340, 122, f"{nf(tot, 1)} {unit} in total")
    return {'viewBox': '0 0 400 150', 'svg': s, 'alt': f"Stopping distance split into {nf(react, 1)} {unit} travelled during the driver's reaction and {nf(brake, 1)} {unit} while braking."}
def jump(y1, y2):
    k = 90 / y2; s = f"<line x1='30' y1='140' x2='370' y2='140' stroke='{SL}' stroke-width='3'/><path d='M30 140 L30 {140-y1*k:.0f} L170 {140-y1*k:.0f} Q200 {140-y2*k-14:.0f} 230 {140-y2*k:.0f} L370 {140-y2*k:.0f} L370 140 Z' fill='{BL}' fill-opacity='.3' stroke='{BL}' stroke-width='2'/>"
    s += harrow(50, 110, 140 - y1 * k / 2, EM) + T(100, 140 - y1 * k - 8, f"{nf(y1, 2)} m, fast and shallow", z=11) + T(300, 140 - y2 * k - 8, f"{nf(y2, 2)} m, slow and deep", z=11) + T(200, 160, 'Hydraulic jump', w='600', z=11)
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': f"A hydraulic jump: flow {nf(y1, 2)} m deep rises abruptly to {nf(y2, 2)} m."}
def tank2(h1, sg, h2, p=None):
    k = 110 / (h1 + h2); s = f"<rect x='70' y='30' width='150' height='{h1*k:.0f}' fill='{CR}' stroke='{SL}'/><rect x='70' y='{30+h1*k:.0f}' width='150' height='{h2*k:.0f}' fill='{BL}' fill-opacity='.3' stroke='{SL}'/><path d='M70 30 L70 {30+(h1+h2)*k:.0f} L220 {30+(h1+h2)*k:.0f} L220 30' fill='none' stroke='{SL}' stroke-width='3'/>"
    s += T(145, 30 + h1 * k / 2 + 4, f"Oil, SG {nf(sg, 2)}, {nf(h1)} m") + T(145, 30 + h1 * k + h2 * k / 2 + 4, f"Water, {nf(h2)} m")
    if p: s += f"<path d='M250 30 L250 {30+(h1+h2)*k:.0f} L{250+90:.0f} {30+(h1+h2)*k:.0f} L{250+90*sg*h1/(sg*h1+h2):.0f} {30+h1*k:.0f} Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>" + T(300, 30 + (h1 + h2) * k + 16, f"{nf(p, 2)} kPa at the floor", c=EM, w='600', z=11) + T(300, 22, 'Pressure', z=11)
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': f"A tank with {nf(h1)} m of oil floating on {nf(h2)} m of water" + (', with the pressure diagram, which steepens in the denser water.' if p else '.')}
def fpress(B, qmax, qmin):
    k = 60 / qmax; s = f"<rect x='180' y='10' width='40' height='40' fill='{RU}' stroke='{SL}' stroke-width='2'/><rect x='100' y='50' width='200' height='22' fill='{CR}' stroke='{SL}' stroke-width='2'/><path d='M100 76 L300 76 L300 {76+qmax*k:.0f} L100 {76+max(qmin,0)*k:.0f} Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>"
    s += T(306, 80 + qmax * k, f"{nf(qmax, 1)} kPa", a='start', c=EM, w='600') + T(94, 80 + max(qmin, 0) * k, f"{nf(qmin, 1)} kPa", a='end', c=EM, w='600') + dim(100, 300, 156, f"{nf(B)} m")
    return {'viewBox': '0 0 400 178', 'svg': s, 'alt': f"Bearing pressure under an eccentrically loaded footing {nf(B)} m wide, varying from {nf(qmin, 1)} to {nf(qmax, 1)} kPa."}
from author_v import cashflow
_money = lambda v: '$' + nf(v)
BY_ID.update({
 'structural-0006': (None, L(0, lambda e: bmd(e.L, 'cantl', e.P * e.L))), 'structural-0013': (BY_ID['structural-0013'][0], L(0, lambda e: bmd(e.L, 'fixed', e.w * e.L ** 2 / 12))),
 'transport-0001': (None, L(0, lambda e: ssd(1.47 * e.V * 2.5, e.ans - 1.47 * e.V * 2.5))), 'fluids-0015': (L(0, lambda e: tank2(e.h1, e.sg, e.h2)), L(0, lambda e: tank2(e.h1, e.sg, e.h2, e.ans))),
 'geotech-0027': (BY_ID['geotech-0027'][0], L(0, lambda e: fpress(e.B, e.ans, e.P / e.B * (1 - 6 * (e.M / e.P) / e.B)))), 'water-0029': (None, L(0, lambda e: jump(e.y1, e.ans))),
 'econ-0001': (L(0, lambda e: cashflow(min(e.n, 30), P=_money(e.P), F='F = ?')), None), 'econ-0002': (L(0, lambda e: cashflow(e.n, P=_money(e.P), A='A = ?')), None), 'econ-0007': (L(0, lambda e: cashflow(min(e.n, 30), P='P = ?', F=_money(e.Fv))), None),
 'surveying-0013': (None, L(0, lambda e: vec([('A to B', e.EB - e.EA, e.NB - e.NA), ('departure', e.EB - e.EA, 0, BL, True), ('latitude', 0, e.NB - e.NA, JD, True)]))),
})
BY_STEM.update({
 'A cantilever beam [L|1] m long carries a uniform load of [w] kN/m over its whole length and a [P] kN': (BY_STEM['A cantilever beam [L|1] m long carries a uniform load of [w] kN/m over its whole length and a [P] kN'][0], L(0, lambda e: bmd(e.L, 'cant', e.ans))),
 'A beam [L|1] m long is fixed at one end and simply supported': (BY_STEM['A beam [L|1] m long is fixed at one end and simply supported'][0], L(0, lambda e: bmd(e.L, 'propped', e.ans))),
 'A vehicle travels at [V] mph on a [G]% grade': (None, L(0, lambda e: ssd(1.47 * e.V * 2.5, e.ans - 1.47 * e.V * 2.5))),
 'The toe of a retaining wall is embedded': (BY_STEM['The toe of a retaining wall is embedded'][0], L(0, lambda e: wall(e.H, e.ans))),
 'What is the present worth of $[A] received': (L(0, lambda e: cashflow(e.n, P='P = ?', A=_money(e.A))), None), 'An agency needs $[F] in [n] years': (L(0, lambda e: cashflow(e.n, A='A = ?', F=_money(e.F))), None),
 'A project costs $[C] now, returns': (L(0, lambda e: cashflow(e.n, P=_money(e.C) + ' cost', A=_money(e.A), F=_money(e.Sv) + ' salvage')), None),
 'Point A is at N [NA|2], E [EA|2]': (None, L(0, lambda e: vec([('A to B', e.EB - e.EA, e.NB - e.NA), ('departure', e.EB - e.EA, 0, BL, True), ('latitude', 0, e.NB - e.NA, JD, True)]))),
 'A total station with a height of instrument': (None, L(0, lambda e: vec([('sloping', e.S * cos(rad(e.va)), e.S * sin(rad(e.va))), ('level', e.S * cos(rad(e.va)), 0, BL, True)]))),
 'A line passes through the points ([x1], [y1])': (None, L(0, lambda e: vec([('given line', e.x2 - e.x1, e.y2 - e.y1), ('at 90°', -(e.y2 - e.y1), e.x2 - e.x1, BL, True)]))),
 'A rectangular channel carries [q|1] m^{3}/s per metre': (None, None),
})
# ---- further explanation figures for questions that involve forces ----
def bar(segs, forces=(), walls=(True, False), note=''):
    """A straight bar. segs: (label, share of length). forces: (position 0 to 1, label, +1 to the right or -1 to the left, colour)."""
    x0, x1, y = 90, 310, 86; X = lambda t: x0 + (x1 - x0) * t; s = ''; t = 0
    for i, (lab, fr) in enumerate(segs): s += f"<rect x='{X(t):.0f}' y='{y-11}' width='{(x1-x0)*fr:.0f}' height='22' fill='{CR if i % 2 == 0 else LG}' stroke='{SL}' stroke-width='2'/>" + T(X(t + fr / 2), y + 30, lab, z=11); t += fr
    for k, w in enumerate(walls):
        if w: s += f"<rect x='{(x0 - 14) if k == 0 else x1}' y='{y-36}' width='14' height='72' fill='{RU}' stroke='{SL}' stroke-width='2'/>"
    for n, (xf, lab, d, col) in enumerate(forces):
        yy = y - 24 - 16 * (n % 3); s += harrow(X(xf), X(xf) + 44 * d, yy, col or EM) + T(X(xf) + 50 * d, yy + 4, lab, a='start' if d > 0 else 'end', c=col or EM, w='600', z=11)
    return {'viewBox': '0 0 400 150', 'svg': s + (T(200, 142, note, z=11) if note else ''), 'alt': 'A bar' + (' held between rigid supports' if all(walls) else '') + ' with ' + '; '.join(f[1] for f in forces) + '.' + (' ' + note + '.' if note else '')}
def dshear(P, tau=None, u='kN'):
    s = f"<rect x='60' y='46' width='190' height='16' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='60' y='98' width='190' height='16' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='170' y='70' width='180' height='20' fill='{LG}' stroke='{SL}' stroke-width='2'/><rect x='200' y='34' width='18' height='92' fill='{JD}' stroke='{SL}' stroke-width='2'/>"
    s += f"<line x1='180' y1='66' x2='240' y2='66' stroke='{BL}' stroke-width='2' stroke-dasharray='6 4'/><line x1='180' y1='94' x2='240' y2='94' stroke='{BL}' stroke-width='2' stroke-dasharray='6 4'/>"
    s += harrow(350, 392, 80) + T(392, 68, f"{nf(P)} {u}", a='end', c=EM, w='600') + harrow(60, 18, 54) + harrow(60, 18, 106) + T(18, 42, f"{nf(P / 2)} {u}", a='start', c=EM, w='600') + T(18, 126, f"{nf(P / 2)} {u}", a='start', c=EM, w='600')
    s += T(250, 150, 'Two shear planes (dashed): each carries half the force', c=BL, z=11)
    return {'viewBox': '0 0 400 160', 'svg': s, 'alt': f"A pin through a clevis in double shear. The middle plate pulls with {nf(P)} {u} and each outer plate with {nf(P / 2)} {u}, so the pin is cut on two planes."}
def bearing(d, t, P):
    s = f"<rect x='70' y='70' width='260' height='34' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='182' y='36' width='36' height='102' fill='{RU}' stroke='{SL}' stroke-width='2'/><rect x='182' y='70' width='36' height='34' fill='{LG}' stroke='{JD}' stroke-width='2'/>"
    s += harrow(218, 290, 52) + T(296, 56, f"{nf(P)} kN", a='start', c=EM, w='600') + dim(182, 218, 150, f"bolt {nf(d)} mm") + T(62, 91, f"plate {nf(t)} mm", a='end', z=11) + T(200, 22, f"Bearing area = {nf(d)} × {nf(t)} = {nf(d * t)} mm²", c=JD, w='600', z=11)
    return {'viewBox': '0 0 400 168', 'svg': s, 'alt': f"A {nf(d)} mm bolt passing through a {nf(t)} mm plate. The bearing area is the bolt diameter times the plate thickness, {nf(d * t)} mm²."}
def vessel(hoop, ax):
    s = f"<rect x='70' y='40' width='260' height='90' rx='44' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='182' y='67' width='36' height='36' fill='{LG}' stroke='{JD}' stroke-width='2'/>"
    s += arrow(200, 67, 34, EM) + arrow(200, 103, 136, EM) + harrow(218, 262, 85, BL) + harrow(182, 138, 85, BL) + T(200, 24, f"Hoop stress {nf(hoop, 1)} MPa (around the tank)", c=EM, w='600', z=11) + T(200, 156, f"Axial stress {nf(ax, 1)} MPa (along the tank), half the hoop stress", c=BL, w='600', z=11)
    return {'viewBox': '0 0 400 166', 'svg': s, 'alt': f"A small piece of the wall of a pressurised cylinder. Hoop stress of {nf(hoop, 1)} MPa acts around the tank and axial stress of {nf(ax, 1)} MPa acts along it."}
def lever(P, a, b, F, u='mm'):
    k = 260 / (a + b); px = 70 + b * k
    s = f"<rect x='70' y='78' width='260' height='12' fill='{CR}' stroke='{SL}' stroke-width='2'/><path d='M{px:.0f} 90 L{px-12:.0f} 112 L{px+12:.0f} 112 Z' fill='#FFFFFF' stroke='{SL}' stroke-width='2'/>" + arrow(330, 30, 76) + arrow(70, 30, 76, BL)
    s += T(330, 22, f"Hand {nf(P)} N", a='end', c=EM, w='600') + T(70, 22, f"Wire pushes back {nf(F)} N", a='start', c=BL, w='600') + dim(70, px, 130, f"{nf(b)} {u}") + dim(px, 330, 130, f"{nf(a)} {u}") + T(px + 18, 108, 'pivot', a='start', z=11)
    return {'viewBox': '0 0 400 164', 'svg': s, 'alt': f"One handle as a lever about the pivot: a hand force of {nf(P)} N at {nf(a)} {u} balances a jaw force of {nf(F)} N at {nf(b)} {u}."}
def fcs(F, d, M):
    s = f"<line x1='60' y1='110' x2='340' y2='110' stroke='{RU}' stroke-width='3'/><circle cx='130' cy='110' r='5' fill='{SL}'/>" + T(130, 132, 'O') + arr(270, 40, 270, 106, SL, 2, True) + T(278, 50, 'original position', a='start', z=11) + arrow(130, 40, 104) + T(122, 50, f"{nf(F)} N", a='end', c=EM, w='600')
    s += f"<path d='M106 96 A28 28 0 1 1 158 96' fill='none' stroke='{BL}' stroke-width='3'/><path d='M158 102 L150 88 L166 90 Z' fill='{BL}'/>" + T(168, 76, f"{nf(M)} N·m clockwise", a='start', c=BL, w='600') + dim(130, 270, 150, f"{nf(d)} m")
    return {'viewBox': '0 0 400 170', 'svg': s, 'alt': f"The {nf(F)} N force moved to point O, together with a clockwise moment of {nf(M)} N·m that makes up for moving it {nf(d)} m."}
def press(h, pr):
    s = f"<rect x='60' y='30' width='150' height='120' fill='{BL}' fill-opacity='.3'/><path d='M60 30 L60 150 L210 150 L210 30' fill='none' stroke='{SL}' stroke-width='3'/><line x1='60' y1='30' x2='210' y2='30' stroke='{BL}' stroke-width='2'/>"
    s += f"<path d='M250 30 L250 150 L350 150 Z' fill='{LG}' stroke='{JD}' stroke-width='2'/>" + T(52, 94, f"{nf(h)} m", a='end') + T(300, 168, f"{nf(pr, 1)} kPa at the bottom", c=EM, w='600', z=11) + T(250, 22, 'zero at the surface', a='start', z=11)
    return {'viewBox': '0 0 400 176', 'svg': s, 'alt': f"Water {nf(h)} m deep with its pressure diagram: zero at the surface, rising in a straight line to {nf(pr, 1)} kPa at the bottom."}
def jet(F, th=None):
    s = harrow(40, 180, 90, BL, 6) + T(100, 76, 'Jet', c=BL, w='600')
    if th is None: s += f"<rect x='186' y='30' width='12' height='120' fill='{RU}' stroke='{SL}' stroke-width='2'/>" + harrow(200, 290, 90) + T(296, 94, f"{nf(F, 1)} N on the plate", a='start', c=EM, w='600', z=11) + T(200, 168, 'The plate removes all of the jet\'s forward momentum', z=11)
    else:
        a = rad(th); s += f"<path d='M180 90 Q230 90 {230 + 60 * cos(a):.0f} {90 - 60 * sin(a):.0f}' fill='none' stroke='{SL}' stroke-width='4'/>" + arr(232 + 62 * cos(a), 88 - 62 * sin(a), 232 + 120 * cos(a), 88 - 120 * sin(a), BL, 6) + harrow(206, 286, 120) + T(206, 140, f"{nf(F, 1)} N on the vane, along the jet", a='start', c=EM, w='600', z=11) + T(200, 168, f"Turned through {nf(th)}°: the forward momentum falls by the factor (1 - cos {nf(th)}°)", z=11)
    return {'viewBox': '0 0 400 176', 'svg': s, 'alt': f"A water jet striking a {'flat plate at right angles' if th is None else f'vane that turns it through {nf(th)}°'}; the force on it along the jet is {nf(F, 1)} N."}
def jack(F1, d1, d2, F2):
    s = f"<path d='M70 60 L70 140 L330 140 L330 60 L250 60 L250 110 L110 110 L110 60 Z' fill='{BL}' fill-opacity='.3' stroke='{SL}' stroke-width='2'/><rect x='70' y='52' width='40' height='10' fill='{RU}' stroke='{SL}' stroke-width='2'/><rect x='250' y='52' width='80' height='10' fill='{RU}' stroke='{SL}' stroke-width='2'/>"
    s += arrow(90, 12, 50) + arrow(290, 50, 12, JD) + T(100, 24, f"{nf(F1)} N in", a='start', c=EM, w='600') + T(300, 24, f"{nf(F2)} N out", a='start', c=JD, w='600') + T(90, 158, f"{nf(d1)} mm piston", z=11) + T(290, 158, f"{nf(d2)} mm piston", z=11) + T(200, 130, 'same pressure throughout', z=11)
    return {'viewBox': '0 0 400 166', 'svg': s, 'alt': f"A hydraulic jack: {nf(F1)} N on a {nf(d1)} mm piston produces the same pressure under a {nf(d2)} mm piston, which lifts {nf(F2)} N."}
def mcline(c, phi, sn, tau):
    xm = sn * 1.45; ym = c + xm * math.tan(rad(phi)); k = min(280 / xm, 120 / ym); X = lambda v: 60 + v * k; Y = lambda v: 150 - v * k
    s = f"<line x1='60' y1='150' x2='360' y2='150' stroke='{SL}' stroke-width='2'/><line x1='60' y1='150' x2='60' y2='16' stroke='{SL}' stroke-width='2'/><line x1='60' y1='{Y(c):.0f}' x2='{X(xm):.0f}' y2='{Y(ym):.0f}' stroke='{JD}' stroke-width='3'/>"
    s += f"<line x1='{X(sn):.0f}' y1='150' x2='{X(sn):.0f}' y2='{Y(tau):.0f}' stroke='{SL}' stroke-dasharray='5 4'/><line x1='60' y1='{Y(tau):.0f}' x2='{X(sn):.0f}' y2='{Y(tau):.0f}' stroke='{SL}' stroke-dasharray='5 4'/><circle cx='{X(sn):.0f}' cy='{Y(tau):.0f}' r='5' fill='{EM}'/>"
    s += T(X(sn), 166, f"normal stress {nf(sn)} kPa", z=11) + T(X(sn) + 10, Y(tau) + 16, f"shear strength {nf(tau, 1)} kPa", a='start', c=EM, w='600', z=11) + T(X(xm) - 4, Y(ym) - 8, f"rises at the friction angle, {nf(phi, 1)}°", a='end', c=JD, w='600', z=11) + (T(66, Y(c) - 6, f"cohesion {nf(c)} kPa", a='start', z=11) if c else '')
    return {'viewBox': '0 0 400 176', 'svg': s, 'alt': f"The soil's strength line: shear strength against normal stress, starting at a cohesion of {nf(c)} kPa and rising at the friction angle of {nf(phi, 1)}°. At {nf(sn)} kPa normal stress the strength is {nf(tau, 1)} kPa."}
def slip(R, La, x, W, su):
    s = f"<line x1='40' y1='70' x2='360' y2='70' stroke='{SL}' stroke-width='2'/><path d='M96 70 A116 116 0 0 0 304 70' fill='{CR}' stroke='{JD}' stroke-width='3'/><circle cx='200' cy='18' r='4' fill='{SL}'/>" + T(190, 16, 'O', a='end')
    s += f"<line x1='200' y1='18' x2='120' y2='102' stroke='{SL}' stroke-dasharray='5 4'/>" + T(150, 56, f"R = {nf(R)} m", a='end', z=11) + arrow(248, 78, 124) + T(240, 108, f"W = {nf(W)} kN", a='end', c=EM, w='600') + dim(200, 248, 36, f"{nf(x)} m")
    s += T(200, 150, f"Clay strength {nf(su)} kPa acts along the {nf(La)} m arc, at radius R from O", c=JD, w='600', z=11) + T(200, 166, 'Driving moment = W × its distance from O', z=11)
    return {'viewBox': '0 0 400 174', 'svg': s, 'alt': f"A circular slip surface of radius {nf(R)} m about O. The weight of {nf(W)} kN acts {nf(x)} m from O and tries to rotate the mass; the clay strength of {nf(su)} kPa along the {nf(La)} m arc resists at radius R."}
def two1(B, z, dq):
    k = 150 / (B + z); x0 = 200 - B * k / 2; h = min(z * k, 90); sp = z * k / 2
    s = f"<line x1='40' y1='44' x2='360' y2='44' stroke='{SL}' stroke-width='2'/><rect x='{x0:.0f}' y='30' width='{B*k:.0f}' height='14' fill='{CR}' stroke='{SL}' stroke-width='2'/>" + arrow(200, 4, 28) + f"<path d='M{x0:.0f} 44 L{x0 - sp:.0f} {44 + h:.0f} L{x0 + B * k + sp:.0f} {44 + h:.0f} L{x0 + B * k:.0f} 44' fill='{LG}' fill-opacity='.5' stroke='{JD}' stroke-width='2' stroke-dasharray='6 4'/>"
    s += T(x0 + B * k + 8, 40, f"{nf(B)} m wide", a='start', z=11) + T(x0 - sp - 6, 44 + h / 2, f"{nf(z)} m", a='end', z=11) + dim(x0 - sp, x0 + B * k + sp, 44 + h + 14, f"{nf(B)} + {nf(z)} = {nf(B + z)} m") + T(200, 44 + h + 44, f"The same load over the larger area: {nf(dq, 1)} kPa", c=EM, w='600', z=11)
    return {'viewBox': f"0 0 400 {44 + h + 54:.0f}", 'svg': s, 'alt': f"The 2:1 method: the loaded area spreads outward by 1 for every 2 of depth, so {nf(z)} m down each side is {nf(z)} m longer and the stress falls to {nf(dq, 1)} kPa."}
def trib(sp, w=None, q=None):
    s = ''.join(f"<line x1='{x}' y1='30' x2='{x}' y2='130' stroke='{SL}' stroke-width='{4 if x == 200 else 2}'/>" for x in (80, 200, 320)) + f"<rect x='140' y='30' width='120' height='100' fill='{LG}' fill-opacity='.6' stroke='{JD}' stroke-dasharray='6 4'/>"
    s += dim(80, 200, 148, f"{nf(sp)} m") + dim(200, 320, 148, f"{nf(sp)} m") + T(200, 20, f"This beam carries a strip {nf(sp)} m wide: half a bay on each side", c=JD, w='600', z=11) + (T(200, 190, f"{nf(q)} kPa × {nf(sp)} m = {nf(w, 1)} kN/m along the beam", c=EM, w='600', z=11) if w else '')
    return {'viewBox': '0 0 400 198', 'svg': s, 'alt': f"Plan of floor beams {nf(sp)} m apart. The middle beam carries the floor from halfway to each neighbour, a strip {nf(sp)} m wide."}
def tribcol(a, b, note=''):
    s = ''.join(f"<rect x='{x-5}' y='{y-5}' width='10' height='10' fill='{SL}'/>" for x in (90, 200, 310) for y in (30, 90, 150)) + f"<rect x='145' y='60' width='110' height='60' fill='{LG}' fill-opacity='.6' stroke='{JD}' stroke-dasharray='6 4'/>" + dim(90, 200, 172, f"{nf(a)} m") + T(322, 64, f"{nf(b)} m", a='start', z=11)
    s += T(200, 14, f"The middle column carries {nf(a)} m × {nf(b)} m = {nf(a * b)} m² of each floor", c=JD, w='600', z=11) + (T(200, 214, note, c=EM, w='600', z=11) if note else '')
    return {'viewBox': '0 0 400 222', 'svg': s, 'alt': f"Plan of a column grid {nf(a)} m by {nf(b)} m. An interior column carries the floor halfway to each neighbouring column, {nf(a * b)} m² per floor."}
def lap(n, R, u='kips'):
    xs = [150 + 100 * (i + 0.5) / n for i in range(n)]
    s = f"<rect x='40' y='60' width='210' height='40' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='150' y='70' width='210' height='40' fill='{LG}' fill-opacity='.7' stroke='{SL}' stroke-width='2'/>" + ''.join(f"<circle cx='{x:.0f}' cy='85' r='7' fill='{JD}' stroke='{SL}'/>" for x in xs)
    s += harrow(40, 6, 80) + harrow(360, 394, 90) + T(200, 136, f"{n} bolts, each cut on one plane between the plates", z=11) + T(200, 154, f"Design strength of the group = {nf(R, 1)} {u}", c=EM, w='600', z=11)
    return {'viewBox': '0 0 400 162', 'svg': s, 'alt': f"Two overlapping plates pulled in opposite directions and joined by {n} bolts, each in single shear."}
def swing(Ln):
    s = f"<circle cx='110' cy='40' r='5' fill='{SL}'/><rect x='110' y='35' width='180' height='10' fill='{CR}' stroke='{SL}' stroke-width='2'/><rect x='105' y='40' width='10' height='130' fill='{LG}' fill-opacity='.6' stroke='{JD}' stroke-dasharray='6 4'/><circle cx='200' cy='40' r='4' fill='{EM}'/><circle cx='110' cy='105' r='4' fill='{EM}'/>"
    s += f"<line x1='200' y1='40' x2='200' y2='105' stroke='{EM}' stroke-dasharray='5 4'/><line x1='110' y1='105' x2='200' y2='105' stroke='{EM}' stroke-dasharray='5 4'/>" + T(208, 78, f"centre of mass falls {nf(Ln / 2, 2)} m", a='start', c=EM, w='600', z=11) + T(200, 26, f"{nf(Ln)} m rod, released level", z=11) + T(124, 168, 'passing through the vertical', a='start', z=11)
    return {'viewBox': '0 0 400 180', 'svg': s, 'alt': f"A {nf(Ln)} m rod pinned at one end, shown level at release and hanging vertically. Its centre of mass falls by half its length, {nf(Ln / 2, 2)} m."}
_ws = (None, None)
def _keep(d, key): return d.get(key, _ws)[0]
BY_ID.update({
 'statics-0007': (None, L(0, lambda e: fcs(e.Fc, e.d, e.ans))),
 'fluids-0001': (None, L(0, lambda e: press(e.h, e.ans))), 'fluids-0012': (None, L(0, lambda e: jet(e.ans))), 'fluids-0014': (None, L(0, lambda e: jet(e.ans, e.th))),
 'geotech-0005': (None, L(0, lambda e: mcline(e.c, e.phi, e.sn, e.ans))), 'geotech-0021': (None, L(0, lambda e: slip(e.R, e.La, e.x, e.W, e.su))),
 'mechmat-0010': (None, L(0, lambda e: bar([('Heated bar: it tries to lengthen', 1)], [(0, 'wall pushes back', 1, BL), (1, 'wall pushes back', -1, BL)], (True, True), f"Expansion is prevented, so the bar is squeezed to {nf(e.ans, 1)} MPa"))),
 'mechmat-0013': (None, L(0, lambda e: vessel(e.ans, e.ans / 2))), 'structural-0014': (None, L(0, lambda e: trib(e.s, e.ans, e.q))),
 'structural-0015': (None, L(0, lambda e: bar([(f"gross area {nf(e.Ag)} mm²", 1)], [(0, 'pull', -1, EM), (1, f"{nf(e.ans, 1)} kN", 1, EM)], (False, False), 'Design strength in yielding: 0.9 × yield strength × gross area'))),
 'dynamics-0011': (None, L(0, lambda e: fbd([('Spring force', 0, BL), ('Weight', 270, EM), ('Support from the surface', 90, JD)], 0, 'Spring force = stiffness × compression; it pushes until its stored energy is used up'))),
})
BY_STEM.update({
 'A [m] kg object moving at [v] m/s is brought to rest': (None, L(0, lambda e: fbd([(f"{nf(e.ans)} N", 180, EM)], 0, f"Moving right at {nf(e.v)} m/s; this average force acts against the motion for {nf(e.dt)} s"))),
 'A [m] kg block sliding at [v] m/s on a frictionless surface runs into a spring': (None, L(0, lambda e: fbd([('Spring force', 180, BL), ('Weight', 270, EM), ('Support from the surface', 90, JD)], 0, 'Spring force = stiffness × compression; it slows the block until its motion energy is stored'))),
 'A uniform slender rod [L|1] m long is released from rest': (None, L(0, lambda e: swing(e.L))),
 'A horizontal [d] mm pipe bend turns the flow': (None, L(0, lambda e: vec([('p A in', 1, 0), ('p A out', -cos(rad(e.th)), -sin(rad(e.th)), JD), (f"{nf(e.ans, 2)} kN", 1 - cos(rad(e.th)), -sin(rad(e.th)), BL, True)]))),
 'A flat plate with an area of [A|2] m^{2} slides': (None, L(0, lambda e: fbd([(f"Pull = {nf(e.ans, 1)} N", 0, EM), ('Oil drag', 180, BL)], 0, 'Constant speed: the pull equals the oil film drag, shear stress × plate area'))),
 'A sample weighs [Wa|1] N in air': (None, L(0, lambda e: fbd([(f"Weight = {nf(e.Wa, 1)} N", 270, EM), (f"Scale reads {nf(e.Ww, 1)} N", 112, JD), (f"Buoyant force = {nf(e.Wa - e.Ww, 1)} N", 68, BL)], 0, 'Buoyant force = weight in air - weight in water = weight of the water displaced'))),
 'A hydraulic jack has an input piston': (None, L(0, lambda e: jack(e.F1, e.d1, e.d2, e.ans))),
 'A sign panel with an area of [A|1] m^{2}': (None, L(0, lambda e: fbd([(f"Drag = {nf(e.ans, 1)} N", 0, EM)], 0, 'The flow comes from the left; drag acts in the direction of the flow'))),
 'A footing [B|1] m by [Lf|1] m carries a load of [Q] kN. Using the 2:1 method': (None, L(0, lambda e: two1(e.B, e.z, e.ans))),
 'A direct shear test on dry sand fails': (None, L(0, lambda e: mcline(0, e.ans, e.sn, e.ta))),
 'A soil has a cohesion of [c] kPa and a friction angle of [phi]°. In a triaxial test': (None, L(0, lambda e: mohr(e.ans, e.s3, 0))),
 'A clevis is pinned by a single [d] mm diameter bolt': (None, L(0, lambda e: dshear(e.P))),
 'A [d] mm diameter bolt bears against a plate': (None, L(0, lambda e: bearing(e.d, e.t, e.P))),
 'A steel bar (E = 200 GPa) [L1] mm long': (None, L(0, lambda e: bar([(f"Steel {nf(e.L1)} mm", e.L1 / (e.L1 + e.L2)), (f"Aluminium {nf(e.L2)} mm", e.L2 / (e.L1 + e.L2))], [(1, f"{nf(e.ans, 1)} kN", 1, EM)], (True, False), 'The same force passes through both bars; their stretches add'))),
 'A uniform bar [L|1] m long is fixed to rigid walls at both ends': (None, L(0, lambda e: bar([(f"{nf(e.a)} m, stretched", e.a / e.L), (f"{nf(e.L - e.a)} m, squeezed", 1 - e.a / e.L)], [(e.a / e.L, f"{nf(e.P)} kN", 1, EM), (0, f"{nf(e.ans, 1)} kN", -1, BL), (1, f"{nf(e.P - e.ans, 1)} kN", -1, BL)], (True, True), 'The shorter, stiffer part takes the larger share'))),
 'A thin-walled cylindrical tank with closed ends': (None, L(0, lambda e: vessel(2 * e.ans, e.ans))),
 'A hand force of [P] N is applied to each handle of a pair of pliers': (None, L(0, lambda e: lever(e.P, e.a, e.b, e.ans))),
 'A short composite column has a steel core': (None, L(0, lambda e: fbd([(f"Load {nf(e.P)} kN", 270, EM), (f"Steel {nf(e.ans, 1)} kN", 112, JD), (f"Concrete {nf(e.P - e.ans, 1)} kN", 68, BL)], 0, 'Both shorten equally, so each takes load in proportion to its E × area'))),
 'A connection has [n] bolts of [db|3] in diameter': (None, L(0, lambda e: lap(e.n, e.ans))),
 'An interior column supports [n] floors': (None, L(0, lambda e: tribcol(e.a, e.b, f"{nf(e.n)} floors × {nf(e.q, 1)} kPa × {nf(e.a * e.b)} m² = {nf(e.ans)} kN"))),
 'Floor beams span [L] m and are spaced [s] m apart': (None, L(0, lambda e: trib(e.s))),
})
def lookup(base, stem):
    if base in BY_ID: return BY_ID[base]
    for k, v in BY_STEM.items():
        if stem.startswith(k): return v
    return None, None
def post(q):
    """Vector diagram for a written-out vector question (no numeric template)."""
    if q.get('solutionFigure') or q.get('subtopic') != 'math-c': return
    num = r'(-?\d+(?:\.\d+)?)'; items = []
    for m in re.finditer(r'\*\*([A-Z])\*\* = ' + num + r'\*\*i\*\* ([+-]) ' + num + r'\*\*j\*\*', q['stem']): items.append((m.group(1), float(m.group(2)), float(m.group(4)) * (1 if m.group(3) == '+' else -1)))
    for m in re.finditer(r'\*\*([A-Z])\*\* = \(' + num + ', ' + num + r'\)', q['stem']): items.append((m.group(1), float(m.group(2)), float(m.group(3))))
    if items: q['solutionFigure'] = vec(items)
