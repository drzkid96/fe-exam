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
