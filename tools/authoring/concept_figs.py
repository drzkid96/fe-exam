"""Concept figures for the lessons: each one draws the idea itself (what the quantity means, how the parts relate), not a worked problem.
Original drawings in the site palette. Imported by author_concept.py."""
import math
from author_v import T, SL, EM, JD, BL, CR, LG, RU
OR, WH = '#FF6622', '#FFFFFF'
cos, sin, rad, sqrt, exp, log10 = math.cos, math.sin, math.radians, math.sqrt, math.exp, math.log10


# ---------------- drawing helpers ----------------
def A(x1, y1, x2, y2, c=EM, wd=2.5, dash=False, head=10):
    """Arrow from (x1, y1) with its head at (x2, y2)."""
    a = math.atan2(y2 - y1, x2 - x1); bx, by = x2 - head * cos(a), y2 - head * sin(a); px, py = head * 0.5 * sin(a), -head * 0.5 * cos(a)
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{bx:.1f}' y2='{by:.1f}' stroke='{c}' stroke-width='{wd}'" + (" stroke-dasharray='6 4'" if dash else '') +
            f"/><path d='M{x2:.1f} {y2:.1f} L{bx + px:.1f} {by + py:.1f} L{bx - px:.1f} {by - py:.1f} Z' fill='{c}'/>")
def Ln(x1, y1, x2, y2, c=SL, wd=1.5, dash=False):
    return f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{c}' stroke-width='{wd}'" + (" stroke-dasharray='6 4'" if dash else '') + "/>"
def R(x, y, w, h, f=CR, s=SL, wd=1.5, op=None):
    return f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{f}'" + (f" fill-opacity='{op}'" if op else '') + f" stroke='{s}' stroke-width='{wd}'/>"
def Cc(cx, cy, r, f=WH, s=SL, wd=1.5):
    return f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r:.1f}' fill='{f}' stroke='{s}' stroke-width='{wd}'/>"
def Dot(cx, cy, c=EM, r=4): return f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r}' fill='{c}'/>"
def Pa(d, f='none', s=SL, wd=2, dash=False, op=None):
    return f"<path d='{d}' fill='{f}'" + (f" fill-opacity='{op}'" if op else '') + f" stroke='{s}' stroke-width='{wd}'" + (" stroke-dasharray='6 4'" if dash else '') + "/>"
def poly(pts, close=False): return 'M' + ' L'.join(f"{x:.1f} {y:.1f}" for x, y in pts) + (' Z' if close else '')
def curve(fn, a, b, n=60): return [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)]
def axes(x0, y0, x1, y1, xl, yl, c=SL):
    return A(x0, y0, x1, y0, c, 1.5, head=8) + A(x0, y0, x0, y1, c, 1.5, head=8) + T(x1, y0 + 16, xl, a='end', z=11) + T(x0 + 6, y1 + 4, yl, a='start', z=11)
def box(x, y, w, h, lab, f=CR, s=SL, c=SL, z=11, wt='600', op=None):
    ls = lab.split('\n'); y0 = y + h / 2 - (len(ls) - 1) * (z + 2) / 2 + z * 0.35
    return R(x, y, w, h, f, s, 1.5, op) + ''.join(T(x + w / 2, y0 + i * (z + 2), t, c=c, w=wt, z=z) for i, t in enumerate(ls))
def lines(x, y, txt, a='start', c=SL, z=11, w='400', dy=None):
    return ''.join(T(x, y + i * (dy or z + 4), t, a=a, c=c, w=w, z=z) for i, t in enumerate(txt.split('\n')))
def arc(cx, cy, r, a1, a2, c=SL, wd=1.5, head=False):
    """Arc of radius r about (cx, cy) from angle a1 to a2 (degrees, counter-clockwise from +x as on paper)."""
    p1 = (cx + r * cos(rad(a1)), cy - r * sin(rad(a1))); p2 = (cx + r * cos(rad(a2)), cy - r * sin(rad(a2)))
    big = 1 if abs(a2 - a1) > 180 else 0; sw = 0 if a2 > a1 else 1
    s = Pa(f"M{p1[0]:.1f} {p1[1]:.1f} A{r} {r} 0 {big} {sw} {p2[0]:.1f} {p2[1]:.1f}", s=c, wd=wd)
    if head:
        t = rad(a2); d = 1 if a2 > a1 else -1; tx, ty = -sin(t) * d, -cos(t) * d     # direction of travel at the end, in screen coordinates
        s += A(p2[0] - tx * 8, p2[1] - ty * 8, p2[0] + tx * 2, p2[1] + ty * 2, c, wd, head=8)
    return s
def dimh(x1, x2, y, lab, c=SL, below=True):
    return Ln(x1, y, x2, y, c, 1) + Ln(x1, y - 5, x1, y + 5, c, 1) + Ln(x2, y - 5, x2, y + 5, c, 1) + T((x1 + x2) / 2, y + (14 if below else -6), lab, c=c, z=11)
def dimv(x, y1, y2, lab, c=SL, side='right'):
    return Ln(x, y1, x, y2, c, 1) + Ln(x - 5, y1, x + 5, y1, c, 1) + Ln(x - 5, y2, x + 5, y2, c, 1) + T(x + (8 if side == 'right' else -8), (y1 + y2) / 2 + 4, lab, a='start' if side == 'right' else 'end', c=c, z=11)
def hatch(x1, x2, y, down=True):
    return Ln(x1, y, x2, y, SL, 2) + ''.join(Ln(x, y, x - 6, y + (7 if down else -7), SL, 1) for x in range(int(x1) + 6, int(x2) + 1, 8))
def pin(x, y): return Pa(f"M{x} {y} L{x - 10} {y + 16} L{x + 10} {y + 16} Z", WH, SL, 1.5) + hatch(x - 14, x + 14, y + 16)
def roller(x, y): return Pa(f"M{x} {y} L{x - 10} {y + 14} L{x + 10} {y + 14} Z", WH, SL, 1.5) + Cc(x - 5, y + 18, 3.5) + Cc(x + 5, y + 18, 3.5) + Ln(x - 14, y + 22, x + 14, y + 22, SL, 2)
def wall(x, y1, y2, side='left'):
    w = 12; xr = x - w if side == 'left' else x
    return R(xr, y1, w, y2 - y1, RU, SL, 1.5)
def udl(x1, x2, y, n=9, c=EM, h=16):
    return Ln(x1, y - h, x2, y - h, c, 1.5) + ''.join(A(x1 + (x2 - x1) * i / (n - 1), y - h, x1 + (x2 - x1) * i / (n - 1), y - 1, c, 1.5, head=6) for i in range(n))
def F(h, svg, alt, w=400): return {'viewBox': f'0 0 {w} {h}', 'svg': svg, 'alt': alt}


# ---------------- Mathematics ----------------
def math_a():
    X = lambda u: 50 + u * 30; Y = lambda v: 190 - v * 30
    s = axes(50, 190, 380, 18, 'x', 'y')
    s += Ln(X(0), Y(1), X(9), Y(5.5), EM, 2.5) + Dot(X(0), Y(1), EM) + T(X(0) + 8, Y(1) + 14, 'b, where the line crosses the y-axis', a='start', c=EM, z=11)
    s += Ln(X(2), Y(2), X(6), Y(2), SL, 1.5, True) + Ln(X(6), Y(2), X(6), Y(4), SL, 1.5, True) + T(X(4), Y(2) + 14, 'run = 4', z=11) + T(X(6) - 6, Y(3) + 4, 'rise = 2', a='end', z=11)
    s += T(X(1.2), Y(4.9), 'y = m x + b', a='start', c=EM, w='600') + T(X(1.2), Y(4.4), 'm = rise / run = 2 / 4 = 0.5', a='start', c=EM, z=11)
    s += Ln(X(5.25), Y(5.5), X(8), Y(0), BL, 2.5) + T(X(8.1), Y(0.6), 'perpendicular line:', a='start', c=BL, z=11) + T(X(8.1), Y(0.6) + 14, 'slope = -1 / m = -2', a='start', c=BL, z=11)
    px, py = X(6), Y(4); d1 = (2 / sqrt(5), -1 / sqrt(5)); d2 = (1 / sqrt(5), 2 / sqrt(5)); k = 9
    s += Pa(f"M{px + k * d1[0]:.1f} {py + k * d1[1]:.1f} L{px + k * (d1[0] + d2[0]):.1f} {py + k * (d1[1] + d2[1]):.1f} L{px + k * d2[0]:.1f} {py + k * d2[1]:.1f}", s=SL, wd=1)
    return F(215, s, 'A straight line y = m x + b: the slope m is rise over run, b is where it crosses the y-axis, and a perpendicular line has slope -1 / m.')

def math_b():
    s = axes(30, 175, 195, 20, 'x', 'y') + axes(215, 175, 390, 20, 'x', 'y')
    X = lambda t: 40 + t * 145; Y = lambda f: 168 - f * 120; f = lambda t: 4 * t * (1 - t)
    s += Pa(poly([(X(t), Y(f(t))) for t, _ in curve(lambda t: 0, 0, 1)]), s=JD, wd=2.5)
    t0 = 0.2; m = (4 - 8 * t0) * 120 / 145; x0, y0 = X(t0), Y(f(t0))
    s += Ln(x0 - 22, y0 + 22 * m, x0 + 18, y0 - 18 * m, EM, 2) + Dot(x0, y0) + T(115, 140, 'slope of the tangent', c=EM, z=11) + T(115, 154, '= derivative dy/dx', c=EM, z=11)
    s += Ln(X(0.5) - 34, Y(1), X(0.5) + 34, Y(1), EM, 2, True) + Dot(X(0.5), Y(1)) + T(X(0.5), Y(1) - 10, 'peak: dy/dx = 0', c=EM, z=11)
    X2 = lambda t: 225 + t * 155; g = lambda t: 0.25 + 0.75 * t - 0.45 * t * t
    pts = [(X2(t), Y(g(t))) for t, _ in curve(lambda t: 0, 0.25, 0.8, 30)]
    s += Pa(poly([(X2(0.25), Y(0))] + pts + [(X2(0.8), Y(0))], True), LG, 'none', 0)
    s += Pa(poly([(X2(t), Y(g(t))) for t, _ in curve(lambda t: 0, 0, 1)]), s=JD, wd=2.5)
    s += T(X2(0.25), 190, 'a', z=11) + T(X2(0.8), 190, 'b', z=11) + T(X2(0.52), Y(0.22), 'area under the curve', c=EM, w='600', z=11) + T(X2(0.52), Y(0.22) + 14, '= integral from a to b', c=EM, z=11)
    return F(200, s, 'Left: the derivative is the slope of the tangent, and it is zero at a peak. Right: the integral from a to b is the area under the curve.')

def math_c():
    O = (40, 170); sc = 20; A_ = (5, 2); B_ = (2, 4)
    ax, ay = O[0] + A_[0] * sc, O[1] - A_[1] * sc; bx, by = ax + B_[0] * sc, ay - B_[1] * sc
    s = Ln(20, 170, 205, 170, RU, 1) + A(O[0], O[1], ax, ay, EM) + A(ax, ay, bx, by, JD) + A(O[0], O[1], bx, by, BL, 3)
    s += Ln(O[0], O[1] + 0, ax, O[1], SL, 1.2, True) + Ln(ax, O[1], ax, ay, SL, 1.2, True) + T((O[0] + ax) / 2, 186, 'Ax', z=11) + T(ax + 6, (O[1] + ay) / 2 + 8, 'Ay', a='start', z=11)
    s += T((O[0] + ax) / 2 - 4, (O[1] + ay) / 2 - 8, 'A', c=EM, w='600') + T((ax + bx) / 2 + 10, (ay + by) / 2 + 4, 'B', a='start', c=JD, w='600') + T((O[0] + bx) / 2 - 10, (O[1] + by) / 2 - 4, 'A + B', a='end', c=BL, w='600')
    s += T(12, 18, 'Tip to tail: add x parts, then y parts', a='start', z=11)
    O2 = (240, 170); a1, a2 = 10, 55; la, lb = 135, 100
    pa = (O2[0] + la * cos(rad(a1)), O2[1] - la * sin(rad(a1))); pb = (O2[0] + lb * cos(rad(a2)), O2[1] - lb * sin(rad(a2)))
    pr = lb * cos(rad(a2 - a1)); foot = (O2[0] + pr * cos(rad(a1)), O2[1] - pr * sin(rad(a1)))
    s += A(O2[0], O2[1], pa[0], pa[1], EM) + A(O2[0], O2[1], pb[0], pb[1], JD) + Ln(pb[0], pb[1], foot[0], foot[1], SL, 1.2, True) + Ln(O2[0], O2[1] + 6, foot[0], foot[1] + 6, BL, 3)
    s += arc(O2[0], O2[1], 34, a1, a2) + T(O2[0] + 40, O2[1] - 18, 'θ', a='start') + T(pa[0], pa[1] + 16, 'A', c=EM, w='600') + T(pb[0] - 4, pb[1] - 6, 'B', a='end', c=JD, w='600')
    s += T((O2[0] + foot[0]) / 2, foot[1] + 26, '|B| cos θ', c=BL, w='600', z=11) + T(315, 18, 'A · B = |A| |B| cos θ', c=SL, w='600', z=11)
    return F(205, s, 'Left: vectors add tip to tail, component by component. Right: the dot product is |A| times the part of B that lies along A, |B| cos θ.')

def math_d():
    X = lambda z: 200 + z * 52; Y = lambda p: 175 - p * 130; ph = lambda z: exp(-z * z / 2)
    s = ''
    for a, b, f in ((-2, 2, CR), (-1, 1, LG)):
        pts = [(X(z), Y(ph(z))) for z, _ in curve(lambda z: 0, a, b, 40)]
        s += Pa(poly([(X(a), Y(0))] + pts + [(X(b), Y(0))], True), f, 'none', 0)
    s += Pa(poly([(X(z), Y(ph(z))) for z, _ in curve(lambda z: 0, -3.4, 3.4, 80)]), s=JD, wd=2.5) + Ln(20, 175, 380, 175, SL, 1.5)
    s += R(14, 22, 14, 10, LG, SL, 0.8) + T(32, 31, 'about 68% within one σ', a='start', z=11) + R(14, 40, 14, 10, CR, SL, 0.8) + T(32, 49, 'about 95% within two σ', a='start', z=11)
    for z, lab in ((-2, 'μ - 2σ'), (-1, 'μ - σ'), (0, 'μ'), (1, 'μ + σ'), (2, 'μ + 2σ')):
        s += Ln(X(z), 175, X(z), 181, SL, 1.5) + T(X(z), 195, lab, z=11, w='600' if z == 0 else '400')
    s += T(390, 30, 'μ = mean (centre)', a='end', z=11) + T(390, 45, 'σ = standard deviation (spread)', a='end', z=11) + T(390, 60, 'z = (x - μ) / σ', a='end', z=11)
    return F(205, s, 'A normal distribution: centred on the mean μ, with about 68% of values within one standard deviation σ of it and about 95% within two.')


# ---------------- Statics ----------------
def statics_a():
    O = (70, 170); L, th = 190, 35; tip = (O[0] + L * cos(rad(th)), O[1] - L * sin(rad(th)))
    s = Ln(30, 170, 300, 170, RU, 1) + Ln(70, 190, 70, 30, RU, 1)
    s += A(O[0], O[1], tip[0], O[1], BL, 2, True) + A(tip[0], O[1], tip[0], tip[1], BL, 2, True) + A(O[0], O[1], tip[0], tip[1], EM, 3)
    s += arc(O[0], O[1], 44, 0, th) + T(O[0] + 50, O[1] - 10, 'θ', a='start')
    s += T((O[0] + tip[0]) / 2 - 6, (O[1] + tip[1]) / 2 - 8, 'F', a='end', c=EM, w='600') + T((O[0] + tip[0]) / 2, 188, 'Fx = F cos θ', c=BL, w='600', z=11) + T(tip[0] + 8, (O[1] + tip[1]) / 2 + 4, 'Fy = F sin θ', a='start', c=BL, w='600', z=11)
    s += lines(262, 40, 'Several forces?\nAdd all the Fx: ΣFx\nAdd all the Fy: ΣFy\nR = √(ΣFx² + ΣFy²)\ntan θR = ΣFy / ΣFx', z=11)
    return F(200, s, 'A force F at angle θ split into its parts: Fx = F cos θ along x and Fy = F sin θ along y. Several forces are added part by part.')

def statics_b():
    O = (80, 150); P = (80 + 180 * cos(rad(30)), 150 - 180 * sin(rad(30)))
    s = Pa(f"M{O[0]} {O[1]} L{O[0] - 10} {O[1] + 16} L{O[0] + 10} {O[1] + 16} Z", WH, SL, 1.5) + hatch(O[0] - 14, O[0] + 14, O[1] + 16)
    s += Ln(O[0], O[1], P[0], P[1], SL, 7) + Ln(O[0], O[1], P[0], P[1], CR, 4) + Cc(O[0], O[1], 5) + T(O[0] - 16, O[1] + 6, 'O', a='end', w='600')
    s += Ln(P[0], 18, P[0], 176, EM, 1, True) + A(P[0], P[1] - 40, P[0], P[1] - 2, EM, 3) + T(P[0] + 8, P[1] - 30, 'F', a='start', c=EM, w='600') + T(P[0] - 8, 26, 'line of action', a='end', c=EM, z=11)
    s += Ln(O[0], O[1], P[0], O[1], BL, 2) + R(P[0] - 8, O[1] - 8, 8, 8, 'none', SL, 1) + T((O[0] + P[0]) / 2 + 20, O[1] + 44, 'd, measured at 90° to the line of action', c=BL, w='600', z=11)
    s += arc(O[0], O[1], 30, 150, 40, EM, 2, True) + T(O[0] + 6, O[1] - 40, 'M', c=EM, w='600')
    s += lines(258, 118, 'M = F × d\nnot F × (length of the arm)', z=11, w='600')
    return F(206, s, 'Moment about O is the force times the perpendicular distance d from O to the line of action of the force, not the length of the arm it is applied to.')

def statics_c():
    s = ''
    for cx, kind, n in ((70, 'Roller', 1), (200, 'Pin', 2), (330, 'Fixed', 3)):
        if kind == 'Fixed': s += R(cx - 36, 50, 84, 10, CR, SL, 1.5) + R(cx - 48, 26, 12, 58, RU, SL, 1.5); bx = cx - 36; s += R(cx - 36, 120, 84, 10, CR, SL, 1.5)
        else: s += R(cx - 48, 50, 96, 10, CR, SL, 1.5) + (roller(cx, 60) if kind == 'Roller' else pin(cx, 60)); bx = cx; s += R(cx - 48, 120, 96, 10, CR, SL, 1.5)
        s += T(cx, 20, kind, w='600') + A(bx, 172, bx, 132, EM) + T(bx + 6, 168, 'Ry', a='start', c=EM, w='600', z=11)
        if kind == 'Pin': s += A(bx - 44, 140, bx - 4, 140, EM) + T(bx - 46, 156, 'Rx', a='start', c=EM, w='600', z=11)
        if kind == 'Fixed': s += A(bx - 40, 125, bx - 2, 125, EM) + T(bx - 40, 144, 'Rx', a='start', c=EM, w='600', z=11) + arc(bx, 125, 18, 250, 110, BL, 2, True) + T(bx + 24, 112, 'M', a='start', c=BL, w='600', z=11)
        s += T(cx, 198, f"{n} unknown{'s' if n > 1 else ''}", c=EM, w='600', z=11)
    s += Ln(10, 100, 390, 100, RU, 1)
    return F(210, s, 'Each support is replaced by the forces it can apply: a roller pushes one way (1 unknown), a pin holds both directions (2), a fixed support also stops rotation (3).')
def statics_d():
    s = R(60, 52, 110, 12, CR, SL, 1.5) + A(60, 58, 22, 58, EM) + A(170, 58, 208, 58, EM) + T(115, 40, 'Tension: the member is pulled', c=EM, w='600', z=11)
    s += R(60, 122, 110, 12, CR, SL, 1.5) + A(20, 128, 58, 128, BL) + A(210, 128, 172, 128, BL) + T(115, 110, 'Compression: the member is pushed', c=BL, w='600', z=11)
    s += lines(20, 166, 'Assume each unknown member\nis in tension. A negative\nanswer means compression.', z=11)
    bot = [(230, 170), (275, 170), (320, 170), (365, 170)]; top = [(252, 120), (297, 120), (342, 120)]
    mem = [(bot[0], bot[1]), (bot[1], bot[2]), (bot[2], bot[3]), (top[0], top[1]), (top[1], top[2])] + [(bot[i], top[i]) for i in range(3)] + [(top[i], bot[i + 1]) for i in range(3)]
    s += ''.join(Ln(a[0], a[1], b[0], b[1], SL, 2.5) for a, b in mem) + ''.join(Cc(x, y, 3.5) for x, y in bot + top)
    s += Ln(286, 100, 286, 190, EM, 2, True) + T(286, 92, 'cut', c=EM, w='600', z=11) + lines(222, 22, 'Method of sections:\ncut through at most three\nunknown members, then take\nmoments where two meet.', z=11)
    return F(205, s, 'Tension members are pulled and compression members pushed. Assume tension; a negative result means compression. The method of sections cuts through three members at most.')

def statics_e():
    s = R(60, 40, 40, 140, CR, SL, 1.5) + R(100, 140, 120, 40, LG, SL, 1.5)
    s += Dot(80, 110, JD) + T(74, 104, '1', a='end', c=JD, w='600') + Dot(160, 160, JD) + T(160, 152, '2', c=JD, w='600')
    s += Ln(80, 110, 160, 160, JD, 1, True) + Cc(116.9, 133.1, 6, WH, EM, 2.5) + Ln(108, 133.1, 126, 133.1, EM, 1.5) + Ln(116.9, 124, 116.9, 142, EM, 1.5)
    s += T(126, 122, 'composite centroid', a='start', c=EM, w='600', z=11)
    s += T(58, 200, 'A1 = 5,600', a='start', z=11) + T(222, 200, 'A2 = 4,800', a='end', z=11)
    s += lines(236, 46, 'x̄ = Σ(A x) / ΣA\nȳ = Σ(A y) / ΣA\n\nSplit into simple parts.\nThe centroid lies on the\nline between the parts,\nnearer the bigger one.\nIt can fall outside.', z=11)
    return F(210, s, 'An L-shape split into two rectangles. The composite centroid is the area-weighted average of their centroids; it lies on the line between them, nearer the larger area, and here falls outside the shape.')

def statics_f():
    s = R(60, 30, 20, 80, CR, SL, 1.5) + Ln(40, 70, 100, 70, EM, 1, True) + R(130, 60, 80, 20, CR, SL, 1.5) + Ln(115, 70, 225, 70, EM, 1, True)
    s += T(70, 126, 'standing', z=11) + T(70, 140, 'I = 20 × 80³ / 12', z=11) + T(70, 154, '= 853,333 mm⁴', c=EM, w='600', z=11)
    s += T(170, 126, 'lying flat', z=11) + T(170, 140, 'I = 80 × 20³ / 12', z=11) + T(170, 154, '= 53,333 mm⁴', c=EM, w='600', z=11)
    s += lines(20, 180, 'Same area, 16 times stiffer standing up:\narea far from the axis counts most (I = Σ A y²).', z=11)
    s += R(270, 40, 90, 50, LG, SL, 1.5) + Ln(255, 65, 375, 65, EM, 1.5, True) + T(380, 69, 'c', a='start', c=EM, w='600') + Ln(255, 140, 375, 140, BL, 2) + T(380, 144, "x'", a='start', c=BL, w='600')
    s += dimv(262, 65, 140, 'd', SL, 'left') + lines(260, 165, "I about x' = Ī + A d²\nĪ: about the centroid c", z=11)
    return F(220, s, 'Left: the same plank is far stiffer on edge, because area far from the axis counts most. Right: the parallel axis theorem moves I from the centroidal axis to any parallel axis a distance d away.')

def statics_g():
    s = Ln(20, 140, 170, 140, SL, 2) + hatch(20, 170, 140) + R(60, 90, 60, 50, CR, SL, 1.5)
    s += A(90, 110, 90, 176, EM) + T(98, 172, 'W', a='start', c=EM, w='600', z=11) + A(76, 186, 76, 142, JD) + T(70, 182, 'N', a='end', c=JD, w='600', z=11)
    s += A(120, 112, 168, 112, BL) + T(166, 104, 'P', c=BL, w='600', z=11) + A(84, 136, 34, 136, OR) + T(32, 130, 'F', a='start', c=OR, w='600', z=11)
    s += axes(210, 175, 390, 20, 'applied force P', 'friction F')
    s += Ln(210, 175, 300, 85, EM, 2.5) + Dot(300, 85) + Ln(300, 85, 306, 110, EM, 2.5) + Ln(306, 110, 385, 110, EM, 2.5)
    s += Ln(210, 85, 300, 85, SL, 1, True) + T(214, 80, 'μs N', a='start', c=EM, w='600', z=11) + Ln(210, 110, 300, 110, SL, 1, True) + T(214, 124, 'μk N', a='start', z=11)
    s += T(246, 150, 'F = P', a='start', z=11) + T(246, 164, '(no sliding)', a='start', z=11) + T(312, 104, 'sliding', a='start', z=11)
    return F(200, s, 'Friction matches the push until it reaches μs N; then the block slides and friction drops to μk N. Friction always opposes the motion or the tendency to move.')


# ---------------- Dynamics ----------------
def dynamics_a():
    s = axes(50, 180, 380, 20, 'time t', 'velocity v') + Pa(poly([(50, 180), (50, 140), (300, 60), (300, 180)], True), LG, 'none', 0) + Ln(50, 140, 300, 60, EM, 2.5)
    s += Ln(50, 140, 34, 140, SL, 1) + T(30, 144, 'v0', a='end', z=11) + Ln(300, 60, 300, 180, SL, 1, True) + T(300, 196, 't', z=11) + T(306, 58, 'v', a='start', z=11)
    s += Ln(160, 105, 220, 105, SL, 1, True) + Ln(220, 105, 220, 86, SL, 1, True) + T(226, 100, 'slope = acceleration a', a='start', c=EM, w='600', z=11)
    s += T(175, 152, 'area under the line', c=EM, w='600', z=11) + T(175, 166, '= distance travelled', c=EM, z=11)
    s += lines(310, 120, 'v = v0 + a t\ns = v0 t + ½ a t²\nv² = v0² + 2 a s', z=11)
    return F(205, s, 'A velocity-time graph for constant acceleration: the slope is the acceleration and the area under the line is the distance travelled.')

def dynamics_b():
    s = Cc(100, 95, 60, 'none', SL, 2) + ''.join(Dot(100 + 60 * cos(rad(a)), 95 - 60 * sin(rad(a)), EM, 6) for a in range(0, 360, 30)) + Dot(100, 95, SL, 4)
    s += Cc(290, 95, 60, LG, SL, 2) + ''.join(Dot(290 + r * cos(rad(a)), 95 - r * sin(rad(a)), EM, 3) for r in (15, 30, 45) for a in range(0, 360, 360 // int(r / 2.5))) + Dot(290, 95, SL, 4)
    s += arc(100, 95, 72, 60, 120, BL, 2, True) + arc(290, 95, 72, 60, 120, BL, 2, True)
    s += T(100, 178, 'Thin ring: I = m r²', c=EM, w='600', z=11) + T(290, 178, 'Solid disc: I = ½ m r²', c=EM, w='600', z=11)
    s += T(200, 202, 'Same mass and radius: the ring\'s mass is all far from the axis,', z=11) + T(200, 216, 'so it is twice as hard to spin up.', z=11)
    return F(224, s, 'A ring and a disc of the same mass and radius. All the ring\'s mass is at the rim, so its mass moment of inertia is twice the disc\'s: mass far from the axis counts most.')

def dynamics_c():
    s = R(60, 70, 70, 50, CR, SL, 1.5) + A(95, 95, 95, 160, EM) + T(103, 158, 'W = m g', a='start', c=EM, w='600', z=11) + A(80, 162, 80, 122, JD) + T(74, 160, 'N', a='end', c=JD, w='600', z=11)
    s += A(130, 90, 180, 90, BL) + T(178, 82, 'P', c=BL, w='600', z=11) + A(70, 116, 24, 116, OR) + T(20, 134, 'friction', a='start', c=OR, z=11) + T(95, 30, 'Free-body diagram:', w='600', z=11) + T(95, 44, 'every force acting', z=11)
    s += T(210, 100, '=', w='600', z=22)
    s += R(260, 70, 70, 50, CR, SL, 1.5) + A(330, 95, 385, 95, EM, 3.5) + T(358, 86, 'm a', c=EM, w='600') + T(300, 30, 'Kinetic diagram:', w='600', z=11) + T(300, 44, 'the mass times its acceleration', z=11)
    s += T(200, 190, 'ΣF = m a in each direction.', w='600', z=11) + T(200, 204, 'Vertically here: N - W = 0 (no vertical acceleration).', z=11)
    return F(212, s, 'Newton\'s second law drawn as two diagrams: the forces on the body (left) add up to its mass times its acceleration (right).')

def dynamics_d():
    s = Ln(30, 180, 110, 180, SL, 2) + hatch(30, 110, 180) + Ln(70, 40, 70, 170, RU, 1, True)
    for y, pe, lab in ((40, 1, 'top: at rest'), (105, 0.5, 'halfway'), (168, 0, 'at the ground')):
        s += Cc(70, y, 9, BL, SL, 1.5) + T(88, y + 4, lab, a='start', z=11)
        s += R(200, y - 8, 160 * pe, 16, BL, 'none', 0, 0.6) if pe else ''
        s += R(200 + 160 * pe, y - 8, 160 * (1 - pe), 16, EM, 'none', 0, 0.85) if pe < 1 else ''
        s += R(200, y - 8, 160, 16, 'none', SL, 1)
    s += A(48, 50, 48, 160, SL, 1.5) + T(44, 108, 'h', a='end', w='600')
    s += R(200, 192, 12, 10, BL, 'none', 0, 0.6) + T(216, 201, 'PE = m g h', a='start', z=11) + R(290, 192, 12, 10, EM, 'none', 0, 0.85) + T(306, 201, 'KE = ½ m v²', a='start', z=11)
    s += T(280, 20, 'With no friction, PE + KE stays the same', w='600', z=11)
    return F(212, s, 'A falling ball: potential energy m g h turns into kinetic energy ½ m v², and with no friction their total stays the same.')


# ---------------- Mechanics of materials ----------------
def mechmat_a():
    x0, x1 = 70, 330; s = R(x0, 40, x1 - x0, 8, CR, SL, 1.5) + udl(x0, x1, 40, 11) + pin(x0, 48) + roller(x1, 48)
    s += T(30, 44, 'Load', a='middle', w='600', z=11)
    yv = 118; s += Ln(x0, yv, x1, yv, SL, 1) + Pa(poly([(x0, yv), (x0, yv - 26), (x1, yv + 26), (x1, yv)], True), LG, JD, 1.5)
    s += T(30, yv + 4, 'Shear V', w='600', z=11) + T(x0 + 4, yv - 30, '+wL/2', a='start', z=11) + T(x1 + 6, yv + 30, '-wL/2', a='start', z=11)
    s += Dot((x0 + x1) / 2, yv) + T((x0 + x1) / 2 + 8, yv - 8, 'V = 0 at midspan', a='start', c=EM, z=11)
    ym = 200; pts = [(x0 + (x1 - x0) * t, ym - 40 * 4 * t * (1 - t)) for t, _ in curve(lambda t: 0, 0, 1)]
    s += Ln(x0, ym, x1, ym, SL, 1) + Pa(poly(pts + [(x1, ym)], True), LG, JD, 1.5) + T(30, ym - 10, 'Moment M', w='600', z=11)
    s += T((x0 + x1) / 2, ym - 46, 'largest where V = 0: wL²/8', c=EM, w='600', z=11)
    s += lines(200, 228, 'Slope of the moment diagram = shear.\nChange in moment = area under the shear diagram.', a='middle', z=11)
    return F(258, s, 'A uniformly loaded simple beam with its shear and moment diagrams stacked: shear falls linearly and crosses zero at midspan, where the moment peaks at wL²/8.')

def mechmat_b1():
    s = R(30, 60, 120, 30, CR, SL, 1.5) + A(30, 75, 4, 75, EM) + A(150, 75, 176, 75, EM) + T(16, 66, 'P', c=EM, w='600') + T(166, 66, 'P', c=EM, w='600')
    s += Ln(100, 50, 100, 100, BL, 1.5, True) + ''.join(A(100, 64 + 7 * i, 120, 64 + 7 * i, BL, 1.2, head=5) for i in range(4))
    s += T(90, 120, 'Normal stress', w='600', z=11) + T(90, 134, 'acts at 90° to the cut', z=11) + T(90, 150, 'σ = P / A', c=EM, w='600')
    s += R(230, 55, 150, 18, CR, SL, 1.5) + R(230, 80, 150, 18, LG, SL, 1.5) + R(296, 45, 18, 64, RU, SL, 1.5)
    s += A(380, 64, 398, 64, EM) + A(230, 89, 212, 89, EM) + Ln(286, 76.5, 324, 76.5, BL, 1.5, True) + ''.join(A(298 + 6 * i, 76.5, 305 + 6 * i, 76.5, BL, 1.2, head=4) for i in range(3))
    s += T(305, 120, 'Shear stress', w='600', z=11) + T(305, 134, 'acts along the cut', z=11) + T(305, 150, 'τ = V / A', c=EM, w='600')
    s += T(200, 176, 'A is the area of the cut surface the stress acts on.', z=11)
    return F(186, s, 'Left: a bar in tension has normal stress P/A acting at right angles to the cut. Right: a bolt between two plates has shear stress V/A acting along the cut.')

def mechmat_b2():
    s = R(60, 40, 140, 120, CR, SL, 1.5) + Ln(50, 100, 210, 100, EM, 1, True) + T(196, 94, 'neutral axis', a='end', c=EM, z=11)
    s += arc(60, 100, 26, 120, 240, BL, 2, True) + T(28, 100, 'M', a='end', c=BL, w='600')
    for i in range(7):
        y = 44 + i * 9; L = 70 * (100 - y) / 56
        s += A(202 + L, y, 202, y, BL, 1.3, head=5) if L > 6 else ''
        y2 = 156 - i * 9; L2 = 70 * (y2 - 100) / 56
        s += A(202, y2, 202 + L2, y2, EM, 1.3, head=5) if L2 > 6 else ''
    s += Ln(272, 44, 202, 100, SL, 1) + Ln(202, 100, 272, 156, SL, 1)
    s += T(280, 52, 'compression (top)', a='start', c=BL, w='600', z=11) + T(280, 154, 'tension (bottom)', a='start', c=EM, w='600', z=11) + T(280, 104, 'zero at the neutral axis', a='start', z=11)
    s += lines(20, 186, 'σ = M c / I. c: distance from the neutral axis to the outer edge;\nI: moment of inertia of the section. Stress grows in a straight\nline with distance from the neutral axis.', z=11)
    return F(234, s, 'Bending stress across a beam section under a sagging moment: compression at the top, tension at the bottom, zero at the neutral axis, largest at the outer edges, σ = M c / I.')

def mechmat_c():
    s = R(40, 40, 200, 24, 'none', SL, 1, None).replace("stroke-width='1'", "stroke-width='1' stroke-dasharray='5 4'") + R(40, 40, 230, 24, CR, SL, 1.5) + wall(40, 30, 74)
    s += dimh(240, 270, 84, 'δ = α L ΔT') + T(300, 56, 'Free to grow:', a='start', w='600', z=11) + T(300, 70, 'no stress', a='start', z=11)
    s += R(40, 120, 230, 24, LG, SL, 1.5) + wall(40, 110, 154) + wall(282, 110, 154, 'right')
    s += A(316, 132, 274, 132, BL) + A(4, 132, 26, 132, BL) + T(300, 112, 'Walls push back:', a='start', w='600', z=11) + T(300, 172, 'σ = E α ΔT', a='start', c=BL, w='600') + T(300, 186, '(compression)', a='start', z=11)
    s += T(150, 180, 'α = expansion per degree', z=11) + T(150, 194, 'ΔT = temperature change', z=11)
    return F(204, s, 'Top: a heated bar free to grow lengthens by α L ΔT with no stress. Bottom: held between rigid walls it cannot grow, so the walls squeeze it with stress E α ΔT.')

def _elem(cx, cy, h, ang, normals, shear=False):
    c = [(cx + h * sqrt(2) * cos(rad(ang + 45 + 90 * k)), cy - h * sqrt(2) * sin(rad(ang + 45 + 90 * k))) for k in range(4)]
    s = Pa(poly(c, True), CR, SL, 1.5)
    for phi, L, col in normals:
        n = (cos(rad(phi)), -sin(rad(phi))); f = (cx + h * n[0], cy + h * n[1])
        s += A(f[0] + 4 * n[0], f[1] + 4 * n[1], f[0] + (4 + L) * n[0], f[1] + (4 + L) * n[1], col, 2.2, head=8)
    if shear:
        for fx, fy, dx, dy in ((h + 7, 0, 0, -1), (-h - 7, 0, 0, 1), (0, -h - 7, 1, 0), (0, h + 7, -1, 0)):
            s += A(cx + fx - 16 * dx, cy + fy - 16 * dy, cx + fx + 16 * dx, cy + fy + 16 * dy, JD, 1.8, head=7)
    return s
def mechmat_d():
    s = _elem(100, 105, 32, 0, [(0, 28, EM), (180, 28, EM), (90, 18, BL), (270, 18, BL)], True)
    s += T(166, 109, 'σx', a='start', c=EM, w='600', z=11) + T(108, 50, 'σy', a='start', c=BL, w='600', z=11) + T(146, 66, 'τ', a='start', c=JD, w='600', z=11)
    s += T(100, 186, 'Any orientation:', w='600', z=11) + T(100, 200, 'normal and shear stress', z=11)
    s += A(178, 150, 222, 150, SL, 1.5) + T(200, 140, 'rotate by θp', z=11)
    th = 25; s += _elem(300, 105, 32, th, [(th, 34, EM), (th + 180, 34, EM), (th + 90, 12, BL), (th + 270, 12, BL)])
    s += Ln(300, 105, 370, 105, RU, 1, True) + arc(300, 105, 48, 0, th) + T(352, 96, 'θp', a='start', z=11)
    s += T(342, 52, 'σ1', a='start', c=EM, w='600', z=11) + T(268, 60, 'σ2', a='end', c=BL, w='600', z=11)
    s += T(300, 186, 'Principal orientation:', w='600', z=11) + T(300, 200, 'no shear; σ1 largest, σ2 smallest', z=11)
    return F(210, s, 'The same state of stress on a square element at two orientations. Rotated by the principal angle θp, the shear disappears and only the principal stresses σ1 and σ2 remain.')


# ---------------- Structural ----------------
def structural_a():
    x0, x1 = 60, 340; s = Ln(x0, 50, x1, 50, RU, 1, True) + pin(x0, 50) + roller(x1, 50)
    f = lambda x: 50 + 26 * sin(math.pi * (x - x0) / (x1 - x0))
    s += Pa(poly([(x, f(x)) for x, _ in curve(lambda x: 0, x0, x1)]), s=SL, wd=4) + Pa(poly([(x, f(x) + 6) for x, _ in curve(lambda x: 0, x0, x1)]), s=EM, wd=2.5)
    s += A(200, 20, 200, 70, BL) + T(206, 28, 'P', a='start', c=BL, w='600') + T(200, 98, 'sags: tension along the bottom (positive moment)', c=EM, w='600', z=11)
    y0 = 140; g = lambda x: y0 + 36 * ((x - x0) / (x1 - x0)) ** 2 * (3 - (x - x0) / (x1 - x0)) / 2
    s += wall(x0, y0 - 30, y0 + 30) + Ln(x0, y0, x1, y0, RU, 1, True) + Pa(poly([(x, g(x)) for x, _ in curve(lambda x: 0, x0, x1)]), s=SL, wd=4) + Pa(poly([(x, g(x) - 6) for x, _ in curve(lambda x: 0, x0, x1)]), s=EM, wd=2.5)
    s += A(x1, y0 - 20, x1, g(x1) - 4, BL) + T(x1 - 8, y0 - 14, 'P', a='end', c=BL, w='600') + T(200, 196, 'cantilever: tension along the top (negative moment)', c=EM, w='600', z=11)
    s += T(390, 214, 'Green line = tension face. Concrete needs its steel on that face.', a='end', z=11)
    return F(222, s, 'Deflected shapes: a simply supported beam sags, with tension along the bottom; a cantilever bends down from its support, with tension along the top. Reinforcing steel goes on the tension face.')

def structural_b():
    s = wall(60, 30, 140); f = lambda t: t * t * (3 - t) / 2
    s += Ln(60, 50, 370, 50, RU, 1, True)
    s += Pa(poly([(60 + 140 * t, 50 + 9 * f(t)) for t, _ in curve(lambda t: 0, 0, 1)]), s=EM, wd=3.5) + A(200, 28, 200, 57, EM, 2) + T(206, 34, 'P', a='start', c=EM, w='600', z=11)
    s += Pa(poly([(60 + 280 * t, 50 + 72 * f(t)) for t, _ in curve(lambda t: 0, 0, 1)]), s=BL, wd=3.5) + A(340, 90, 340, 120, BL, 2) + T(346, 98, 'P', a='start', c=BL, w='600', z=11)
    s += dimv(214, 50, 59, 'δ', EM) + dimv(356, 50, 122, '8 δ', BL)
    s += T(130, 76, 'span L', c=EM, w='600', z=11) + T(270, 136, 'span 2L', c=BL, w='600', z=11)
    s += lines(20, 168, 'Tip deflection δ = P L³ / (3 E I).\nDouble the span: 2³ = 8 times the deflection. Double E (stiffer material) or\nI (deeper section): half the deflection.', z=11)
    return F(214, s, 'Two cantilevers with the same tip load: doubling the span multiplies the tip deflection by eight, because deflection grows with L cubed and falls with E I.')

def structural_c():
    s = ''; cols = ((55, 'Pinned-pinned', '1.0', lambda u: sin(math.pi * u), 'pin', 'pin'), (150, 'Fixed-free', '2.0', lambda u: 1 - cos(math.pi * u / 2), 'fix', 'free'),
                    (245, 'Fixed-pinned', '0.7', lambda u: 6.75 * u * u * (1 - u), 'fix', 'pin'), (340, 'Fixed-fixed', '0.5', lambda u: (1 - cos(2 * math.pi * u)) / 2, 'fix', 'fix'))
    for cx, name, K, fn, bot, top in cols:
        yb, yt = 176, 46; amp = 30 if top == 'free' else 18
        s += Ln(cx, yb, cx, yt, RU, 1, True) + Pa(poly([(cx + amp * fn((yb - y) / (yb - yt)), y) for y, _ in curve(lambda y: 0, yb, yt)]), s=EM, wd=3)
        s += pin(cx, yb) if bot == 'pin' else R(cx - 16, yb, 32, 10, RU, SL, 1.5)
        tx = cx + amp * fn(1)
        if top == 'pin': s += Pa(f"M{cx} {yt} L{cx - 9} {yt - 13} L{cx + 9} {yt - 13} Z", WH, SL, 1.5)
        elif top == 'fix': s += R(cx - 16, yt - 10, 32, 10, RU, SL, 1.5)
        s += A(tx, 10, tx, yt - (14 if top != 'free' else 2), BL, 2) + T(cx, 218, name, w='600', z=11) + T(cx, 234, f"K = {K}", c=EM, w='600', z=12)
    s += T(200, 256, 'Effective length = K L; buckling load P = π² E I / (K L)².', w='600', z=11) + T(200, 270, 'More end restraint: shorter K L, higher buckling load.', z=11)
    return F(278, s, 'Buckled shapes of columns with different end supports and their effective length factors: pinned both ends K = 1.0, fixed-free K = 2.0, fixed-pinned K = 0.7, fixed both ends K = 0.5.')

def structural_d():
    s = ''
    rows = ((45, 'pin+roller', 'Pin + roller: 3 reactions', '= 3 equations: determinate', EM), (115, 'fix+roller', 'Fixed + roller: 4 reactions', 'one extra: indeterminate', BL), (185, 'roller+roller', 'Two rollers: nothing', 'resists sliding: unstable', OR))
    for y, kind, l1, l2, col in rows:
        s += R(40, y, 180, 8, CR, SL, 1.5)
        if kind == 'pin+roller': s += pin(40, y + 8) + roller(220, y + 8)
        elif kind == 'fix+roller': s += wall(40, y - 20, y + 30) + roller(220, y + 8)
        else: s += roller(40, y + 8) + roller(220, y + 8)
        s += T(240, y + 2, l1, a='start', z=11) + T(240, y + 16, l2, a='start', c=col, w='600', z=11)
    s += A(4, 207, 26, 207, OR, 2) + T(200, 236, 'Degree of indeterminacy of a beam = reactions - 3 (if stable).', z=11)
    return F(244, s, 'Three beams: a pin and a roller give three reactions and are determinate; a fixed end and a roller give four and are indeterminate to the first degree; two rollers cannot resist sideways load and are unstable.')
def structural_e():
    s = ''; f = lambda t: t * t * (3 - t) / 2
    s += wall(40, 20, 64) + R(40, 38, 200, 8, CR, SL, 1.5) + udl(40, 240, 38, 9) + roller(240, 46) + T(140, 14, 'Actual beam: fixed end and a prop', z=11)
    s += T(140, 84, '=', w='600', z=18)
    s += wall(40, 98, 142) + Ln(40, 116, 240, 116, RU, 1, True) + udl(40, 240, 116, 9) + Pa(poly([(40 + 200 * t, 116 + 30 * f(t)) for t, _ in curve(lambda t: 0, 0, 1)]), s=SL, wd=4)
    s += dimv(256, 116, 146, 'Δ', EM) + T(140, 166, '+', w='600', z=18)
    s += wall(40, 176, 220) + Ln(40, 202, 240, 202, RU, 1, True) + Pa(poly([(40 + 200 * t, 202 - 30 * f(t)) for t, _ in curve(lambda t: 0, 0, 1)]), s=SL, wd=4) + A(240, 236, 240, 176, BL, 2.5) + T(248, 232, 'R', a='start', c=BL, w='600')
    s += lines(282, 60, 'Take away the\nextra support.\nFind how far the\nbeam moves there (Δ).\nFind the force R\nthat pushes it\nback by Δ.\nTotal movement\nat the prop = 0.', z=11)
    return F(244, s, 'A propped cantilever solved by superposition: remove the prop, find the deflection Δ there, then find the prop force R that pushes the beam back by the same amount.')

def structural_f():
    s = ''
    for y in (40, 110):
        s += R(50, y - 6, 200, 8, CR, SL, 1.5) + udl(55, 245, y - 6, 8, EM, 14)
    s += R(66, 34, 10, 146, RU, SL, 1.5) + R(224, 34, 10, 146, RU, SL, 1.5) + R(51, 180, 40, 12, CR, SL, 1.5) + R(209, 180, 40, 12, CR, SL, 1.5)
    s += Ln(20, 192, 280, 192, SL, 2) + ''.join(A(56 + 10 * i, 208, 56 + 10 * i, 194, JD, 1.2, head=5) for i in range(4)) + ''.join(A(214 + 10 * i, 208, 214 + 10 * i, 194, JD, 1.2, head=5) for i in range(4))
    s += A(90, 50, 90, 150, BL, 2) + T(96, 70, 'down through', a='start', c=BL, z=10) + T(96, 82, 'the columns', a='start', c=BL, z=10) + T(150, 222, 'soil pushes back on the footings', c=JD, z=11)
    labs = ('Slab', 'Beam', 'Girder', 'Column', 'Footing', 'Soil')
    for i, t in enumerate(labs):
        y = 14 + i * 32; s += box(300, y, 86, 22, t, LG if i in (0, 5) else CR, SL, SL, 11)
        if i < 5: s += A(343, y + 22, 343, y + 31, SL, 1.5, head=6)
    s += T(343, 222, 'the load path', w='600', z=11)
    return F(230, s, 'The load path: floor and roof loads go from the slab to the beams, girders and columns, down to the footings and into the soil. Each member carries the load from its tributary area.')

def structural_g():
    s = R(40, 50, 300, 90, CR, SL, 1.5) + Cc(200, 75, 9, WH) + Cc(200, 115, 9, WH)
    s += A(40, 95, 6, 95, EM, 3) + A(340, 95, 380, 95, EM, 3) + T(10, 84, 'P', a='start', c=EM, w='600') + T(374, 84, 'P', c=EM, w='600')
    s += Ln(110, 40, 110, 150, BL, 2, True) + T(110, 168, 'gross section Ag', c=BL, w='600', z=11) + T(110, 182, '(full width)', c=BL, z=11)
    s += Ln(200, 40, 200, 150, OR, 2, True) + T(200, 30, 'net section An: width minus the holes', c=OR, w='600', z=11)
    s += lines(250, 168, 'Yielding: φ = 0.90 on Ag Fy\nRupture: φ = 0.75 on Ae Fu\nThe smaller strength governs.', z=11)
    return F(214, s, 'A plate in tension with two bolt holes. It can yield along its full width (gross area) or tear through the holes (net area); the design strength is the smaller of the two.')

def structural_h():
    s = R(40, 30, 70, 160, CR, SL, 1.5) + ''.join(Cc(54 + 14 * i, 172, 5, SL) for i in range(4)) + T(75, 210, 'section', z=11)
    s += Ln(30, 90, 400, 90, EM, 1, True) + T(398, 84, 'neutral axis', a='end', c=EM, z=10)
    s += Ln(190, 30, 190, 190, SL, 1) + Pa(poly([(160, 30), (190, 90), (220, 172)]), s=SL, wd=2) + Ln(160, 30, 190, 30, SL, 1) + Ln(190, 172, 220, 172, SL, 1)
    s += T(156, 26, 'εc = 0.003', a='end', z=11) + T(226, 176, 'εs', a='start', z=11) + T(190, 210, 'strain', z=11) + dimv(130, 30, 90, 'c', SL, 'left')
    a = 51; s += R(270, 30, 40, a, LG, JD, 1.5) + T(290, 24, '0.85 f′c', c=JD, z=11) + dimv(262, 30, 30 + a, 'a', SL, 'left')
    s += A(330, 30 + a / 2, 312, 30 + a / 2, BL, 2.5) + T(336, 30 + a / 2 + 4, 'C', a='start', c=BL, w='600') + A(312, 172, 350, 172, EM, 2.5) + T(356, 176, 'T', a='start', c=EM, w='600')
    s += dimv(386, 30 + a / 2, 172, 'd - a/2', SL, 'left') + T(310, 210, 'forces', z=11)
    s += T(200, 232, 'a = β1 c.  C = 0.85 f′c a b = T = As fy.  Mn = T (d - a/2).', w='600', z=11)
    return F(240, s, 'A reinforced concrete beam at strength: strain grows linearly from the neutral axis (0.003 at the top); concrete compression is a rectangular block of depth a; C equals T and they form a couple with lever arm d - a/2.')


# ---------------- Fluid mechanics ----------------
def fluids_a():
    top = [(20, 100), (110, 100), (160, 122), (200, 122), (290, 100), (380, 100)]; bot = [(x, 280 - y) for x, y in top]
    s = Pa(poly(top + bot[::-1], True), BL, 'none', 0, op=0.25) + Pa(poly(top), s=SL, wd=2.5) + Pa(poly(bot), s=SL, wd=2.5)
    for x, yb, yw in ((65, 100, 38), (180, 122, 80)):
        s += R(x - 5, 22, 10, yb - 22, 'none', SL, 1.2) + R(x - 4, yw, 8, yb - yw, BL, 'none', 0, 0.6)
    s += Ln(65, 38, 250, 38, SL, 1, True) + Ln(180, 80, 250, 80, SL, 1, True) + dimv(250, 38, 80, 'Δh: pressure drop', SL)
    s += A(30, 140, 80, 140, BL, 2) + A(150, 140, 230, 140, BL, 3) + T(55, 160, 'slow,', z=11) + T(55, 174, 'high pressure', z=11) + T(180, 196, 'throat: fast, low pressure', z=11)
    s += lines(200, 222, 'Continuity: A1 V1 = A2 V2. The speed gained at the throat comes\nfrom pressure, so the drop Δh gives the flow:\nQ = Cd A2 √(2 g Δh / (1 - (A2/A1)²))', a='middle', z=11)
    return F(262, s, 'A Venturi meter: the flow speeds up through the narrow throat, its pressure drops, and the drop Δh read on the tubes gives the flow rate.')

def fluids_b():
    s = Ln(40, 170, 330, 170, SL, 2) + hatch(40, 330, 170) + R(40, 50, 290, 10, CR, SL, 1.5) + A(330, 55, 376, 55, EM, 3) + T(372, 46, 'V', c=EM, w='600')
    s += R(40, 60, 290, 110, BL, 'none', 0, 0.15)
    for i in range(1, 8):
        y = 170 - i * 13.75; L = 120 * i / 8
        s += A(100, y, 100 + L, y, BL, 1.4, head=6)
    s += Ln(100, 170, 220, 60, SL, 1, True) + dimv(60, 60, 170, 'y', SL, 'left') + T(18, 200, 'Moving plate drags the fluid; the fixed plate holds it back.', a='start', z=11)
    s += lines(236, 100, 'τ = μ du/dy\n   = μ V / y\nF = τ × plate area\nμ = viscosity', z=11)
    return F(210, s, 'Viscosity: fluid between a moving plate and a fixed plate. The velocity grows linearly across the gap, and the shear stress is the viscosity times that velocity gradient.')

def fluids_c1():
    s = ''; base = 160; h = 100
    for x, shape in ((30, 'tall'), (140, 'wide'), (290, 'flare')):
        if shape == 'tall': pts = [(x + 20, base - h - 20), (x + 20, base), (x + 60, base), (x + 60, base - h - 20)]; w = [(x + 20, base - h), (x + 20, base), (x + 60, base), (x + 60, base - h)]
        elif shape == 'wide': pts = [(x, base - h - 20), (x, base), (x + 120, base), (x + 120, base - h - 20)]; w = [(x, base - h), (x, base), (x + 120, base), (x + 120, base - h)]
        else: pts = [(x - 10, base - h - 20), (x + 25, base), (x + 65, base), (x + 100, base - h - 20)]; w = [(x - 6.5, base - h), (x + 25, base), (x + 65, base), (x + 96.5, base - h)]
        s += Pa(poly(w, True), BL, 'none', 0, op=0.3) + Pa(poly(pts), s=SL, wd=2.5)
    s += Ln(10, base - h, 395, base - h, BL, 1, True) + dimv(14, base - h, base, 'h', SL, 'right')
    s += T(200, base + 20, 'The bottom pressure is the same in all three: p = γ h', c=EM, w='600', z=11) + T(200, base + 36, 'Pressure depends on depth only, not on the shape or the amount of water.', z=11)
    return F(206, s, 'Three containers of different shapes filled to the same depth h have the same pressure at the bottom, p = γ h: hydrostatic pressure depends only on depth.')

def fluids_c2():
    s = R(20, 80, 360, 100, BL, 'none', 0, 0.25) + Ln(20, 80, 380, 80, BL, 2)
    s += R(150, 50, 100, 70, CR, SL, 1.5) + R(150, 80, 100, 40, LG, 'none', 0, 0.9) + R(150, 50, 100, 70, 'none', SL, 1.5)
    s += A(200, 70, 200, 150, EM, 2.5) + T(208, 148, 'W', a='start', c=EM, w='600') + A(176, 140, 176, 98, BL, 2.5) + T(170, 136, 'FB', a='end', c=BL, w='600')
    s += T(258, 110, 'displaced water', a='start', c=JD, w='600', z=11)
    s += lines(20, 196, 'Buoyant force FB = γ water × volume of water displaced.\nA floating body sinks until FB = W.\nFully submerged: FB uses the whole volume.', z=11)
    return F(240, s, 'A floating block: the water pushes up with a buoyant force equal to the weight of the water it displaces, and it floats when that equals its own weight.')

def fluids_d():
    s = Pa('M20 40 L20 190 L90 190 L90 172', s=SL, wd=2) + R(20, 40, 70, 150, BL, 'none', 0, 0.25) + Ln(20, 40, 90, 40, BL, 2) + Ln(90, 160, 90, 40, SL, 2)
    s += R(90, 160, 290, 12, BL, SL, 1.5, 0.25) + Ln(10, 205, 390, 205, SL, 1.5) + T(390, 200, 'datum', a='end', z=11)
    egl = lambda x: 44 + (80 - 44) * (x - 95) / 285; hgl = lambda x: egl(x) + 22
    s += Ln(95, egl(95), 380, egl(380), EM, 2.5) + Ln(95, hgl(95), 380, hgl(380), BL, 2.5, True)
    s += T(100, egl(100) - 6, 'energy line (EGL)', a='start', c=EM, w='600', z=11) + T(100, hgl(100) + 26, 'hydraulic grade line (HGL)', a='start', c=BL, w='600', z=11)
    x = 310; s += dimv(x, 166, 205, 'z') + dimv(x, hgl(x), 166, 'p / γ') + dimv(x, egl(x), hgl(x), 'V²/2g')
    s += lines(10, 228, 'Total head = z (elevation) + p/γ (pressure head) + V²/2g (velocity head).\nBoth lines slope down by the friction loss along the pipe.', z=11)
    return F(254, s, 'Energy and hydraulic grade lines for a pipe fed by a reservoir: at any point, total head is elevation plus pressure head plus velocity head, and both lines drop by the friction loss.')

# ---------------- Water resources and environmental ----------------
def water_a():
    s = axes(50, 200, 385, 30, 'time', '') + T(44, 120, 'Q', a='end', w='600', z=11) + Ln(50, 30, 385, 30, SL, 1.5)
    for i, hgt in enumerate((14, 30, 40, 22, 10)):
        s += R(70 + i * 12, 30, 12, hgt, BL, SL, 0.8, 0.8)
    s += T(140, 46, 'rainfall', a='start', c=BL, w='600', z=11)
    q = lambda x: 180 - (8 + 120 * ((x - 80) / 110 * exp(1 - (x - 80) / 110)) ** 3) if x > 80 else 172
    pts = [(x, q(x)) for x, _ in curve(lambda x: 0, 50, 380, 90)]
    s += Pa(poly([(80, 172)] + [p for p in pts if p[0] >= 80] + [(380, 172)], True), LG, 'none', 0) + Ln(50, 172, 385, 172, SL, 1, True) + Pa(poly(pts), s=JD, wd=2.5)
    s += T(386, 168, 'baseflow', a='end', z=10) + T(190, 44 + 0, '', z=1) + Dot(190, q(190)) + T(196, q(190) - 6, 'peak flow', a='start', c=EM, w='600', z=11)
    s += T(128, 140, 'rising', a='end', z=11) + T(300, 112, 'recession', a='start', z=11) + T(210, 160, 'runoff volume = area', c=EM, w='600', z=11)
    s += dimh(100, 190, 82, 'lag time', SL, False)
    return F(222, s, 'A storm hydrograph: after the rainfall, streamflow rises to a peak and recedes; the shaded area above baseflow is the volume of direct runoff, and the delay to the peak is the lag time.')

def water_b():
    X = lambda E: 55 + E * 95; Y = lambda y: 200 - y * 52; K = 0.5
    s = axes(55, 200, 385, 20, 'specific energy E', 'depth y') + Ln(X(0), Y(0), X(3.3), Y(3.3), RU, 1, True)
    pts = [(X(y + K / y / y), Y(y)) for y, _ in curve(lambda y: 0, 0.44, 3.2, 80)]
    s += Pa(poly(pts), s=JD, wd=2.5) + Dot(X(1.5), Y(1)) + Ln(X(0), Y(1), X(1.5), Y(1), SL, 1, True) + T(X(0) + 4, Y(1) - 5, 'yc', a='start', w='600', z=11)
    s += T(X(1.5) + 8, Y(1) + 4, 'critical depth: least energy', a='start', c=EM, w='600', z=11)
    s += Ln(X(2.2), Y(0), X(2.2), Y(2.3), SL, 1, True) + Dot(X(2.2), Y(2.085), BL) + Dot(X(2.2), Y(0.551), BL) + T(X(2.2) + 6, Y(1.5), 'alternate depths', a='start', c=BL, z=11)
    s += T(X(2.15), Y(2.6), 'subcritical: deep, slow', a='end', z=11) + T(X(1.7), Y(0.25), 'supercritical: shallow, fast', a='end', z=11)
    s += T(X(0.2), 36, 'E = y + V²/2g', a='start', w='600', z=11)
    return F(222, s, 'The specific energy curve for a given flow per unit width: each energy above the minimum has two possible depths, subcritical and supercritical; the minimum is at critical depth.')

def water_c():
    X = lambda Q: 60 + Q * 30; Y = lambda H: 195 - H * 1.6
    s = axes(60, 195, 385, 20, 'flow Q', 'head H')
    s += Pa(poly([(X(q), Y(100 - 0.6 * q * q)) for q, _ in curve(lambda q: 0, 0, 10)]), s=EM, wd=2.5) + Pa(poly([(X(q), Y(30 + 0.5 * q * q)) for q, _ in curve(lambda q: 0, 0, 10)]), s=BL, wd=2.5)
    qo = sqrt(70 / 1.1); ho = 30 + 0.5 * qo * qo
    s += Dot(X(qo), Y(ho), SL, 5) + Ln(X(qo), Y(ho), X(qo), 195, SL, 1, True) + T(X(qo) + 8, Y(ho) + 18, 'operating point', a='start', w='600', z=11)
    s += T(X(3), 36, 'pump curve', a='start', c=EM, w='600', z=11) + T(X(9.7), Y(30 + 0.5 * 94) - 8, 'system curve', a='end', c=BL, w='600', z=11)
    s += dimv(X(0) + 12, Y(30), 195, 'static lift', BL) + T(X(5), Y(30 + 12.5) + 30, 'friction losses grow with Q²', c=BL, z=11)
    return F(212, s, 'The pump curve falls as flow rises; the system curve starts at the static lift and rises with friction loss. The pump runs where the two cross.')

def water_d():
    s = Dot(20, 60, SL) + T(20, 50, 'A', w='600') + R(20, 54, 80, 12, BL, SL, 1.2, 0.3) + R(100, 56, 80, 8, BL, SL, 1.2, 0.3) + Dot(180, 60, SL) + T(180, 50, 'B', w='600')
    s += T(60, 86, 'pipe 1', z=10) + T(140, 86, 'pipe 2', z=10) + T(100, 112, 'Series', w='600', z=12) + lines(100, 130, 'same flow Q through both\nhead losses add:\nhL = h1 + h2', a='middle', z=11)
    s += Dot(230, 60, SL) + T(222, 64, 'A', a='end', w='600') + Dot(380, 60, SL) + T(388, 64, 'B', a='start', w='600')
    s += Pa('M230 60 Q305 18 380 60', s=BL, wd=6) + Pa('M230 60 Q305 102 380 60', s=BL, wd=4) + T(305, 30, 'pipe 1', z=10) + T(305, 98, 'pipe 2', z=10)
    s += T(305, 122, 'Parallel', w='600', z=12) + lines(305, 140, 'same head loss in each\nflows add:\nQ = Q1 + Q2', a='middle', z=11)
    return F(190, s, 'Pipes in series carry the same flow and their head losses add; pipes in parallel have the same head loss and their flows add.')

def water_e():
    s = axes(50, 200, 385, 25, 'time', 'flow')
    I = lambda x: 150 * ((x - 50) / 90 * exp(1 - (x - 50) / 90)) ** 3 if x > 50 else 0
    O = lambda x: 87.8 * ((x - 50) / 155 * exp(1 - (x - 50) / 155)) ** 2 if x > 50 else 0
    Y = lambda v: 200 - v
    s += Pa(poly([(x, Y(I(x))) for x, _ in curve(lambda x: 0, 50, 205, 60)] + [(x, Y(O(x))) for x, _ in curve(lambda x: 0, 205, 50, 60)], True), LG, 'none', 0)
    s += Pa(poly([(x, Y(I(x))) for x, _ in curve(lambda x: 0, 50, 380, 90)]), s=BL, wd=2.5) + Pa(poly([(x, Y(O(x))) for x, _ in curve(lambda x: 0, 50, 380, 90)]), s=EM, wd=2.5)
    s += T(112, 58, 'inflow', a='end', c=BL, w='600', z=11) + T(270, 112, 'outflow', a='start', c=EM, w='600', z=11) + T(160, 150, 'stored', c=JD, w='600', z=11)
    s += Ln(140, Y(150), 220, Y(150), SL, 1, True) + Ln(205, Y(87.8), 220, Y(87.8), SL, 1, True) + dimv(220, Y(150), Y(87.8), 'peak cut', SL) + dimh(140, 205, Y(150) - 14, 'peak delayed', SL, False)
    return F(222, s, 'A detention pond stores part of the storm runoff: the outflow peak is lower and later than the inflow peak, and the shaded area is the volume held in storage.')

def water_f():
    shed = [(50, 40), (150, 22), (240, 48), (290, 120), (240, 180), (160, 196), (80, 170), (30, 110)]
    s = Pa(poly(shed, True), LG, JD, 2) + Pa(poly([(160, 196), (184, 130), (240, 100), (264, 120), (240, 180)], True), CR, 'none', 0)
    s += Pa(poly(shed, True), 'none', JD, 2) + Dot(160, 196, SL, 5) + T(168, 212, 'outlet', a='start', w='600', z=11)
    s += Pa('M60 58 Q100 100 120 136 Q140 172 160 196', s=BL, wd=2, dash=True) + Dot(60, 58, BL) + T(68, 54, 'farthest point', a='start', c=BL, z=11)
    s += T(132, 104, 'travel time from here', a='start', c=BL, w='600', z=10) + T(132, 116, '= time of concentration tc', a='start', c=BL, w='600', z=10)
    s += T(222, 162, 'paved: C high', c=SL, w='600', z=11) + T(96, 150, 'grass: C low', c=JD, w='600', z=11)
    s += lines(300, 36, 'Q = C i A\n\nC: runoff coefficient\n(share of rain that\nruns off)\ni: intensity for a\nstorm lasting tc\nA: drainage area', z=10, dy=13)
    return F(222, s, 'The rational method: peak runoff Q = C i A occurs when the whole watershed is contributing, so the rainfall intensity is taken for a storm lasting the time of concentration.')
def water_g():
    s = Pa('M10 40 Q100 34 200 46 T390 44', s=SL, wd=2) + R(60, 42, 20, 108, CR, SL, 1.5) + R(310, 45, 20, 130, CR, SL, 1.5) + T(70, 30, 'manhole', z=10) + T(320, 30, 'manhole', z=10)
    s += Pa(poly([(80, 128), (310, 153), (310, 165), (80, 140)], True), WH, SL, 1.5) + Pa(poly([(80, 134), (310, 159), (310, 165), (80, 140)], True), BL, 'none', 0, op=0.6)
    s += A(150, 118, 230, 127, BL, 1.5) + T(190, 112, 'flow', c=BL, z=11)
    s += T(196, 166, 'invert (inside bottom)', a='end', z=10) + Ln(198, 162, 205, 152, SL, 1) + T(130, 118, 'crown', a='end', z=10)
    s += Ln(80, 140, 356, 140, SL, 1, True) + dimv(350, 140, 165, 'drop') + dimh(80, 310, 186, 'length L')
    s += lines(20, 214, 'Gravity flow, usually partly full. Slope S = drop / L.\nSize with Manning\'s equation; keep the velocity high enough\n(about 2 ft/s, 0.6 m/s) to carry the solids along.', z=11)
    return F(256, s, 'A gravity sewer between two manholes: flow runs partly full down the slope, which is the invert drop over the length; the pipe is sized so the velocity stays high enough to carry solids.')

def water_h():
    base = 215; Hh, hw, rw, Rr, xw = 145, 70, 8, 330, 50
    h = lambda r: sqrt(hw * hw + (Hh * Hh - hw * hw) * log10(r / rw) / log10(Rr / rw)) if r > rw else hw
    base = 215; s = R(10, base - Hh - 15, 380, Hh + 15, CR, 'none', 0) + hatch(10, 390, base) + Ln(10, base - Hh - 15, 390, base - Hh - 15, SL, 2)
    pts = [(xw + r, base - h(r)) for r, _ in curve(lambda r: 0, rw, Rr, 80)]
    s += Pa(poly([(xw + rw, base)] + pts + [(390, base - Hh), (390, base)], True), BL, 'none', 0, op=0.3) + Pa(poly(pts), s=BL, wd=2.5) + Ln(xw, base - Hh, 390, base - Hh, BL, 1, True)
    s += R(xw - 6, base - Hh - 30, 12, Hh + 30, WH, SL, 1.5) + A(xw, base - Hh - 32, xw, base - Hh - 52, EM, 2) + T(xw + 8, base - Hh - 40, 'pumping Q', a='start', c=EM, w='600', z=11)
    for r, lab in ((110, 'h1'), (230, 'h2')):
        s += R(xw + r - 3, base - Hh - 15, 6, Hh + 15, WH, SL, 1) + dimv(xw + r + 12, base - h(r), base, lab, SL)
    s += T(330, base - Hh - 22, 'original water table', c=BL, z=10) + Ln(330, base - Hh - 18, 330, base - Hh, BL, 1) + T(170, base - Hh - 22, 'cone of depression', c=BL, w='600', z=11) + Ln(170, base - Hh - 18, 170, base - h(120), BL, 1)
    s += T(200, 236, 'Unconfined: Q = π K (h2² - h1²) / ln(r2 / r1)', w='600', z=11) + T(200, 250, 'h measured up from the impervious base; r from the pumped well', z=10)
    return F(258, s, 'A well pumping an unconfined aquifer draws the water table down into a cone of depression; the water levels h1 and h2 in two observation wells give the permeability K.')

def water_i():
    X = lambda t: 55 + t * 16; Y = lambda b: 190 - b * 140
    s = axes(55, 190, 385, 25, 'time (days)', 'oxygen used (BOD)') + Ln(55, Y(1), 380, Y(1), SL, 1, True) + T(380, Y(1) - 6, 'ultimate BOD, L0', a='end', w='600', z=11)
    s += Pa(poly([(X(t), Y(1 - exp(-0.23 * t))) for t, _ in curve(lambda t: 0, 0, 20)]), s=EM, wd=2.5)
    b5 = 1 - exp(-0.23 * 5); s += Ln(X(5), 190, X(5), Y(b5), SL, 1, True) + Ln(55, Y(b5), X(5), Y(b5), SL, 1, True) + Dot(X(5), Y(b5)) + T(X(5), 206, '5', z=11) + T(X(5) + 8, Y(b5) + 14, 'BOD5: measured at 5 days', a='start', c=EM, w='600', z=11)
    s += lines(X(8), Y(0.36), 'BOD_t = L0 (1 - e^(-k t))\nk = rate constant, per day\nBacteria use oxygen as they\nbreak down organic matter.', z=11)
    return F(212, s, 'Biochemical oxygen demand: the oxygen used by bacteria rises toward the ultimate BOD L0; the standard test reads it at 5 days.')

def water_j():
    s = ''
    for y, name, g, m in ((50, 'Most contaminants', 160, 160), (130, 'Carcinogens', 40, 140)):
        s += T(20, y - 18, name, a='start', w='600', z=11) + Ln(40, y, 380, y, SL, 2) + R(m, y - 7, 380 - m, 14, OR, 'none', 0, 0.25) + Ln(40, y - 6, 40, y + 6, SL, 1.5)
        if g != 40: s += T(40, y + 20, '0', z=11)
        s += Ln(g, y - 10, g, y + 10, JD, 3) + T(g, y + 22, 'MCLG' if g != 40 else 'MCLG = 0', c=JD, w='600', z=11, a='middle' if g != 40 else 'start')
        s += (Ln(m, y - 10, m, y + 10, EM, 3) + T(m, y + 22, 'MCL', c=EM, w='600', z=11)) if m != g else T(m, y - 14, 'MCL', c=EM, w='600', z=11)
        s += T(375, y - 12, 'violation', a='end', c=OR, w='600', z=10)
    s += lines(20, 180, 'MCLG: health goal, no expected effect; not enforced.\nMCL: the enforceable limit, as close to the goal as treatment allows.\nFor carcinogens the goal is zero but the MCL is not.', z=11)
    return F(226, s, 'Drinking water standards on a concentration scale: the MCLG is a non-enforceable health goal and the MCL the enforceable limit; for carcinogens the goal is zero while the limit is above zero.')
def _train(steps, rows, w=84, h=36, gx=12, y0=30, gy=60):
    s = ''; pos = []
    for i, t in enumerate(steps):
        r, c = divmod(i, rows); c = c if r % 2 == 0 else rows - 1 - c
        x, y = 10 + c * (w + gx), y0 + r * gy; pos.append((x, y)); s += box(x, y, w, h, t, LG if i in (0, len(steps) - 1) else CR, SL, SL, 10)
    for (x1, y1), (x2, y2) in zip(pos, pos[1:]):
        if y1 == y2: s += A(x1 + w if x2 > x1 else x1, y1 + h / 2, x2 if x2 > x1 else x2 + w, y2 + h / 2, SL, 1.5, head=7)
        else: s += A(x1 + w / 2, y1 + h, x2 + w / 2, y2, SL, 1.5, head=7)
    return s, pos
def water_k1():
    s, pos = _train(['Intake', 'Coagulation\n(rapid mix)', 'Flocculation\n(slow mix)', 'Sedimentation', 'Filtration', 'Disinfection', 'Distribution'], 4)
    s += T(200, 16, 'Drinking water: remove particles, then kill what is left', w='600', z=11)
    s += lines(10, 150, 'Coagulant (alum) makes fine particles stick together; the flocs settle;\nfilters catch the rest; chlorine kills pathogens and keeps a residual\nin the pipes.', z=10, dy=13)
    return F(190, s, 'A conventional drinking water treatment train: intake, coagulation, flocculation, sedimentation, filtration and disinfection before distribution.')
def water_k2():
    s, pos = _train(['Screening', 'Grit removal', 'Primary\nclarifier', 'Aeration tank\n(bacteria)', 'Secondary\nclarifier', 'Disinfection', 'Discharge'], 4)
    (xa, ya), (xs, ys) = pos[3], pos[4]
    s += Pa(f"M{xs + 84} {ys + 18} L{xs + 96} {ys + 18} L{xs + 96} {ya + 18}", s=EM, wd=1.5) + A(xs + 96, ya + 18, xa + 85, ya + 18, EM, 1.5, head=7)
    s += T(200, 16, 'Wastewater: settle solids, then let bacteria eat the dissolved organics', w='600', z=11)
    s += lines(10, 150, 'Primary treatment settles solids. In secondary treatment, bacteria in the\naeration tank eat the organic matter (BOD), then settle in the secondary\nclarifier; part of that sludge is returned (green arrow) to keep them working.', z=10, dy=13)
    return F(190, s, 'A conventional wastewater treatment train: screening, grit removal, primary clarifier, activated sludge aeration with sludge return from the secondary clarifier, then disinfection and discharge.')


# ---------------- Geotechnical ----------------
def geotech_a1():
    X = lambda d: 60 + (log10(10) - log10(d)) * 100; Y = lambda p: 200 - p * 1.6
    s = Ln(60, 200, 380, 200, SL, 1.5) + Ln(60, 200, 60, 36, SL, 1.5) + T(220, 228, 'particle size, mm (log scale, coarse on the left)', z=11) + T(54, 30, 'percent finer', a='start', z=11)
    for d in (10, 1, 0.1, 0.01): s += Ln(X(d), 200, X(d), 205, SL, 1) + T(X(d), 216, str(d), z=10)
    for p in (0, 50, 100): s += T(54, Y(p) + 4, str(p), a='end', z=10)
    pf = lambda d, d50, w: 100 / (1 + exp(-(log10(d) - log10(d50)) / w))
    for d50, w, col, lab, lx in ((0.5, 0.35, EM, 'well graded: Cu = 8.2, Cc = 1.1', 0.04), (0.25, 0.08, BL, 'poorly graded: Cu = 1.6', 0.06)):
        s += Pa(poly([(X(10 ** e), Y(pf(10 ** e, d50, w))) for e, _ in curve(lambda e: 0, 1, -2, 90)]), s=col, wd=2.5)
    for d, p, lab in ((0.085, 10, 'D10'), (0.252, 30, 'D30'), (0.693, 60, 'D60')):
        s += Ln(60, Y(p), X(d), Y(p), SL, 1, True) + Ln(X(d), Y(p), X(d), 200, SL, 1, True) + T(64, Y(p) - 3, lab, a='start', c=EM, w='600', z=10)
    s += T(375, 60, 'well graded: Cu = 8.2, Cc = 1.1', a='end', c=EM, w='600', z=11) + T(375, 76, 'poorly graded: Cu = 1.6', a='end', c=BL, w='600', z=11)
    s += T(375, 96, 'Cu = D60 / D10', a='end', z=11) + T(375, 110, 'Cc = D30² / (D10 × D60)', a='end', z=11)
    return F(236, s, 'Grain size curves: a well graded soil has a wide spread of sizes and a gentle curve; a poorly graded soil has a steep one. D10, D30 and D60 give the coefficients of uniformity and curvature.')

def geotech_a2():
    s = A(20, 70, 385, 70, SL, 2, head=9) + T(385, 92, 'water content w', a='end', z=11)
    for x, lab in ((110, 'SL'), (200, 'PL'), (300, 'LL')): s += Ln(x, 56, x, 84, SL, 2) + T(x, 50, lab, w='600', z=11)
    for x1, x2, lab, f in ((20, 110, 'solid', RU), (110, 200, 'semisolid', CR), (200, 300, 'plastic', LG), (300, 380, 'liquid', BL)):
        s += R(x1, 98, x2 - x1, 22, f, 'none', 0, 0.6 if f == BL else None) + T((x1 + x2) / 2, 113, lab, z=11, w='600')
    s += dimh(200, 300, 30, 'plasticity index PI = LL - PL', EM, False)
    s += lines(20, 146, 'Liquidity index LI = (w - PL) / PI:\nbelow 0 the soil is stiff; above 1 it behaves like a liquid.', z=11)
    return F(170, s, 'Atterberg limits on a water content scale: the shrinkage, plastic and liquid limits separate the solid, semisolid, plastic and liquid states, and the plasticity index is LL minus PL.')

def geotech_b():
    x0, x1 = 140, 230; s = box(x0, 30, x1 - x0, 40, 'Air', WH, SL, SL, 11) + box(x0, 70, x1 - x0, 50, 'Water', BL, SL, SL, 11, op=0.35) + box(x0, 120, x1 - x0, 80, 'Solids', RU, SL, SL, 11)
    s += dimv(124, 30, 70, 'Va', SL, 'left') + dimv(124, 70, 120, 'Vw', SL, 'left') + dimv(124, 120, 200, 'Vs', SL, 'left') + dimv(90, 30, 120, 'Vv', EM, 'left') + dimv(56, 30, 200, 'V', SL, 'left')
    s += T(244, 54, 'Wa = 0', a='start', z=11) + T(244, 99, 'Ww', a='start', z=11) + T(244, 164, 'Ws', a='start', z=11) + T(185, 20, 'volumes   |   weights', z=11)
    s += lines(300, 50, 'e = Vv / Vs\nn = Vv / V\nS = Vw / Vv\nw = Ww / Ws\nγ = W / V\nγd = Ws / V', z=11, w='600', dy=18)
    return F(210, s, 'The phase diagram: a soil sample drawn as separate layers of air, water and solids, with volumes on the left and weights on the right; void ratio, porosity, saturation and water content are ratios of these parts.')

def geotech_c():
    X = lambda w: 60 + (w - 6) * 21; Y = lambda g: 200 - (g - 90) * 3.2
    s = axes(60, 200, 385, 25, 'water content w (%)', 'dry unit weight γd')
    s += Pa(poly([(X(w), Y(165.4 / (1 + w * 0.0265))) for w, _ in curve(lambda w: 0, 10, 20)]), s=BL, wd=2, dash=True) + T(X(10.3), Y(134) - 6, 'zero air voids (S = 100%)', a='start', c=BL, z=11)
    s += Pa(poly([(X(w), Y(115 - 0.6 * (w - 14) ** 2)) for w, _ in curve(lambda w: 0, 8, 20)]), s=EM, wd=2.5)
    s += Dot(X(14), Y(115)) + Ln(X(14), Y(115), X(14), 200, SL, 1, True) + Ln(60, Y(115), X(14), Y(115), SL, 1, True)
    s += T(X(14), 216, 'OMC', w='600', z=11) + T(64, Y(115) - 6, 'max γd', a='start', w='600', z=11) + T(X(10), Y(100) + 26, 'dry of optimum', z=11) + T(X(18.5), Y(100) + 26, 'wet of optimum', z=11)
    s += T(200, 236, 'Up to the optimum, water helps the grains pack; past it, water takes up space.', z=10)
    return F(244, s, 'A Proctor compaction curve: dry unit weight rises with water content to a maximum at the optimum moisture content, then falls; it always stays below the zero-air-voids line.')

def geotech_d():
    s = R(30, 30, 60, 170, CR, SL, 1.5) + Ln(20, 80, 390, 80, BL, 1.5, True) + T(30, 76, 'water table', a='start', c=BL, z=10)
    s += Pa(poly([(120, 30), (150, 80), (210, 200), (120, 200)], True), LG, JD, 1.5) + T(150, 22, 'total σ', c=JD, w='600', z=11)
    s += Pa(poly([(240, 80), (280, 200), (240, 200)], True), BL, BL, 1.5, op=0.35) + T(250, 22, 'pore u', c=BL, w='600', z=11)
    s += Pa(poly([(310, 30), (340, 80), (360, 200), (310, 200)], True), CR, EM, 1.5) + T(340, 22, 'effective σ\'', c=EM, w='600', z=11)
    s += T(225, 140, '-', w='600', z=20) + T(295, 140, '=', w='600', z=20) + Ln(120, 30, 120, 200, SL, 1) + Ln(240, 30, 240, 200, SL, 1) + Ln(310, 30, 310, 200, SL, 1)
    s += T(200, 222, 'σ\' = σ - u', w='600', z=12) + T(200, 238, 'Strength and settlement depend on effective stress: the part the grains carry.', z=11)
    return F(246, s, 'Stress with depth below a water table: total stress σ, pore water pressure u (zero above the water table), and effective stress σ\' = σ - u, which is what the soil grains carry.')

def geotech_e():
    s = ''
    for x0, mode in ((20, 'active'), (215, 'passive')):
        s += R(x0 + 40, 40, 14, 130, RU, SL, 1.5) + Pa(poly([(x0 + 54, 60), (x0 + 175, 60), (x0 + 175, 170), (x0 + 54, 170)], True), CR, 'none', 0) + Ln(x0 + 54, 60, x0 + 175, 60, SL, 2)
        ang = 60 if mode == 'active' else 30; dx = 110 / math.tan(rad(ang)); dx = min(dx, 118)
        s += Pa(poly([(x0 + 54, 170), (x0 + 54 + dx, 60), (x0 + 54, 60)], True), LG if mode == 'active' else BL, JD, 1.5, op=0.6 if mode == 'passive' else None)
        if mode == 'active': s += A(x0 + 40, 115, x0 + 8, 115, EM, 2.5) + A(x0 + 80, 82, x0 + 70, 110, EM, 2) + T(x0 + 100, 26, 'Wall moves away: active', w='600', z=11) + T(x0 + 100, 190, 'Ka = tan²(45° - φ/2)', c=EM, w='600', z=11) + T(x0 + 100, 205, 'lowest pressure: 0.33 for φ = 30°', z=10)
        else: s += A(x0 + 2, 115, x0 + 38, 115, BL, 2.5) + A(x0 + 110, 110, x0 + 130, 86, BL, 2) + T(x0 + 100, 26, 'Wall pushed in: passive', w='600', z=11) + T(x0 + 100, 190, 'Kp = tan²(45° + φ/2)', c=BL, w='600', z=11) + T(x0 + 100, 205, 'highest: 3.0 for φ = 30°', z=10)
    s += T(200, 226, 'Wall does not move: at rest, K0 ≈ 1 - sin φ = 0.5 for φ = 30°, between the two.', z=11)
    return F(234, s, 'Rankine earth pressure: a wall moving away from the soil lets a wedge slide down (active, lowest pressure); a wall pushed into the soil shoves a wedge up (passive, highest pressure); at rest lies between.')

def geotech_f():
    X = lambda v: 50 + v * 1.8; Y = lambda t: 200 - t * 1.8; c, phi, s3 = 10, 30, 40
    s1 = s3 * math.tan(rad(45 + phi / 2)) ** 2 + 2 * c * math.tan(rad(45 + phi / 2)); C = (s1 + s3) / 2; r = (s1 - s3) / 2
    s = axes(50, 200, 385, 15, 'σ', 'τ') + Ln(X(0), Y(c), X(175), Y(c + 175 * math.tan(rad(phi))), EM, 2.5)
    s += Pa(f"M{X(s3):.1f} 200 A{r * 1.8:.1f} {r * 1.8:.1f} 0 0 1 {X(s1):.1f} 200", s=BL, wd=2.5)
    tp = (C - r * sin(rad(phi)), r * cos(rad(phi))); s += Dot(X(tp[0]), Y(tp[1]), SL, 5) + T(X(tp[0]) - 8, Y(tp[1]) - 8, 'failure', a='end', w='600', z=11)
    s += T(X(s3), 214, 'σ3', w='600', z=11) + T(X(s1), 214, 'σ1', w='600', z=11) + Dot(X(0), Y(c), EM) + T(X(0) + 6, Y(c) + 14, 'c (cohesion)', a='start', c=EM, z=11)
    s += T(236, 46, 'τ = c + σ tan φ', a='end', c=EM, w='600', z=11) + T(236, 60, '(φ: slope of the line)', a='end', c=EM, z=10)
    s += T(X(C), Y(r) + 22, 'Mohr circle', c=BL, z=11) + T(X(C), Y(r) + 36, 'at failure', c=BL, z=11)
    return F(222, s, 'The Mohr-Coulomb failure envelope τ = c + σ tan φ, with the Mohr circle of a sample at failure just touching it. A circle that stays below the line is safe.')

def geotech_g():
    s = Ln(10, 70, 390, 70, SL, 2) + R(170, 54, 60, 16, RU, SL, 1.5) + A(200, 20, 200, 52, EM, 3) + T(208, 30, 'Q', a='start', c=EM, w='600')
    s += Pa('M170 70 L230 70 L200 120 Z', LG, JD, 1.5) + T(200, 90, 'I', w='600', z=11)
    for sgn in (1, -1):
        cx = 200 + sgn * 30
        s += Pa(f"M200 120 Q{200 + sgn * 70} 150 {200 + sgn * 100} 104 L{200 + sgn * 160} 70 L{cx} 70 Z", CR, SL, 1.2)
        s += Ln(cx, 70, 200 + sgn * 100, 104, SL, 1) + Ln(cx, 70, 200 + sgn * 60, 128, SL, 0.8)
        s += T(200 + sgn * 72, 110, 'II', w='600', z=11) + T(200 + sgn * 128, 82, 'III', w='600', z=11)
        s += Pa(f"M{200 + sgn * 112} 70 Q{200 + sgn * 136} 58 {200 + sgn * 160} 70", s=SL, wd=1.5) + A(200 + sgn * 130, 92, 200 + sgn * 140, 76, BL, 1.8, head=7)
    s += T(200, 170, 'I: wedge pushed down. II: soil shears sideways. III: pushed up (heave).', z=11)
    s += T(200, 190, 'qult = c Nc + q Nq + ½ γ B Nγ', w='600', z=11) + T(200, 206, 'c: cohesion; q: soil weight beside the footing per area (γ × depth);', z=10) + T(200, 220, 'B: footing width; Nc, Nq, Nγ: factors read from φ', z=10)
    return F(228, s, 'General shear failure under a footing: a wedge under the footing pushes down, the soil beside it shears outward, and the ground heaves up on both sides. Bearing capacity sums cohesion, surcharge and width terms.')

def geotech_h():
    s = R(10, 50, 380, 110, CR, 'none', 0) + R(10, 160, 380, 50, RU, 'none', 0) + Ln(10, 50, 390, 50, SL, 2) + T(386, 66, 'weak soil', a='end', z=10) + T(386, 176, 'firm layer', a='end', z=10)
    s += R(50, 40, 20, 24, RU, SL, 1.5) + R(30, 64, 60, 14, LG, SL, 1.5) + A(60, 14, 60, 38, EM, 2.5) + ''.join(A(34 + 13 * i, 100, 34 + 13 * i, 80, JD, 1.2, head=5) for i in range(5))
    s += T(60, 120, 'Spread footing', w='600', z=11) + T(60, 134, '(shallow): bears', z=10) + T(60, 146, 'on the soil just below', z=10)
    for cx in (200, 300):
        s += R(cx - 7, 42, 14, 150, LG, SL, 1.5) + A(cx, 12, cx, 40, EM, 2.5)
    s += ''.join(A(193 - 4, 70 + 25 * i, 193 - 4, 54 + 25 * i, JD, 1.3, head=5) + A(207 + 4, 70 + 25 * i, 207 + 4, 54 + 25 * i, JD, 1.3, head=5) for i in range(5))
    s += A(300, 214, 300, 194, JD, 2) + T(200, 228, 'friction pile: side friction', c=JD, w='600', z=10) + T(300, 228, 'end-bearing pile: tip', c=JD, w='600', z=10).replace("x='300'", "x='318'")
    return F(236, s, 'Shallow and deep foundations: a spread footing bears on the soil just below it; piles carry load down through weak soil by friction along their sides and by bearing at the tip on a firm layer.')

def geotech_i():
    s = axes(60, 200, 385, 20, 'effective stress σ\' (log scale)', 'void ratio e') + Pa('M70 50 L180 68 Q205 74 220 94 L360 190', s=EM, wd=2.5)
    s += Ln(205, 74, 205, 200, SL, 1, True) + T(205, 214, 'σ\'p', w='600', z=11) + T(70, 84, 'recompression: Cr', a='start', c=JD, z=11) + T(296, 132, 'virgin compression:', a='start', c=JD, z=11) + T(296, 146, 'slope Cc (large)', a='start', c=JD, z=11)
    s += T(200, 236, 'Stay below σ\'p (overconsolidated): little settlement. Go past it: much more.', z=11)
    s += T(212, 46, 'σ\'p: the most the soil has ever carried', a='start', z=10)
    return F(246, s, 'The e-log σ\' curve of a clay: loading below the preconsolidation pressure σ\'p follows the flat recompression line (Cr); beyond it the soil follows the steep virgin compression line (Cc) and settles much more.')

def geotech_j():
    s = Pa('M10 190 L110 190 L230 90 L390 90 L390 215 L10 215 Z', CR, 'none', 0) + Pa('M10 190 L110 190 L230 90 L390 90', s=SL, wd=2)
    s += Pa('M110 190 A159.6 159.6 0 0 0 300 90 L230 90 Z', LG, 'none', 0, op=0.8) + Pa('M110 190 A159.6 159.6 0 0 0 300 90', s=JD, wd=2.5, dash=True)
    s += Dot(150, 35.5, SL) + T(142, 32, 'O', a='end', w='600') + Ln(150, 35.5, 150, 195, SL, 1, True) + T(156, 115, 'R', a='start', z=11)
    s += A(215, 120, 215, 165, EM, 2.5) + T(222, 158, 'W', a='start', c=EM, w='600') + dimh(150, 215, 55, 'arm', SL, False)
    s += A(186, 192, 238, 180, BL, 2) + T(250, 192, 'strength along the arc resists', a='start', c=BL, w='600', z=11)
    s += T(200, 236, 'FS = resisting moment / driving moment', w='600', z=11) + T(200, 250, 'Driving: W × arm. Resisting: strength × arc length × R.', z=10)
    return F(258, s, 'A circular slip surface through a slope: the weight W of the sliding mass tends to rotate it about O; the soil strength along the arc resists. The factor of safety is resisting over driving moment.')

def geotech_k():
    s = ''; titles = ('Separation', 'Filtration', 'Drainage', 'Reinforcement')
    for i, t in enumerate(titles):
        x = 10 + i * 97; s += R(x, 30, 88, 110, CR, SL, 1) + T(x + 44, 22, t, w='600', z=11)
        if i == 0: s += ''.join(Cc(x + 12 + 16 * (k % 5), 46 + 14 * (k // 5), 6, RU, SL, 1) for k in range(10)) + Ln(x, 80, x + 88, 80, EM, 3) + R(x + 1, 82, 86, 57, LG, 'none', 0)
        if i == 1: s += Ln(x, 80, x + 88, 80, EM, 3) + ''.join(A(x + 18 + 20 * k, 50, x + 18 + 20 * k, 112, BL, 1.5, head=6) for k in range(4)) + ''.join(Dot(x + 12 + 18 * k, 72, SL, 2.5) for k in range(5))
        if i == 2: s += R(x, 80, 88, 8, EM, 'none', 0) + A(x + 8, 84, x + 82, 84, BL, 2, head=7) + ''.join(A(x + 20 + 20 * k, 54, x + 20 + 20 * k, 78, BL, 1.2, head=5) for k in range(3))
        if i == 3: s += ''.join(Ln(x + 10, y, x + 80, y, EM, 3) for y in (55, 85, 115)) + ''.join(A(x + 50, y - 6, x + 80, y - 6, JD, 1.2, head=5) for y in (55, 85, 115))
    s += lines(10, 162, 'Keep layers apart; pass water but hold the soil back; carry water\nalong the fabric; take tension so walls and slopes stand steeper.\nLime or cement mixed into the soil lowers plasticity and adds strength.', z=10, dy=13)
    return F(204, s, 'The four functions of geosynthetics: separation, filtration, drainage and reinforcement, with chemical stabilization by lime or cement as the alternative.')


# ---------------- Materials ----------------
def materials_a():
    X = lambda r: 50 + (r - 0.3) * 300; Y = lambda f: 190 - f * 3.2
    s = axes(50, 190, 215, 20, '', 'strength') + Pa(poly([(X(r), Y(96 * 0.13 ** (r - 0.3) * 0.55)) for r, _ in curve(lambda r: 0, 0.3, 0.8)]), s=EM, wd=2.5)
    s += T(132, 210, 'water-cement ratio (0.3 to 0.8)', z=10) + T(120, 48, 'more water,', a='start', c=EM, z=11) + T(120, 62, 'weaker concrete', a='start', c=EM, z=11)
    parts = (('Coarse aggregate', 41, CR), ('Fine aggregate', 26, RU), ('Air', 6, WH), ('Water', 16, BL), ('Cement', 11, SL)); y = 20
    for name, pct, col in parts:
        h = pct * 1.7; s += R(236, y, 36, h, col, SL, 1, 0.5 if col == BL else None) + T(280, y + h / 2 + 4, f"{name} {pct}%", a='start', z=10); y += h
    s += T(254, 206, 'typical, by volume', z=10)
    return F(216, s, 'Concrete mix design: strength falls as the water-cement ratio rises (left); a typical mix by volume is mostly aggregate, with cement, water and some entrained air (right).')
def materials_b():
    s = Pa('M30 180 L48 70 L84 70 L102 180 Z', 'none', SL, 2, dash=True) + T(66, 60, 'cone mould', z=10)
    s += Pa('M115 180 Q115 116 140 100 Q165 90 190 100 Q215 116 215 180 Z', LG, JD, 2) + Ln(20, 180, 230, 180, SL, 2)
    s += Ln(84, 70, 196, 70, SL, 1, True) + dimv(202, 70, 94, 'slump', EM)
    s += T(124, 204, 'Slump test: workability of fresh concrete', w='600', z=11) + T(124, 218, 'cone 300 mm (12 in) tall; slump = drop of the top', z=10)
    s += R(258, 70, 40, 100, CR, SL, 1.5) + R(246, 56, 64, 12, RU, SL, 1.5) + R(246, 172, 64, 12, RU, SL, 1.5) + A(278, 22, 278, 54, EM, 2.5) + A(278, 216, 278, 186, EM, 2.5)
    s += lines(318, 100, "Cylinder\nbreak:\nf'c = P / A\nat 28 days", z=11)
    return F(226, s, 'Two standard concrete tests: the slump test measures how far fresh concrete sags when the cone is lifted; the cylinder test crushes a hardened cylinder to give the compressive strength f\'c.')
def materials_c():
    s = axes(30, 190, 205, 20, 'ε', 'stress σ') + Pa('M30 190 L60 80 L100 80 Q140 40 165 50 Q180 58 190 78', s=EM, wd=2.5) + Dot(190, 78, OR, 4)
    s += T(64, 72, 'Fy (yield)', a='start', z=10) + T(150, 36, 'Fu (ultimate)', z=10) + T(196, 74, 'break', a='start', c=OR, z=10) + T(52, 140, 'slope = E', a='start', c=EM, w='600', z=10)
    s += T(118, 226, 'Steel: yields, stretches far: ductile', w='600', z=10)
    s += axes(230, 190, 395, 20, 'ε', 'stress σ') + Pa('M230 190 Q275 70 305 66 Q330 66 350 95', s=BL, wd=2.5) + Dot(350, 95, OR, 4)
    s += Ln(305, 66, 305, 190, SL, 1, True) + T(305, 58, "f'c", w='600', z=11) + T(305, 204, '0.002', z=10) + Ln(350, 95, 350, 190, SL, 1, True) + T(352, 204, '0.003', a='start', z=10) + T(354, 92, 'crushes', a='start', c=OR, z=10)
    s += T(312, 226, 'Concrete in compression: brittle', w='600', z=10)
    return F(236, s, 'Stress-strain curves: steel is linear to yield, then stretches a long way before breaking (ductile); concrete in compression peaks at f\'c near a strain of 0.002 and crushes at about 0.003 (brittle).')


# ---------------- Surveying ----------------
def surveying_a():
    cx, cy, r = 200, 118, 82; s = A(cx, cy + r + 10, cx, cy - r - 14, SL, 1.2, head=8) + Ln(cx - r - 14, cy, cx + r + 14, cy, SL, 1.2)
    s += T(cx, cy - r - 18, 'N', w='600') + T(cx, cy + r + 24, 'S', w='600') + T(cx + r + 20, cy + 4, 'E', a='start', w='600') + T(cx - r - 20, cy + 4, 'W', a='end', w='600')
    for az, lab, col in ((60, 'Az 60° = N 60° E', EM), (150, 'Az 150° = S 30° E', BL), (210, 'Az 210° = S 30° W', JD), (300, 'Az 300° = N 60° W', SL)):
        x, y = cx + r * sin(rad(az)), cy - r * cos(rad(az)); s += A(cx, cy, x, y, col, 2.5)
        s += T(x + (6 if x > cx else -6), y + (-6 if y < cy else 16), lab, a='start' if x > cx else 'end', c=col, w='600', z=11)
    s += arc(cx, cy, 30, 90, 30, EM, 1.5, True) + arc(cx, cy, 24, 270, 300, BL, 1.5)
    s += lines(10, 236, 'Azimuth: clockwise from north, 0° to 360°.\nBearing: from north or south toward east or west, 0° to 90°.', z=11)
    return F(258, s, 'Azimuths and bearings: an azimuth is measured clockwise from north through 360°; a bearing is measured from north or south toward east or west, never more than 90°.')

def surveying_b():
    s = Ln(30, 180, 370, 180, SL, 2) + T(370, 196, 'baseline', a='end', z=10); hs = (60, 95, 80, 115, 70); xs = [50 + 75 * i for i in range(5)]
    for i in range(4):
        s += Pa(poly([(xs[i], 180), (xs[i], 180 - hs[i]), (xs[i + 1], 180 - hs[i + 1]), (xs[i + 1], 180)], True), LG if i % 2 == 0 else CR, 'none', 0)
    s += Pa('M50 120 Q70 70 125 85 Q160 98 200 100 Q240 98 275 65 Q310 40 350 110', s=SL, wd=2) + T(200, 80, 'boundary', z=10)
    for i, (x, h) in enumerate(zip(xs, hs)): s += Ln(x, 180, x, 180 - h, BL, 2) + T(x + 4, 178 - h / 2, f'h{i + 1}', a='start', c=BL, w='600', z=11)
    s += dimh(xs[0], xs[1], 194, 'd', SL)
    s += T(200, 22, 'Trapezoidal rule: Area ≈ d (h1/2 + h2 + h3 + h4 + h5/2)', w='600', z=11) + T(200, 38, 'each strip is a trapezoid; equal spacing d', z=10)
    return F(214, s, 'Area of an irregular boundary by offsets: perpendicular offsets h at equal spacing d from a baseline split the area into trapezoids, which are summed.')

def surveying_c():
    f1 = [(40, 190), (170, 190), (145, 135), (65, 135)]; dx, dy = 160, -60; f2 = [(40 + dx - 10, 190 + dy), (170 + dx + 20, 190 + dy), (145 + dx + 10, 120 + dy), (65 + dx - 5, 120 + dy)]
    s = ''.join(Ln(a[0], a[1], b[0], b[1], RU, 1.2, True) for a, b in zip(f1, f2)) + Pa(poly(f2, True), LG, JD, 2) + Pa(poly(f1, True), LG, JD, 2)
    s += T(105, 172, 'A1', c=JD, w='600') + T(285, 102, 'A2', c=JD, w='600') + Ln(170, 190, 360, 130, SL, 1) + T(290, 186, 'L: distance between stations', a='start', z=10).replace("x='290'", "x='250'")
    s += T(30, 30, 'Average end area:', a='start', w='600', z=11) + T(30, 46, 'V = L (A1 + A2) / 2', a='start', c=EM, w='600', z=12) + T(30, 62, 'cubic feet ÷ 27 = cubic yards', a='start', z=10)
    s += T(30, 80, 'Slightly high; the prismoidal', a='start', z=10) + T(30, 92, 'formula is more exact.', a='start', z=10)
    return F(206, s, 'The average end area method: the earthwork volume between two stations is the distance between them times the average of the two cross-section areas.')

def surveying_d():
    pts = [(80, 170), (300, 180), (350, 70), (150, 40)]; end = (90, 158)
    s = ''.join(A(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], EM, 2.5) for i in range(3)) + A(pts[3][0], pts[3][1], end[0], end[1], EM, 2.5)
    s += ''.join(Dot(x, y, SL, 4) for x, y in pts) + T(72, 184, 'A (start)', a='end', w='600', z=11) + T(292, 196, 'B', a='end', w='600') + T(360, 66, 'C', a='start', w='600') + T(146, 32, 'D', w='600')
    s += Ln(300, 180, 350, 180, BL, 1.5, True) + Ln(350, 180, 350, 70, BL, 1.5, True) + T(326, 196, 'departure', c=BL, z=10) + T(356, 128, 'latitude', a='start', c=BL, z=10)
    s += A(end[0], end[1], 80, 170, OR, 2, head=7) + T(98, 150, 'misclosure', a='start', c=OR, w='600', z=11)
    s += lines(10, 222, 'Latitude = L cos(azimuth)\nDeparture = L sin(azimuth)\nClosed loop: ΣLat = ΣDep = 0', z=10, dy=13) + lines(210, 222, 'Misclosure = √(ΣLat² + ΣDep²)\nPrecision = misclosure / perimeter', z=10, dy=13)
    return F(256, s, 'A closed traverse whose measured legs do not quite return to the start: each leg splits into a latitude and a departure, and the leftover sums give the linear misclosure.')
def surveying_e():
    s = Pa('M10 190 L120 180 L240 140 L390 110', s=SL, wd=2)
    s += R(30, 120, 6, 66, WH, SL, 1) + T(33, 112, 'BM', w='600', z=11) + R(180, 90, 6, 72, WH, SL, 1) + T(183, 82, 'TP', w='600', z=11) + R(340, 54, 6, 64, WH, SL, 1) + T(343, 46, 'B', w='600', z=11)
    for x, y, a_, b_ in ((105, 120, 33, 183), (265, 84, 183, 343)):
        s += Ln(x - 10, y + 60, x, y, SL, 1.5) + Ln(x + 10, y + 60, x, y, SL, 1.5) + R(x - 10, y - 10, 20, 10, SL, SL, 1)
        s += Ln(a_ + 3, y - 5, x - 10, y - 5, BL, 1.5, True) + Ln(x + 10, y - 5, b_ - 3, y - 5, EM, 1.5, True)
        s += T((a_ + x) / 2, y - 10, 'BS', c=BL, w='600', z=11) + T((x + b_) / 2, y - 10, 'FS', c=EM, w='600', z=11)
    s += lines(10, 30, 'Height of instrument HI = elevation + backsight (BS)\nNew elevation = HI - foresight (FS)\nElev B = Elev BM + ΣBS - ΣFS', z=11)
    return F(206, s, 'Differential leveling through a turning point: each setup adds the backsight to get the height of instrument and subtracts the foresight; overall, elevation of B = BM + sum of backsights - sum of foresights.')


# ---------------- Transportation ----------------
def transport_a():
    s = Ln(60, 150, 200, 60, SL, 1.5, True) + Ln(200, 60, 340, 130, SL, 1.5, True) + Pa('M60 150 Q200 60 340 130', s=EM, wd=3)
    for x, y, lab in ((60, 150, 'PVC'), (200, 60, 'PVI'), (340, 130, 'PVT')): s += Dot(x, y, SL) + T(x, y + (18 if lab != 'PVI' else -10), lab, w='600', z=11)
    s += Ln(200, 60, 200, 100, BL, 1.5) + T(194, 86, 'E', a='end', c=BL, w='600', z=11) + Dot(217.5, 99.4, BL) + T(222, 126, 'high point', a='start', c=BL, z=10)
    s += T(110, 98, 'G1 (+)', a='end', z=11) + T(292, 92, 'G2 (-)', a='start', z=11) + dimh(60, 340, 172, 'L (horizontal length)')
    s += Ln(80, 128, 330, 112, SL, 1, True).replace("stroke-dasharray='6 4'", "stroke-dasharray='2 4'")
    s += lines(10, 204, 'A = |G2 - G1| in percent; K = L / A; middle ordinate E = A L / 800.\nDotted: the driver\'s sight line. A longer curve (bigger K) lets the driver\nsee farther: L is chosen so sight distance covers stopping sight distance.', z=10, dy=13)
    return F(246, s, 'A crest vertical curve: a parabola joins grade G1 to grade G2 between PVC and PVT; its length controls how far a driver can see over the crest.')

def transport_b():
    s = ''
    for x0, kind in ((15, 'flexible'), (210, 'rigid')):
        layers = (('Asphalt surface', 14, SL), ('Base', 26, CR), ('Subbase', 26, RU), ('Subgrade (soil)', 60, LG)) if kind == 'flexible' else (('Concrete slab', 32, RU), ('Base', 22, CR), ('Subgrade (soil)', 72, LG))
        y = 50
        for name, h, col in layers:
            s += R(x0, y, 175, h, col, SL, 1) + T(x0 + 170, y + h / 2 + 4, name, a='end', c=WH if col == SL else SL, z=10); y += h
        s += Cc(x0 + 60, 36, 13, SL, SL) + A(x0 + 60, 50, x0 + 60, 56, EM, 2, head=6)
        sp = 40 if kind == 'flexible' else 58
        s += Ln(x0 + 56, 56, x0 + 60 - sp, 176, EM, 1.5, True) + Ln(x0 + 64, 56, x0 + 60 + sp, 176, EM, 1.5, True)
        s += T(x0 + 88, 20, 'Flexible pavement' if kind == 'flexible' else 'Rigid pavement', w='600', z=11)
    s += lines(15, 196, 'Flexible: layers of better material spread the wheel load down\nuntil the subgrade can carry it. Rigid: the stiff slab bends as a\nplate and spreads the load over a wide area.', z=10, dy=13)
    return F(236, s, 'Flexible and rigid pavement sections: in a flexible pavement successive layers spread the wheel load down to the subgrade; a rigid slab spreads it over a much wider area by bending.')

def transport_c():
    X = lambda k: 55 + k * 3.1; Y = lambda q: 200 - q * 0.075
    s = axes(55, 200, 385, 20, 'k', 'flow q') + Pa(poly([(X(k), Y(60 * k * (1 - k / 100))) for k, _ in curve(lambda k: 0, 0, 100)]), s=EM, wd=2.5)
    s += Dot(X(50), Y(1500), SL, 5) + Ln(X(50), Y(1500), X(50), 200, SL, 1, True) + T(X(50), 214, 'kj / 2', z=10) + T(X(50) + 8, Y(1500) - 10, 'capacity qmax = vf kj / 4', a='start', w='600', z=11)
    s += T(X(25), Y(500), 'uncongested', c=JD, w='600', z=11) + T(X(78), Y(500), 'congested', c=OR, w='600', z=11) + T(X(100), 214, 'kj', z=10)
    s += Ln(X(0), Y(0), X(25), Y(1500), BL, 1.5, True) + T(X(24), Y(1500) - 8, 'slope = vf', a='end', c=BL, z=10)
    s += T(385, 30, 'q = k v', a='end', w='600', z=12)
    s += lines(10, 234, 'k: density (veh/mi/lane); kj: jam density; vf: free-flow speed.\nSpeed at any point = q / k, the slope of a line from the origin.', z=10, dy=13)
    return F(256, s, 'The flow-density curve (Greenshields): flow rises with density to capacity at half the jam density, then falls as traffic becomes congested; the slope of a line from the origin is the speed.')
def transport_d():
    X = lambda t: 70 + t * 3.2; s = ''
    rows = ((60, 'Phase 1', ((0, 40, JD, 'Green'), (40, 44, LG, 'Y'), (44, 46, RU, 'AR'), (46, 100, SL, 'Red'))), (110, 'Phase 2', ((0, 46, SL, 'Red'), (46, 86, JD, 'Green'), (86, 90, LG, 'Y'), (90, 92, RU, 'AR'), (92, 100, SL, 'Red'))))
    for y, name, segs in rows:
        s += T(64, y + 15, name, a='end', w='600', z=11)
        for a, b, col, lab in segs:
            s += R(X(a), y, X(b) - X(a), 22, col, SL, 0.8) + (T((X(a) + X(b)) / 2, y + 15, lab, c=WH if col in (JD, SL) else SL, z=10, w='600') if b - a >= 4 else '')
    s += dimh(X(0), X(100), 150, 'cycle length C (here 100 s)') + T(X(42), 50, 'change interval', z=9)
    s += lines(10, 186, 'Effective green g = green + yellow + all-red - lost time.\nLane group capacity = s × g / C (s: saturation flow, veh/h of green).\nLonger cycles lose less time per hour but make drivers wait longer.', z=10, dy=13)
    return F(228, s, 'A two-phase signal cycle on a timeline: each phase gets green, yellow and all-red, then red while the other phase runs; capacity depends on the share of the cycle that is effective green.')

def transport_e():
    steps = (('1. Trip generation', 'How many trips start\nand end in each zone?'), ('2. Trip distribution', 'Which zone do they\ngo to?'), ('3. Mode choice', 'Car, transit, walk\nor bike?'), ('4. Route assignment', 'Which roads or\nlines do they use?'))
    s = ''
    for i, (t, q) in enumerate(steps):
        x = 10 + i * 98; s += box(x, 30, 86, 40, t.replace(' ', '\n', 1), LG, SL, SL, 10)
        s += lines(x + 43, 92, q, a='middle', z=10, dy=13)
        if i < 3: s += A(x + 86, 50, x + 98, 50, SL, 1.5, head=6)
    s += T(200, 150, 'The four-step travel demand model: each step feeds the next.', w='600', z=11)
    s += T(200, 166, 'Outputs: volumes on each link, used to size roads, transit and signals.', z=10)
    return F(176, s, 'The four-step travel demand model: trip generation, trip distribution, mode choice and route assignment, each answering one question and feeding the next.')


# ---------------- Construction ----------------
def construction_a():
    s = ''
    panels = ((10, 'Design-bid-build', [('Designer', 0), ('Contractor', 1)], True), (140, 'Design-build', [('Design-builder\n(designer + builder)', None)], False), (270, 'CM at risk', [('Designer', 0), ('Construction\nmanager', 1)], True))
    for x, title, kids, two in panels:
        s += T(x + 60, 20, title, w='600', z=11) + box(x + 25, 34, 70, 26, 'Owner', LG, SL, SL, 11)
        if two:
            for lab, k in kids: s += box(x + k * 64, 110, 60, 34, lab, CR, SL, SL, 9) + Ln(x + 60, 60, x + 30 + k * 64, 110, EM, 2)
            s += Ln(x + 60, 127, x + 64, 127, SL, 1, True)
        else:
            s += box(x + 10, 110, 100, 34, kids[0][0], CR, SL, SL, 9) + Ln(x + 60, 60, x + 60, 110, EM, 2)
    s += T(76, 166, 'Two contracts; low bid wins.', z=9) + T(76, 178, 'Design finished before bidding.', z=9) + T(200, 166, 'One contract, one point of', z=9) + T(200, 178, 'responsibility; can overlap.', z=9)
    s += T(330, 166, 'CM joins during design and', z=9) + T(330, 178, 'guarantees a maximum price.', z=9)
    s += Ln(80, 200, 110, 200, EM, 2) + T(116, 204, 'contract', a='start', z=10) + Ln(190, 200, 220, 200, SL, 1, True) + T(226, 204, 'coordinate, no contract', a='start', z=10)
    return F(212, s, 'Three project delivery methods as contract diagrams: design-bid-build has separate owner contracts with designer and contractor; design-build has one; with a construction manager at risk the CM joins during design.')

def construction_b():
    s = ''; blocks = (('Bank', 1.00, 'in the ground', CR), ('Loose', 1.25, 'dug, in the truck', LG), ('Compacted', 0.90, 'rolled in the fill', RU)); x = 20
    for name, v, note, col in blocks:
        w = 80 * v; s += R(x, 140 - 80, w, 80, col, SL, 1.5) + T(x + w / 2, 104, f"{v:.2f}", w='600', z=13) + T(x + w / 2, 44, name, w='600', z=11) + T(x + w / 2, 158, note, z=10)
        if name != 'Compacted': s += A(x + w + 6, 100, x + w + 40, 100, SL, 1.5, head=7)
        x += w + 48
    s += T(200, 186, 'Swell = loose / bank - 1 = 25%.  Shrinkage = 1 - compacted / bank = 10%.', w='600', z=11)
    s += T(200, 202, 'Haul is priced in loose volume; fill is specified in compacted volume.', z=10)
    return F(210, s, 'The same soil in three states: one bank cubic yard swells to about 1.25 loose cubic yards when dug and shrinks to about 0.90 when compacted (typical values for illustration).')

def construction_c():
    X = lambda t: 50 + t * 3.3; Y = lambda v: 200 - v * 1.6; S = lambda t: 100 / (1 + exp(-(t - 50) / 14))
    s = axes(50, 200, 385, 20, 'time', 'cost') + Pa(poly([(X(t), Y(S(t))) for t, _ in curve(lambda t: 0, 0, 100)]), s=SL, wd=2.5)
    s += Pa(poly([(X(t), Y(S(t) * 0.82)) for t, _ in curve(lambda t: 0, 0, 55)]), s=EM, wd=2.5) + Pa(poly([(X(t), Y(S(t) * 0.98)) for t, _ in curve(lambda t: 0, 0, 55)]), s=OR, wd=2.5)
    s += Ln(X(55), 200, X(55), 40, SL, 1, True) + T(X(55), 34, 'status date', z=10)
    pv, ev, ac = S(55), S(55) * 0.82, S(55) * 0.98
    s += T(X(80), Y(S(80)) - 8, 'PV (planned)', a='end', w='600', z=11) + T(X(56) + 4, Y(ev) + 4, 'EV (earned)', a='start', c=EM, w='600', z=11) + T(X(52), Y(ac) - 8, 'AC (actual)', a='end', c=OR, w='600', z=11)
    s += lines(246, 150, 'SV = EV - PV (- : behind)\nCV = EV - AC (- : over budget)\nSPI = EV / PV, CPI = EV / AC', z=10)
    return F(222, s, 'Earned value S-curves at a status date: earned value below planned value means the work is behind schedule, and actual cost above earned value means it is over budget.')

def construction_d():
    parts = (('Materials', 70, CR), ('Labor', 60, LG), ('Equipment', 34, RU), ('Overhead', 30, CR), ('Profit', 22, LG), ('Contingency', 24, RU)); x = 20; s = ''
    for i, (n, w, c) in enumerate(parts):
        w = w * 1.4; s += R(x, 60, w, 40, c, SL, 1) + T(x + w / 2, 52 if i % 2 == 0 else 116, n, z=10, w='600'); x += w
    s += dimh(20, 20 + 164 * 1.4, 134, 'direct cost = quantity × unit cost') + dimh(20, x, 168, 'bid price')
    s += lines(20, 198, 'Unit cost = (labor hours × wage + equipment hours × rate\n+ materials) / quantity', z=10, dy=13)
    return F(220, s, 'An estimate built up from direct costs (materials, labor, equipment, each a quantity times a unit cost) plus overhead, profit and contingency to reach the bid price.')
def construction_e():
    s = R(30, 30, 340, 70, RU, 'none', 0) + R(30, 30, 340, 14, CR, SL, 1) + R(30, 86, 340, 14, CR, SL, 1) + Ln(30, 65, 370, 65, WH, 2, True).replace(WH, '#FFFFFF')
    s += Ln(200, 18, 200, 112, BL, 2, True) + A(200, 18, 222, 18, BL, 2, head=7) + A(200, 112, 222, 112, BL, 2, head=7) + T(196, 16, 'A', a='end', c=BL, w='600') + T(196, 122, 'A', a='end', c=BL, w='600')
    s += T(372, 26, 'Plan (from above)', a='end', w='600', z=11)
    y = 170; s += R(60, y, 40, 8, CR, SL, 1) + R(100, y + 4, 200, 8, RU, SL, 1) + R(300, y, 40, 8, CR, SL, 1) + Ln(100, y, 100, y + 12, SL, 2) + Ln(300, y, 300, y + 12, SL, 2)
    s += T(80, y - 6, 'sidewalk', z=9) + T(200, y - 2, 'roadway', z=9) + T(320, y - 6, 'sidewalk', z=9) + T(200, y + 32, 'Section A-A: the cut seen in the direction of the arrows', w='600', z=11)
    s += R(30, 214, 40, 6, SL, SL, 1) + R(70, 214, 40, 6, WH, SL, 1) + T(30, 234, '0', z=9) + T(110, 234, '20 ft', z=9) + T(118, 220, 'scale bar: measure, do not guess', a='start', z=9)
    return F(240, s, 'Reading drawings: a section cut line A-A on the plan, with arrows giving the direction of view, and the matching cross-section drawn below it; a scale bar converts drawing distance to real distance.')


# ---------------- Engineering economics ----------------
def econ_a():
    X = lambda k: 50 + k * 60; s = Ln(40, 120, 370, 120, SL, 2) + ''.join(Ln(X(k), 114, X(k), 126, SL, 1.5) + T(X(k), 140, str(k) if k < 5 else 'n', z=11) for k in range(6))
    s += A(X(0), 120, X(0), 50, EM, 3) + T(X(0) + 6, 54, 'P', a='start', c=EM, w='600') + A(X(5), 120, X(5), 40, BL, 3) + T(X(5) + 6, 44, 'F', a='start', c=BL, w='600')
    s += ''.join(A(X(k), 120, X(k), 90, JD, 2) for k in range(1, 6)) + T(X(3), 82, 'A each year (end of year)', c=JD, w='600', z=11)
    s += Pa(f"M{X(0)} 46 Q{X(2.5)} 4 {X(5) - 8} 36", s=SL, wd=1.2) + T(X(2.5), 18, 'F = P (1 + i)ⁿ, factor (F/P, i, n)', z=11)
    s += lines(10, 166, 'P now, F later and the series A are equivalent at interest rate i.\nFactors read (want / have, i, n): P from A is (P/A, i, n); A from F is (A/F, i, n).', z=10, dy=13)
    return F(196, s, 'A cash flow timeline: a present amount P, a future amount F and a uniform annual series A are equivalent at interest rate i, and each factor converts one into another.')

def econ_b():
    X = lambda q: 50 + q * 2.75; Y = lambda v: 200 - v * 1.3
    s = axes(50, 200, 385, 20, 'quantity Q', '$') + Ln(X(0), Y(40), X(120), Y(40), SL, 1.5, True) + T(X(120), Y(40) + 14, 'fixed cost', a='end', z=10)
    s += Ln(X(0), Y(40), X(120), Y(112), OR, 2.5) + T(X(120), Y(112) + 22, 'total cost', a='end', c=OR, w='600', z=11) + Ln(X(0), Y(0), X(120), Y(132), EM, 2.5) + T(X(116), Y(128) - 10, 'revenue', a='end', c=EM, w='600', z=11)
    qb = 80; s += Dot(X(qb), Y(88), SL, 5) + Ln(X(qb), Y(88), X(qb), 200, SL, 1, True) + T(X(qb) - 8, Y(88) - 10, 'break-even', a='end', w='600', z=11)
    s += T(X(30), Y(45), 'loss', c=OR, w='600', z=11) + T(296, 34, 'profit', a='end', c=EM, w='600', z=11) + Ln(300, 36, 352, 50, EM, 1)
    s += T(200, 236, 'Break-even Q = fixed cost / (price - variable cost per unit)', z=11)
    return F(244, s, 'Break-even analysis: total cost starts at the fixed cost and rises with quantity; revenue rises faster; they cross at the break-even quantity, with loss below it and profit above.')
def econ_c():
    X = lambda i: 55 + i * 13; Y = lambda v: 120 - v * 0.55; pw = lambda i: 100 * (1 - i / 12) * (1.6 / (1 + i / 10))
    s = axes(55, 200, 385, 20, 'interest rate i (%)', 'present worth PW') + Ln(55, 120, 380, 120, SL, 1.5)
    s += Pa(poly([(X(i), Y(pw(i))) for i, _ in curve(lambda i: 0, 0, 24)]), s=EM, wd=2.5) + Dot(X(12), 120, SL, 5) + T(X(12) + 4, 112, 'IRR: PW = 0', a='start', w='600', z=11)
    s += Ln(X(8), 200, X(8), Y(pw(8)), BL, 1.5, True) + Dot(X(8), Y(pw(8)), BL) + T(X(8), 214, 'MARR', c=BL, w='600', z=11) + T(X(8) + 6, Y(pw(8)) - 6, 'PW > 0 at MARR: accept', a='start', c=BL, z=10)
    s += T(200, 236, 'Same decision two ways: PW at the MARR above zero, or IRR above the MARR.', z=10) + T(200, 250, 'Compare alternatives over the same study period.', z=10)
    return F(258, s, 'Present worth plotted against interest rate: it falls as the rate rises and crosses zero at the internal rate of return; a project with positive PW at the MARR has an IRR above the MARR.')

def econ_d():
    s = R(20, 90, 26, 26, LG, SL, 1.5) + T(33, 132, 'decide', z=10)
    s += Ln(46, 103, 140, 50, SL, 2) + Ln(46, 103, 140, 160, SL, 2) + Cc(150, 50, 12, CR) + T(150, 34, 'Option A', w='600', z=11) + T(150, 186, 'Option B: a certain $60,000', w='600', z=11).replace("x='150'", "x='170'")
    s += Ln(162, 50, 260, 25, SL, 1.5) + Ln(162, 50, 260, 80, SL, 1.5) + T(210, 26, 'p = 0.6', z=10) + T(210, 82, 'p = 0.4', z=10) + T(266, 29, '$100,000', a='start', z=11) + T(266, 84, '$20,000', a='start', z=11)
    s += Ln(140, 160, 260, 160, SL, 1.5) + T(266, 164, '$60,000', a='start', z=11)
    s += T(390, 130, 'EV(A) = 0.6 × 100,000 + 0.4 × 20,000', a='end', c=EM, w='600', z=10) + T(390, 144, '= $68,000, more than B on average', a='end', c=EM, z=10)
    s += T(390, 116, 'Expected value: Σ (probability × outcome)', a='end', z=10)
    return F(198, s, 'A decision tree: option A has a 60% chance of $100,000 and 40% of $20,000, an expected value of $68,000; option B is a certain $60,000. By expected value A is better, though it carries risk.')


# ---------------- Ethics and professional practice ----------------
def ethics_a():
    rows = (('1. The public: health, safety and welfare first', EM, WH), ('2. Employers and clients: faithful agent', LG, SL), ('3. Other licensees: fair dealing, credit', CR, SL))
    s = ''.join(box(20 + i * 10, 24 + i * 46, 310 - i * 20, 36, t, f, SL, c, 11) for i, (t, f, c) in enumerate(rows))
    s += A(352, 150, 352, 30, SL, 2) + lines(362, 76, 'higher\nduty\nwins', z=10)
    s += lines(20, 176, 'When duties conflict, the higher one wins: report a danger\nto the public even if the client objects.', z=11)
    return F(206, s, 'The order of an engineer\'s obligations in the NCEES Model Rules: to the public first, then to employers and clients, then to other licensees.')
def ethics_b():
    steps = ('Duty', 'Breach', 'Causation', 'Damages'); notes = ('the engineer owed\na duty of care', 'work fell below the\nstandard of care', 'the breach caused\nthe harm', 'real loss or\ninjury occurred'); s = ''
    for i, (t, n) in enumerate(zip(steps, notes)):
        x = 10 + i * 98; s += box(x, 20, 84, 30, t, LG, SL, SL, 11) + lines(x + 42, 70, n, a='middle', z=10, dy=13)
        if i < 3: s += A(x + 84, 35, x + 98, 35, SL, 1.5, head=6)
    s += T(200, 118, 'All four must be proved for negligence. A bad outcome alone is not negligence.', w='600', z=11)
    return F(128, s, 'The four elements of negligence: duty, breach of the standard of care, causation and damages; all four must be proved.')

def ethics_c():
    steps = ('Engineering\ndegree', 'Pass the\nFE exam', 'Engineer intern\n(EI or EIT)', 'Supervised\nexperience,\nusually 4 yr', 'Pass the\nPE exam', 'Licensed\nPE', 'Other states:\ncomity')
    s, pos = _train(list(steps), 4)
    s = s.replace(f"fill='{LG}'", f"fill='{CR}'", 1)
    s += T(200, 16, 'The usual path to licensure (each state board sets its own rules)', w='600', z=11)
    s += T(200, 156, 'Only a licensed PE may seal work or offer engineering to the public.', z=10)
    return F(166, s, 'The usual path to a professional engineering licence: degree, FE exam, engineer intern, supervised experience, PE exam, licence, and licensure in other states by comity.')

def ethics_d():
    els = ('Offer', 'Acceptance', 'Consideration', 'Competent\nparties', 'Lawful\npurpose'); s = T(200, 16, 'A valid contract needs all five', w='600', z=11)
    s += ''.join(box(10 + i * 77, 26, 70, 34, t, LG, SL, SL, 10) for i, t in enumerate(els))
    s += R(30, 104, 340, 18, CR, SL, 1) + A(200, 113, 30, 113, BL, 2.5) + A(200, 113, 370, 113, EM, 2.5)
    s += T(30, 96, 'owner carries the cost risk', a='start', c=BL, w='600', z=10) + T(370, 96, 'contractor carries it', a='end', c=EM, w='600', z=10)
    for x, t in ((40, 'Cost-plus'), (200, 'Unit price'), (360, 'Lump sum')): s += T(x, 140, t, w='600', z=11)
    s += T(200, 156, 'paid actual cost + fee    |    paid per unit, owner takes quantity risk    |    one fixed price', z=9)
    return F(166, s, 'A valid contract needs offer, acceptance, consideration, competent parties and a lawful purpose. Contract types range from cost-plus, where the owner carries the cost risk, to lump sum, where the contractor does.')


# ---------------- Topic overview: how the parts connect ----------------
def topic_map(name, subs, needs, short, tname):
    """subs: [(id, code, short name)] in suggested order; needs: {sub: [prereq subs]}. Left: what to refresh first; right: where it comes back."""
    ids = [s for s, _, _ in subs]; left = []; right = []
    for s, _, _ in subs:
        for p in needs.get(s, []):
            if p not in ids and p not in left: left.append(p)
    for t, ps in needs.items():
        if t.split('-')[0] != ids[0].split('-')[0] and any(p in ids for p in ps) and t not in right: right.append(t)
    n = len(subs); bh, gap, top = 22, 6, 40; W = 540; L0, M0, MW, R0 = 186, 198, 140, 356
    span = max(n * (bh + gap) - gap, 16 * max(len(left), len(right), 1)); y_of = {s: top + i * span / n + bh / 2 for i, (s, _, _) in enumerate(subs)}
    ys = lambda k, m: top + (span / 2 if m == 1 else (span - bh) * k / (m - 1) + bh / 2)
    out = T(L0 - 70, 20, 'Refresh first', c=BL, w='600', z=11) + T(M0 + MW / 2, 20, tname, w='600', z=11) + T(R0 + 70, 20, 'Comes back in', c=EM, w='600', z=11)
    for k, p in enumerate(left):
        y = ys(k, len(left)); out += T(L0 - 4, y + 4, f"{tname_of(p)} {p[-1].upper()}: {short[p]}", a='end', c=BL, z=10)
        for s, _, _ in subs:
            if p in needs.get(s, []): out += Ln(L0, y, M0, y_of[s], BL, 1)
    for k, t in enumerate(right):
        y = ys(k, len(right)); out += T(R0 + 4, y + 4, f"{tname_of(t)} {t[-1].upper()}: {short[t]}", a='start', c=EM, z=10)
        for p in needs[t]:
            if p in ids: out += Ln(M0 + MW, y_of[p], R0, y, EM, 1)
    for i, (s, code, nm) in enumerate(subs):
        out += box(M0, y_of[s] - bh / 2, MW, bh, f"{i + 1}. {nm} ({code})", LG, SL, SL, 10)
    return F(top + span + 12, out, f"How {name} connects: the subtopics in a suggested study order, the earlier topics to refresh first, and the later topics that use this one.", w=W)
TNAME = {}
def tname_of(sub): return TNAME.get(sub.split('-')[0], sub.split('-')[0])
